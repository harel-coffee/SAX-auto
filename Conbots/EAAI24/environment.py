import random, math, gym, sys
import numpy as np
from gym import spaces

stiffness_type = {1: (1.8, 1.8), 2: (0.6, 0.6), 3: (1.8, 0.6), 4: (0.6, 1.8)}


class EnvClass(gym.Env):
    def __init__(self, args):
        self.env_size = args.env_size
        self.action_space = spaces.Box(low=-2, high=2, shape=(2,), dtype=np.float32)
        self.observation_space = spaces.Box(low=0, high=1, shape=(6,), dtype=np.float32)
        self.action_number = 2
        self.action_size = 1
        self.observation_size = 6
        self.stiffness_type = args.stiffness_type
        self.t_spring_force, self.s_spring_force = stiffness_type[args.stiffness_type]
        self.connected = args.connected
        self.visual_noise = args.visual_noise
        self.radius = args.radius
        self.const_radius = args.const_radius
        self.noise_type = args.noise_type
        self.max_steps = args.max_steps
        self.s_location = None
        self.t_location = None
        self.step_scaler = args.step_scaler
        self.t_policy = None
        self.t_env = None
        self.target_loc = None
        self.noised_target_loc = None
        self.dist_to_prev_target_loc = None
        self.steps = 0
        self.run_number = -2
        self.args = args
        self.offset = self.offset_strategy()
        self.statistics = {'t_position': [], 's_position': [], 'target_position': [],
                           'frames': [], 'action_forces': [], 'actions': []}
        self.reset()

    def get_s_location(self):
        return self.s_location

    def get_t_location(self):
        return self.t_location

    def get_target_location(self):
        return self.target_loc

    def offset_strategy(self):
        return 3 if self.args.offset_strategy == 'constant' else random.randint(0, 10)

    def set_t_policy(self, t_policy, t_env):
        self.t_policy = t_policy
        self.t_env = t_env
        self.t_env.align_env(self.s_location, self.t_location, self.target_loc)

    def get_t_action(self):
        obs = self.get_actual_state()
        action, _ = self.t_policy.predict(obs, deterministic=True)
        return action

    def get_actual_state(self):
        return np.array([*list(self.t_location),
                         *list(self.s_location),
                         *list(self.target_loc)]) / self.env_size

    def get_noised_state(self):
        return np.array([*list(self.t_location),
                         *list(self.s_location),
                         *list(self.noised_target_loc)]) / self.env_size

    def update_noised_target_loc(self):
        if self.noise_type == 'normal':
            self.noised_target_loc = np.random.normal(self.target_loc, self.visual_noise, size=2)
        elif self.noise_type == 'uniform':
            angle = random.uniform(0, 1) * (math.pi * 2)
            if not self.const_radius:
                self.radius = random.randint(4, 17)
            x = math.cos(angle) * self.radius
            y = math.sin(angle) * self.radius
            self.noised_target_loc = np.array([x, y]) + self.target_loc
        elif self.noise_type == 'none':
            self.noised_target_loc = self.target_loc
        else:
            sys.exit('wrong noise type, please try again. options are: normal, uniform')
        self.noised_target_loc = np.clip(self.noised_target_loc, 4, self.env_size - 4).round(2)


    def reset(self, seed=None):
        """
        Resets all the env variables
        """
        self.run_number += 1
        self.steps = 0
        self.s_location = np.array([30, 30])
        self.t_location = np.array([30, 30])
        self.target_loc = np.array([31, 30])
        self.update_noised_target_loc()

        self.statistics = {'t_position': [], 's_position': [], 'target_position': [],
                           'frames': [], 'action_forces': [], 'actions': []}
        self.offset = self.offset_strategy()

        # reset teacher env
        if self.t_env is not None:
            self.t_env.reset()
            self.t_env.align_reset(self.offset, self.visual_noise)
        return self.get_noised_state()

    def update_target(self, ):
        """
        Update the targets locations
        """
        return self.update_target_shapes()

    def update_target_shapes(self):
        """
        update the target according to follow the cursor physics
        """
        time_step = (10 / 300) * self.steps + self.offset
        x_t = 3 * np.sin(1.8 * time_step) + 3.4 * np.sin(1.8 * time_step) + 2.5 * np.sin(
            1.82 * time_step) + 4.3 * np.sin(2.34 * time_step)
        y_t = 3 * np.sin(1.1 * time_step) + 3.2 * np.sin(3.6 * time_step) + 3.8 * np.sin(
            2.5 * time_step) + 4.8 * np.sin(1.48 * time_step)
        self.target_loc = np.array([x_t, y_t]) + 30
        self.target_loc = np.clip(self.target_loc, 4, self.env_size - 4).round(2)
        self.update_noised_target_loc()
        return False


    def update_locations(self, s_action, t_action):
        if self.connected == 1:
            diff_t_s = self.s_location - self.t_location
            diff_t_s = diff_t_s / 100
            diff_s_t = self.t_location - self.s_location
            diff_s_t = diff_s_t / 100

            f1 = self.t_spring_force * diff_t_s + t_action
            s_f = self.s_spring_force * diff_s_t
            f2 = (s_f + s_action) * self.step_scaler
        else:
            f1 = t_action
            f2 = s_action * self.step_scaler
            s_f = 0

        self.t_location = self.t_location + f1
        self.s_location = self.s_location + f2

        self.s_location = np.clip(self.s_location, 3, self.env_size - 3).round(2)
        self.t_location = np.clip(self.t_location, 3, self.env_size - 3).round(2)
        return s_f

    def calc_distance(self, player, force_on_student, s_action):
        if player == 'Student':
            distance = self.noised_target_loc - self.s_location
            distance = np.linalg.norm(distance)
            reached_goal = distance < 1.5
            min_dist = 1e-12
            distance = min_dist if distance <= min_dist else distance
            if self.connected == 1:
                distance += np.linalg.norm(force_on_student) * 50
        else:
            distance = np.linalg.norm(self.t_location - self.target_loc)
            distance = 1 if distance <= 1 else distance
            reached_goal = 0
        distance_reward = 1 / (distance + np.finfo(np.float).eps) + 15 * int(reached_goal)
        return distance_reward, reached_goal

    def step(self, s_action):
        """
        :param s_action: a number (0-actions_number)
        :return: new state, reward, done
        """
        self.steps += 1

        # get teacher's next step
        t_action = self.get_t_action()
        # update location for both envs (this and the teacher's)
        force_on_student = self.update_locations(s_action, t_action)
        self.t_env.align_env(self.s_location, self.t_location, self.target_loc)

        # Calculate and normalize distance
        distance_reward_s, _ = self.calc_distance('Student', force_on_student, s_action)

        # Check if the episode ended
        done_op1 = self.steps == self.max_steps

        # Update players targets
        done_op2 = self.update_target()
        done = done_op1 or done_op2
        return np.array([*list(self.t_location),
                         *list(self.s_location),
                         *list(self.noised_target_loc)]) / self.env_size, distance_reward_s, done, {}

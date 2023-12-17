import random
import numpy as np
import gym
from gym import spaces

########
##  This is a simulated environment in the case where a teacher environment is being played (loaded)
##  during learning of a student policy.
##  every update here is being manually changed by the real evironment (which is used for the student)
########

stiffness_type = {1: (1.8, 1.8), 2: (0.6, 0.6), 3: (1.8, 0.6), 4: (0.6, 1.8)}


class SimEnvClass(gym.Env):
    def __init__(self, args):
        self.env_size = args.env_size
        self.action_space = spaces.Box(low=-2, high=2, shape=(2,), dtype=np.float32)
        self.observation_space = spaces.Box(low=0, high=1, shape=(6,), dtype=np.float32)
        self.action_number, self.action_size, self.observation_size = 2, 1, 6
        self.visual_noise = args.visual_noise
        self.s_location, self.t_location, self.target_loc = None, None, None
        self.steps, self.run_number = 0, -2
        self.offset = random.randint(0, 10)
        self.reset()

    def get_state(self):
        return np.array([*list(self.t_location),
                         *list(self.s_location),
                         *list(self.target_loc)]) / self.env_size

    def reset(self, seed=None):
        """
        Resets all the env variables
        """
        self.run_number += 1
        self.target_loc = np.array([30, 30])
        self.s_location = np.array([30, 30])
        self.t_location = np.array([30, 30])
        self.steps = 0

        return self.get_state()

    def align_reset(self, offset, visual_noise):
        self.visual_noise = visual_noise
        self.offset = offset

    def align_env(self, s_location, t_location, target_loc):
        self.s_location = s_location
        self.t_location = t_location
        self.target_loc = target_loc

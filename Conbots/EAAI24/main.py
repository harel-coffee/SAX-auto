#!/usr/bin/env python -W ignore::DeprecationWarning
import os, warnings, argparse
from environment import EnvClass
from t_sim_environment import SimEnvClass
from stable_baselines3 import A2C
from stable_baselines import GAIL

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
stiff_num_to_type = {1: 'HH', 2: 'LL', 3: 'HL', 4: 'LH'}


def get_parser():
    parser = argparse.ArgumentParser(description='Framework for training a virtual teacher agent or for teaching a motor skill')

    parser.add_argument('-env_size', type=int, help='Env size', default=60)
    parser.add_argument('-connected', type=int, help='are the student and the teacher connected',
                        choices=[0, 1], default=0)
    parser.add_argument('-n_iterations', type=int, help='Number of training iterations'
                        , default=10)
    parser.add_argument('-stiffness_type', type=int, default=4, help='The force of the teacher spring', choices=[1, 2, 3, 4])
    parser.add_argument('-visual_noise', type=float, default=16, help='The visual noise magnitude')
    parser.add_argument('-max_steps', type=int, default=250, help='Number of episodes to run')
    parser.add_argument('-n_rounds', type=int, default=400, help='Number data collection rounds')
    parser.add_argument('-version', type=int, default=3)
    parser.add_argument('-teacher_stiffness', type=int,
                        help='type of teach-student interation desired to load. int 1-4', default=4, choices=[1, 2, 3, 4])
    parser.add_argument('-noise_type', type=str,
                        help='type noise to apply on the target', default='normal', choices=['normal', 'unifrom', 'none'])
    parser.add_argument('-repeats', type=int,
                        help='relevant for when training is on. How many time to repeat the process of creating 10 models?', default=1)
    parser.add_argument('-radius', type=int,
                        help='set the radius of the noise to the entire train run. only when noise_type is uniform', default=4)
    parser.add_argument('-const_radius', type=bool,
                        help='does the noise radius stays constant throughout the run?', default=True)
    parser.add_argument('-l_steps', type=int,
                        help='amount of learning steps for each game unit', default=1000)
    parser.add_argument('-eval_size', type=int,
                        help='amount of shapes or letters to evaluate the model on, at each game iteration', default=50)
    parser.add_argument('-offset_strategy', type=str,
                        help='how to deal with the target offset, options: constant, random', default='constant')
    parser.add_argument('-step_scaler', type=float,
                        help='scaler factor to be used as a way of enlarging the student step size', default=1)
    return parser


def get_updated_args():
    parser = get_parser()
    args = parser.parse_args()

    args.model_path = f'a2c_student_{args.stiffness_type}_conn_{args.connected}'
    t_dir = 'trained_teacher_models/'
    t_stiff = stiff_num_to_type[args.teacher_stiffness]
    args.teacher_policy_path = f'{t_dir}{t_stiff}_teacher.zip'
    return args


def train_student(args):
    env = EnvClass(args)
    for r in range(1, args.repeats + 1):
        # load teacher policy
        sim_env = SimEnvClass(args)
        t_policy = GAIL.load(args.teacher_policy_path)
        t_policy.set_env(sim_env)
        env.set_t_policy(t_policy, sim_env)

        model = A2C("MlpPolicy", env, verbose=0)
        for i in range(1, args.n_iterations + 1):
            print('start')
            model.learn(args.l_steps)
            model.save(args.model_path + f'_{i}_{r}.zip')


if __name__ == '__main__':
    args = get_updated_args()
    train_student(args)

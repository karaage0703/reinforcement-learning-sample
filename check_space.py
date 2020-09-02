import gym
import sys
from gym.spaces import *


def print_spaces(space):
    print(space)

    if isinstance(space, Box):
        print('min:', space.low)
        print('max:', space.high)
    if isinstance(space, Discrete):
        print('min:', 0)
        print('max:', space.n-1)


if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ('Usage: $ python ' + 'ENV_ID')
        quit()

    print(param[1])
    env = gym.make(param[1])

    print('Env ID: ', param[1])
    print_spaces(env.action_space)
    print_spaces(env.observation_space)
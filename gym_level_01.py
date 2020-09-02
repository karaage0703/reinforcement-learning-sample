import gym
env = gym.make('CartPole-v1')
env.reset()
for _ in range(1000): # run for 1000 steps
    env.render()
    action = env.action_space.sample() # pick a random action
    env.step(action) # take action
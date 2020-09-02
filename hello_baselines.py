import gym
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

env = gym.make('CartPole-v1')
env = DummyVecEnv([lambda: env])
model = PPO2('MlpPolicy', env, verbose=1)

# model.learn(total_timesteps=100000)
model.learn(total_timesteps=10000)

state = env.reset()

for i in range(2000):
    env.render()

    action, _ = model.predict(state, deterministic=True)

    state, rewards, done, info = env.step(action)

    if done:
        break

env.close()
import gym
# requires gym
# use: conda install -c powerai gym
# or
# pip install gym
# and
# pip install gym[atari]
# task =
def main():
    env = gym.make('SpaceInvaders-v0')
    env.reset()
    for i in range(1000):
            action = 1 # input int, n actions = env.action_space
            obs, reward, done, _ = env.step(action) # input action to gym, returns 4 variables
            # obs is observation - 3d rgb array
            print(f'reward: {reward}, done: {done},  _: {_} ') # f'stringtext{x}moretext' - fstring, drop var into text
            env.render()


if __name__ == '__main__':
    main()

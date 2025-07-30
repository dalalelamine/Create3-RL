from gymnasium.envs.registration import register

register(
    id="gymnasium_env/GridWorld-v0",
    entry_point="gymnasium_env.envs:GridWorldEnv",
)
register(
    id="gymnasium_env/CreateRedBall-v0",
    entry_point="gymnasium_env.envs.create_red_ball:CreateRedBall",
)

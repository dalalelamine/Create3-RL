
from setuptools import setup, find_packages

setup(
    name="gymnasium_env",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "gymnasium",
        "pygame",
        "numpy",
    ],
    entry_points={
        "gymnasium.envs": [
            "CreateRedBall-v0 = gymnasium_env.envs.create_red_ball:CreateRedBall",
            "GridWorld-v0 = gymnasium_env.envs.grid_world:GridWorldEnv",
        ]
    },
)
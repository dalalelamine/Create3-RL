import gymnasium
import gymnasium_env
import numpy as np
#from gymnasium_env.envs.create_red_ball import CreateRedBall

class NullAgent:
    """
    A null agent that takes random actions to test the environment.
    """
    
    def __init__(self, action_space):
        self.action_space = action_space
    
    def act(self, observation):
        """Return a random action from the action space."""
        return self.action_space.sample()


def test_environment():
    """Test the GridWorld environment with a null agent."""
    
    print("Testing GridWorld Environment with Null Agent")
    print("=" * 50)
    
    # Create environment
    env = gymnasium.make("gymnasium_env/CreateRedBall-v0", render_mode="human")

    # Create null agent
    agent = NullAgent(env.action_space)
    
    print(f"Observation space: {env.observation_space}")
    print(f"Action space: {env.action_space}")
    print()
    
    # Test multiple episodes
    num_episodes = 3
    max_steps_per_episode = 10
    
    for episode in range(num_episodes):
        print(f"Episode {episode + 1}")
        print("-" * 20)
        
        # Reset environment
        observation, info = env.reset()
        print(f"Initial observation: {observation}")
        print(f"Initial info: {info}")
        
        total_reward = 0
        
        for step in range(max_steps_per_episode):
            # Agent takes action
            action = agent.act(observation)
            
            # Environment steps
            observation, reward, terminated, truncated, info = env.step(action)
            
            total_reward += reward
            
            print(f"  Step {step + 1}: action={action}, obs={observation}, reward={reward}, terminated={terminated}, truncated={truncated}")
            
            # Check if episode is done
            if terminated or truncated:
                print(f"  Episode ended after {step + 1} steps")
                break
        
        print(f"  Total reward: {total_reward}")
        print()
    
    # Test observation and action spaces
    print("Testing Space Properties")
    print("-" * 25)
    
    # Test observation space
    print(f"Observation space contains 0: {0 in env.observation_space}")
    print(f"Observation space contains 5: {5 in env.observation_space}")
    print(f"Observation space contains 15: {15 in env.observation_space}")
    
    # Test action space
    print(f"Action space size: {env.action_space.n}")
    for i in range(env.action_space.n):
        print(f"Action {i} in action space: {i in env.action_space}")
    
    # Test sampling
    print("\nTesting Sampling")
    print("-" * 16)
    print("Sample observations:", [env.observation_space.sample() for _ in range(5)])
    print("Sample actions:", [env.action_space.sample() for _ in range(5)])
    
    # Test edge cases
    print("\nTesting Edge Cases")
    print("-" * 18)
    
    # Test with invalid action (should handle gracefully or raise appropriate error)
    try:
        obs, info = env.reset()
        # Try action outside valid range - this might raise an error depending on gym version
        obs, reward, term, trunc, info = env.step(999)
        print("Invalid action handled without error")
    except Exception as e:
        print(f"Invalid action raised error (expected): {type(e).__name__}: {e}")
    
    # Test render method
    print("\nTesting Render Method")
    print("-" * 20)
    result = env.render()
    print(f"Render method returned: {result}")
    
    # Close environment
    env.close()
    print("\nEnvironment closed successfully")
    print("All tests completed!")


if __name__ == "__main__":
    test_environment()

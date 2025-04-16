import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input, Concatenate
from tensorflow.keras.optimizers import Adam
import tensorflow_probability as tfp
from ..environment import Environment

class PolicyGradient:
    def __init__(
        self,
        input_dims=28,  # 14 features for current + 14 for suggested listing
        learning_rate=0.001,
        gamma=0.99  # Discount factor
    ):
        self.gamma = gamma
        self.states = []
        self.actions = []
        self.rewards = []
        self.probs = []
        self.model = self._build_policy_network()
        self.optimizer = Adam(learning_rate=learning_rate)

    def _build_policy_network(self):
        # Input layers for current listing and suggested listing
        current_listing_input = Input(shape=(14,), name='current_listing')
        suggested_listing_input = Input(shape=(14,), name='suggested_listing')

        # Process current listing
        current_x = Dense(64, activation='relu')(current_listing_input)
        current_x = Dense(32, activation='relu')(current_x)

        # Process suggested listing
        suggested_x = Dense(64, activation='relu')(suggested_listing_input)
        suggested_x = Dense(32, activation='relu')(suggested_x)

        # Combine both processed inputs
        combined = Concatenate()([current_x, suggested_x])

        # Shared layers
        x = Dense(64, activation='relu')(combined)
        x = Dense(32, activation='relu')(x)

        # Output layer - probability score for the suggested listing
        output = Dense(1, activation='sigmoid')(x)

        # Create model
        model = Model(inputs=[current_listing_input, suggested_listing_input], outputs=output)

        return model

    def choose_action(self, current_listing, available_listings):
        action_probs = []

        # Calculate score for each available listing
        for listing in available_listings:
            current = np.array(current_listing).reshape(1, 14)
            suggested = np.array(listing).reshape(1, 14)

            # Forward pass to get probability
            prob = self.model([current, suggested], training=False)
            action_probs.append(prob.numpy()[0][0])

        # Convert to probability distribution
        action_probs = np.array(action_probs)
        if np.sum(action_probs) == 0:
            action_probs = np.ones_like(action_probs) / len(action_probs)
        else:
            action_probs = action_probs / np.sum(action_probs)

        # Sample action based on probabilities
        action_idx = np.random.choice(len(available_listings), p=action_probs)

        return action_idx, action_probs[action_idx]

    def store_transition(self, state, action, action_prob, reward):
        self.states.append(state)
        self.actions.append(action)
        self.probs.append(action_prob)
        self.rewards.append(reward)

    def learn(self):
        # Convert episode history to arrays
        action_probs = tf.convert_to_tensor(self.probs, dtype=tf.float32)
        rewards = np.array(self.rewards)

        # Calculate discounted returns
        # For single-step episodes, this is just the reward
        # But the algorithm works for multi-step episodes too
        G = np.zeros_like(rewards, dtype=np.float32)
        for t in range(len(rewards)):
            G_sum = 0
            discount = 1
            for k in range(t, len(rewards)):
                G_sum += rewards[k] * discount
                discount *= self.gamma
            G[t] = G_sum

        # Normalize returns for stability
        if len(G) > 1:
            G = (G - np.mean(G)) / (np.std(G) + 1e-8)

        with tf.GradientTape() as tape:
            loss = 0
            for idx, (state, action, prob, G_t) in enumerate(
                zip(self.states, self.actions, action_probs, G)
            ):
                current = tf.convert_to_tensor([state["current_listing"]], dtype=tf.float32)
                suggested = tf.convert_to_tensor([action], dtype=tf.float32)

                # Calculate current probability
                current_prob = self.model([current, suggested], training=True)

                # Policy gradient loss
                # For a sigmoid output, we use binary cross-entropy
                # Multiply by G_t to weight by the return
                loss += -tf.math.log(current_prob) * G_t

            # Average loss over batch
            loss = loss / len(self.states)

        # Calculate gradients and apply updates
        gradients = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))

        # Clear episode history
        self.states, self.actions, self.probs, self.rewards = [], [], [], []

        return loss

# Function to train the policy gradient agent
def train_pg_agent(env, agent, episodes=1000):
    """Train Policy Gradient agent on recommendation environment"""
    total_rewards = []

    for episode in range(episodes):
        # Reset environment
        state, _ = env.reset()
        episode_reward = 0
        done = False

        # For our single-step episode
        current_listing = state["current_listing"]
        available_listings = state["available_listings"]

        # Choose action
        action_idx, action_prob = agent.choose_action(current_listing, available_listings)
        action = available_listings[action_idx]

        # Take action in environment
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        episode_reward += reward

        # Store transition
        agent.store_transition(state, action, action_prob, reward)

        # Learn at episode end
        loss = agent.learn()

        total_rewards.append(episode_reward)

        # Print progress
        if episode % 50 == 0:
            avg_reward = np.mean(total_rewards[-50:])
            print(f"Episode: {episode}, Avg Reward: {avg_reward:.2f}")

    return agent

agent = PolicyGradient()
env = Environment(listings[0], listings, column_name_to_index)
train_pg_agent(env, agent)
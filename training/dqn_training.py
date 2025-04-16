import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input, Concatenate
from tensorflow.keras.optimizers import Adam
import random
from collections import deque

class RecommendationDQN:
    def __init__(
        self,
        state_size=28,
        action_size=1,
        memory_size=10000,
        gamma=0.95,
        epsilon=1.0,
        epsilon_min=0.01,
        epsilon_decay=0.995,
        learning_rate=0.001,
        batch_size=32
    ):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=memory_size)
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.model = self._build_model()
        self.target_model = self._build_model()
        self.update_target_model()

    def _build_model(self):
        # Define the model architecture
        # Input layers for current listing and suggested listing
        current_listing_input = Input(shape=(13,), name='current_listing')
        suggested_listing_input = Input(shape=(13,), name='suggested_listing')

        # Process current listing
        current_x = Dense(32, activation='relu')(current_listing_input)
        current_x = Dense(16, activation='relu')(current_x)

        # Process suggested listing
        suggested_x = Dense(32, activation='relu')(suggested_listing_input)
        suggested_x = Dense(16, activation='relu')(suggested_x)

        # Combine both processed inputs
        combined = Concatenate()([current_x, suggested_x])

        # Fully connected layers after combination
        x = Dense(32, activation='relu')(combined)
        x = Dense(16, activation='relu')(x)

        # Output layer - a single score representing how good the suggestion is
        output = Dense(1, activation='linear')(x)

        # Create the model
        model = Model(inputs=[current_listing_input, suggested_listing_input], outputs=output)

        # Compile the model
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))

        return model

    def update_target_model(self):
        """Copy weights from model to target_model"""
        self.target_model.set_weights(self.model.get_weights())

    def remember(self, state, action, reward, next_state, done):
        """Store experience in memory"""
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state, available_listings):
        """Choose a listing to recommend"""
        if np.random.rand() <= self.epsilon:
          # Ensure the agent cannot pick the current listing
          suggested_idx = np.random.randint(low=0, high=len(available_listings) - 1)
          suggested_listing = available_listings[suggested_idx]

          while np.array_equal(suggested_listing, state):
            suggested_idx = np.random.randint(low=0, high=len(available_listings) - 1)
            suggested_listing = available_listings[suggested_idx]

          return suggested_idx

        # Format state as expected by the model
        current_listing = state.reshape(1, len(state))

        # Calculate scores for all available listings
        scores = []
        for listing in available_listings:
          # Ensure listing is different from available listings
          if not np.array_equal(listing, state):
            suggested_listing = listing.reshape(1, len(state))
            scores.append(self.model.predict([current_listing, suggested_listing], verbose=0)[0][0])
          else:
            scores.append(-np.inf)

        # Choose the listing with the highest score
        return np.argmax(scores)

    def replay(self, batch_size):
        """Train the model on experiences from memory"""
        if len(self.memory) < batch_size:
            return

        # Sample random experiences from memory
        minibatch = random.sample(self.memory, batch_size)

        for state, action, reward, next_state, done in minibatch:
            current_listing = state.reshape(1, len(state))
            suggested_listing = action.reshape(1, len(state))

            target = reward

            # Get current prediction
            current_prediction = self.model.predict([current_listing, suggested_listing], verbose=0)[0][0]

            # Create target array that's identical to current prediction except for the chosen action
            target_f = np.array([[target]])

            # Train the model
            self.model.fit([current_listing, suggested_listing], target_f, epochs=1, verbose=0)

        # Decay epsilon to reduce exploration over time
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        """Load model weights"""
        self.model.load_weights(name)
        self.update_target_model()

    def save(self, name):
        """Save model weights"""
        self.model.save_weights(name)


# Training loop
def train_dqn(env, agent, listings, episodes=1000, target_update_freq=100):
    """Train the DQN on the recommendation environment"""
    for episode in range(episodes):
        # Reset environment to get initial state
        state, _ = env.reset()

        # Since episodes are of length 1, we only need one step per episode
        # Choose action (which suggestion to make)
        action_idx = agent.act(state, listings)
        suggested_listing = listings[action_idx]

        # Take action in environment
        next_state, reward, terminated, truncated, _ = env.step(suggested_listing)
        done = terminated or truncated

        # Store experience in memory
        agent.remember(state, suggested_listing, reward, next_state, done)

        # Train the network
        agent.replay(agent.batch_size)

        # Every so often, update target network
        if episode % target_update_freq == 0:
            agent.update_target_model()

        # Print training progress
        print(f"Episode: {episode}, Reward: {reward}, Epsilon: {agent.epsilon:.2f}")

    return agent

# Create environment
env = Environment(listings, column_name_to_index)

# Create DQN agent
agent = RecommendationDQN(state_size=28, action_size=1, memory_size=100000, learning_rate=0.0001)

# Train the agent
trained_agent = train_dqn(env, agent, listings, episodes=1000)

# Save the trained model
trained_agent.save("recommendation_model.h5")
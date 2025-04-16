# Housing Platform Recommendation System

This project implements a recommendation system, based on reinforcement learning, for a housing marketplace. The problem statement is "Given that a user is currently viewing one listing, which listing in the dataset would they be most interested in viewing next. Since this recommendation system is a prototype, it is implemented using fake housing data and simulated user behaviour. The value of this exercise was learning how such a feature can be implemented in production.

# Framing the problem

Since this problem is supposed to be solved as a reinforcement learning problem, it is necessary to frame it as Markov Decision Process. Specifically,
I should identify the different states, actions and rewards that make up the environment.

## States

Each listing in the dataset is a state. A user viewing listing one is in state one.

## Actions

Each listing is also an action. Action one would mean recommending listing one.

## Rewards

T
The system uses a custom environment built with the `gymnasium` library to model the recommendation process and simulate user responses.

## Features

- **Custom Environment**: A custom environment is implemented to simulate the recommendation process, including user interactions and decision-making.
- **Dynamic Action and Observation Spaces**: The environment defines observation and action spaces based on the housing listings dataset.
- **User Behavior Simulation**: Simulates user responses to recommendations based on predefined rules and thresholds.
- **Categorical Encoding**: Encodes categorical features like `offering_type` and `property_type` for machine learning compatibility.
- **Reward System**: Implements a reward system to evaluate the effectiveness of recommendations.

## Project Structure

### 1. `environment/`

Contains the custom environment implementation.

- **`custom_env.py`**: Defines the `Environment` class, which models the recommendation system. Key methods include:
  - `reset`: Resets the environment and initializes a random current listing.
  - `step`: Processes user actions and updates the environment state.
  - `_simulate_user_response`: Simulates user decisions based on listing attributes.
  - `_get_obs`: Returns the current observation (current listing and available listings).
  - `_get_info`: Provides additional information about the environment state.

### 2. `common/`

Contains shared utilities and data.

- **`listings.py`**: Defines the housing listings dataset and preprocessing steps. Key components include:
  - `listings_data`: A list of dictionaries representing housing listings.
  - `listings_df`: A Pandas DataFrame created from `listings_data`.
  - `column_name_to_index`: A mapping of column names to their indices in the dataset, used for vectorized operations.

### 3. `README.md`

This file provides an overview of the project.

## How It Works

1. **Dataset**: The dataset consists of housing listings with attributes such as `offering_type`, `n_beds`, `price`, `latitude`, `longitude`, and `property_type`. Categorical columns are one-hot encoded for compatibility with the environment.

2. **Environment Initialization**:

   - The environment is initialized with a `current_listing` and a list of `available_listings`.
   - Observation space includes the current listing and all available listings.
   - Action space allows selecting any listing as a recommendation.

3. **User Simulation**:

   - The `_simulate_user_response` method evaluates a recommendation based on predefined rules:
     - Matching `offering_type`.
     - Number of bedrooms.
     - Price thresholds (e.g., 10-20% above the current listing price).

4. **Rewards**:

   - Positive rewards for user engagement (e.g., clicks).
   - Negative rewards for ignored recommendations.

5. **Reset and Step**:
   - The `reset` method initializes the environment with a random current listing.
   - The `step` method processes user actions, updates the state, and returns the next observation, reward, and done flag.

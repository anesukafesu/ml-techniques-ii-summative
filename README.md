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

## Environment implementation

The environment was implemented using gymnasium inside the [environment/custom_env.py](environment/custom_env.py) file. It uses simulated user behaviour to simulate how real-world users might have responded to the suggestions made by the agent.

# Agent Implementation

- Two agents were implemented, one using a DQN and the other using policy gradient methods.
- The DQN agent performed better and was used in the visualisation.

# Visualisation

There are two visualisations available–environment visualisation and the agent visualisation.

## Environment Visualisation

Here's a [link](https://drive.google.com/file/d/1nOQvjDJlaFHG_eKbr9D3C_lFdkyfbd3f/view?usp=sharing) to a video to help you visualise the environment.

## Agent visualisation

This visualisation enables you to see the DQN agent in action. The video demo is available [here](https://drive.google.com/file/d/1Rf_iI58ogCdlyxBXFubH2eamBzAWwvJe/view?usp=drive_link). You can also use a live version of the application [here](https://ml-techniques-ii-summative-git-main-anesukafesus-projects.vercel.app/).

## Project Structure

### 1. `environment/`

Contains the custom environment implementation.

### 2. `common/`

Contains shared utilities and data.

### 3. `README.md`

This file provides an overview of the project.

### 4. `models/`

Contains the models used by the DQN and policy gradient agents.

### 5. `visualisations/`

Contains code to generate the visualisations.

### 6. `training`

Contains the training code for the DQN and policy gradient agents.

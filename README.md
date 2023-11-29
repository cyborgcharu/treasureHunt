# Treasure Hunt

## **Overview:**

The Q-Learning Treasure Hunt Grid Game is a simple, yet engaging Python-based project designed to demonstrate the principles of Q-Learning, a fundamental algorithm in reinforcement learning. The game consists of a 4x4 grid where an agent moves through the grid to find a treasure. The goal is to train the agent to find the most efficient path to the treasure using Q-Learning. 

## **Key Features:**

### **1. Grid-Based Game Environment**

- A 4x4 grid where each cell can be an empty space, the agent's starting position, or the treasure location.
- Randomized positions for the starting point and treasure in each game iteration.

### **2. Agent Movement and Interaction**

- The agent can move up, down, left, or right, and cannot move outside the grid boundaries.
- Movement results in a reward or penalty, with a significant reward for finding the treasure.

### **3. Q-Learning Implementation**

- Utilization of the Q-Learning algorithm to guide the agent's movements.
- Updates to the Q-table after each move, based on the received reward and the anticipated future rewards.

### **4. Training and Learning**

- Iterative training process where the agent learns the optimal path over multiple episodes.
- Adjustable learning rate (*α*) and discount factor (*γ*) to experiment with learning efficiency.

## **Dependencies:**

### **Python Environment**

1. **Python 3.x**: The primary programming language for the project.
2. **Numpy**: For efficient numerical computations, especially for handling the Q-table.
3. **Matplotlib** (optional): For visualizing the grid and the agent's path.

## **Roadmap:**

### **1. Environment Setup**

- **Grid Initialization**: Create a 4x4 grid environment.
- **State Representation**: Define states for each cell in the grid.

### **2. Q-Learning Algorithm Development**

- **Q-Table Initialization**: Create and initialize a Q-table with dimensions corresponding to the grid size and available actions.
- **Learning Mechanism**: Implement the Q-Learning algorithm, including the update rule for Q-values.

### **3. Agent Movement Logic**

- **Action Definition**: Define possible actions (up, down, left, right) for the agent.
- **Reward System**: Implement a reward system where the agent receives feedback from the environment based on its actions.

### **4. Training Phase**

- **Episodes and Iterations**: Run multiple episodes for training the agent, with each episode consisting of a series of actions until the treasure is found or a maximum number of moves is reached.
- **Learning Parameters**: Allow for adjustment of the learning rate (*α*) and discount factor (*γ*) to observe different learning behaviors.

### **5. Evaluation and Visualization**

- **Performance Metrics**: Evaluate the agent's performance over time, such as the number of steps taken to find the treasure in each episode.
- **Path Visualization**: Use Matplotlib to visually represent the agent's path through the grid in each episode.

### **6. Experimentation and Tuning**

- **Parameter Tuning**: Experiment with different values of learning rate and discount factor to find the most efficient learning strategy.
- **Environment Variation**: Test the agent's adaptability by changing the starting point and treasure location between episodes.
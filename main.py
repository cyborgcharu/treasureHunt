import numpy as np
import matplotlib.pyplot as plt


alpha = 0.1
gamma = 0.9
epsilon = 0.25
n = 20

q_table = np.zeros((16,4))

randInt = np.random.randint(1,5, size=4)
treasure_coordinates = (randInt[0] - 1, randInt[1] - 1)
start_coordinates = (randInt[2] - 1, randInt[3] - 1)


def coordinatesToStates(coordinates):
	return coordinates[0] * 4 + coordinates[1]


def stateToCoordinates(state):
	x = state // 4
	y = state % 4
	return (x,y)


def applyActionToCoordinates(currentCoordinates, action):
	newX = currentCoordinates[0] + action[0]
	newY = currentCoordinates[1] + action[1]
	return (newX, newY)


def isOffGrid(coordinates):
	x = coordinates[0]
	y = coordinates[1]

	if (x not in range(0,4)) or (y not in range(0,4)):
		return True


def takeAction(stateX, action):
	currentCoordinates = stateToCoordinates(stateX)
	print(f"Current Coordinates: {currentCoordinates}, Action Taken: {action}")  # Debugging line

	actions = [(-1,0), (1,0), (0,-1), (0,1)]
	newCoordinates = applyActionToCoordinates(currentCoordinates, actions[action])

	if isOffGrid(newCoordinates) == True:
		print(f"New Coordinates: {newCoordinates} (Off Grid)")
		return stateX, -100, False

	if newCoordinates == treasure_coordinates:
		print(f"Found Treasure at: {newCoordinates}")
		return coordinatesToStates(newCoordinates), +100, True

	print(f"Moved to: {newCoordinates}")
	return coordinatesToStates(newCoordinates), -1, False


def updateVisualization(stateX, ax):
	ax.clear()

	data = np.arange(1,17).reshape((4,4))
	cax = ax.imshow(data, cmap='inferno')
	ax.scatter(treasure_coordinates[0], treasure_coordinates[1], c='gold', marker='X', label='Treasure')

	agentCoordinates = stateToCoordinates(stateX)
	ax.scatter(agentCoordinates[0], agentCoordinates[1], c='black', marker='.', label='Agent')

	ax.set_xticks(np.arange(4))
	ax.set_yticks(np.arange(4))
	ax.set_xticklabels(np.arange(1, 5))
	ax.set_yticklabels(np.arange(1, 5))
	ax.legend()

	plt.draw()
	plt.pause(0.1)

def learn(stateX, ax):

	stateX = coordinatesToStates(stateX)

	for episode in range(n):
		done = False

		while not done:

			print(f"Current State: {stateX}, Q-Table: {q_table[stateX]}")

			if np.random.uniform(0,1) < epsilon:
				action = np.random.choice([0,1,2,3])
			else:
				action = np.argmax(q_table[stateX])


		stateY, reward, done = takeAction(stateX, action)
		q_table[state, action] = q_table[state, action] + alpha * (reward + gamma*np.max(q_table[stateY]) - q_table[stateX, action])
		stateX = stateY

	updateVisualization(stateX, ax)


def playGame():


	data = np.arange(1,17).reshape((4,4))
	fig, ax = plt.subplots()
	cax = ax.imshow(data, cmap='inferno')

	ax.scatter(start_coordinates[0], start_coordinates[1], c='black', marker='.')
	ax.scatter(treasure_coordinates[0], treasure_coordinates[1], c='gold', marker='X', label='Treasure')


	ax.set_xticks(np.arange(4))
	ax.set_yticks(np.arange(4))
	ax.set_xticklabels(np.arange(1, 5))
	ax.set_yticklabels(np.arange(1, 5))

	ax.legend()


	learn(start_coordinates, ax)

	plt.show(block=False)


def main():
	playGame()

if __name__ == "__main__":
	main()
import numpy as np
import matplotlib.pyplot as plt


alpha = 0.1
gamma = 0.9
epsilon = 0.25
n = 20

q_table = np.zeros((16,4))


def updateVisualization(stateX):
	plt.draw()

def coordinatesToStates(coordinates):
	return coordinates[0] * 4 + coordinates[1]

def takeAction(stateX, action):
	return stateY, reward, done



def learn(stateX, callback):

	for episode in range(n):
		stateX = coordinatesToStates(stateX)
		done = False

		while not done:
			if np.random.uniform(0,1) < epsilon:
				action = np.random.choice(np.arange(1,17))
			else:
				action = np.argmax(q_table[stateX])


	stateY, reward, done = takeAction(stateX, action)
	q_table[state, action] = q_table[state, action] + alpha * (reward + gamma*np.max(q_table[stateY]) - q_table[stateX, action])

	stateX = stateY

	callback(stateX)


def playGame():

	randInt = np.random.randint(1,5, size=4)

	treasure_coordinates = (randInt[0] - 1, randInt[1] - 1)
	start_coordinates = (randInt[2] - 1, randInt[3] - 1)

	print(treasure_coordinates, start_coordinates)

	data = np.arange(1,17).reshape((4,4))
	fig, ax = plt.subplots()
	cax = ax.imshow(data, cmap='viridis')

	ax.scatter(start_coordinates[0], start_coordinates[1], c='black', marker='.', label='Start')
	ax.scatter(treasure_coordinates[0], treasure_coordinates[1], c='gold', marker='X', label='Treasure')


	ax.set_xticks(np.arange(4))
	ax.set_yticks(np.arange(4))
	ax.set_xticklabels(np.arange(1, 5))
	ax.set_yticklabels(np.arange(1, 5))

	ax.legend()


	learn(start_coordinates, updateVisualization)

	plt.show()


def main():
	playGame()

if __name__ == "__main__":
	main()
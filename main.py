import numpy as np
import matplotlib.pyplot as plt

def initializeGame():

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

	plt.show()


def main():
	initializeGame()

if __name__ == "__main__":
	main()
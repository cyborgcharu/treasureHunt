import numpy as np
import matplotlib.pyplot as plt

def initializeGame():

	randInt = np.random.randint(0,4, size=4)

	treasure_coordinates = (randInt[0], randInt[1])
	start_coordinates = (randInt[2], randInt[3])

	print(treasure_coordinates, start_coordinates)

	data = np.arange(1,17).reshape((4,4))
	fig, ax = plt.subplots()
	cax = ax.imshow(data, cmap='viridis')

	ax.set_xticks(np.arange(4))
	ax.set_yticks(np.arange(4))
	ax.set_xticklabels(np.arange(1, 5))
	ax.set_yticklabels(np.arange(1, 5))

	plt.show()


def main():
	initializeGame()

if __name__ == "__main__":
	main()
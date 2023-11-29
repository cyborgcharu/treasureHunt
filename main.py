import numpy as np
import matplotlib

def initializeGame():
	"""Generates random coordinates for treasure and agent start

	Returns
	-------
	treasure_coordinates: 
		tuple of treasure x, y location

	start_coordinates:
		tuple of agent start x, y location
	"""

	randInt = np.random.randint(0,4, size=4)

	treasure_coordinates = (randInt[0], randInt[1])
	start_coordinates = (randInt[2], randInt[3])

	print(treasure_coordinates, start_coordinates)


def main():
	initializeGame()

if __name__ == "__main__":
	main()
def tower_of_hanoi(height, start, finish, aux):
    if height >= 1: # when height is 0, that allows us to use the step function
        tower_of_hanoi(height-1, start, aux, finish)  # moving n-1 disks to intermediary tower
        print("Moving from", start, "to", finish)
        tower_of_hanoi(height-1, aux, finish, start) # moving those n-1 disks to the final place

# showing what step is now taken
def step(start, finish):
    print("Moving from", start, "to", finish)

def main():
	tower_of_hanoi(3, "START", "FINISH", "AUX")

if __name__ == "__main__":
	main()

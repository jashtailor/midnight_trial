import random

def generate_random_list():
    random_list = random.sample(range(1, 101), 10)
    return random_list

def run_at_midnight():
    # Generate a random list of 10 integers
    random_list = generate_random_list()

    # Print the list
    print("Random List at Midnight:", random_list)

if __name__ == "__main__":
    run_at_midnight()

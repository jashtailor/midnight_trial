import random
import os

def generate_random_list():
    return random.sample(range(1, 101), 10)

def save_list_to_txt_file(version, random_list):
    filename = f"v{version}.txt"
    with open(filename, "w") as file:
        for item in random_list:
            file.write(str(item) + "\n")

def run_at_midnight(version):
    # Generate a random list of 10 integers
    random_list = generate_random_list()

    # Save the list to a TXT file
    save_list_to_txt_file(version, random_list)

    # Print the list (optional)
    print(f"Random List for v{version}:", random_list)

if __name__ == "__main__":
    # Get the current version by counting the existing TXT files
    version = 1
    while os.path.exists(f"v{version}.txt"):
        version += 1
    
    run_at_midnight(version)

import ao_core as ao
import math
import numpy as np
from arch__tester import arch

list_of_all_combs = []
for i in range(20):
    for j in range(20):
        for k in range(20):
            list_of_all_combs.append([i,j,k])

agent = ao.Agent(arch)
for i in range(4):
    agent.reset_state()
    agent.reset_state(training=True)

num_binary_digits = 5

def get_binary(id):
    bucket_binary = np.array(list(np.binary_repr(id, num_binary_digits)), dtype=int)
    return bucket_binary.tolist()

def distance_calculation(genre_id, theme_id, comp_title_id):
    max_distance = -1
    furthest_comb = None

    for comb in list_of_all_combs:
        x, y, z = comb
        # Calculate Euclidean distance
        distance = math.sqrt((x - genre_id) ** 2 + (y - theme_id) ** 2 + (z - comp_title_id) ** 2)
        
        # Track the furthest combination
        if distance > max_distance:
            max_distance = distance
            furthest_comb = comb

    return furthest_comb

#Main loop
while True:

    # Get user input
    genre_id = int(input("Genre ID: "))
    theme_id = int(input("Theme ID: "))
    comp_title_id = int(input("Comp Title ID: "))

    #convert inputs to binary
    genre_binary = get_binary(genre_id)
    theme_binary = get_binary(theme_id)
    comp_title_binary = get_binary(comp_title_id)

    #combine inputs for the agent
    input_to_agent = genre_binary + theme_binary + comp_title_binary
    agent.next_state(input_to_agent, print_result=True)
    recommendation_result = input("Did you like the recommendation (y/n)? ")

    opposite_array = distance_calculation(genre_id, theme_id, comp_title_id)
    

    if recommendation_result.lower() == "y":
        label = [1] 
    else:
        label = [0]
    agent.next_state(input_to_agent, LABEL=label, print_result=True)

    
    print("Opposite array:", opposite_array) 
    agent.next_state(input_to_agent, LABEL = [0], print_result = True)

    if input("Continue? (y/n): ").lower() == "n":
        break


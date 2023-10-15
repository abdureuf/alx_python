def best_score(a_dictionary):
    # Initialize variables to keep track of the best score and key
    best_key = None
    best_value = float("-inf")

    # Iterate over each key-value pair in the dictionary
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            # Check if the current value is greater than the best value
            if value > best_value:
                # Update the best value and key
                best_value = value
                best_key = key

    # Return the key with the best score
    return best_key
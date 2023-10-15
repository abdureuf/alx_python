def update_dictionary(a_dictionary, key, value):
    # Update the value if the key already exists
    if key in a_dictionary:
        a_dictionary[key] = value
    # Add a new key/value pair if the key doesn't exist
    else:
        a_dictionary[key] = value

    # Return the updated dictionary
    return a_dictionary
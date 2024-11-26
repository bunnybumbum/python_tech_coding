def flatten_dict(d, parent_key = '', sep = '.'):
    if not isinstance(d, dict):
        raise TypeError("Input must be a dictionary")
    flattened = {}
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key, sep))
        else:
            flattened[new_key] = value
    return flattened

if __name__ == "__main__":
    # Example usage:
    nested_dict = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3,
                'f': 4
            }
        },
        'g': {
            'h': 5
        }
    }

    flattened = flatten_dict(nested_dict)
    print(flattened)
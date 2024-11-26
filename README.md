Flatten Nested Dictionary
This project contains a Python solution for flattening a nested dictionary into a single-level dictionary, as described in the technical assesment.

Task Description: Implement a function flatten_dict(d) that takes a nested dictionary d and returns a new dictionary with all nested keys flattened into a single level. The keys in the flattened dictionary should represent the path to each value in the original dictionary, joined by dots (.).

Constraints:
- All keys are strings.
- Values can be integers, strings, or other dictionaries.
- Assume there are no lists or other data types in the values.

Solution Description
The solution invloves a recursive approach to traverse the nested dictionary and build a flattened version using a separator to concatenate keys.

Key Features:
- Recursive Traversal: Handles nested dictionaries of any depth.
- Customizable Separator: Allows specifying a different separator for joining keys.
- Error Handling : Validates input to ensure it is a dictionary.
- Edge Cases: Handles emplty dictionaries and special characters in keys.
import json

# Load the data from the JSON file
with open ('../functional_programs/ClassEval_GPT3_5.json') as f:
    data = json.load(f)


# Initialize an empty list to store task_ids
methods_with_lib_dependencies_GPT = []

# Iterate over the tasks in data
for task in data:
    for method in task['methods_info']:
    # Check if the task has at least one method with a third-party dependency
        if method['dependencies']['lib_dependencies']:
        # If it does, append its task_id to the list
            methods_with_lib_dependencies_GPT.append(method)

print(methods_with_lib_dependencies_GPT)
print(f"Number of methods with library dependencies in ClassEval_GPT3_5: {len(methods_with_lib_dependencies_GPT)}")
import json

# Load the JSON data
with open('../data/ClassEval_data.json') as f:
    data = json.load(f)


# with open ('../')
# Filter tasks with library dependencies
tasks_with_lib_dependencies = [task for task in data if any(method['dependencies']['lib_dependencies'] for method in task['methods_info'])]
#wizard_with_lib_dependencies = 
print(f"Number of tasks with at least one method of library dependency in ClassEval.data: {len(tasks_with_lib_dependencies)}")

# Print the names of the tasks with library dependencies 

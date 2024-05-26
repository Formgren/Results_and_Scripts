import json

# Load the JSON data
with open('../data/ClassEval_data.json') as f:
    classeval_data = json.load(f)


# with open ('../')
# Filter tasks with library dependencies
tasks_with_lib_dependencies = [task for task in classeval_data if any(method['dependencies']['lib_dependencies'] for method in task['methods_info'])]
#wizard_with_lib_dependencies = 
print(f"Number of tasks with at least one method of library dependency in ClassEval.data: {len(tasks_with_lib_dependencies)}")

with open ('../functional_programs/ClassEval_GPT3_5.json') as f:
    data = json.load(f)


# Initialize an empty list to store task_ids
task_ids_with_lib_dependencies_GPT = []

# Iterate over the tasks in data
for task in data:
    # Check if the task has at least one method with a third-party dependency
    if any(method['dependencies']['lib_dependencies'] for method in task['methods_info']):
        # If it does, append its task_id to the list
        task_ids_with_lib_dependencies_GPT.append(task['task_id'])

print(task_ids_with_lib_dependencies_GPT)

with open ('../functional_programs/ClassEval_wizardcoder.json') as f:
    data2 = json.load(f)


# Initialize an empty list to store task_ids
task_ids_with_lib_dependencies_wiz = []

# Iterate over the tasks in data
for task in data2:
    # Check if the task has at least one method with a third-party dependency
    if any(method['dependencies']['lib_dependencies'] for method in task['methods_info']):
        # If it does, append its task_id to the list
        task_ids_with_lib_dependencies_wiz.append(task['task_id'])

print(task_ids_with_lib_dependencies_wiz)
import json


def library_methods():
    # This method extract methods that have a library dependency
    with open ('../functional_programs/ClassEval_GPT3_5.json') as f:
        data = json.load(f)
    with open ('../functional_programs/ClassEval_wizardcoder.json') as f:
        data2 = json.load(f)

    # Initialize an empty list to store task_ids
    methods_with_lib_dependencies_GPT = []
    methods_with_lib_dependencies_wizard = []

    # Iterate over the tasks in data
    for task in data:
        for method in task['methods_info']:
        # Check if the task has at least one method with a lib dependency
            if method['dependencies']['lib_dependencies']:
            # If it does, append it to the list
                methods_with_lib_dependencies_GPT.append(method)
                print(method['method_name'])
    print('****')
    for task in data2:
        for method in task['methods_info']:
        # Check if the task has at least one method with a lib dependency
            if method['dependencies']['lib_dependencies']:
            # If it does, append it to the list
                methods_with_lib_dependencies_wizard.append(method)
                print(method['method_name'])


    print(f"Number of methods with library dependencies in ClassEval_GPT: {len(methods_with_lib_dependencies_GPT)}")
    print(f"Number of methods with library dependencies in ClassEval_wizardcoder: {len(methods_with_lib_dependencies_wizard)}")
    

def standalone_methods():
    # This method extract all succesfult methods that have a standalone dependency
     # Load the data from the JSON file
    with open ('../functional_programs/ClassEval_GPT3_5.json') as f:
        data = json.load(f)

    with open ('../functional_programs/ClassEval_wizardcoder.json') as f:
        data2 = json.load(f)

    # Initialize an empty list to store task_ids
    standalone_methods_GPT = []
    standalone_methods_wizardcoder = []

    # Iterate over the tasks in data
    for task in data:
        for method in task['methods_info']:
        # Check if the task has at least one method with a third-party dependency
            if method['dependencies']['Standalone']:
            # If it does, append its task_id to the list
                standalone_methods_GPT.append(method)
                print(method['method_name'])
    print('****')
    for task in data2:
        for method in task['methods_info']:
        # Check if the task has at least one method with a third-party dependency
            if method['dependencies']['Standalone']:
            # If it does, append its task_id to the list
                standalone_methods_wizardcoder.append(method)
                print(method['method_name'])
    print('****')
    #print(methods_with_lib_dependencies_GPT)
    print(f"Number of completed standalone methods in ClassEval_GPT: {len(standalone_methods_GPT)}")
    print(f"Number of completed standalone methods in ClassEval_wizardcoder: {len(standalone_methods_wizardcoder)}")

def fields():
        # This method extract methods that have a field dependency
    with open ('../functional_programs/ClassEval_GPT3_5.json') as f:
        data = json.load(f)
    with open ('../functional_programs/ClassEval_wizardcoder.json') as f:
        data2 = json.load(f)

    # Initialize an empty list to store task_ids
    methods_with_field_dependencies_GPT = []
    methods_with_field_dependencies_wizard = []

    # Iterate over the tasks in data
    for task in data:
        for method in task['methods_info']:
            if method['dependencies']['field_dependencies']:
                methods_with_field_dependencies_GPT.append(method)
                # If it does, append its task_id to the list
                methods_with_field_dependencies_GPT.append(method)
                print(method['method_name'])
    print('****')
    for task in data2:
        for method in task['methods_info']:
            if method['dependencies']['field_dependencies']:
                methods_with_field_dependencies_wizard.append(method)
                # If it does, append its task_id to the list
                methods_with_field_dependencies_wizard.append(method)
                print(method['method_name'])
    print('****')
    #print(methods_with_lib_dependencies_GPT)
    print(f"Number of completed field methods in ClassEval_GPT: {len(methods_with_field_dependencies_GPT)}")
    print(f"Number of completed field methods in ClassEval_wizardcoder: {len(methods_with_field_dependencies_wizard)}")


def methods_dep():
        # This method extract methods that have a field dependency
    with open ('../functional_programs/ClassEval_GPT3_5.json') as f:
        data = json.load(f)
    with open ('../functional_programs/ClassEval_wizardcoder.json') as f:
        data2 = json.load(f)

    # Initialize an empty list to store task_ids
    methods_with_method_dependencies_GPT = []
    methods_with_method_dependencies_wizard = []

    # Iterate over the tasks in data
    for task in data:
        for method in task['methods_info']:
            if method['dependencies']['method_dependencies']:
                methods_with_method_dependencies_GPT.append(method)
                # If it does, append its task_id to the list
                methods_with_method_dependencies_GPT.append(method)
                print(method['method_name'])
    print('****')
    for task in data2:
        for method in task['methods_info']:
            if method['dependencies']['method_dependencies']:
                methods_with_method_dependencies_wizard.append(method)
                # If it does, append its task_id to the list
                methods_with_method_dependencies_wizard.append(method)
                print(method['method_name'])
    print('****')
    #print(methods_with_lib_dependencies_GPT)
    print(f"Number of completed method dependent methods in ClassEval_GPT: {len(methods_with_method_dependencies_GPT)}")
    print(f"Number of completed method dependent methods in ClassEval_wizardcoder: {len(methods_with_method_dependencies_wizard)}")



standalone_methods()
library_methods()
fields()
methods_dep()
import json
import re

def extract_passed_programs():
    programs_filepath = '/Users/mac/Desktop/KTH/TIDAB3/Exjobb/Resultat/ClassEval/model_output/ClassEval_wizardcoder_greedy.json'
    results_filepath ='/Users/mac/Desktop/KTH/TIDAB3/Exjobb/Resultat/ClassEval/evals/ClassEval_wizardcoder_greedy.json'
    output_filename = 'passed_programs.json'
    # Load the programs and the test file
    with open(programs_filepath, 'r') as f:
        programs = json.load(f)
    with open(results_filepath, 'r') as f:
        results = json.load(f)

    # Extract the programs that passed all the tests
    i = 0
    passed_programs = []
    print("name of program file:")

    programs_filename = programs_filepath.split('/model_output/')[1].split('.json')[0]
    print(programs_filename)

    for task_id in results[programs_filename]:
        #print(task_id)
        #print(type(task_id))
        if results[programs_filename][task_id]['TestClass']['class_success'] > 0:
            i += 1
            print(task_id)
            # strip the string of ClassEval_ and only taske the number
            task_number = int(re.search(r'\d+', task_id).group())
            passed_programs.append(programs[task_number])
            
        # print(programs[task_number]['predict'])
    print(f"Number of succesful classes:", i)

    with open(output_filename, 'w') as f:
        json.dump(passed_programs, f)

extract_passed_programs()
# extract_passed_programs(file_path_programs, file_path_results, output_file)
import csv
import subprocess
import json
import re

def test_code_snippet(code):
    with open('temp.py', 'w') as f:
        f.write(code)
    subprocess.run(['flake8', '--max-complexity', '1','temp.py', '--extend-ignore', 'E302,E305,E303,E231,E225,E291,E501'], encoding='utf-8')
    print('************************************')
        # subprocess.run(['flake8', '--max-complexity', '1','temp.py', '--extend-ignore', 'E501'], encoding='utf-8')
    #subprocess.run(
    #    [ 'flake8', 'temp.py'],
    #    encoding='utf-8',
    #)
    #if result.stdout:
    #    print(result.stdout)
    #if result.stderr:
    #    print(result.stderr)

def postprocess_markdown(response):
    pattern = r'```python\s+(.*?)```'
    code_snippet = re.search(pattern, response, re.DOTALL).group(1)
    return code_snippet


with open('../functional_programs/ClassEval_wizardcoder.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    predict = data[i]['predict']
    for j in range(len(predict)):
        code = postprocess_markdown(predict[j])
        # print(code)
        test_code_snippet(code)
    

    




#pattern_list = [r"```python(.*?)```", r"```ruby(.*?)```", r"```scss(.*?)```",
#    r"```python(.*?)", r"```(.*?)```", r"\[PYTHON\](.*?)\[/PYTHON\]"] 
#i = 0

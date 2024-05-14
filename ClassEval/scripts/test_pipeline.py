import csv
import subprocess
import json
import re

def test_code_snippet(code):
    with open('temp.py', 'w') as f:
        f.write(code)
    result = subprocess.run(['pycodestyle', '--statistics', '-qq', 'temp.py'], stdout=subprocess.PIPE)
    print(result.stdout)

def postprocess_markdown(response):
    pattern = r'```python\s+(.*?)```'
    code_snippet = re.search(pattern, response, re.DOTALL).group(1)
    return code_snippet


with open('../functional_programs/ClassEval_GPT3_5.json', 'r') as f:
    data = json.load(f)

for i in range(len(data)):
    predict = data[i]['predict']
    code = postprocess_markdown(predict[0])
    # print(code)
    test_code_snippet(code)
    break

    




#pattern_list = [r"```python(.*?)```", r"```ruby(.*?)```", r"```scss(.*?)```",
#    r"```python(.*?)", r"```(.*?)```", r"\[PYTHON\](.*?)\[/PYTHON\]"] 
#i = 0

import requests
import random
import json

# Get the math problem dataset from the internet
url = 'https://raw.githubusercontent.com/openai/grade-school-math/master/grade_school_math/data/train.jsonl'
response = requests.get(url)
content = response.content.decode('utf-8')

# Each problem in the response content is on a separate line, split on newline into problems list
problems = content.split('\n')

# Make new list which stores each problem with its index/ID from the original list
# This will help us find the answer to the problem later
problems_with_ids = []
for index, problem in enumerate(problems):
    problems_with_ids.append((index, problem))

# Problems are in fixed order, so let's randomize the order to get new problems each time
random.shuffle(problems_with_ids)

# From the random ordering, slice the first 10 problems into a new list
first_10_problems = problems_with_ids[:10]

# Print the first 10 problems
for index, problem_data in first_10_problems:
    dictionary = json.loads(problem_data)
    print(f"Problem {index}: {dictionary['question']}\n")
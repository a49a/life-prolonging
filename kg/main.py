from random import choice
import toml

with open('./food.toml', 'r') as f:
    toml_string = f.read()

parsed_toml = toml.loads(toml_string)
vegetables = []
for x in parsed_toml['vegetables']:
    vegetables.append(x)

print(choice(vegetables))
# %%
import requests as req
import json

response = req.get('https://pokeapi.co/api/v2/pokemon/ditto')

print(f'Status code: {response.status_code}')
print(f'{response.text}')

data = json.loads(response.text)
print(data)
print(type(response))
print(type(data))

peso = 0

for key, value in data.items():
    if key == 'weight':
        peso = float(value)

print(peso)
# %%

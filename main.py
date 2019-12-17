import json
import pykeen


with open('configuration.json', 'r') as config_file:
    config = json.load(config_file)



results = pykeen.run(
    config=config,
    output_directory='output'
)

print('Keys:', *sorted(results.results.keys()), sep='\n ')

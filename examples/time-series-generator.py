import os
from pathlib import Path
import json
from generator.generator import TimeSeriesGenerator


dirname = Path(__file__)
dirname = dirname.parent

# Load config
config_file = os.path.join(dirname, "representation_learning_experiment.json")

with open(config_file) as file:
    configuration = json.load(file)

# Generate time series
for time_serie_config in configuration["time_series"]:
    generator = TimeSeriesGenerator(time_serie_config["meta"])
    generator.generate(time_serie_config)
    generator.save(time_serie_config)



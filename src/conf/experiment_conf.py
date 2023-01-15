from dataclasses import dataclass
from pathlib import Path
import yaml


@dataclass
class ExperimentConf:
    name: str
    conf_path: None
    dataset: str = "data/example.csv"
    output_dir: str = "runs"

    def __init__(self, config_file):
        self.conf_path = config_file
        with open(config_file, 'r') as f:
            params = yaml.safe_load(f)
            self.__dict__.update(params)


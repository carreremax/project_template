from dataclasses import dataclass
import yaml


@dataclass
class ExperimentConf:
    conf_path: str = None
    name: str = "Experiment example"
    dataset: str = "data/example.csv"
    output_dir: str = "runs"

    def __init__(self, config_file=None):
        self.conf_path = config_file
        if self.conf_path is not None:
            with open(config_file, 'r') as f:
                params = yaml.safe_load(f)
                self.__dict__.update(params)

import os
from pathlib import Path
import pandas as pd
from datetime import datetime
from conf.experiment_conf import ExperimentConf
from dataclasses import asdict
import yaml


class ExperimentWriter:
    def __init__(self, conf: ExperimentConf) -> None:
        self.experiment = conf
        self.records = []
        os.makedirs(self.experiment.output_dir, exist_ok=True)

    def add_record(self, name: str, record: pd.DataFrame) -> None:
        self.records.append({"name": name, "content": record})

    def export(self) -> None:
        run_name = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{self.experiment.name}"
        run_dir = Path(self.experiment.output_dir) / run_name
        os.makedirs(run_dir)
        with open(run_dir / (self.experiment.name + ".yml"), 'w') as f:
            yaml.dump(asdict(self.experiment), f, default_flow_style=False)
        for record in self.records:
            record_name = record["name"]
            record["content"].to_csv(run_dir / f"{record_name}.csv", index=False)

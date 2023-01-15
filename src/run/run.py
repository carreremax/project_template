import argparse
import pandas as pd
from pathlib import Path
from conf.experiment_conf import ExperimentConf
from output.experiment_writer import ExperimentWriter


def run(conf: ExperimentConf):
    """
    Example of a run from an experiment configuration

    :param conf: Experiment parameters and configuration
    :type conf: ExperimentConf
    :return:
    """
    print(conf)
    writer = ExperimentWriter(conf)
    writer.add_record("examples_perfs", pd.DataFrame())
    writer.export()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Example run script',
        description='Example of importing a configuration')
    parser.add_argument('filename', default="conf/experiment_example.yml")
    args = parser.parse_args()

    config = ExperimentConf(args.filename)
    run(config)

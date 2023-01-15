# project_template

A nice description of your new project



# Setup:
You can install the specific version of the packages needed for this project through conda:

    conda env create -f env.yml -p ./env

Alternatively, if you only want the required packages, without their specific versions (in case they are 
not available for your hardware or os for example):
    
    conda env create -f env_simplified.yml -p ./env

Then activate your newly created environment :
    
    conda activate ./env

Mark the project source directory (./src) as source root, or 
manually add it to your Pythonpath.

## Launch
Every script and notebook should be used with the project root directory
(the directory where this Readme is) as the working directory, as every path
used is relative to the project root directory.

- Example:

  
    python src/run/example.py conf/example.yml

- Example for notebooks:

  
    jupyter notebook 
Then go to ./notebook and launch the one you want.

## Project structure

- ./conf : configuration files for experiments, models, pipeline parameters, ...
- ./doc : documentation : code documentation, experiment report, eventual presentations
- ./data : dataset(s), both provided and eventual preprocessed export
- ./models : trained models used or exported
- ./notebooks : main directory for project notebooks
- ./runs : experiment exported files and results
- ./src : code directory


## Code Documentation
At MVP stage, with Sphinx in ./doc, 

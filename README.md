# Example Project: Fuel Consumption Data Analysis

This project template demonstrates/highlights: setting up an anaconda environment, working with local raw data, building a neural network model, analysing the model through jupyter notebook.

This project illustrates structuring a DS project that approaches the
very simple task of analysing the correlation between different aspects 
of a car (engine_size, number of cylinders) with its fuel consumption. 
The project explores the implementation of a very simple neural network that tries to predict the fuel consumption of a car from its engine_size and number of cylinders (a.k.a regression task). While the quality of the approach to building a model is not set to a high
of a car (engine_size, number of cylinders) with its fuel consumption.


The project explores the implementation of a very simple neural network that tries to predict the fuel consumption of a car from its engine_size and number of cylinders. While the quality of the approach to building a model is not set to a high standard, the code is just non-trivial enough to illustrate how to
handle making a DS project rerunnable and easy to navigate.



## Retrieving the data locally:

(1) To download the data, we will use !wget to download it from IBM Object Storage.
`!wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv§` 

* This will download the data and cast it in a .csv file locally (remember the path for the next step)

(2) Edit the file: _config/data-params.json_ to include the location of the data in the value of the _outdir_ key



## Running the project

* This project assumes data is stored locally in .csv file
* To setup the environment using conda: `conda env create -f environment.yml`
This will create an environment called dsc180A (the first line of the .yml sets the env name).

  
### Building the project stages using `run.py`

* To get the data, from the project root dir, run `python run.py data
  features`
  - This fetches the data, then creates features (defined in
    `src/features.py`) and saves them in the location specified in
    `features-params.json`.
* To get the data, from the project root dir, run `python run.py data
  features model`
  - This fetches the data, creates the features, then trains a model
    (with parameters specified in `config`). It writes both the
    prediction from the model for analysis and pickles the model using
    `joblib`.

  




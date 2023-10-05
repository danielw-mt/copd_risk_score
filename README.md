# COPD Offline Risk Score

This repository contains 6 self-explained notebooks for the different analyses performed during this thesis. 
They should be executed in the following order to ensure reproducibility of the results:

1. ./harvard/harvard_data_cleaning.ipynb
This notebook is used for data cleaning and pre-processing of the Harvard data set. 

2. ./triage/triage_eda_data_cleaning.ipynb
This notebook is used for data cleaning and pre-processing of the Triage data set.

3. ./cross_dataset_validation/feature_engineering.ipynb
This notebook is used to extract additionally overlapping features for both data sets. 

4. ./cross_dataset_validation/feature_analysis.ipynb
This notebook is used to perform bivariate and multivariate analysis before harmonization. Statistical sensitivity analysis and generation of descriptive statistics is also performed.

5. ./cross_dataset_validation/model_development.ipynb
This notebook is used to develop reference models specifically optimized for each data set

6. ./cross_dataset_validation/generalizable_model.ipynb
This notebook is used to perform data set harmonization and to examine the transfer of models from one data set to the other

Further information:
* The original data files can be found in the "./harvard/data/Original Data" or "./triage/data" folders respectively
* An overview over the different open source models we investigated is contained in ./Dataset Overview.xlsx
* The original papers for each data set can be found in the "./harvard/data/Original Data" and "./triage" folders
* the "results" folders contain plots and results of our analyses



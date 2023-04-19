# Anesthesia Monitor
This is a new integrated visual display prototype for the monitoring of vital signs in anesthesia

The project was coded in Python using Visual Studio Code (VSC).

## monitor.py

The main file is monitor.py. To run it in VSC you first have to load the virtual environment with the following command:

*source studysession/bin/activate*

Then the program can be run as a web app using streamlit:

*streamlit run monitor.py*

## preprocessing.py

The second file preprocessing allows to preprocess the file test_data.csv which was originally downloaded from the VitalDB database https://vitaldb.net. It was the file used to run the program during development. Once preprocessed it is saved under the name preprocessed_data.csv and can be read with the monitor.

## scenarios

Four scenarios were created (fake data) to test the display against standard monitoring. Each scenario in its .csv form is available and can be run on the monitor by changing the name of the file in line 20.

Scenario 1: Malignant hyperthermia

Scenario 2: Anaphylactic shock

Scenario 3: Awareness

Scenario 4: Bronchospasm

![Model](https://github.com/MelSup/anesthesia_monitor/blob/main/monitor.png)

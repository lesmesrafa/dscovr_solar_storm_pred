# Solar Storm DSCOVR Prediction

<p align="center">
  <a href="https://docs.python.org/3.10/">
  <img alt="Python version" src="https://img.shields.io/badge/python-3.10-blue?&logo=python">
  </a>
  <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit" alt="pre-commit" style="max-width:100%;"></a>
  <a href="https://github.com/astral-sh/ruff">
  <img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json?style=for-the-badge">
  </a>
  <a href="https://mypy-lang.org/">
  <img alt="Checked with mypy" src="https://www.mypy-lang.org/static/mypy_badge.svg">
  </a>
  <a href="https://github.com/psf/black">
  <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
  <a href="https://jupyterbook.org">
  <img alt="Documentation with jupyterbook" src="https://raw.githubusercontent.com/executablebooks/jupyter-book/master/docs/images/badge.svg">
  </a>
</p>


## Overview

When operating reliably, the **National Oceanic and Atmospheric Administration's (NOAA's) space weather station, the Deep Space Climate Observatory (DSCOVR)📡🛰️**, can measure the strength and speed of the solar wind in space. This capability is crucial for predicting geomagnetic storms that can severely impact critical systems like **GPS🌐** and **electrical power grids on Earth⚡**. DSCOVR, however, continues to operate beyond its expected lifetime⌛, leading to occasional faults. Interestingly, these faults may themselves serve as indicators of space weather.

The objective🎯 of this project is to utilize the "raw" data from DSCOVR, specifically the faults, and to predict🔮 geomagnetic storms on Earth🌍.


## Background

[![Explanation](https://i.ytimg.com/vi/cdwJ6gqR0AM/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgYSgyMA8=&rs=AOn4CLC0eTxVhDCHVrrX2c14k74eqdZ9-A&quot)](https://youtu.be/m_pDSJive-E)

The Carrington Event of 1859 was perhaps the most intense solar event of the century. During this event, a series of powerful coronal mass ejections hit Earth head-on. The resulting effects were observed worldwide and observations of glowing night sky auroras were recorded globally, including near the equator. This space weather event caused geomagnetically induced currents in long stretches of the telegraph transmission lines that were common in that day, generating enough current for the lines to operate without batteries. Some telegraph stations even caught fire from the induced currents. There were no high voltage (HV) electrical power transmission lines back then, so fortunately, the impact of the Carrington Event on global safety and economics was minor.

***Geomagnetic storms*** on Earth ***are a menace to many modern technologies***, particularly GPS satellite systems and electrical power grids. These storms occur when strong gusts of wind or storms from the Sun traverse interplanetary space and reach Earth, deforming Earth's magnetic field and showering particles into Earth's magnetic poles. ***These storms are notoriously difficult to predict.*** Even when solar flares and eruptions are observed that may cause a geomagnetic storm, the travel time for material to reach Earth could be anywhere from about two to four days (or it could miss Earth entirely).

NOAA’s space weather station, the ***Deep Space Climate Observatory*** (DSCOVR), orbits about a million miles from Earth in a unique ***location*** called Lagrange point 1, which basically allows it to hover ***between the Sun and our planet***. From that vantage point, DSCOVR measures the plasma that may cause geomagnetic storms hours before it reaches us, ideally providing an early warning of what’s coming our way. The time that it takes for that plasma to reach Earth and trigger a geomagnetic storm might be anywhere from about 15 minutes to a few hours.

NOAA uses measurements of the solar wind density, temperature, speed, and magnetic field to run computer simulations of the Earth's magnetic field and atmosphere. Based on those simulations, NOAA forecasts when a geomagnetic storm will occur and how strong it will be. ***The strength of the geomagnetic storm is measured on a scale called the Planetary K-index (Kp).***

The DSCOVR mission, which was initially planned for five years, is now in its eighth year. Although the instrument onboard DSCOVR that measures the solar wind's magnetic field continues to function very well, the ***instrument*** that measures the solar ***wind density, temperature, and speed has lost sensitivity and experiences faults*** and anomalies from time to time. These faults are unpredictable and can even be difficult to catch in real time, making them particularly troublesome when they occur during events that may cause storms. To make matters more urgent, the Sun is nearing the peak activity phase of its 11-year cycle; these storms are more frequent now than at any point in DSCOVR's mission.


## Objectives

Your challenge is to develop a machine learning (ML) algorithm or neural network pipeline for the DSCOVR spacecraft's FC instrument to track and follow the changes in the peak solar wind speed so that DSCOVR can continue to provide early warnings of the next potential Carrington-like event that could adversely impact life and property on Earth. You can access historical solar wind data from DSCOVR and other missions to use to train your ML algorithm to correctly detect and track these solar wind peaks.


## Potential Considerations

You may (but are not required to) consider the following when creating your solution:

- What is Currently Measured by DSCOVR:\
The DSCOVR Faraday Cup is the instrument that provides the solar wind density, speed, and temperature used by NOAA to run its forecast models. NOAA refers to the densities, speeds, and temperatures as "level 2" data. These quantities are not measured directly, however; the instrument actually measures the entire spectra of solar wind particles over time and then computes those quantities from the spectra. These spectral data are referred to as "level 1" data, or sometimes as "raw" data.

- DSCOVR Anomalies:\
To work well, a space science experiment must be stable and well-calibrated to translate the "raw" data into the more useful "level 2" data. DSCOVR no longer meets this criteria; in its old age, certain electrical anomalies and faults have been observed that shift the calibration and introduce noisy signals in unpredictable ways into DSCOVR raw data. When these faults occur, NOAA generally attempts to identify them and switches to a backup weather station rather than attempting to recalibrate or mitigate the error to produce the level 2 data accurately.

- One possible approach to solve this challenge:\
There are many ways to approach this problem. In particular, one powerful method has become widely accessible only in the last few years: machine learning regression. This challenge is a natural application for an adaptive neural network (ANN).

In a machine learning regression, experimental data is fed to a system of linear operations, or network, with adjustable weights. Those weights are adjusted, or "trained" to produce outputs that mimic the provided ground truth. Once trained, the network can be applied to future experimental data to produce predictions.

In this case, the experimental data are the DSCOVR raw data, though it is left for you to decide how you will use this data (for example, does one point in time have predictive power? Ten points? An hour?).

The ground truth could be any number of desirable indicators– there are no rules here! It could be the Planetary K-index (Kp) or some other measure of geomagnetic activity at a particular point in time (though some thought would have to be given to the timing). It could be a classification– "a severe Kp>6 storm will occur within 2 hours." It could be a prediction for whether Dubliners will witness the aurora borealis in the next 24 hours. What will you use as ground truth? Check out the records of various geomagnetic activity indices in the Resources section for ideas.

There are a number of open-source software packages available that you can search for on the internet (particularly in Python) that provide the tools for a non-expert to perform optimized ANN training.

- Consider the timing of your predictions. Predicting when may be as challenging as predicting what.
- Some data sets will contain gaps, as most experiments do not run uninterrupted for years at a time!
- You may need to account for 'filled' data. These are data that are set to some very unusual value meant to be unmistakable for real measurements—often such data are a special value like NaN (not a number).

As you develop your designs, you may (but are not required to) consider the following:

- [Read a notional DSCOVR Faraday Cup instrument “calibration” and data analysis procedure.](https://www-2022.spaceappschallenge.org/space-apps-challenge-2022-example-resource-save-the-earth-from-another-carrington-event/)

For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

NASA does not endorse any non-U.S. Government entity and is not responsible for information contained on non-U.S. Government websites. For non-U.S. Government websites, participants must comply with any data use parameters of that specific website.
## Data

[What is DSCOVR?](https://solarsystem.nasa.gov/missions/DSCOVR/in-depth/)

- Geospace Observatory (GO) Canada:
  -   [Open data and information Portal (asc-csa.gc.ca)](https://donnees-data.asc-csa.gc.ca/en/dataset/0176458c-553b-48b4-a5e2-492022c81e85)
  -   The GO Canada initiative is a project that brings together a variety of space weather (including solar wind) research tools and infrastructure. This network of ground-based instruments (more than 120 as of June 2019) that monitor space weather over Canada's North collects geospatial data, conducts scientific research, and turns scientific knowledge into applications that benefit Canadians. These data could be used to help validate the DSCOVR dataset.
- [CARISMA Magnetometer Network](https://donnees-data.asc-csa.gc.ca/dataset/06f5e364-6e2c-4d1c-95c2-9fb7d871ca20)
  - The Canadian Array for Realtime Investigations of Magnetic Activity (CARISMA) project is a series of ground-based sensors that detect disturbances in the Earth's magnetosphere (often related to solar winds). It could be useful for validating the DSCVR dataset. Please note that it is considered part of the GO Canada suite of projects, but it is being specifically mentioned here due to its pertinence to this challenge.
- [Canadian Solar Flux Archive (F10.7)](https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-en.php)
  -  Data from the Canadian solar flux archive could help you validate the data and your results from the DSCVR mission.
- [CASSIOPE](https://donnees-data.asc-csa.gc.ca/dataset/98466021-2q1w-5g2d-677zwru214wx68)
  -  The Canadian CASSIOPE satellite, operated by the University of Calgary, carries the Enhanced Polar Outflow Probe (e-POP) suite of scientific instruments to study the ionosphere, where space meets the upper atmosphere. The instruments collect data about the effects of solar storms and, more specifically, their harmful impact on radio communications, satellite navigation, and other space and ground-based technologies. This dataset could help you validate the DSCVR data.
- NOAA Space Weather Prediction Center:
  -  [Real Time Solar Wind](https://www.swpc.noaa.gov/products/real-time-solar-wind)
  -  [Geospace Magnetosphere Movies](https://www.swpc.noaa.gov/products/geospace-magnetosphere-movies)
  -  [3D Geomagnetic Forecast](https://www.swpc.noaa.gov/products/3-day-geomagnetic-forecast)
  -  [Planetary K Index](https://www.swpc.noaa.gov/products/planetary-k-index)
- [Experimental Data Repository](https://www.spaceappschallenge.org/develop-the-oracle-of-dscovr-experimental-data-repository/)
  -  A description of the data set and some very brief quick-start tutorial material for loading and inspecting the data in Python will be provided.
- [Records of various geomagnetic activity indices](https://hpde.io/NASA/NumericalData/OMNI/PT1H)
  -  Working demonstration for reading the DSCOVR experimental data.

- NASA Resources
  - [Earth Observing Dashboard](https://eodashboard.org/) \
The Earth Observing Dashboard showcases examples of global environmental changes for 7 themes: Atmosphere, Water and Ocean, Biomass, Cryosphere, Agriculture, Covid-19, and Economy. You can explore countries and regions around the world to see how the indicators in specific locations changed over time.
  - [The Wind Mission’s Magnetic Field Data Sets, BW(t)](https://cdaweb.gsfc.nasa.gov/pub/data/wind/mfi/mfi_h2/2022/) 
 

```https://cdaweb.gsfc.nasa.gov/pub/data/wind/mfi/mfi_h2/2022/```

To obtain BW(t) data for other years, replace the “2022” in the above URL with the desired year (e.g., 2021, 2020).

Tips on How to Open/Read a CDF File:
These instructions serve to cover the basics of how to open and read data saved in the cdf format. This will assume you have the following packages installed in your python environment:
```
cdflib
spacepy
matplotlib
numpy
wget
```
  - Install CDF library
CDF library version 3.8 can be downloaded here: CDF library version 3.8 can be downloaded here:
https://spdf.gsfc.nasa.gov/pub/software/cdf/dist/cdf38_0/
For Windows, it is suggested you use the InstallMate installer to automatically set paths. For MacOS, the universal installer is probably easiest.
Another option is to use
https://pypi.org/project/cdflib/
which can be installed without having to first install and configure the CDF software from NASA above.

   - Install python packages to read CDF
The two python packages we will use here to read CDF files are the pycdf package found within the spacepy toolset, and cdflib. These can be installed easily using pip, and possible conda (depending on your version of python). Depending on how you have your environment set up, it should be as simple as:
pip install cdflib
pip install spacepy


Open a cdf file
>from spacepy import pycdf

>cdf_pycdf = pycdf.CDF(whateverfilename.cdf)

Example Inspection
>print('These are the variables within this file:\n')

>print(cdf_pycdf)

>print('This is the global metadata record of the file:\n')

>print(cdf_pycdf.attrs)


## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://docs.kedro.org/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:


```
python -m piptools compile --upgrade --resolver backtracking -o src/requirements.lock src/requirements.txt -v
```
```
pip install -r src/requirements.lock
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.


## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project
You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#cell-tags) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Note:* The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.



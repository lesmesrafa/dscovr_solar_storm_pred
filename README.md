# Classification of Solar Flares using Machine Learning Techniques 

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

This project is centered around the study and prediction of solar flares. Solar flares are highly energetic solar events that pose a significant threat to a wide array of electronic systems that are integral to modern society, including satellites 🛰️ and communication networks 📡.

The primary goal 🎯 of this project is to harness machine learning techniques to analyze and interpret data from the Space-weather HMI Active Region Patches (SHARP), combining data of magnetic field properties and flaring activity. The capability to predict solar flares is of immense importance, as these phenomena can severely impact critical infrastructures and systems, such as GPS navigation 🌐 and electrical power grids on Earth ⚡.

Through sophisticated data analysis and machine learning models, this project aims to differentiate and classify the various types of solar flares. This will not only contribute to a deeper understanding of solar flare mechanisms but also aid in the development of early warning systems to mitigate the potential risks associated with these powerful solar events.

## Introduction

Solar flares can produce streams of highly energetic particles able to reach the Earth's magnetosphere in minutes which can affect negatively the electric components in the satellites or, in the most extreme cases, knock out the electrical power grids, which can cause a huge socio-economical issue.

This work focuses on the development of an unsupervised machine learning algorithm for the classification of solar active regions and their relationship with the flaring events and the intensity of these events. The data used is based on the SHARP parameters extracted from SDO HMI samples of the magnetic field active regions. The use of unsupervised algorithms is explained as they can extract information and get patterns that are unknown to human experts. 

## Active Regions vs Solar Flares

Solar active regions are zones on the Sun atmosphere where the magnetic activity temporally increases and, therefore, the magnetic field in this area is complex and thousand times stronger than the average. This solar active regions are common during the peak of the solar cycle.

[![Solar Active Region](https://upload.wikimedia.org/wikipedia/commons/4/47/Solar_Archipelago_-_Flickr_-_NASA_Goddard_Photo_and_Video.jpg)](https://en.wikipedia.org/wiki/File:Growing_Sunspots_Tracking_Closeup_-_February_2011.ogv)


The solar flares are a sudden and bright small areas of the Sun that can last minutes to a few hours and they occur in the corona when magnetic field lines of opposite polarity are forced together, causing a sudden transformation of magnetic energy into kinetic and thermal energy (aka magnetic reconnection).

Flares are classified according to the strength of their X-ray emission, recorded by the GOES satellites in geostationary orbit. There is 5 types of intensity and they increase exponentially the magnitude: A, B, C, M and X, being the X-type ones the least frequent as they are the most intense and dangerous ones. In the other hand weak solar flares are frequent what produces an imbalance in the data.

[![Solar Flare](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/X_Class_Solar_Flare_Sends_%E2%80%98Shockwaves%E2%80%99_on_The_Sun_%286819094556%29.jpg/1920px-X_Class_Solar_Flare_Sends_%E2%80%98Shockwaves%E2%80%99_on_The_Sun_%286819094556%29.jpg)](https://en.wikipedia.org/wiki/File:SDO_EVE_Late_Phase_Flares.webm)


## Data set

The data set contains data extracted from the Space Weather HMI Active Region Patch series (SHARP), integrated with information from solar flare catalogs. The data is derived from the Helioseismic and Magnetic Imager (HMI) from the solar Dynamics Observatory (SDO). 

Click [here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EBCFKM) to download the data set.


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



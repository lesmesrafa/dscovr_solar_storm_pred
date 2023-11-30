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
https://youtu.be/cdwJ6gqR0AM

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



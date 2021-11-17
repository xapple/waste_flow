[![PyPI version](https://badge.fury.io/py/waste_flow.svg)](https://badge.fury.io/py/waste_flow)
![Pytest passing](https://github.com/xapple/waste_flow/actions/workflows/pytest_master_branch.yml/badge.svg)

# `waste_flow` version 1.3.1

`waste_flow` is a python package for retrieving and analyzing data concerning the waste management of European countries.

<p align="center">
<img height="200" src="waste_flow/reports/template/logo.png?raw=true">
</p>

## Installing

Since `waste_flow` is written in python it is compatible with all operating systems: Linux, macOS and Windows. The only prerequisite is python version 3.6 or above which is often installed by default. Simply choose one of the two following methods to install, depending on which package manager you prefer to use.

### Installing via `conda`

    $ conda install -c conda-forge -c xapple waste_flow

### Installing via `pip`

    $ python3 -m pip install --user waste_flow

### Troubleshooting

* If you do not have `conda` on your system you can refer to [this section](docs/installing_tips.md#installing-python-with-conda).
* If you do not have `pip3` on your system you can refer to [this section](docs/installing_tips.md#obtaining-pip3).
* If you do not have `python3` on your system or have an outdated version, you can refer to [this other section](docs/installing_tips.md#obtaining-python3).
* If none of the above has enabled you to install `waste_flow`, please open an issue on [the bug tracker](https://github.com/xapple/waste_flow/issues) and we will get back to you shortly.

## Usage

Bellow are some examples to illustrate the various ways there are to use this package.

To retrieve the large dataframe with dry mass for all years and all countries you can do the following from your python interpreter:

    >>> from waste_flow.analysis import waste_ana
    >>> print(waste_ana.dry_mass)

If you just want to see how much rubber waste did the UK generate in 2008, you can do the following:

    >>> from waste_flow.generation import waste_gen
    >>> params = ("waste   == 'W073' & "
    >>>           "country == 'UK' & "
    >>>           "year    == '2008'")
    >>> result = waste_gen.long_format.query(params)
    >>> print(result)

To create the waste generation plots do the following:

    >>> from waste_flow.viz.gen_by_country import legend
    >>> print(legend.plot(rerun=True))
    >>> from waste_flow.viz.gen_by_country import countries
    >>> for gen_viz in countries.values():
    >>>     print(gen_viz.plot(rerun=True))

## Cache

When you import `waste_flow`, we will check the `$WASTE_FLOW_CACHE` environment variable to see where to download and store the cached data. If this variable is not set, we will default to the platform's temporary directory and clone a repository there. This could result in re-downloading the cache after every reboot.

## Features

The first time you run `waste_flow`, it will automatically download the raw CSVs from the EUROSTAT website to disk and parse the resulting data. On later runs, `waste_flow` will simply retrieve this information directly from the disk. This means that the first time you execute the pipeline things will be noticeably slower: this is normal.

## Source

The two datasets used in this pipeline are available at the following addresses:

* https://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=env_wasgen&lang=en

* https://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=env_wastrt&lang=en

These are obtained by starting at https://ec.europa.eu/eurostat/data/database and following "Database by themes -> Environment -> Waste -> Waste treatment"

The full name of the datasets are:

* Generation of waste by waste category, hazardousness and NACE Rev. 2 activity (`env_wasgen`).
* Treatment of waste by waste category, hazardousness and waste management operations (`env_wastrt`).

## Customizing

The pipeline is flexible as the user can specify what coefficients they desire or even what custom waste categories they want to create. These input parameters are in the files under the `waste_flow/extra_data_xls` directory.

## Visualizations

The `waste_flow` package can also generate several types of plots that enable the user to compare and visualize the data.

For instance here is a series of graphs comparing the total reported waste generated in wet tonnes between European countries for the *nace* category `C20-C22`.

##### "Manufacture of chemical, pharmaceutical, rubber and plastic products"

![Waste generated graph part 1](docs/showcase_graphs/AT_BA_BE_BG.svg?sanitize=true "Waste generated graph part 1")
![Waste generated graph part 2](docs/showcase_graphs/CY_CZ_DE_DK.svg?sanitize=true "Waste generated graph part 2")
![Waste generated graph part 3](docs/showcase_graphs/EE_EL_ES_EU27_2020.svg?sanitize=true "Waste generated graph part 3")
![Waste generated graph part 4](docs/showcase_graphs/EU28_FI_FR_HR.svg?sanitize=true "Waste generated graph part 4")
![Waste generated graph part 5](docs/showcase_graphs/HU_IE_IS_IT.svg?sanitize=true "Waste generated graph part 5")
![Waste generated graph part 6](docs/showcase_graphs/LI_LT_LU_LV.svg?sanitize=true "Waste generated graph part 6")
![Waste generated graph part 7](docs/showcase_graphs/ME_MK_MT_NL.svg?sanitize=true "Waste generated graph part 7")
![Waste generated graph part 8](docs/showcase_graphs/NO_PL_PT_RO.svg?sanitize=true "Waste generated graph part 8")
![Waste generated graph part 9](docs/showcase_graphs/RS_SE_SI_SK.svg?sanitize=true "Waste generated graph part 9")

<p align="center">
<img height="200" src="docs/showcase_graphs/legend.svg?sanitize=true">
</p>

### Distributing the package

* Instructions for distributing and uploading `waste_flow` on PyPI so that it can be installed by `pip` can [be found here](https://packaging.python.org/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi). The current uploaded version is [listed here](https://pypi.org/project/waste_flow/).

* Instructions for distributing and uploading `waste_flow` on anaconda so that it can be installed by `conda` can [be found here](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html). The current uploaded version is [listed here](https://anaconda.org/xapple/waste_flow).

Two scripts that automate these processes can be found in the following repository:

https://github.com/xapple/bumphub

### Developer documentation

The internal documentation of the `waste_flow` python package is available at:

http://xapple.github.io/waste_flow/waste_flow

This documentation is simply generated from the source code with this command:

    $ pdoc3 --html --output-dir docs --force waste_flow

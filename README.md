# `waste_flow` version 1.0.0

`waste_flow` is a python package for retrieving data concerning the waste management of European countries.

## Installing

`forest_puller` is a python package and hence is compatible with all operating systems: Linux, macOS and Windows. The only prerequisite is python3 which is often installed by default. Simply type the following on your terminal:

    $ pip3 install --user waste_flow

Or if you want to install it for all users of the system:

    $ sudo pip3 install waste_flow

If you do not have `pip` on your system you can usually get it with these commands (fresh Ubuntu 18-LTS):

    sudo apt-get update
    sudo apt-get install python3-distutils
    curl -O https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py --user

## Usage

For instance to retrieve the XYZ can do the following:

```python
# Import #
from waste_flow import countries

# Get the country #
austria = countries['AT']

# Get the 2017 indexed dataframe #
at_2017 = austria.years[2017].indexed

# Print some data #
print(at_2017.loc['xxx', 'yyy']['zzz'])
```

     904282.4970403439

To see what information is available you can of course display the column titles and row indexes of that data frame:

```python
print(at_2017.columns)
print(at_2017.index)
```

To examine what countries and what years are available:

```python
print(list(c.iso2_code for c in countries.values()))
print(list(y for y in austria.years))
```

To get a large data frame with all years and all countries inside:

```python
from forest_puller.ipcc.concat import df
print(df)
```

## Cache

When you import `waste_flow`, we will check the `$WASTE_FLOW_CACHE` environment variable to see where to download and store the cached data. If this variable is not set, we will default to the platform's temporary directory and clone a repository there. This could result in re-downloading the cache after every reboot.
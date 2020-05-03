# `waste_flow` version 1.0.5

`waste_flow` is a python package for retrieving data concerning the waste management of European countries.

<p align="center">
<img height="200" src="waste_flow/reports/template/logo.png?raw=true">
</p>

## Installing

`waste_flow` is a python package and hence is compatible with all operating systems: Linux, macOS and Windows. The only prerequisite is python3 which is often installed by default. Simply type the following on your terminal:

    $ pip3 install --user waste_flow

Or if you want to install it for all users of the system:

    $ sudo pip3 install waste_flow

If you do not have `pip` on your system you can usually get it with these commands (fresh Ubuntu 18-LTS):

    $ sudo apt-get update
    $ sudo apt-get install python3-distutils
    $ curl -O https://bootstrap.pypa.io/get-pip.py
    $ python3 get-pip.py --user

## Usage

Here are some examples to use the pacakge.

To retrieve the large dataframe with dry mass for all years and all countries you can do the following:

    from waste_flow.generation import waste_gen
    print(waste_gen.dry_mass)

If you just want to see how much rubber waste did the UK generate in 2008, you can do the following:

    from waste_flow.generation import waste_gen
    params = ("waste   == 'W073' & "
              "country == 'UK' & "
              "year    == '2008'")
    result = waste_gen.dry_long.query(params) 
    print(result)

To generate the waste generation plots do the following:


## Cache

When you import `waste_flow`, we will check the `$WASTE_FLOW_CACHE` environment variable to see where to download and store the cached data. If this variable is not set, we will default to the platform's temporary directory and clone a repository there. This could result in re-downloading the cache after every reboot.
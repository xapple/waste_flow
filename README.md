# `waste_flow` version 1.1.7

`waste_flow` is a python package for retrieving and analyzing data concerning the waste management of European countries.

<p align="center">
<img height="200" src="waste_flow/reports/template/logo.png?raw=true">
</p>

## Installing

Since `waste_flow` is written in python it is compatible with all operating systems: Linux, macOS and Windows. The only prerequisite is python3 which is often installed by default. Simply type the following commands on your terminal:

    $ pip3 install --user waste_flow

Alternatively if you want to install it for all users of the system:

    $ sudo pip3 install waste_flow

If you do not have `pip` on your system you can usually get it with these commands (fresh Ubuntu 18-LTS):

    $ sudo apt-get update
    $ sudo apt-get install python3-distutils
    $ curl -O https://bootstrap.pypa.io/get-pip.py
    $ python3 get-pip.py --user

## Usage

Bellow are some examples to illustrate the various ways there are to use this package.

To retrieve the large dataframe with dry mass for all years and all countries you can do the following:

    from waste_flow.analysis import waste_ana
    print(waste_ana.dry_mass)

If you just want to see how much rubber waste did the UK generate in 2008, you can do the following:

    from waste_flow.generation import waste_gen
    params = ("waste   == 'W073' & "
              "country == 'UK' & "
              "year    == '2008'")
    result = waste_gen.long_format.query(params)
    print(result)

To create the waste generation plots do the following:

    from waste_flow.viz.gen_by_country import legend
    print(legend.plot(rerun=True))
    from waste_flow.viz.gen_by_country import countries
    for gen_viz in countries.values():
        print(gen_viz.plot(rerun=True))

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

* Generation of waste by waste category, hazardousness and NACE Rev. 2 activity (env_wasgen)                                  
* Treatment of waste by waste category, hazardousness and waste management operations (env_wastrt)

## Customizing

The pipeline is flexible as the user can specify what coefficients they desire or even what custom waste categories they want to create. These input parameters are in the files under the `waste_flow/extra_data_xls` directory.

## Visualizations

The `waste_flow` package can also generate several types of plots that enable the user to compare and visualize the data.

For instance here is a series of graphs comparing the total reported waste generated in wet tonnes between european countries for the nace category `C20-C22`. 

##### "Manufacture of chemical, pharmaceutical, rubber and plastic products"

![Waste generated graph part 1](showcase/AT_BA_BE_BG.svg?sanitize=true "Waste generated graph part 1")
![Waste generated graph part 2](showcase/CY_CZ_DE_DK.svg?sanitize=true "Waste generated graph part 2")
![Waste generated graph part 3](showcase/EE_EL_ES_EU27_2020.svg?sanitize=true "Waste generated graph part 3")
![Waste generated graph part 4](showcase/EU28_FI_FR_HR.svg?sanitize=true "Waste generated graph part 4")
![Waste generated graph part 5](showcase/HU_IE_IS_IT.svg?sanitize=true "Waste generated graph part 5")
![Waste generated graph part 6](showcase/LI_LT_LU_LV.svg?sanitize=true "Waste generated graph part 6")
![Waste generated graph part 7](showcase/ME_MK_MT_NL.svg?sanitize=true "Waste generated graph part 7")
![Waste generated graph part 8](showcase/NO_PL_PT_RO.svg?sanitize=true "Waste generated graph part 8")
![Waste generated graph part 9](showcase/RS_SE_SI_SK.svg?sanitize=true "Waste generated graph part 9")
![Waste generated graph legend](showcase/legend.svg?sanitize=true "Waste generated graph legend")

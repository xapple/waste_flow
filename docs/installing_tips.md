## Obtaining `python3`

Most modern operating systems, with the exception of Windows, come with `python3` pre-installed.

If you are using Windows, you can try [the chocolatey method](https://lmgtfy.com/?q=install+python3+on+windows+with+chocolatey).

Otherwise, if you are using an old version of macOS that doesn't ship with the latest python, you can simply run the following command after installing [homebrew](https://brew.sh/):

    $ brew install python@3.9

Finally, if you are using an old version of Linux that doesn't have a very recent python, you can install your own version of python in your home directory without administrator privileges.

To do this there are two possible roads. Go with `conda` or go with `pyenv`. See below for more information.


## Installing python with `conda`

To install miniconda, follow these instructions:

https://conda.io/projects/conda/en/latest/user-guide/install/index.html

If you are using Linux this boils down to downloading an `.sh` file and running it.

Then you follow the interactive instructions on the terminal. Once the installation is finished, you relaunch the shell. Finally, you can create a new environment called `myenv` by typing the following command:

    $ conda create -n myenv python=3.9

To activate this environment, type:

    $ conda activate myenv

You should now be using the latest version of python.

To check the version of python simply type:

    $ python3 -V


## Installing python with `pyenv`

This project enables you to install your own python version in your home directory: https://github.com/yyuu/pyenv

To install it you may use this sister project: https://github.com/yyuu/pyenv-installer

Basically you just need to type this command:

    $ curl https://pyenv.run | bash

Then these lines go into your ``.bash_profile``:

    $ vim ~/.bash_profile

        export PATH="$HOME/.pyenv/bin:$PATH"
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)"

Finally, relaunch your shell for changes to take effect and type these commands to get the right version of python:

    $ pyenv install 3.9.5
    $ pyenv global 3.9.5
    $ pyenv rehash


## Obtaining `pip3`

If you are using a recent Ubuntu operating system and are an administrator of the computer, the following commands should install `pip3` onto your computer:

    $ sudo apt-get update
    $ sudo apt-get install python3-pip

Otherwise, if that didn't work, you can attempt this more generic method that works with a wider range of configurations and doesn't require the sudo command. Use the `get-pip` script like so:

    $ curl -O https://bootstrap.pypa.io/get-pip.py
    $ python3 get-pip.py --user

If you still did not succeed, check that you have the following required package installed before running the `get-pip` script again:

    $ sudo apt-get update
    $ sudo apt-get install python3-distutils

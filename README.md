# Based on https://nadiah.org/2020/03/01/example-debug-mixed-python-c-in-visual-studio-code/

# Key differences
Difference 1. I use conda not virtualenv and Python 3.11 not 3.6 So I do 
`conda create -n [MYENVNAME] python=3.11` and `conda activate nadia` instead of `virtualenv --python=python3.6 myadd`


Dif 1.5 
Extension compiled w -g0 


Difference 2. 
When you get to `python3 setup.py install` I will get an error:
```
/Users/grace_ibm/miniconda3/envs/nadia/lib/python3.11/site-packages/setuptools/_distutils/cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` directly.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.

        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
        ********************************************************************************
```
To fix, do not run `setup.py` directly. Instead add `pyproject.toml` which has requirements and build info. Put the following in your `pyproject.toml`:
```
[build-system]
requires = ["setuptools", "wheel", "pybind11~=2.11.1"]
build-backend = "setuptools.build_meta"
```
Then run ` pip install .` to install instead of `python3 setup.py install`

Now `python myscript.py` should work fine to produce 11. 

Difference 3
I will use my conda environment in VS Code: https://stackoverflow.com/questions/66869413/visual-studio-code-does-not-detect-virtual-environments

I will not look at my `settings.json`


Difference 4 
debugpy
conda prefix
While setting up my launch.json, I will go into the terminal (with the conda env activated) and run `echo $CONDA_PREFIX` to get the prefix for my python path. Example output: /bob/     which I add too       "program": "${workspaceRoot}/bin/python", /* My virtual env */. There is possibly a way to use string interpolation here too but I don't know it. 


# vscode-docker-playground

# AIHAO
## Anthony's personal AI assistant


## Presequisite:
*please note that currently this library is only compatible with macosX*

*make sure `pyobjc-core==9.0.1`*

*after do pip freeze > requirements.txt delete all the pyobjc-framework\* entries to avoid package conflict*

## Setup
`cd ./config`

`./setup.sh`

* After this go to your project settings and add the python interpreter to be your virtual env and the virtual env will 
* be sourced everytime a new terminal is open (this is only applicable to pycharm).

## Publish release using Github CLI
`gh release create --repo seanh/gha-python-packaging-demo --title "First release!" --notes "This is the first release!" 0.0.1`
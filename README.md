# AIHAO
## Anthony's personal AI assistant


## Presequisite:
*make sure `pyobjc-core==9.0.1`*

*after do pip freeze > requirements.txt delete all the pyobjc-framework\* entries to avoid package conflict*

## Setup
`cd ./config`

`./setup.sh`


## Publish release using Github CLI
`gh release create --repo seanh/gha-python-packaging-demo --title "First release!" --notes "This is the first release!" 0.0.1`
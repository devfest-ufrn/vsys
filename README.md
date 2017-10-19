# vsys
A System to automate the process of rent a vehicle
By vehicle we mean cars, trucks, bycicles, boats, etc.


Getting Started
---------------

- Install virtualenv

- Create new env
 
 	$ virtualenv env

- Enter env

	$ source env/bin/activate

- Change directory into your newly created project.

    (env) $ cd vsys

- Upgrade packaging tools.

    (env) $ pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    (env) $ pip install -e ".[testing]"

- Run your project's tests.

    (env) $ pytest

- Run your project.

    (env) $ pserve development.ini

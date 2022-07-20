# DevNet intro scripts

When you see a box that looks like this:

```
Terminal command here
```
You will copy this text and paste it into the terminal. 
For Linux:

### Copy - CTRL+INSERT
### Paste - SHIFT+INSERT

Clone the repo

```
git clone https://github.com/oborys/DevNet-intro-scripts.git
```

Work with Python:

```
cd DevNet-intro-scripts
```

### Setup virtualenvironment

**Install the virtualenv package**

The virtualenv package is required to create virtual environments. You can install it with pip:
```
pip install virtualenv
```
**Create the virtual environment**

To create a virtual environment, you must specify a path. For example to create one in the local directory called `py3-venv`, type the following:
```
python3 -m venv py3-venv
```

**"Activate" the environment**

Mac OS / Linux
```
source py3-venv/bin/activate
```

Windows
```
py3-venv\Scripts\activate
```

**Install packages (list of packages in file `requirements.txt`) into the current python environment**
```
pip install -r requirements.txt 
```

**Run script**

```
python simple_api_operation_http_errors.py
```

**Deactivate the virtual environment**

To decativate the virtual environment and use your original Python environment, simply type `deactivate`.

```
deactivate
```

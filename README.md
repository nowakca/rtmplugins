# rtmplugins

Depends on https://github.com/slackapi/python-rtmbot

## Environment setup

### Install Homebrew
_From https://brew.sh/_

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Install python3
_From https://programwithus.com/learn-to-code/install-python3-mac/_

```
brew install python3
python3 -m pip install --user virtualenv
```

### Get the source code in place

```
git clone https://github.com/nowakca/rtmplugins.git
```

This will make your rtpmplugins directory.

### Prep the virtual environment
```
cd rtmplugins
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
open rtmplugins.code-workspace
```

This will create your virtual environment, and since it's in your project folder (where you're VSCode workspace is, VSCode will autodetect the workspace. Click the python version on the bottom left corner to select the 'env' virtual environment)

## running it (from the project directory)

```
./runner.py
```

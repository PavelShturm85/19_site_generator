# Encyclopedia

**The module make sites from markdown files**

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

*Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.*

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quickstart
**Ways to use:**
- Have to use  module `site_generator.py` after `python3`.
  - This is create site in path `/site`
  - After make change in `template.html` or `/articles/`,site auto recreate.


Example of script launch on Linux, Python 3.5:


```bash
$ python3 site_generator.py
[I 171225 19:38:27 server:283] Serving on http://127.0.0.1:5500
[I 171225 19:38:27 handlers:60] Start watching changes
[I 171225 19:38:27 handlers:62] Start detecting changes

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

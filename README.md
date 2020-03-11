# A Voice based email system for visually challenged

## Installation

* [Download and install Miniconda](http://conda.pydata.org/miniconda.html) Choose the Python 3.x version for your 
platform.

* Open a Terminal (Linux/macOS) or Command Prompt (Windows) and run the following commands (One Time):
```
$ conda update conda
$ conda install git
$ git clone https://github.com/namanchikara/Voice-based-email-system-for-visually-challenged.git
$ cd Voice-Based-Email-For-Blind
$ conda env create -f conda_env.yml
```

* Commands to run every time you want to run the program from the cloned directory:
```
$ conda activate voicemail
(voicemail)$ python voicemail/__init__.py 
```

* You can run command `conda env list` to check location of env, and if you want env in custom directory then you can 
run `conda env create --prefix <Directory Path> -f conda_env.yml`
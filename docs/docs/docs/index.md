# Vicmil-pip

vicmil-pip is a package manager for installing things, much like pip in python
(but with other things such as utility files and other things that may not be related to python)

# Getting started

## Step 1:

Create a new file called vicmil-pip.py

## Step 2:

Paste in the following code and run it

```
# install latest version of vicmil-pip in this file
import urllib.request
with urllib.request.urlopen('https://raw.githubusercontent.com/vicmil-pip/vicmil-pip/refs/heads/main/vicmil-pip.py') as f:
    html = f.read().decode('utf-8')
    with open(__file__, "w") as this_file:
        this_file.write(html)
```

## Step 3

Get help using the following command

```
python3 vicmil-pip.py help
```

You can for example install packages using

```
python3 vicmil-pip.py install some_packagename
```

You can find a list of available packages using

```
python3 vicmil-pip.py packages
```

# More details

When you install something, a map called vicmil_pip/ will be created, where all packages
you install will be stored under vicmil_pip/packages. Nothing external will be installed on
your computer.

The idea is for all the packages to be cross-platform(windows, linux, mac), so the thing
that actually gets installed may vary depending on platform. The idea is for all packages
to use a permissive licence, so they can be used in commercial applications.

You can also opt-out of using vicmil-pip but still use the packages by navigating to
the package you want to install, found under packages and then install it manually.
It should work the same, but may be more work to get up and running. In most cases,
you can just extract the repo and put it under vicmil_pip/packages/<package name\>.
Some packages may also have a setup.py script you need to run and require that you
install other packages, listed under requirements.

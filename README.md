# Lilite: A Linux Package Auto-installer

[https://www.lilite.co](https://www.lilite.co)

[![Build Status](https://travis-ci.org/cmoscardi/lilite.svg?branch=master)](https://travis-ci.org/cmoscardi/lilite)

## Supported Linux versions

- Ubuntu 16.04
- Ubuntu 14.04

If you're interested in building out support for another distro,
let me know! Some of the infra for distro-specific install methods is WIP.

## Contributing

To contribute, you just need to do two things:

1. Add the instructions on how to install a package
2. Add in the logo

Package definitions live in [packages/packages.json](https://github.com/cmoscardi/lilite/tree/master/packages). Logos live in [static/images](https://github.com/cmoscardi/lilite/tree/master/static/images)

### To add a new package

1. Make a new entry in `packages/packages.json`. There are three important fields:

    - `pre_install` : List of shell commands to run before installing the package.
    - `package_name` : Name of the package manager's package. This can be empty
                   if you're using a .deb file, for example.
    - `post_install` : List of shell commands to run after the package is installed
                   via package manager.

2. Add two copies of the logo - one "large" (i.e. original size) and one 48x48, PNG format - into static/images

### To test and debug locally

If you'd like to ensure everything is working before you send in a PR, then you can also set up a local environment to test.
1. `pip install -r requirements.txt` - This installs the required dependencies
2. Checkout the respective git branch
3. `python packages/seed_packages.py` - This will seed/prepare a local database
4. `python app.py` - will start the local server and you should see your package here
5. Select the linux version, select your package and click on install package. You'll see command to install it which looks somthing like this
`sudo apt-get install curl; curl 'http://127.0.0.1:5000/get_installer?version=ubuntu_16&packages=<PACKAGE_NAME>' | sudo bash`
6. Just run the curl command in your terminal and you'll see your script there. Ensure it's as intended.
7. Make a PR

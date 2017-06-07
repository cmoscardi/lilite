# Lilite: A Linux Package Auto-installer

[http://www.lilite.co](http://www.lilite.co)

[![Build Status](https://travis-ci.org/cmoscardi/package-installer.svg?branch=master)](https://travis-ci.org/cmoscardi/package-installer)


## Supported Linux versions

- Ubuntu 16.04
- Ubuntu 14.04

If you're interested in building out support for another distro,
let me know! Some of the infra for distro-specific install methods is WIP.

## Adding new packages
Package definitions live in `packages.json`.

### To add a new package (i.e. contributing)
Make a new entry in `packages.json` and submit a PR! There are three important fields:
- `pre_install` : List of shell commands to run before installing the package.
- `package_name` : Name of the package manager's package. This can be empty
                   if you're using a .deb file, for example.
- `post_install` : List of shell commands to run after the package is installed
                   via package manager.


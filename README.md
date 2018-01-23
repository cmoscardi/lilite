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

1. add the instructions on how to install a package
2. add in the logo

Package definitions live in [packages/packages.json](https://github.com/cmoscardi/lilite/tree/master/packages). Logos live in [static/images](https://github.com/cmoscardi/lilite/tree/master/static/images)

### To add a new package 
First, make a new entry in `packages/packages.json`. There are three important fields:
- `pre_install` : List of shell commands to run before installing the package.
- `package_name` : Name of the package manager's package. This can be empty
                   if you're using a .deb file, for example.
- `post_install` : List of shell commands to run after the package is installed
                   via package manager.

Second, add two copies of the logo - one "large" (i.e. original size) and one 48x48, PNG format - into static/images

Last, make a PR!

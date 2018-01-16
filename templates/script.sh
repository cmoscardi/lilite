#!/bin/bash
set -e

apt-get -y update
# standard packages
apt-get -y install {% for package in standard %}{{ package }} {% endfor %}

VERSION=`lsb_release -a | grep Description | cut -d ':' -f 2 | xargs | cut -d ' ' -f 2`
echo "Version is $VERSION"

# weird packages
{% for pre, package, post in weird %}
{% if pre %}{{pre}}{% endif %}
{% if package %}apt-get -y install {{package}}{% endif %}
{% if post %}{{post}}{% endif %}
{% endfor %}

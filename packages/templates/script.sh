#!/bin/bash
set -e

apt-get -y update
# standard packages
apt-get -y install {% for package in standard %}{{ package }} {% endfor %}

# weird packages
{% for pre, package, post in weird %}
{% if pre %}{{pre}}{% endif %}
{% if package %}apt-get -y --allow-unauthenticated install {{package}}{% endif %}
{% if post %}{{post}}{% endif %}
{% endfor %}

#!/bin/bash

for filename in `ls | grep large.png`; do
  name="${filename%.*}"
  name=`echo $name | cut -d "-" -f 1`
  convert $filename -resize 48x48 ${name}-48.png
done

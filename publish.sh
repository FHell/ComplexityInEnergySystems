#! /bin/sh

jekyll build
rm -r docs
mv _site docs

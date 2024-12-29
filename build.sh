#!/bin/bash

echo "Building..."

sudo dpkg-deb --build ../unifier
sudo mv ../unifier.deb ./unifier.deb
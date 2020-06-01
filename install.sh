#!/bin/bash

# Check root
if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root"
    exit 1
fi

# Installation
sudo pip install -r requirements.txt
sudo cp stegopy.py /usr/local/bin/stegopy.py
sudo chmod +x /usr/local/bin/stegopy.py
sudo mv /usr/local/bin/stegopy.py /usr/local/bin/stegopy
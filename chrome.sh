#! /bin/bash
sudo apt-get update
sudo apt-get install -y libxss1 libappindicator1 libindicator7 unzip xvfb libxi6 libgconf-2-4
sudo apt-get install default-jdk
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

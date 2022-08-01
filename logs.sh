#! /bin/bash

today=$(date "+%Y-%m-%d")
sudo docker logs --since=$today zstu-covid19-report
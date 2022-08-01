#! /bin/bash

sudo docker pull hlf01/python-selenium
sudo docker run --name zstu-covid19-report -i hlf01/python-selenium
sudo docker cp main.py zstu-covid19-report:/srv
sudo docker cp option.json zstu-covid19-report:/srv
sudo docker run --name zstu-covid19-report -e ZSTU_ID -e ZSTU_PASSWD -i hlf01/python-selenium bash -c "cd /srv && python main.py"
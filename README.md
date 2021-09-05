## Installation
```bash
$ sudo apt-get install python3-pip
$ sudo apt install python3-virtualenv python3-venv
$ git clone git@github.com:rafavg77/PokedexInlineTotaBot.git
$ cd PokedexInlineTotaBot 
$ cp src/Utils/config/config_example.ini src/Utils/config/config.ini
$ #Config Telegram token param in config.ini
$ virtualenv vevn
$ source venv/bin/activate
$ pip3 install -r requeriments.txt
$ cp systemd/bot_telegram_pokedex.service /etc/systemd/system/bot_telegram_pokedex.service
$ python3 src/boy.py
$ sudo systemctl enable bot_telegram_pokedex.service.service
$ sudo service bot_telegram_pokedex.service start
$ sudo service bot_telegram_pokedex.service status
```

## TODO:

- [x] Create pokedex Class
    - [] Search by ID or Name
- [x] Inline Commnad
- [X] Filter Commnad
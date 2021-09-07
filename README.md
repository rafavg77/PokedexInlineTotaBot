# PokedexInlineTotaBot
Telegram Pokedex Bot by Tota

![screen](https://raw.githubusercontent.com/rafavg77/PokedexInlineTotaBot/main/img/1.jpg)

![screen](https://raw.githubusercontent.com/rafavg77/PokedexInlineTotaBot/main/img/2.jpg)

## Installation
```bash
$ sudo apt-get install python3-pip
$ sudo apt install python3-virtualenv python3-venv
$ git clone https://github.com/rafavg77/PokedexInlineTotaBot.git
$ cd PokedexInlineTotaBot 
$ cp src/Utils/Config/config_example.ini src/Utils/Config/config.ini
$ #Config Telegram token param in config.ini
$ virtualenv vevn
$ #python3 -m virtualenv -p /usr/bin/python3.7 venv (for raspberry pi)
$ source venv/bin/activate
$ pip3 install -r requeriments.txt
$ sudo cp systemd/bot_telegram_pokedex.service /etc/systemd/system/bot_telegram_pokedex.service
$ python3 src/boy.py
$ sudo systemctl enable bot_telegram_pokedex.service
$ sudo service bot_telegram_pokedex start
$ sudo service bot_telegram_pokedex status
```

## TODO:

- [x] Create pokedex Class
    - [X] Search by ID or Name
- [x] Inline Commnad
- [X] Filter Commnad..

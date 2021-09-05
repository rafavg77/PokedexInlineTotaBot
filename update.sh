#!/bin/bash

sudo service bot_telegram_pokedex stop
sleep 60
cd /home/pi/Production/Bots/PokedexInlineTotaBot/
git pull
sudo service bot_telegram_pokedex start
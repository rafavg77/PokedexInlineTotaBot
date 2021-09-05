#!/bin/bash

echo "[+] Stopping bot_telegram_pokedex service"
sudo service bot_telegram_pokedex stop
echo "[+] waiting ..."
sleep 60
echo "[+] Accessing to directory"
cd /home/pi/Production/Bots/PokedexInlineTotaBot/
echo "[+] Downloading updates from git"
git pull
echo "[+] Starting service"
sudo service bot_telegram_pokedex start
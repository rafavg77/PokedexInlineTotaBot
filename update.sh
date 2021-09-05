#!/bin/bash

echo "[+] Stopping bot_telegram_pokedex service"
echo "[+] Stopping bot_telegram_pokedex service" | systemd-cat -t bot_telegram_pokedex -p info
sudo service bot_telegram_pokedex stop
echo "[+] waiting ..."
echo "[+] waiting ..." | systemd-cat -t bot_telegram_pokedex -p info
sleep 60
echo "[+] Accessing to directory"
echo "[+] Accessing to directory" | systemd-cat -t bot_telegram_pokedex -p info
cd /home/pi/Production/Bots/PokedexInlineTotaBot/
echo "[+] Downloading updates from git"
echo "[+] Downloading updates from git" | systemd-cat -t bot_telegram_pokedex -p info
git pull
echo "[+] Starting service"
echo "[+] Starting service" | systemd-cat -t bot_telegram_pokedex -p info
sudo service bot_telegram_pokedex start
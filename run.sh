clear
echo -e "\e[1m"
echo "    _______       __             _  __ "
echo "   / ____(_)___  / /_  ___  ____| |/ / "
echo "  / /   / / __ \/ __ \/ _ \/ ___/   /  "
echo " / /___/ / /_/ / / / /  __/ /  /   |   "
echo " \____/_/ .___/_/ /_/\___/_/  /_/|_|   "
echo "       /_/                             "
echo -e "\e[0m"
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" 
apt-get update
apt-get upgrade -y
apt upgrade -y
apt install python wget -y
pip3 install --no-cache-dir -U -r requirements.txt
clear
python3 -m bot

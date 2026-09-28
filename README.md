# BBBB

Scripts for the BBBB project

# Pi 4

## SD card

Burn an SD card, bookworm ('legacy') 64-bit lite. Trixie doesn't work yet. Use password rather than keys for now so we can all login if need be.

## Install eink stuff - old inky phat 

Log in, install git

    sudo apt-get install git

Install this repo

    git clone https://github.com/libbymiller/bbbb

Install inky phat examples

    git clone https://github.com/pimoroni/inky
    cd inky/
    ./install.sh

let it create a virtual env
let it create the examples and install the requirements for them
reboot

## test (old inky phat)

    /home/pi/.virtualenvs/pimoroni/bin/python3 /home/pi/inky/examples/name-badge.py -n "_IP=$(hostname -I)" -t phat --colour red

## test (new spectra6)


    cp bbbb/spectra6/hello_world.py  /home/pi/inky/examples/spectra6/
    /home/pi/.virtualenvs/pimoroni/bin/python3 /home/pi/inky/examples/spectra6/hello_world.py "_IP=$(hostname -I)"

## install birdnet-pi

    curl -s https://raw.githubusercontent.com/Nachtzuster/BirdNET-Pi/main/newinstaller.sh | bash

reboot and test by going to hostname.local or the IP from the eink in a browser

## show IP on boot on eink screen

Add rc.local - see files in this directory

    # old inky phat
    sudo cp rc.local /etc/rc.local

    # spectra6
    sudo cp rc.local.spectra6 /etc/rc.local

    # then
    sudo cp rc-local.service /etc/systemd/system/rc-local.service
    sudo chmod +x /etc/rc.local
    sudo systemctl enable rc-local
    sudo systemctl start rc-local
    sudo systemctl status rc-local

# Test birdnet pi with e.g. merlin

Play file close to mic; blackbird works well, no other speakng or noise as it will ignore it

# MQTT

You can add MQTT under settings; I've done this before and it works fine, although title needs to be blank or it sends malformed json

    {
      "common_name":"$comname",
      "species":"$sciname",
      "date":"$date",
      "time":"$time",
      "confidence":$confidence,
      "file":"$listenurl"
    }


# TODO

 * figure out how best to add wifi
 * figure out where to send the MQTT
 * try different eink display - https://shop.pimoroni.com/products/inky-impression?variant=56039376912763


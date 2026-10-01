# BBBB

Scripts / instructions for the BBBB project

# Pi 4 - wifi / garden install

## SD card

Burn an SD card, bookworm ('legacy') 64-bit lite. Trixie doesn't work yet. Use password rather than keys for now so we can all login if need be.

## Install eink libraries (all pimoroni einks)

Log in, install git

    sudo apt-get install git

Install this repo

    git clone https://github.com/libbymiller/bbbb

Install inky phat examples

    git clone https://github.com/pimoroni/inky
    cd inky/
    ./install.sh

let it create a virtual env, let it create the examples and install the requirements for them, then reboot

## test (old inky phat)

    /home/pi/.virtualenvs/pimoroni/bin/python3 /home/pi/inky/examples/name-badge.py -n "_IP=$(hostname -I)" -t phat --colour red

## test (new spectra6)

    cp /home/pi/bbbb/spectra6/hello_world.py  /home/pi/inky/examples/spectra6/
    /home/pi/.virtualenvs/pimoroni/bin/python3 /home/pi/inky/examples/spectra6/hello_world.py "_IP=$(hostname -I)"

## install birdnet-pi

    curl -s https://raw.githubusercontent.com/Nachtzuster/BirdNET-Pi/main/newinstaller.sh | bash

reboot and test by going to hostname.local or the IP from the eink in a browser

## show IP on boot on eink screen

First disable IPV6:

If you are connected by SSH, check the first address shown here:

    printf '%s\n' "$SSH_CONNECTION"

An address containing : is IPv6. Do not apply the change from that session; it will disconnect immediately. Confirm that IPv4 access, local console access, or another recovery path works first.

Disable IPv6

    sudo nano /boot/firmware/cmdline.txt

add " ipv6.disable=1" to the end

check after reboot by looking at ifconfig

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

Play file close to mic; blackbird works well, no other speaking or noise as it will ignore it

# MQTT

Install mosquitto

    sudo apt install mosquitto mosquitto-clients -y

test mosquitto is working
    
in one window (see everything coming in):

    mosquitto_sub -v -h localhost -p 1883 -t '#'

in another:

    mosquitto_pub -h localhost -p 1883 -m '{"foo":"bar"}' -t 'boids'

You can add MQTT under tools-> basic settings -> notifications in the birdnet UI tools: (username: 'birdnet', pwd blank)

Add this in the first box:

    mqtt://localhost:1883/boids

and this in the second (title needs to be blank or it sends malformed json)

    {
      "common_name":"$comname",
      "species":"$sciname",
      "date":"$date",
      "time":"$time",
      "confidence":$confidence,
      "file":"$listenurl"
    }

we'll have to grab the id of the device from the hostname in file, I think.

IMPORTANT: tick 'notify each new detection"

Then we use a custom python file to send it onwards - see example in this directory - process_and_forward_message.py - ask libby for the mqtt servedr etails

    pip3 install paho-mqtt --break-system-packages

    python mqtt/process_and_forward_message.py

add in a systemd file

    sudo cp mqtt/mqtt_forward.service /etc/systemd/system/
    sudo systemctl enable mqtt_forward.service
    sudo systemctl start mqtt_forward.service

# TODO

 * figure out how best to add wifi - sudo nmtui is a bit of a pain
 * figure out device ids
 * ✅ add systemd ffile for the mqtt python stuff
 * ✅ figure out where to send the MQTT -> to localhost and then to naturetelemetry
 * ✅ try different eink display - https://shop.pimoroni.com/products/inky-impression?variant=56039376912763


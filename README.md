# BBBB

Scripts / instructions for the BBBB project

# Pi 4 - wifi / garden install

## SD card

Burn an SD card, bookworm ('legacy') 64-bit lite. Trixie doesn't work yet. Use password rather than keys for now so we can all login if need be.

## Install eink libraries 

    sudo apt-get install git -y
    
Use these instructions for the display: https://github.com/kwmc-chris/bbbb-display

## install birdnet-pi

    curl -s https://raw.githubusercontent.com/Nachtzuster/BirdNET-Pi/main/newinstaller.sh | bash

reboot and test by going to hostname.local or the IP from the eink in a browser

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

IMPORTANT: tick 'notify each new detection"

We'll have to grab the id of the device from the hostname in file, I think.

Then we use a custom python file to send it onwards - see example in this directory - process_and_forward_message.py - ask libby for the mqtt server details

    pip3 install paho-mqtt --break-system-packages

edit mqtt/process_and_forward_message.py to use the correct mqtt server (ask libby)

    python mqtt/process_and_forward_message.py

add in a systemd file

    sudo cp mqtt/mqtt_forward.service /etc/systemd/system/
    sudo systemctl enable mqtt_forward.service
    sudo systemctl start mqtt_forward.service

## Disable IPv6

    sudo nano /boot/firmware/cmdline.txt

add " ipv6.disable=1" to the end

check after reboot by looking at ifconfig

# TODO

 * add geo to mqtt (at scale required)
 * replace forwarder with a bridge file
 * ✅ figure out how best to add wifi - sudo nmtui is a bit of a pain
 * ✅ figure out device ids
 * ✅ add systemd file for the mqtt python stuff
 * ✅ figure out where to send the MQTT -> to localhost and then to naturetelemetry
 * ✅ try different eink display - https://shop.pimoroni.com/products/inky-impression?variant=56039376912763


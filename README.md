# BBBB

Scripts / instructions for the BBBB project

# Pi 4 - wifi / garden install

## SD card

Burn an SD card, bookworm ('legacy') 64-bit lite. Trixie doesn't work yet. Use password rather than keys for now so we can all login if need be.

## Disable IPv6

    sudo nano /boot/firmware/cmdline.txt

add " ipv6.disable=1" to the end

check after reboot by looking at ifconfig

## Install eink libraries 

    sudo apt-get install git -y
    
Use these instructions for the display: https://github.com/kwmc-chris/bbbb-display

## install birdnet-pi

    curl -s https://raw.githubusercontent.com/Nachtzuster/BirdNET-Pi/main/newinstaller.sh | bash

It will automatically reboot. Test by going to hostname.local or the IP from the eink in a browser

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
     "latitude": $latitude,
     "longitude":$longitude,
     "file":"$listenurl"
    }

IMPORTANT: tick 'notify each new detection"

We'll have to grab the id of the device from the hostname in file, I think.

Then add a bridge file in /etc/mosquitto/conf.d/

    nano bridge.conf

contents:

    connection birdnet
    bridge_protocol_version mqttv311
    address dev.naturetelemetry.com:1883
    remote_username [ask libby]
    remote_password [ask libby]
    topic # out 0
    log_type all


# TODO

 * add geo to mqtt (at scale required)
 * ✅ replace forwarder with a bridge file
 * ✅ figure out how best to add wifi - sudo nmtui is a bit of a pain
 * ✅ figure out device ids
 * ✅ add systemd file for the mqtt python stuff
 * ✅ figure out where to send the MQTT -> to localhost and then to naturetelemetry
 * ✅ try different eink display - https://shop.pimoroni.com/products/inky-impression?variant=56039376912763


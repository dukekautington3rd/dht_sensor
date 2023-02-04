*Prerequisits for deploying on a container worker host*

```
sudo tee -a /etc/modules <<eof>/dev/null
i2c-bcm2708
i2c-dev
eof
```
* This enables the i2c interface *

```
sudo sed -i 's/\#dtparam=i2c_arm=on/dtparam=i2c_arm=on/' /boot/config.txt && sudo reboot
```

*If you need to install Docker*

```
sudo apt-get install -y docker.io docker-compose
```
*Enable non-root to interact with docker*
```
sudo usermod -aG docker $USER
```

*Clone this repo*
```
git clone https://github.com/dukekautington3rd/dht_sensor.git
```

*Customize for your environment*
```
cd dht_sensor && \
echo "room=My Room" > .env 
```

*Bring it up!*
```
cd dht_sensor ; \
docker-compose up -d
``` 

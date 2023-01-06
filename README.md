*Prerequisits for deploying on a container worker host*

```
sudo tee -a /etc/modules <<eof>/dev/null
i2c-bcm2708
i2c-dev
eof
```
* This enables the i2c interface *

```
sudo sed -i 's/\#dtparam=i2c_arm=on/dtparam=i2c_arm=on/' /boot/config.txt
```

*If you need to install Docker*

https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script
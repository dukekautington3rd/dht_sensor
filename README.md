*Prerequisits for deploying on a container worker host*

```
cat | sudo tee /etc/modules <<eof
   i2c-bcm2708
   i2c-dev
   eof
```
* This enables the i2c interface *

```
sudo sed -i 's/\#dtparam=i2c_arm=on/dtparam=i2c_arm=on/' /boot/config.txt
```
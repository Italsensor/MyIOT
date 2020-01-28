# MyIOT

**How to install the RTC module**

As first step you have to enable the I2C communication through the *raspi-config* configuration utility:

```
$ sudo raspi-config
```

when the configuration utility are up go to the *Interfacing Options*, then select the *I2C* entry and select *YES* to enable the I2C communication interface on your Raspberry board then exit from the utility.

Now you have to install the *I2C-tools* package:

```
$ sudo apt-get update
$ sudo apt-get install i2c-tools
```

When all the above steps are completed, download and then install the RTC configuration script by using these commands:

```
wget https://github.com/Italsensor/MyIOT/blob/master/configrtc.sh
chmod 755 rtc-install
sudo ./rtc-install
```

**How to install the batch file for command line command usage**

To locally download the command-line script utility use the following commands:

```
cd /usr/local/bin
sudo wget https://github.com/Italsensor/MyIOT/blob/master/rpicm3extended
sudo chmod 755 rpicm3extended
```

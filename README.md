# MyIOT

**How to install the RTC module**

As first step you have to enable the I2C communication through the raspi-config configuration utility:

```
$ sudo raspi-config
```

then go to the "Interfacing Options", then select the "I2C" entry and select "YES" to enable the I2C communication interface on your Raspberry board. Exit from the utility.

Now you have to installthe I2C-tools package:

```
$ sudo apt-get update
$ sudo apt-get install
```

With the comepleted above steps you can download and then install the RTC on board module by using these commands:

```
wget https://github.com/Italsensor/MyIOT/blob/master/rtc-install
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

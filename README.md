# MyIOT

**RTC: how to install the RTC module**

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
chmod 755 configrtc.sh
sudo ./configrtc.sh
```

If the installation end succesfully you can delete the install file and then reboot the Raspberry board in order to properly setup the RTC hardware module.

```
$ rm configrtc.sh
$ sudo reboot
```

**RTC: how to test the RTC module**

Ensure that the Raspberry is connected to the Internet and that you are able to reach a public NTP server, by means of the *date* command on the command line the current date should be shown:

```
$ date
Tue 28 Jan 13:09:18 CET 2020
```

In order to check the date stored into the hardware clock module you can use this command:

```
$ sudo hwclock -r
2020-01-28 13:10:26.785306+0100
```
if the returned date are not correct use the -w flag to force the correct date to be written inside the hardware clock module, so:

```
$ sudo hwclock -w
```

Now check again the date with the -r option as did above and look if this time the returned date is right or not.
If the date is not correct this may be due to an incorrect I2C bus behavior so run these commands:

```
sudo modprobe -r rtc_ds1307
sudo i2cdetect 1
```

here bwlow the expected output, press Y to perform the checking:

```
WARNING! This program can confuse your I2C bus, cause data loss and worse!
I will probe file /dev/i2c-1.
I will probe address range 0x03-0x77.
Continue? [Y/n] Y
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- 57 -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 6f
70: -- -- -- -- -- -- -- --
```

you must see the 6f address inside the list.
If you can not see this address may be that the I2C interface is not proper functioning or may be a hardware related the on board hardware RTC module.
To check about the proper I2C module initialization by the Linux Kernel use the command:

```
$ lsmod
```
inside the shown list check if the *i2c_dev* and *i2c_bcm2835* identifier are still presents, this mean that the Linux kernel was able to load the right modules needed to handle the I2C communication interface, then double check if you have properly installed the RTC module (see the previus section for the installing step).

if all the check concenrning the kernel modules and the installing step are succesfully may be an hardware issue of the RTC module or the Raspberry Compute Module, so try to change first the Compute Module with another one that you know is properly working and check again.

**How to install the batch file for command line command usage**

To locally download the command-line script utility use the following commands:

```
cd /usr/local/bin
sudo wget https://github.com/Italsensor/MyIOT/blob/master/rpicm3extended
sudo chmod 755 rpicm3extended
```

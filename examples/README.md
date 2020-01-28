# MyIOT - examples section

This folder is related that you can use in order to test the functionality of the MyIOT module.

All the module functionalities can be managed through a dedicated system application which can be executed directly from the command line. In order to show the online guide type:

```
$ ./rpicm3extended
RPICM3 utility - User Manual
rpicm3extended led on|off|time_ms|time_on_ms time_off_ms num_cycles
rpicm3extended led1 on|off|time_ms|time_on_ms time_off_ms num_cycles
rpicm3extended out<n> (n=1...8) on|off
rpicm3extended outall on|off|unexport
rpicm3extended outen<n> (n=1..2) on|off
rpicm3extended outenall on|off
rpicm3extended watchdog enable|disable|heartbeat|timeout
rpicm3extended reset
```

for example:

To manage outputs on expansion module there are the following options:

- led     : turn (on) o turn (off) led L1
- led1    : turn (on) turn (off) led L2
- out<n>  : set to “1” (5V) or to “0” (0V) output line n (n=1…8)
- outall  : set to “1” (5V) or to “0” (0V) all the output line
- outen<n>: enable (on) or disable (off) first or second group of the 4 output lines
- outenall: enable (on) or disable (off) all the outputs placing them on high impedance (3-state)
  
There are also other demo programs, written in Python, that can be used as starting point in writing their own applications.

**testout.py** expansion interface outputs and led demo
**tstGPIO18.py** set the GPIO18 line to high in order to activate the Common Module reset procedure after 60s
**tstGPIO25.py** Read the GPIO25 line state (status of RST button)
**tstHWWDT.py** Hardware watchdog usage example

Each demo can be interrupted during execution anytime by pressing the CTRL+C key combination.

Major details are written into the comments contained inside every file.

For other details about the available GPIO and related function take a look at the module [manual](/manual/First-Startup_ENG.pdf) into the *manual* section of this repository.

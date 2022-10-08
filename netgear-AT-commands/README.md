# Netgear M6 Pro (MR6400/MR6500) AT Command list

Get to the serial console: https://www.waveform.com/a/b/guides/mr1100-band-locking as described in Step 1

Useful tool: [sierrakeygen.py](https://github.com/bkerler/edl/tree/master/edlclient/Tools) [Readme](https://github.com/bkerler/edl/blob/master/sierrakeygen_README.md)

---

### Usual Sierra LOCK/MEP/CND commands
```
#Use SDX55 for -d, even though it uses a SDX65
#example: 
#python3 sierrakeygen.py -d SDX55 -l AA11BB22CC33DD44

#Get LOCK challenge, use -l in sierrakeygen
AT!OPENLOCK? 
AT!OPENLOCK=[challenge response]
#Get MEP challenge, use -m in sierrakeygen
AT!OPENMEP? 
AT!OPENMEP=[challenge response]
#Get CND challenge, use -c in sierrakeygen
AT!OPENCND? 
AT!OPENCND=[challenge response]
#Sets a new password for CND
AT!SETCND="CNDPW"
AT!ENTERCND="CNDPW"
```

---

### Info
```
ATI
AT!GSTATUS?
```

---

### SIM Unlock
```
AT!OPENLOCK?
AT!OPENLOCK=[challenge response]
AT!OPENMEP?
AT!OPENMEP=[challenge response]
AT!NVMEPRST
AT!GRESET
```

---

### Enable ROOT telnet (port 23)
```
AT!OPENLOCK?
AT!OPENLOCK=[challenge response]
AT!TELEN=1
AT!CUSTOM="RDENABLE",1
AT!RESET
```
Then, just wait till reboot and telnet to port 23 and you're root. You might need to reboot twice.

---

### Disable ROOT telnet
```
AT!OPENLOCK?
AT!OPENLOCK=[challenge response]
AT!TELEN=0
AT!CUSTOM="RDENABLE",0
AT!RESET
```

---

### Band locking

#### List your current band list
```
AT!BAND?
AT!BAND=?
```

#### Set some bands (THIS HAS NO EFFECT ON THE MR6400)
```
AT!BAND=01,"ALL 4G ONLY",0,A1003300385F,42,0,0,0
AT!BAND=02,"TMO HIGH B2/4/66 n41/77",0,1000300000A,2,10001000000,1002,0
AT!BAND=03,"TMO NRSA n41/71/77",0,0,0,0000010001000000,1042,0
AT!BAND=04,"VZW NRNSA B2/4/5/13/66 n2/5/66/77",0,101A,2,12,1002,0
AT!RESET
```

#### Remove some bands
```
AT!BAND=04,"",0
```

#### Select a band (Only necessary on the 6500, the 6400 UI allows selection)
```
#Select the band in index 01, "ALL 4G ONLY" in the example above
AT!BAND=01
AT!RESET
```

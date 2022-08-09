# Netgear Mobile Router Firmware Tools

Python3 script to decrypt a Netgear Mobile Router firmware. It will generates all of the individual files, headers, and a full representation of the plaintext sierra update file.

Use https://github.com/jrspruitt/ubi_reader or something like it to browse UBIFS

#### Compatible devices:
- M6 Pro (MR6400, MR6500)
- M5 5G  (MR5200)
- Nighthawk M1 (MR1100)
- Should work on any Sierra based Netgear mobile broadband routers

#### Tested on:
- MR1100-1EEEUS_23113575_NTG9x50C_12.06.03.00_00_EEUK_04.01.secc
- MR1100-100NAS_23113828_NTG9x50C_12.06.11.00_00_GenericNA_05.03.secc
- MR6400-1DNNAS_23115595_NTGX65_10.01.41.02_00_Dish_01.03_00.secc

pip install -r requirements.txt


### Thanks to
Based on work by G Richter at PenTestPartners and his talk at Defcon 27
- https://media.defcon.org/DEF%20CON%2027/DEF%20CON%2027%20presentations/DEFCON-27-grichter-Reverse-Engineering-4G-Hotspots-For-Fun-Bugs-Net-Financial-Loss.pdf
- https://github.com/pentestpartners/defcon27-4grouters

### To-do:
Encrypt a Sierra update file to Netgear

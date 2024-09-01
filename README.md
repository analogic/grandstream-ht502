Grandstream HT502 reverse engineering attempt
/////////////////////////////////////////////

1. NOR flash was dumped directly by desoldering to another board - flash-dump.bin
2. binwalk -e flash-dump.bin // produced multiple files which are not inspectable
3. binwalk -Bbe D0000.squashfs // decoded blocks which was compressed, no other known squashfs decoding worked
4. we have found block "426A2" which contained "%s:GrandstreamTX2013lZpRbM:%s" secret - almost the same as with HT802, see https://github.com/BigNerd95/Grandstream-Firmware-HT802/blob/master/SuperUser/GSSU.py
5. got root shell with gssu
6. # echo "#!/bin/sh" > /tmp/cgi-bin/download
   # echo "tar cf - /rom 2> /dev/null" >> /tmp/cgi-bin/download
   # httpd -p 8080 -h /tmp
7. !

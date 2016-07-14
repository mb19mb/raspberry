# Infrarot Kamera 

## Installation
RaspiConfig tool starten und "Enable Camera" auswählen
~ $ raspi-config

## Fotos

JPEG-Foto:
~ $ raspistill -o image.jpg

PNG-Foto:
~ $ raspistill -o image.png –e png

Foto bei Tastendruck (Enter)
~ $ raspistill -t 0 -k -o image%02d.jpg

Zeitverzögert (5 Sekunden)
~ $ raspistill -o image.jpg -t 5000

Auflösung (640x480)
~ $ raspistill -o image.jpg -w 640 -h 480

Qualität ändern (0-100)
~ $ raspistill -o image.jpg -q 20

Zeitraffer (Aufnahmedauer 3600000 (1h), Intervall 5000 (5 Sekunden))
~ $ raspistill -o image_%04d.jpg -tl 5000 -t 3600000

## Videos

5 Sekunden 1080p (1920 x 1080)
~ $ raspivid -o video.h264 -t 50000

Endlosaufname mit -t 0

5 Sekunden 720p (1280 x 720)
~ $ raspivid -o video.h264 -t 50000 -w 1280 -h 720

individueller Bitrate (1.5MBits/s)
~ $ raspivid -o video.h264 -t 50000 -b 1500000

individueller Framerate (10 Frames/Sekunde)
~ $ raspivid -o video.h264 -t 50000 -f 10

Videostream an stdout
~ $ raspivid -t 50000 -o -

## Videos konvertieren

H264 nach mp4
~ $ apt-get install gpac
~ $ MP4Box -fps 30 -add video.h264 video.mp4

# Videostream

## Server
Konfiguration

~ $ apt-get install netcat

~ $ raspivid -t 0 -o - | nc 192.168.20.100 5555


## Client

Konfiguration

~ $ apt-get install mplayer netcat
~ $ nc -l -p 5555 | mplayer -fps 31 -cache 1024 -

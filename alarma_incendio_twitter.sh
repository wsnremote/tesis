#!/bin/sh
mensaje='Se activo la alarma contra incendios del apartamento '$2' con una medicion de: '$3'. La temperatura ambiente es '$4'C '$5'F y humedad: '$6
/usr/bin/python /home/pi/tesis/enviar_twitter.py $1 $mensaje

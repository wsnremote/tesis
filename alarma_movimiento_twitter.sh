#!/bin/sh
mensaje='Se detecto movimiento cerca del apartamento '$2' a una distancia de: '$3'cm.'
/usr/bin/python /home/pi/tesis/enviar_twitter_movimiento.py $1 $mensaje

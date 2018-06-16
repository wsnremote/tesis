#!/usr/bin/env python
import json
import serial
import time
import os

contador_linea_apto01=0
contador_linea_apto02=0
contador_linea_apto03=0
contador_linea_apto04=0
contador_linea_apto05=0
contador_linea_apto06=0
contador_linea_apto07=0
contador_linea_apto08=0
contador_linea_apto09=0
contador_linea_apto10=0
contador_linea_apto11=0
contador_linea_apto12=0
contador_linea_apto13=0
contador_linea_apto14=0
contador_linea_apto15=0
contador_linea_apto16=0
contador_linea_apto17=0
contador_linea_apto18=0
contador_linea_apto19=0
contador_linea_apto20=0

leer_puerto_serial = serial.Serial('/dev/ttyUSB0', 115200)

while True:
	fecha = time.strftime("%y%m%d%H")
	linea = leer_puerto_serial.readline().strip()
	cantidad_bytes = str.encode(linea)
	if len(cantidad_bytes) > 1 :
        	valores_linea = eval(linea)
		if valores_linea['IDA'] == 1 :
			apartamento ='01'
			telefono_apto01 = '59897349014'
			twitter_apto01 = '@pedrobonillor'
			contador_linea_apto01 = contador_linea_apto01 + 1
			if contador_linea_apto01 == 1 :
				SP1_APTO01 = valores_linea['SP']
				SL1_APTO01 = valores_linea['SL']
				SU1_APTO01 = valores_linea['SU']
			if contador_linea_apto01 == 2 :
				SP2_APTO01 = valores_linea['SP']
				SL2_APTO01 = valores_linea['SL']
				SU2_APTO01 = valores_linea['SU']
			if contador_linea_apto01 == 3 :
				SP3_APTO01 = valores_linea['SP']
				SL3_APTO01 = valores_linea['SL']
				SU3_APTO01 = valores_linea['SU']
			if contador_linea_apto01 == 4 :
				SP4_APTO01 = valores_linea['SP']
				SL4_APTO01 = valores_linea['SL']
				SU4_APTO01 = valores_linea['SU']
			if contador_linea_apto01 == 5 :
				SP5_APTO01 = valores_linea['SP']
				SL5_APTO01 = valores_linea['SL']
				SU5_APTO01 = valores_linea['SU']
				SLF_APTO01 = min([SL1_APTO01,SL2_APTO01,SL3_APTO01,SL4_APTO01,SL5_APTO01])
                                SUF_APTO01 = min([SU1_APTO01,SU2_APTO01,SU3_APTO01,SU4_APTO01,SU5_APTO01])
				if SP1_APTO01 == 1 or SP2_APTO01 == 1 or SP3_APTO01 == 1 or SP4_APTO01 == 1 or SP5_APTO01 == 1 :
					SPF_APTO01 = 1
				else :
					SPF_APTO01 = 0
				if SPF_APTO01 ==1 or SUF_APTO01 < 10 :
					ejecucion_kill_alarma_movimiento_whatsup = 'kill -9 `ps -ax | grep alarma_movimiento_whatsup_apto'+apartamento+' | head -1 | awk '+'\''+'{printf $1}'+'\''+'`'
					os.system(ejecucion_kill_alarma_movimiento_whatsup)
					ejecucion_alarma_movimiento_whatsup = 'nohup /home/pi/tesis/alarma_movimiento_watsup.sh '+telefono_apto01+' '+apartamento+' '+str(SUF_APTO01)+' &'
					os.system(ejecucion_alarma_movimiento_whatsup)
					ejecucion_alarma_movimiento_twitter = 'nohup /home/pi/tesis/alarma_movimiento_twitter.sh '+twitter_apto01+' '+apartamento+' '+str(SUF_APTO01)+' &'
					os.system(ejecucion_alarma_movimiento_twitter)
				if SLF_APTO01 < 100 :
					ejecucion_kill_alarma_incendio_whatsup = 'kill -9 `ps -ax | grep alarma_incendio_whatsup_apto'+apartamento+' | head -1 | awk '+'\''+'{printf $1}'+'\''+'`'
					os.system(ejecucion_kill_alarma_incendio_whatsup)
					ejecucion_alarma_incendio_whatsup = 'nohup /home/pi/tesis/alarma_incendio_watsup.sh '+telefono_apto01+' '+apartamento+' '+str(SLF_APTO01)+' '+str(valores_linea['C'])+' '+str(valores_linea['F'])+' '+str(valores_linea['H'])+' &'
					os.system(ejecucion_alarma_incendio_whatsup)
					ejecucion_alarma_incendio_twitter = 'nohup /home/pi/tesis/alarma_incendio_twitter.sh '+twitter_apto01+' '+apartamento+' '+str(SLF_APTO01)+' '+str(valores_linea['C'])+' '+str(valores_linea['F'])+' '+str(valores_linea['H'])+' &'
					os.system(ejecucion_alarma_incendio_twitter)
				LINEA_APTO01 =  "{'IDA': 1, 'D': "+str(valores_linea['D'])+", 'M': "+str(valores_linea['M'])+", 'A': "+str(valores_linea['A'])+", 'HO': "+str(valores_linea['HO'])+", 'MI': "+str(valores_linea['MI'])+", 'S': "+str(valores_linea['S'])+", 'SP': "+str(SPF_APTO01)+", 'SL': "+str(SLF_APTO01)+", 'SU': "+str(SUF_APTO01)+", 'C': "+str(valores_linea['C'])+", 'F': "+str(valores_linea['F'])+", 'H': "+str(valores_linea['H'])+"}"
				contador_linea_apto01 = 0
				ejecucion = 'nohup echo "'+LINEA_APTO01+'" '+'|'+ ' /home/pi/hadoop/bin/hdfs dfs -appendToFile - /WSN_REMOTE/APTO'+apartamento+'/'+fecha+' &'
				os.system(ejecucion)





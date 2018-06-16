sleep 10
kill -9 `ps -ax | grep alarma_movimiento_whatsup_apto$1 | head -1 | awk '{ printf $1}'`

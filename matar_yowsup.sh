$proceso = `ps -ax | grep $1 | head -1 | awk '{ printf $1}'`
echo $proceso

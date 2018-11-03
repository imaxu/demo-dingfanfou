#! /bin/bash
# restart uwsgi
process=uwsgi
pid=$(netstat -anlp | awk '{print $7}' | grep $process | grep -o '[0-9]\+' | head -1)
for i in $pid
do
echo "Kill the $1  process [ $i ]"
kill -9 $i
done

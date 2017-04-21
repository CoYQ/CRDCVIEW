pid=$(ps -aux | grep "ec" |awk '{print $2}')
echo "kill pid "$pid
kill -9 $pid
echo 'kill success.'
sleep 1


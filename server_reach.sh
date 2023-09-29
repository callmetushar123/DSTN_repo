echo "============Head & Metadata Node==============="
ping -c5 -W1 10.147.17.102 >> syslog.txt && echo 'Server REACHABLE at [IP:10.147.17.102] ' || echo 'Server UNREACHABLE'
echo "============Storage Node1==============="
ping -c5 -W1 10.147.17.79 >> syslog.txt && echo 'Server REACHABLE at [IP:10.147.17.79] ' || echo 'Server UNREACHABLE'
echo "============Storage Node2==============="
ping -c5 -W1 10.147.17.202 >> syslog.txt && echo 'Server REACHABLE at [IP:10.147.17.202] ' || echo 'Server UNREACHABLE'
echo "============Storage Node3==============="
ping -c5 -W1 10.147.17.88 >> syslog.txt && echo 'Server REACHABLE at [IP:10.147.17.88] ' || echo 'Server UNREACHABLE'

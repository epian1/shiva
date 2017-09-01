# shiva

Small DoS (or DDoS if you count multithreading) that currently holds two attack methods, udp and syn flooding.
Also comes with other tweaks the user can change such as flood time (in seconds), thread count, and method switch.


# Requires
* [Python3.x+](http://www.dropwizard.io/1.0.2/docs/)
* Root access. (must run sudo as shown below)

# Examples
```
sudo python3 main.py -h
```
```
sudo python3 main.py -v 127.0.0.1 -d 80 -m udp -t 60 -p 10
```
```
sudo python3 main.py -v 127.0.0.1 -d 80 -m syn -t 60 -p 10
```

# shiva

Small DoS (or DDoS if you count multithreading) that currently holds two attack methods, udp and syn flooding.
Also comes with other tweaks the user can change such as flood time (in seconds), thread count, and method switch.

comments, conserns or criticism find me here: https://discord.gg/cKv2DMF

# Usage
-v, --victim      | The IP address.                             
-d, --destination | The targeted Port number.                   
-m, --method      | The attack Method.                          
-p, --processes   | The Thread count.                         
-t, --time        | The attack Time length in second(s).        
-s, --sleep       | The time between each packet in second(s).  


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

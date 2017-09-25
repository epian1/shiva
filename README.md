# shiva

User friendly command-line based SYN & UDP attack script that lets the user have complete control over the script settings (listed below), also displays attack review (shows inputed settings, if the user is happy they can continue else they can quit and re-enter value(s)) & summary.

comments, conserns or criticism find me here: https://discord.gg/cKv2DMF

# Usage
* The only option you have to give an argument to is -v, --victim. The rest are given reasonable deafault values if no argument is given an option.

-v, --victim      | The IP address.                             
-d, --destination | The targeted Port number.                   
-m, --method      | The attack Method.                          
-p, --processes   | The Thread count.                         
-t, --time        | The attack Time length in second(s).        
-s, --sleep       | The time between each packet in second(s).  


# Requires
* [Python3.5+](http://www.dropwizard.io/1.0.2/docs/)
* Root access. (must run sudo as shown below)

# Examples
* Does not need to be in this format / order.
```
sudo python3 main.py -h
```
```
sudo python3 main.py -v 127.0.0.1 -d 80 -m udp -t 60 -p 10 -s .1
```
```
sudo python3 main.py -v 127.0.0.1 -d 80 -m syn -t 60 -p 10 -s .1
```

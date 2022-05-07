"""
Zen Environment

Zen Environment is a Python package for managing your environments.
"""

from argparse import ArgumentParser

__version__ = '0.1.0'


def main():
    """
    Main entry point for the Zen Environment package.
    """
    parser = ArgumentParser(description='Zen Environment')

    cmd = parser.add_mutually_exclusive_group()
    dbg = parser.add_mutually_exclusive_group()

    parser.add_argument('directory', nargs='?', default='.', help='Directory to work in')

    cmd.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')
    cmd.add_argument('-C', '--create', action='store_true', help='Create a new environment')
    cmd.add_argument('-I', '--import', action='store_true', help='Import from other environment manager')
    cmd.add_argument('-E', '--enter', action='store_true', help='Enter an environment')
    cmd.add_argument('-D', '--delete', action='store_true', help='Delete an environment')
    cmd.add_argument('-i', '--info', action='store_true', help='Show environment information')
    cmd.add_argument('-U', '--update', action='store_true', help='Update an environment')
    cmd.add_argument('-A', '--add', action='store_true', help='Add packages to an environment')
    cmd.add_argument('-R', '--remove', action='store_true', help='Remove packages from an environment')
    cmd.add_argument('-F', '--freeze', action='store_true', help='Freeze an environment to a requirements.txt')

    dbg.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
    dbg.add_argument('-q', '--quiet', action='store_true', help='Disable output')

    parser.add_argument('-p', '--python', type=str, action='store', help='Python interpreter to use')
    parser.add_argument('-P', '--package', nargs='?', action='append', help='Package to install')
    parser.add_argument('--dev', action='store_true', help='Mark as development package')
    parser.add_argument('-M', '--mirror', action='store', help='Mirror to use')

    args = parser.parse_args()

    if args.debug:
        print('Debug mode enabled')
        print(args)
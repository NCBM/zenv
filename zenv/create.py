"""
Create Zen Environment
"""

from dataclasses import dataclass
import os
from platform import python_version
from typing import List
from zenv import debug
import venv
import toml


@dataclass
class CreateZenEnvArgs:
    """
    Create Zen Environment arguments.
    """
    directory: str
    pyversion: str
    mirror: str


def create_zen_env(args: CreateZenEnvArgs, dbg: debug.DebugArgs) -> None:
    """
    Create a Zen Environment.

    * ZenEnv structure:
        - .zenv/
            - venv/  (virtual environment)
            - zenenv.toml  (to store the configuration)
    """
    if not dbg.quiet:
        print(f'Creating Zen Environment in {args.directory}')
    
    # Create the Zen Environment Directory Tree
    if not os.path.exists(args.directory):
        os.makedirs(args.directory)
    if not os.path.exists(os.path.join(args.directory, '.zenv')):
        os.makedirs(os.path.join(args.directory, '.zenv'), exist_ok=True)
    else:
        if not dbg.quiet:
            print('Zen Environment already exists')
            print('Do you want to override it? (y/N)')
            answer = input()
            if answer.lower() != 'y':
                return
        else:
            return
    if not os.path.exists(os.path.join(args.directory, '.zenv', 'venv')):
        os.makedirs(os.path.join(args.directory, '.zenv', 'venv'))

    # Create the virtual environment
    if not dbg.quiet:
        print('Creating virtual environment')
    venv_path = os.path.join(args.directory, '.zenv', 'venv')
    venv.create(
        venv_path,
        system_site_packages=False,
        clear=True,
        with_pip=True,
    )

    # Create the configuration file
    if not dbg.quiet:
        print('Creating configuration file')

    filepath = os.path.join(args.directory, '.zenv', 'zenenv.toml')
    with open(filepath, 'w') as f:
        f.write(
            toml.dumps(
                {
                    'pyversion': args.pyversion if args.pyversion else python_version(),
                    'mirror': args.mirror if args.mirror else 'https://pypi.org/simple/',
                }
            )
        )
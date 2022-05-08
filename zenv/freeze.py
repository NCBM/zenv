"""
ZenEnv data freezing tool.
"""

import os
import sys
from dataclasses import dataclass
from typing import List, Tuple
import toml
from zenv import debug


@dataclass
class FreezeArgs:
    """
    Freeze arguments.
    """
    directory: str
    dev: bool


def _freeze(args: FreezeArgs, dbg: debug.DebugArgs) -> List[Tuple[str, str]]:
    """
    Get Packages from Zen Environment.
    """
    if not dbg.quiet:
        print('Looking VENV for packages')

    venv_path = os.path.join(args.directory, '.zenv', 'venv')
    site_packages = os.path.join(venv_path, 'Lib' if sys.platform == 'nt' else 'lib', 'site-packages')
    packages = []
    for root, dirs, files in os.walk(site_packages):
        if 'METADATA' in files:
            with open(os.path.join(root, 'METADATA'), 'r') as f:
                pkg, version = '', ''
                for line in f:
                    if line.startswith('Name:'):
                        pkg = line.split(':')[1].strip()
                    if line.startswith('Version:'):
                        version = line.split(':')[1].strip()
                if not pkg or not version or pkg in ['setuptools', 'pip', 'wheel']:
                    continue
                packages.append((pkg, version))
    if not dbg.quiet:
        print(f'Found {len(packages)} packages')
    return packages



def freeze_zen_env(args: FreezeArgs, dbg: debug.DebugArgs) -> None:
    """
    Freeze the Zen Environment into requirements.txt.
    """
    if not dbg.quiet:
        print(f'Freezing Zen Environment in {args.directory}')

    if not os.path.exists(os.path.join(args.directory, '.zenv', 'zenenv.toml')):
        if not dbg.quiet:
            print('No Zen Environment found')
        sys.exit(1)

    # Read the Zen Environment configuration
    with open(os.path.join(args.directory, '.zenv', 'zenenv.toml'), 'r') as f:
        config = toml.load(f)

    # Freeze the Zen Environment
    if not dbg.quiet:
        print('Freezing Zen Environment')
    packages = _freeze(args, dbg)
    with open(os.path.join(args.directory, 'requirements.txt'), 'w') as f:
        for pkg, version in packages:
            f.write(f'{pkg}=={version}\n')

    # Freeze dev
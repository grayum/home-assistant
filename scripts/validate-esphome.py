#!/usr/bin/env python3
"""Validate the public example with throwaway credentials; never touch hardware."""

import argparse
import base64
from pathlib import Path
import secrets
import shutil
import subprocess
import sys
import tempfile

import yaml


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generate', action='store_true', help='also generate C++ (not a full firmware build)')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    project = root / 'esphome' / 'eurom-mon-soleil-dsp'
    with tempfile.TemporaryDirectory(prefix='eurom-esphome-') as directory:
        config = Path(directory) / 'eurom-400-wifi.yaml'
        shutil.copyfile(project / config.name, config)
        dummy_secrets = {
            'wifi_ssid': 'CI-NOT-A-REAL-NETWORK',
            'wifi_password': secrets.token_urlsafe(24),
            'eurom_400_wifi_fallback_password': secrets.token_urlsafe(24),
            'eurom_400_wifi__encryption_key': base64.b64encode(secrets.token_bytes(32)).decode('ascii'),
        }
        (Path(directory) / 'secrets.yaml').write_text(yaml.safe_dump(dummy_secrets), encoding='utf-8')
        # Config output contains only throwaway values, never local device secrets.
        commands = [['config', str(config)]]
        if args.generate:
            commands.append(['compile', str(config), '--only-generate'])
        for command in commands:
            subprocess.run([sys.executable, '-m', 'esphome', *command], check=True)
    print('Validation complete. No device access or firmware flashing performed.')


if __name__ == '__main__':
    main()

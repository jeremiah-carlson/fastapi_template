import os
from pathlib import Path
import yaml
from typing import Dict

PARENT_DIR = Path('.')

def load_app_info()-> Dict:
    with open(PARENT_DIR / 'conf' / 'app_info.yaml', 'r') as ai:
        return yaml.safe_load(ai)        

def parse_configs()-> Dict:
    with open(PARENT_DIR / 'conf' / 'config.yaml', 'r') as conf:
        return yaml.safe_load(conf)

def parse_secrets()-> Dict:
    with open(PARENT_DIR / 'conf' / '.secrets', 'r') as conf:
        return yaml.safe_load(conf)

def log_runtime()-> None:
    with open(PARENT_DIR / 'conf' / 'runtime.yaml', 'w') as p_log:
        p_log.write('ppid: %s\npid: %s' % (os.getppid(), os.getpid()))

app_info = load_app_info()
configs = parse_configs()
secrets = parse_secrets()
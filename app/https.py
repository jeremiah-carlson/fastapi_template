from pathlib import Path
import uvicorn

from scripts.setup import configs
from main import app

PATH_RT = Path('.')

if __name__ == '__main__':
    uvicorn.run(
        app,
        host=configs['deployment']['host'],
        port=443,
        ssl_keyfile=configs['ssl']['key'],
        ssl_certfile=configs['ssl']['cert']
        )
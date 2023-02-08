from fastapi import FastAPI, Response, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from http import HTTPStatus
from sys import platform
from subprocess import Popen

from scripts.setup import configs, app_info, log_runtime


log_runtime() # Store current ppid and pid in conf/runtime.yaml

app = FastAPI(
    title = app_info.get('title', ''),
    description = app_info.get('description', ''),
    version = app_info.get('version', '0.0.0'),
    contact = app_info.get('contact',
        {
            'name': 'Bob Ross',
            'email': 'HappyTrees@gmail.com'
        }
    ),
    openapi_tags = app_info.get('tags', [])
)


app.add_middleware(
    CORSMiddleware,
    allow_origins = configs['cors']['allow_origins'],
    allow_credentials = configs['cors']['allow_credentials'],
    allow_methods = configs['cors']['allow_methods'],
    allow_headers = configs['cors']['allow_headers'],
)

@app.get('/')
def read_root(response: Response):
    response.status_code = HTTPStatus.MOVED_PERMANENTLY.value
    return RedirectResponse('/docs')


if __name__ == '__main__':

    ''' #Run https as subprocess
    if platform == 'linux':
        Popen(['python3', '-m', 'https'])
    else:
        Popen(['.\env\Scripts\python.exe', '-m', 'https'])
    '''
    uvicorn.run(
        app,
        host=configs['deployment']['host'],
        port=configs['deployment']['port']
        )
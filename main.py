import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
import uvicorn
from appconfig import Config

conf = Config()
port = conf.service()

if __name__ == '__main__':
    uvicorn.run('server.app:app', host="0.0.0.0", port=port['port'], reload=True)

import requests
import logging
import os
import json
from datadog import initialize
from datadog import statsd
import time

class EWBFStats:
    def __init__(self):
        self.config = self._getconfig()
        self._initialize_dogstatsd()

    def poll_stats(self):
        poll_time = self.config['poll']
        while(True):
            stats = self._getstats()
            self._send_stats(stats)
            time.sleep(poll_time)
        
    def _getconfig(self):
        config = {}
        config['host'] = os.getenv('HOST', default='127.0.0.1')
        config['port'] = os.getenv('PORT', default=5000)
        config['uri'] = os.getenv('URI', default='/getstat')
        config['poll'] = os.getenv('POLLSEC', default=15)
        # Purposefully going to fail if these values are not set
        config['api_key'] = os.environ['API_KEY']
        config['app_key'] = os.environ['APP_KEY']

        return config

    def _initialize_dogstatsd(self):
        options = {
            'api_key': self.config['api_key'],
            'app_key': self.config['app_key']
        }
        initialize(**options)

    def _getstats(self):
        stats = {}
        request_url = 'http://{}:{}{}'.format(self.config['host'], self.config['port'], self.config['uri'])
        try:
            r = requests.get(request_url)
            r.raise_for_status()
            stats = json.loads(r.text)
        except requests.HTTPError:
            logging.critical('Unable fetch stats at %s, retrying', request_url, exc_info=True)
        except requests.ConnectionError:
            logging.critical('Unable to connect to EWBF at address %s', request_url, exc_info=True)
        return stats

    def _send_stats(self, stats):
        for result in stats['result']:
            for k,v in result.items():
                if isinstance(v, str):
                    continue
                statsd.gauge('ewbf.{}'.format(k), v, tags=['name:{}-{}'.format(result['name'], result['gpuid'])])
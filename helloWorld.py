from flask import Flask

import os
import utests

import logging

open('server.log', 'w').close()
logging.basicConfig(filename='server.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

isServer = False

if __name__ == '__main__':
	f = open('server.cfg','r')
	lines = [line for line in f]
	if (lines[0].strip() == "server"):
		isServer=True
	ip,port = lines[1].split(':')

	logging.info('Is server='+str(isServer))
	if (isServer == False):
		utests.utest()

	app.run(host=ip,port=int(port))

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return ("Exception: "+e), 500

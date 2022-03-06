import functools
from flask import Flask, request, jsonify
import logging
from time import strftime
import sys
app = Flask(__name__)

option = True if len(sys.argv) >=2 and sys.argv[1]=="debug" else False

if option == True:
    logging.basicConfig( level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
 


def accept(func_or_mimetype=None):
    """Decorator which allows to use multiple MIME type handlers for a single
    endpoint.
    """

    # Default MIME type.
    mimetype = 'text/html'

    class Accept(object):
        def __init__(self, func):
            self.default_mimetype = mimetype
            self.accept_handlers = {mimetype: func}
            functools.update_wrapper(self, func)

        def __call__(self, *args, **kwargs):
            default = self.default_mimetype
            mimetypes = request.accept_mimetypes
            best = mimetypes.best_match(self.accept_handlers.keys(), default)
            # In case of Accept: */*, choose default handler.
            if best != default and mimetypes[best] == mimetypes[default]:
                best = default
            return self.accept_handlers[best](*args, **kwargs)

        def accept(self, mimetype):
            """Register a MIME type handler."""

            def decorator(func):
                self.accept_handlers[mimetype] = func
                return func
            return decorator

    # If decorator is called without argument list, return Accept instance.
    if callable(func_or_mimetype):
        return Accept(func_or_mimetype)

    # Otherwise set new MIME type (if provided) and let Accept act as a
    # decorator.
    if func_or_mimetype is not None:
        mimetype = func_or_mimetype
    return Accept

@app.route('/hello')
@accept     # Or: @accept('text/html')
def index():
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    app.logger.debug('%s %s ', timestamp, request.full_path);
    return '<p>Hello, World</p>'

@index.accept('application/json')
def index_json():
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    app.logger.debug('%s %s ', timestamp, request.full_path);
    return jsonify({"message":"Hello, World"})

@index.accept('text/plain')
def index_text():
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    app.logger.debug('%s %s ', timestamp, request.full_path);
    return 'Hello, World', 200, {'Content-Type': 'text/plain'}


app.run(host='localhost', port=8000, debug=option)
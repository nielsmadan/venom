import vim

_BUF_STR_OPTS = set(('buftype',))

class extbuffer(object):
    def __init__(self, vimbuf):
        self._buf = vimbuf

    def __setattr__(self, name, val):
        if name in _BUF_STR_OPTS:
            vim.eval('setbufvar(%s, "&%s", "%s")' % (self._buf.number, name, val))
        else:
            super(extbuffer, self).__setattr__(name, val)


vim.extbuffer = extbuffer

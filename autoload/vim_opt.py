import vim

_BOOL_OPTS = set(('allowrevins', 'altkeymap', 'antialias', 'autochdir', 'arabic', 'arabicshape',
                  'autoindent', 'autoread', 'autowrite', 'backup', 'ballooneval'))

_NUM_OPTS = set(('aleph', 'balloondelay'))

_STR_OPTS = set(('ambiwidth', 'background', 'backspace', 'backupcopy', 'backupdir', 'backupext',
                 'backupskip', ))


class _opt(object):
    def __getattr__(self, name):
        print "TRYING TO GET %s" % name
        if name in _BOOL_OPTS:
            return vim.eval('&%s' % name) == '1'

    def __setattr__(self, name, val):
        print "TRYING TO SET %s TO %s" % (name, val)
        if name in _BOOL_OPTS:
            if val:
                vim.command('set %s' % name)
            else:
                vim.command('set no%s' % name)


vim.opt = _opt()
vim.opt.number = True
print vim.opt.number
vim.opt.number = False
print vim.opt.number

print "VIM OPT LOADED"

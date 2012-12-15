import vim

_BOOL_OPTS = set(('allowrevins', 'altkeymap', 'antialias', 'autochdir', 'arabic', 'arabicshape',
                  'autoindent', 'autoread', 'autowrite', 'backup', 'ballooneval', 'binary',
                  'bioskey', 'bomb', 'buflisted', 'buftype', 'cindent', 'compatible', 'confirm',
                  'conskey', 'copyindent', 'cscoperelative', 'cscopetag', 'cscopeverbose',
                  'cursorbind', 'cursorcolumn', 'cursorline', 'delcombine', 'diff', 'digraph'))

_NUM_OPTS = set(('aleph', 'balloondelay', 'cmdheight', 'cmdwinheight', 'columns', 'concellevel',
                 'cscopepathcomp', 'cscopetagorder'))

_STR_OPTS = set(('ambiwidth', 'background', 'backspace', 'backupcopy', 'backupdir', 'backupext',
                 'backupskip', 'balloonexpr', 'breakat', 'browsedir', 'bufhidden', 'casemap',
                 'cdpath', 'cedit', 'charconvert', 'cinkeys', 'cinoptions', 'cinwords',
                 'clipboard', 'colorcolumn', 'comments', 'commentstring', 'complete',
                 'completefunc', 'completeopt', 'concealcursor', 'cpoptions', 'cryptmethod',
                 'cscopeprg', 'cscopequickfix', 'debug', 'define', 'dictionary', 'diffexpr',
                 'diffopt', 'directory', 'display', 'eadirection'))


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

import vim

_BOOL_OPTS = set(('allowrevins', 'altkeymap', 'antialias', 'autochdir', 'arabic', 'arabicshape',
                  'autoindent', 'autoread', 'autowrite', 'backup', 'ballooneval', 'binary',
                  'bioskey', 'bomb', 'buflisted', 'buftype', 'cindent', 'compatible', 'confirm',
                  'conskey', 'copyindent', 'cscoperelative', 'cscopetag', 'cscopeverbose',
                  'cursorbind', 'cursorcolumn', 'cursorline', 'delcombine', 'diff', 'digraph',
                  'edcompatible', 'endofline', 'equalalways', 'equalprg', 'errorbells', 'esckeys',
                  'expandtab', 'exrc', 'fkmap', 'foldenable', 'fsync', 'gdefault', 'guipty',
                  'hidden', 'hlsearch', 'hkmap', 'hkmapp', 'icon', 'ignorecase', 'imcmdline', 'imdisable',
                  'incsearch', 'infercase', 'insertmode', 'joinspaces', 'lazyredraw', 'linebreak', 'lisp',
                  'list', 'loadplugins', 'macatsui', 'magic', 'modeline', 'modifiable', 'modified',
                  'more', 'mouse', 'mousefocus', 'mousehide', 'number', 'opendevice', 'paste',
                  'preserveindent', 'previewwindow', 'prompt', 

                  ))

_NUM_OPTS = set(('aleph', 'balloondelay', 'cmdheight', 'cmdwinheight', 'columns', 'concellevel',
                 'cscopepathcomp', 'cscopetagorder', 'foldcolumn', 'foldlevel', 'foldlevelstart',
                 'foldminlines', 'foldnestmax', 'guiheadroom', 'history', 'iminsert', 'imsearch',
                 'laststatus', 'lines', 'linespace', 'matchtime', 'maxcombine', 'maxfuncdepth',
                 'maxmem', 'maxmempattern', 'maxmemtot', 'menuitems', 'modelines', 'mousetime',
                 'mzquantum', 'numberwidth', 'previewheight', 'pumheight', 

                 ))

_STR_OPTS = set(('ambiwidth', 'background', 'backspace', 'backupcopy', 'backupdir', 'backupext',
                 'backupskip', 'balloonexpr', 'breakat', 'browsedir', 'bufhidden', 'casemap',
                 'cdpath', 'cedit', 'charconvert', 'cinkeys', 'cinoptions', 'cinwords',
                 'clipboard', 'colorcolumn', 'comments', 'commentstring', 'complete',
                 'completefunc', 'completeopt', 'concealcursor', 'cpoptions', 'cryptmethod',
                 'cscopeprg', 'cscopequickfix', 'debug', 'define', 'dictionary', 'diffexpr',
                 'diffopt', 'directory', 'display', 'eadirection', 'encoding', 'errorfile',
                 'errorformat', 'eventignore', 'fileencoding', 'fileencodings', 'fileformat',
                 'fileformats', 'filetype', 'fillchars', 'foldclose', 'foldexpr', 'foldignore',
                 'foldmarker', 'foldmethod', 'foldopen', 'foldtext', 'formatoptions',
                 'formatlistpat', 'formatprg', 'formatexpr', 'grepformat', 'grepprg',
                 'guicursor', 'guifont', 'guifontset', 'guifontwide', 'guioptions',
                 'guitablabel', 'guitabtooltip', 'helpfile', 'helpheight', 'helplang',
                 'highlight', 'iconstring', 'imactivatekey', 'include', 'includeexpr', 'indentexpr',
                 'indentkeys', 'isfname', 'isindent', 'iskeyword', 'isprint', 'key', 'keymap',
                 'keymodel', 'keywordprg', 'langmap', 'langmenu', 'lispwords', 'listchars',
                 'makeef', 'makeprg', 'matchpairs', 'mkspellmem', 'mousemodel', 'mouseshape', 
                 'nrformats', 'omnifunc', 'operatorfunc', 'osfiletype', 'paragraphs', 'pastetoggle',
                 'patchexpr', 'patchmode', 'path', 'printdevice', 'printencoding', 'printexpr',
                 'printfont', 'printheader', 'printmbcharset', 'printmbfont', 'printoptions', 
                 'quoteescape', 

                 ))


class _opt(object):
    def __getattr__(self, name):
        # print "TRYING TO GET %s" % name
        if name in _BOOL_OPTS:
            return vim.eval('&' + name) == '1'
        elif name in _NUM_OPTS:
            return int(vim.eval('&' + name), 0)
        elif name in _STR_OPTS:
            return vim.eval('&' + name)

    def __setattr__(self, name, val):
        # print "TRYING TO SET %s TO %s" % (name, val)
        if name in _BOOL_OPTS:
            if val:
                vim.command('set %s' % name)
            else:
                vim.command('set no%s' % name)


vim.opt = _opt()

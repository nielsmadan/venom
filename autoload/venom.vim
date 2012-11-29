if exists('g:venom_sourced') || &cp
    finish
endif
let g:venom_sourced = 1

function! venom#Load()
    if exists('g:venom_loaded')
        return
    endif
    let g:venom_loaded = 1

py << END_PY
import vim

class venom(object):
    @staticmethod
    def include_guard(name):
        res = vim.eval("exists('g:%s') || &cp") == '0'
        vim.command("let g:%s = 1" % name)
        return res

vim.venom = venom
END_PY

echom "VENOM LOADED"
endfunction

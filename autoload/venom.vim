if exists('g:venom_sourced') || &cp
    finish
endif
let g:venom_sourced = 1

let s:sfile = expand("<sfile>")

function! venom#Import(sfile, module_name)
py << END_PY
import vim
import os
import sys

sys.path.append(os.path.dirname(vim.eval("a:sfile")))

if vim.eval("a:module_name") not in globals():
    globals()[vim.eval("a:module_name")] = __import__(vim.eval("a:module_name"))

sys.path.remove(os.path.dirname(vim.eval("a:sfile")))
END_PY
endfunction

function! venom#Load()
    if exists('g:venom_loaded')
        return
    endif
    let g:venom_loaded = 1

    call venom#Import(s:sfile, "venom")
endfunction

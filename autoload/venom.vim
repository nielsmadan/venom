if exists('g:venom_sourced') || &cp
    finish
endif
let g:venom_sourced = 1

let s:sfile = expand("<sfile>")

function! venom#Load()
    if exists('g:venom_loaded')
        return
    endif
    let g:venom_loaded = 1

py << END_PY
import sys

sys.path.append(os.path.dirname(vim.eval("s:sfile")))

import venom

sys.path.remove(os.path.dirname(vim.eval("s:sfile")))
END_PY
endfunction

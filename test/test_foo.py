import flexmock

import vim_stub

import vim

import autoload.venom as venom


def test_nnoremap():
    flexmock.flexmock(vim)
    vim.should_receive("command").with_args("nnoremap <c-c> :py venom.fn_proxy[0]()<CR>").once

    venom.nnoremap("<c-c>", lambda x: x)

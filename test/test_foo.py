import sys
import types

import flexmock

dummy_vim = types.ModuleType('Dummy Vim Module', "Dummy")

sys.modules['vim'] = dummy_vim

import vim
vim.command = lambda x: x

import autoload.venom as venom


def test_nnoremap():
    flexmock.flexmock(vim)
    vim.should_receive("command").with_args("nnoremap <c-c> :py venom.fn_proxy[0]()<CR>")

    venom.nnoremap("<c-c>", lambda x: x)

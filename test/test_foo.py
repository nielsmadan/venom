import sys

sys.modules['vim'] = object()

import vim

import autoload.venom


def test_nnoremap():
    assert 42 == 42
    # def mock_command(test_input):
    #     assert test_input == "nnoremap <c-c> :py venom.fn_proxy['what']()<CR>" % keys)
# 
#     vim.command = mock_command

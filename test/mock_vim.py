import sys
import types

if 'vim' not in sys.modules:
    dummy_vim = types.ModuleType('Dummy Vim Module', "Dummy")
    sys.modules['vim'] = dummy_vim

    import vim
    vim.command = lambda *args, **kwargs: None
    vim.eval = lambda *args, **kwargs: None

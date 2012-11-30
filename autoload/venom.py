import sys
import os

import vim


fn_proxy = {}


def include_guard(name):
    res = vim.eval("exists('g:%s') || &cp") == '0'
    vim.command("let g:%s = 1" % name)
    return res


def run(sfile, module_name):
    sys.path.append(os.path.dirname(sfile))

    __import__(module_name)

    sys.path.remove(os.path.dirname(sfile))


def add_path(sfile):
    sys.path.append(os.path.dirname(sfile))


def rm_path(sfile):
    sys.path.remove(os.path.dirname(sfile))


def nnoremap(keys, fn):
    fn_proxy["what"] = fn
    vim.command("nnoremap %s :py venom.fn_proxy['what']()<CR>" % keys)

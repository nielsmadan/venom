import sys
import os

import vim
import vim_opt
import vim_g
import vim_fn
import vim_map


fn_proxy = {}
PROXY_INDEX = 0
wrap_proxy = {}
WRAP_INDEX = 0


def include_guard(name):
    res = vim.eval("exists('g:%s') || &cp") == '0'
    vim.command("let g:%s = 1" % name)
    return res


def import_py(sfile, module_name):
    sys.path.append(os.path.dirname(sfile))

    __import__(module_name)

    sys.path.remove(os.path.dirname(sfile))


def add_path(sfile):
    sys.path.append(os.path.dirname(sfile))


def rm_path(sfile):
    sys.path.remove(os.path.dirname(sfile))


def py_fn_to_vim_function(vimscript_fn_name, py_fn):
    global WRAP_INDEX
    wrap_proxy[WRAP_INDEX] = py_fn
    vim.command("function! g:%s()\npy venom.wrap_proxy[%d]()\nendfunction" % (vimscript_fn_name, WRAP_INDEX))
    WRAP_INDEX += 1


def py_fn_to_vim_command(command_name, py_fn, allow_range=False):
    args = ""
    if allow_range:
        print "ADDING RANGE"
        args += "-range"
    global WRAP_INDEX
    wrap_proxy[WRAP_INDEX] = py_fn
    vim.command("command! %s %s :py venom.wrap_proxy[%d]()" % (args, command_name, WRAP_INDEX))
    WRAP_INDEX += 1


def _create_mapping_fn(map_cmd):
    def _inner_map(keys, fn):
        global PROXY_INDEX
        fn_proxy[PROXY_INDEX] = fn
        vim.command("%s %s :py venom.fn_proxy[%d]()<CR>" % (map_cmd, keys, PROXY_INDEX))
        PROXY_INDEX += 1

    return _inner_map

noremap = _create_mapping_fn("noremap")
nnoremap = _create_mapping_fn("nnoremap")
inoremap = _create_mapping_fn("inoremap")
vnoremap = _create_mapping_fn("vnoremap")
xnoremap = _create_mapping_fn("xnoremap")


# class pos(object):
#     def __init__(self, line, col):
#         self.line = line
#         self.col = col


def get_selection_coords():
    start_line, start_col = vim.eval("getpos(\"'<\")")[1:3]
    end_line, end_col = vim.eval("getpos(\"'>\")")[1:3]

    return ((int(start_line) - 1, int(start_col) - 1), (int(end_line) - 1, int(end_col) - 1))


def get_visual_selection(read_only=False):
    ((start_line, start_col), (end_line, end_col)) = get_selection_coords()
    if read_only:
        buf = vim.current.buffer
        if start_line == end_line:
            return [buf[start_line][start_col:end_col + 1]]
        elif start_line + 1 == end_line:
            return [buf[start_line][start_col:]] + [buf[end_line][:end_col + 1]]
        else:
            return [buf[start_line][start_col:]] + buf[start_line + 1:end_line] + [buf[end_line][:end_col + 1]]


def get_current_line(read_only=True):
    if read_only:
        return vim.eval('getline(".")')

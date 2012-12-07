import sys
import os

import vim


fn_proxy = {}
PROXY_INDEX = 0


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


def _create_mapping_fn(map_cmd):
    def _inner_map(keys, fn):
        global PROXY_INDEX
        fn_proxy[PROXY_INDEX] = fn
        vim.command("nnoremap %s :py venom.fn_proxy[%d]()<CR>" % (keys, PROXY_INDEX))
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
# 
# 
# def get_selection_coords():
#     start_line, start_col = vim.eval("getpos('v')")[1:3]
#     end_line, end_col = vim.eval("getpos('.')")[1:3]
# 
#     if start_line < end_line or (start_line == end_line and start_col < end_col):
#         return ((start_line, start_col), (end_line, end_col))
#     else:
#         return ((end_line, end_col), (start_line, start_col))
# 
# 
# def get_visual_selection():
#     print get_selection_coords()

import vim


class _highlight(object):
    def highlight_line(self, line, group):
        vim.eval("matchadd('%s', '\\%%%sl')" % (group, line))

    def highlight_region(self, start_line, end_line, start_col, end_col):
        pass

vim.highlight = _highlight()

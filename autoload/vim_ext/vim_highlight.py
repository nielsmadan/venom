import vim


class _highlight(object):
    def highlight_line(self, line, group):
        vim.eval("matchadd('%s', '\\%%%sl')" % (group, line))

    def highlight_lines(self, start_line, end_line, group):
        vim.eval("matchadd('%s', '\\%%>%sl\\%%<%sl')" % (group, first_line - 1, last_line + 1))

    def highlight_section(self, start_line, end_line, start_col, end_col, group):
        vim.eval("matchadd('%s', '\\%%>%sl\\%%<%sl\\%%>%sc\\%%<%sc')" %
                    (group, start_line - 1, end_line + 1, start_col - 1, end_col + 1))

    def highlight_region(self, start_line, end_line, start_col, end_col):
        pass

vim.highlight = _highlight()

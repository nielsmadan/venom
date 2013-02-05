import vim


class _fn(object):
    #CURSOR AND MARK FUNCTIONS
    def cursor_column(self):
        """Get the column number of the cursor."""
        return int(vim.eval('col(".")')) - 1

    def mark_column(self, mark_name):
        """Get the column number of a mark."""
        return int(vim.eval('col("\'%s")' % mark_name)) - 1

    def line_column_len(self, line_nr=None):
        """Get the number of columns of line line_nr."""
        if line_nr is None:
            return int(vim.eval('col("$")')) - 1
        else:
            return int(vim.eval('col([%d, "$"])' % line_nr)) - 1

    def cursor_virt_column(self):
        """Get the screen column number of the cursor."""
        return int(vim.eval('virtcol(".")')) - 1

    def mark_virt_column(self, mark_name):
        """Get the screen column number of a mark."""
        return int(vim.eval('virtcol("\'%s")' % mark_name)) - 1

    def line_virt_column_len(self, line_nr=None):
        """Get the number of screen columns of line line_nr."""
        if line_nr is None:
            return int(vim.eval('virtcol("$")')) - 1
        else:
            return int(vim.eval('virtcol([%d, "$"])' % line_nr)) - 1


    def exists(self, name):
        return vim.eval('exists("%s")' % name) == "1"

    def input(self, prompt, default='', comletion_type=None):
        return vim.eval('input("%s", "%s")' % (prompt, default))

vim.fn = _fn()

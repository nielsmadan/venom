import vim


class _map(object):
    def nnoremap(self, lhs, rhs):
        return vim.command('nnoremap %s %s' % (lhs, rhs))

    def vnoremap(self, lhs, rhs):
        return vim.command('vnoremap %s %s' % (lhs, rhs))

    def inoremap(self, lhs, rhs):
        return vim.command('inoremap %s %s' % (lhs, rhs))

    def xnoremap(self, lhs, rhs):
        return vim.command('xnoremap %s %s' % (lhs, rhs))

    def noremap(self, lhs, rhs):
        return vim.command('noremap %s %s' % (lhs, rhs))

vim.map = _map()

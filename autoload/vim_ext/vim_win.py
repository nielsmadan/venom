import vim


class _win(object):
    def new(self, win_height=None):
        vim.command('new')

    def hnew(self, win_height=None):
        vim.command('new')

    def vnew(self, win_height=None):
        vim.command('vnew')


vim.win = _win()

import vim


class _win(object):
    def new(self, win_height=None):
        #TODO: Do it according to 'her' or 'ver'
        vim.command('new')

    def hnew(self, win_height=None):
        #TODO IGNORE 'ver' option
        vim.command('new')

    def vnew(self, win_height=None):
        #TODO IGNORE 'hor' option
        vim.command('vnew')


vim.win = _win()

import vim


class _registers(object):
    def __getattr__(self, name):
        return self.get(name)

    def __setattr__(self, name, val):
        self.set(name, val)

    def get(self, name):
        return vim.eval("@%s" % name)

    def set(self, name, val):
        if isinstance(val, int) or isinstance(val, float):
            vim.command('let @%s=%s' % (name, val))
        else:
            vim.command('let @%s="%s"' % (name, val))

    def copy(self, reg_from, reg_to):
        vim.command('let @%s=@%s' % (reg_to, reg_from))


vim.registers = _registers()

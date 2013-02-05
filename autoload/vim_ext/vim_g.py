import vim


class _g(object):
    def __getattr__(self, name):
        return vim.eval("g:%s" % name)

    def __setattr__(self, name, val):
        vim.command("let g:%s=%s" % (name, val))

    def __contains__(self, name):
        return vim.fn.exists("g:" + name)

vim.g = _g()

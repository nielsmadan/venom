import vim


class _fn(object):
    def exists(self, name):
        # print "CHECKING FOR %s" % name
        return vim.eval('exists("%s")' % name) == "1"

vim.fn = _fn()

import unittest

import flexmock

import mock_vim

import vim

vim.command = lambda *args, **kwargs: None

import autoload.venom as venom


class VimOption(unittest.TestCase):
    def setUp(self):
        flexmock.flexmock(vim)

    def test_set_bool_option_true(self):
        vim.should_receive("command").with_args("set number").once

        vim.opt.number = True

    def test_set_bool_option_false(self):
        vim.should_receive("command").with_args("set nonumber").once

        vim.opt.number = False

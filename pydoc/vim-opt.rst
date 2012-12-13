Vim Options
===========

Venom allows setting and reading vim options in python through the `vim.opt` add-in interface. Any option from the
`official vim documentation`_ can be set. Boolean options take `True` or `False` parameters, number options take
numbers and string options take strings.

Example::

    vim.opt.number = True                    # show line numbers
    print vim.opt.number                     # prints 'True'
    vim.opt.number = not vim.opt.number      # toggle options, number is now 'False'

Vim includes a stupendous amount of options, many of which are pretty niche. So here is a non-authoritative list
of the more generally useful options to give you a quick idea of what's available.

* **autochdir**: automatically change dir to dir of file associated with current buffer.
* **autoindent**: copy indent from current line when starting a new line.
* **autoread**: update buffer automatically if file has changed outside of vim.
* **autowrite**: automatically write a buffer to file on certain actions.
* **autowriteall**: automatically write all buffers on leaving vim.
* **backspace**: set backspace to move over indents, eols and start of insert (whatever that means).
* **balloondelay**: delay in msecs until balloon pops up.
* **autoread**: update file automatically
* **autoread**: update file automatically
* **autoread**: update file automatically
* **autoread**: update file automatically



And here is another list of intriguing but not immediately useful options.

* **allowrevins**: 

.. _official vim documentation: http://vimdoc.sourceforge.net/htmldoc/options.html#option-summary

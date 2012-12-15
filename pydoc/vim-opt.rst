Vim Options
===========

Venom allows setting and reading vim options in python through the `vim.opt` add-in interface. Any option from the
`official vim documentation`_ can be set. Boolean options take `True` or `False` parameters, number options take
numbers and string options take strings.

Example::

    vim.opt.number = True                    # show line numbers
    print vim.opt.number                     # prints 'True'
    vim.opt.number = not vim.opt.number      # toggle options, number is now 'False'

Vim includes a stupendous amount of options, many of which are somewhat niche or not useful for writing plugins. So here is a non-authoritative list
of the more generally useful options to give you a quick idea of what's available.

* **autochdir**: automatically change dir to dir of file associated with current buffer.
* **autoindent**: copy indent from current line when starting a new line.
* **autoread**: update buffer automatically if file has changed outside of vim.
* **autowrite**: automatically write a buffer to file on certain actions.
* **autowriteall**: automatically write all buffers on leaving vim.
* **backspace**: set backspace to move over indents, eols and start of insert (whatever that means).
* **balloondelay**: delay in msecs until balloon pops up.
* **ballooneval**: display debug information in pop up. (`see here
  <http://vimdoc.sourceforge.net/htmldoc/debugger.html#balloon-eval>`_)
* **balloonexpr**: interface to ballooneval.
* **binary**: for editing binary files.
* **breakat**: choose which characters to linebreak on.
* **browsedir**: choose which dir to use for the file browser.
* **bufhidden**: what to do when a buffer is not shown in a window any more.
* **buflisted**: choose to show (or not to show) a buffer in the buffer list.
* **buftype**: set the type of buffer (e.g. 'nowrite', 'quickfix', etc.)
* **casemap**: how to change the case of letters
* **cdpath**: which directories to search when using :cd and :lcd.
* **clipboard**: clipboard options.
* **cmdheight**: number of lines to use for command-line.
* **cmdwinheight**: number of lines to use for command line window.
* **colorcolumn**: where to draw color columns.
* **columns**: number of columns, window width in gvim.
* **complete**: specify how insert completion works.
* **completefunc**: specify function for insert completion.
* **completeopt**: options for insert completion.
* **cursorbind**: cursor in current window moves other cursorbound windows.
* **cursorcolumn**: highlight column cursor is in.
* **cursorline**: highlight line cursor is in.
* **debug**: options for more verbose errors.
* **dictionary**: file names to look up words for keyword completion.
* **diff**: add current window to diffing window group.
* **diffopt**: options for diff mode.
* **asdf**: update file automatically
* **asdf**: update file automatically

And here is another list of the intriguing but not immediately useful options. These two lists should cover every
options there is (according to the official docs).

* **aleph**: for Hebrew mode.
* **allowrevins**: how to get into reverse insert mode.
* **altkeymap**: second language is Farsi.
* **ambiwidth**: what to do with characters where the width is ambiguous.
* **antialias**: font anti aliasing on the Mac.
* **arabic**: set this to edit Arabic text.
* **arabicshape**: visual corrections for Arabic characters.
* **background**: 'dark' or 'light' background color.
* **backup**: make back up before overwriting a file.
* **backupcopy**: how to make a backup.
* **backupdir**: where to make a backup.
* **backupext**: string to append to backup file name.
* **backupskip**: which files not to back up.
* **bioskey**: call bios to obtain a keyboard character.
* **bomb**: prepend byte order mark to file.
* **cedit**: key used to open command line window in command mode.
* **charconvert**: expression for character encoding conversion.
* **cindent**: enable indentation for C.
* **cinkeys**: what keys to re-indent on if cindent is enabled.
* **cinoptions**: how to cindent.
* **cinwords**: words that start extra indent on next line.
* **comments**: characters that can start a comment line.
* **commentstring**: template for comments for folding.
* **compatible**: make vim more vi compatible.
* **concealcursor**: set modes in which text in the cursor line can be concealed.
* **conceallevel**: how to show concealed text.
* **confirm**: raise dialog to confirm saving.
* **conskey**: use direct console I/O to obtain keyboard characters (see bioskey).
* **copyindent**: copy structure of existing lines when auto indenting.
* **cpoptions**: when to be vi compatible.
* **cryptmethod**: method to use to encrypt when writing encrypted file.
* **cscopepathcomp**: how many components of path to show.
* **cscopeprg**: specify command to execute cscope.
* **cscopequickfix**: show cscope results in quickfix.
* **cscoperelative**: use basename of cscope.out path as prefix.
* **cscopetag**: use cscope for tag commands.
* **cscopetagorder**: specify order in which :cstag performs search.
* **cscopeverbose**: give message when adding database.
* **define**: pattern to use to find macro definitions.
* **delcombine**: in unicode, option to delete combined character.
* **diffexpr**: expression to evaluate to get ed-style diff file.
* **digraph**: enable entering of digraphs in insert mode.
* **directory**: list of dir names for the swap file.
* **display**: how to display a last line that does not fit.
* **asdf**: prepend byte order mark to file.
* **asdf**: prepend byte order mark to file.
* **asdf**: prepend byte order mark to file.

.. _official vim documentation: http://vimdoc.sourceforge.net/htmldoc/options.html#option-summary

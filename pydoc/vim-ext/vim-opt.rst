Vim Options
===========

Venom allows setting and reading vim options in python through the ``vim.opt`` add-in interface. Any option from the
`official vim documentation`_ can be set. Boolean options take ``True`` or ``False`` parameters, number options take
numbers and string options take strings.

Example::

    vim.opt.number = True                    # show line numbers
    print vim.opt.number                     # prints 'True'
    vim.opt.number = not vim.opt.number      # toggle options, number is now 'False'

Summary of Useful Options
-------------------------

Vim includes a stupendous amount of options, many of which are somewhat niche or not useful for writing plugins. So here is a non-authoritative list
of the more generally useful options to give you a quick idea of what's available. Before using any of these, you
should read the full full documentation. This list is intended just as a high level overview.

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
* **eadirection**: option when equalalways applies.
* **encoding**: character encoding used inside vim.
* **equalalways**: automatically make windows same size.
* **equalprg**: external program to use for '=' command.
* **errorfile**: name of errorfile for quickfix mode.
* **errorformat**: Scanf-like description of format of error file.
* **eventignore**: list of event names to ignore.
* **expandtab**: replace tabs with spaces.
* **fileencoding**: set character encoding for file in buffer.
* **fileformat**: give the end of line for the current buffer.
* **filetype**: manually set filetype.
* **fillchars**: characters to use to fill separators, foldtext markers.
* **formatoptions**: options for automatic formatting.
* **formatlistpat**: how to recognize a list header for automatic formatting.
* **formatprg**: program to use for the 'gq' operator.
* **formatexpr**: used to format a range of lines with 'gq' operator.
* **grepformat**: scanf like format to use for grep output.
* **grepprg**: program to use for grep command.
* **guicursor**: change look of cursor in different modes.
* **guifont**: list of fonts to try in gvim.
* **guitablabel**: text to display in the gui tab pages line.
* **highlight**: set highlighting mode.
* **hlsearch**: when there is a previous search pattern, highlight all matches.
* **ignorecase**: ignore case in search and tags.
* **include**: pattern to be used to find an include command with "[i" or "]I".
* **includeexpr**: expression to be used to transform include statement to filename.
* **incsearch**: show matched pattern while typing a search.
* **indentexpr**: expression used to obtain proper indent of a line.
* **indentkeys**: keys used to indenting in insert mode.
* **isfname**: characters to include in file and path names (e.g. for 'gf' command).
* **isindent**: characters to include for identifiers.
* **iskeyword**: characters to include in keywords.
* **isprint**: characters to display directly on screen. 
* **key**: key that is used to encrypting the current buffer.
* **keymap**: name of a keyboard mapping.
* **keywordprg**: program to use to lookup keyword under cursor ('K' command).
* **laststatus**: when to show status line on last window.
* **lazyredraw**: redraw while executing macros / registers / other commands
* **linebreak**: wrap long lines only at character in 'breakat' (only affect display).
* **lines**: number of lines of Vim window.
* **linespace**: number of pixel lines inserted between characters.
* **list**: show whitespace.
* **listchars**: characters used to display whitespace.
* **magic**: change special characters in regex patterns.
* **makeef**: name of error file for make command.
* **makeprg**: program to use for make command.
* **matchpairs**: characters that form pairs for '%' command.
* **matchtime**: tenths of second to show matching paren for 'showmatch'.
* **modifiable**: allow changing of buffer contents (and setting fileformat / fileencoding).
* **modified**: consider buffer to have been modified.
* **number**: print line numbers in front of each line.
* **numberwidth**: minimum number of columns for number column.
* **omnifunc**: function to use for insert mode omni completion.
* **operatorfunc**: function to be called with 'g@'.
* **paragraphs**: specify the nroff macros that separate paragraphs.
* **paste**: enable paste mode to make pasting more sensible (especially in terminal).
* **pastetoggle**: mapping to use to toggle paste.
* **patchexpr**: expression to evaluate when applying a patch.
* **patchmode**: create a backup when first writing a file.
* **path**: paths to search for relative path files.
* **previewheight**: default height for preview window.
* **previewwindow**: set a window to be the preview window (usually not set directly).
* **prompt**: use ':' prompt in Ex mode.
* **pumheight**: maximum number of items to show in pop-up for insert mode completion.
* **quoteescape**: characters that are used to escape quotes in a string.
* **asdf**:

Folding
```````

* **foldclose**: automatic fold closing when cursor is not in them.
* **foldcolumn**: show column at the side of window indicating open / closed folds.
* **foldenable**: enable folding.
* **foldexpr**: expression used when foldmethod is expr.
* **foldignore**: pattern for lines to get their foldlevel from surrounding lines.
* **foldlevel**: set the foldlevel.
* **foldlevelstart**: set foldlevel when starting to edit a buffer.
* **foldmarker**: start and endmarker when using foldmethod marker.
* **foldmethod**: foldmethod for current window.
* **foldminlines**: number of screen lines above which a fold can be displayed closed.
* **foldnestmax**: maximum nesting of folds.
* **foldopen**: specify for which commands folds will be opened.
* **foldtext**: text to display for folded text.

Summary of Maybe-not-so-useful Options
--------------------------------------

And here is another list of the intriguing but not immediately useful options for writing plugins.
These two lists should cover every options there is (according to the official docs).

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
* **edcompatible**: make substitute work like in ed.
* **endofline**: write end of line at end of file.
* **errorbells**: beep or screen flash on errors.
* **esckeys**: Function keys are recognized in insert mode.
* **exrc**: enable reading of rc files in current directory.
* **fileencodings**: list of character encodings to consider when opening a file.
* **fileformats**: end of line characters to try when opening a buffer.
* **fkmap**: map for farsi.
* **fsync**: use fsync to ensure data is written to disk (on by default).
* **gdefault**: default to substituting all matches on a line with :substitute.
* **guifontset**: specifies two fonts, one for English, one for another language.
* **guifontwide**: list of fonts to be used for double width characters.
* **guiheadroom**: number of pixels to leave at the top when fitting the gui window on screen.
* **guioptions**: options to load gui components and gui behavior.
* **guipty**: try to use pseudo-tty for shell commands (default on).
* **guitabtooltip**: tooltip for gui tab pages line.
* **helpfile**: file path to main help file.
* **helpheight**: minimal initial height of help window.
* **helplang**: list of desired languages for help.
* **hidden**: abandon buffer when unloading.
* **history**: how many commands / searches to remember.
* **hkmap**: map for Hebrew character set.
* **hkmapp**: use phonetic keyboard mapping.
* **icon**: set window icon.
* **imactivatekey**: specify key used by X-Windows for Input Method (IM) activation.
* **imcmdline**: Input Method is always on when editting a command line.
* **imdisable**: never use Input Method.
* **iminsert**: use :lmap or Input Method in Insert mode.
* **imsearch**: use :lmap or Input Method when entering a search pattern.
* **infercase**: change letter cases of match when doing keyword completion with ignorecase.
* **insertmode**: make insert mode the default.
* **joinspaces**: add two spaces when joining lines that end with a '.', '?', or '!'.
* **keymodel**: possibility to have a shifted key (cursors, <End>, <PageUp>, etc.) start visual mode.
* **langmap**: switch key into a special language mode.
* **langmenu**: language to use for menu translation.
* **lisp**: enable lisp indentation in insert mode.
* **listwords**: words that influence lisp indenting.
* **loadplugins**: enable loading of plugins.
* **macatsui**: workaround for drawing problems
* **maxcombine**: maximum number of combined characters for displaying (in utf-8).
* **maxfuncdepth**: maximum depth of function calls for user defined functions.
* **maxmapdepth**: maximum number of mappings (in circular maps for example).
* **maxmem**: maximum amount of memory to be used for one buffer.
* **maxmempattern**: maximum amount of memory used for pattern matching.
* **maxmemtot**: maximum amount of memory to be used for all buffers.
* **menuitems**: maximum number of menu items for menus generated from lists (e. g. list of buffers).
* **mkspellmem**: set when to start compressing word tree (for languages with lots of words).
* **modeline**: enable modelines (setting vim options inside files).
* **modelines**: number of lines to check at the beginning and end of files for modelines.
* **more**: pause listings and show more-prompt when screen is filled.
* **mouse**: enable use of mouse in terminals.
* **mousefocus**: automatically activate window that the mouse pointer is in.
* **mousehide**: hide mouse pointer when characters are typed.
* **mousemodel**: set what the right mouse button is used for.
* **mouseshape**: set the shape of the mouse in different modes.
* **mousetime**: time between mouse clicks for double-click.
* **mzquantum**: msecs between polls of MzScheme threads.
* **nrformats**: what vim considers numbers for CTRL-A and CTRL-X commands.
* **opendevice**: enable reading and writing from devices.
* **osfiletype**: deprecated option for RISC OS.
* **preserveindent**: when changing indent of the current line, re-use whatever whitespace is available to get to the new indentation.
* **asdf**:

Printing
````````
* **printdevice**: device to use for printing.
* **printencoding**: character encoding to use for printing.
* **printexpr**: expression to be used to print the PostScript.
* **printfont**: font to use for printing.
* **printheader**: format for header for prints.
* **printmbcharset**: CJK character set to be used for CJK output.
* **printmbfont**: list of fonts to be used for CJK output.
* **printoptions**: list of format options for printing.


.. _official vim documentation: http://vimdoc.sourceforge.net/htmldoc/options.html#option-summary

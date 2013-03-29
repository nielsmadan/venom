venom
=====

This is a possibly crazy project to extend the python interface of vim to the point where it's possible to write
plugins in pure python (without using eval or command or knowing any vimscript, really) and then extend it further to
provide functionality that's needed by many plugins.

The current plan is:

1. write a plugin using venom.
2. extend venom to support the functionality of the plugin (in the develop branch).
3. once the plugin is done, merge develop into master and fixup all other plugins.
4. repeat until venom is done.

List of completed plugins:

* [mercury](https://github.com/nielsmadan/mercury): execute any fragment of code directly from vim.

List of plugins in development:

* [yankee](https://github.com/nielsmadan/yankee): vim yank manager.

Find the full (work-in-progress) documentation [here](https://nielsmadan.github.com/venom).

Current stable version is 0.1. You're welcome to play around with it, but it's probably going to change a lot.

### Links

You can also get this plugin at [vim.org](http://www.vim.org/scripts/script.php?script_id=4491).
    
[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/9827ba0171e58b1ba399f7913e6e8307 "githalytics.com")](http://githalytics.com/nielsmadan/venom)

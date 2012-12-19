venom
=====

Vimscript is a finnicky, low-level, homely pain in the neck that's hard to test and troubleshoot, and impossible to debug.
Most vim distributions have python compiled in and provide an interface, but it's so limited that you will probably
be forced to either drop back into vimscript or eval little bits of it throughout your code.

`venom` aims to fix this. Its goals are:

* extend the python interface to cover all scripting functionality (without eval) and make it possible to write
  a plugin in 100% pure python.
* provide a set of higher level functions and objects to make it easier to perform common vim plugin tasks.
* have excellent documentation that covers the interface, as well as how to set up a plugin (testing, debugging, code layout,
  etc.).

Writing a vimscript plugin is neither easy nor fun. We'll see if it's possible to do something about that.

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/9827ba0171e58b1ba399f7913e6e8307 "githalytics.com")](http://githalytics.com/nielsmadan/venom)

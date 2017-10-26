Click Base
==========

This is a placeholder for a Click-based command-line program in
Python. Used for coding portion of October PyYYC meetup.

To get going with this (steps expanded below):

 - prepare your checkout
 - create a virtualenv
 - install this project
 - run the tests

Prepare Your Checkout
---------------------

Clone this repository to your machine and open a shell in the
directory you cloned to. The simplest thing that can work is to open a
terminal and do this:

```
git clone https://github.com/py-yyc/click-base
cd click-base
```

Create a Virtualenv
-------------------

If you have ``virtualenv`` installed already, do this:

```
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
```

Install This Project
--------------------

Within an "activated" virtualenv (you did this in the last step if
you're folowing along) install this project as "editable". This means
that any changes you make to the code will be immediately available
when running scripts, tests etc.

```
pip install --editable .
```

You should now be able to type "yycli" and see the default help
display.


Run the Tests
-------------

We do test-driven development, so you need to be able to run the one
"placeholder" test.

```
py.test -sv test
```

This should print out some diagnostic information showing that one
test was run (and that it passed).

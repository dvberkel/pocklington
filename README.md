Pocklington
===========

[![Build Status](https://secure.travis-ci.org/dvberkel/pocklington.png?branch=master)](http://travis-ci.org/dvberkel/pocklington)

The Pocklington project aims to provide an implementation of the 
[Pocklington Primality Test](http://en.wikipedia.org/wiki/Pocklington_primality_test "Wikipedia on Pocklington's criteria").

Environment
-----------

We use 
[Python](http://www.python.org/ "Python's official homepage") to
implement the Pocklington's criteria.

In order to allow python to see the project definitions I encourage
you to add the current directory to the `PYTHONPATH`. I use the
following command for this:

    export PYTHONPATH=.

Test
----

To run all test in the project execute the command

    python pocklington/test/test_all.py
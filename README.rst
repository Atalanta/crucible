========================================================
Crucible - A Generator of Strong yet Memorable Passwords
========================================================

about
*****
`crucible <http://github.com/Atalanta/crucible>` provides a simple command-line interface which will generate passwords using a simple scheme that allows for reasonably secure, yet also reasnably memorable passwords.

The scheme is simple: locate a film (from, for example IMDB) which contains two words, and insert 3 digits between the words.  For example:

::

  Oliver762Twist

usage
*****

By default, the command will return a single password to standard out.  However, additional options are supported:

::

	Usage: crucible.py [options]

	Options:
	  -h, --help            show this help message and exit
	  -l MIN_LENGTH, --min-length=MIN_LENGTH
				Minimum length of film title
	  -n NUMBER, --number=NUMBER
				Number of passwords to generate
	  -s, --db-size         Print size of candidate database

installation
************

*on most UNIX-like systems, you'll probably need to run the following 
`install` commands as root or by using sudo*

**pip**

::

  pip install crucible 

**easy_install**

::

  easy_install crucible 

**from source**

::

  pip install -e git://github.com/Atalanta/crucible.git#egg=crucible

*or*

::

  git clone git://github.com/Atalanta/crucible.git
  cd github-cli
  python setup.py install

as a result, the ``crucible`` executable will be installed into a system ``bin`` 
directory

configuration
*************
Crucible reads its candidate films from a text file.  You can refresh this at will.

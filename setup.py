#!/usr/bin/env python2

from distutils.core import setup
from playmusicextractor import __version__

setup(name = "playmusicextractor",
      version = __version__,
      description = "Extracts MP3 files from Google Play Music offline storage (All Access)",
      author = "Anonymous",
      author_email = "",
      url = "https://github.com/wilcodex/playmusicextractor",
      license = "GNU GPLv3",
      py_modules=["playmusicextractor", "superadb"],
      scripts = ["playmusicextractor", "superadb"],
      requires = ["pycrypto", "eyed3"]
)

# MBVGrep

### Setup

Currently mvbgrep.py needs BeautifulSoup2 to be installed, you can install it via pip or easyinstall.  

~~~
usage: MVBgrep [-h] [--version] -s [Station [Station ...]]
               [-l [Line [Line ...]]] [-t [{30,60,120} [{30,60,120} ...]]]
               [--link]

Get the current tram / bus informations.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -s [Station [Station ...]], --station [Station [Station ...]]
                        the sataion name you want information about
  -l [Line [Line ...]], --line [Line [Line ...]]
                        a tram / bus number you want to filter for
  -t [{30,60,120} [{30,60,120} ...]], --time [{30,60,120} [{30,60,120} ...]]
                        how long in the future should the depature times be
                        (default: ['30'])
  --link                display the search link
~~~

### How it works

I simply parse the html from [mvbnet.de](http://www.movi.de/mvb/fgi2/index.php) with some custom parameters.  
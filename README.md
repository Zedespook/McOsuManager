### Osu!importer
This project is for those who want to use a different importer
than the one that exists in osu!

## Why would you do this?
If you are on Linux, or you want to use a different osu! client
than you would have to do everything manually. I thought it was
tedious, and that I can make a script to do importing automatically.

## Why not shell scripts, if it's going to be used mainly on Linux.
Shell scripts would be the most efficient way to do this, but I
couldn't find an archive manager which can "silently" just unzip
files from my downloads folder. Thankfully, Python has a module
which can do that, and now the script can be used on any system
assuming if that system can run Python scripts.

## How to use?
Linux/MacOS:
Since you might already have a Python runner, you just run the
`main.py` file and open up McOsu, or your normal osu! and just
start downloading maps.

Windows:
You need to download a Python enviourment from (here)[https://www.python.org/downloads/]!
After that, you can run the Python script and have fun with downloading maps!

import codecs
from distutils.core import setup
from glob import glob
import os.path as path

# Snippet taken from - http://goo.gl/BnjFzw
# It's to fix a bug for generating a Windows distribution on Linux systems.
# Linux doesn't have access to the "mbcs" encoding.
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    def wrapper(name, enc=ascii):
        return {True: enc}.get(name == 'mbcs')
    codecs.register(wrapper)

install_requires = ['nfldb>=0.0.16']
try:
    import argparse
except ImportError:
    install_requires.append('argparse')
try:
    from collections import OrderedDict
except ImportError:
    install_requires.append('ordereddict')

cwd = path.dirname(__file__)
longdesc = codecs.open(path.join(cwd, 'longdesc.rst'), 'r', 'utf-8').read()

version = '0.0.0'
with codecs.open(path.join(cwd, 'nflcmd/version.py'), 'r', 'utf-8') as f:
    exec(f.read())
    version = __version__
assert version != '0.0.0'

docfiles = glob('doc/nflcmd/*.html') + glob('doc/*.pdf') + glob('doc/*.png')

setup(
    name='nflcmd',
    author='Andrew Gallant',
    author_email='nflcmd@burntsushi.net',
    version=version,
    license='UNLICENSE',
    description='A set of commands for viewing and ranking NFL data.',
    long_description=longdesc,
    url='https://github.com/BurntSushi/nflcmd',
    classifiers=[
        'License :: Public Domain',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
    ],
    platforms='ANY',
    packages=['nflcmd', 'nflcmd/cmds'],
    data_files=[('share/doc/nflcmd',
                 ['README.md', 'longdesc.rst', 'UNLICENSE']
                ),
                ('share/doc/nflcmd/doc', docfiles),
               ],
    install_requires=install_requires,
    scripts=['scripts/nflstats']
)

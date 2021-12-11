#!/usr/bin/env python3
from subprocess import run
from itertools import chain


TAG_PREFIX = 'adamrehn'
WINE_VERSION = '6.22'


# Builds the specified container image
def build(tag, context, buildArgs={}):
	flags = [['--build-arg', '{}={}'.format(k,v)] for k, v in buildArgs.items()]
	command = ['docker', 'buildx', 'build', '--progress=plain', '-t', tag, context] + list(chain.from_iterable(flags))
	print(command, flush=True)
	run(command, check=True)


# Build all available container images
build('adamrehn/common-base:latest', './common-base')
build('adamrehn/wine-base:{}'.format(WINE_VERSION), './wine/base', {'WINE_VERSION': WINE_VERSION, 'WINETRICKS_VERSION': '4340f09f0c17566205dcc74e15211ddac7780148'})
build('adamrehn/wine-dotnet:{}'.format(WINE_VERSION), './wine/dotnet', {'WINE_VERSION': WINE_VERSION})
build('adamrehn/wine-foxitreader:latest', './wine-foxitreader', {'WINE_VERSION': WINE_VERSION})

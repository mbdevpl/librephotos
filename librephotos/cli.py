"""Command-line interface for LibrePhotos project."""

import logging
import os

import boilerplates.logging
import boilerplates.sentry

from ._version import VERSION


class Logging(boilerplates.logging.Logging):
    """Logging configuration for this project."""

    packages = ['api', 'image_similarity', 'librephotos', 'service']
    level_global = logging.INFO


class Sentry(boilerplates.sentry.Sentry):
    """Sentry configuration for this project."""

    release = VERSION
    environment = 'development' if os.environ.get("DEBUG", "0") == "1" else 'production'


def prepare_cli():
    """Prepare denigai command-line interface."""
    Logging.configure()
    Sentry.init()

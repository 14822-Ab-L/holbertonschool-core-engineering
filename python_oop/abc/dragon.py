#!/usr/bin/env python3
"""Defines mixins and a Dragon class."""


class SwimMixin:
    """Provides swimming behaviour."""

    def swim(self):
        """Print a message about swimming."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying behaviour."""

    def fly(self):
        """Print a message about flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon with swimming and flying abilities."""

    def roar(self):
        """Print a message about the dragon roaring."""
        print("The dragon roars!")

#!/usr/bin/env python3
"""Defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print a message about the fish swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message about the fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print a message about the bird flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message about the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish."""

    def fly(self):
        """Print a message about the flying fish soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message about the flying fish swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print a message about the flying fish habitat."""
        print("The flying fish lives both in water and the sky!")

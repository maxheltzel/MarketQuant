# marketquant/interpolation.py

import numpy as np
from typing import List

class Interpolate:
    """
    A versatile interpolator for generating interpolated values between two points
    using various interpolation methods.

    Supported Methods:
        - linear
        - ease-in
        - ease-out
        - ease-in-out
        - cubic

    Example Usage:
        interpolated_values = Interpolator(start=0, end=10, steps=5, method='ease-in').interpolate()
    """

    def __init__(self,
                 start: float,
                 end: float,
                 steps: int = 10,
                 method: str = 'linear'):
        """
        Initialize the Interpolator.

        Parameters:
            start (float): The starting value.
            end (float): The ending value.
            steps (int): Number of interpolation steps (default: 10).
            method (str): Interpolation method ('linear', 'ease-in', 'ease-out', 'ease-in-out', 'cubic').
        """
        self.start = start
        self.end = end
        self.steps = steps
        self.method = method.lower()

        self.interpolation_methods = {
            'linear': self.linear,
            'ease-in': self.ease_in,
            'ease-out': self.ease_out,
            'ease-in-out': self.ease_in_out,
            'cubic': self.cubic
            # Add more methods here if needed
        }

        if self.method not in self.interpolation_methods:
            raise ValueError(f"Unsupported interpolation method '{self.method}'. "
                             f"Supported methods: {list(self.interpolation_methods.keys())}")

    def linear(self, t: float) -> float:
        """Linear interpolation."""
        return t

    def ease_in(self, t: float) -> float:
        """Ease-in interpolation (quadratic)."""
        return t ** 2

    def ease_out(self, t: float) -> float:
        """Ease-out interpolation (quadratic)."""
        return t * (2 - t)

    def ease_in_out(self, t: float) -> float:
        """Ease-in-out interpolation (cubic)."""
        return 3 * t ** 2 - 2 * t ** 3

    def cubic(self, t: float) -> float:
        """Cubic interpolation."""
        return t ** 3

    def interpolate(self) -> List[float]:
        """
        Perform the interpolation and return the interpolated values.

        Returns:
            List[float]: A list of interpolated values.
        """
        interp_func = self.interpolation_methods[self.method]
        t_values = np.linspace(0, 1, self.steps)
        interpolated = [self.start + (self.end - self.start) * interp_func(t) for t in t_values]
        return interpolated

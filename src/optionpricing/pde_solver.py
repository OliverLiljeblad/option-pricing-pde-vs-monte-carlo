"""Finite-difference solver interfaces for the Black-Scholes PDE."""

from typing import Literal

import numpy as np


OptionType = Literal["call", "put"]


def solve_explicit(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    n_space: int,
    n_time: int,
    option_type: OptionType = "call",
) -> np.ndarray:
    """Solve the Black-Scholes PDE with an explicit finite-difference scheme.

    Parameters
    ----------
    S : float
        Current underlying asset price at which the solution is evaluated.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Continuously compounded risk-free interest rate.
    sigma : float
        Constant volatility of the underlying asset.
    n_space : int
        Number of spatial grid intervals.
    n_time : int
        Number of time-step intervals.
    option_type : {"call", "put"}, default="call"
        European option payoff to solve.

    Returns
    -------
    numpy.ndarray
        The finite-difference solution on the asset-price and time grid.

    Notes
    -----
    The PDE is V_t + r S V_S + 0.5 sigma^2 S^2 V_SS - r V = 0.
    The explicit scheme computes each earlier-time value directly from
    values at the next time level and is subject to a stability condition.
    """
    raise NotImplementedError


def solve_implicit(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    n_space: int,
    n_time: int,
    option_type: OptionType = "call",
) -> np.ndarray:
    """Solve the Black-Scholes PDE with an implicit finite-difference scheme.

    Parameters
    ----------
    S : float
        Current underlying asset price at which the solution is evaluated.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Continuously compounded risk-free interest rate.
    sigma : float
        Constant volatility of the underlying asset.
    n_space : int
        Number of spatial grid intervals.
    n_time : int
        Number of time-step intervals.
    option_type : {"call", "put"}, default="call"
        European option payoff to solve.

    Returns
    -------
    numpy.ndarray
        The finite-difference solution on the asset-price and time grid.

    Notes
    -----
    The implicit scheme solves a linear system at every time step for the
    discretized PDE V_t + r S V_S + 0.5 sigma^2 S^2 V_SS - r V = 0.
    """
    raise NotImplementedError


def solve_crank_nicolson(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    n_space: int,
    n_time: int,
    option_type: OptionType = "call",
) -> np.ndarray:
    """Solve the Black-Scholes PDE with the Crank-Nicolson scheme.

    Parameters
    ----------
    S : float
        Current underlying asset price at which the solution is evaluated.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Continuously compounded risk-free interest rate.
    sigma : float
        Constant volatility of the underlying asset.
    n_space : int
        Number of spatial grid intervals.
    n_time : int
        Number of time-step intervals.
    option_type : {"call", "put"}, default="call"
        European option payoff to solve.

    Returns
    -------
    numpy.ndarray
        The finite-difference solution on the asset-price and time grid.

    Notes
    -----
    Crank-Nicolson averages the explicit and implicit spatial operators,
    giving second-order accuracy in both space and time for smooth solutions.
    It discretizes V_t + r S V_S + 0.5 sigma^2 S^2 V_SS - r V = 0.
    """
    raise NotImplementedError


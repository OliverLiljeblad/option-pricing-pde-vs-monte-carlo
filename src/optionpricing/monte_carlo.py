"""Monte Carlo simulation interfaces for geometric Brownian motion."""

import numpy as np


def simulate_euler_maruyama(
    S: float,
    T: float,
    r: float,
    sigma: float,
    n_steps: int,
    n_paths: int,
    seed: int | None = None,
) -> np.ndarray:
    """Simulate geometric Brownian motion with Euler-Maruyama.

    Parameters
    ----------
    S : float
        Initial underlying asset price.
    T : float
        Time horizon in years.
    r : float
        Constant risk-free rate and drift under the risk-neutral measure.
    sigma : float
        Constant volatility.
    n_steps : int
        Number of time steps per simulated path.
    n_paths : int
        Number of simulated paths.
    seed : int or None, default=None
        Seed for reproducible random-number generation.

    Returns
    -------
    numpy.ndarray
        Simulated asset paths with shape (n_paths, n_steps + 1).

    Notes
    -----
    Euler-Maruyama applies S_(k+1) = S_k + r S_k dt +
    sigma S_k sqrt(dt) Z_k, where Z_k is standard normal and dt = T/n_steps.
    """
    raise NotImplementedError


def simulate_antithetic_paths(
    S: float,
    T: float,
    r: float,
    sigma: float,
    n_steps: int,
    n_paths: int,
    seed: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Simulate paired Euler-Maruyama paths using antithetic variates.

    Parameters
    ----------
    S : float
        Initial underlying asset price.
    T : float
        Time horizon in years.
    r : float
        Constant risk-free rate and drift under the risk-neutral measure.
    sigma : float
        Constant volatility.
    n_steps : int
        Number of time steps per simulated path.
    n_paths : int
        Number of independent normal-noise paths before pairing.
    seed : int or None, default=None
        Seed for reproducible random-number generation.

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray]
        Two path arrays generated from opposite normal increments, each with
        shape (n_paths, n_steps + 1).

    Notes
    -----
    For every sequence of standard normal increments Z, the paired path uses
    -Z. Averaging the two resulting payoffs reduces estimator variance without
    changing its expectation.
    """
    raise NotImplementedError


def price_call_monte_carlo(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    n_steps: int,
    n_paths: int,
    seed: int | None = None,
    antithetic: bool = True,
) -> float:
    """Estimate a European call price by Monte Carlo simulation.

    Parameters
    ----------
    S : float
        Initial underlying asset price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Constant risk-free rate and drift under the risk-neutral measure.
    sigma : float
        Constant volatility.
    n_steps : int
        Number of Euler-Maruyama time steps per path.
    n_paths : int
        Number of simulated paths.
    seed : int or None, default=None
        Seed for reproducible random-number generation.
    antithetic : bool, default=True
        Whether to use antithetic variates when estimating the payoff mean.

    Returns
    -------
    float
        The discounted Monte Carlo estimate of max(S_T - K, 0).

    Notes
    -----
    The estimator is exp(-r T) times the sample mean of the terminal call
    payoff. With antithetic variates, paired terminal payoffs are averaged
    before the sample mean is taken.
    """
    raise NotImplementedError


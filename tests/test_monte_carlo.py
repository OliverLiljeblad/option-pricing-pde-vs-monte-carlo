"""Placeholder tests for Monte Carlo simulation."""

import pytest


@pytest.mark.skip(reason="Implement after the Monte Carlo simulator is added.")
def test_monte_carlo_error_shrinks_like_inverse_sqrt_paths() -> None:
    """Verify statistical error decreases approximately as 1/sqrt(N)."""
    pass


@pytest.mark.skip(reason="Implement after antithetic variates are added.")
def test_antithetic_variates_reduce_estimator_variance() -> None:
    """Verify antithetic variates reduce variance for a fixed path budget."""
    pass


@pytest.mark.skip(reason="Implement after Euler-Maruyama pricing is added.")
def test_monte_carlo_price_approaches_black_scholes_reference() -> None:
    """Verify the Monte Carlo estimate approaches the exact call price."""
    pass


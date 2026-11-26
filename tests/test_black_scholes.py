"""Placeholder tests for closed-form Black-Scholes functions."""

import pytest


@pytest.mark.skip(reason="Implement after the exact Black-Scholes formulas are added.")
def test_put_call_parity() -> None:
    """Verify C - P = S - K exp(-r T)."""
    pass


@pytest.mark.skip(reason="Implement after the exact Black-Scholes formulas are added.")
def test_delta_and_gamma_match_finite_differences() -> None:
    """Verify analytical delta and gamma against numerical derivatives."""
    pass


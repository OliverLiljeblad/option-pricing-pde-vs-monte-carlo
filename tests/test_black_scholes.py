"""Tests for the closed-form Black-Scholes formulas and Greeks."""

from math import exp

import pytest

from optionpricing.black_scholes import (
    call_delta,
    call_gamma,
    call_price,
    put_delta,
    put_gamma,
    put_price,
)


S = 100.0
K = 100.0
T = 1.0
r = 0.05
sigma = 0.20


def test_put_call_parity() -> None:
    """Verify C - P = S - K exp(-r T)."""
    call_minus_put = call_price(S, K, T, r, sigma) - put_price(S, K, T, r, sigma)
    assert call_minus_put == pytest.approx(S - K * exp(-r * T))


def test_prices_match_standard_reference_values() -> None:
    """Verify prices against a standard Black-Scholes example."""
    assert call_price(S, K, T, r, sigma) == pytest.approx(10.45058357, rel=1e-7)
    assert put_price(S, K, T, r, sigma) == pytest.approx(5.57352602, rel=1e-7)


def test_delta_and_gamma_identities() -> None:
    """Verify call-put delta parity and equality of call and put gamma."""
    delta_difference = call_delta(S, K, T, r, sigma) - put_delta(S, K, T, r, sigma)
    assert delta_difference == pytest.approx(1.0)
    assert call_gamma(S, K, T, r, sigma) == pytest.approx(put_gamma(S, K, T, r, sigma))


def test_zero_time_prices_equal_intrinsic_values() -> None:
    """Verify prices at maturity equal their option payoffs."""
    assert call_price(110.0, K, 0.0, r, sigma) == pytest.approx(10.0)
    assert put_price(90.0, K, 0.0, r, sigma) == pytest.approx(10.0)


def test_invalid_inputs_raise_value_error() -> None:
    """Verify invalid asset, strike, maturity, and volatility values are rejected."""
    with pytest.raises(ValueError):
        call_price(0.0, K, T, r, sigma)
    with pytest.raises(ValueError):
        call_price(S, -K, T, r, sigma)
    with pytest.raises(ValueError):
        call_price(S, K, -T, r, sigma)
    with pytest.raises(ValueError):
        call_price(S, K, T, r, -sigma)

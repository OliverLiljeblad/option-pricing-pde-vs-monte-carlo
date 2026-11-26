"""Placeholder tests for finite-difference PDE solvers."""

import pytest


@pytest.mark.skip(reason="Implement after the finite-difference PDE solvers are added.")
def test_crank_nicolson_convergence_slope_is_near_two() -> None:
    """Verify Crank-Nicolson convergence is approximately second order."""
    pass


@pytest.mark.skip(reason="Implement after the explicit PDE solver is added.")
def test_explicit_scheme_becomes_unstable_past_stability_limit() -> None:
    """Verify the explicit scheme is unstable beyond its stability limit."""
    pass


@pytest.mark.skip(reason="Implement after all PDE solvers are added.")
def test_pde_prices_approach_black_scholes_reference() -> None:
    """Verify PDE prices converge to the closed-form reference price."""
    pass


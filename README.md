# Option Pricing: PDE vs Monte Carlo

This project compares two numerical approaches for pricing European options on the S&P 500: finite-difference solutions of the Black-Scholes PDE and Monte Carlo simulation of geometric Brownian motion. The numerical results will be benchmarked against the exact closed-form Black-Scholes formula.

## Project overview

The model is geometric Brownian motion under the risk-neutral measure:

`dS = r S dt + sigma S dW`.

The project will study convergence rates, explicit-scheme stability, accuracy versus runtime, and the estimation of delta and gamma, ending with an S&P 500 (SPX) case study.

## Methods

The PDE method solves

`V_t + r S V_S + 0.5 sigma^2 S^2 V_SS - r V = 0`

with explicit, implicit, and Crank-Nicolson finite-difference schemes. The Monte Carlo method approximates the same risk-neutral expectation by simulating geometric Brownian motion with Euler-Maruyama and antithetic variates.

The connection between the two methods is the Feynman-Kac theorem: the Black-Scholes PDE solution equals the discounted expected payoff under the risk-neutral SDE. This provides a common mathematical basis for comparing their prices and numerical errors.

## Repository structure

```text
src/optionpricing/
  black_scholes.py   # Exact prices and Greeks
  pde_solver.py      # Finite-difference PDE solver interfaces
  monte_carlo.py     # Euler-Maruyama and antithetic simulation interfaces
tests/               # Placeholder tests for future implementations
notebooks/           # Experiments and visualizations
figures/             # Generated figures
report/              # Course report materials
```

## Getting started

Create and activate a virtual environment:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Install the package and its dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

Run the test suite:

```bash
pytest
```

## Results

Coming soon. This section will contain convergence plots, stability experiments, runtime comparisons, Greek estimates, and the SPX case study.

## Limitations

- Volatility is assumed constant.
- The risk-free interest rate is assumed constant.
- Dividends are ignored.
- The current scope focuses on European options under the Black-Scholes model.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).

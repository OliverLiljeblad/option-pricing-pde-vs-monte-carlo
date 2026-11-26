"""Closed-form Black-Scholes pricing and sensitivity functions."""

from math import exp, log, sqrt

from scipy.stats import norm


def _validate_inputs(S: float, K: float, T: float, sigma: float) -> None:
    """Validate parameters shared by all Black-Scholes calculations."""
    if S <= 0:
        raise ValueError("S must be positive.")
    if K <= 0:
        raise ValueError("K must be positive.")
    if T < 0:
        raise ValueError("T must be non-negative.")
    if sigma < 0:
        raise ValueError("sigma must be non-negative.")


def _d1_d2(S: float, K: float, T: float, r: float, sigma: float) -> tuple[float, float]:
    """Return the standard d1 and d2 terms used in Black-Scholes formulas."""
    time_volatility = sigma * sqrt(T)
    d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / time_volatility
    return d1, d1 - time_volatility


def _maturity_delta(S: float, K: float, option_type: str) -> float:
    """Return a practical delta convention at maturity."""
    if S > K:
        return 1.0 if option_type == "call" else 0.0
    if S < K:
        return 0.0 if option_type == "call" else -1.0
    # The payoff is not differentiable at the strike; 0.5 is the midpoint
    # convention commonly used for an at-the-money option at maturity.
    return 0.5 if option_type == "call" else -0.5


def call_price(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Return the exact Black-Scholes price of a European call option.

    Parameters
    ----------
    S : float
        Current underlying asset price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Continuously compounded risk-free interest rate.
    sigma : float
        Constant volatility of the underlying asset.

    Returns
    -------
    float
        The discounted expected call payoff under the risk-neutral measure.

    Notes
    -----
    The formula is C = S N(d1) - K exp(-r T) N(d2), where
    d1 = [log(S / K) + (r + sigma^2 / 2) T] / (sigma sqrt(T))
    and d2 = d1 - sigma sqrt(T).
    """
    _validate_inputs(S, K, T, sigma)
    if T == 0:
        return max(S - K, 0.0)
    if sigma == 0:
        return max(S - K * exp(-r * T), 0.0)

    d1, d2 = _d1_d2(S, K, T, r, sigma)
    return S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)


def put_price(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Return the exact Black-Scholes price of a European put option.

    Parameters
    ----------
    S : float
        Current underlying asset price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Continuously compounded risk-free interest rate.
    sigma : float
        Constant volatility of the underlying asset.

    Returns
    -------
    float
        The discounted expected put payoff under the risk-neutral measure.

    Notes
    -----
    The formula is P = K exp(-r T) N(-d2) - S N(-d1), using the
    d1 and d2 definitions from :func:`call_price`.
    """
    _validate_inputs(S, K, T, sigma)
    if T == 0:
        return max(K - S, 0.0)
    if sigma == 0:
        return max(K * exp(-r * T) - S, 0.0)

    d1, d2 = _d1_d2(S, K, T, r, sigma)
    return K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


def call_delta(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Return the exact delta of a European call option.

    Parameters
    ----------
    S : float
        Current underlying asset price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Continuously compounded risk-free interest rate.
    sigma : float
        Constant volatility of the underlying asset.

    Returns
    -------
    float
        The derivative of the call price with respect to S.

    Notes
    -----
    The Black-Scholes call delta is N(d1).
    """
    _validate_inputs(S, K, T, sigma)
    if T == 0:
        return _maturity_delta(S, K, "call")
    if sigma == 0:
        forward_strike = K * exp(-r * T)
        return 1.0 if S > forward_strike else 0.0 if S < forward_strike else 0.5

    d1, _ = _d1_d2(S, K, T, r, sigma)
    return float(norm.cdf(d1))


def put_delta(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Return the exact delta of a European put option.

    Parameters
    ----------
    S : float
        Current underlying asset price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Continuously compounded risk-free interest rate.
    sigma : float
        Constant volatility of the underlying asset.

    Returns
    -------
    float
        The derivative of the put price with respect to S.

    Notes
    -----
    The Black-Scholes put delta is N(d1) - 1.
    """
    _validate_inputs(S, K, T, sigma)
    if T == 0:
        return _maturity_delta(S, K, "put")
    if sigma == 0:
        forward_strike = K * exp(-r * T)
        return -1.0 if S < forward_strike else 0.0 if S > forward_strike else -0.5

    d1, _ = _d1_d2(S, K, T, r, sigma)
    return float(norm.cdf(d1) - 1.0)


def call_gamma(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Return the exact gamma of a European call option.

    Parameters
    ----------
    S : float
        Current underlying asset price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Continuously compounded risk-free interest rate.
    sigma : float
        Constant volatility of the underlying asset.

    Returns
    -------
    float
        The second derivative of the call price with respect to S.

    Notes
    -----
    The Black-Scholes gamma is n(d1) / (S sigma sqrt(T)), where n is
    the standard normal probability density function.
    """
    _validate_inputs(S, K, T, sigma)
    if T == 0 or sigma == 0:
        return 0.0

    d1, _ = _d1_d2(S, K, T, r, sigma)
    return float(norm.pdf(d1) / (S * sigma * sqrt(T)))


def put_gamma(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Return the exact gamma of a European put option.

    Parameters
    ----------
    S : float
        Current underlying asset price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Continuously compounded risk-free interest rate.
    sigma : float
        Constant volatility of the underlying asset.

    Returns
    -------
    float
        The second derivative of the put price with respect to S.

    Notes
    -----
    The Black-Scholes gamma is the same for calls and puts:
    n(d1) / (S sigma sqrt(T)).
    """
    # Call and put prices have the same second derivative with respect to S.
    return call_gamma(S, K, T, r, sigma)


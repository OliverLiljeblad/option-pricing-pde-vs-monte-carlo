"""Closed-form Black-Scholes pricing and sensitivity functions."""

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
    raise NotImplementedError


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
    raise NotImplementedError


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
    raise NotImplementedError


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
    raise NotImplementedError


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
    raise NotImplementedError


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
    raise NotImplementedError


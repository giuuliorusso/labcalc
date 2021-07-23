from dataclasses import dataclass
from typing import Optional
import unittest

from matplotlib import rc
from numpy.typing import NDArray
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

rc("text", usetex=True)
rc("font", **{"family": "serif", "serif": ["Computer Modern"]})

Array = NDArray[np.float64]


#


@dataclass
class PColor:
    primary: str
    secondary: str


colors: dict[str, PColor] = {
    "blue": PColor("tab:blue", "blue"),
    "green": PColor("tab:green", "darkgreen"),
    "orange": PColor("tab:orange", "brown"),
    "pink": PColor("tab:pink", "red")
}


#


def plot_histogram(
    data: Array,
    xlabel: str,
    bindiv: float = 2,
    color: PColor = colors["blue"],
    digits: int = 5,
    mu: Optional[float] = None,
    sigma: Optional[float] = None
):
    """ Plot istogramma con relativa distribuzione normale. """

    N = np.count_nonzero(~np.isnan(data))
    print(f"N = {N}")

    if mu is None or sigma is None:
        mu = data.mean()
        sigma = data.std(ddof=1)

    print(f"mu = {mu}")
    print(f"sigma = {sigma}")

    # Binning
    binsize = sigma / bindiv
    print(f"binsize = {binsize}")
    interval = data.max() - data.min()
    nbins = int(interval / binsize) if binsize != 0 else 1

    # Istogramma
    counts, bins, patches = plt.hist(
        data, bins=nbins,
        color=color.primary,
        alpha=0.45, edgecolor="black"
    )

    # Gaussiana
    norm_factor = N * binsize
    xmin = mu - 3.5 * sigma
    xmax = mu + 3.5 * sigma
    x = np.linspace(xmin, xmax, 1000)
    y = norm_factor * stats.norm.pdf(x, mu, sigma)

    plt.plot(x, y, color=color.secondary)
    plt.vlines(mu, 0, np.amax(counts), linestyles="--", color=color.secondary)

    plt.xlabel(xlabel)
    plt.ylabel("entries")

    plt.title(
        fr"$ \mu = {round(mu, digits)}, \sigma = {round(sigma, digits)} $"
    )

    plt.tight_layout()


#


def mean(x: Array, w: Array) -> float:
    """ Media pesata. """
    return np.sum(x * w) / np.sum(w)


def cov(x: Array, y: Array, w: Array) -> float:
    """ Covarianza. """
    return mean(x * y, w) - mean(x, w) * mean(y, w)


def var(x: Array, w: Array) -> float:
    """ Varianza. """
    return cov(x, x, w)


def line(x: Array, m: float, c: float) -> Array:
    """ Retta best fit (mu_Y). """
    return m * x + c


def sigma_line(
    x: Array,
    sigma_m: float,
    sigma_c: float,
    cov_mc: float
) -> Array:
    """ Incertezza su mu_Y ottenuta della propagazione delle incertezze. """
    return np.sqrt(
        (x * sigma_m) ** 2 +
        sigma_c ** 2 +
        2 * x * cov_mc
    )


@dataclass
class Fit:
    # Coefficiente angolare
    m: float
    var_m: float
    sigma_m: float

    # Termine noto
    c: float
    var_c: float
    sigma_c: float

    # Covarianza e coefficiente di correlazione
    cov_mc: float
    rho_mc: float


def linear_fit(
    x: Array,
    y: Array,
    sigma_y: Array,
    digits: Optional[int] = None,
    verbosity: int = 1
) -> Fit:
    """ Fit lineare con metodo dei minimi quadrati. """

    # Pesi
    w = 1 / (sigma_y ** 2)

    # m
    m = cov(x, y, w) / var(x, w)
    var_m = 1 / (var(x, w) * np.sum(w))
    sigma_m = np.sqrt(var_m)

    # c
    c = mean(y, w) - m * mean(x, w)
    var_c = mean(x ** 2, w) * var_m
    sigma_c = np.sqrt(var_c)

    # cov, rho
    cov_mc = -mean(x, w) * var_m
    rho_mc = cov_mc / np.sqrt(var_m * var_c)

    fit = Fit(m, var_m, sigma_m, c, var_c, sigma_c, cov_mc, rho_mc)

    def print_info(dict: dict[str, float]):
        for k, v in dict.items():
            if digits is not None:
                v = round(v, digits)
            print(f"\t{k} = {v}")

    info: dict[str, float] = {
        "mean(x, w)": mean(x, w),
        "mean(x^2, w)": mean(x ** 2, w),
        "mean(y, w)": mean(y, w),
        "mean(xy, w)": mean(x * y, w),
        "var_x": var(x, w),
        "var_y": var(y, w),
        "cov_xy": cov(x, y, w),
        "rho_xy": cov(x, y, w) / np.sqrt(var(x, w) * var(y, w)),
        "sum(w)": np.sum(w)
    }

    if verbosity >= 1:
        print("Fit:")
        print_info(fit.__dict__)

    if verbosity >= 2:
        print("Other:")
        print_info(info)

    return fit


def plot_linear_fit(
    x: Array,
    y: Array,
    sigma_y: Array,
    xlabel: str,
    ylabel: str,
    sigmas: list[float] = [1],
    digits: Optional[int] = None,
    verbosity: int = 1
) -> Fit:
    """ Plot fit lineare. """

    fit = linear_fit(x, y, sigma_y, digits, verbosity)

    # Punti con incertezza
    plt.errorbar(
        x, y,
        yerr=sigma_y,
        ls="", marker=".",
        color="black",
        label="dati"
    )

    # Retta best fit
    xdiff = x.max() - x.min()
    xmin = x.min() - 0.2 * xdiff
    xmax = x.max() + 0.2 * xdiff
    xs = np.linspace(xmin, xmax, 1000)
    ys = line(xs, fit.m, fit.c)
    plt.plot(xs, ys, "-", color="red", label=r"$ \mu_Y $")

    # Incertezza/e retta best fit
    colors = ["tab:orange", "tab:green", "tab:blue"]
    assert len(sigmas) <= len(colors)

    previous_s = 0
    for s, color in zip(sigmas, colors):
        label = fr"$ \mu_Y \pm {s} \sigma $"
        sigma = sigma_line(xs, fit.sigma_m, fit.sigma_c, fit.cov_mc)

        plt.plot(
            xs,
            ys + (s * sigma),
            "-", linewidth=1,
            color=color, label=label
        )

        plt.plot(
            xs,
            ys - (s * sigma),
            "-", linewidth=1,
            color=color
        )

        plt.fill_between(
            xs,
            ys + (s * sigma),
            ys + (previous_s * sigma),
            color=color, alpha=0.2
        )

        plt.fill_between(
            xs,
            ys - (s * sigma),
            ys - (previous_s * sigma),
            color=color, alpha=0.2
        )

        previous_s = s

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xlim(xmin, xmax)

    plt.grid()
    plt.legend()
    plt.tight_layout()

    return fit


def plot_residuals(
    x: Array,
    y: Array,
    sigma_y: Array,
    xlabel: str,
    yunit: str,
    color: PColor = colors["blue"],
    standardized: bool = False,
    digits: Optional[int] = None,
    verbosity: int = 0
):
    fit = linear_fit(x, y, sigma_y, digits, verbosity)

    mu_Y = line(x, fit.m, fit.c)
    d = y - mu_Y

    ylabel = r"$ d = y - \mu_Y $"

    if standardized:
        d /= sigma_y
        sigma_y /= sigma_y
        ylabel = r"$ d / \sigma_y $"

    ylabel += f" {yunit}"

    plt.errorbar(
        x, d,
        yerr=sigma_y,
        marker=".", markersize=12, linestyle="",
        ecolor=color.primary, color=color.secondary
    )

    plt.axhline(0, linestyle="--", color="black")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.grid()
    plt.tight_layout()


#


class TestFit(unittest.TestCase):
    def setUp(self) -> None:
        x = np.arange(3, 8.5, 0.5)
        y = np.array([
            6.66, 6.29, 6.81, 4.70, 5.31, 4.84, 4.08, 3.09, 3.29, 2.74, 2.01
        ])
        sigma_y = np.array([
            0.32, 0.58, 0.63, 0.47, 0.67, 0.37, 0.38, 0.72, 0.34, 0.83, 0.38
        ])

        self.fit = linear_fit(x, y, sigma_y, verbosity=0)

    def test_m(self):
        self.assertEqual(self.fit.m, -0.9108806156213155)

    def test_sigma_m(self):
        self.assertEqual(self.fit.sigma_m, 0.08009860609272347)

    def test_c(self):
        self.assertEqual(self.fit.c, 9.517901891168307)

    def test_sigma_c(self):
        self.assertEqual(self.fit.sigma_c, 0.4589859021311939)

    def test_rho_mc(self):
        self.assertEqual(self.fit.rho_mc, -0.9560360371170425)


if __name__ == "__main__":
    unittest.main(verbosity=2)

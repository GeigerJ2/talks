#!/apps/share64/debian10/anaconda/anaconda-7/bin/python

import argparse
from pathlib import Path

import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(
    prog="Plot eigenvalues from matrix diagonalization.",
    description="Plot eigenvalues from matrix diagonalization.",
)
parser.add_argument(
    "-i",
    "--input-file",
    help="Input file containing the eigenvalues of the previous matrix diagonalization.",
)
parser.add_argument(
    "-p",
    "--plot-type",
    help="Type of plot to create from the eigenvalues [violin|hist|dens|box].",
    default="violin",
)


def read_eigenvals(file_path):
    eigenvalues = []
    with open(file_path, "r") as file:
        for line in file:
            try:
                # Convert each line to a float and add it to the list
                eigenvalue = float(line.strip())
                eigenvalues.append(eigenvalue)
            except ValueError:
                # Skip lines that can't be converted to float
                continue
    return eigenvalues


def plot_eigvals(eigenvalues, plot_type):
    # Create a figure and axis object
    fig, ax = plt.subplots(figsize=(8, 6))

    if plot_type == "hist":
        ax.hist(eigenvalues, bins=10, color="c", edgecolor="black")
        ax.set_title("Histogram of Eigenvalues")
        ax.set_xlabel("Eigenvalue")
        ax.set_ylabel("Frequency")

    elif plot_type == "dens":
        density, bins, _ = ax.hist(eigenvalues, bins=30, density=True, alpha=0.0)
        ax.plot(bins[:-1], density, color="m")
        ax.fill_between(bins[:-1], density, color="m", alpha=0.3)
        ax.set_title("Density Plot of Eigenvalues")
        ax.set_xlabel("Eigenvalue")
        ax.set_ylabel("Density")

    elif plot_type == "box":
        ax.boxplot(
            eigenvalues, vert=False, patch_artist=True, boxprops=dict(facecolor="g")
        )
        ax.set_title("Box Plot of Eigenvalues")
        ax.set_xlabel("Eigenvalue")

    elif plot_type == "violin":
        ax.violinplot(eigenvalues, vert=False)
        ax.set_title("Violin Plot of Eigenvalues")
        ax.set_xlabel("Eigenvalue")

    else:
        raise ValueError(f"Unsupported plot type: <{plot_type}>")

    # Return the figure and axis objects
    return fig, ax


if __name__ == "__main__":
    args = parser.parse_args()
    input_file = args.input_file
    plot_type = args.plot_type
    eigenvalues = read_eigenvals(file_path=input_file)
    if not Path(input_file).exists():
        raise FileNotFoundError(
            f"Could not find the input file {input_file.resolve()}."
        )

    fig, ax = plot_eigvals(eigenvalues=eigenvalues, plot_type=plot_type)

    # Save the plot outside of the function
    filename = input_file.replace('.txt', '')
    filename += f"-{plot_type}.png"
    fig.savefig(filename, format="png")
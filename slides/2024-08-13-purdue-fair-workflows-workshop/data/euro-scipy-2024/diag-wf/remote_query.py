#!/apps/share64/debian10/anaconda/anaconda-7/bin/python

import argparse
import sqlite3
from pathlib import Path

import numpy as np

parser = argparse.ArgumentParser(
    prog="Query npy matrix from a database.",
    description="Queries a matrix from a matrix database.",
)
parser.add_argument("db_path", help="Path of the database to query from.")
parser.add_argument("pk", help="The primary key of the matrix to query from.")


def query_matrix(database_path: Path, pk: int):
    """ """
    sqlite3.register_converter("NP_NDARRAY", np.frombuffer)
    with sqlite3.connect(database_path, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT pk, arr, arr_rows, arr_cols FROM matrices WHERE pk = ?", (pk,)
        )
        result = cur.fetchone()
    if result is None:
        raise ValueError(
            f"No matrix with pk {pk} is available in database {database_path}"
        )
    else:
        pk, mat, rows, cols = result
        return mat


if __name__ == "__main__":
    args = parser.parse_args()
    db_path = Path(args.db_path)
    if not db_path.exists():
        raise FileNotFoundError(f"Could not find database file {db_path.absolute()}.")
    else:
        mat = query_matrix(db_path, args.pk)
        filename = f"matrix-{args.pk}"
        np.save(filename, mat)
        print(f"Saved matrix to file {filename}.npy")

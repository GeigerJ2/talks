import sqlite3
import numpy as np
import io

import argparse
parser = argparse.ArgumentParser(
                    prog='Create an sqlite database with matrices.',
                    description='Create an sqlite database with matrices with the name. It randomly generates square matrices of size 100.')
parser.add_argument('--db_name', default="matrices.db", help="Name of the database.")
parser.add_argument('--nb_mats', default=100, help="Number of matrices to populate the database with.", required=False)
parser.add_argument('--dim_mats', default=50, help="Dimension of the matrices.")
parser.add_argument('--offset', default=0, help="Offset in dimension of the matrices.")

def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(arr_text):
    out = io.BytesIO(arr_text)
    out.seek(0)
    return np.load(out)

def create_sqlite_database(database_filename: str, nb_mats: int, dim_mats : int, offset : int):
    """ create a database connection to an SQLite database """
    sqlite3.register_adapter(np.ndarray, lambda x: x.tobytes())
    sqlite3.register_converter("NP_NDARRAY", np.frombuffer)
    with sqlite3.connect(database_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:


        cur = conn.cursor()
        cur.execute("""CREATE TABLE matrices (
                                            pk INTEGER NOT NULL PRIMARY KEY,
                                            arr NP_NDARRAY,
                                            arr_rows INTEGER, 
                                            arr_cols INTEGER)""")

        rng = np.random.default_rng(seed=0)
        for pk in range(nb_mats):
            offset_ = np.random.randint(-offset, offset)
            mat = rng.random((dim_mats+offset_, dim_mats+offset_))

            cur.execute("INSERT INTO matrices (pk, arr, arr_rows, arr_cols) VALUES (?, ?, ?, ?)",
                        (pk, mat, mat.shape[0], mat.shape[1]))


if __name__ == '__main__':
    args = parser.parse_args()
    create_sqlite_database(args.db_name, int(args.nb_mats), int(args.dim_mats), int(args.offset))
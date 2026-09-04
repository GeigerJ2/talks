### How to create the matrices.db

To create the database with matrices 

```console
python create_database.py # you will get an error the matrices.db still exists  
cp matrices ../
```

### How to compile diagonalization binary with the rust code

For producing the binary for running the rust project do

```console
cd diag-rs
cargo build --release # compile release version
cp target/release/diag-rs ../../bin/default # overwrite default binary
```

### How to compile the python diagonalization file
```code
pip install nuitka
sudo apt install patchelf
nuitka --standalone diager.py
```

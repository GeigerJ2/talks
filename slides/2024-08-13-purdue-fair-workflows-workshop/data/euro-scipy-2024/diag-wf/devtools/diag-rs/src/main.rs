extern crate npy;

use nalgebra::DMatrix;
use std::f64;

use std::io::Read;
use npy::NpyData;

use std::env;

use std::io::{Write, self};
use std::fs::File;

use std::path::Path;

fn help() {
    println!("
Reads a .npy file reshapes it to a square matrix and computes the absolute eigenvalues.

Usage:

    ./diager <NPY_FILENAME>");
}

fn read_npy(filename: String) -> DMatrix<f64>{
    let mut buf = vec![];
    std::fs::File::open(filename).unwrap()
        .read_to_end(&mut buf).unwrap();

    let data: Vec<f64> = NpyData::from_bytes(&buf).unwrap().to_vec();
    let cols = (data.len() as f64).sqrt() as usize;
    let rows = cols;
    let b = DMatrix::from_row_slice(rows, cols, &data[..]);
    b
}

fn write_vec_to_file(vec: &Vec<f64>, filename: &str) -> io::Result<()> {
    // Open the file in write-only mode, creating it if it doesn't exist
    let mut file = File::create(filename)?;

    // Write each value in the vector to the file, separated by newlines
    for &num in vec {
        writeln!(file, "{}", num)?;
    }

    Ok(())
}

fn get_file_stem(filename: &str) -> String {
    // Create a Path from the filename
    let path = Path::new(filename);

    // Get the file stem (the filename without extension)
    match path.file_stem() {
        Some(stem) => stem.to_string_lossy().to_string(),
        None => filename.to_string(), // If there's no file stem, return the original filename
    }
}


fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        2 => {
            let filename_arg = &args[1];
            let filename: String = match filename_arg.parse::<String>() {
                Ok(f) => {
                    f.to_string()
                },
                Err(_) => {
                    eprintln!("error: second argument not an string");
                    help();
                    return Ok(());
                },
            };
            let mat = read_npy(filename.clone());
            // println!("Matb {}", mat);
            let schur = mat.schur();
            let eigvals = schur.complex_eigenvalues();
            let abs_eigvals = eigvals.map(|c| c.norm_sqr());
            let vec = abs_eigvals.data.as_vec();
            let filestem = get_file_stem(&filename);
            println!("{}",filestem);
            write_vec_to_file(&vec, &(filestem + "-eigvals.txt"))?;
            Ok(())
        },
        // all the other cases
        _ => {
            // show a help message
            help();
            Ok(())
        }
    }
}

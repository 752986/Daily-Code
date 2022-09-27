use std::{io::stdin, array};

fn main() {
    let mut password: String = String::new();
    stdin().read_line(&mut password).expect("uh oh");

    println!("{}", crack(&password, password.len()));
}

fn crack(search: &String, length: usize) -> String {
    let chars: [u8; length];

}
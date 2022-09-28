// This code is pretty much just a straight port of the python code. It seems to run roughly 100 times faster.

use std::io::{stdin, stdout, Write};
use std::time::Instant;

fn main() {
    loop {
        let mut password: String = String::new();
        print!("enter a password to find! (`exit` to quit)\n> ");
        stdout().flush().expect("");
        stdin().read_line(&mut password).expect("");
        password.retain(|c| !(c == '\r' || c == '\n'));

        if password == "exit" {
            break;
        }

        let start = Instant::now();

        match crack(&password, password.len()) {
            Some(pw) => { println!("The password is {}.", pw) },
            None => { println!("No value was found!") }
        }

        let elapsed = start.elapsed();
        println!("(took {:?} seconds)", elapsed.as_secs_f32())
    }
}

fn crack(search: &String, length: usize) -> Option<String> {
    let chars = search.bytes().collect::<Vec<u8>>();
    let mut check = vec![32; length]; // start with space, the lowest ascii value we care to check 

    loop {
        if chars == check {
            return Some(String::from_utf8(check).expect(""));
        }

        check[0] += 1;

        if check[length-1] > 126 {
            return None;
        }

        for i in 0..length {
            if check[i] > 126 {
                check[i] = 32;
                check[i + 1] += 1;
            }
        }
    }
}

// This function attempts to be faster by using fixed-size arrays, but it currently has a weird bug where it refuses to return `None` if it doesn't find the value. That may be caused by the provided length being longer than the string it's searching for?
fn crack_static<const length: usize>(search: &String) -> Option<String> {
    let chars = search.as_bytes();
    let check = &mut [32; length]; // start with space, the lowest ascii value we care to check 

    loop {
        if chars == check {
            return Some(String::from_utf8(check.to_vec()).expect(""));
        }

        check[0] += 1;

        if check[length-1] > 126 {
            println!("aaa");
            return None;
        }

        for i in 0..length {
            if check[i] > 126 {
                check[i] = 32;
                check[i + 1] += 1;
            }
        }
    }
}
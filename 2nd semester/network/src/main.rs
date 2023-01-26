use std::{net::{TcpListener, TcpStream, Shutdown}, io::{Write, Read, read_to_string, BufReader, BufRead}};

fn main() {
    let listener: TcpListener = TcpListener::bind("10.17.68.53:42069").expect("unable to bind listener");

    loop {
        match listener.accept() {
            Ok((mut client, ip)) => {
                println!("accepted incoming connection from {ip}");
                client.write_all(b"hello from declan!").unwrap();
                let mut reader = BufReader::new(&client);
                let mut response = String::new();
                loop {
                    match reader.read_line(&mut response) {
                        Ok(0) | Err(_) => break,
                        Ok(_) => println!("{}", response)
                    }
                }
            },
            Err(ip) => {
                println!("unable to connect to client at {ip}");
            }
        }
    }

}

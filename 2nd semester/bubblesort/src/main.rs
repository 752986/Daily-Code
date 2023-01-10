use std::time::Instant;
use rand::random;

fn main() {
    let length = 100000;
    let mut a: Vec<i32> = (0..length).map(|_| (random::<i32>() % 100).abs()).collect();

    let start = Instant::now();
    bubble_sort(&mut a);
    let elapsed_seconds = start.elapsed().as_secs_f64();

    println!("{} elements, {} secs", length, elapsed_seconds)

    // println!("{:?}", a);
}

fn bubble_sort<T>(list: &mut Vec<T>) where T: PartialOrd + Copy {
    let mut sorted = false;
    let mut finished = 0;
    while !sorted {
        sorted = true;
        for i in 0..(list.len() - 1 - finished) {
            if list[i] > list[i + 1] {
                let temp = list[i + 1];
                list[i + 1] = list[i];
                list[i] = temp;
                sorted = false;
            }
        }
        finished += 1;
    }
}

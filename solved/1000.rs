use std::io;


fn main() {
    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Error");

    let input_vec:Vec<usize> = input.split_ascii_whitespace()
        .map(|s| s.trim().parse().expect("Error"))
        .collect::<Vec<_>>();

    let output = input_vec[0] + input_vec[1];

    println!("{output}");

}

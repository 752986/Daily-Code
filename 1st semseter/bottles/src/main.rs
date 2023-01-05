// 100,000,000 bottles will generate a 14gb file. use at your own risk.

fn main() {
	let mut a = String::new();
	for i in (1..100_000u64).rev() {
		a.push_str(&(i.to_string() + " bottles of root beer on the wall, "));
		a.push_str(&(i.to_string() + " bottles of root beer! \ntake one down, pass it around, "));
		a.push_str(&((i - 1).to_string() + " bottles of root beer on the wall!"));
		a.push_str("\n\n");
	}
	std::fs::File::create("bottles.txt").unwrap();
	std::fs::write("bottles.txt", a).unwrap();
}
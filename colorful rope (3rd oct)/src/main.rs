struct Solution {}

impl Solution {
	pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
		let mut chars = colors.chars().collect::<Vec<char>>();
		let mut cost = 0;
		loop {
			let mut zipped = chars.iter().zip(&needed_time);
			let mut prev = zipped.next().unwrap();
			for (i, curr) in zipped.enumerate() {
				if curr.0 == prev.0 {
					if curr.1 < prev.1 {
						zipped.remove(i);
					}
				}
			}
		}
		return cost;
	}
}

fn main() {
	let result = Solution::min_cost(String::from("aaabbbabbbb"), vec![3,5,10,7,5,3,5,5,4,8,1]);
	println!("{}", &result);
}
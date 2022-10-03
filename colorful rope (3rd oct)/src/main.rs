struct Solution {}

impl Solution {
	pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
		let mut cost = 0;
		let zipped = colors.chars().zip(needed_time).collect::<Vec<(char, i32)>>();
		let mut prev = zipped[0];
		for i in 1..zipped.len() {
			let curr = zipped[i];
			if i == 0 {
				continue;
			} else if curr.0 == prev.0 {
				cost += prev.1.min(curr.1);
			}
			prev = curr;
		}
		return cost;
	}
}

fn main() {
	let result = Solution::min_cost(String::from("aaabbbabbbb"), vec![3,5,10,7,5,3,5,5,4,8,1]);
	println!("{}", &result);
}
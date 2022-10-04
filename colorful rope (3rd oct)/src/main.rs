struct Solution {}

impl Solution {
	pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
		// part 1: find the lengths of each span of chars
		let mut cost = 0;
		let mut chars = colors.chars();
		let mut costs = needed_time.iter();
		
		for i in 0.. {
			let prev_char = chars.next().unwrap();
			let mut current_cost = 0;
			let mut max_cost = costs.next().unwrap();
			while prev_char == chars.next().unwrap() {
				let char_cost = costs.next().unwrap();
				current_cost += char_cost;
				if char_cost > max_cost {
					max_cost = char_cost;
				}
			}
			cost += current_cost - max_cost;
		}
		
		return cost
	}
}

fn main() {
	let result = Solution::min_cost(String::from("aaabbbabbbb"), vec![3,5,10,7,5,3,5,5,4,8,1]);
	println!("{}", &result);
}
use std::ops::Index;

struct Solution {}

impl Solution {
	pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
		// part 1: find the lengths of each span of chars
		let mut cost = 0;
		let mut chars = colors.chars();
		let mut ranges = Vec::new();
		ranges.push((chars.next().unwrap(), 1));
		for c in chars {
			if c != ranges.last().unwrap().0 {
				ranges.push((c, 1));
			} else {
				ranges.last_mut().unwrap().1 += 1;
			}
		}
		
		// part 2: remove all but the max cost values in each range
		let mut offset = 0;
		for r in ranges {
			let slice = &needed_time[offset..(offset + r.1)];
			let max = slice.iter().max().unwrap();
			let mut skipped = false;
			for t in slice.iter() {
				if !skipped && t == max {
					skipped = true;
					continue
				} else {
					cost += t;
				}
			}

			offset += r.1;
		}
		return cost
	}
}

fn main() {
	let result = Solution::min_cost(String::from("aaabbbabbbb"), vec![3,5,10,7,5,3,5,5,4,8,1]);
	println!("{}", &result);
}
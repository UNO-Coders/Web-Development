fn main() {}

pub fn annotate(minefield: &[&str]) -> Vec<String> {
    let mut result: Vec<String> = Vec::new();

    // base condition
    if minefield.is_empty() {
        return result;
    }

    let x: [i32; 8] = [-1, -1, -1, 0, 0, 1, 1, 1];
    let y: [i32; 8] = [-1, 0, 1, -1, 1, -1, 0, 1];

    let n = minefield.len();
    let m = minefield[0].len();
    // println!("n: {}\tm:{}", n, m);
    for (i, row) in minefield.iter().enumerate() {
        let mut result_row = String::from("");
        for (j, col) in row.chars().into_iter().enumerate() {
            if col == ' ' {
                let mut count: usize = 0;
                // println!("position: {}x{}", i, j);
                for k in 0..8 {
                    let new_i = i as i32 + x[k];
                    if new_i < 0 {
                        continue;
                    } else if new_i >= n as i32 {
                        continue;
                    }

                    let new_j = j as i32 + y[k];
                    if new_j < 0 {
                        continue;
                    } else if new_j >= m as i32 {
                        continue;
                    }
                    // println!("   ====>checking positions: {}x{}", new_i, new_j);
                    if minefield[new_i as usize]
                        .chars()
                        .nth(new_j as usize)
                        .unwrap()
                        == '*'
                    {
                        count += 1;
                    }
                }
                if count != 0 {
                    result_row.push_str(format!("{}", count).as_str());
                } else {
                    result_row.push_str(" ");
                }
            } else {
                result_row.push_str("*");
            }
        }
        result.push(result_row);
    }

    result
}

#[cfg(test)]
mod tests {
    use crate::annotate;
    #[test]
    fn empty() {
        let input = &[];
        let expected: Vec<String> = Vec::new();
        assert_eq!(expected, annotate(input));
    }
    #[test]
    fn no_column() {
        let input = &[""];
        let expected: Vec<String> = Vec::new();
        assert_eq!(expected, annotate(input));
    }
    #[test]
    fn no_mines() {
        let input = &["   ", "   ", "   "];
        let expected: Vec<String> = Vec::new();
        assert_eq!(expected, annotate(input));
    }
    #[test]
    fn instruct_input() {
        let input = &[" * * ", "  *  ", "  *  ", "     "];
        let expected: Vec<String> = Vec::new();
        assert_eq!(expected, annotate(input));
    }
}

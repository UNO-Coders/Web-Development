fn main() {
    println!("Hello, World");
}

///function checkLuhn(string purportedCC) {
///    int nDigits := length(purportedCC)
///    int sum := 0;
///    int parity := (nDigits-2)modulus 2
///    for i from 0 to nDigits - 1 {
///        int digit := integer(purportedCC[i])
///        if i modulus 2 = parity
///            digit := digit × 2
///        if digit > 9
///            digit := digit - 9
///        sum := sum + digit
///    }
///    return (sum modulus 10) = 0
///}
pub fn is_valid(code: &str) -> bool {
    // base condition
    if code.is_empty() {
        return false;
    }
    let without_spaces = code.replace(" ", "");
    let code_chars = without_spaces.chars();
    let n_digits = without_spaces.len();
    if n_digits < 2 {
        // another base condition or an edge case
        return false;
    }
    let mut sum = 0;
    let parity = (n_digits - 2) % 2;
    for (i, ch) in code_chars.enumerate() {
        if !ch.is_ascii_digit() {
            return false;
        }
        let mut digit = ch.to_string().parse::<i32>().unwrap();
        if i % 2 == parity {
            digit *= 2;
        }
        if digit > 9 {
            digit -= 9;
        }
        sum += digit;
    }
    return sum % 10 == 0;
}

#[cfg(test)]
mod tests {
    #[test]
    fn empty() {}
}

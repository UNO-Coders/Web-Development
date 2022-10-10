use std::collections::HashMap;
use std::sync::{Arc, Mutex};
use std::thread;
const INPUT: [&str; 8] = [
    "Freude schöner Götterfunken",
    "Tochter aus Elysium,",
    "Wir betreten feuertrunken,",
    "Himmlische, dein Heiligtum!",
    "Deine Zauber binden wieder",
    "Was die Mode streng geteilt;",
    "Alle Menschen werden Brüder,",
    "Wo dein sanfter Flügel weilt.",
];
fn main() {
    frequency(&INPUT, 10);
}

pub fn frequency(input: &[&str], worker_count: usize) -> HashMap<char, usize> {
    let result = Arc::new(Mutex::new(HashMap::new()));
    let data: Vec<String> = input.iter().map(|s| s.to_lowercase()).collect();
    let arc_data = Arc::new(data);

    let mut threads = vec![];

    for i in 0..worker_count {
        let data = arc_data.clone();
        let kk = result.clone();
        let mut k = i;

        let t = thread::spawn(move || {
            let mut temp = kk.lock().unwrap();
            while k < data.len() {
                // println!("i: {}\tk: {}\tk+worker_count: {}", i, k, k + worker_count);
                for c in data.get(k).unwrap().chars().filter(|c| c.is_alphabetic()) {
                    *temp.entry(c).or_insert(0) += 1;
                }
                k += worker_count;
            }
        });

        threads.push(t);
    }

    for handler in threads {
        handler.join().unwrap();
    }

    let val = &*result.lock().unwrap();
    val.to_owned()
}

#[cfg(test)]
mod tests {
    #[test]
    fn print_hello_world() {
        crate::main()
    }
}

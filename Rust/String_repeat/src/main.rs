fn main() {
    println!("{}", repeatStr("Hello", 6));
}

fn repeatStr(src: &str, count: usize) ->String{
    let mut s = String::new();
    let mut c = count;
    while c != 0 {
        s = s + &src;
        c = c - 1;
    }
    s
}

use std::iter::repeat;

fn repeatStr(src: &str, count: usize) -> String{
    repeat(src).take(count).collect()
}


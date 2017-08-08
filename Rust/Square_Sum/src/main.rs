fn main() {
    let v = vec![1, 2, 2];
    println!("Sum: {}", square_sun(v));
}

fn square_sum(vec: Vec<i32>) ->i32{
    let mut count = 0;
    for element in vec.iter(){
        count = count + element * element;
    }
    count
}

fn square_sun(vec: Vec<i32>) -> i32{
    vec.iter().fold(0, |t, i| t + i*i)
}
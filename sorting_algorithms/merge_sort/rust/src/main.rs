
fn merge_sort<T:Clone + Ord>(arg: &[T]) -> ~[T] {
    unimplemented!();
}

// TODO: Figure out proptest crate...
// proptest! {
    // #[test]
    // fn bleh(){
    //     assert!(true == true);;
    // }
// }

fn main() {
    println!("Hello, world!");
    let mut list = vec![
        4,
        1,
        3,
        2,
    ] as Vec<i32>;
    merge_sort(&mut list);
}

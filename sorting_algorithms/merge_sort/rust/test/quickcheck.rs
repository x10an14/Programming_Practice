#![feature(plugin)]
#![plugin(quickcheck_macros)]

#[cfg(test)]
extern crate quickcheck;

// #[cfg(test)]
// mod tests {
//     fn reverse<T: Clone>(xs: &[T]) -> Vec<T> {
//         let mut rev = vec!();
//         for x in xs {
//             rev.insert(0, x.clone())
//         }
//         rev
//     }

//     #[quickcheck]
//     fn double_reversal_is_identity(xs: Vec<isize>) -> bool {
//         xs == reverse(&reverse(&xs))
//     }
// }


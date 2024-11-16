## Plotting instruction for HP 7440A

* To create HPGL from text, use [typewriter](https://github.com/WesleyAC/plotter-tools/tree/master/typewriter). Example `cargo run -- [x] [y] [size] "STRING" /path/font.ttf > /new_file.hpgl`
* To plot, use [chunker](https://github.com/WesleyAC/plotter-tools/tree/master/chunker). Example: `sudo ./target/debug/chunker ~/path/file.hpgl /dev/tty.usbserial-[num]`

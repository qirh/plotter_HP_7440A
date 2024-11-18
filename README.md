## Plotting instruction for HP 7440A

Helpful repos:
* https://github.com/codekitchen/drawbot
* https://github.com/abey79/vpype
* https://github.com/WesleyAC/plotter-tools
* https://github.com/dbalan/plotter-scripts

To create HPGL from text, use [typewriter](https://github.com/WesleyAC/plotter-tools/tree/master/typewriter). Example:
  `cargo run -- [x] [y] [size] "STRING" /path/font.ttf > /new_file.hpgl`

To plot a HPGL, use [chunker](https://github.com/WesleyAC/plotter-tools/tree/master/chunker). Example:
  `sudo ./target/debug/chunker ~/path/file.hpgl /dev/tty.usbserial-[num]`
 
![name_tag](https://github.com/user-attachments/assets/93c80d2d-8c12-41ad-8b10-d6644f85c997)

https://github.com/user-attachments/assets/8c248b19-73fd-4116-96b5-ca7d240a77f8

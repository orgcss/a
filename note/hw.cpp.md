# hello world cpp & asm & rust
## ubuntu
apt install g++; apt install nasm

curl https://sh.rustup.rs -sSf | sh; --.cargo, .rustup(1.1G,toolchain), .cargo/env
```cpp
#include <stdio.h>
int main(){
  printf("hw");
}
```
```asm
global _start

section .text:

_start:
  mov eax, 0x4
  mov ebx, 1
  mov ecx, msg
  mov edx, msg_len
  int 0x80
  
  mov eax, 0x1
  mov ebx, 0
  int 0x80
  
section .data:
  msg: db "Hello world css!", 0xA
  msg_len equ $-msg
```
```
fn main(){
  println!("hw rust!");
}
```
- nasm -f elf
- ld -m elf_i386
- objdump -D
- readelf --sections

## win10
google "MinGW c compiler", download setup.exe and run manager, mark base, c++ to install.

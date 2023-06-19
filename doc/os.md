## 启动
- BIOS
  - MBR
- UEFI
  - boot manager固件 -> efi文件在ESP FAT上, /efi/boot/bootx64.efi
- virtualbox
  - 打开efi支持
  - 不停按F2进boot manager,设boot order, 从efi文件启动，从光盘启动，等
## 显示
- X11
  - client(window managers, compositors, apps)->x server->device
- wayland
  - client->compositor->device
  - security
- ubuntu mir

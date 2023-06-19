## 启动
- BIOS
  - MBR
- UEFI
  - boot manager固件 -> efi文件在ESP FAT上, /efi/boot/bootx64.efi
  - efi文件: 在edk2用c开发的pre-os程序
- virtualbox uefi
  - 打开efi支持
  - 不停按F2进boot manager,设boot order, 从efi文件启动，从光盘启动，等
- 光盘: genisoimage
- 软盘:
  ```bash
  dd if=/dev/zero of=hw.img bs=512 count=1
  losetup /dev/loop0 hw.img
  mkfs.msdos /dev/loop0
  losetup -d /dev/loop0
  mount -o loop hw.img .tmp
  ```
## 显示
- X11
  - client(window managers, compositors, apps)->x server->device
- wayland
  - client->compositor->device
  - security
- ubuntu mir

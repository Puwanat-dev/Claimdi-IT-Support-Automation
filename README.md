# Claimdi-IT-Support-Automation
Tha Project That I made for automation my IT Support routine when I work at Claimdi

Source path configuration
-------------------------
Create `source_base.xlsx` in the project folder and put the image source root
path in cell `C2`, for example `P:\pic.claimdi.com\bike\ImageInspection`.
The application reads this value when `ImagePacker` starts. A different workbook
can be supplied with `ImagePacker(pic_path, source_base_file=...)`.

1. Download ISO image from Microsoft official site:

https://www.microsoft.com/de-de/software-download/windows10ISO

2. Create windows installation disk

3. Split install.wim file so it won't exceed 4GB

wimsplit /tmp/winiso/sources/install.wim install.swm 2048

and delete install.wim in the install USB, copy wim files to substitute it.
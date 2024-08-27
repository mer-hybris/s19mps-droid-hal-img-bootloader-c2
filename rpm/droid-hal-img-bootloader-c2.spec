Name:       droid-hal-img-bootloader-c2
Version:    1.0
Release:    1
License:    Proprietary
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch
Summary:    Bootloader and logo images for C2 device

%description
Bootloader and logo images for C2 device.

%prep

%autosetup

%build

%install
mkdir -p %{buildroot}/boot/
install -m 644 lk.bin %{buildroot}/boot/lk.bin
install -m 644 logo.bin %{buildroot}/boot/logo.bin

%post
# When doing install that is done during the image creation thus we don't add
# the oneshot on install but on all other cases.
if [ $1 -ne 1 ] ; then
  add-preinit-oneshot /var/lib/platform-updates/flash-bootloader.sh || :
fi

%files
%defattr(-,root,root,-)
/boot/lk.bin
/boot/logo.bin


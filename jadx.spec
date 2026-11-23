Name:           jadx
Version:        1.5.7
Release:        1%{?dist}
Summary:        Dex to Java decompiler

License:        Apache-2.0
URL:            https://github.com/skylot/%{name}
BugURL:	        https://github.com/infiniti151/%{name}-copr

Source0:        %{URL}/releases/download/v%{version}/%{name}-%{version}.zip
Source1:        %{URL}/raw/v%{version}/%{name}-gui/src/main/resources/logos/%{name}-logo.png

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  unzip

# Allow either Java 25 LTS or Java 27 (full runtime required for Swing/AWT in jadx-gui)
Requires:       (java-25-openjdk or java-27-openjdk)

%description
Command line and GUI tools for producing Java source code from Android Dex,
APK, AAB, APKS, APKM, XAPK, JAR, Class, AAR, and Smali files. Includes a
deobfuscator and AndroidManifest.xml/resources.arsc decoder.

%prep
%autosetup -c -n %{name}-%{version}

# Remove Windows batch scripts
rm -f bin/*.bat

%build
# Prebuilt universal JAR bundle; nothing to compile

%install
install -d -m 0755 %{buildroot}%{_datadir}/%{name}/bin
install -d -m 0755 %{buildroot}%{_datadir}/%{name}/lib
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

install -m 0755 bin/%{name} bin/%{name}-gui %{buildroot}%{_datadir}/%{name}/bin/
install -m 0644 lib/*.jar %{buildroot}%{_datadir}/%{name}/lib/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

ln -s ../share/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}
ln -s ../share/%{name}/bin/%{name}-gui %{buildroot}%{_bindir}/%{name}-gui

cat << 'EOF' > %{buildroot}%{_datadir}/applications/%{name}-gui.desktop
[Desktop Entry]
Name=JADX GUI
Comment=Dex to Java decompiler
Exec=%{name}-gui %F
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;Debugger;
MimeType=application/vnd.android.package-archive;application/java-archive;
StartupWMClass=%{name}-gui-JadxGUI
EOF

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop

test -x %{buildroot}%{_datadir}/%{name}/bin/%{name}
test -x %{buildroot}%{_datadir}/%{name}/bin/%{name}-gui
test -L %{buildroot}%{_bindir}/%{name}
test -L %{buildroot}%{_bindir}/%{name}-gui
test -s %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
ls %{buildroot}%{_datadir}/%{name}/lib/*.jar >/dev/null

%files
%license LICENSE NOTICE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

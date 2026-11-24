# jadx-copr
<img src="https://raw.githubusercontent.com/skylot/jadx/master/jadx-gui/src/main/resources/logos/jadx-logo.png" align="right" width="130" alt="jadx logo">

[![Build](https://img.shields.io/github/actions/workflow/status/Infiniti151/jadx-copr/copr-build.yml?branch=main&style=for-the-badge&logo=github-actions&logoColor=white&label=Build)](https://github.com/Infiniti151/jadx-copr/actions/workflows/copr-build.yml)
[![COPR Build Status](https://img.shields.io/badge/dynamic/json?url=https://copr.fedorainfracloud.org/api_3/build/list/%3Fownername%3Dinfiniti151%26projectname%3Djadx%26limit%3D1&query=$.items[0].state&label=COPR&style=for-the-badge&logo=fedora&logoColor=white&color=%2351A2DA)](https://copr.fedorainfracloud.org/coprs/infiniti151/jadx/)
[![jadx version](https://img.shields.io/badge/jadx-1.5.7-pink?style=for-the-badge&logo=android)](https://github.com/skylot/jadx/releases)
[![Fedora Versions](https://img.shields.io/badge/Fedora-44%20%7C%2045%20%7C%20Rawhide%20%7C%20ELN-3c6eb4?style=for-the-badge&logo=fedora&logoColor=white)](https://fedoraproject.org/)
![Arch x86_64 | arm64](https://img.shields.io/badge/Arch-x86__64%20%7C%20arm64-purple?style=for-the-badge)
[![License](https://img.shields.io/github/license/Infiniti151/jadx-copr?style=for-the-badge&logo=spdx&logoColor=white&color=yellow&label=License)](https://github.com/Infiniti151/jadx-copr/blob/main/LICENSE)

Fedora packaging for [jadx](https://github.com/skylot/jadx), a command-line
and graphical decompiler for producing Java source code from Android Dex and
APK files.

Built from upstream `jadx` release archives using an FHS-compliant layout
(`/usr/share/jadx/` with symlinks in `/usr/bin/`), providing both `jadx` and
`jadx-gui` with desktop integration and an OpenJDK runtime dependency.

**Copr project:** <https://copr.fedorainfracloud.org/coprs/infiniti151/jadx>

## Install

```bash
sudo dnf copr enable infiniti151/jadx
sudo dnf install jadx
```

## License

The packaging files in this repository (the spec file, README and scripts) are
licensed under the [MIT License](LICENSE).

`jadx` itself is licensed separately, under Apache-2.0. See the
[upstream repository](https://github.com/pskylot/jadx).

The jadx logo at the top is loaded from the upstream repository and is not covered by the license of this repository.
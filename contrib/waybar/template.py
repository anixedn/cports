pkgname = "waybar"
pkgver = "0.10.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dcava=disabled",
    "-Ddbusmenu-gtk=enabled",
    "-Djack=disabled",
    "-Dlibevdev=enabled",
    "-Dlibinput=enabled",
    "-Dlibnl=enabled",
    "-Dlibudev=enabled",
    "-Dlogind=enabled",
    "-Dman-pages=enabled",
    "-Dmpd=enabled",
    "-Dmpris=enabled",
    "-Dpipewire=enabled",
    "-Dpulseaudio=disabled",
    "-Drfkill=enabled",
    "-Dsndio=disabled",
    "-Dsystemd=disabled",
    "-Dtests=enabled",
    "-Dupower_glib=enabled",
    "-Dwireplumber=enabled",
]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-protocols",
]
makedepends = [
    "catch2-devel",
    "fmt-devel",
    "gtk-layer-shell-devel",
    "gtkmm3.0-devel",
    "jsoncpp-devel",
    "libdbusmenu-devel",
    "libevdev-devel",
    "libgirepository-devel",
    "libinput-devel",
    "libmpdclient-devel",
    "libnl-devel",
    "libsigc++2-devel",
    "libxkbcommon-devel",
    "pipewire-devel",
    "playerctl-devel",
    "spdlog-devel",
    "udev-devel",
    "upower-devel",
    "wayland-devel",
    "wireplumber-devel",
]
pkgdesc = "Wayland bar for Sway and wlroots-based compositors"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "MIT"
url = "https://github.com/Alexays/Waybar"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3af6665889868f2334ba1793c8b0f3104c4c3b176a8c759f0d08f07266ad2620"
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")

pkgname = "date"
pkgver = "3.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_SYSTEM_TZ_DB=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DENABLE_DATE_TESTING=ON",
    "-DBUILD_TZ_LIB=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
checkdepends = ["bash"]
pkgdesc = "Date and time library based on the C++11/14/17 <chrono> header"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "MIT"
url = "https://howardhinnant.github.io/date/date.html"
source = f"https://github.com/HowardHinnant/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7a390f200f0ccd207e8cff6757e04817c1a0aec3e327b006b7eb451c57ee3538"
hardening = ["cfi", "vis"]
# 37 of 108 tests fail
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("date-devel")
def _devel(self):
    return self.default_devel()

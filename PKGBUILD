# Maintainer: fhdk <fh at manjaro org>

pkgname=manjaro-application-utility
pkgver=1.0
pkgrel=1
pkgdesc="Manjaro Application Utility"
arch=('any')
license=('MIT')
depends=("python" "gtk3" "python-gobject" "zenity" "manjaro-icons" "pamac")
source=("app-utility" "app-utility.desktop" "default.json" "advanced.json" "LICENSE")
provides=('manjaro-application-utility')
conflicts=('manjaro-software-install-tool')
replaces=('manjaro-software-install-tool')
sha256sums=('4a6fec6f9e22977f4a859c7234c3ddacbce2829ddd8531c5c16386e232724848'
            '6efdedb8b3dc150e17d946b60e8d6681365018ce7b096356c3189f6dce749abf'
            '3f2ada3842e8e0c97c2d67b729dddf734a9359c626151c5337451122316df7b9'
            '25cd0258d3aa28c6047a3169803b734249ec0514f23c0ad0b8acb7b5ea5d51af'
            '56e5360e91198fbcde04a9775758ae669cddb73123b9d89944ca9572bcefb9cf'
            '198fa22b0f276c8810470fbb3cec7fac6fb48473092daeb150668c1610a7f52f')

package() {
    install -Dm644 "default.json" "$pkgdir/usr/share/app-utility/default.json"
    install -Dm644 "advanced.json" "$pkgdir/usr/share/app-utility/advanced.json"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/app-utility/LICENSE"
    install -Dm644 "app-utility.desktop" "$pkgdir/usr/share/applications/app-utility.desktop"
    install -Dm755 "app-utility" "$pkgdir/usr/bin/app-utility"
}


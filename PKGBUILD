# Maintainer: fhdk <fh at manjaro org>

pkgname=manjaro-application-utility
pkgver=0.7.3
pkgrel=2
pkgdesc="Manjaro Application Utility"
arch=('any')
license=('MIT')
depends=("python" "gtk3" "python-gobject" "zenity" "manjaro-icons")
source=("app-install" "app-utility" "app-utility.desktop" "default.json" "advanced.json" "LICENSE")
provides=('manjaro-application-utility')
conflicts=('manjaro-software-install-tool')
replaces=('manjaro-software-install-tool')
sha256sums=('4a6fec6f9e22977f4a859c7234c3ddacbce2829ddd8531c5c16386e232724848'
            '4e75efb1729f38e338d880b005ef5f39b1276e54cda811be2f5945ef1257f716'
            '3f2ada3842e8e0c97c2d67b729dddf734a9359c626151c5337451122316df7b9'
            'dedbf65f44033a330d76dbeacda449942ac6133292bad7e236bf38eaca7343d5'
            '7a05876d3bedd97f01064ef97246e9c7ab6bffdf0f71f5bb023e769e7de06dcd'
            '198fa22b0f276c8810470fbb3cec7fac6fb48473092daeb150668c1610a7f52f')

package() {
    install -Dm644 "default.json" "$pkgdir/usr/share/app-utility/default.json"
    install -Dm644 "advanced.json" "$pkgdir/usr/share/app-utility/advanced.json"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/app-utility/LICENSE"
    install -Dm644 "app-utility.desktop" "$pkgdir/usr/share/applications/app-utility.desktop"
    install -Dm755 "app-utility" "$pkgdir/usr/bin/app-utility"
    install -Dm755 "app-install" "$pkgdir/usr/bin/app-install"
}


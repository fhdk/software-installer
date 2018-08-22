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
            '4fe547e7b133cf94e28d83f12ed01e81a07e2679b4f1697b409d65ba84304fa6'
            '3f2ada3842e8e0c97c2d67b729dddf734a9359c626151c5337451122316df7b9'
            'aff497c86b0ee505fd58b2e83eb8895cff4d85f4cf25bb12d4a98ffba2697e51'
            '481ae4b3e8c4e92b80ffb9eec287c45dbfa71556b863217b668679853c38fa5a'
            '198fa22b0f276c8810470fbb3cec7fac6fb48473092daeb150668c1610a7f52f')

package() {
    install -Dm644 "default.json" "$pkgdir/usr/share/app-utility/default.json"
    install -Dm644 "advanced.json" "$pkgdir/usr/share/app-utility/advanced.json"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/app-utility/LICENSE"
    install -Dm644 "app-utility.desktop" "$pkgdir/usr/share/applications/app-utility.desktop"
    install -Dm755 "app-utility" "$pkgdir/usr/bin/app-utility"
    install -Dm755 "app-install" "$pkgdir/usr/bin/app-install"
}


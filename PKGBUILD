# Maintainer: fhdk <fh at manjaro org>

pkgname=manjaro-application-utility
pkgver=1.0
pkgrel=5
pkgdesc="Manjaro Application Utility"
arch=('any')
license=('MIT')
depends=("python" "gtk3" "python-gobject" "zenity" "manjaro-icons" "pamac>=6.9.0")
source=("app-utility" "app-utility.desktop" "default.json" "advanced.json" "LICENSE")
provides=('manjaro-application-utility')
conflicts=('manjaro-software-install-tool')
replaces=('manjaro-software-install-tool')
sha256sums=('c6c7961371f6ada44bbb449bd97e91e033d56cf18d72d60be8fae978ceceb537'
            '3f2ada3842e8e0c97c2d67b729dddf734a9359c626151c5337451122316df7b9'
            'ffa2d0e41dc31f198d8b107d82add1b951dd2e7881b0b0d33b2a56cb19152d7a'
            'fd45c3975900bec901dd089189a2e1666adc6d2def536e3b5df878bc032f58b3'
            '198fa22b0f276c8810470fbb3cec7fac6fb48473092daeb150668c1610a7f52f')

package() {
    install -Dm644 "default.json" "$pkgdir/usr/share/app-utility/default.json"
    install -Dm644 "advanced.json" "$pkgdir/usr/share/app-utility/advanced.json"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/app-utility/LICENSE"
    install -Dm644 "app-utility.desktop" "$pkgdir/usr/share/applications/app-utility.desktop"
    install -Dm755 "app-utility" "$pkgdir/usr/bin/app-utility"
}


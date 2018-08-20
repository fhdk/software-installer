# Maintainer: fhdk <fh at manjaro org>

pkgname=manjaro-application-utility
pkgver=0.7
pkgrel=4
pkgdesc="Manjaro Application Utility"
arch=('any')
license=('MIT')
depends=("python" "gtk3" "python-gobject" "zenity" "manjaro-icons")
source=("app-install" "app-utility" "app-utility.desktop" "apps.json" "LICENSE")
provides=('manjaro-application-utility')
conflicts=('manjaro-software-install-tool')
replaces=('manjaro-software-install-tool')
sha256sums=('c06ebcaeaabe8eefc71e27ce6f4ad9ed0d6fecd990c8b1dcb099ee2986f4efd8'
            '3aacc6b2780db1ff9948e94db74204ebd6a7954b45759b62cb5209fd45b8659a'
            '3f2ada3842e8e0c97c2d67b729dddf734a9359c626151c5337451122316df7b9'
            '058c5015e2a5db6d730270d8f1e0a8157969bdc7411a23c95dd56be292d0bc8d'
            'b214e41e35b078f2e19c73e8fd3a4298678444d23efee53b8d25283432419987')

package() {
    install -Dm644 "apps.json" "$pkgdir/usr/share/app-utility/apps.json"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/app-utility/LICENSE"
    install -Dm755 "app-utility" "$pkgdir/usr/bin/app-utility"
    install -Dm755 "app-install" "$pkgdir/usr/bin/app-install"
    install -Dm644 "app-utility.desktop" "$pkgdir/usr/share/applications/app-utility.desktop"
}


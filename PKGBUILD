# Maintainer: fhdk <fh at manjaro org>

pkgname=manjaro-application-utility
pkgver=0.7.1
pkgrel=2
pkgdesc="Manjaro Application Utility"
arch=('any')
license=('MIT')
depends=("python" "gtk3" "python-gobject" "zenity" "manjaro-icons")
source=("app-install" "app-utility" "app-utility.desktop" "apps.json" "LICENSE")
provides=('manjaro-application-utility')
conflicts=('manjaro-software-install-tool')
replaces=('manjaro-software-install-tool')
sha256sums=('c06ebcaeaabe8eefc71e27ce6f4ad9ed0d6fecd990c8b1dcb099ee2986f4efd8'
            'c92a74048334ee7745fdca909406fb322618604c45b231e0a01618695caf375b'
            '3f2ada3842e8e0c97c2d67b729dddf734a9359c626151c5337451122316df7b9'
            '9d52260bc49d33705524db6868ba9c032a1969d988edc7818392babdf9cd7a6b'
            'b214e41e35b078f2e19c73e8fd3a4298678444d23efee53b8d25283432419987')

package() {
    install -Dm644 "apps.json" "$pkgdir/usr/share/app-utility/apps.json"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/app-utility/LICENSE"
    install -Dm755 "app-utility" "$pkgdir/usr/bin/app-utility"
    install -Dm755 "app-install" "$pkgdir/usr/bin/app-install"
    install -Dm644 "app-utility.desktop" "$pkgdir/usr/share/applications/app-utility.desktop"
}


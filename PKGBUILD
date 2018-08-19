# Maintainer: fhdk <fh at manjaro org>

pkgname=manjaro-application-utility
pkgver=0.1
pkgrel=1
pkgdesc="Manjaro Application Utility"
arch=('any')
license=('MIT')
depends=("python" "gtk3" "python-gobject" "zenity")
source=("app-install" "app-utility" "app-utility.desktop" "apps.json" "LICENSE")
provides=('manjaro-application-utility')
sha256sums=('05218d733cdccd21e0287ea7d74eb43825f7fe12db0d25d45c963c41bbec2848'
            '7325eda56cc329715e6e3f752cbf0e07631ded15a5d58137effd88cf3e6f97f6'
            '3f2ada3842e8e0c97c2d67b729dddf734a9359c626151c5337451122316df7b9'
            'a2ae2d0feeb3a0605c0ac6d14c84792edb6ccad016a80a82b85fabf30c4d43d6'
            'b214e41e35b078f2e19c73e8fd3a4298678444d23efee53b8d25283432419987')

package() {
    install -Dm755 "apps.json" "$pkgdir/usr/share/app-utility/apps.json"
    install -Dm755 "LICENSE" "$pkgdir/usr/share/app-utility/LICENSE"
    install -Dm755 "app-utility" "$pkgdir/usr/bin/app-utility"
    install -Dm755 "app-install" "$pkgdir/usr/bin/app-install"
    install -Dm755 "app-utility.desktop" "$pkgdir/usr/share/applications/app-utility.desktop"
}


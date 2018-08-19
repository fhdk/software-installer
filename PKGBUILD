# Maintainer: fhdk <fh at manjaro org>

pkgname=manjaro-application-utility
pkgver=0.6
pkgrel=1
pkgdesc="Manjaro Application Utility"
arch=('any')
license=('MIT')
depends=("python" "gtk3" "python-gobject" "zenity" "manjaro-icons")
source=("app-install" "app-utility" "app-utility.desktop" "apps.json" "LICENSE")
provides=('manjaro-application-utility')
sha256sums=('8fed6d086302304a142d9f1ec50d330df7f7522564c1af762e64b0dcd6056b4a'
            'eb2a9be8865b18ccadf926235939e59122ab8348782501631aa5a3490dda228a'
            '3f2ada3842e8e0c97c2d67b729dddf734a9359c626151c5337451122316df7b9'
            '058c5015e2a5db6d730270d8f1e0a8157969bdc7411a23c95dd56be292d0bc8d'
            'b214e41e35b078f2e19c73e8fd3a4298678444d23efee53b8d25283432419987')

package() {
    install -Dm755 "apps.json" "$pkgdir/usr/share/app-utility/apps.json"
    install -Dm755 "LICENSE" "$pkgdir/usr/share/app-utility/LICENSE"
    install -Dm755 "app-utility" "$pkgdir/usr/bin/app-utility"
    install -Dm755 "app-install" "$pkgdir/usr/bin/app-install"
    install -Dm755 "app-utility.desktop" "$pkgdir/usr/share/applications/app-utility.desktop"
}


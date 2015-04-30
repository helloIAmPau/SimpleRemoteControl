# Copyright 1999-2010 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

DESCRIPTION="An mpd client embedded in your own gnome-panel"
HOMEPAGE="http://code.google.com/p/simplerc/"
SRC_URI="http://simplerc.googlecode.com/files/${P}.tar.gz"

LICENSE="gpl2"
SLOT="0"
KEYWORDS="~x86"
IUSE=""

DEPEND="dev-python/gnome-applets-python
		dev-python/notify-python"
RDEPEND="${DEPEND}"

src_install(){
cp * -vr ${D}
}

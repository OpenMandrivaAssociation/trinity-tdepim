%bcond clang 1
%bcond kitchensync 0
%bcond gamin 1
%bcond gnokii 1
%bcond xscreensaver 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg tdepim
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Summary:	Personal Information Management apps from the official Trinity release
Version:	%{tde_version}
Release:	%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Group:		Applications/Productivity
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:	%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ARTS=ON -DWITH_SASL=ON -DWITH_NEWDISTRLISTS=ON
BuildOption:    -DWITH_EXCHANGE=ON -DWITH_EGROUPWARE=ON -DWITH_KOLAB=ON
BuildOption:    -DWITH_SLOX=ON -DWITH_GROUPWISE=ON -DWITH_FEATUREPLAN=ON 
BuildOption:    -DWITH_GROUPDAV=ON -DWITH_BIRTHDAYS=ON -DWITH_NEWEXCHANGE=ON
BuildOption:    -DWITH_SCALIX=ON -DWITH_CALDAV=ON -DWITH_CARDDAV=ON 
BuildOption:    -DWITH_INDEXLIB=ON -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DWITH_GNOKII=%{!?with_gnokii:OFF}%{?with_gnokii:ON}
BuildOption:    -DWITH_XSCREENSAVER=%{!?with_xscreensaver:OFF}%{?with_xscreensaver:ON}
BuildOption:    -DBUILD_KITCHENSYNC=%{!?with_kitchensync:OFF}%{?with_kitchensync:ON}

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	libcaldav-devel >= %{tde_epoch}:0.6.5
BuildRequires:	libcarddav-devel >= %{tde_epoch}:0.6.2

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	fdupes
BuildRequires:	desktop-file-utils

BuildRequires:	pkgconfig(gpgme)
BuildRequires:	flex
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libidn)

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# ICAL support
BuildRequires:  pkgconfig(libical)

# GPG-ERROR support
BuildRequires:  pkgconfig(gpg-error)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# ACL support
BuildRequires:  pkgconfig(libacl)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# KDEPIM specific features
%{?with_gnokii:BuildRequires:  pkgconfig(gnokii)}

# BISON support
BuildRequires:	bison

# CURL support
BuildRequires:	pkgconfig(libcurl)

# GLIB2 support
BuildRequires:	pkgconfig(glib-2.0)

# SASL support
BuildRequires:  pkgconfig(libsasl2)

# XCOMPOSITE support
BuildRequires:  pkgconfig(xcomposite)

# XSCREENSAVER support
#  RHEL 4: disabled
#  RHEL 6: available in EPEL
#  RHEL 7: available in NUX
#  RHEL 8: available in EPEL
#  RHEL 9: available in EPEL
%if %{with xscreensaver}
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-base
BuildRequires:	xscreensaver-gl
BuildRequires:  pkgconfig(xscrnsaver)
%endif

BuildRequires:  pkgconfig(xrender)


Requires:	trinity-libtdepim = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-wizards = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-akregator = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kalarm = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kandy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-karm = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kleopatra = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kmail = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kmailcvt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kmobile = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knode = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knotes = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kode = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-konsolekalendar = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kontact = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-korganizer = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-korn = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-ktnef = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libindex = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkcal = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkgantt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkleopatra = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkmime = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimexchange = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimidentities = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libksieve = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libktnef = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libmimelib = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdepim < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdepim = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdepim < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdepim = %{?epoch:%{epoch}:}%{version}-%{release}

%description
This metapackage includes a collection of Personal Information Management
(PIM) applications provided with the official release of Trinity.

%files
%defattr(-,root,root,-)

##########

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries/Other

Obsoletes:	tdepim-cmake < %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdepim-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdepim-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-akregator-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kaddressbook-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-karm-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kmail-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knode-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knotes-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kode-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kontact-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-korganizer-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libindex-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkcal-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkgantt-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkleopatra-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkmime-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimexchange-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimidentities-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libksieve-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libktnef-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libmimelib-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tderesources-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This metapackage includes all development files for TDE PIM.
It also contains the CMAKE macros.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/share/cmake/*

##########

%package -n trinity-akregator
Summary:	RSS feed aggregator for TDE
Group:		Applications/Internet
Requires:	trinity-libtdepim = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkcal = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-akregator
aKregator is a fast, lightweight, and intuitive feed reader program
for TDE.  It allows you to quickly browse through hundreds of
thousands of internet feeds in a quick, efficient, and familiar way.

%files -n trinity-akregator
%defattr(-,root,root,-)
%{tde_prefix}/bin/akregator
%{tde_prefix}/%{_lib}/trinity/libakregatorpart.la
%{tde_prefix}/%{_lib}/trinity/libakregatorpart.so
%{tde_prefix}/%{_lib}/trinity/libakregator_mk4storage_plugin.la
%{tde_prefix}/%{_lib}/trinity/libakregator_mk4storage_plugin.so
%{tde_prefix}/%{_lib}/libakregatorprivate.so.*
%{tde_prefix}/share/applications/tde/akregator.desktop
%{tde_prefix}/share/apps/akregator
%{tde_prefix}/share/config.kcfg/akregator.kcfg
%{tde_prefix}/share/config.kcfg/mk4config.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/actions/rss_tag.png
%{tde_prefix}/share/icons/crystalsvg/16x16/apps/akregator_empty.png
%{tde_prefix}/share/icons/hicolor/*/apps/akregator.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/akregator.svgz
%{tde_prefix}/share/services/akregator_mk4storage_plugin.desktop
%{tde_prefix}/share/services/akregator_part.desktop
%{tde_prefix}/share/services/feed.protocol
%{tde_prefix}/share/services/kontact/akregatorplugin*.desktop
%{tde_prefix}/share/servicetypes/akregator_plugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/akregator/
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/feed/

##########

%package -n trinity-akregator-devel
Summary:	Development files for trinity-akregator
Group:		Development/Libraries/Other
Requires:	trinity-akregator = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-akregator-devel
%{summary}

%files -n trinity-akregator-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/akregator/
%{tde_prefix}/%{_lib}/libakregatorprivate.la
%{tde_prefix}/%{_lib}/libakregatorprivate.so

##########

%package -n trinity-kaddressbook
Summary:	TDE addressbook application
Group:		Applications/Communications
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
Requires:       %{_lib}sasl2-plug-anonymous
Requires:       %{_lib}sasl2-plug-crammd5
Requires:       %{_lib}sasl2-plug-digestmd5
Requires:       %{_lib}sasl2-plug-gssapi
Requires:       %{_lib}sasl2-plug-ldapdb
Requires:       %{_lib}sasl2-plug-login
Requires:       %{_lib}sasl2-plug-ntlm
Requires:       %{_lib}sasl2-plug-plain
%endif
Requires:	trinity-tdebase-tdeio-pim-plugins
Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kaddressbook
KAddressBook is the main address book application for TDE; it enables you
to manage your contacts efficiently and comfortably. It can load and save
your contacts to many different locations, including the local file system,
LDAP servers, and SQL databases.

%files -n trinity-kaddressbook
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdeabc2mutt
%{tde_prefix}/bin/kaddressbook
%{tde_prefix}/bin/tdeabcdistlistupdater
%{tde_prefix}/%{_lib}/trinity/kcm_kabconfig.la
%{tde_prefix}/%{_lib}/trinity/kcm_kabconfig.so
%{tde_prefix}/%{_lib}/trinity/kcm_kabcustomfields.la
%{tde_prefix}/%{_lib}/trinity/kcm_kabcustomfields.so
%{tde_prefix}/%{_lib}/trinity/kcm_kabldapconfig.la
%{tde_prefix}/%{_lib}/trinity/kcm_kabldapconfig.so
%{tde_prefix}/%{_lib}/trinity/ldifvcardthumbnail.la
%{tde_prefix}/%{_lib}/trinity/ldifvcardthumbnail.so
%{tde_prefix}/%{_lib}/trinity/libkaddrbk_*.la
%{tde_prefix}/%{_lib}/trinity/libkaddrbk_*.so
%{tde_prefix}/%{_lib}/trinity/libkaddressbookpart.la
%{tde_prefix}/%{_lib}/trinity/libkaddressbookpart.so
%{tde_prefix}/%{_lib}/libkabinterfaces.so.*
%{tde_prefix}/%{_lib}/libkaddressbook.so.*
%{tde_prefix}/share/applications/tde/kaddressbook.desktop
%{tde_prefix}/share/apps/kaddressbook
%{tde_prefix}/share/icons/hicolor/*/apps/kaddressbook.png
%{tde_prefix}/share/services/kabconfig.desktop
%{tde_prefix}/share/services/kabcustomfields.desktop
%{tde_prefix}/share/services/kabldapconfig.desktop
%{tde_prefix}/share/services/kaddressbook
%{tde_prefix}/share/services/kontact/kaddressbookplugin.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/imap.desktop
%{tde_prefix}/share/services/ldifvcardthumbnail.desktop
%{tde_prefix}/share/servicetypes/dcopaddressbook.desktop
%{tde_prefix}/share/servicetypes/kaddressbook_contacteditorwidget.desktop
%{tde_prefix}/share/servicetypes/kaddressbookimprotocol.desktop
%{tde_prefix}/share/servicetypes/kaddressbook_extension.desktop
%{tde_prefix}/share/servicetypes/kaddressbook_view.desktop
%{tde_prefix}/share/servicetypes/kaddressbook_xxport.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kaddressbook/
%{tde_prefix}/share/autostart/tdeabcdistlistupdater.desktop
%{tde_prefix}/include/tde/kaddressbook/
%{tde_prefix}/include/tde/tdeabc/

##########

%package -n trinity-kaddressbook-devel
Summary:	Development files for trinity-kaddressbook
Group:		Development/Libraries/Other
Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kaddressbook-devel
%{summary}

%files -n trinity-kaddressbook-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkabinterfaces.la
%{tde_prefix}/%{_lib}/libkabinterfaces.so
%{tde_prefix}/%{_lib}/libkaddressbook.la
%{tde_prefix}/%{_lib}/libkaddressbook.so

##########

%package -n trinity-kalarm
Summary:	Trinity alarm message, command and email scheduler
Group:		Applications/Communications
Requires:	trinity-libkpimidentities = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kalarm
KAlarm provides a graphical interface to schedule personal timed events -
pop-up alarm messages, command execution and sending emails. There is a
range of options for configuring recurring events.

A pop-up alarm can show either a simple text message, or the contents of a
text or image file, It can optionally be spoken, or play a sound file. You
can choose its appearance, and set reminders. Among KAlarm's other
facilities, you can set up templates to allow KAlarm to be used as a 'tea
timer'.

As an alternative to using the graphical interface, alarms can be scheduled
from the command line or via DCOP calls from other programs. KAlarm is
TDE-based, but will also run on other desktops.

%files -n trinity-kalarm
%defattr(-,root,root,-)
%{tde_prefix}/bin/kalarm
%{tde_prefix}/bin/kalarmd
%{tde_prefix}/share/applications/tde/kalarm.desktop
%{tde_prefix}/share/applnk/.hidden/kalarmd.desktop
%{tde_prefix}/share/applnk/Applications/kalarm.desktop
%{tde_prefix}/share/apps/kalarm
%{tde_prefix}/share/autostart/kalarm.tray.desktop
%{tde_prefix}/share/autostart/kalarmd.autostart.desktop
%{tde_prefix}/share/icons/crystalsvg/*/actions/kalarm.png
%{tde_prefix}/share/icons/hicolor/*/apps/kalarm.png
%{tde_prefix}/share/doc/tde/HTML/en/kalarm/

##########

%package -n trinity-kandy
Summary:	Trinity mobile phone utility
Group:		Applications/Communications

%description -n trinity-kandy
At the moment Kandy is more or less a terminal program with some special
features to store commands and their parameters, but is also has a simple GUI
to access the phone book of a mobile phone and it is able to save this phone
book to the TDE address book.

Kandy is aimed at mobile phones with integrated (GSM) modems.

%files -n trinity-kandy
%defattr(-,root,root,-)
%{tde_prefix}/bin/kandy
%{tde_prefix}/bin/kandy_client
%{tde_prefix}/share/applications/tde/kandy.desktop
%{tde_prefix}/share/applnk/Utilities/kandy.desktop
%{tde_prefix}/share/apps/kandy/
%{tde_prefix}/share/icons/crystalsvg/*/apps/kandy.png
%{tde_prefix}/share/icons/hicolor/*/apps/kandy.png
%{tde_prefix}/share/config.kcfg/kandy.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/kandy/

##########

%package -n trinity-karm
Summary:	Trinity time tracker tool
Group:		Applications/Productivity

%description -n trinity-karm
KArm is a time tracker for busy people who need to keep track of the amount of
time they spend on various tasks.

%files -n trinity-karm
%defattr(-,root,root,-)
%{tde_prefix}/bin/karm
%{tde_prefix}/%{_lib}/libkarm.so.*
%{tde_prefix}/%{_lib}/trinity/libkarmpart.la
%{tde_prefix}/%{_lib}/trinity/libkarmpart.so
%{tde_prefix}/share/applications/tde/karm.desktop
%{tde_prefix}/share/applnk/Utilities/karm.desktop
%{tde_prefix}/share/apps/karm/
%{tde_prefix}/share/apps/karmpart/
%{tde_prefix}/share/icons/hicolor/*/apps/karm.png
%{tde_prefix}/share/services/karm_part.desktop
%{tde_prefix}/share/services/kontact/karmplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/karm/

##########

%package -n trinity-karm-devel
Summary:	Development files for karm
Group:		Development/Libraries/Other

%description -n trinity-karm-devel
%{summary}

%files -n trinity-karm-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkarm.so
%{tde_prefix}/%{_lib}/libkarm.la

##########

%package kfile-plugins
Summary:	TDE File dialog plugins for palm and vcf files
Group:		Environment/Libraries

Obsoletes:	tdepim-kfile-plugins < %{?epoch:%{epoch}:}%{version}-%{release}

%description kfile-plugins
File dialog plugins for palm and vcf files.

%files kfile-plugins
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/tdefile_ics.la
%{tde_prefix}/%{_lib}/trinity/tdefile_ics.so
%{tde_prefix}/%{_lib}/trinity/tdefile_vcf.la
%{tde_prefix}/%{_lib}/trinity/tdefile_vcf.so
%{tde_prefix}/share/services/tdefile_ics.desktop
%{tde_prefix}/share/services/tdefile_vcf.desktop

##########

%package tdeio-plugins
Summary:	Trinity PIM I/O Slaves
Group:		Environment/Libraries

Obsoletes:	tdepim-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdepim-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdepim-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-plugins
This package includes the pim kioslaves. This includes imap4, sieve,
and mbox.

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/tdeio_groupwise.la
%{tde_prefix}/%{_lib}/trinity/tdeio_groupwise.so
%{tde_prefix}/%{_lib}/trinity/tdeio_imap4.la
%{tde_prefix}/%{_lib}/trinity/tdeio_imap4.so
%{tde_prefix}/%{_lib}/trinity/tdeio_mbox.la
%{tde_prefix}/%{_lib}/trinity/tdeio_mbox.so
%{tde_prefix}/%{_lib}/trinity/tdeio_scalix.la
%{tde_prefix}/%{_lib}/trinity/tdeio_scalix.so
%{tde_prefix}/%{_lib}/trinity/tdeio_sieve.la
%{tde_prefix}/%{_lib}/trinity/tdeio_sieve.so
%{tde_prefix}/share/services/groupwise.protocol
%{tde_prefix}/share/services/groupwises.protocol
%{tde_prefix}/share/services/imap4.protocol
%{tde_prefix}/share/services/imaps.protocol
%{tde_prefix}/share/services/mbox.protocol
%{tde_prefix}/share/services/scalix.protocol
%{tde_prefix}/share/services/scalixs.protocol
%{tde_prefix}/share/services/sieve.protocol
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/groupwise/
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/mbox/
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/scalix/

##########

%package tderesources
Summary:	Trinity pim resource plugins
Group:		Environment/Libraries
#Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:	trinity-korganizer = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:	trinity-knotes = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libcaldav
Requires:	libcarddav

Obsoletes:	tdepim-kresources < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdepim-kresources < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdepim-kresources = %{?epoch:%{epoch}:}%{version}-%{release}

%description tderesources
This package includes several plugins needed to interface with groupware
servers. It also includes plugins for features such as blogging and
tracking feature plans.

%files tderesources
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kcal_caldav.la
%{tde_prefix}/%{_lib}/trinity/kcal_caldav.so
%{tde_prefix}/%{_lib}/trinity/kcal_groupdav.la
%{tde_prefix}/%{_lib}/trinity/kcal_groupdav.so
%{tde_prefix}/%{_lib}/trinity/kcal_groupwise.la
%{tde_prefix}/%{_lib}/trinity/kcal_groupwise.so
%{tde_prefix}/%{_lib}/trinity/kcal_kolab.la
%{tde_prefix}/%{_lib}/trinity/kcal_kolab.so
%{tde_prefix}/%{_lib}/trinity/kcal_scalix.la
%{tde_prefix}/%{_lib}/trinity/kcal_scalix.so
%{tde_prefix}/%{_lib}/trinity/kcal_newexchange.la
%{tde_prefix}/%{_lib}/trinity/kcal_newexchange.so
%{tde_prefix}/%{_lib}/trinity/kcal_resourcefeatureplan.la
%{tde_prefix}/%{_lib}/trinity/kcal_resourcefeatureplan.so
%{tde_prefix}/%{_lib}/trinity/kcal_slox.la
%{tde_prefix}/%{_lib}/trinity/kcal_slox.so
%{tde_prefix}/%{_lib}/trinity/kcal_xmlrpc.la
%{tde_prefix}/%{_lib}/trinity/kcal_xmlrpc.so
%{tde_prefix}/%{_lib}/trinity/knotes_kolab.la
%{tde_prefix}/%{_lib}/trinity/knotes_kolab.so
%{tde_prefix}/%{_lib}/trinity/knotes_scalix.la
%{tde_prefix}/%{_lib}/trinity/knotes_scalix.so
%{tde_prefix}/%{_lib}/trinity/knotes_xmlrpc.la
%{tde_prefix}/%{_lib}/trinity/knotes_xmlrpc.so
%{tde_prefix}/%{_lib}/libtdeabckolab.so.*
%{tde_prefix}/%{_lib}/libtdeabcscalix.so.*
%{tde_prefix}/%{_lib}/libtdeabc_groupdav.so.*
%{tde_prefix}/%{_lib}/libtdeabc_groupwise.so.*
%{tde_prefix}/%{_lib}/libtdeabc_newexchange.so.*
%{tde_prefix}/%{_lib}/libtdeabc_slox.so.*
%{tde_prefix}/%{_lib}/libtdeabc_xmlrpc.so.*
%{tde_prefix}/%{_lib}/libkcalkolab.so.*
%{tde_prefix}/%{_lib}/libkcalscalix.so.*
%{tde_prefix}/%{_lib}/libkcal_caldav.so.*
%{tde_prefix}/%{_lib}/libtdeabc_carddav.so.*
%{tde_prefix}/%{_lib}/libkcal_groupdav.so.*
%{tde_prefix}/%{_lib}/libkcal_groupwise.so.*
%{tde_prefix}/%{_lib}/libkcal_newexchange.so.*
%{tde_prefix}/%{_lib}/libkcal_resourcefeatureplan.so.*
%{tde_prefix}/%{_lib}/libkcal_slox.so.*
%{tde_prefix}/%{_lib}/libkcal_xmlrpc.so.*
%{tde_prefix}/%{_lib}/libkgroupwarebase.so.*
%{tde_prefix}/%{_lib}/libkgroupwaredav.so.*
%{tde_prefix}/%{_lib}/libknoteskolab.so.*
%{tde_prefix}/%{_lib}/libknotesscalix.so.*
%{tde_prefix}/%{_lib}/libknotes_xmlrpc.so.*
%{tde_prefix}/%{_lib}/libkslox.so.*
%{tde_prefix}/%{_lib}/libgwsoap.so.*
%{tde_prefix}/share/services/tderesources/tdeabc/tdeabc_groupdav.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/tdeabc_groupwise.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/tdeabc_newexchange.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/tdeabc_opengroupware.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/tdeabc_ox.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/tdeabc_slox.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/tdeabc_xmlrpc.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/kolab.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/scalix.desktop
%dir %{tde_prefix}/share/services/tderesources/kcal
%{tde_prefix}/share/services/tderesources/kcal/exchange.desktop
%{tde_prefix}/share/services/tderesources/kcal/kcal_caldav.desktop
%{tde_prefix}/share/services/tderesources/tdeabc/tdeabc_carddav.desktop
%{tde_prefix}/share/services/tderesources/kcal/kcal_groupdav.desktop
%{tde_prefix}/share/services/tderesources/kcal/kcal_groupwise.desktop
%{tde_prefix}/share/services/tderesources/kcal/kcal_newexchange.desktop
%{tde_prefix}/share/services/tderesources/kcal/kcal_opengroupware.desktop
%{tde_prefix}/share/services/tderesources/kcal/kcal_ox.desktop
%{tde_prefix}/share/services/tderesources/kcal/kcal_resourcefeatureplan.desktop
%{tde_prefix}/share/services/tderesources/kcal/kcal_slox.desktop
%{tde_prefix}/share/services/tderesources/kcal/kcal_xmlrpc.desktop
%{tde_prefix}/share/services/tderesources/kcal/kolab.desktop
%{tde_prefix}/share/services/tderesources/kcal/scalix.desktop
%dir %{tde_prefix}/share/services/tderesources/knotes
%{tde_prefix}/share/services/tderesources/knotes/knotes_xmlrpc.desktop
%{tde_prefix}/share/services/tderesources/knotes/kolabresource.desktop
%{tde_prefix}/share/services/tderesources/knotes/scalix.desktop

%{tde_prefix}/share/apps/tdeconf_update/upgrade-resourcetype.pl
%{tde_prefix}/share/apps/tdeconf_update/kolab-resource.upd

%{tde_prefix}/%{_lib}/trinity/tdeabc_carddav.la
%{tde_prefix}/%{_lib}/trinity/tdeabc_carddav.so
%{tde_prefix}/%{_lib}/trinity/tdeabc_groupdav.la
%{tde_prefix}/%{_lib}/trinity/tdeabc_groupdav.so
%{tde_prefix}/%{_lib}/trinity/tdeabc_groupwise.la
%{tde_prefix}/%{_lib}/trinity/tdeabc_groupwise.so
%{tde_prefix}/%{_lib}/trinity/tdeabc_kolab.la
%{tde_prefix}/%{_lib}/trinity/tdeabc_kolab.so
%{tde_prefix}/%{_lib}/trinity/tdeabc_newexchange.la
%{tde_prefix}/%{_lib}/trinity/tdeabc_newexchange.so
%{tde_prefix}/%{_lib}/trinity/tdeabc_scalix.la
%{tde_prefix}/%{_lib}/trinity/tdeabc_scalix.so
%{tde_prefix}/%{_lib}/trinity/tdeabc_slox.la
%{tde_prefix}/%{_lib}/trinity/tdeabc_slox.so
%{tde_prefix}/%{_lib}/trinity/tdeabc_xmlrpc.la
%{tde_prefix}/%{_lib}/trinity/tdeabc_xmlrpc.so

##########

%package tderesources-devel
Summary:	Development files for tderesources
Group:		Development/Libraries/Other
Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	libcaldav
Requires:	libcarddav

Obsoletes:	tdepim-tderesources-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdepim-kresources-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdepim-kresources-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description tderesources-devel
%{summary}

%files tderesources-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkslox.la
%{tde_prefix}/%{_lib}/libkslox.so
%{tde_prefix}/%{_lib}/libtdeabc_groupdav.la
%{tde_prefix}/%{_lib}/libtdeabc_groupdav.so
%{tde_prefix}/%{_lib}/libtdeabc_groupwise.la
%{tde_prefix}/%{_lib}/libtdeabc_groupwise.so
%{tde_prefix}/%{_lib}/libgwsoap.la
%{tde_prefix}/%{_lib}/libgwsoap.so
%{tde_prefix}/%{_lib}/libtdeabc_carddav.la
%{tde_prefix}/%{_lib}/libtdeabc_carddav.so
%{tde_prefix}/%{_lib}/libtdeabc_newexchange.la
%{tde_prefix}/%{_lib}/libtdeabc_newexchange.so
%{tde_prefix}/%{_lib}/libtdeabc_slox.la
%{tde_prefix}/%{_lib}/libtdeabc_slox.so
%{tde_prefix}/%{_lib}/libtdeabc_xmlrpc.la
%{tde_prefix}/%{_lib}/libtdeabc_xmlrpc.so
%{tde_prefix}/%{_lib}/libtdeabckolab.la
%{tde_prefix}/%{_lib}/libtdeabckolab.so
%{tde_prefix}/%{_lib}/libtdeabcscalix.la
%{tde_prefix}/%{_lib}/libtdeabcscalix.so
%{tde_prefix}/%{_lib}/libkcal_caldav.la
%{tde_prefix}/%{_lib}/libkcal_caldav.so
%{tde_prefix}/%{_lib}/libkcal_groupdav.la
%{tde_prefix}/%{_lib}/libkcal_groupdav.so
%{tde_prefix}/%{_lib}/libkcal_groupwise.la
%{tde_prefix}/%{_lib}/libkcal_groupwise.so
%{tde_prefix}/%{_lib}/libkcal_newexchange.la
%{tde_prefix}/%{_lib}/libkcal_newexchange.so
%{tde_prefix}/%{_lib}/libkcal_resourcefeatureplan.la
%{tde_prefix}/%{_lib}/libkcal_resourcefeatureplan.so
%{tde_prefix}/%{_lib}/libkcal_slox.la
%{tde_prefix}/%{_lib}/libkcal_slox.so
%{tde_prefix}/%{_lib}/libkcal_xmlrpc.la
%{tde_prefix}/%{_lib}/libkcal_xmlrpc.so
%{tde_prefix}/%{_lib}/libkcalkolab.la
%{tde_prefix}/%{_lib}/libkcalkolab.so
%{tde_prefix}/%{_lib}/libkcalscalix.la
%{tde_prefix}/%{_lib}/libkcalscalix.so
%{tde_prefix}/%{_lib}/libkgroupwarebase.la
%{tde_prefix}/%{_lib}/libkgroupwarebase.so
%{tde_prefix}/%{_lib}/libkgroupwaredav.la
%{tde_prefix}/%{_lib}/libkgroupwaredav.so
%{tde_prefix}/%{_lib}/libknotes_xmlrpc.la
%{tde_prefix}/%{_lib}/libknotes_xmlrpc.so
%{tde_prefix}/%{_lib}/libknoteskolab.la
%{tde_prefix}/%{_lib}/libknoteskolab.so
%{tde_prefix}/%{_lib}/libknotesscalix.la
%{tde_prefix}/%{_lib}/libknotesscalix.so
%{tde_prefix}/include/tde/kpimprefs.h

##########

%package wizards
Summary:	Trinity server configuration wizards
Group:		Applications/Communications

Obsoletes:	tdepim-wizards < %{?epoch:%{epoch}:}%{version}-%{release}

%description wizards
This package contains TDE-based wizards for configuring eGroupware,
Kolab, and SUSE Linux Openexchange servers.

%files wizards
%defattr(-,root,root,-)
%{tde_prefix}/bin/egroupwarewizard
%{tde_prefix}/bin/exchangewizard
%{tde_prefix}/bin/groupwarewizard
%{tde_prefix}/bin/groupwisewizard
%{tde_prefix}/bin/kolabwizard
%{tde_prefix}/bin/scalixadmin
%{tde_prefix}/bin/scalixwizard
%{tde_prefix}/bin/sloxwizard
%{tde_prefix}/%{_lib}/trinity/libegroupwarewizard.la
%{tde_prefix}/%{_lib}/trinity/libegroupwarewizard.so
%{tde_prefix}/%{_lib}/trinity/libexchangewizard.la
%{tde_prefix}/%{_lib}/trinity/libexchangewizard.so
%{tde_prefix}/%{_lib}/trinity/libgroupwisewizard.la
%{tde_prefix}/%{_lib}/trinity/libgroupwisewizard.so
%{tde_prefix}/%{_lib}/trinity/libkolabwizard.la
%{tde_prefix}/%{_lib}/trinity/libkolabwizard.so
%{tde_prefix}/%{_lib}/trinity/libscalixwizard.la
%{tde_prefix}/%{_lib}/trinity/libscalixwizard.so
%{tde_prefix}/%{_lib}/trinity/libsloxwizard.la
%{tde_prefix}/%{_lib}/trinity/libsloxwizard.so
%{tde_prefix}/share/applications/tde/groupwarewizard.desktop
%{tde_prefix}/share/config.kcfg/egroupware.kcfg
%{tde_prefix}/share/config.kcfg/groupwise.kcfg
%{tde_prefix}/share/config.kcfg/kolab.kcfg
%{tde_prefix}/share/config.kcfg/scalix.kcfg
%{tde_prefix}/share/config.kcfg/slox.kcfg

##########

%if %{with kitchensync}
%package -n trinity-kitchensync
Summary:	Synchronization framework
Group:		Applications/Communications
BuildRequires:	opensync-devel
#Suggests: konqueror-trinity
#Conflicts: kdebluetooth-irmcsync-trinity (<< 0.99+1.0beta2-4.1), ksync-trinity

%description -n trinity-kitchensync
This package contains a synchronization framework, still under heavy
development (?).  Kitchensync uses opensync.

%files -n trinity-kitchensync
%defattr(-,root,root,-)
%{tde_prefix}/bin/kitchensync
%{tde_prefix}/%{_lib}/trinity/libkitchensyncpart.la
%{tde_prefix}/%{_lib}/trinity/libkitchensyncpart.so
%{tde_prefix}/share/apps/kitchensync
%{tde_prefix}/%{_lib}/libkitchensync.so.*
%{tde_prefix}/%{_lib}/libqopensync.so.*
%{tde_prefix}/share/applications/tde/kitchensync.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kitchensync.png
%endif

##########

%package -n trinity-kleopatra
Summary:	Trinity Certificate Manager
Group:		Applications/Communications

# GPG support
Requires:	pinentry
Requires:	gnupg

%description -n trinity-kleopatra
Kleopatra is the TDE tool for managing X.509 certificates in the gpgsm
keybox and for retrieving certificates from LDAP servers.

%files -n trinity-kleopatra
%defattr(-,root,root,-)
%{tde_prefix}/bin/kleopatra
%{tde_prefix}/bin/kwatchgnupg
%{tde_prefix}/%{_lib}/trinity/kcm_kleopatra.la
%{tde_prefix}/%{_lib}/trinity/kcm_kleopatra.so
%{tde_prefix}/share/applications/tde/kleopatra_import.desktop
%{tde_prefix}/share/apps/kleopatra
%{tde_prefix}/share/apps/kwatchgnupg
%{tde_prefix}/share/services/kleopatra_config_*.desktop
%{tde_prefix}/share/applications/tde/kleopatra.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kleopatra/
%{tde_prefix}/share/doc/tde/HTML/en/kwatchgnupg/
%{tde_prefix}/share/icons/hicolor/*/apps/kleopatra.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kleopatra.svgz

##########

%package -n trinity-kmail
Summary:	Trinity Email client
Group:		Applications/Communications

Requires:       %{_lib}sasl2-plug-anonymous
Requires:       %{_lib}sasl2-plug-crammd5
Requires:       %{_lib}sasl2-plug-digestmd5
Requires:       %{_lib}sasl2-plug-gssapi
Requires:       %{_lib}sasl2-plug-ldapdb
Requires:       %{_lib}sasl2-plug-login
Requires:       %{_lib}sasl2-plug-ntlm
Requires:       %{_lib}sasl2-plug-plain
Requires:	%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdebase-tdeio-pim-plugins >= %{tde_version}

# GPG support
Requires:	gnupg

# Pinentry
Requires:	pinentry

Requires:	procmail
Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kleopatra = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdebase-tdeio-pim-plugins >= %{tde_version}

Provides: imap-client, mail-reader

%description -n trinity-kmail
KMail is a fully-featured email client that fits nicely into the TDE
desktop. It has features such as support for IMAP, POP3, multiple accounts,
mail filtering and sorting, PGP/GnuPG privacy, and inline attachments.

You need to install %{name}-tdeio-plugins if you want to use IMAP or
mbox files, and/or trinity-tdebase-tdeio-plugins if you want to use POP3.

%files -n trinity-kmail
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/kmail.antispamrc
%config(noreplace) %{_sysconfdir}/trinity/kmail.antivirusrc
%{tde_prefix}/bin/kmail
%{tde_prefix}/bin/kmail_*.sh
%{tde_prefix}/%{_lib}/trinity/kcm_kmail.la
%{tde_prefix}/%{_lib}/trinity/kcm_kmail.so
%{tde_prefix}/%{_lib}/trinity/libkmail_bodypartformatter_application_octetstream.la
%{tde_prefix}/%{_lib}/trinity/libkmail_bodypartformatter_application_octetstream.so
%{tde_prefix}/%{_lib}/trinity/libkmail_bodypartformatter_text_calendar.la
%{tde_prefix}/%{_lib}/trinity/libkmail_bodypartformatter_text_calendar.so
%{tde_prefix}/%{_lib}/trinity/libkmail_bodypartformatter_text_vcard.la
%{tde_prefix}/%{_lib}/trinity/libkmail_bodypartformatter_text_vcard.so
%{tde_prefix}/%{_lib}/trinity/libkmail_bodypartformatter_text_xdiff.la
%{tde_prefix}/%{_lib}/trinity/libkmail_bodypartformatter_text_xdiff.so
%{tde_prefix}/%{_lib}/trinity/libkmailpart.la
%{tde_prefix}/%{_lib}/trinity/libkmailpart.so
%{tde_prefix}/share/applications/tde/KMail.desktop
%{tde_prefix}/share/applications/tde/kmail_view.desktop
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.1-update-new-mail-notification-settings.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.1-use-UOID-for-identities.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.1.4-dont-use-UOID-0-for-any-identity.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.2-misc.sh
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.2-update-loop-on-goto-unread-settings.sh
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.3-aegypten.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.3-misc.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.3-move-identities.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.3-split-sign-encr-keys.sh
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.3-use-ID-for-accounts.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.3b1-misc.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.4-misc.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.4.1-update-status-filters.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.5-trigger-flag-migration.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-3.5-filter-icons.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-pgpidentity.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail-upd-identities.pl
%{tde_prefix}/share/apps/tdeconf_update/kmail.upd
%{tde_prefix}/share/apps/tdeconf_update/upgrade-signature.pl
%{tde_prefix}/share/apps/tdeconf_update/upgrade-transport.pl
%{tde_prefix}/share/apps/kmail
%{tde_prefix}/share/apps/konqueror/servicemenus/email.desktop
%{tde_prefix}/share/config.kcfg/custommimeheader.kcfg
%{tde_prefix}/share/config.kcfg/kmail.kcfg
%{tde_prefix}/share/config.kcfg/customtemplates_kfg.kcfg
%{tde_prefix}/share/config.kcfg/replyphrases.kcfg
%{tde_prefix}/share/config.kcfg/templatesconfiguration_kfg.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/apps/kmaillight.png
%{tde_prefix}/share/icons/hicolor/*/apps/kmail.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kmail.svgz
%{tde_prefix}/share/services/kmail_config_*.desktop
%{tde_prefix}/share/services/kontact/kmailplugin.desktop
%{tde_prefix}/share/servicetypes/dcopimap.desktop
%{tde_prefix}/share/servicetypes/dcopmail.desktop
# 'libkmailprivate.so' is required at runtime, not devel !
%{tde_prefix}/%{_lib}/libkmailprivate.so
%{tde_prefix}/%{_lib}/libkmailprivate.la
%{tde_prefix}/share/doc/tde/HTML/en/kmail/

##########

%package -n trinity-kmail-devel
Summary:	Development files for kmail
Group:		Development/Libraries/Other

%description -n trinity-kmail-devel
%{summary}

%files -n trinity-kmail-devel
%defattr(-,root,root,-)
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/kmail/
%{tde_prefix}/include/tde/kmail*.h

##########
 
%package -n trinity-kmailcvt
Summary:	Trinity KMail mail folder converter
Group:		Applications/Communications
Requires:	trinity-kmail = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kmailcvt
Converts mail folders to KMail format.  Formats supported for import
include Outlook Express, Evolution, and plain mbox.

%files -n trinity-kmailcvt
%defattr(-,root,root,-)
%{tde_prefix}/bin/kmailcvt
%{tde_prefix}/share/applnk/Utilities/kmailcvt.desktop
%{tde_prefix}/share/apps/kmailcvt
%{tde_prefix}/share/icons/crystalsvg/*/apps/kmailcvt.png

##########

%package -n trinity-knode
Summary:	Trinity news reader
Group:		Applications/Internet

%description -n trinity-knode
KNode is an easy-to-use, convenient newsreader. It is intended to be usable
by inexperienced users, but also includes support for such features as
MIME attachments, article scoring, and creating and verifying GnuPG
signatures.

%files -n trinity-knode
%defattr(-,root,root,-)
%{tde_prefix}/bin/knode
%{tde_prefix}/%{_lib}/trinity/kcm_knode.la
%{tde_prefix}/%{_lib}/trinity/kcm_knode.so
%{tde_prefix}/%{_lib}/trinity/libknodepart.la
%{tde_prefix}/%{_lib}/trinity/libknodepart.so
%{tde_prefix}/%{_lib}/libknodecommon.so.*
%{tde_prefix}/share/applications/tde/KNode.desktop
%{tde_prefix}/share/apps/knode/
%{tde_prefix}/share/icons/hicolor/*/apps/knode.png
%{tde_prefix}/share/icons/hicolor/*/apps/knode2.png
%{tde_prefix}/share/services/knewsservice.protocol
%{tde_prefix}/share/services/knode_config_*.desktop
%{tde_prefix}/share/services/kontact/knodeplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/knode/

##########

%package -n trinity-knode-devel
Summary:	Development files for trinity-knode
Group:		Development/Libraries/Other
Requires:	trinity-knode = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-knode-devel
%{summary}

%files -n trinity-knode-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libknodecommon.la
%{tde_prefix}/%{_lib}/libknodecommon.so

##########

%package -n trinity-knotes
Summary:	Trinity sticky notes
Group:		Applications/Utilities
Requires:	trinity-tdepim-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-knotes
KNotes is a program that lets you write sticky notes. The notes are saved
automatically when you exit the program, and they display when you open the
program.  The program supports printing and mailing your notes.

%files -n trinity-knotes
%defattr(-,root,root,-)
%{tde_prefix}/bin/knotes
%{tde_prefix}/%{_lib}/trinity/knotes_local.la
%{tde_prefix}/%{_lib}/trinity/knotes_local.so
%{tde_prefix}/%{_lib}/libknotes.so.*
%{tde_prefix}/share/applications/tde/knotes.desktop
%{tde_prefix}/share/apps/knotes/
%{tde_prefix}/share/config.kcfg/knoteconfig.kcfg
%{tde_prefix}/share/config.kcfg/knotesglobalconfig.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/knotes.png
%{tde_prefix}/share/services/tderesources/knotes/imap.desktop
%{tde_prefix}/share/services/tderesources/knotes/local.desktop
%{tde_prefix}/share/services/tderesources/knotes_manager.desktop
%{tde_prefix}/share/services/kontact/knotesplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/knotes/

##########

%package -n trinity-knotes-devel
Summary:	Development files for knots
Group:		Development/Libraries/Other
Requires:	trinity-knotes = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tderesources-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-knotes-devel
%{summary}

%files -n trinity-knotes-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libknotes.so
%{tde_prefix}/%{_lib}/libknotes.la
%{tde_prefix}/include/tde/KNotesAppIface.h
%{tde_prefix}/include/tde/KNotesIface.h

##########

%package -n trinity-kode
Summary:	Helper library for programmatic generation of C++ code
Group:		Development/Libraries

%description -n trinity-kode
This package includes a program kode for generation of C++ template files
and kxml_compiler for generation of C++ classes representing XML data
described by RelaxNG schemes.

%files -n trinity-kode
%defattr(-,root,root,-)
%{tde_prefix}/bin/kode
%{tde_prefix}/bin/kxml_compiler
%{tde_prefix}/%{_lib}/libkode.so.*

##########

%package -n trinity-kode-devel
Summary:	Development files for trinity-kode
Group:		Development/Libraries/Other
Requires:	trinity-kode = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kode-devel
%{summary}

%files -n trinity-kode-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkode.la
%{tde_prefix}/%{_lib}/libkode.so

##########

%package -n trinity-konsolekalendar
Summary:	Trinity konsole personal organizer
Group:		Applications/Productivity

%description -n trinity-konsolekalendar
KonsoleKalendar is a command-line interface to TDE calendars.
Konsolekalendar complements the TDE KOrganizer by providing a console
frontend to manage your calendars.

%files -n trinity-konsolekalendar
%defattr(-,root,root,-)
%{tde_prefix}/bin/konsolekalendar
%{tde_prefix}/share/applications/tde/konsolekalendar.desktop
%{tde_prefix}/share/icons/crystalsvg/*/apps/konsolekalendar.png
%{tde_prefix}/share/doc/tde/HTML/en/konsolekalendar/

##########

%package -n trinity-kontact
Summary:	Trinity pim application
Group:		Applications/Communications
Requires:	trinity-kmail = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-korganizer = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kaddressbook = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knode = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-knotes = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-akregator = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kontact
Kontact is the integrated solution to your personal information management
needs. It combines TDE applications like KMail, KOrganizer, and
KAddressBook into a single interface to provide easy access to mail,
scheduling, address book and other PIM functionality.

%files -n trinity-kontact
%defattr(-,root,root,-)
%{tde_prefix}/bin/kontact
%{tde_prefix}/%{_lib}/trinity/kcm_kmailsummary.la
%{tde_prefix}/%{_lib}/trinity/kcm_kmailsummary.so
%{tde_prefix}/%{_lib}/trinity/kcm_kontact.la
%{tde_prefix}/%{_lib}/trinity/kcm_kontact.so
%{tde_prefix}/%{_lib}/trinity/kcm_kontactknt.la
%{tde_prefix}/%{_lib}/trinity/kcm_kontactknt.so
%{tde_prefix}/%{_lib}/trinity/kcm_kontactsummary.la
%{tde_prefix}/%{_lib}/trinity/kcm_kontactsummary.so
%{tde_prefix}/%{_lib}/trinity/kcm_korgsummary.la
%{tde_prefix}/%{_lib}/trinity/kcm_korgsummary.so
%{tde_prefix}/%{_lib}/trinity/kcm_sdsummary.la
%{tde_prefix}/%{_lib}/trinity/kcm_sdsummary.so
%{tde_prefix}/%{_lib}/trinity/libkontact_*.la
%{tde_prefix}/%{_lib}/trinity/libkontact_*.so
%{tde_prefix}/%{_lib}/libkontact.so.*
%{tde_prefix}/%{_lib}/libkpinterfaces.so.*
%{tde_prefix}/share/applications/tde/Kontact.desktop
%{tde_prefix}/share/applications/tde/kontactdcop.desktop
%{tde_prefix}/share/apps/kontact/
%{tde_prefix}/share/apps/kontactsummary/
%{tde_prefix}/share/config.kcfg/kontact.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kontact.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/kontact_*.png
%{tde_prefix}/share/services/kcmkmailsummary.desktop
%{tde_prefix}/share/services/kcmkontactknt.desktop
%{tde_prefix}/share/services/kcmkontactsummary.desktop
%{tde_prefix}/share/services/kcmkorgsummary.desktop
%{tde_prefix}/share/services/kcmsdsummary.desktop
%dir %{tde_prefix}/share/services/kontact
%{tde_prefix}/share/services/kontact/newstickerplugin.desktop
%{tde_prefix}/share/services/kontact/specialdatesplugin.desktop
%{tde_prefix}/share/services/kontact/summaryplugin.desktop
%{tde_prefix}/share/services/kontact/weatherplugin.desktop
%{tde_prefix}/share/services/kontactconfig.desktop
%{tde_prefix}/share/servicetypes/kontactplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kontact/

##########

%package -n trinity-kontact-devel
Summary:	Development files for kontact
Group:		Development/Libraries/Other
Requires:	trinity-kontact = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kontact-devel
%{summary}

%files -n trinity-kontact-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkontact.la
%{tde_prefix}/%{_lib}/libkontact.so
%{tde_prefix}/%{_lib}/libkpinterfaces.la
%{tde_prefix}/%{_lib}/libkpinterfaces.so
%{tde_prefix}/include/tde/kontact/

##########

%package -n trinity-korganizer
Summary:	Trinity personal organizer
Group:		Applications/Productivity
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
Requires:       %{_lib}sasl2-plug-anonymous
Requires:       %{_lib}sasl2-plug-crammd5
Requires:       %{_lib}sasl2-plug-digestmd5
Requires:       %{_lib}sasl2-plug-gssapi
Requires:       %{_lib}sasl2-plug-ldapdb
Requires:       %{_lib}sasl2-plug-login
Requires:       %{_lib}sasl2-plug-ntlm
Requires:       %{_lib}sasl2-plug-plain
%endif
Requires:	trinity-libkpimidentities = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkpimexchange = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	perl

%description -n trinity-korganizer
This package contains KOrganizer, a calendar and scheduling program.

KOrganizer aims to be a complete program for organizing appointments,
contacts, projects, etc. KOrganizer natively supports information interchange
with other calendar applications, through the industry standard vCalendar
personal data interchange file format. This eases the move from other
modern PIMs to KOrganizer.

KOrganizer offers full synchronization with Palm Pilots, if kpilot is
installed.

%files -n trinity-korganizer
%defattr(-,root,root,-)
%{tde_prefix}/bin/ical2vcal
%{tde_prefix}/bin/korgac
%{tde_prefix}/bin/korganizer
%{tde_prefix}/%{_lib}/trinity/kcm_korganizer.la
%{tde_prefix}/%{_lib}/trinity/kcm_korganizer.so
%{tde_prefix}/%{_lib}/trinity/libkorg_*.la
%{tde_prefix}/%{_lib}/trinity/libkorg_*.so
%{tde_prefix}/%{_lib}/trinity/libkorganizerpart.la
%{tde_prefix}/%{_lib}/trinity/libkorganizerpart.so
%{tde_prefix}/%{_lib}/libkocorehelper.so.*
%{tde_prefix}/%{_lib}/libkorg_stdprinting.so.*
%{tde_prefix}/%{_lib}/libkorganizer.so.*
%{tde_prefix}/%{_lib}/libkorganizer_calendar.so.*
%{tde_prefix}/%{_lib}/libkorganizer_eventviewer.so.*
%{tde_prefix}/share/applications/tde/korganizer.desktop
%{tde_prefix}/share/apps/tdeconf_update/korganizer.upd
%{tde_prefix}/share/apps/korgac/
%{tde_prefix}/share/apps/korganizer/
%{tde_prefix}/share/autostart/korgac.desktop
%{tde_prefix}/share/config.kcfg/korganizer.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/korganizer.png
%dir %{tde_prefix}/share/services/kontact
%{tde_prefix}/share/services/kontact/korganizerplugin.desktop
%{tde_prefix}/share/services/kontact/journalplugin.desktop
%{tde_prefix}/share/services/kontact/todoplugin.desktop
%{tde_prefix}/share/services/korganizer_*.desktop
%{tde_prefix}/share/services/korganizer
%{tde_prefix}/share/services/webcal.protocol
%{tde_prefix}/share/servicetypes/calendardecoration.desktop
%{tde_prefix}/share/servicetypes/calendarplugin.desktop
%{tde_prefix}/share/servicetypes/dcopcalendar.desktop
%{tde_prefix}/share/servicetypes/korganizerpart.desktop
%{tde_prefix}/share/servicetypes/korgprintplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/korganizer/
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/webcal/

##########

%package -n trinity-korganizer-devel
Summary:	Development files for korganizer
Group:		Development/Libraries/Other
Requires:	trinity-korganizer = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-korganizer-devel
%{summary}

%files -n trinity-korganizer-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/korganizer/
%{tde_prefix}/include/tde/calendar/
%{tde_prefix}/%{_lib}/libkocorehelper.la
%{tde_prefix}/%{_lib}/libkocorehelper.so
%{tde_prefix}/%{_lib}/libkorg_stdprinting.la
%{tde_prefix}/%{_lib}/libkorg_stdprinting.so
%{tde_prefix}/%{_lib}/libkorganizer.la
%{tde_prefix}/%{_lib}/libkorganizer.so
%{tde_prefix}/%{_lib}/libkorganizer_calendar.la
%{tde_prefix}/%{_lib}/libkorganizer_calendar.so
%{tde_prefix}/%{_lib}/libkorganizer_eventviewer.la
%{tde_prefix}/%{_lib}/libkorganizer_eventviewer.so

##########

%package -n trinity-korn
Summary:	Trinity mail checker
Group:		Applications/Communications

Requires:       %{_lib}sasl2-plug-anonymous
Requires:       %{_lib}sasl2-plug-crammd5
Requires:       %{_lib}sasl2-plug-digestmd5
Requires:       %{_lib}sasl2-plug-gssapi
Requires:       %{_lib}sasl2-plug-ldapdb
Requires:       %{_lib}sasl2-plug-login
Requires:       %{_lib}sasl2-plug-ntlm
Requires:       %{_lib}sasl2-plug-plain
Requires:	%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-korn
Korn is a TDE mail checker that can display a small summary in the Kicker
tray.  It supports checking mbox, pop3, imap4, and nntp sources.

Once mail is received you can have Korn run a third party program or change
the color/icon of the Kicker display.  In addition to this you can have
Korn run a program once you click on the docked icon in Kicker.

%files -n trinity-korn
%defattr(-,root,root,-)
%{tde_prefix}/bin/korn
%{tde_prefix}/%{_lib}/tdeconf_update_bin/korn-3-4-config_change
%{tde_prefix}/share/applications/tde/KOrn.desktop
%{tde_prefix}/share/apps/tdeconf_update/korn-3-4-config_change.upd
%{tde_prefix}/share/apps/tdeconf_update/korn-3-5-metadata-update.pl
%{tde_prefix}/share/apps/tdeconf_update/korn-3-5-ssl-update.pl
%{tde_prefix}/share/apps/tdeconf_update/korn-3-5-update.upd
%{tde_prefix}/share/icons/hicolor/*/apps/korn.png
%{tde_prefix}/share/doc/tde/HTML/en/korn/

##########

%package -n trinity-ktnef
Summary:	Trinity TNEF viewer
Group:		Applications/Communications

%description -n trinity-ktnef
The TNEF File Viewer allows you to handle mail attachments using the TNEF
format. These attachments are usually found in mails coming from Microsoft
mail servers and embed the mail properties as well as the actual attachments.

%files -n trinity-ktnef
%defattr(-,root,root,-)
%{tde_prefix}/bin/ktnef
%{tde_prefix}/share/applications/tde/ktnef.desktop
%{tde_prefix}/share/apps/ktnef
%{tde_prefix}/share/icons/hicolor/*/apps/ktnef.png
%{tde_prefix}/share/icons/locolor/*/apps/ktnef.png
%{tde_prefix}/share/mimelnk/application/ms-tnef.desktop
%{tde_prefix}/share/doc/tde/HTML/en/ktnef/

##########

%package -n trinity-libindex
Summary:	Trinity indexing library
Group:		Environment/Libraries

%description -n trinity-libindex
This library provides text indexing and is currently used by KMail
to implement fast searches in mail bodies.

This is the runtime package for programs that use the libindex library.

%files -n trinity-libindex
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libindex.so.*

##########

%package -n trinity-libindex-devel
Summary:	Trinity indexing library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libindex = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libindex-devel
This library provides text indexing and is currently used by KMail
to implement searching through mail text.

This is the development package which contains the headers for the libindex-trinity
library.

%files -n trinity-libindex-devel
%defattr(-,root,root,-)
%{tde_prefix}/bin/indexlib-config
%{tde_prefix}/include/tde/index
%{tde_prefix}/%{_lib}/libindex.la
%{tde_prefix}/%{_lib}/libindex.so

##########

%package -n trinity-libkcal
Summary:	Trinity calendaring library
Group:		Environment/Libraries
#Requires:	%{name}-tderesources = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkmime = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkcal
This library provides a C++ API for handling the vCalendar and iCalendar
formats.

This is the runtime package for programs that use the libkcal-trinity library.

%files -n trinity-libkcal
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kcal_tdeabc.la
%{tde_prefix}/%{_lib}/trinity/kcal_tdeabc.so
%{tde_prefix}/%{_lib}/trinity/kcal_localdir.la
%{tde_prefix}/%{_lib}/trinity/kcal_localdir.so
%{tde_prefix}/%{_lib}/trinity/kcal_local.la
%{tde_prefix}/%{_lib}/trinity/kcal_local.so
%{tde_prefix}/%{_lib}/trinity/kcal_remote.la
%{tde_prefix}/%{_lib}/trinity/kcal_remote.so
%{tde_prefix}/%{_lib}/libkcal.so.*
%{tde_prefix}/%{_lib}/libkcal_resourceremote.so.*
%{tde_prefix}/%{_lib}/libkholidays.so.*
%{tde_prefix}/share/apps/libkholidays/
%dir %{tde_prefix}/share/services/tderesources/kcal
%{tde_prefix}/share/services/tderesources/kcal/imap.desktop
%{tde_prefix}/share/services/tderesources/kcal/tdeabc.desktop
%{tde_prefix}/share/services/tderesources/kcal/local.desktop
%{tde_prefix}/share/services/tderesources/kcal/localdir.desktop
%{tde_prefix}/share/services/tderesources/kcal/remote.desktop
%{tde_prefix}/share/services/tderesources/kcal_manager.desktop

##########

%package -n trinity-libkcal-devel
Summary:	Trinity calendaring library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libkcal = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libktnef-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkcal-devel
This library provides a C++ API for handling the vCalendar and iCalendar
formats.

This is the development package which contains the headers for the libkcal-trinity
library.

%files -n trinity-libkcal-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/libemailfunctions/
%{tde_prefix}/include/tde/libkcal
%{tde_prefix}/%{_lib}/libkcal.la
%{tde_prefix}/%{_lib}/libkcal.so
%{tde_prefix}/%{_lib}/libkcal_resourceremote.la
%{tde_prefix}/%{_lib}/libkcal_resourceremote.so
%{tde_prefix}/%{_lib}/libkholidays.la
%{tde_prefix}/%{_lib}/libkholidays.so

##########

%package -n trinity-libtdepim
Summary:	Trinity PIM library
Group:		Environment/Libraries
Requires:	trinity-libkcal = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libktnef = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	libtdepim < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	libtdepim = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtdepim
This is the runtime package for programs that use the trinity-libtdepim library.

%files -n trinity-libtdepim
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/plugins/designer/tdepimwidgets.la
%{tde_prefix}/%{_lib}/trinity/plugins/designer/tdepimwidgets.so
%{tde_prefix}/%{_lib}/trinity/plugins/designer/tdepartsdesignerplugin.la
%{tde_prefix}/%{_lib}/trinity/plugins/designer/tdepartsdesignerplugin.so
%{tde_prefix}/%{_lib}/libtdepim.so.*
%{tde_prefix}/share/apps/tdepimwidgets
%{tde_prefix}/share/apps/libtdepim
%{tde_prefix}/share/apps/tdepim
%{tde_prefix}/share/config.kcfg/pimemoticons.kcfg
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/button_fewer.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/button_more.png

##########

%package -n trinity-libtdepim-devel
Summary:	Trinity PIM library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libtdepim = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdelibs-devel >= %{version}

Obsoletes:	libtdepim-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtdepim-devel
This is the development package which contains the headers for the libtdepim-trinity
library.

%files -n trinity-libtdepim-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libtdepim.la
%{tde_prefix}/%{_lib}/libtdepim.so

##########

%package -n trinity-libkgantt
Summary:	Trinity gantt charting library
Group:		Environment/Libraries

%description -n trinity-libkgantt
This is the runtime package for programs that use the libkgantt-trinity library.

%files -n trinity-libkgantt
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkgantt.so.*
%{tde_prefix}/share/apps/kgantt

##########

%package -n trinity-libkgantt-devel
Summary:	Trinity gantt charting library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libkgantt = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkgantt-devel
This is the development package which contains the headers for the libkgantt-trinity
library.

%files -n trinity-libkgantt-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/kgantt
%{tde_prefix}/%{_lib}/libkgantt.la
%{tde_prefix}/%{_lib}/libkgantt.so

##########

%package -n trinity-libkleopatra
Summary:	TDE GnuPG interface libraries
Group:		Environment/Libraries
Requires:	gnupg

%description -n trinity-libkleopatra
This library is used by several TDE applications to interface to the
GnuPG program.

This is the runtime package for programs that use the libkleopatra-trinity library.

%files -n trinity-libkleopatra
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/libkleopatrarc
%{tde_prefix}/%{_lib}/libgpgme++.so.*
%{tde_prefix}/%{_lib}/libkleopatra.so.*
%{tde_prefix}/%{_lib}/libkpgp.so.*
%{tde_prefix}/%{_lib}/libqgpgme.so.*
%{tde_prefix}/share/apps/tdeconf_update/kpgp-3.1-upgrade-address-data.pl
%{tde_prefix}/share/apps/tdeconf_update/kpgp.upd
%{tde_prefix}/share/apps/libkleopatra/
%{tde_prefix}/share/icons/crystalsvg/*/apps/dirmngr.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gpg.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gpg_agent.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/gpgsm.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/pinentry.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/scdaemon.png

##########

%package -n trinity-libkleopatra-devel
Summary:	Trinity GnuPG interface libraries [development]
Group:		Development/Libraries/Other
Requires:	trinity-libkleopatra = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkleopatra-devel
This library is used by several TDE applications to interface to the
GnuPG program.

This is the development package which contains the headers for the
libkleopatra-trinity library.

%files -n trinity-libkleopatra-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/gpgme++/
%{tde_prefix}/include/tde/kleo/
%{tde_prefix}/include/tde/qgpgme/
%{tde_prefix}/%{_lib}/libgpgme++.la
%{tde_prefix}/%{_lib}/libgpgme++.so
%{tde_prefix}/%{_lib}/libkleopatra.la
%{tde_prefix}/%{_lib}/libkleopatra.so
%{tde_prefix}/%{_lib}/libkpgp.la
%{tde_prefix}/%{_lib}/libkpgp.so
%{tde_prefix}/%{_lib}/libqgpgme.la
%{tde_prefix}/%{_lib}/libqgpgme.so

##########

%package -n trinity-libkmime
Summary:	Trinity MIME interface library
Group:		Environment/Libraries
#Conflicts:	trinity-libmimelib

%description -n trinity-libkmime
This library provides a C++ interface to MIME messages, parsing them into
an object tree.

%files -n trinity-libkmime
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkmime.so.*

##########

%package -n trinity-libkmime-devel
Summary:	Development files for libkmime
Group:		Development/Libraries/Other
Requires:	trinity-libkmime = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkmime-devel
%{summary}

%files -n trinity-libkmime-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkmime.la
%{tde_prefix}/%{_lib}/libkmime.so

##########

%package -n trinity-libkpimexchange
Summary:	Trinity PIM Exchange library
Group:		Development/Libraries/Other

%description -n trinity-libkpimexchange
This is the runtime package for programs that use the libkpimexchange-trinity
library. 

%files -n trinity-libkpimexchange
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/resourcecalendarexchange.la
%{tde_prefix}/%{_lib}/trinity/resourcecalendarexchange.so
%{tde_prefix}/%{_lib}/libkpimexchange.so.*

##########

%package -n trinity-libkpimexchange-devel
Summary:	Trinity PIM Exchange library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libkpimexchange = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkcal-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkpimexchange-devel
This is the development package which contains the headers for the
libkpimexchange-trinity library.

%files -n trinity-libkpimexchange-devel
%defattr(-,root,root,-)
%dir %{tde_prefix}/include/tde/tdepim
%{tde_prefix}/include/tde/tdepim/exchangeaccount.h
%{tde_prefix}/include/tde/tdepim/exchangeclient.h
%{tde_prefix}/%{_lib}/libkpimexchange.la
%{tde_prefix}/%{_lib}/libkpimexchange.so

##########

%package -n trinity-libkpimidentities
Summary:	Trinity PIM user identity information library
Group:		Environment/Libraries

%description -n trinity-libkpimidentities
This library provides information to TDE programs about user identity,
such as email address, organization, etc.

This is the runtime package for programs that use the libkpimidentities-trinity
library.

%files -n trinity-libkpimidentities
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkpimidentities.so.*

##########

%package -n trinity-libkpimidentities-devel
Summary:	Development files for libkpimidentities
Group:		Development/Libraries/Other
Requires:	trinity-libkpimidentities = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libkpimidentities-devel
%{summary}

%files -n trinity-libkpimidentities-devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkpimidentities.la
%{tde_prefix}/%{_lib}/libkpimidentities.so

##########

%package -n trinity-libksieve
Summary:	Trinity mail/news message filtering library
Group:		Environment/Libraries

%description -n trinity-libksieve
This is the runtime package for programs that use the libksieve-trinity library.

%files -n trinity-libksieve
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libksieve.so.*
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/sieve/

##########

%package -n trinity-libksieve-devel
Summary:	Trinity mail/news message filtering library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libksieve = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libksieve-devel
This is the development package which contains the headers for the libksieve-trinity
library.

%files -n trinity-libksieve-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/ksieve
%{tde_prefix}/%{_lib}/libksieve.la
%{tde_prefix}/%{_lib}/libksieve.so

##########

%package -n trinity-libktnef
Summary:	Library for handling KTNEF email attachments
Group:		Environment/Libraries

%description -n trinity-libktnef
This library handles mail attachments using the TNEF format. These
attachments are usually found in mails coming from Microsoft mail
servers and embed the mail properties as well as the actual
attachments.
.
This is the runtime library for packages using the ktnef-trinity library.

%files -n trinity-libktnef
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libktnef.so.*

##########

%package -n trinity-libktnef-devel
Summary:	KTNEF handler library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libktnef = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdepim-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libktnef-devel
This library handles mail attachments using the TNEF format. These
attachments are usually found in mails coming from Microsoft mail
servers and embed the mail properties as well as the actual
attachments.

This is the development package which contains the headers for the
ktnef-trinity library.

%files -n trinity-libktnef-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/ktnef
%{tde_prefix}/%{_lib}/libktnef.la
%{tde_prefix}/%{_lib}/libktnef.so

##########

%package -n trinity-libmimelib
Summary:	Trinity mime library
Group:		Environment/Libraries

%description -n trinity-libmimelib
This library is used by several Trinity applications to handle mime types.

This is the runtime package for programs that use the libmimelib-trinity library.

%files -n trinity-libmimelib
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libmimelib.so.*

##########

%package -n trinity-libmimelib-devel
Summary:	Trinity mime library [development]
Group:		Development/Libraries/Other
Requires:	trinity-libmimelib = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libmimelib-devel
This library is used by several TDE applications to handle mime types.

This is the development package which contains the headers for the
libmimelib library.

%files -n trinity-libmimelib-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/mimelib/
%{tde_prefix}/%{_lib}/libmimelib.la
%{tde_prefix}/%{_lib}/libmimelib.so

##########

%package -n trinity-kmobile
Summary:	Synchronize and manage mobile phone with your PC.
Group:		Applications/Communications

%description -n trinity-kmobile
KMobileTools is a nice TDE-based application that allows to synchronize 
and manage mobile phones with your PC. It handles full SMS control, 
dialing calls, phonebook, and phone status monitoring.

%files -n trinity-kmobile
%defattr(-,root,root,-)
%{tde_prefix}/bin/kmobile
%{tde_prefix}/share/icons/default.tde/32x32/devices/mobile_camera.png
%{tde_prefix}/share/icons/default.tde/32x32/devices/mobile_musicplayer.png
%{tde_prefix}/share/icons/default.tde/32x32/devices/mobile_organizer.png
%{tde_prefix}/share/icons/default.tde/32x32/devices/mobile_phone.png
%{tde_prefix}/share/icons/default.tde/32x32/devices/mobile_unknown.png
%{tde_prefix}/share/icons/hicolor/*/apps/kmobile.png
%{tde_prefix}/share/services/libkmobile_digicam.desktop
%{tde_prefix}/share/services/libkmobile_gammu.desktop
%{tde_prefix}/share/services/libkmobile_skeleton.desktop
%{tde_prefix}/share/servicetypes/libkmobile.desktop
%{tde_prefix}/share/apps/kmobile/
%{tde_prefix}/share/applications/tde/kmobile.desktop
%{tde_prefix}/%{_lib}/trinity/libkmobile_skeleton.la
%{tde_prefix}/%{_lib}/trinity/libkmobile_skeleton.so
%{tde_prefix}/%{_lib}/libkmobileclient.la
%{tde_prefix}/%{_lib}/libkmobileclient.so
%{tde_prefix}/%{_lib}/libkmobiledevice.la
%{tde_prefix}/%{_lib}/libkmobiledevice.so
%{tde_prefix}/share/doc/tde/HTML/en/kmobile/

%prep -a
# Fix 'ical2vcal' contains '/bin/perl' instead of '/usr/bin/perl'
if [ -x /usr/bin/perl ]; then
  %__sed -i "korganizer/ical2vcal.in" -e "s|@PERL@|/usr/bin/perl|"
fi


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# Adds missing icons in 'hicolor' theme
pushd "%{?buildroot}%{tde_prefix}/share/icons"
for i in {16,32,48};           do %__cp crystalsvg/"$i"x"$i"/apps/kandy.png                           hicolor/"$i"x"$i"/apps/kandy.png      ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/places/network.png  hicolor/"$i"x"$i"/apps/kleopatra.png  ;done
popd

# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"


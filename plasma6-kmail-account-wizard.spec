#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Account wizard for KMail
Name:		plasma6-kmail-account-wizard
Version:	24.12.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kmail-account-wizard/-/archive/%{gitbranch}/kmail-account-wizard-%{gitbranchd}.tar.bz2#/kmail-account-wizard-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kmail-account-wizard-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6LdapCore)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6PimCommon)
BuildRequires:	cmake(KPim6Libkleo)
BuildRequires:	cmake(KPim6IMAP)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(Qt6UiTools)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Qt6Keychain)

%description
Launch the account wizard to configure PIM accounts.

%files -f all.lang
%{_datadir}/applications/org.kde.accountwizard.desktop
%{_datadir}/metainfo/org.kde.accountwizard.appdata.xml
%{_bindir}/accountwizard

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kmail-account-wizard-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang all --all-name

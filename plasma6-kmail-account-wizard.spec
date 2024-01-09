%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Account wizard for KMail
Name:		plasma6-kmail-account-wizard
Version:	24.01.85
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kmail-account-wizard-%{version}.tar.xz
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
Provides:	accountwizard = %{EVRD}
Conflicts:	accountwizard < 3:17.04.0
Obsoletes:	accountwizard < 3:17.04.0
Obsoletes:	kdepim-accountwizard < 3:17.04.0
Conflicts:	kdepim-accountwizard < 3:17.04.0

%description
Launch the account wizard to configure PIM accounts.

%files -f all.lang
%{_datadir}/applications/org.kde.accountwizard.desktop
%{_bindir}/accountwizard
%{_datadir}/qlogging-categories6/accountwizard.categories
%{_datadir}/qlogging-categories6/accountwizard.renamecategories
%{_libdir}/libaccountwizard.so*
%{_qtdir}/qml/org/kde/pim/accountwizard

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kmail-account-wizard-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang all --all-name

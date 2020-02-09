%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Account wizard for KMail
Name:		kmail-account-wizard
Version:	19.12.2
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5Ldap)
BuildRequires:	cmake(KF5MailTransportAkonadi)
BuildRequires:	cmake(KF5PimCommon)
BuildRequires:	cmake(KF5LibkdepimAkonadi)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(MailTransportDBusService)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(Qt5UiTools)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	cmake(QGpgme)
Provides:	accountwizard = %{EVRD}
Conflicts:	accountwizard < 3:17.04.0
Obsoletes:	accountwizard < 3:17.04.0
Obsoletes:	kdepim-accountwizard < 3:17.04.0
Conflicts:	kdepim-accountwizard < 3:17.04.0

%description
Launch the account wizard to configure PIM accounts.

%files -f all.lang
%{_kde5_applicationsdir}/org.kde.accountwizard.desktop
%{_bindir}/accountwizard
%{_bindir}/ispdb
%dir %{_datadir}/akonadi/accountwizard/tine20/
%{_datadir}/akonadi/accountwizard/tine20/*
%{_datadir}/knsrcfiles/accountwizard.knsrc
%{_datadir}/qlogging-categories5/accountwizard.categories
%{_datadir}/qlogging-categories5/accountwizard.renamecategories
%{_datadir}/mime/packages/accountwizard-mime.xml
%{_qt5_plugindir}/accountwizard_plugin.so

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang accountwizard
%find_lang accountwizard_tine20

cat *.lang >all.lang

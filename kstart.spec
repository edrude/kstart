# RPM spec file for kstart.
#
# Written by Russ Allbery <eagle@eyrie.org>
# Copyright 2015, 2021 Russ Allbery <eagle@eyrie.org>
# Copyright 2005-2012
#     The Board of Trustees of the Leland Stanford Junior University
#
# SPDX-License-Identifier: MIT

Name: kstart
Summary: Kerberos kinit variants supporting ticket refreshing
Version: 4.3.1
Release: 1%{?dist}
License: MIT
Group: System Environment/Base
URL: https://www.eyrie.org/~eagle/software/kstart/
Source: https://archives.eyrie.org/software/kerberos/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gcc, make, automake, autoconf, libtool, krb5-devel
Requires: krb5
Vendor: Russ Allbery

%description
k5start and krenew are modified versions of kinit which add support for
running as a daemon to maintain a ticket cache, running a command with
credentials from a keytab and maintaining a ticket cache until that command
completes, obtaining AFS tokens (via an external aklog) after obtaining
tickets, and creating an AFS PAG for a command.  They are primarily useful in
conjunction with long-running jobs; for moving ticket handling code out of
servers, cron jobs, or daemons; and to obtain tickets and AFS tokens with a
single command.

%prep
%setup -q -n kstart-%{version}
./bootstrap

%build
PATH="/sbin:/bin:/usr/sbin:/usr/bin:$PATH" \
%configure --enable-setpag
%make_build

%install
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/*
%doc LICENSE NEWS README TODO
%{_mandir}/*/*

%changelog
* Mon Aug 30 2021 Ed Rude <
- Notify systemd of main pid if running as a systemd service of type notify
* Mon Aug 30 2021 Russ Allbery <eagle@eyrie.org> 4.3-1
- New version for 4.3 release.

* Tue Mar 20 2021 Russ Allbery <eagle@eyrie.org> 4.2-2
- Update upstream URL.

* Fri Dec 25 2015 Russ Allbery <eagle@eyrie.org> 4.2-1
- New version for 4.2 release.

* Mon Jan 9 2012 Robbert Eggermont <R.Eggermont@tudelft.nl> 4.1-1
- New version for 4.1 release.
- Require krb5 instead of krb5-libs for SLED compatibility.
- Fix %defattr lines to not cause directory permission issues.
- Tested on RHEL5/6 and SLED10/11.

* Tue Dec 27 2011 Russ Allbery <eagle@eyrie.org> 3.16-2
- Remove references to k4start from description.

* Mon Mar 29 2010 Andy Cobaugh <phalenor@bx.psu.edu> 3.16-1
- New version for 3.16 release.
- Require krb5-libs instead of krb5-workstation.

* Sat Aug 15 2008 Russ Allbery <eagle@eyrie.org> 3.15-1
- New version for 3.15 release.

* Tue Jul 22 2008 Russ Allbery <eagle@eyrie.org> 3.14-1
- New version for 3.14 release.
- Fix default file attributes for non-executables.
- Remove the BSD license; everything is under an MIT license.

* Wed May 28 2008 Russ Allbery <eagle@eyrie.org> 3.13-1
- New version for 3.13 release.

* Wed Apr 23 2008 Russ Allbery <eagle@eyrie.org> 3.12-1
- New version for 3.12 release.

* Tue Apr 10 2008 Russ Allbery <eagle@eyrie.org> 3.11-1
- New version for 3.11 release.
- Add LICENSE and TODO to documentation.
- Build with --enable-setpag now that it no longer requires extra libraries.

* Sat Mar 3 2007 Russ Allbery <eagle@eyrie.org> 3.9-1
- New version for 3.9 release.

* Sat Mar 3 2007 Russ Allbery <eagle@eyrie.org> 3.8-1
- New version for 3.8 release.

* Sun Jan 28 2007 Russ Allbery <eagle@eyrie.org> 3.7-1
- New version for 3.7 release.

* Wed Oct 04 2006 Russ Allbery <eagle@eyrie.org> 3.6-1
- New version for 3.6 release.

* Tue Jun 13 2006 Russ Allbery <eagle@eyrie.org> 3.5-1
- New version for 3.5 release.

* Mon Apr 10 2006 Russ Allbery <eagle@eyrie.org> 3.3-1
- New version for 3.3 release.

* Sun Mar 05 2006 Russ Allbery <eagle@eyrie.org> 3.2-1
- New version for 3.2 release.

* Sun Jan 22 2006 Russ Allbery <eagle@eyrie.org> 3.0-1
- New version for 3.0 release.
- Update description to include krenew.
- No longer build with --enable-reduced-depends.

* Sat Dec 31 2005 Russ Allbery <eagle@eyrie.org> 2.9-1
- New version for 2.9 release.
- No longer generated via Autoconf, since the changelog has to be added.

* Sat Dec 10 2005 Russ Allbery <eagle@eyrie.org> 2.8-2
- Incorporate into the package, remove Autoreq.

* Thu Oct 27 2005 Buck <buckh@> 2.8-1
- stole spec file (not recently) from
  http://svn.rpmforge.net/svn/trunk/rpms/nagios-plugins/nagios-plugins.spec

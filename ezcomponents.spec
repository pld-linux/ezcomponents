%include	/usr/lib/rpm/macros.php
Summary:	eZ Components
Name:		ezcomponents
Version:	2008.2
Release:	0.1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://ezcomponents.org/files/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	57b211e2e85670633ebb165e14742f95
URL:		http://www.ezcomponents.org/
BuildRequires:	php-common >= 4:5.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{php_data_dir}/%{name}

# fool adapter: allow version macro in url
%define		docver	%{version}

%description
eZ Components is an enterprise ready general purpose PHP components
library used independently or together for PHP application
development. With eZ Components, developers do not have to reinvent
the wheel, instead they can concentrate on solving customer-specific
needs.

%package Archive
Summary:	Archive
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Archive.html
Requires:	%{name} = %{version}-%{release}

%description Archive
The component allows you to create, modify, and extract archive files
of various formats. The currently supported archives formats are Tar
(with the flavours: ustar, v7, pax, and gnu) and Zip.

%package Authentication
Summary:	Authentication
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Authentication.html
Requires:	%{name} = %{version}-%{release}

%description Authentication
The purpose of the Authentication component is to provide support for
different means of identification and authentication of users using
different providers and protocols.

%package AuthenticationDatabaseTiein
Summary:	AuthenticationDatabaseTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_AuthenticationDatabaseTiein.html
Requires:	%{name} = %{version}-%{release}

%description AuthenticationDatabaseTiein
The purpose of the Authentication component is to provide support for
different means of identification and authentication of users using
different providers and protocols.

%package Base
Summary:	Base
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Base.html
Requires:	%{name} = %{version}-%{release}

%description Base
The Base package provides the basic infrastructure that all packages
rely on. Therefore every component relies on this package.

%package Cache
Summary:	Cache
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Cache.html
Requires:	%{name} = %{version}-%{release}

%description Cache
A solution for caching, supporting multiple backends allowing you to
specify the best performing solution for your caching-problem.

%package Configuration
Summary:	Configuration
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Configuration.html
Requires:	%{name} = %{version}-%{release}

%description Configuration
A component that allows you to use configuration files in different
formats. The formats include the standard .ini file, and an array
based format.

%package ConsoleTools
Summary:	ConsoleTools
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_ConsoleTools.html
Requires:	%{name} = %{version}-%{release}

%description ConsoleTools
A set of classes to do different actions with the console (also called
shell). It can render a progress bar, tables and a status bar and
contains a class for parsing command line options.

%package Database
Summary:	Database
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Database.html
Requires:	%{name} = %{version}-%{release}

%description Database
A lightweight database layer on top of PHP's PDO that allows you to
utilize a database without having to take care of differences in SQL
dialects.

%package DatabaseSchema
Summary:	DatabaseSchema
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_DatabaseSchema.html
Requires:	%{name} = %{version}-%{release}

%description DatabaseSchema
A set of classes that allow you to extract information from a database
schema, compare database schemas and apply a set of changes to a
database schema.

%package Debug
Summary:	Debug
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Debug.html
Requires:	%{name} = %{version}-%{release}

%description Debug
This component provides a set of classes that help you to debug an
application. It provides timers and report generators for different
formats that give a summary of warnings and errors that occurred
within your application.

%package Document
Summary:	Document
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Document.html
Requires:	%{name} = %{version}-%{release}

%description Document
The Document components provides a general conversion framework for
different semantic document markup languages like XHTML, Docbook, RST
and similar.

%package EventLog
Summary:	EventLog
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_EventLog.html
Requires:	%{name} = %{version}-%{release}

%description EventLog
Allows you to log events or audit trails into files or other storage
spaces in different formats.

%package EventLogDatabaseTiein
Summary:	EventLogDatabaseTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_EventLogDatabaseTiein.html
Requires:	%{name} = %{version}-%{release}

%description EventLogDatabaseTiein
Contains the database writer backend for the EventLog component.

%package Execution
Summary:	Execution
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Execution.html
Requires:	%{name} = %{version}-%{release}

%description Execution
Provides functionality to give feedback to your application's users
when a fatal error happened or an uncaught exception was thrown.

%package Feed
Summary:	Feed
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Feed.html
Requires:	%{name} = %{version}-%{release}

%description Feed
This component handles parsing and creating RSS1, RSS2 and ATOM feeds,
with support for different feed modules (dc, content, creativeCommons,
geo, iTunes).

%package File
Summary:	File
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_File.html
Requires:	%{name} = %{version}-%{release}

%description File
Provides support for file operations which are not covered by PHP or
are just missing.

%package Graph
Summary:	Graph
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Graph.html
Requires:	%{name} = %{version}-%{release}

%description Graph
A component for creating pie charts, line graphs and other kinds of
diagrams.

%package GraphDatabaseTiein
Summary:	GraphDatabaseTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_GraphDatabaseTiein.html
Requires:	%{name} = %{version}-%{release}

%description GraphDatabaseTiein
The GraphDatabaseTiein provides functionality to directly use PDO
statements as basis for ezcGraph Datasets.

%package ImageAnalysis
Summary:	ImageAnalysis
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_ImageAnalysis.html
Requires:	%{name} = %{version}-%{release}

%description ImageAnalysis
This class allows you to analyse image files in different ways. At
least the MIME type of the file is returned. In some cases (JPEG, TIFF
and GIF) additional information is gathered as well.

%package ImageConversion
Summary:	ImageConversion
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_ImageConversion.html
Requires:	%{name} = %{version}-%{release}

%description ImageConversion
A set of classes to apply different filters on images, such as colour
changes, resizing and special effects.

%package Mail
Summary:	Mail
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Mail.html
Requires:	%{name} = %{version}-%{release}

%description Mail
The component allows you construct and/or parse Mail messages
conforming to the mail standard. It has support for attachments,
multipart messages and HTML mail. It also interfaces with SMTP to send
mail or IMAP, POP3 or mbox to retrieve e-mail.

%package MvcMailTiein
Summary:	MvcMailTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_MvcMailTiein.html
Requires:	%{name} = %{version}-%{release}

%description MvcMailTiein
This component provides a request parser that extracts request data
from e-mail messages.

%package MvcTemplateTiein
Summary:	MvcTemplateTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_MvcTemplateTiein.html
Requires:	%{name} = %{version}-%{release}

%description MvcTemplateTiein
This component provides a view handler that renders result data with
the Template component.

%package MvcTools
Summary:	MvcTools
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_MvcTools.html
Requires:	%{name} = %{version}-%{release}

%description MvcTools
The MvcTools component provides functionality for request parsing,
routing, dispatching, views and response writing. With the tools in
this component you can very easily build an MVC framework.

%package PersistentObject
Summary:	PersistentObject
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_PersistentObject.html
Requires:	%{name} = %{version}-%{release}

%description PersistentObject
This component allows you to store an arbitrary data structures to a
fixed database table. The component provides all the functionality
needed to fetch, list, delete etc these datastructures.

%package PersistentObjectDatabaseSchemaTiein
Summary:	PersistentObjectDatabaseSchemaTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_PersistentObjectDatabaseSchemaTiein.html
Requires:	%{name} = %{version}-%{release}

%description PersistentObjectDatabaseSchemaTiein
This component allows the automatic generation of PersistentObject
definition files from DatabaseSchema definitions.

%package PhpGenerator
Summary:	PhpGenerator
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_PhpGenerator.html
Requires:	%{name} = %{version}-%{release}

%description PhpGenerator
Provides a simple interface for creating PHP files and executing PHP
code.

%package Search
Summary:	Search
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Search.html
Requires:	%{name} = %{version}-%{release}

%description Search
The Search component provides an interface to index and query
documents with different search engine backends.

%package SignalSlot
Summary:	SignalSlot
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_SignalSlot.html
Requires:	%{name} = %{version}-%{release}

%description SignalSlot
The SignalSlot component implements a mechanism for inter and intra
object communication through the use of signals and slots.

%package SystemInformation
Summary:	SystemInformation
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_SystemInformation.html
Requires:	%{name} = %{version}-%{release}

%description SystemInformation
Provides access to common system variables, such as CPU type and
speed, and the available amount of memory.

%package Template
Summary:	Template
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Template.html
Requires:	%{name} = %{version}-%{release}

%description Template
A fully functional Templating system, supporting template compilation
in different levels, user defined functions and operators, an
optimizer, output escaping for different output handlers to prevent
XSS and other security problems and a plug in system for extra
functionality (such as a Translation system).

%package TemplateTranslationTiein
Summary:	TemplateTranslationTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_TemplateTranslationTiein.html
Requires:	%{name} = %{version}-%{release}

%description TemplateTranslationTiein
Provides functionality to use translations inside templates.

%package Translation
Summary:	Translation
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Translation.html
Requires:	%{name} = %{version}-%{release}

%description Translation
A component that reads XML translation definitions (the Qt Linguist
format), supports caching of translation contexts and presents you
with a class to apply translations to strings. A filter system allows
you to transform translation definitions for special use.

%package TranslationCacheTiein
Summary:	TranslationCacheTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_TranslationCacheTiein.html
Requires:	%{name} = %{version}-%{release}

%description TranslationCacheTiein
This component adds the TranslationCache backend to the Translation
component and allows cached translations.

%package Tree
Summary:	Tree
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Tree.html
Requires:	%{name} = %{version}-%{release}

%description Tree
The Tree component handles the creating, manipulating and querying of
tree structures. The component supports different storage algorithms
for optimal performance.

%package TreeDatabaseTiein
Summary:	TreeDatabaseTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_TreeDatabaseTiein.html
Requires:	%{name} = %{version}-%{release}

%description TreeDatabaseTiein
The Tree component handles the creating, manipulating and querying of
tree structures. This component implements the database related
backends and data stores.

%package TreePersistentObjectTiein
Summary:	TreePersistentObjectTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_TreePersistentObjectTiein.html
Requires:	%{name} = %{version}-%{release}

%description TreePersistentObjectTiein
The Tree component handles the creating, manipulating and querying of
tree structures. This component uses persistent objects as data
storage for the data elements of the tree nodes.

%package Url
Summary:	Url
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Url.html
Requires:	%{name} = %{version}-%{release}

%description Url
The Url package provides basic operations to handle urls (parse,
build, get/set path, get/set query).

%package UserInput
Summary:	UserInput
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_UserInput.html
Requires:	%{name} = %{version}-%{release}

%description UserInput
A component that assists you to safely user input variables coming
into your application. It builds on top of PHP's filter extension and
extends it by providing a more inituitive API.

%package Webdav
Summary:	Webdav
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Webdav.html
Requires:	%{name} = %{version}-%{release}

%description Webdav
This component allows you to set up and run your own WebDAV (RFC 2518)
server, to enable online content editing for the users of your system
through the WebDAV HTTP extension.

%package Workflow
Summary:	Workflow
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_Workflow.html
Requires:	%{name} = %{version}-%{release}

%description Workflow
The purpose of the Workflow component is to provide the core
functionality of an activity-based workflow system including the
definition and execution of workflow specifications.

%package WorkflowDatabaseTiein
Summary:	WorkflowDatabaseTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_WorkflowDatabaseTiein.html
Requires:	%{name} = %{version}-%{release}

%description WorkflowDatabaseTiein
Contains the database backend for the Workflow component.

%package WorkflowEventLogTiein
Summary:	WorkflowEventLogTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_WorkflowEventLogTiein.html
Requires:	%{name} = %{version}-%{release}

%description WorkflowEventLogTiein
Contains the EventLog listener for the Workflow component.

%package WorkflowSignalSlotTiein
Summary:	WorkflowSignalSlotTiein
Group:		Development/Languages/PHP
URL:		http://www.ezcomponents.org/docs/api/%{docver}/classtrees_WorkflowSignalSlotTiein.html
Requires:	%{name} = %{version}-%{release}

%description WorkflowSignalSlotTiein
Contains the SignalSlot links for the Workflow component.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -a autoload $RPM_BUILD_ROOT%{_appdir}

for a in [A-Z]*/; do
	a=${a%/}
	cp -a $a/src $RPM_BUILD_ROOT%{_appdir}/$a

	# produce spec template
	cat > $a-desc.spec <<-EOF
		%%package $a
		Summary:	$a
		Group:		Development/Languages/PHP
		URL:		http://www.ezcomponents.org/docs/api/%%{version}/classtrees_$a.html
		Requires:	%%{name} = %%{version}-%%{release}

		%%description $a
		$(cat $a/DESCRIPTION)

	EOF

	cat > $a-files.spec <<-EOF
		%%files $a
		%%defattr(644,root,root,755)
		%%doc $a/{ChangeLog,CREDITS}$(
		if [ "$(ls $a/*.txt 2>/dev/null)" ]; then
			echo ""
			echo "%%doc $a/*.txt"
		fi
		)
		%%{_appdir}/$a

	EOF
done
cat *-desc.spec *-files.spec > ez.spec
rm -f *-desc.spec *-files.spec

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_appdir}
%{_appdir}/autoload

%files Archive
%defattr(644,root,root,755)
%doc Archive/{ChangeLog,CREDITS}
%{_appdir}/Archive

%files Authentication
%defattr(644,root,root,755)
%doc Authentication/{ChangeLog,CREDITS}
%doc Authentication/*.txt
%{_appdir}/Authentication

%files AuthenticationDatabaseTiein
%defattr(644,root,root,755)
%doc AuthenticationDatabaseTiein/{ChangeLog,CREDITS}
%{_appdir}/AuthenticationDatabaseTiein

%files Base
%defattr(644,root,root,755)
%doc Base/{ChangeLog,CREDITS}
%doc Base/*.txt
%{_appdir}/Base

%files Cache
%defattr(644,root,root,755)
%doc Cache/{ChangeLog,CREDITS}
%doc Cache/*.txt
%{_appdir}/Cache

%files Configuration
%defattr(644,root,root,755)
%doc Configuration/{ChangeLog,CREDITS}
%{_appdir}/Configuration

%files ConsoleTools
%defattr(644,root,root,755)
%doc ConsoleTools/{ChangeLog,CREDITS}
%doc ConsoleTools/*.txt
%{_appdir}/ConsoleTools

%files Database
%defattr(644,root,root,755)
%doc Database/{ChangeLog,CREDITS}
%{_appdir}/Database

%files DatabaseSchema
%defattr(644,root,root,755)
%doc DatabaseSchema/{ChangeLog,CREDITS}
%doc DatabaseSchema/*.txt
%{_appdir}/DatabaseSchema

%files Debug
%defattr(644,root,root,755)
%doc Debug/{ChangeLog,CREDITS}
%doc Debug/*.txt
%{_appdir}/Debug

%files Document
%defattr(644,root,root,755)
%doc Document/{ChangeLog,CREDITS}
%doc Document/*.txt
%{_appdir}/Document

%files EventLog
%defattr(644,root,root,755)
%doc EventLog/{ChangeLog,CREDITS}
%{_appdir}/EventLog

%files EventLogDatabaseTiein
%defattr(644,root,root,755)
%doc EventLogDatabaseTiein/{ChangeLog,CREDITS}
%{_appdir}/EventLogDatabaseTiein

%files Execution
%defattr(644,root,root,755)
%doc Execution/{ChangeLog,CREDITS}
%{_appdir}/Execution

%files Feed
%defattr(644,root,root,755)
%doc Feed/{ChangeLog,CREDITS}
%doc Feed/*.txt
%{_appdir}/Feed

%files File
%defattr(644,root,root,755)
%doc File/{ChangeLog,CREDITS}
%{_appdir}/File

%files Graph
%defattr(644,root,root,755)
%doc Graph/{ChangeLog,CREDITS}
%{_appdir}/Graph

%files GraphDatabaseTiein
%defattr(644,root,root,755)
%doc GraphDatabaseTiein/{ChangeLog,CREDITS}
%{_appdir}/GraphDatabaseTiein

%files ImageAnalysis
%defattr(644,root,root,755)
%doc ImageAnalysis/{ChangeLog,CREDITS}
%{_appdir}/ImageAnalysis

%files ImageConversion
%defattr(644,root,root,755)
%doc ImageConversion/{ChangeLog,CREDITS}
%doc ImageConversion/*.txt
%{_appdir}/ImageConversion

%files Mail
%defattr(644,root,root,755)
%doc Mail/{ChangeLog,CREDITS}
%doc Mail/*.txt
%{_appdir}/Mail

%files MvcMailTiein
%defattr(644,root,root,755)
%doc MvcMailTiein/{ChangeLog,CREDITS}
%{_appdir}/MvcMailTiein

%files MvcTemplateTiein
%defattr(644,root,root,755)
%doc MvcTemplateTiein/{ChangeLog,CREDITS}
%{_appdir}/MvcTemplateTiein

%files MvcTools
%defattr(644,root,root,755)
%doc MvcTools/{ChangeLog,CREDITS}
%doc MvcTools/*.txt
%{_appdir}/MvcTools

%files PersistentObject
%defattr(644,root,root,755)
%doc PersistentObject/{ChangeLog,CREDITS}
%doc PersistentObject/*.txt
%{_appdir}/PersistentObject

%files PersistentObjectDatabaseSchemaTiein
%defattr(644,root,root,755)
%doc PersistentObjectDatabaseSchemaTiein/{ChangeLog,CREDITS}
%{_appdir}/PersistentObjectDatabaseSchemaTiein

%files PhpGenerator
%defattr(644,root,root,755)
%doc PhpGenerator/{ChangeLog,CREDITS}
%{_appdir}/PhpGenerator

%files Search
%defattr(644,root,root,755)
%doc Search/{ChangeLog,CREDITS}
%doc Search/*.txt
%{_appdir}/Search

%files SignalSlot
%defattr(644,root,root,755)
%doc SignalSlot/{ChangeLog,CREDITS}
%{_appdir}/SignalSlot

%files SystemInformation
%defattr(644,root,root,755)
%doc SystemInformation/{ChangeLog,CREDITS}
%{_appdir}/SystemInformation

%files Template
%defattr(644,root,root,755)
%doc Template/{ChangeLog,CREDITS}
%doc Template/*.txt
%{_appdir}/Template

%files TemplateTranslationTiein
%defattr(644,root,root,755)
%doc TemplateTranslationTiein/{ChangeLog,CREDITS}
%{_appdir}/TemplateTranslationTiein

%files Translation
%defattr(644,root,root,755)
%doc Translation/{ChangeLog,CREDITS}
%doc Translation/*.txt
%{_appdir}/Translation

%files TranslationCacheTiein
%defattr(644,root,root,755)
%doc TranslationCacheTiein/{ChangeLog,CREDITS}
%{_appdir}/TranslationCacheTiein

%files Tree
%defattr(644,root,root,755)
%doc Tree/{ChangeLog,CREDITS}
%{_appdir}/Tree

%files TreeDatabaseTiein
%defattr(644,root,root,755)
%doc TreeDatabaseTiein/{ChangeLog,CREDITS}
%{_appdir}/TreeDatabaseTiein

%files TreePersistentObjectTiein
%defattr(644,root,root,755)
%doc TreePersistentObjectTiein/{ChangeLog,CREDITS}
%{_appdir}/TreePersistentObjectTiein

%files Url
%defattr(644,root,root,755)
%doc Url/{ChangeLog,CREDITS}
%doc Url/*.txt
%{_appdir}/Url

%files UserInput
%defattr(644,root,root,755)
%doc UserInput/{ChangeLog,CREDITS}
%{_appdir}/UserInput

%files Webdav
%defattr(644,root,root,755)
%doc Webdav/{ChangeLog,CREDITS}
%doc Webdav/*.txt
%{_appdir}/Webdav

%files Workflow
%defattr(644,root,root,755)
%doc Workflow/{ChangeLog,CREDITS}
%doc Workflow/*.txt
%{_appdir}/Workflow

%files WorkflowDatabaseTiein
%defattr(644,root,root,755)
%doc WorkflowDatabaseTiein/{ChangeLog,CREDITS}
%{_appdir}/WorkflowDatabaseTiein

%files WorkflowEventLogTiein
%defattr(644,root,root,755)
%doc WorkflowEventLogTiein/{ChangeLog,CREDITS}
%{_appdir}/WorkflowEventLogTiein

%files WorkflowSignalSlotTiein
%defattr(644,root,root,755)
%doc WorkflowSignalSlotTiein/{ChangeLog,CREDITS}
%{_appdir}/WorkflowSignalSlotTiein

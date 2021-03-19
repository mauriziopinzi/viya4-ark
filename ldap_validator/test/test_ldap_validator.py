
####################################################################
# ### test_ldap_validator.py                                 ###
####################################################################
# ### Author: SAS Institute Inc.                                 ###
####################################################################
#                                                                ###
# Copyright (c) 2020, SAS Institute Inc., Cary, NC, USA.         ###
# All Rights Reserved.                                           ###
# SPDX-License-Identifier: Apache-2.0                            ###
#                                                                ###
####################################################################
import os
import sys

import pprint
import json
import logging
import yaml
import traceback
import pytest

try:
    from yaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader
from ldap_validator.ldap_validator import pingHost, parse_connection_results, importSiteDefault, performLDAPQuery
from ldap_validator.ldap_validator import failTestSuite
from ldap_validator.library.utils import ldap_messages
from viya_ark_library.logging import ViyaARKLogger

sas_logger = ViyaARKLogger("test_report.log", logging_level=logging.INFO, logger_name="test_logger")
ldap_logger = sas_logger.get_logger()
# setup sys.path for import of viya_constants
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
#

# setup sys.path for import of ldap_constants
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))

def test_pinghost():
    ldap_server_host = "myldap.fyi.sas.com"
    result = pingHost()
    assert(result == False)

def test_failTestSuite():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            failTestSuite()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 3

def test_parse_connection_results_true():
    #sas_logger = ViyaARKLogger("test_report.log", logging_level=logging.INFO, logger_name="test_logger")
    #ldap_logger = sas_logger.get_logger()
    result = {'description': 'sizeLimitExceeded', 'dn': '', 'message': '', 'referrals': None,
              'result': 4, 'type': 'searchResDone'}
    entries = [{'attributes': {}, 'dn': 'DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'CN=Exchange Servers,OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'CN=Exchange Organization Administrators,OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'CN=Exchange Recipient Administrators,OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}]
    response = {
	"entries": [{
		"attributes": {},
		"dn": "OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=[PTD] XML Case Study Team,OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=PMM PAM Team,OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=CCG Cumulus Digital Asset Management System,OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=VSTI ONDEMAND,OU=Groups,DC=na,DC=SAS,DC=com"
	}]
    }
    verify = True
    parse_result: bool = parse_connection_results(ldap_logger, response, result, entries, verify)
    ldap_logger.info(" Parse result is " + str(parse_result))
    assert(parse_result == True)

def test_parse_connection_results_false():
    #sas_logger = ViyaARKLogger("test_report.log", logging_level=logging.INFO, logger_name="test_logger")
    #ldap_logger = sas_logger.get_logger()
    result = {'description': 'sizeLimitExceeded', 'dn': '', 'message': '', 'referrals': None,
              'result': 999, 'type': 'searchResDone'}
    entries = [{'attributes': {}, 'dn': 'DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'CN=Exchange Servers,OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'CN=Exchange Organization Administrators,OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'CN=Exchange Recipient Administrators,OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}]
    response = {
	"entries": [{
		"attributes": {},
		"dn": "OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=[PTD] XML Case Study Team,OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=PMM PAM Team,OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=CCG Cumulus Digital Asset Management System,OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=VSTI ONDEMAND,OU=Groups,DC=na,DC=SAS,DC=com"
	}]
    }
    verify = True
    parse_result: bool = parse_connection_results(ldap_logger, response, result, entries, verify)
    ldap_logger.info(" Parse result is " + str(parse_result))
    assert(parse_result == False)

def test_parse_connection_results_empty():
    #sas_logger = ViyaARKLogger("test_report.log", logging_level=logging.INFO, logger_name="test_logger")
    #ldap_logger = sas_logger.get_logger()
    result = {'description': 'sizeLimitExceeded', 'dn': '', 'message': '', 'referrals': None,
              'result': 4, 'type': 'searchResDone'}
    # entries = [{'attributes': {}, 'dn': 'DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'CN=Exchange Servers,OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'CN=Exchange Organization Administrators,OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}, {'attributes': {}, 'dn': 'CN=Exchange Recipient Administrators,OU=Microsoft Exchange Security Groups,DC=SAS,DC=com'}]
    entries = []

    response = {
	"entries": [{
		"attributes": {},
		"dn": "OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=[PTD] XML Case Study Team,OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=PMM PAM Team,OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=CCG Cumulus Digital Asset Management System,OU=Groups,DC=na,DC=SAS,DC=com"
	}, {
		"attributes": {},
		"dn": "CN=VSTI ONDEMAND,OU=Groups,DC=na,DC=SAS,DC=com"
	}]
    }
    verify = True
    parse_result: bool = parse_connection_results(ldap_logger, response, result, entries, verify)
    ldap_logger.info(" Parse result is " + str(parse_result))
    assert(parse_result == False)

def test_importSiteDefault_bad_file_loc():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sitedefault_loc = os.path.join(current_dir, "test_data" + os.sep + "yaml_data"
								   + os.sep + "testsitedefault_invalid.yml")
    ldap_logger.info(" sitedefault file = " + str(sitedefault_loc))
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            importSiteDefault(sitedefault_loc, ldap_logger)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 3
    ldap_logger.info("pytest code" + str(pytest_wrapped_e.value.code))

def test_importSiteDefault_keyerror():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sitedefault_loc = os.path.join(current_dir, "test_data" + os.sep + "yaml_data"
								   + os.sep + "testsitedefault_keyerror.yml")
    ldap_logger.info(" sitedefault file = " + str(sitedefault_loc))
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            importSiteDefault(sitedefault_loc, ldap_logger)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 3
    ldap_logger.info("pytest code" + str(pytest_wrapped_e.value.code))

def test_importSiteDefault_asserterror():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sitedefault_loc = os.path.join(current_dir, "test_data" + os.sep + "yaml_data"
								   + os.sep + "testsitedefault_assertion.yml")
    ldap_logger.info(" sitedefault file = " + str(sitedefault_loc))
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            importSiteDefault(sitedefault_loc, ldap_logger)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 3
    ldap_logger.info("pytest code" + str(pytest_wrapped_e.value.code))

def test_importSiteDefault_valid():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sitedefault_loc = os.path.join(current_dir, "test_data" + os.sep + "yaml_data"
								   + os.sep + "testsitedefault_invalidServer.yml")
    ldap_logger.info(" sitedefault file = " + str(sitedefault_loc))
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            importSiteDefault(sitedefault_loc, ldap_logger)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 3
    ldap_logger.info("pytest code" + str(pytest_wrapped_e.value.code))

def test_performLDAPQuery_invalid():
    searchBase = "OU = Groups, DC = na, DC = SAS, DC = com"
    searchFilter = "(objectclass= *)"
    server = "myldapserver.mycompany.com"

    parse_result = performLDAPQuery(ldap_logger, server, searchBase, searchFilter, False)
    assert(parse_result == False)


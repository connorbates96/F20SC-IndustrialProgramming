#Imports
import pandas
from collections import Counter
import re
import matplotlib.pyplot as plt
import json
import sys

#Dictionaries used for getting the continent that a countr belongs to
continentsFullName = { 'AF' : 'Africa', 'AS' : 'Asia', 'EU' : 'Europe', 'NA' : 'North America', 'SA' : 'South America', 'OC' : 'Oceania', 'AN' : 'Antarctica' }
cntry_to_cont = { 'AF' : 'AS', 'AX' : 'EU', 'AL' : 'EU', 'DZ' : 'AF', 'AS' : 'OC', 'AD' : 'EU', 'AO' : 'AF', 'AI' : 'NA', 'AQ' : 'AN', 'AG' : 'NA', 'AR' : 'SA', 'AM' : 'AS', 'AW' : 'NA', 'AU' : 'OC', 'AT' : 'EU', 'AZ' : 'AS', 'BS' : 'NA', 'BH' : 'AS', 'BD' : 'AS', 'BB' : 'NA', 'BY' : 'EU', 'BE' : 'EU', 'BZ' : 'NA', 'BJ' : 'AF', 'BM' : 'NA', 'BT' : 'AS', 'BO' : 'SA', 'BQ' : 'NA', 'BA' : 'EU', 'BW' : 'AF', 'BV' : 'AN', 'BR' : 'SA', 'IO' : 'AS', 'VG' : 'NA', 'BN' : 'AS', 'BG' : 'EU', 'BF' : 'AF', 'BI' : 'AF', 'KH' : 'AS', 'CM' : 'AF', 'CA' : 'NA', 'CV' : 'AF', 'KY' : 'NA', 'CF' : 'AF', 'TD' : 'AF', 'CL' : 'SA', 'CN' : 'AS', 'CX' : 'AS', 'CC' : 'AS', 'CO' : 'SA', 'KM' : 'AF', 'CD' : 'AF', 'CG' : 'AF', 'CK' : 'OC', 'CR' : 'NA', 'CI' : 'AF', 'HR' : 'EU', 'CU' : 'NA', 'CW' : 'NA', 'CY' : 'AS', 'CZ' : 'EU', 'DK' : 'EU', 'DJ' : 'AF', 'DM' : 'NA', 'DO' : 'NA', 'EC' : 'SA', 'EG' : 'AF', 'SV' : 'NA', 'GQ' : 'AF', 'ER' : 'AF', 'EE' : 'EU', 'ET' : 'AF', 'FO' : 'EU', 'FK' : 'SA', 'FJ' : 'OC', 'FI' : 'EU', 'FR' : 'EU', 'GF' : 'SA', 'PF' : 'OC', 'TF' : 'AN', 'GA' : 'AF', 'GM' : 'AF', 'GE' : 'AS', 'DE' : 'EU', 'GH' : 'AF', 'GI' : 'EU', 'GR' : 'EU', 'GL' : 'NA', 'GD' : 'NA', 'GP' : 'NA', 'GU' : 'OC', 'GT' : 'NA', 'GG' : 'EU', 'GN' : 'AF', 'GW' : 'AF', 'GY' : 'SA', 'HT' : 'NA', 'HM' : 'AN', 'VA' : 'EU', 'HN' : 'NA', 'HK' : 'AS', 'HU' : 'EU', 'IS' : 'EU', 'IN' : 'AS', 'ID' : 'AS', 'IR' : 'AS', 'IQ' : 'AS', 'IE' : 'EU', 'IM' : 'EU', 'IL' : 'AS', 'IT' : 'EU', 'JM' : 'NA', 'JP' : 'AS', 'JE' : 'EU', 'JO' : 'AS', 'KZ' : 'AS', 'KE' : 'AF', 'KI' : 'OC', 'KP' : 'AS', 'KR' : 'AS', 'KW' : 'AS', 'KG' : 'AS', 'LA' : 'AS', 'LV' : 'EU', 'LB' : 'AS', 'LS' : 'AF', 'LR' : 'AF', 'LY' : 'AF', 'LI' : 'EU', 'LT' : 'EU', 'LU' : 'EU', 'MO' : 'AS', 'MK' : 'EU', 'MG' : 'AF', 'MW' : 'AF', 'MY' : 'AS', 'MV' : 'AS', 'ML' : 'AF', 'MT' : 'EU', 'MH' : 'OC', 'MQ' : 'NA', 'MR' : 'AF', 'MU' : 'AF', 'YT' : 'AF', 'MX' : 'NA', 'FM' : 'OC', 'MD' : 'EU', 'MC' : 'EU', 'MN' : 'AS', 'ME' : 'EU', 'MS' : 'NA', 'MA' : 'AF', 'MZ' : 'AF', 'MM' : 'AS', 'NA' : 'AF', 'NR' : 'OC', 'NP' : 'AS', 'NL' : 'EU', 'NC' : 'OC', 'NZ' : 'OC', 'NI' : 'NA', 'NE' : 'AF', 'NG' : 'AF', 'NU' : 'OC', 'NF' : 'OC', 'MP' : 'OC', 'NO' : 'EU', 'OM' : 'AS', 'PK' : 'AS', 'PW' : 'OC', 'PS' : 'AS', 'PA' : 'NA', 'PG' : 'OC', 'PY' : 'SA', 'PE' : 'SA', 'PH' : 'AS', 'PN' : 'OC', 'PL' : 'EU', 'PT' : 'EU', 'PR' : 'NA', 'QA' : 'AS', 'RE' : 'AF', 'RO' : 'EU', 'RU' : 'EU', 'RW' : 'AF', 'BL' : 'NA', 'SH' : 'AF', 'KN' : 'NA', 'LC' : 'NA', 'MF' : 'NA', 'PM' : 'NA', 'VC' : 'NA', 'WS' : 'OC', 'SM' : 'EU', 'ST' : 'AF', 'SA' : 'AS', 'SN' : 'AF', 'RS' : 'EU', 'SC' : 'AF', 'SL' : 'AF', 'SG' : 'AS', 'SX' : 'NA', 'SK' : 'EU', 'SI' : 'EU', 'SB' : 'OC', 'SO' : 'AF', 'ZA' : 'AF', 'GS' : 'AN', 'SS' : 'AF', 'ES' : 'EU', 'LK' : 'AS', 'SD' : 'AF', 'SR' : 'SA', 'SJ' : 'EU', 'SZ' : 'AF', 'SE' : 'EU', 'CH' : 'EU', 'SY' : 'AS', 'TW' : 'AS', 'TJ' : 'AS', 'TZ' : 'AF', 'TH' : 'AS', 'TL' : 'AS', 'TG' : 'AF', 'TK' : 'OC', 'TO' : 'OC', 'TT' : 'NA', 'TN' : 'AF', 'TR' : 'AS', 'TM' : 'AS', 'TC' : 'NA', 'TV' : 'OC', 'UG' : 'AF', 'UA' : 'EU', 'AE' : 'AS', 'GB' : 'EU', 'US' : 'NA', 'UM' : 'OC', 'VI' : 'NA', 'UY' : 'SA', 'UZ' : 'AS', 'VU' : 'OC', 'VE' : 'SA', 'VN' : 'AS', 'WF' : 'OC', 'EH' : 'AF', 'YE' : 'AS', 'ZM' : 'AF', 'ZW' : 'AF' }


#Getting information directly from the file-------------------------------------
def loadFromFileReadEvent(path):
    """Loads the data from the file specified by path and checks that the lines
    to be saved are of event_type 'read' """
    data = []
    with open(path) as data_file:
        for line in data_file:
            if '"event_type":"read"' in line:
                data.append(json.loads(line))
    return data

def loadFromFileDocID(path, documentID):
    """Loads the data from the file specified by path as long as the
    subject_doc_id matches the parameter documentID. Before returning the data,
    all non-read events are removed"""
    data = []
    docIDString = '"subject_doc_id":"{}"'.format(documentID)
    with open(path) as data_file:
        for line in data_file:
            if docIDString in line:
                data.append(json.loads(line))
    removeNonReads(data)
    return data

def loadFromFileVisID(path, visitorUUID):
    """Loads the data from the file specified by path as long as the
    visitor_uuid matches the parameter visitorUUID. Before returning the data,
    all non-read events are removed"""
    data = []
    visIDString = '"visitor_uuid":"{}"'.format(visitorUUID)
    with open(path) as data_file:
        for line in data_file:
            if visIDString in line:
                data.append(json.loads(line))
    removeNonReads(data)
    return data


def removeNonReads(documents):
    """Removes all of the non-read events from documents"""
    for line in documents:
        if '","event_type":"read","subject_type":' not in line:
            documents.remove(line)

#TASK2--------------------------------------------------------------------------

#Takes a list of all matched lines and returns a list of the countriesList
def getCountriesList(matchedLines):
    """Given a list of 'matchedLines', this functions finds which country the
    document's reader is from and returns a list of each reader's country"""
    countryList = []
    for entry in matchedLines:
        country = entry["visitor_country"]
        countryList.append(country)
    return countryList

#Takes a list of all countries and replaces it with the continent
def getContinentList(countriesList):
    """Given a list of countries, this function uses the dictionary specified at
    the top of this document to convert the list of countries to a list of continents"""
    continentList = []
    for x in range(len(countriesList)):
        try:
            continentList.append(cntry_to_cont[countriesList[x]])
        except:
            print("Error:: getContinentList:: Country Code Isn't Recognised -- {}\n".format(countriesList[x]))
    return continentList

#Given a list of abbreviated continent names, returns a list of the full name
def getFullContinentName(continentList):
    """Simple function for converting the list of abbreviated continent names
    to their full name"""
    fullContinentList = []
    for x in range(len(continentList)):
            fullContinentList.append(continentsFullName[continentList[x]])
    return fullContinentList

#TASK3--------------------------------------------------------------------------

#Return a list of all occurrences of the visitor_agent given a list of all read lines
def getBrowserAgents(data):
    """Given some data which has already been filtered, the visitor_useragent (i.e.
    the browser) is extracted from each line and returned as a list"""
    visitorAgents = []
    for entry in data:
        agent = entry["visitor_useragent"]
        visitorAgents.append(agent)
    return visitorAgents


#Return a list of all occurrences of the visitor_agent given a list of all read lines
#Uses regular expression to seach for the agent
def getBrowserAgentsNameOnly(data):
    """Given some data which has already been filtered, the visitor_useragent (i.e.
    the browser) is extracted from each line and returned as a list. Unlike getBrowserAgents,
    this function only returns a list of the browser name (such as Mozilla, Opera etc.)"""
    visitorAgents = []
    for entry in data:
        agent = entry["visitor_useragent"]
        agentName = re.search("(.*?)/", agent).group(1)
        visitorAgents.append(agentName)
    return visitorAgents

#TASK4--------------------------------------------------------------------------

#Loads files with docID, for each entry, gets visitor and returns a list of unique visitors
def getAllReaders(documentID, filePath):
    """Function for getting all readers that have read the specified document (documentID).
    First a call to loadFromFileDocID filters the data by document ID and then returns a list
    of each of the visitors UUIDs. Visitors is first made as a set so that the visitor UUIDs
    don't repeat then it is converted to a list before returning."""
    data = loadFromFileDocID(filePath, documentID)
    visitors = set()
    for entry in data:
            visitor = entry["visitor_uuid"]
            visitors.add(visitor)
    return list(visitors)

#Loads files with visitorID, for each entry, gets docID and returns a list of unique docIDs
def getVisitorsReads(visitorUUID, filePath):
    """Function for getting all of the document IDs that have been read by a certain,
    specified user. A call to loadFromFileVisID returns a list of all 'read' lines in the
    data that contain the visitorUUID anf then extracts the document ID from each line and returns
    this as a list. Documents is first made as a set to ensure there is no duplicates before being
    returned as a list"""
    data = loadFromFileVisID(filePath, visitorUUID)
    documents = set()
    for entry in data:
        try:
            document = entry["subject_doc_id"]
            documents.add(document)
        except:
            print("Error:: getVisitorsReads:: subject_doc_id not found\n")
    return list(documents)

#Gets all readers of this docID, for each reader, gets docIDs theyve read and returns list of these (contains duplicates)
def getAlsoLikes(documentID, filePath, sortFunction=len, visitorUUID=None):
    """Function for finding which documents have also been read by a user that read the document
    with the ID that is provided. If a visitorUUID is provided, then only the documents read by
    that user are returned. The list is sorted by the sortFunction parameter (default set to len)
    before being returned"""
    alsoLikes = []
    if visitorUUID is None:
        readers = getAllReaders(documentID, filePath)
        for reader in readers:
            documents = getVisitorsReads(reader, filePath)
            alsoLikes.extend(documents)
    else:
        documents = getVisitorsReads(visitorUUID, filePath)
        alsoLikes.extend(documents)

    alsoLikes.sort(key=sortFunction)
    return alsoLikes

#MATPLOT------------------------------------------------------------------------

def createHistogramOfCount(dataList, title, xaxisLabel, extraLabelRoom):
    """
    Takes a list of occurences and shows a histogram showing the count of each item

    Inputs: dataList->input list of occurences
            title->title for the Histogram
            xaxisLabel->label for the x axis
            extraLabelRoom->adds extra room at bottom for larger labels
    """
    data_counts = Counter(dataList)
    df = pandas.DataFrame.from_dict(data_counts, orient="index")
    df.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xaxisLabel)
    plt.ylabel("Count")
    plt.legend().remove()
    if extraLabelRoom is True:
        plt.subplots_adjust(bottom = 0.3)
    plt.show()

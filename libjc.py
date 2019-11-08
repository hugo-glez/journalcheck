# Copyright (c) 2019 Hugo Gonzalez @hugo_glez
#
# This file is part of JournalCheck
# (see github.com/hugo-glez/journalcheck).

# License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
#
""" 
This script consult the scimago website to ask for ISSN or other keyword.
ISSN works better because only one result is returned in the case it
exists. Also it retrieves the image of the journal

It can be used in command line or the gui interface.

"""

import requests as req
import sys
from bs4 import BeautifulSoup

BASE = "https://www.scimagojr.com/"
SITE = "https://www.scimagojr.com/journalsearch.php?q="
IMGURL = "https://www.scimagojr.com/journal_img.php?id="


def getinfo(query):
    """ Get the information from the scimago website

    Parameters
    ----------
    query : str
        The ISSN or keyword to query the website

    Returns
    -------
    t : str
        The string that identified the journal or the text "Nothing Found!"
    im : data
        The data from the png image retrieved from the website, or empty.
    
    """
    p = req.get(SITE+query)

    soup = BeautifulSoup(p.text, "lxml")

    # This part of the website have the results
    r = soup.find_all('div', class_="search_results")

    try:
        # Get the link
        N = r[0].find_all('a')[0]
        #print(N)
        # This is the text of the html part
        t = N.text
        # Find the link and extract the id 
        u = N.attrs['href']
        u = u[u.find('=')+1:u.find('&')]
        ii = IMGURL+u 
        # Obtain the png data of the image
        ix = req.get(ii)
        im = ix.content
        #print(ii)
    except:
    # Nothing found, so no result.
        t = "Nothing Found!"
        im = ""

    return(t,im)


import multiprocessing as mp
from soup import main
import time
import pickle
from convertFormat import formattedServices
from serviceCodeMap import codeMap
import pandas as pd

###################################################################################################

# manual setup
# thread count should be the closet factor of numURlstoCheck to your number of processor Cores * 2

threads = 62
numURLStoCheck = 3641756
servOutputName = "servResults.xlsx"
geoOutputName = "geoResults.xlsx"

# setup
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def loadLinks(subset):
    with open (subset, 'rb') as f:
        urls = pickle.load(f)
    numURLStoCheck = len(urls)
    return urls

urls = loadLinks("allLinks")


##########################################################################################


if __name__ == "__main__":
    #creating shared variables
    manager = mp.Manager()
    rList = manager.list()
    stateDict = manager.dict()
    serviceDict = manager.dict()
    serviceReviewsDict = manager.dict()
    jobs = []
    threadLoad = numURLStoCheck / threads

    #creating dictionaries for each service and state
    for service in codeMap:
        serviceDict[service] = []
        serviceReviewsDict[service] = []
    for state in states: 
        stateDict[state] = []


    #duplicating codeMap reversed
    codeToState = {}
    for service in codeMap:
        codeToState[codeMap[service]] = service


    # launch all threads
    for server in range(1,threads + 1):
        p = mp.Process(target=main, args= (threadLoad* (server - 1), threadLoad * (server) - 1, rList, stateDict, serviceDict, urls, codeToState, serviceReviewsDict))
        jobs.append(p)

    start = time.time()
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    print(time.time() - start)


    # write results to excel (can change column names and such)
    dServ = {"Service": list(codeMap.keys()), "Number of Pros": [], "Average Reviews per Pro": []}
    dGeo = {"State": [], "Number of Pros": []}
    
    for service in codeMap: 
        dServ["Number of Pros"] += [len(serviceDict[service])]
        servReview = serviceReviewsDict[service] 
        try:
            dServ["Average Reviews per Pro"] += [sum(servReview) / len(servReview)]
        except ZeroDivisionError: 
            dServ["Average Reviews per Pro"] += [None]

    for state in stateDict.keys():
        dGeo["State"] += [state]
        dGeo["Number of Pros"] += [len(stateDict[state])]


    dfServ = pd.DataFrame(data=dServ)
    dfGeo = pd.DataFrame(data=dGeo)
    dfServ.to_excel(servOutputName)
    dfGeo.to_excel(geoOutputName)
    
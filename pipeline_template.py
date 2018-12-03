
#==========================================================================
#=============================DEPENDENCIES=================================
#==========================================================================


import sys
sys.path.append('/pipeline/')

import pipeline_dfci
import datetime
import random
import string
import utils

#==========================================================================
#============================PARAMETERS====================================
#==========================================================================



projectName = 'work'
dataFile = '/home/%s/datatable.txt' % (projectName)
genome ='hg19'
annotFile = '/pipeline/annotation/%s_refseq.ucsc' % (genome)

#project folders
projectFolder = '/home/%s/' % (projectName) #PATH TO YOUR PROJECT FOLDER

#standard folder names
gffFolder ='%sgff/' % (projectFolder)
macsFolder = '%smacsFolder/' % (projectFolder)
macsEnrichedFolder = '%smacsEnriched/' % (projectFolder)
mappedEnrichedFolder = '%smappedEnriched/' % (projectFolder)
mappedFolder = '%smappedFolder/' % (projectFolder)
wiggleFolder = '%swiggles/' % (projectFolder)
metaFolder = '%smeta/' % (projectFolder)

#making folders
folderList = [gffFolder,macsFolder,macsEnrichedFolder,mappedEnrichedFolder,mappedFolder,wiggleFolder,metaFolder]

for folder in folderList:
    pipeline_dfci.formatFolder(folder,True)


#==========================================================================
#=======================LOADING DATA ANNOTATION============================
#==========================================================================

##THIS SECTION LOADS A DATA TABLE.  MUST BE UNCOMMENTED FOR REST OF CODE TO WORK


#LOADING THE DATA TABLE
dataDict = pipeline_dfci.loadDataTable(dataFile)

#==========================================================================
#=============================CALL MACS====================================
#==========================================================================

##THIS SECTION CALLS THE MACS ERROR MODEL

namesList = dataDict.keys()

pipeline_dfci.callMacs(dataFile,macsFolder,namesList,overwrite=False,pvalue='1e-9')


#==========================================================================
#=======================FORMAT MACS OUTPUT=================================
#==========================================================================

##THIS SECTION FORMATS THE OUTPUT FROM MACS, CREATES THE MACSENRICHED FOLDER AND MOVES WIGGLES TO THE DESTINATION

#pipeline_dfci.formatMacsOutput(dataFile,macsFolder,macsEnrichedFolder,wiggleFolder,wigLink='/ark/wiggles/')


#==========================================================================
#====================ADDITIONAL PIPELINE ANALYSIS==========================
#==========================================================================

#==========================================================================                                      
#==============================ROSE2=======================================                                      
#==========================================================================                                      


#parentFolder = '%srose' % (projectFolder)
#parentFolder = utils.formatFolder(parentFolder,True)

##PICK RIGHT GENOME MASK FILE                                                                                    
#maskFile ='/raider/index/hg19/Masks/hg19_encode_blacklist.bed'
#bashFileName = '%srose/160825_rose.sh' %(projectFolder)
#namesList= ['B6GA_trt_H3K27Ac']
#namesList = [x for x in dataDict.keys() if 'input' not in x]

#pipeline_dfci.callRose2(dataFile,macsEnrichedFolder,parentFolder,namesList,[],'',2500,'',bashFileName,maskFile)

#print namesList


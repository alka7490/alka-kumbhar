#!/usr/bin/env python
# coding: utf-8

# Leukemia is the most common malignancy and the second most frequent general cause of childhood death. It is classified as acute lymphoid of the B- or T-lineage being the most prevalent type in children, and as acute myeloid. Although tremendous improvements have been made in the treatment of leukemia in the past few years, there is still a large proportion of patients who do not benefit from the available therapy. The overall survival of pediatric acute lymhoblastic leukemia (ALL) and acute myeloid leukemia (AML) patients treated with the current chemotherapy regimens is above 80 and 70%, respectively

# Idea behind the operation(Top 250 data  from GEO2R database which is microarray data  with Accession No GSE4072,  and the platform GPL2695 GEO2R Data(df) :https://www.ncbi.nlm.nih.gov/geo/geo2r/backend/geo2r.cgiand the genes which are  differentially expressed which are about 133 out of 250 rows are differentially expressed  gene_symbol('gs').This gene symbols are fed to the biological tool called STRING:(https://string-db.org/) to find a protein protein interaction this string gives a .tsv file which intern is input to the tool cytoscape cytoscape produces a data file which is named as cytoscape_data1 in the code)
# from this cytoscape data a new dataframe is created as df1.then top 10 from cytoscape data are selected as 'b' list
#  and 'gs'as 'b' list bothe are compared to find match and i got 2 genes out of 133 in top 10 which are important to study about the lukemia cancer.

# In[21]:



import pandas as pd   #simply import pandas 
import numpy as np
#read dataset
df=pd.read_excel(r'E:\CSIR\GEO2R Data.xlsx')


# In[ ]:





# In[4]:


#datframe collection of rows and column

df


# In[7]:


Gene_symbol=df['Gene.symbol'] #selected particular column which i needed this is nothing but the series with same datatype


# In[8]:


#see the type of the Gene_symbol
type(Gene_symbol)


# In[9]:


#simple opetaion to drop the values which are Nan
df.dropna(inplace=True)


# In[98]:


Gene_symbol


# In[11]:


#using pandas we can count the no of entries in particular column or dataset 

(Gene_symbol).count()


# In[12]:


#i reassigned the Gene_symbol to gs for simple access 
gs=(Gene_symbol).unique()


# In[22]:


sort_by_pvalues=np.sort(['P.Values']) #........................sorted the dataframe by column P.Value in ascending order

sort_by_pvalues
# In[331]:


df


# In[309]:


#....exported new file  CYTOSCAPE FILE


# In[26]:


cytoscape_data=pd.read_excel(r'C:\Users\dell\Desktop\cytoscape_data1.xlsx')


# In[27]:


cytoscape_sorted=np.sort(['Degree'])#............sorted by degree descenind 


# In[28]:


cytoscape_data.iloc[1::]


# In[29]:


cytoscape_data['Degree'].max() #find highest value in the column using max() function


# In[30]:


cytoscape_sorted=np.sort(['Degree'], axis=0)


# In[31]:


#cytoscape_data


# In[32]:


cytoscape_data=pd.DataFrame(cytoscape_data,columns=['name','Degree','BetweennessCentrality','ClosenessCentrality','NeighborhoodConnectivity'])


# In[33]:


cytoscape_data    #..created new dataframe with five columns only which are the strong features of the gene


# In[ ]:





# In[45]:


df1=cytoscape_data


# In[46]:


df1.dropna()           #.......again data is cleaned 


# In[114]:



# top 10 values are selected for the comparision 
b=df1.loc[0:10].tolist()
b


# In[123]:


for i in range(0,10):
    
    for j in range(0,133): 
        
        if a[j]==b[i]:       
             print("found the match at {}th position".format(j))
        
            


# In[ ]:





# bacteriatool-
bactetool is a corpus of python script to deal with a lot of problem about bacteria genome analysis. 

you can use it to manage the data created by resfinder.py(https://bitbucket.org/genomicepidemiology/resfinder.git) to build a csv matrix about the presence of drug resistance genes in different individuals by Resfinder2csv.py. 

you can use it to manage the data created by toxicity database :VFDB by blast2.7(default output) to build a csv matrix about the presence of drug toxicity genes in different individuals by VFDB2csv.py.

you can use it to extract the information like "organism","isolation_source","host","country","lat_lon","collection_date","sample_name" of GBK(GCA) file form NCBI and create a csv matrix of your information by GBKinf2csv.py. 
___
In the manage of Resfinder2csv.py /VFDB2csv.py /GBKinf2csv.py you should put all you file into one dir.
You use the script by commanding python Resfinder2csv.py /VFDB2csv.py /GBKinf2csv.py <Input_dir> <Output_file>

In the manage of snpdistance.py.
You use the script by commanding python snpdistance.py <Input_file> <Output_file>

In the manage of recombinant2out.py.
You use the script by commanding python recombinant2out.py <Input_file> <recombinant.txt form fastGear> <Output_file>


 

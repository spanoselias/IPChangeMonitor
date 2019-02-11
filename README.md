# Real-Time data synchronization tool 
Real-Time replication tool will be mainly used to backup critical files from a local, or even remote locations such as NAS (e.g synology).
The idea behind this project is to have a tool that can be automatically backup critical files based on an event (change, modified, added and deleted files) or scheduled task. 

What's differentiate this project from other similar tools? We will design and implement an algorithm that can hold all the versions of every backup without to create a completely new backup every time. For example, if the only difference between the new and old version is just a deleted file, then, in the new backup version the size of the backup will be almost zero bytes!
 
Thus, even though many versions can be existed at any given time, the size of every new backup will be only the new files added. 
As a result, in order to achieve that smart data structures will be used such as  trees - holds the version in every backup in combination with hashmap.
 
If somebody want to be a collaborator to this project and contribute to this idea please fell free to open an issue.      

> This project is under-development yet.
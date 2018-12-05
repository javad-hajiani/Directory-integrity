import os
import syslogclient


class Integrity:
    def __init__(self, swapfile, ip="0", port=514, directory='/etc/'):
        self.ip = ip
        self.port = port
        self.swapfile = swapfile
        self.integrity_dict = {}
        self.integritydict_last = {}
        self.directory = directory.replace(',', ' ')
        # print ("{},{},{},{}".format(self.integrity_dict,self.integritydict_last,self.swapfile,self.directory))

#List Section
    def list_now(self):
        cmd = "find {} -type f | xargs md5sum ".format(self.directory)
        list_checks = os.popen(cmd).read()
        with open(self.swapfile, 'w') as swap_file:
            swap_file.writelines(list_checks)
        list_files = list_checks.split('\n')
        files_dict = {}
        for iter_dict in list_files:
                lines = iter_dict.split(' ')
                if(len(lines) > 2):
                    files_dict.update({lines[2]: lines[0]})
        self.integrity_dict = files_dict
        #print (self.integrity_dict)
        return True

    def list_last(self):
        lines = []
        if os.path.isfile(self.swapfile):
            with open(self.swapfile, 'r') as ports_file:
                result = ports_file.read().splitlines()
        else:
            cmd = "find {} -type f | xargs md5sum ".format(self.directory)
            result = os.popen(cmd).read()
            with open(self.swapfile, 'w') as integrity_file:
                integrity_file.writelines(result)
            result = result.split('\n')
        dict_last = {}
        for iter_dict in result:
            if len(iter_dict) > 1:
                lines = iter_dict.split(' ')
                #print ("Started \n {} \n Ended".format(lines))
            address = ''
            mdhash = ''
            if(len(lines) > 2):
                    dict_last.update({lines[2]: lines[0]})
            #        print ("Portdict_last = {}".format(dict_last))
        self.integritydict_last = dict_last
        return True

    def check_integrity(self):
        logger = syslogclient.LoggingClass(self.ip, self.port)
        for int_key in self.integrity_dict.keys():
            try:
                if (self.integrity_dict[int_key] != self.integritydict_last[int_key]):
                    experssion = "File Changed|{}".format(int_key)
                    command="echo \" this file {} changed \" | mail -s \"file changed {} \" {} ".format(int_key,int_key,"root")
                    os.popen(command)
                    logger.Send(experssion)
            except:
                pass

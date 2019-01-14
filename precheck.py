#!/usr/bin/python
# encoding=utf8
import os
import boto3
import hashlib
import commands

def getmd5sum(in_filename):
    md5filename = in_filename
    hasher = hashlib.md5()
    with open(md5filename,'rb') as open_file:
        content = open_file.read()
        hasher.update(content)
    return hasher.hexdigest()

def checkConfigfile(in_filename_Conf):
    openFile = "verification.txt"
    f = open(openFile, "r")
    lines = f.readlines()
    result = False
    for line in lines:
        if in_filename_Conf in line:
            result = True
    return result


def getIPandPath(in_filename_IP):
    openFile = "verification.txt"
    f = open(openFile, "r")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # print(line)
        val = line.split(',')
        val2 = val[2]
        val3 = val[3]
        val4 = val[4]
#       print "val2 = %s" % val2;
#       print "val3 = %s" % val3;
#       print "val4 = %s" % val4;
#       print "return IP is %s" % val2
#       print "return Path is %s" % val4
        return val2,val4

def getmd5sumbySSH(in_filename_S):
    ipofget,pathofget = getIPandPath(in_filename_S)
#    print "in_ipaddress is %s" % ipofget
#    print "in_path is %s" % pathofget
    command_line = 'ssh -o serveraliveinterval=60 ubuntu@{in_ipaddress} sudo md5sum {in_path}'
    formatedcmd = command_line.format(in_ipaddress=ipofget, in_path=pathofget)
#    print "command_line is %s" % formatedcmd
    p = os.popen(formatedcmd)
    x = p.read()
    return x
#    print "ssh feedback is %s" % x
    p.close()

s3 = boto3.resource('s3')
mybucket = s3.Bucket("com.cn.control-tec.deployment")
# if blank prefix is given, return everything)
bucket_prefix="qualifier/Qualifier_"
objs = mybucket.objects.filter(Prefix = bucket_prefix)
print "object is %s" % objs

for obj in objs:
    print "obj: %s" % obj
    path, filename = os.path.split(obj.key)
    print "path: %s" % path
    print "filename: %s" % filename
    # boto3 s3 download_file will throw exception if folder not exists
    try:
        os.makedirs(path)
    except:
        pass
    print "obj.key is %s" % obj.key
#    mybucket.download_file(obj.key, obj.key)
    if checkConfigfile(filename):
        print "getmd5sum(obj.key) is %s" % getmd5sum(obj.key)
        print "getmd5sumbySSH(filename) is %s" % getmd5sumbySSH(filename)
    else:
        print "Can't find the package name in the config file!"

#print (getmd5sum('/root/PycharmProjects/control-tec_verify/qualifier/Qualifier_GEELY.war'))

#print(hashlib.md5('~/PycharmProjects/control-tec_verify/qualifier/Qualifier_GEELY.war').hexdigest())
#print(md5sum('~/PycharmProjects/control-tec_verify/qualifier/Qualifier_GEELY.war'))

status,output=commands.getstatusoutput('pwd')
print "status is %s" % status;
print "output is %s" % output;

status1,output1=commands.getstatusoutput('md5sum ~/PycharmProjects/control-tec_verify/qualifier/Qualifier_GEELY.war')
print "status is %s" % status1;
print "output is %s" % output1;

#s3_conn = boto3.client('s3')
#bucket = s3_conn.

#files_in_s3 = bucket.objects.all()

#print(files_in_s3)

#if 'Contents' not in s3_result:
#    print(s3_result)

#file_list = []
#for key in s3_result['Contents']:
#    file_list.append(key['Key'])

#print("List count = {len(file_list)}")

#while s3_result['IsTruncated']:
#    continuation_key = s3_result['NextContinuationToken']
#    s3_result = s3_conn.list_object_v2(Bucket=bucket_name, Prefix=prefix, Delimiter = "/", ContinuationToken=continuation_key)
#    for key in s3_result['Contents']:
#        file_list.append(key['Key'])
#    print("List count = {len(file_list)")
#print file_list

#s3 = boto3.resource('s3')

#s3 = boto3.client('s3')
#i=0
#my_bucket = s3.Bucket('com.cn.control-tec.deployment')

#for s3_file in my_bucket.object.all():
#    print(s3_file.key)
#for bucket in s3.buckets.all():
#    for key in bucket.objects.all():
#        print(key.key)


#for key in s3.list_objects(Bucket='com.cn.control-tec.deployment', Prefix='qualifier/Qualifier_')['Contents']:
#    i=i+1
#    print "internal i is %s" % i
#    print(key['Key'],key['LastModified'],key['ETag'],key['Size'],key['StorageClass'])
#    tmp_file_name = key['Key']
#    print "tmp_file_name is %s" % tmp_file_name
#    file_name = tmp_file_name.split('/',1)[1]
#    print "file_name is %s" % file_name

#s3_bucket = boto3.resource('s3')

#s3_bucket.download_file('com.cn.control-tec.deployment',file_name,'/tmp')
#try:
#    s3_bucket.Bucket('com.cn.control-tec.deployment').download_file(KEY, '*.war')
#except botocore.exceptions.ClientError as e:
#    if e.response['Error']['Code'] == "404":
#        print("The object does not exist.")
#    else:
#        raise
#print "i is %s" % i;


#response = s3.list_buckets(Bucket='com.cn.control-tec.deployment')
#buckets = [bucket['Name'] for bucket in response['Buckets']]
#print "Bucket List: %s" % buckets





import xmlrpclib
import yaml
import argparse

parser = argparse.ArgumentParser(description='Submit tool for lava efficios')
parser.add_argument('--user', help='username', default='jenkins')
parser.add_argument('--token', help='API token', default='')
parser.add_argument('--hostname', help='hostname', default='lava-master.internal.efficios.com')
parser.add_argument('job', help='json job to submit')

args = parser.parse_args()


username = args.user
token = args.token
hostname = args.hostname
server = xmlrpclib.ServerProxy("http://%s:%s@%s/RPC2" % (username, token, hostname))

with open(args.job) as job:
    job_json = job.read()
    job_id = server.scheduler.submit_job(job_json);

print ('job_id: {0}'.format(job_id))


#### create by catbuilts - Jan 21th 2017 ####

from __future__ import print_function
from urllib.request import urlretrieve
import json
from multiprocessing import Pool, Process
from math import ceil
import requests
import mimetypes

def download_file(num_files, process_id, url, i, path_to_store='', file_link_url =''):
    """Down the image with url"""
    print("downloading {0}/{1} from process {2}...".format(i + 1, num_files, process_id))

    file_name = "process_" + str(process_id) + "_" + str(i) + str(get_extension_file(url))

    urlretrieve(url + file_link_url, path_to_store + '/' + file_name)
    # print("dowloading completed.")
    return file_name

def edit_file_before_parsing(file_name):

    filedata = None
    with open(file_name, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('for (;;);', '')

    # Write the file out again
    with open(file_name, 'w') as file:
        file.write(filedata)

def parse_json_file(json_file):
    # open json file
    with open(json_file) as data_file:
        data = json.load(data_file)

    obj_payload = data['payload']
    keys_payload = obj_payload.keys()

    first_index = (list(keys_payload))[0]

    obj_list = obj_payload[first_index]['message_shared_media']['edges']

    url_list = []
    for obj in obj_list:
        url_list.append(obj['node']['image2']['uri'])

    return url_list

#parallel
def run(args):
    process_id, urls, storing_folder = args
    num_files = len(urls)

    for i in range(num_files):
        download_file(num_files, process_id, urls[i], i+1, storing_folder)


    print("==== process {0} is done ! ======\n".format(process_id))
    return process_id


def chunks(a_list, n):
    """Yield successive n-sized chunks from a_list."""
    for i in range(0, len(a_list), n):
        yield a_list[i:i + n]


def main():
    json_file_list = ["html_1.json", "html_2.json", "html_3.json"]

    # list of a list
    url_list = []

    for json_file in json_file_list:
        edit_file_before_parsing(json_file)
        urls = parse_json_file(json_file)
        url_list += urls

    NUM_PROCESS = 3
    p = Pool(NUM_PROCESS)

    num_files = len(url_list)
    url_list_splited = list(chunks(url_list, ceil(num_files / NUM_PROCESS)))



    # prep some arguments:
    process_id_list = list(range(1, NUM_PROCESS + 1))
    ## url_list_splited
    storing_folder = ["Images"] * NUM_PROCESS

    job_args = zip(process_id_list, url_list_splited, storing_folder)

    ### Running...

    # if we use 'imap_unordered':
    # res = p.imap_unordered(run, job_args)
    # for i in res:
    #     pass

    # another way, "imap" method:
    # res = p.imap(run, job_args)
    # for i in res:
    #      pass

    # "map" as well:
    # p.map(run, job_args)

    # or "map_async"
    p.map_async(run, job_args).get()

    print("=========== DONE - The total is {} files. ============".format(num_files))


def get_extension_file(url):

    response = requests.get(url)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)

    return extension

def read_urls_file(file_name):
    f = open(file_name, 'r')
    url_next = f.readline()

    url_list = []
    while(url_next != ''):
        if (url_next.find("https://scontent.fdad1-1.fna.fbcdn.net/v/t34.0-12/") != -1):
            url_list.append(url_next.rstrip('\n')) # strip to get rid of '\n' at the end of the line
        url_next = f.readline()

    return url_list

def main_2_already_have_urls(file_name):
    url_list = read_urls_file(file_name)

    NUM_PROCESS = 3
    p = Pool(NUM_PROCESS)

    num_files = len(url_list)
    url_list_splited = list(chunks(url_list, ceil(num_files / NUM_PROCESS)))

    # prep some arguments:
    process_id_list = list(range(1, NUM_PROCESS + 1))
    ## url_list_splited
    storing_folder = ["Images"] * NUM_PROCESS

    job_args = zip(process_id_list, url_list_splited, storing_folder)

    ### Running...
    # "map_async"
    p.map_async(run, job_args).get()

    print("=========== DONE - The total is {} files. ============".format(num_files))


if __name__ == '__main__':

    main_2_already_have_urls("urls.txt")

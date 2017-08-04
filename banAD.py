import requests as rq

file_location = './split_files/'
file_name = 'banAD.txt'
file_combine = file_location + file_name

argv = ['outbound_block_list', 'bypass_list', 'proxy_list']


def outbound_block_list(file_washed):

    # argc
    outbound_block_list_clean = open(
        file_location + 'outbound_block_list.txt', mode='w').close()
    outbound_block_list_append = open(
        file_location + 'outbound_block_list.txt', mode='a')
    sub_outbound_block_list = []

    # start and end position of keyword
    start = file_washed.index('[outbound_block_list]\n')
    end = file_washed.index('[bypass_list]\n')

    # main part of function
    for line in file_washed[start + 1:end]:
        if line != '\n':
            sub_outbound_block_list.append(line)

    for line in sub_outbound_block_list:
        outbound_block_list_append.write(line)

    outbound_block_list_append.close()


def bypass_list(file_washed):

    # argc
    bypass_list_clean = open(
        file_location + 'bypass_list.txt', mode='w').close()
    bypass_list_append = open(file_location + 'bypass_list.txt', mode='a')
    sub_bypass_list = []

    # start and end position of keyword
    start = file_washed.index('[bypass_list]\n')
    end = file_washed.index('[proxy_list]\n')

    # main part of function
    for line in file_washed[start + 1:end]:
        if line != '\n':
            sub_bypass_list.append(line)

    for line in sub_bypass_list:
        bypass_list_append.write(line)

    bypass_list_append.close()
    pass


def edit_file(file_combine):

    with open(file_combine, mode='r') as f_open:
        file_washed = []
        for line in f_open.readlines():
            if line[0] == '#':
                continue
            else:
                file_washed.append(line)
        f_open.close()
        outbound_block_list(file_washed)
        bypass_list(file_washed)


def download_file(file_combine):
    raw_file = rq.get(
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/banAD.acl")

    with open(file_combine, mode='w') as f_write:
        f_write.write(raw_file.text)
        f_write.close()


def main():
    print("Hello World")

    download_file(file_combine)
    edit_file(file_combine)


if __name__ == '__main__':
    main()

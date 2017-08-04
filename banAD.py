import requests as rq

file_location = './split_files/'
file_name = 'banAD.txt'
file_combine = file_location + file_name

argv = ['outbound_block_list', 'bypass_list', 'proxy_list']


def outbound_block_list(file):
    outbound_block_list_write = open(
        file_location + 'outbound_block_list.txt', mode='a')
    pass


def bypass_list(file):
    bypass_list_write = open(file_location + 'bypass_list.txt', mode='a')
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
    # print(raw_file.text)
    with open(file_combine, mode='w') as f_write:
        f_write.write(raw_file.text)
        f_write.close()


def main():
    print("Hello World")

    download_file(file_combine)
    edit_file(file_combine)


if __name__ == '__main__':
    main()

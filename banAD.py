import requests as rq

file_location = './split_files/banAD.txt'


def edit_file(file_location):
    pass


def download_file(file_location):
    raw_file = rq.get(
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/banAD.acl")
    # print(raw_file.text)
    with open(file_location, mode='w') as f:
        f.write(raw_file.text)
        f.close()


def main():
    print("Hello World")

    download_file(file_location)
    edit_file(file_location)


if __name__ == '__main__':
    main()

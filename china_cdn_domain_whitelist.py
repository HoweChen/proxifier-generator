import requests as rq
import copy


def top_edit(top_list):
    top_list_temp = top_list[0:-1]
    top_list_temp = [x for x in top_list_temp if x[0] != '#']
    top_list_temp = ['*' + x for x in top_list_temp]
    for i in range(1, len(top_list_temp)):
        top_list_temp[i] = ';' + top_list_temp[i]

    top_list_result = ''
    for line in top_list_temp:
        top_list_result += line

    with open('./split_files/top_list.txt', mode='w', encoding='utf8') as top_list_clear:
        top_list_clear.close()

    with open('./split_files/top_list.txt', mode='a', encoding='utf8') as top_list_append:
        top_list_append.write(top_list_result)


def cdn_edit(cdn_list):
    # print(cdn_list)
    cdn_list_temp = [x for x in cdn_list if x != '']
    cdn_list_temp = [x for x in cdn_list_temp if x[0] != '#']
    cdn_list_temp = ['*.' + x for x in cdn_list_temp]
    for i in range(0, len(cdn_list_temp)):
        cdn_list_temp[i] = cdn_list_temp[i] + ';'

    cdn_list_result = ''
    for line in cdn_list_temp:
        cdn_list_result += line

    with open('./split_files/cdn_list.txt', mode='w', encoding='utf8') as cdn_list_clear:
        cdn_list_clear.close()

    with open('./split_files/cdn_list.txt', mode='a', encoding='utf8') as cdn_list_append:
        cdn_list_append.write(cdn_list_result)


def cdn_list():
    raw_cdn_list = rq.get(
        'https://raw.githubusercontent.com/mawenjian/china-cdn-domain-whitelist/master/china-cdn-domain-whitelist.txt')

    raw_cdn_list = raw_cdn_list.text.split('\n')
    cdn_edit(raw_cdn_list)


def top_list():
    raw_top_list = rq.get(
        'https://raw.githubusercontent.com/mawenjian/china-cdn-domain-whitelist/master/china-top-website-whitelist.txt')

    raw_top_list = raw_top_list.text.split('\n')
    top_edit(raw_top_list)


def main():
    print('Hello World')
    top_list()
    cdn_list()


if __name__ == '__main__':
    main()

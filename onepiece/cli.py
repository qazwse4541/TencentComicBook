import argparse


def cli():
    """
    根据腾讯漫画id下载图片,默认下载海贼王最新一集。

    下载海贼王最新一集:
    python3 onepiece.py

    下载漫画 id=505430 最新一集:
    python3 onepiece.py -id 505430

    下载漫画 id=505430 所有章节:
    python3 onepiece.py -id 505430 -m all

    下载漫画 id=505430 第800集:
    python3 onepiece.py -id 505430 -c 800

    下载漫画 id=505430 倒数第二集:
    python3 onepiece.py -id 505430 -c -2

    下载漫画 id=505430 1到5集,7集，9到10集:
    python3 onepiece.py -id 505430 -i 1-5,7,9-10
    """
    msg = {
        'comicid': '漫画id，海贼王: 505430 (http://ac.qq.com/Comic/ComicInfo/id/505430)',
        'chapter': '要下载的章节chapter，默认下载最新章节。如 -c 666',
        'interval': '要下载的章节区间, 如 -i 1-5,7,9-10',
        'thread': '线程池数,默认开启8个线程池,下载多个章节时效果才明显',
        'all': '若设置了则下载该漫画的所有章节, 如 --all',
        'pdf': '若设置了则生成pdf文件, 如 --pdf',
        'output': '文件保存路径，默认保存在当前路径下的download文件夹',
        'site': '网站：支持qq，ishuhui',
        'mail': '若设置了则发送到邮箱, 如 --mail。需要预先创建配置文件。\
可以参照onepiece/config.py.example文件，创建并修改onepiece/config.py文件',
    }
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', '--comicid', type=int, default=505430, help=msg['comicid'])
    parser.add_argument('-i', '--interval', type=str, help=msg['interval'])
    parser.add_argument('-c', '--chapter', type=int, default=-1, help=msg['chapter'])
    parser.add_argument('-t', '--thread', type=int, default=8, help=msg['thread'])
    parser.add_argument('--all', action='store_true', help=msg['all'])
    parser.add_argument('--pdf', action='store_true', help=msg['pdf'])
    parser.add_argument('--mail', action='store_true', help=msg['mail'])
    parser.add_argument('-o', '--output', type=str, default='./download', help=msg['output'])
    parser.add_argument('--site', type=str, default='qq', choices=('qq', 'ishuhui'), help=msg['site'])
    args = parser.parse_args()
    from onepiece.site import ComicBook
    crawler = ComicBook(args)
    crawler.run()

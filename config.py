from pywebio.output import *
from database import userDB, configDB
from json import loads


def get_configs(cids):
    configs = configDB.query(cids)
    print(configs)
    widgets = []
    for cid, name, owner, data in configs:
        js = loads(data)
        color, bname = userDB.query('COLOR,NICKNAME', USERNAME=owner)
        widgets.append(
            put_collapse(f'配置：{name}', [
                put_tabs([
                    {'title': '基本信息', 'content': [
                        put_markdown(f'`配置所有`：<font color="{color}">{bname}</font>'),
                        put_markdown(f'`配置序号`：{cid}'),
                        put_markdown(f'`直播间号`：{js["roomid"]}'),
                        put_markdown(f'`监听阈值`：{js["limited_density"]}'),
                        put_markdown(f'`输出间隔`：{js["send_rate"]}'),
                        put_markdown('`监听词句`：\n&emsp;'+"\n&emsp;".join(js["listening_words"])),
                        put_markdown('`输出词句`：\n&emsp;'+"\n&emsp;".join(js["goodnight_words"])),
                    ]},
                    {
                        'title': '输出终端',
                        'content': [
                            put_buttons([
                                {'label': '▷', 'value': f'{cid}.run'},
                                {'label': '■', 'color': 'danger', 'value': f'{cid}.exit'}
                            ], onclick=lambda _: put_markdown(f'`{_}`', scope=f'scrollable_{_.split(".")[0]}')),
                            put_scrollable(put_scope(f'scrollable_{cid}'), height=200, keep_bottom=True)
                        ]
                    },
                    {'title': '源代码', 'content': put_code(data, 'json')},
                ]).style('border:none;')
            ])
        )
    return widgets


if __name__ == '__main__':
    '''
    configDB.insert(CID=1, NAME='曹你', OWNER='Admin', DATA='fuck you')
    configDB.insert(CID=2, NAME='曹我', OWNER='Admin2', DATA='fuck me')
    configDB.insert(CID=3, NAME='曹谁', OWNER='Admin3', DATA='fuck who')
    '''
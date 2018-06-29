# -*-coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def output_html(self):
        f = open('output.html', 'w', encoding='utf-8')
        f.write('<html >')
        f.write("<meta %s>" % 'http-equiv = "Content-Type" content = "text/html;charset=UTF-8"')
        f.write('<body>')
        f.write('<table>')
        for data in self.datas:
            f.write('<tr>')
            f.write('<td>{0}</td>' .format(data['url']))
            f.write('<td>{0}</td>' .format(data['title']))
            f.write('<td>{0}</td>' .format(data['summary']))
            f.write('</tr>')
        f.write('</table>')
        f.write('</body>')
        f.write('</html>')
        f.close()

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

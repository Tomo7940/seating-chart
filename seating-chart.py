# coding: UTF-8

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm


class SeatingChartMaker:

    @staticmethod
    def createPdf():
        # 白紙をつくる（A4縦）
        FILENAME = 'HelloWorld.pdf'
        c = canvas.Canvas(FILENAME, pagesize=portrait(A4))

        # フォント登録
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
        font_size = 20
        c.setFont('HeiseiMin-W3', 20)

        # 真ん中に文字列描画
        width, height = A4  # A4用紙のサイズ
        str = "Hello, World!"
        c.drawCentredString(width / 2, height / 2 - font_size * 0.4, str)

        # 線を引く
        # c.rect(2*cm, 2*cm, 6*cm, 6*cm, stroke=1, fill=1)

        c.line(5*cm, 5*cm, 5*cm, 6*cm)

        # Canvasに書き込み
        c.showPage()
        # ファイル保存
        c.save()


if __name__ == '__main__':
    SeatingChartMaker.createPdf()

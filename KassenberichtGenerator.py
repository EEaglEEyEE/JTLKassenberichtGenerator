#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

import pyodbc
import ssl
import smtplib
import email

from fpdf import FPDF
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# PDF Tabellenanpassung - optional
Titel = 'Kassenbericht - Firma - Kasse'
Bonnummer_width = 22
Anzahl_width = 12
Artikelname_width = 105
Preis_width = 15
Rabatt_width = 16
Uhrzeit_width = 20
border = 1
header_row_height = 10

# PDF - obligatorisch
path = 'C:\Kassenberichte\\' # Speicherpfad des PDFs angeben
Kassenname = 'Kasse' # Kassenname angeben

# Mail - obligatorisch
sender_email = "Absender E-Mail"
receiver_email = "Empfänger E-Mail"
password = "Absender Passwort"
mail_server = "smtp.server.com"
port = 465

# SQL: Verbindungsaufbau - obligatorisch
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=Serveradresse,Port\Instanz;'  # SQL Server, Port und Instanz eintragen
                      'Database=Datenbankname;'  # Datenbankname eintragen
                      'UID=user;'  # SQL User eintragen
                      'PWD=Password;')  # SQL Password eintragen

cursor = conn.cursor()

# SQL: Query
cursor.execute('SELECT  b.cInetBestellNr, '
               'cast(bp.nAnzahl as float), '
               'bp.cString, '
               'ROUND(cast((bp.fVKNetto * 1.16) as float), 2), '
               'convert(varchar, b.dErstellt, 8) '

               'FROM [eazybusiness].[dbo].[tBestellung] AS b '
               'INNER JOIN [eazybusiness].[dbo].[tbestellpos] AS bp '
               'ON bp.tBestellung_kBestellung = b.kBestellung '
               'INNER JOIN [eazybusiness].[dbo].[tPlattform] AS p '
               'ON b.nPlatform = p.nPlattform '

               'Where p.nPlattform = 7 '
               'AND b.dErstellt >= cast (GETDATE() as DATE)'
               'AND bp.cString <> \'Selbstabholer\' '
               )

# 'Where p.nPlattform = 7 '                                         #erste Kasse JTL-POS
# 'Where p.nPlattform = 151 '                                       #erste Kasse LS-POS (wird einfach fortgeführt: 152,153,...)
# 'AND b.dErstellt >= cast (GETDATE() as DATE)'                     #Heute
# 'AND b.dErstellt >= dateadd(day,-1, cast(getdate() as date))'     #Gestern bis Heute

data = list(cursor)

Umsatz = 0
AnzahlVerkaufteArtikel = 0
i = 0
n = len(data)

# Rabatt
while i < n:
    data[i] = list(data[i])
    data[i].insert(4, '')

    row = data[i]

    # Rabattberechnung data[i - 1][4] = row[3] wenn der Rabatt als Preis angegeben werden soll
    if "%" in row[2]:
        data[i - 1][4] = str(round(row[3] / data[i - 1][3] / data[i - 1][1] * 100)) + '%'
        del data[i]
    else:
        i = i + 1
        AnzahlVerkaufteArtikel = AnzahlVerkaufteArtikel + 1

    n = len(data)
    Umsatz = Umsatz + row[3]

print("Umsatz: " + str(round(Umsatz, 2)))
print("AnzahlVerkaufteArtikel: " + str(AnzahlVerkaufteArtikel))

# SQL: Datum
Datum = "Fehler"
Datum = cursor.execute('SELECT CAST(GETDATE() AS Date)').fetchone()[0]
print("Datum: " + str(Datum))

# SQL: AnzahlVerkäufe
AnzahlVerkaeufe = "Fehler"
AnzahlVerkaeufe = cursor.execute('SELECT COUNT(DISTINCT b.cInetBestellNr) '
                                 'FROM [eazybusiness].[dbo].[tBestellung] AS b '
                                 'INNER JOIN [eazybusiness].[dbo].[tPlattform] AS p '
                                 'ON b.nPlatform = p.nPlattform '
                                 'Where p.nPlattform = 7 '
                                 'AND b.dErstellt >= cast (GETDATE() as DATE) '
                                 ).fetchone()[0]

print("AnzahlVerkaeufe: " + str(AnzahlVerkaeufe))


# PDF
class PDF(FPDF):
    # Page Header
    def header(self):
        self.set_font("Helvetica", size=18)
        self.cell(185, 25, txt=Titel, border=0, align="C")
        self.ln(20)
        self.set_font("Helvetica", size=10)
        self.cell(10, 20, txt="", border=0, align="L")
        self.cell(130, 20, txt="Umsatz:" + str(round(Umsatz, 2)), border=0, align="L")
        self.cell(60, 20, txt="Datum:" + str(Datum), border=0, align="L")
        self.ln(10)
        self.cell(10, 20, txt="", border=0, align="L")
        self.cell(130, 20, txt="Anzahl der verkauften Artikel:" + str(AnzahlVerkaufteArtikel), border=0, align="L")
        self.cell(60, 20, txt="Anzahl der Verkäufe:" + str(AnzahlVerkaeufe), border=0, align="L")
        self.ln(18)

        self.cell(Bonnummer_width, header_row_height, txt="Bonnummer", border=border, align="C")
        self.cell(Anzahl_width, header_row_height, txt="Menge", border=border, align="C")
        self.cell(Artikelname_width, header_row_height, txt="Artikelname", border=border, align="L")
        self.cell(Preis_width, header_row_height, txt="Preis", border=border, align="C")
        self.cell(Rabatt_width, header_row_height, txt="Rabatt", border=border, align="C")
        self.cell(Uhrzeit_width, header_row_height, txt="Uhrzeit", border=border, align="C")
        self.ln(header_row_height)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, 'Seite ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()

# PDF Body
pdf.set_font("Helvetica", size=10)
row_height = pdf.font_size
spacing = 2.1

for row in data:

    col_width = Bonnummer_width
    align = "C"
    pdf.set_fill_color(255)

    for item in row:
        if 0 > row[1]:
            pdf.set_fill_color(220)
        pdf.cell(col_width, row_height * spacing, txt=str(item), border=border, align=align, fill=1)
        if col_width == Bonnummer_width:
            col_width = Anzahl_width
            align = "C"
        elif col_width == Anzahl_width:
            col_width = Artikelname_width
            align = "L"
        elif col_width == Artikelname_width:
            col_width = Preis_width
            align = "R"
        elif col_width == Preis_width:
            col_width = Rabatt_width
            align = "R"
        elif col_width == Rabatt_width:
            col_width = Uhrzeit_width
            align = "R"

    pdf.ln(row_height * spacing)

# Output des PDFs
filename = 'Kassenbericht_' + Kassenname + '-' + str(Datum) + '.pdf'
pdf.output(str(path + filename), 'F')

# Mail
subject = 'Kassenbericht_' + Kassenname + '-' + str(Datum)
body = "Dies ist der automatisch generierte Kassenbericht der Kasse " + Kassenname + "vom " + str(Datum)

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

# Open PDF file in binary mode
with open(path + filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(mail_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

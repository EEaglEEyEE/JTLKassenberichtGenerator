# JTLKassenberichtGenerator
Python Skript, dass einen Kassenbericht von JTL-Pos aus der Datenbank erstellt<br>
<br>
Dieses Script ist zum automatischen Erstellen von Kassenberichten der Software von JTL. Dieser wird auch anschließend gleich per Mail versendet.<br>
In der eigenen Kassenlösung (JTL-POS) von JTL besteht leider keine Möglichkeit einen Kassenbericht zu erstellen, aufgrund dessen habe ich ein kleines Skript geschrieben, welches diesen Job übernimmt.<br>
Das Skript ist für JTL-POS Kassen optimiert funktioniert aber auch mit LS-POS.<br>
<br>
Zum ausführen der Skripts wird <a href="https://www.python.org/">Python</a> und der <a href="https://www.microsoft.com/de-de/download/details.aspx?id=56567">ODBC Treiber</a>  benötigt. Anschließend kann das Skript einfach täglich vom Windows <a href="https://praxistipps.chip.de/aufgabenplanung-in-windows-10-so-gehts_48391">Aufgabenplaner</a> (oder ähnliches) aufgerufen werden.<br>
Nach der Installation müssen noch die notwendigen Libs installiert werden: <i>pip install fpdf</i> und <i>pip install pyodbc</i><br>
Command zum ausführen: <i>#pathtopython#\python.exe JTLKassenberichtGenerator.py</i><br>
<br>
Das Script muss noch auf die individuellen Einstellungen angepasst werden. Diese Anpassungen sind in den Programmkommentaren beschrieben.<br>
Obligatorische Anpassungen:<br>
Line 39-41 - PDF Tabellenanpassung<br>
Line 43-48 - Mail Einstellungen<br>
Line 50-55 - Datenbankeinstellungen<br>
Line 72/121 - Plattform-ID/Kassen-ID auswählen (Die Kassen-ID bei JTL-POS fängt bei 7 an und wird fortgeführt (7, 8, 9,...) bei LS-POS fängt es bei 151 an und wird auch einfach fortgeführt (152,153,...))<br>
<br>
Optionale Anpassungen:<br>
Line 28-37 - PDF Tabellenanpassung<br>
<br>
<br>
WTFPL License 
<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png"
       width="88" height="31" alt="WTFPL" /></a>

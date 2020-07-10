# JTLKassenberichtGenerator
Python Skript, dass einen Kassenbericht von JTL-Pos aus der Datenbank erstellt<br>
<br>
Dieses Script ist zum automatischen Erstellen von Kassenberichten der Software von JTL. Dieser wird auch anschließend gleich per Mail versendet.<br>
In der eigenen Kassenlösung (JTL-POS) von JTL besteht leider keine Möglichkeit einen Kassenbericht zu erstellen, aufgrund dessen habe ich ein kleines Skript geschrieben, welches diesen Job übernimmt.<br>
<br>
Das Script muss noch auf die individuellen Einstellungen angepasst werden. Diese Anpassungen sind in den Programmkommentaren beschrieben.<br>
Obligatorische <tab id=t1>Anpassungen:<br>
Line 30 - SQL Server, Port und Instanz<br>
Line 31 - Datenbankname<br>
Line 32 - SQL User<br>
Line 33 - SQL Password<br>
Line 191 - Speicherpfad <br>
Line 192 - Kassenname<br>
Line 199 - Absender E-Mail<br>
Line 200 - Empfänger E-Mail<br>
Line 201 - Absender Passwort<br>
Line 202 - Mail Server<br>
Line 203 - Port<br>
<br>
Optionale Anpassungen:<br>
Line 50/99 - Kassen-ID eintagen<br>
Line 51/100 - Kassenbericht Datum<br>
Line 107-116 - Tabellenanpassung<br>
Line 192 - Kassenname<br>
<br>
<br>
WTFPL License 
<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png"
       width="88" height="31" alt="WTFPL" /></a>

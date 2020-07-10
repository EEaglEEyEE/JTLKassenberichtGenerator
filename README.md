# JTLKassenberichtGenerator
Python Skript, dass einen Kassenbericht von JTL-Pos aus der Datenbank erstellt

Dieses Script ist zum automatischen Erstellen von Kassenberichten der Software von JTL. Dieser wird auch anschließend gleich per Mail versendet
In der eigenen Kassenlösung (JTL-POS) von JTL besteht leider keine Möglichkeit einen Kassenbericht zu erstellen, aufgrund dessen habe ich ein kleines Skript geschrieben, welches diesen Job übernimmt.

Das Script muss noch auf die individuellen Einstellungen angepasst werden. Diese Anpassungen sind in den Programmkommentaren beschrieben.
Obligatorische Anpassungen:
Line 30       SQL Server, Port und Instanz
Line 31       Datenbankname
Line 32       SQL User
Line 33       SQL Password
Line 191      Speicherpfad 
Line 192      Kassenname
Line 199      Absender E-Mail
Line 200      Empfänger E-Mail
Line 201      Absender Passwort
Line 202      Mail Server
Line 203      Port

Optionale Anpassungen:
Line 50/99           Kassen-ID eintagen
Line 51/100          Kassenbericht Datum
Line 107-116         Tabellenanpassung
Line 192             Kassenname


WTFPL License 
<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png"
       width="88" height="31" alt="WTFPL" /></a>

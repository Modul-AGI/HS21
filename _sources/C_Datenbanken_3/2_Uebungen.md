# Übungen 

## 2. Datenbankverbindung zum Server aufbauen 

In den nächsten Übungen wollen wir mit Daten unserer Pflanzendatenbank aus der ersten Datenbank‐Lektion
vor 2 Wochen umgehen. Dazu versuchen Sie die Daten aus den einzelnen Tabellen zu verknüpfen und sinnvoll
aufzubereiten, um Sie anschliessend im ArcGIS Pro einzubinden und zu visualisieren. Unsere
Pflanzendatenbank hat hierbei immer den Namen «modulagi_pdb_hs21». Verwenden Sie, wenn nicht anders
angegeben diese Datenbank.
OPTIONAL: Es ist Ihnen selbst überlassen, ob Sie in den kommenden Übungen die bestehende Server
Datenbank nutzen möchten oder Ihre eigene lokale Pflanzendatenbank. Die Übungen beziehen sich auf die
Server Variante. Bei eigener Datenbank passen Sie die Datanbank Verbindungsparameter entsprechend an.
Wie Sie Ihre eigene lokale Pflanzendatenbank aufsetzen ist in den Vorbereitungsübungen auf Moodle
beschrieben.

https://moodle.zhaw.ch/pluginfile.php/206729/mod_resource/content/13/%C3%9Cbung_Datenbanken3_Vorbereitung_HS21.pdf  


### Übung 1: (Wiederholung) Datenbankverbindung zum Server in pgAdmin herstellen

In den folgenden Übungen wollen wir mit einer Datenbank auf einem ZHAW‐Server arbeiten. Hierzu erstellen
wir zunächst eine Verbindung zu dieser Datenbank über pgAdmin. ACHTUNG: funktioniert nur im ZHAW Netz
(VPN).
1. Starten Sie pgAdmin.
2. Im Dashboard klicken Sie auf NEW Server und geben die folgenden Verbindungsparameter ein:
3. Register General: Name: svma‐s‐01323_modulagi_pdb_hs21_studentNr. Verwenden Sie dabei die Nr.
Ihres zugewiesenen Benutzers.
4. Register Connection:
    - Host name/address: svma‐s‐01323.zhaw.ch
    - Port: 5432
    - Maintenance database: modulagi_pdb_hs21
    - studentNr (Verwenden Sie hier Ihren zugewiesenen Anmeldenamen)
    - Passwort: (Verwenden Sie hier Ihr zugewiesenes Passwort)

    ![grafik](https://user-images.githubusercontent.com/49159820/139634939-ec46e7d4-6980-49ca-a3a1-2247b0fd380a.png)

5. Alle anderen Einstellungen können belassen werden. Speichern Sie mit Klick auf Save.
6. Lassen Sie sich nicht davon verunsichern, dass es bereits einige Einträge hat. Da auf dem Server bereits andere Datenbanken installiert sind, sehen Sie auch diese. Navigieren Sie zur Datenbank «modulagi_pdb_hs21» und verschaffen sich einen Überblick über die vorhandenen Tabellen usw..
7. Verwenden Sie für alle folgenden Übungen diese Datenbankverbindung, wenn nichts anderes angegeben.


### Übung 2: (Wiederholung) Datenbankverbindung zum Server in ArcGIS Pro herstellen

In den folgenden Übungen wollen wir mit einer Datenbank auf einem ZHAW-Server arbeiten. Hierzu erstellen wir zunächst eine Verbindung zu dieser Datenbank über ArcGIS Pro. 

1.	Starten Sie ArcGIS Pro und erstellen Sie ein neues Projekt «Pflanzendatenbank_III».
2.	Sie können alle folgenden Übungen in diesem Projekt durchführen.
3.	Navigieren Sie im Catalog Fenster zum Eintrag Databases. Über das Kontextmenü (Rechtsklick) können Sie eine neue Datenbankverbindung herstellen.
4.	Verwenden Sie folgende Parameter:
      -	Database Platform: PostgreSQL
      -	Instance: svma-s-01323.zhaw.ch
      -	Authentication Type: Database authentication
      -	User Name: studentNr (Verwenden Sie Ihren zugewiesenen Benutzer)
      -	Password: (Verwenden Sie ihr zugewiesenes Passwort)
      -	Database: modulagi_pdb_hs21 (Achtung, auch hier sehen sie eine Reihe von anderen Datenbanken, Achten Sie darauf die korrekte Datenbank zu wählen)

    ![grafik](https://user-images.githubusercontent.com/49159820/139635144-03733a6c-097c-4b1e-a019-1c6c3e709098.png)
 
5.	Speichern Sie die Einstellungen mit Klick auf OK und geben der neuen Datenbankverbindung einen sinnvollen Namen.
6.	Verwenden Sie für alle folgenden Übungen diese Datenbankverbindung, wenn nichts anderes angegeben.



## 3.	Abfragen aus der Datenbank in ArcGIS Pro einbinden

In den nächsten Übungen wollen wir mit den Daten in unserer Beispiel-Datenbank umgehen. Dazu versuchen wir die Daten aus den einzelnen Tabellen zu verknüpfen und sinnvoll aufzubereiten, um Sie anschliessend im ArcGIS Pro einzubinden und zu visualisieren. Unsere Pflanzendatenbank hat hierbei immer den Namen «modulagi_pdb_hs20». Verwenden Sie, wenn nicht anders angegeben diese Datenbank. Erstellen Sie zunächst noch einen beliebigen Ordner auf Ihrem Rechner in welchem wir die jeweiligen Ergebnisse speichern können. Sie finden ein Datenbankschema der Pflanzendatenbank auf dem Moodle. Dies hilft Ihnen beim Verständnis der Datenbank und seinen Beziehungen. Nutzen Sie auch die PostGIS Referenz, um die PostGIS Funktionen zu verstehen.

	Datenbankschema: https://moodle.zhaw.ch/mod/resource/view.php?id=159530 
	PostGIS Referenz: https://postgis.net/docs/manual-3.0/reference.html 
  
Wenn Sie sich bei den SQL-Befehlen nicht ganz sicher sind, so versuchen Sie schrittweise zum Ziel zu kommen. Formulieren Sie zunächst einen einfacheren Teil der Abfrage, z.B. nur Attribute aus einer Tabelle und fügen Sie dann die weiteren Attribute und/oder Tabellen schrittweise hinzu. Probieren Sie bei Bedarf nach jedem Zwischenschritt die Abfrage aus und schauen sich die Ergebnisse an.

   ![grafik](https://user-images.githubusercontent.com/49159820/139635281-6de05977-fd4c-4047-9b41-f8cd9edbe273.png)
    
Datenbankschema: Pflanzendatenbank (die gelben Schlüssel sind Primärschlüssel, die blauen Pfeile sind Fremdschlüssel).


### Übung 3: Werkzeug «Make Query Table» anwenden

Das Werkzeug erstellt aus einer beliebigen Datenbankabfrage eine von ArcGIS Pro lesbare temporäre Tabelle. Dies ist immer dann sinnvoll, wenn z.B. nur eine Teilmenge aller Objekte gebraucht wird. Diese Teilmenge wird dabei in eine neue Tabelle geschrieben. HINWEIS: Die Tabelle wird nur temporär in dem Projekt abgelegt, d.h. es wird keine konkrete Datei geschrieben und auch keine neue Tabelle in der Datenbank erstellt, sondern nur die Abfrage im Projekt gespeichert. 

1.	Starten Sie pgAdmin und verbinden Sie mit der Pflanzendatenbank «modulagi_pdb_hs21» mit Ihrem Benutzer studentNr.
2.	Probieren Sie folgende SQL-Abfrage zu formulieren.
3.	Suchen Sie alle Gattungen der Familie «Asteraceae». Zeigen Sie den Namen der Familie und den Namen der Gattung an.

    ![grafik](https://user-images.githubusercontent.com/49159820/139636566-b10a790a-cfcd-4ba8-a776-20eccba9c0c0.png)
 
4.	Starten Sie ArcGIS Pro und öffnen das Projekt «Pflanzendatenbank».
5.	Erstellen Sie eine neue Karte.
6.	Öffnen Sie das Werkzeug «Make Query Table»
7.	Wählen Sie die beteiligten Tabellen familien und gattungen (über die Datenbankverbindung)
8.	Wählen Sie die anzuzeigenden Felder name_familie und name_gattung
9.	Filtern Sie die Abfrage über die SQL-Expression nach ‘Asteraceae’. HINWEIS: Sie brauchen im Werkzeug nur den WHERE Teil der Abfrage ohne das Schlüsselwort WHERE eingeben. Achten Sie auch auf die verknüpften Schlüssel (id_familie) in beiden Tabellen. Sie können den WHERE Teil natürlich aus pgAdmin kopieren. Achten Sie in dem Fall darauf im Werkzeug auf die SQL-Ansicht umzustellen.
10.	Geben Sie der neuen Tabelle einen Namen.
11.	Prüfen Sie die Inhalte der neuen Tabelle. Vergleichen Sie mit dem Ergebnis aus pgAdmin.
12.	HINWEIS: «Make Query Table» erlaubt nur NICHT-räumliche Abfragen. Es können zwar Felder aus räumlichen Tabellen abgefragt werden, das Ergebnis ist aber immer eine einfache Tabelle und keine Feature Class.


### Übung 4: Werkzeug «Make Query Layer» anwenden

Das Werkzeug erstellt aus einer beliebigen Datenbankabfrage eine von ArcGIS Pro lesbare temporäre Feature Class. HINWEIS: Die Feature Class wird nur temporär in dem Projekt abgelegt, d.h. es wird keine konkrete Datei geschrieben und auch keine neue Tabelle in der Datenbank erstellt, sondern nur die Abfrage im Projekt gespeichert.

1.	Probieren Sie folgende SQL-Abfrage in pgAdmin zu formulieren.
2.	Suchen Sie den Standort aller Eichen (Gattung = Quercus). Zeigen Sie Gattung, Art und den Standort mit der objectid (Attribut shape + objectid).

    ![grafik](https://user-images.githubusercontent.com/49159820/139636807-09e7885d-4be3-409e-b373-fc66d858d3c4.png)

3.	Wechseln Sie zu ArcGIS Pro.
4.	Öffnen Sie das Werkzeug «Make Query Layer».
5.	Schreiben Sie das SQL-Query. TIPP: Sie können die Abfrage aus pgAdmin (Schritt 3) kopieren und hier wieder einfügen. Klicken Sie danach auf eine leere graue Fläche irgendwo im Werkzeug-Fenster damit das Kopierte angenommen wird.
6.	Die folgenden Einstellungen sollten dadurch dann automatisch gefunden werden.
7.	Achten Sie auf den korrekten Geometrietyp (Shape Type) und das Koordinatensystem, die SRID Nummer für das Schweizer Koordinatensystem CH1903+_LV95 lautet 2056.
8.	HINWEIS: Eine Abfrage mit dem Werkzeug «Make Query Layer» benötigt immer ein eindeutiges Identifizierungsfeld (Unique identifier Field(s)). In diesem Fall nutzen wir das Attribut «objectid». Achten Sie auch in den kommenden Abfragen auf ein solches ID-Feld.
9.	Schauen Sie sich den neuen Layer in der Karte an und werfen Sie auch einen Blick auf die Attributtabelle.
10.	Vergleichen Sie wieder mit dem Ergebnis aus pgAdmin.
11.	TIPP: Über das Kontextmenü des neuen Layers im Contents Fenster (Data -> Export Features) können Sie den Layer auch dauerhaft z.B. als neue Feature Class in eine eigene Datenbank oder als neues Shapefile speichern.


### Übung 5: Werkzeug «Create Database View» anwenden

«Create Database View» kann dazu benutzt werden, eine Sicht auf eine Tabelle zu erzeugen bzw. eine Abfrage in der Datenbank zu speichern. Hierbei wird dann nur eine Auswahl von Attributspalten und/oder Objekten zurückgegeben. Eine Sicht ist oft auch nützlich, um komplizierte Abfragen aus mehreren Tabellen in eine Tabelle «zusammen zu fassen», um dann einfacher darauf zugreifen zu können. HINWEIS: Die Sicht wird bei diesem Werkzeug, anders als in den beiden vorigen Werkzeugen, in der Datenbank gespeichert. D.h. es wird eine neue Tabelle bzw. View in der Datenbank erstellt.

1.	Probieren Sie folgende SQL-Abfrage in pgAdmin zu formulieren.
2.	Machen Sie eine Liste mit allen Pflanzen des Kurses «UÖ Stauden Gärtnerisch». Die Liste soll dabei die ID der Spezies, die Gattung, Art und Sorte der Pflanze sowie den Namen des Kurses und den Standort (Attribut shape) enthalten. Speichern Sie diese Abfrage als View mit dem Namen «pdb.view_kursliste_stauden_gaertnerisch_studentNr» in der Datenbank. (CREATE VIEW … AS SELECT…). 
3.	HINWEIS: Mit zwei Minus Zeichen vor einer Zeile können Sie die Zeile auskommentieren.

    ![grafik](https://user-images.githubusercontent.com/49159820/139637024-732ba6d3-380b-49c2-a1dc-1eb7a8ea5476.png)

4.	Wechseln Sie zu ArcGIS Pro.
5.	Erneuern Sie die Datenbankverbindung (Refresh / F5), damit die neue View sichtbar ist.
6.	Eine View verhält sich wie eine neue Tabelle in ArcGIS Pro. Aus diesem Grund müsste die Tabelle eigentlich mit der Datenbank registriert werden. Sie erkennen dies auch in der Catalog Ansicht an dem nicht ausgefüllten Rechteck.

    ![grafik](https://user-images.githubusercontent.com/49159820/139637061-38fb81b6-7bba-4356-a09f-6618ecf271a1.png)

7.	Eine Registrierung bewirkt das Freischalten der Geodatenbank-Funktionen für diese Tabelle, damit auch neue Daten erfasst und bearbeitet werden können. Da Ihr Benutzer studentNr keine Berechtigungen zum Schreiben im Datenbankschema auf der Datenbank hat, kann die Tabelle jetzt nicht registriert werden. Da wir aber die Tabelle nur abfragen wollen ist dies nicht weiter schlimm.
8.	Öffnen Sie das Werkzeug «Create Database View».
9.	Speichern Sie mit dem Werkzeug eine identische Liste für den Kurs «UÖ Gehölze». Geben Sie der View den Namen «pdb.view_kursliste_gehoelze_studentNr». Sie können hierzu wieder das SQL-Select-Statement von oben kopieren (ohne den CREATE VIEW Teil) und den Kursnamen entsprechend anpassen.
10.	Schauen Sie sich das Ergebnis in der Attributtabelle und in der Karte an.
11.	Sie sehen an dieser Übung, dass nur der Datenbankbesitzer neue Tabellen erstellen und hinzufügen kann. Andere Benutzer wie der student1 können nur vorhandene Tabellen und Daten bearbeiten und ändern. Neue Tabellen können nur ohne Schreibberechtigung erstellt werden.


### Übung 6: (optional) Werkzeug «Make Table View»
«Make Table View» kann dazu benutzt werden, um eine reduzierte Sicht auf eine Tabelle zu erzeugen. Hierbei wird dann nur eine Auswahl von Attributspalten (ohne Geometrie-Attribut) angezeigt. HINWEIS: Die Sicht wird nur temporär in dem Projekt abgelegt, d.h. es wird keine konkrete Datei geschrieben und auch keine neue Tabelle in der Datenbank erstellt, sondern nur die Abfrage im Projekt gespeichert.

1.	Starten Sie ArcGIS Pro und laden das Projekt mit dem Namen «Pflanzendatenbank»
2.	Öffnen Sie das Werkzeug «Make Table View».
3.	Erstellen Sie eine Abfrage wie in Übung 5 und filtern nach der Art «japonicum». 
4.	Wählen Sie als Input Table die zuvor erstellte View, lassen Sie aber das Geometriefeld (shape) in der Abfrage weg und filtern über eine «new Expression» nach name_art = «japonicum».
5.	Lassen Sie sich die Attributtabelle der neuen Tabelle anzeigen.



## 4.	Geoverarbeitung in der Datenbank mit ArcGIS Pro und SQL

In diesem Kapitel sollen konkrete Geoverarbeitungsoperationen in ArcGIS Pro und PostGIS/SQL gegenübergestellt werden. Dafür bearbeiten wir die entsprechende Fragestellung zunächst in ArcGIS Pro und stellen anschliessend die gleiche Funktion in PostGIS nach. Zur Visualisierung des Ergebnisses der SQL-Abfrage nutzen wir das Werkzeug «Make Query Layer» in ArcGIS Pro aus Übung 4.


### Übung 7: Geometrien zusammenführen mit «Dissolve»

Die importierten Flächen sind alle einem bestimmten Bereich zugeordnet. Um einen Überblick über die Grösse und Ausdehnung der Bereiche zu bekommen, möchten wir alle Flächen (Tabelle pdb.flaechen_shp) mit identischem Bereich (Attribut «name_bereich») zusammenführen.

1.	Führen Sie die Geometrien mit identischem Bereichsnamen (Attribut «name_bereich») zusammen. Verwenden Sie wieder die Verbindung mit dem Benutzer studentNr.
    - Verwenden Sie das Werkzeug «Dissolve» in ArcGIS Pro. Nutzen Sie dabei Multipart Features. Speichern Sie das Ergebnis als neuen Layer. HINWEIS: Da Ihr Datenbankbenutzer studentNr keine Berechtigungen zum Speichern in der Server Datenbank hat, können Sie das Ergebnis lokal auf Ihrem Rechner in Ihrem Ordner oder einer eigenen Geodatenbank ablegen.
    - Formulieren Sie jetzt die SQL Anfrage in pgAdmin (Verbindung wieder mit Benutzer studentNr). Verwenden Sie dabei die Funktion ST_UNION. Um nur gewünschte Flächen zu erhalten, sollten Sie das Ergebnis im SQL-Befehl nach dem Namen des Bereichs gruppieren (GROUP BY).
    - Optional: Was passiert wenn das GROUP BY weggelassen würde? Probieren Sie es aus.
    - Lassen Sie das Attribute name_bereich für die Flächen anzeigen.
    - Zeigen Sie das Ergebnis mit «Make Query Layer» an und vergleichen mit dem ArcGIS Pro Resultat.

    ![grafik](https://user-images.githubusercontent.com/49159820/139637478-ec631b2c-dbac-4ab9-8bb1-b9fafd8c861c.png)


### Übung 8: Puffer um Geometrie erstellen

Auf dem Campus sollen die Wege im Päoniengarten auf jeder Seite um 25cm verbreitert werden. Um die neuen Wege darzustellen, erstellen wir einen Puffer. Die Wegflächen finden Sie in der Datenbank in der Feature Class «wege_paeoniengarten».

1.	Legen Sie jeweils einen Puffer von beidseitig 25cm um das Wegenetz. 
    - Nutzen Sie dazu einmal das Werkzeug «Buffer» in ArcGIS Pro. Speichern Sie hierbei das Ergebnis. 
    - Nutzen Sie jetzt die POSTGIS Funktion ST_BUFFER in pgAdmin. Geben Sie auch die id der Flächen mit aus. HINWEIS: Achten Sie auf die Einheiten. Welche Einheit nimmt ST_BUFFER? Fragen Sie die Online-Hilfe.
2.	Skizzieren Sie ihr Vorgehen in ArcGIS Pro und notieren ihren SQL-Befehl. 
3.	Um das Ergebnis der PostGIS Funktion zu visualisieren, nutzen Sie das Werkzeug «Make Query Layer» mit Ihrer SQL Abfrage.
4.	Vergleichen Sie die Ergebnisse. Schauen Sie sich auch die Attribute an. Was fällt auf?

    ![grafik](https://user-images.githubusercontent.com/49159820/139638264-4e6b6b85-191e-4cdf-9e59-7b230314aaba.png)


### Übung 9: Geometrien überschneiden mit «Intersect»

An einigen Stellen muss für die Verbreiterung des Weges die Fläche einiger Beete weichen. Ermitteln Sie die betroffenen Beete, welche Fläche für die neuen Wege abgeben müssen.

1.	Bilden Sie die Schnittmenge (Intersection) der gepufferten Wegfläche und der restlichen Flächen aus der Tabelle «pdb.flaechen».
    - In ArcGIS Pro verwenden Sie dazu das Werkzeug «Pairwise Intersect». Sie können als Input entweder Ihr Ergebnis aus der vorigen Übung benutzen oder Sie verwenden den Datensatz «wege_paeoniengarten_buffer» aus der Datenbank. Speichern Sie das Ergebnis.
    - Stellen Sie den SQL-Befehl mit Hilfe der Funktion «ST_INTERSECTION» für diese Abfrage in pgAdmin auf und visualisieren das Ergebnis wieder mit «Make Query Layer». Sie können als Input entweder den gespeicherten Puffer aus der vorigen Übung verwenden oder Sie verwenden den Datensatz «wege_paeoniengarten_buffer» aus der Datenbank. Probieren Sie ebenfalls einmal aus durch eine verschachtelte Abfrage den Puffer mit ST_BUFFER direkt einzubeziehen. Geben Sie in Ihrem SQL-Befehl auch die ID der Fläche mit aus.
2.	Skizzieren Sie ihr Vorgehen in ArcGIS Pro und notieren ihren SQL-Befehl.
3.	Vergleichen Sie die Ergebnisse aus ArcGIS Pro und SQL. HINWEIS: Die SQL Funktion ST_INTERSECTION erzeugt immer eine so genannte Geometry Collection, auch wenn zwei Geometrien keine Schnittmenge aufweisen, gibt es einen dann leeren Eintrag. Aus diesem Grund zeigt das Ergebnis immer alle Geometrien an. Haben die Geometrien keine Schnittmenge, so ist die Geometrie leer. Um leere Geometrien auszuschliessen, sollte im WHERE-Abschnitt z.B. mit der Funktion ST_OVERLAPS oder der Funktion ST_INTERSECTS geprüft werden, ob die zwei Eingabe-Geometrien (Gepufferte Wege und sonstige Flächen) überhaupt irgendwo überlappen. Im ArcGIS Pro werden leere Geometrien automatisch vom Ergebnis abgeschnitten.

    ![grafik](https://user-images.githubusercontent.com/49159820/139638392-bd89ae94-061d-4ee4-bc6f-17ed40674620.png)


### Übung 10: Flächen berechnen in ArcGIS Pro und SQL

In der Übung 10 wurden Flächen ausgeschieden, welche von den betroffenen Beeten abgegeben werden müssen. Die genauen Flächengrössen sollen jetzt berechnet werden.

1.	Welche Beete müssen wie viel Fläche abgeben? Berechnen Sie die Fläche pro Beet in qm.
    - Legen Sie dazu in ArcGIS Pro ein neues Feld in der Attributtabelle ihres gespeicherten Layers an und berechnen dort die jeweiligen Einzelflächen in qm (Calculate Geometry). Haben Sie das Ergebnis in einer Geodatenbank gespeichert gibt es bereits das Attribut shape_area mit der Fläche in qm.
    - Erstellen Sie in pgAdmin eine Abfrage in SQL, welche ebenfalls die jeweiligen Einzelflächen in qm ausgibt. Ergänzen Sie dazu die SQL-Abfrage aus Übung 9 mit einem neuen Feld, welches die Fläche ausgibt. Wenden Sie dazu die Funktion ST_AREA auf das Geometriefeld an.
    - Visualisieren Sie das Ergebnis erneut mit «Make Query Layer».

    ![grafik](https://user-images.githubusercontent.com/49159820/139638536-45da93b3-f2b3-43ae-847e-7df4c02b4efb.png)


### Übung 11: Geometrien ausschneiden mit «Erase»

Als nächstes wollen wir die grosse Hauptwege-Achse zu unseren Flächen hinzufügen. Hierzu haben wir eine weitere Feature Class in der Datenbank mit der Hauptwegeachse zur Verfügung. Leider enthält die Feature Class nur die Aussengrenzen des Weges. Da es auf dem Weg auch Beete gibt, wollen wir diese Beetflächen aus der Wegfläche ausschneiden.

1.	Schneiden Sie die Beetflächen aus der Wegeachse aus. Nutzen Sie dafür:
    - In ArcGIS Pro das Werkzeug «Erase» und speichern das Ergebnis als neue Feature Class oder als Shapefile in Ihrem Ordner.
    - Formulieren Sie in pgAdmin den SQL-Befehl mit der Funktion ST_DIFFERENCE und zeigen Sie das Resultat mit «Make Query Layer» auf der Karte. Geben Sie dabei zusätzlich die id der Fläche sowie die Attribute name_standort und name_bereich mit aus.
    - HINWEIS: Diese Anfrage funktioniert in zwei Schritten mit einer verschachtelten Abfrage (aber trotzdem in einem SQL-Befehl). Um Polygone auszuschneiden, müssen wir zunächst alle Wegeflächen und alle sonstigen Flächen aus der Tabelle «flaechen_shp» zu jeweils einem Polygon zusammenfügen (ST_Union), damit wir nur noch zwei Flächen miteinander vergleichen müssen. Anschliessend werden die beiden Flächen dann mit dem Werkzeug ST_Difference untersucht.
    - HINWEIS: Die Funktion ST_Difference berechnet für jedes eingeschlossene Polygon einmal die Differenzmenge aus der Wegefläche und allen eingeschlossenen Polygonen. Dadurch hat das Ergebnis eigentlich zu viele Einträge, für jedes eingeschlossene Polygon ein Eintrag, welche aber alle dieselbe Geometrie aufweisen. Der Parameter LIMIT 1 limitiert die Ausgabe auf ein Feature.
2.	Vergleichen Sie die Ergebnisse.

    ![grafik](https://user-images.githubusercontent.com/49159820/139638703-5f93166b-3da1-47ca-9d2c-0d7303e63f7e.png)


### Übung 12: Geometrien ausschneiden mit «Clip»

Als nächstes möchten wir alle Pflanzen suchen, welche auf bereits kartierten Flächen stehen. Hierzu nehmen wir den Punktdatensatz der Pflanzen und verschneiden diesen mit den bereits vorhandenen Beet-Flächen.

1.	Suchen Sie alle Standorte (Punkte) der Pflanzen, welche auf kartierten Flächen stehen.
    - In ArcGIS Pro verwenden Sie das Werkzeug «Clip» und schneiden damit überflüssige Punkte weg. Speichern Sie das Resultat in Ihrem Ordner. Alternativ würde auch ein «Select by Location» gehen.
    - Formulieren Sie auch hierzu die SQL-Anfrage in pgAdmin, welche alle Punkte auf den Flächen zurückgibt. Sie können dazu wieder die Funktion ST_INTERSECTION nutzen. Achten Sie darauf, dass wir dabei wieder nur diejenigen Punkte haben wollen, welche auch wirklich in Beziehung zu den Flächen stehen. Diesen Filter müssen Sie im WHERE-Abschnitt bereitstellen. Verwenden Sie dafür diesmal die Funktion ST_INTERSECTS. Binden Sie ausserdem noch die Attribute id_pflanze (objectid) und id_spezies in die Ausgabe ein und sortieren die Liste danach anhand der id_pflanze.

    ![grafik](https://user-images.githubusercontent.com/49159820/139638838-e1f62225-cf01-4de9-9963-5469ab1c6bc1.png)

# REST-API Gestaltungsrichtlinien

## Inhaltsverzeichnis
- [Versionierung](#versionierung)
- [Namenskonventionen](#namenskonventionen)
- [Korrekter Einsatz der HTTP-Methoden](#korrekter-einsatz-der-http-methoden)

## Versionierung
Die Versionierung Ihrer API hilft bei der Handhabung von Änderungen und der Sicherstellung der Rückwärtskompatibilität.

### Ansätze zur Versionierung:
- **URI Path Versioning:** Die Version wird im URI-Pfad angegeben, z.B. `/api/v1/resource`.
- **Query String Versioning:** Die Version wird als Abfrageparameter übergeben, z.B. `/api/resource?version=1`.
- **Header Versioning:** Die Version wird in den HTTP-Headern festgelegt, häufig durch benutzerdefinierte oder Akzept-Header.

## Namenskonventionen
Eine klare und konsistente Benennung erleichtert das Verständnis und die Navigation Ihrer API.

### Richtlinien:
- **Plural vs. Singular:** Verwenden Sie Plural für Kollektionen (z.B. `/users`) und Singular für individuelle Instanzen (z.B. `/user/123`).
- **Konsistenz:** Bleiben Sie konsistent in Ihrer Verwendung von Singular oder Plural über die gesamte API hinweg.
- **Keine Verben:** Nutzen Sie Substantive für Ressourcen und vermeiden Sie Verben, da Aktionen durch HTTP-Methoden repräsentiert werden.

## Korrekter Einsatz der HTTP-Methoden
Verwenden Sie HTTP-Methoden entsprechend ihrer definierten Semantik.

### Methoden und ihre Verwendung:
- **GET:** Abrufen von Ressourcen ohne Seiteneffekte.
- **POST:** Erstellen einer neuen Ressource.
- **PUT:** Vollständiges Ersetzen einer vorhandenen Ressource.
- **PATCH:** Partielles Aktualisieren einer Ressource.
- **DELETE:** Entfernen einer Ressource.

Die korrekte Verwendung dieser Methoden sorgt für Klarheit und Vorhersehbarkeit in der API.



# Best Practices zur Gestaltung von REST-APIs

Um einen Überblick über Best Practices zur Gestaltung von REST-APIs zu geben, nutzen wir die zuvor zitierten Quellen:

## Ressourcenorientiertes Design
REST-APIs sind um Ressourcen herum entworfen, die jede Art von Objekt, Daten oder Dienst sein können, auf die der Client zugreifen kann. Jede Ressource hat einen eindeutigen Identifikator, meist eine URI.

## Verwendung von JSON
JSON (JavaScript Object Notation) ist weitgehend das bevorzugte Format für das Senden und Empfangen von API-Daten, da es leichter zu lesen und zu schreiben ist als XML und HTML.

## Konsistente Namensgebung
Ressourcen sollten im Plural benannt werden, um Kollektionen zu repräsentieren, und im Singular für individuelle Instanzen. Es ist ratsam, eine Konsistenz in der Pluralität über alle Ressourcen hinweg beizubehalten.

## Standard HTTP-Fehlercodes
Nutzen Sie standardisierte HTTP-Fehlercodes, um klar zu kommunizieren, was bei einer fehlerhaften Anfrage schiefgelaufen ist.

## Vermeidung von Verben in Endpunktnamen
Ressourcen sollten durch Substantive und nicht Verben dargestellt werden, um die Aktionen, die auf die Ressourcen angewendet werden können, deutlich von den Ressourcen selbst zu unterscheiden.

## Gruppierung von assoziierten Ressourcen
Verwandte Ressourcen sollten zusammen gruppiert werden, um das Verständnis und die Navigation der API zu erleichtern.

## Integration von Filterung, Sortierung und Pagination
Diese Funktionen sollten in die API integriert werden, um die Verwaltung großer Datenmengen zu erleichtern.

## Daten-Caching
Verwenden Sie Caching, um die Leistung der API zu verbessern und die Last auf dem Server zu verringern.

## Gute Sicherheitspraktiken
Sicherheit ist entscheidend, daher sollten APIs durch Authentifizierung, Autorisierung, Verschlüsselung und andere Sicherheitsmaßnahmen geschützt werden.

Indem Sie diese Best Practices befolgen, können Sie sicherstellen, dass Ihre REST-APIs effizient, sicher und benutzerfreundlich sind. Es ist auch wichtig, bei der Gestaltung von APIs agil zu bleiben und offen für Anpassungen basierend auf neuen Erkenntnissen und Feedback von API-Nutzern.

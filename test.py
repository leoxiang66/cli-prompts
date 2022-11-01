if __name__ == '__main__':
    from terminal import cli
    help = {
        'exit': 'Veranlasst die Termination der main-Methode.',
        'add <Titel>:<fliesstext des dokumentes>': '''Fügt der DocumentCollection ein neues Document mit dem Titel Titel und dem Fließtext fliesstext des dokumentes hinzu. Titel und Fließtext werden dabei durch einen Doppelpunkt (:) getrennt.''',
        'list': '''Listet die Titel aller mittels add hinzugefügten Dokumente auf.''',
        'count <word>': '''Listet für jedes Dokument auf, wie oft darin das Wort word vorkommt.''',
        'query <suchanfrage>': '''Führt die Suchanfrage suchanfrage auf den Documenten der DocumentCollection durch und gibt eine nummerierte Trefferliste der Documente aus'''
    }
    cli(help)
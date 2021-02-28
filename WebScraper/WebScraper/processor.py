from bs4 import BeautifulSoup


def tags_to_line(tags):
    line = ''
    for tag in tags:
        if tag.get_text() == '    ':
            continue
        else:
            line = line + tag.get_text() + ','
    return line


def process_data(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')
    start = False
    data = []
    for row in rows:
        tds = row.find_all('td')
        if not start:
            for td in tds:
                if td.get_text() == '1':
                    start = True
                    break
        if start:
            d = create_dictionary(tags_to_line(tds))
            if d:
                data.append(d)
    return data


def create_dictionary(line):
    splitted = line.replace(u'\xa0', u' ').split(',')
    cleared = list(filter(isEmptyString, splitted))
    if len(cleared) == 13:
        return {
            'Ranking': cleared[0],
            'Player': cleared[1],
            'Age': cleared[2],
            'Elo': cleared[3],
            'HardRaw': cleared[4],
            'ClayRaw': cleared[5],
            'GrassRaw': cleared[6],
            'hElo': cleared[7],
            'cElo': cleared[8],
            'gElo': cleared[9],
            'Peak Match': cleared[10],
            'Peak Age': cleared[11],
            'Peak Elo': cleared[12]
        }


def isEmptyString(s):
    if s is '':
        return False
    else:
        return True

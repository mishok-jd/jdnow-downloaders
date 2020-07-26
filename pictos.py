import webbrowser

print('JDNOW PICTOS DOWNLOADER BY MISHOK')

#codename
codename = input('Please enter a codename with a numerical sequence: ')

#jdnow links
pictos_png = 'http://jdnow-api-contentapistoragest.justdancenow.com/songs/' + codename + '/assets/web/pictos-atlas.png'
pictos_json = 'http://jdnow-api-contentapistoragest.justdancenow.com/songs/' + codename + '/assets/web/pictos-atlas.json'

#download links
if codename == '':
    print('ERROR: 1')
else :
    webbrowser.open(pictos_png)
    webbrowser.open(pictos_json)
    print('Finished!')

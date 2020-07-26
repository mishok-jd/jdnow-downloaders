import webbrowser

print('JDNOW PREVIEW DOWNLOADER BY MISHOK')

#codename
codename = input('Please enter a codename: ')
codename_number = input('Please enter a codename with a numerical sequence: ')

#jdnow links
ogg = 'http://jdnow-api-contentapistoragest.justdancenow.com/songs/' + codename_number + '/assets/web/' + codename + '.json'

#download links
if codename == '':
    print('ERROR: 1')
else :
    webbrowser.open(ogg)
    print('Finished!')

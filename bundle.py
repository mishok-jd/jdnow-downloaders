import webbrowser

print('JDNOW BUNDLE AND JSON DOWNLOADER BY MISHOK')

#codename
codename = input('Please enter a codename: ')
codename_number = input('Please enter a codename with a numerical sequence: ')

#jdnow links
bundle = 'http://jdnow-api-contentapistoragest.justdancenow.com/songs/' + codename_number + '/bundle.zip'
json = 'http://jdnow-api-contentapistoragest.justdancenow.com/songs/' + codename_number + '/' + codename + '.json'

#download links
if codename == '':
    print('ERROR: 1')
else :
    if codename_number == '':
        print('ERROR: 2')
    else :
        webbrowser.open(bundle)
        webbrowser.open(json)
        print('Finished!')

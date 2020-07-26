import webbrowser

print('JDNOW AVATAR DOWNLOADER BY MISHOK')

#codename
code = input('Please enter a code: ')

#jdnow links
avatar = 'http://jdnow-api-contentapistoragest.justdancenow.com/avatars/' + code + '.png'

#download links
if code == '':
    print('ERROR: 1')
else :
    webbrowser.open(avatar)
    print('Finished!')

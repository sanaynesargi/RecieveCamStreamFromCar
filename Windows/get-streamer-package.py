import requests

url = 'https://gstreamer.freedesktop.org/data/pkg/windows/1.14.4/gstreamer-1.0-devel-x86_64-1.14.4.msi'
url2  = 'https://gstreamer.freedesktop.org/data/pkg/windows/1.14.4/gstreamer-1.0-x86_64-1.14.4.msi'

print('\n\nInstalling dev package')
r = requests.get(url, allow_redirects=True)
open('gst-dev.msi', 'wb').write(r.content)

print('\n\nInstalling stream package')
r = requests.get(url2, allow_redirects=True)
open('gst-install.msi', 'wb').write(r.content)

print("\n\n You should see two .msi files, run both the installs, and click typical for the type of install!")
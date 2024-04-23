import os
import subprocess


def download_entire_site(url, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    command = [
        'wget',
        '--mirror',
        '--convert-links',
        '--adjust-extension',
        '--page-requisites',
        '--no-parent',
        '--directory-prefix', output_directory,
        url
    ]

    subprocess.call(command)


output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloaded_site')

site_url = 'Ссылка на сайт в формате https://www.google.com'

download_entire_site(site_url, output_path)

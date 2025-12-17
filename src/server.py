from wsgiref.simple_server import make_server

import falcon
import subprocess

class BeetImportResource:
    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        data = req.get_media()
        print(f"Received import request for directory: {data['LocalDirectoryName']}")
        try:
            print(f"beet import --quiet {data['LocalDirectoryName']}")
            subprocess.Popen(['beet', 'import', '--quiet', data['LocalDirectoryName']])
            resp.status = falcon.HTTP_200
            resp.media = {
                'message': 'Import triggered successfully.',
                'output': f"Beet import process triggered for directory: {data['LocalDirectoryName']}"
            }
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {
                'message': "Import failed for: {data['LocalDirectoryName']}",
                'error': e.stderr
            }

app = falcon.App()
app.add_route('/import', BeetImportResource())

if __name__ == '__main__':
    with make_server('', 8074, app) as httpd:
        print('Serving on port 8074...')

        # Serve until process is killed
        httpd.serve_forever()

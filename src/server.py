from wsgiref.simple_server import make_server

import falcon
import subprocess


class BeetImportResource:
    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        data = req.get_media()
        print(f"Received import request for directory: {data['localDirectoryName']}")
        try:
            print(f"beet import --quiet {data['localDirectoryName']}")
            process = subprocess.Popen(['beet', 'import', '--quiet', data['localDirectoryName']])
            resp.status = falcon.HTTP_200
            resp.media = {
                'message': 'Import triggered successfully.',
                'output': f"Beet import process triggered for directory: {data['localDirectoryName']}"
            }
            exit_code = process.wait()
            if exit_code != 0:
                print(f"Import process failed with exit code: {exit_code}")
            else:
                print("Import process completed successfully.")
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {
                'message': "Import failed for: {data['localDirectoryName']}",
                'error': e.stderr
            }

app = falcon.App()
app.add_route('/import', BeetImportResource())

if __name__ == '__main__':
    with make_server('', 8074, app) as httpd:
        print('Serving on port 8074...')

        # Serve until process is killed
        httpd.serve_forever()

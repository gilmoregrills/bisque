from wsgiref.simple_server import make_server

import falcon
import subprocess
import os
import signal
import time
import psutil


def wait_for_beet_processes(parent_pid: int, timeout: int = 3600) -> None:
    # Wait for all beet processes spawned by parent to complete.
    start_time = time.time()

    while time.time() - start_time < timeout:
        beet_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmdline = proc.info.get('cmdline')
                if cmdline and 'beet' in ' '.join(cmdline):
                    beet_processes.append(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        if not beet_processes:
            break

        time.sleep(0.5)

    if time.time() - start_time >= timeout:
        raise TimeoutError(f"Beet processes did not complete within {timeout} seconds")


class BeetImportResource:
    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        data = req.get_media()
        print(f"Received import request for directory: {data['localDirectoryName']}")
        try:
            print(f"beet import --quiet {data['localDirectoryName']}")
            result = subprocess.run(['beet', '-v', 'import', '--quiet', data['localDirectoryName']])
            print("Main beet process completed, waiting for background imports...")
            wait_for_beet_processes(result.pid)
            print("All import processes completed successfully.")
            resp.status = falcon.HTTP_200
            resp.media = {
                'message': 'Imported complete.',
                'output': f"Beet import process triggered for directory: {data['localDirectoryName']}"
            }
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {
                'message': "Import failed for: {data['localDirectoryName']}",
                'error': f"{e}"
            }

app = falcon.App()
app.add_route('/import', BeetImportResource())

if __name__ == '__main__':
    with make_server('', 8074, app) as httpd:
        print('Serving on port 8074...')

        # Serve until process is killed
        httpd.serve_forever()

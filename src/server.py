import subprocess
from wsgiref.simple_server import make_server

import falcon


class BeetImportResource:
    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        data = req.get_media()
        print(f"Received import request for directory: {data['localDirectoryName']}")
        try:
            print(
                f"beet -v --config=config/config.yaml import --quiet {data['localDirectoryName']}"
            )
            result = subprocess.Popen(
                [
                    "beet",
                    "-v",
                    "--config=config/config.yaml",
                    "import",
                    "--quiet",
                    data["localDirectoryName"],
                ]
            )
            resp.status = falcon.HTTP_200
            resp.media = {
                "message": "Import triggered.",
                "output": f"Beet import process triggered for directory: {data['localDirectoryName']}",
            }
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {
                "message": "Import failed for: {data['localDirectoryName']}",
                "error": f"{e}",
            }


app = falcon.App()
app.add_route("/import", BeetImportResource())

if __name__ == "__main__":
    with make_server("", 8074, app) as httpd:
        print("Serving on port 8074...")

        # mood
        httpd.serve_forever()

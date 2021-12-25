import requests
from pprint import pprint

class OdooConnection:

    def __init__(self, username="", password="", database="", server_url=""):
        self.username = username
        self.password = password
        self.database = database
        self.server_url = server_url

    def getSessionId(self):
        try:
            odoo_url = str(self.server_url) + "/web/session/authenticate"
            headers = {
                "Content-type": "application/json",
                "Accept": "application/json"
                }      
            data = {
                "jsonrpc": "2.0",
                "method": "call",
                "id": 1,
                "params": {
                    "login": self.username,
                    "password": self.password,
                    "db": self.database,
                    "context": {}
                }
            }
            req = requests.post(url=odoo_url, json=data, headers=headers)
            res_json = req.json()
            
            if "error" in res_json:
                # QMessageBox.warning(self,"Error Connection","Connection Error, please check your credentials.",QMessageBox.Ok)
                raise Exception("Connection error, please check your credentials.")
            
            if req.status_code == 200:
                return req.cookies["session_id"]
                # QMessageBox.information(self, "Connection", "------------ Connection Success ------------", QMessageBox.Ok)

        except Exception as e:
            # QMessageBox.warning(self, "Connection failed", str(e), QMessageBox.Ok)
            raise Exception(e)

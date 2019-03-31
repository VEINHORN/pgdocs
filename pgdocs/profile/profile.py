"""
Contains cods which is responsible for user profiles
"""
import os
import json


class Session:
    def __init__(self, host, port, db_name):
        self.host = host
        self.port = port
        self.db_name = db_name


class Profile:
    def __init__(self, sessions):
        self.sessions = sessions

    @classmethod
    def from_json(cls, json_obj):
        sessions = []

        if "sessions" in json_obj:
            for session in json_obj["sessions"]:
                sessions.append(
                    Session(session["host"], session["port"], session["db_name"]))
        return cls(sessions)

    def last_session(self):
        return self.sessions[-1] if self.sessions else None


def save(profile, home_dir=os.path.expanduser('~')):
    with open(config_file(home_dir), "w") as outfile:
        json.dump(profile.__dict__, outfile,
                  default=lambda x: x.__dict__, indent=4)


def read(home_dir=os.path.expanduser('~')):
    """Read user profile from .pgdocs config"""
    outfile = config_file(home_dir)
    if not os.path.exists(outfile):
        open(outfile, "w").close()
        return Profile([])  # return profile with empty sessions

    with open(config_file(home_dir), "r") as inpfile:
        # return empty profile if we cannot parse json
        try:
            return Profile.from_json(json.load(inpfile))
        except:
            return Profile([])


def config_file(home_dir):
    return os.path.join(home_dir, ".pgdocs")

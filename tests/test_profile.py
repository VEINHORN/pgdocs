import unittest
from pgdocs.profile import profile
import os


class TestProfile(unittest.TestCase):
    home_dir = "./"
    config_file = ".pgdocs"

    def sessions(self):
        return [profile.Session("localhost", 5432, "store_db"), profile.Session("192.168.1.2", 7777, "test_db")]

    def test_save(self):
        profile_out = profile.Profile(self.sessions())
        profile.save(profile_out, self.home_dir)

        profile_inp = profile.read(self.home_dir)

        self.assertEquals(profile_inp.sessions[0].host, "localhost")
        self.assertEquals(profile_inp.sessions[0].port, 5432)
        self.assertEquals(profile_inp.sessions[0].db_name, "store_db")

        self.assertEquals(profile_inp.sessions[1].host, "192.168.1.2")
        self.assertEquals(profile_inp.sessions[1].port, 7777)
        self.assertEquals(profile_inp.sessions[1].db_name, "test_db")

    def test_read(self):
        if os.path.exists(self.config_file):  # remove config if exists
            os.remove(self.config_file)
        profile_inp = profile.read(self.home_dir)

        self.assertIsInstance(profile_inp, profile.Profile)

    def test_last_session(self):
        p = profile.Profile(self.sessions())
        last = p.last_session()

        self.assertEquals(last.host, "192.168.1.2")
        self.assertEquals(last.port, 7777)
        self.assertEquals(last.db_name, "test_db")

    def test_last_session_empty(self):
        p = profile.Profile([])

        self.assertIsNone(p.last_session())

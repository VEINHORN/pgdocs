"""
Contains different validations
"""

from profile import profile


def connection_props(host, port, database):
    """Validates and tries to return proper connection properties"""
    home_dir = "./"
    pf = profile.read(home_dir)

    if host and port and database:
        pf.sessions.append(profile.Session(host, port, database))
        if len(pf.sessions) > 5:
            pf.sessions = pf.sessions[1:]
            profile.save(pf, home_dir)
        else:
            profile.save(pf, home_dir)
        return (host, port, database)
    elif pf.sessions and pf.last_session():
        session = pf.last_session()
        return (session.host, session.port, session.db_name)
    elif database:  # when user provided db name it returns default host and port
        return ("localhost", 5432, database)
    else:
        raise Exception(
            "There are no available sessions to get connection properties")

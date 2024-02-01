from typing import Optional, Union


class Database:
    def __init__(self,
                 dialect: str,
                 user: str,
                 host: str,
                 password: str,
                 database: str,
                 port: Optional[Union[str, int]] = "",
                 ) -> None:
        self.dialect = dialect
        self.user = user
        self.host = host
        self.password = password
        self.database = database

        if type(port) is int:
            self.port = port
        else:
            raise ValueError()

    def connection_url():
        # dialect://username:password@host:port/database
        pass

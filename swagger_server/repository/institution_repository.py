class InstitutionRepository:
    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory        

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute("SELECT * FROM institution WHERE status = 'A'")
            return rows
        
    def get_institution_by_id(self, institution_id):
        with self.session_factory() as session:
            row = session.execute(f"SELECT * FROM institution WHERE id = {institution_id} AND status = 'A'")
            return row
        
    def add_institution(self, body):
        with self.session_factory() as session:
            result = session.execute(f"INSERT INTO institution VALUES(default, '{body.name}', '{body.description}', '{body.address}', '{body.created_user}', SYSDATE(), default, SYSDATE(), 'A')")
            session.commit()
            row = session.execute(f"SELECT * FROM institution WHERE id = {result.lastrowid} AND status = 'A'")
            return row
    
    def update_institution(self, body):
        with self.session_factory() as session:
            session.execute(f"UPDATE institution SET name = '{body.name}', description = '{body.description}', address = '{body.address}', updated_user = '{body.updated_user}', updated_at = SYSDATE() WHERE id = {body.id}")
            session.commit()
            row = session.execute(f"SELECT * FROM institution WHERE id = {body.id} AND status = 'A'")
            return row

    def delete_institution(self, institution_id):
        with self.session_factory() as session:
            session.execute(f"DELETE FROM institution WHERE id = {institution_id}")
            session.commit()
            
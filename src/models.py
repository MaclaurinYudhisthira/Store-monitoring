from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Store_status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer)
    timestamp_utc = db.Column(db.DateTime)
    status = db.Column(db.String(50))
    def __init__(self,store_id,timestamp_utc,status):
        self.store_id=store_id
        self.timestamp_utc=timestamp_utc
        self.status=status

class Timezone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store_status.store_id'))
    timezone_str = db.Column(db.String(50))
    def __init__(self,store_id,timezone):
        self.store_id=store_id
        self.timezone_str=timezone_str

class BusinessHours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store_status.store_id'))
    day_of_week = db.Column(db.Integer)
    start_time_local = db.Column(db.Time)
    end_time_local = db.Column(db.Time)
    def __init__(self,store_id,day_of_week,start_time_local,end_time_local):
        self.store_id=store_id
        self.day_of_week=day_of_week
        self.start_time=start_time
        self.end_time=end_time
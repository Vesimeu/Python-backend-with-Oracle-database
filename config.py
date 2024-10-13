class Config:
    SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://my_app:my_password@localhost:1521/?service_name=XEPDB1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

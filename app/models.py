from . import db

class Sotrudnik(db.Model):
    __tablename__ = 'Sotrudnik'
    id = db.Column(db.Integer, primary_key=True)
    familiya = db.Column(db.String(20), nullable=False)
    inmya = db.Column(db.String(20), nullable=False)
    otchestvo = db.Column(db.String(20), nullable=True)
    Kod_sot = db.Column(db.Integer, nullable=False)
    Kod_dol = db.Column(db.Integer, db.ForeignKey('Dolzhnosti.Kod_dol'))
    Kod_step = db.Column(db.Integer, db.ForeignKey('Stepeni.Kod_step'))
    Kod_fac = db.Column(db.Integer, db.ForeignKey('Facultetov.Kod_fac'))
    stazh = db.Column(db.Integer, nullable=True)
    Kod_prin = db.Column(db.Integer, db.ForeignKey('Prinadlezhnosti.Kod_prin'))
    kabinet = db.Column(db.String(5), nullable=True)
    Kod_caf = db.Column(db.Integer, db.ForeignKey('Cafedri.Kod_caf'))

class Dolzhnosti(db.Model):
    __tablename__ = 'Dolzhnosti'
    Kod_dol = db.Column(db.Integer, primary_key=True)
    dolzhnost = db.Column(db.String(50), nullable=False)

class Stepeni(db.Model):
    __tablename__ = 'Stepeni'
    Kod_step = db.Column(db.Integer, primary_key=True)
    stepen = db.Column(db.String(50), nullable=False)

class Facultetov(db.Model):
    __tablename__ = 'Facultetov'
    Kod_fac = db.Column(db.Integer, primary_key=True)
    facultet = db.Column(db.String(50), nullable=False)

class Prinadlezhnosti(db.Model):
    __tablename__ = 'Prinadlezhnosti'
    Kod_prin = db.Column(db.Integer, primary_key=True)
    prinadlezhnost = db.Column(db.String(50), nullable=False)

class Cafedri(db.Model):
    __tablename__ = 'Cafedri'
    Kod_caf = db.Column(db.Integer, primary_key=True)
    cafedra = db.Column(db.String(50), nullable=False)

"""Initial migration for Oracle

Revision ID: b08426b32ccb
Revises: 
Create Date: 2024-10-13 19:22:49.366875

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import oracle

# revision identifiers, used by Alembic.
revision = 'b08426b32ccb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sotrudnik')
    op.drop_table('stepeni')
    op.drop_table('cafedri')
    op.drop_table('prinadlezhnosti')
    op.drop_table('dolzhnosti')
    op.drop_table('facultetov')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facultetov',
    sa.Column('kod_fac', oracle.NUMBER(precision=3, scale=0, asdecimal=False), nullable=False),
    sa.Column('facultet', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('kod_fac', name='sys_c008690'),
    oracle_resolve_synonyms=False
    )
    op.create_table('dolzhnosti',
    sa.Column('kod_dol', oracle.NUMBER(precision=4, scale=0, asdecimal=False), nullable=False),
    sa.Column('dolzhnost', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('kod_dol', name='sys_c008688'),
    oracle_resolve_synonyms=False
    )
    op.create_table('prinadlezhnosti',
    sa.Column('kod_prin', oracle.NUMBER(precision=3, scale=0, asdecimal=False), nullable=False),
    sa.Column('prinadlezhnost', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('kod_prin', name='sys_c008691'),
    oracle_resolve_synonyms=False
    )
    op.create_table('cafedri',
    sa.Column('kod_caf', oracle.NUMBER(precision=4, scale=0, asdecimal=False), nullable=False),
    sa.Column('cafedra', sa.VARCHAR(length=60), nullable=True),
    sa.PrimaryKeyConstraint('kod_caf', name='sys_c008692'),
    oracle_resolve_synonyms=False
    )
    op.create_table('stepeni',
    sa.Column('kod_step', oracle.NUMBER(precision=2, scale=0, asdecimal=False), nullable=False),
    sa.Column('stepen', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('kod_step', name='sys_c008689'),
    oracle_resolve_synonyms=False
    )
    op.create_table('sotrudnik',
    sa.Column('familiya', sa.VARCHAR(length=20), nullable=True),
    sa.Column('inmya', sa.VARCHAR(length=20), nullable=True),
    sa.Column('otchestvo', sa.VARCHAR(length=25), nullable=True),
    sa.Column('kod_sot', oracle.NUMBER(precision=4, scale=0, asdecimal=False), nullable=True),
    sa.Column('kod_dol', oracle.NUMBER(precision=4, scale=0, asdecimal=False), nullable=True),
    sa.Column('kod_step', oracle.NUMBER(precision=2, scale=0, asdecimal=False), nullable=True),
    sa.Column('kod_fac', oracle.NUMBER(precision=3, scale=0, asdecimal=False), nullable=True),
    sa.Column('stazh', oracle.NUMBER(precision=2, scale=0, asdecimal=False), nullable=True),
    sa.Column('kod_prin', oracle.NUMBER(precision=3, scale=0, asdecimal=False), nullable=True),
    sa.Column('kabinet', sa.VARCHAR(length=5), nullable=True),
    sa.Column('kod_caf', oracle.NUMBER(precision=4, scale=0, asdecimal=False), nullable=True),
    sa.Column('id', oracle.NUMBER(asdecimal=False), nullable=False),
    sa.ForeignKeyConstraint(['kod_caf'], ['cafedri.kod_caf'], name='fk_sotrudnik_cafedri'),
    sa.ForeignKeyConstraint(['kod_dol'], ['dolzhnosti.kod_dol'], name='fk_sotrudnik_dolzhnosti'),
    sa.ForeignKeyConstraint(['kod_fac'], ['facultetov.kod_fac'], name='fk_sotrudnik_facultetov'),
    sa.ForeignKeyConstraint(['kod_prin'], ['prinadlezhnosti.kod_prin'], name='fk_sotrudnik_prinadlezhnosti'),
    sa.ForeignKeyConstraint(['kod_step'], ['stepeni.kod_step'], name='fk_sotrudnik_stepeni'),
    sa.PrimaryKeyConstraint('id', name='sys_c008687')
    )
    # ### end Alembic commands ###

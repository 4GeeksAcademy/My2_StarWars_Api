"""empty message

Revision ID: e1aa23afc7e4
Revises: d7a2e8139e0f
Create Date: 2024-10-17 05:38:55.295578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1aa23afc7e4'
down_revision = 'd7a2e8139e0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fcharacter_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('fcvehicle_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('fplanet_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'favoritevehicles', ['fcvehicle_id'], ['id'])
        batch_op.create_foreign_key(None, 'favoriteplanets', ['fplanet_id'], ['id'])
        batch_op.create_foreign_key(None, 'favoritecharacters', ['fcharacter_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fplanet_id')
        batch_op.drop_column('fcvehicle_id')
        batch_op.drop_column('fcharacter_id')

    # ### end Alembic commands ###
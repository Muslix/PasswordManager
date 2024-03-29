"""Add category to password model

Revision ID: 2a3cf1c9b84e
Revises: 
Create Date: 2023-03-19 12:11:35.486889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a3cf1c9b84e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   # Creating category table
    op.create_table(
        'category',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False, unique=True),
    )

    # Adding new columns to password and password_history
    op.add_column('password', sa.Column('category_id', sa.Integer, sa.ForeignKey('category.id')))
    op.add_column('password_history', sa.Column('category_id', sa.Integer, sa.ForeignKey('category.id')))

    # Creating the default 'Personal' category
    conn = op.get_bind()
    conn.execute(text("INSERT INTO category (name) VALUES ('Personal')"))

    # Updating existing records to point to the new 'Personal' category
    conn.execute(text("UPDATE password SET category_id = (SELECT id FROM category WHERE name='Personal')"))
    conn.execute(text("UPDATE password_history SET category_id = (SELECT id FROM category WHERE name='Personal')"))

    # Removing the old 'category' columns
    op.drop_column('password', 'category')
    op.drop_column('password_history', 'category')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('password', schema=None) as batch_op:
        batch_op.drop_column('category')

    # ### end Alembic commands ###

"""added like field to Article

Revision ID: 873c15918216
Revises: be7b96cc1b42
Create Date: 2024-10-14 07:11:03.494081

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "873c15918216"
down_revision: Union[str, None] = "be7b96cc1b42"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("articles", sa.Column("likes", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("articles", "likes")
    # ### end Alembic commands ###

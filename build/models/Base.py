from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

# Usa MetaData para mapear las tablas existentes
metadata = MetaData()

Base = declarative_base(metadata=metadata)

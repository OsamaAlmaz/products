import factory
from productsapp.models.main import Website
from productsapp.main import Engine
engine = Engine()
session = engine.session_maker()

"""
class Website(BaseModel):
    __tablename__ = 'website'
    id = Column (BigInteger, primary_key=True)
    website_name = Column (String(length=225), nullable=False)
    website_base_url = Column(String(length=True), nullable=False)

"""



class WebsiteFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Website
        sqlalchemy_session = engine.session_maker()

    
    website_name = factory.Sequence(lambda n: 'my_website_name_{}'.format(n))
    website_base_url = factory.Sequence(lambda n: 'www.example_{}.com'.format(n))


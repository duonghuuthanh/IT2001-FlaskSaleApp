from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from saleapp import db, app


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)


class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Điện thoại')
        # c2 = Category(name='Máy tính bảng')
        # c3 = Category(name='Phụ kiện')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        p1 = Product(name='iPhone 13', price=27000000, description='Apple, 128GB',
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg', category_id=1)
        p2 = Product(name='iPhone 13 Pro Max', price=32000000, description='Apple, 512GB',
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',
                     category_id=1)
        p3 = Product(name='iPPad Pro 2022', price=22000000, description='Apple, 128GB',
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=2)
        p4 = Product(name='Galaxy Tab S8', price=24000000, description='Samsung, 128GB',
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
                     category_id=2)
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
        # db.create_all()
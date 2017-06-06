from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

def register_models(Base):
    class Package(Base):
        __tablename__ = "packages"
        id = Column(Integer, primary_key=True)

        name = Column(String(100))
        category = Column(String(100))
        description = Column(Text())
        icon_url = Column(String(100))
        
        install_methods = relationship("InstallMethod")


    class InstallMethod(Base):
        ALLOWED_INSTALLERS_BY_VERSION = {
            "ubuntu": ["ubuntu", "apt"],
            "debian": ["debian", "apt"]
        }
        __tablename__ = "install_methods"
        id = Column(Integer, primary_key=True)

        method_type = Column(String(20))
        pre_install = Column(Text())
        package_name = Column(String(80))
        post_install = Column(Text())

        package_id = Column(Integer, ForeignKey('packages.id'))
        package = relationship("Package", back_populates="install_methods")

    return Package, InstallMethod

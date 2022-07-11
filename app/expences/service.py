from app.expences.repository import CatalogRepository


class CatalogService:
    def get_all(self, args):
        return CatalogRepository.get_all(self, args)

    def get_one(self, id, fields):
        return CatalogRepository.get_one(self, id, fields)

    def sum(self, by):
        return CatalogRepository.sum(self, by)

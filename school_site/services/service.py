from django.db import models, IntegrityError, OperationalError
from django.core.exceptions import ObjectDoesNotExist

class Service:
    def __init__(self, model: models.Model):
        self.model = model

    def get_all(self):
        """Retorna todos os registros do modelo"""
        return self.model.objects.all()

    def get_by_pk(self, pk):
        """Busca um registro pelo ID"""
        try:
            return self.model.objects.get(id=pk)
        except ObjectDoesNotExist:
            raise ValueError(f"{self.model.__name__} não encontrado.")  # Deixa a view decidir a resposta

    def create(self, data: dict):
        """Cria um novo registro"""
        try:
            return self.model.objects.create(**data)
        except IntegrityError:
            raise ValueError(f"Erro ao criar {self.model.__name__}, verifique os dados enviados. {IntegrityError}")

    def update(self, pk, data):
        """Atualiza um registro existente"""
        try:
            obj = self.model.objects.get(id=pk)
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        except ObjectDoesNotExist:
            raise ValueError(f"{self.model.__name__} não encontrado.")
        except IntegrityError:
            raise ValueError(f"Erro ao atualizar {self.model.__name__}, verifique os dados.")

    def delete(self, pk):
        """Deleta um registro"""
        try:
            obj = self.model.objects.get(id=pk)
            obj.delete()
            return {"message": f"{self.model.__name__} deletado com sucesso."}
        except ObjectDoesNotExist:
            raise ValueError(f"{self.model.__name__} não encontrado.")
        except OperationalError:
            raise ValueError(f"Erro ao tentar deletar {self.model.__name__}.")

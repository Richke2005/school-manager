from .service import Service
from ..models import Auth_user

class UserService(Service):
    def __init__(self):
        super().__init__(Auth_user)

    def create_user(self, data: dict):
        """Cria um novo usuário"""
        password = data.pop('password', None)
        try:
            # Criar o usuário sem a senha
            user = self.model.objects.create(**data)
            
            # Definir a senha de forma segura
            if password:
                user.set_password(password)  # 🔒 Criptografa a senha corretamente
                user.save()  # Salva as mudanças

            return user
        except Exception as e:
            raise ValueError(f"Erro ao criar usuário: {str(e)}")

from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rol.models import *

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Los usuarios deben tener correo")
        if not username:
            raise ValueError("Los usuarios deben tener username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password= password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser= True
        user.save(using=self._db)
        return user
"""
Se definen los estados de un Usuario
"""
ESTADOS_USUARIO = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo')
)


class Usuario(AbstractBaseUser):
    """
    Implementa la clase de Usuarios, hereda campos de AbstractUser en la que se
    encuentran campos necesarios como Nombre, Apellido, Contraseña, email.
    """
    email= models.EmailField(verbose_name="email", max_length=60)
    username= models.CharField(max_length=30, unique=True)
    first_name= models.CharField(max_length=60, default='')
    last_name = models.CharField(max_length=60, default='')
    date_joined= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    hide_email= models.BooleanField(default=True)
    estado= models.CharField(max_length=8, choices=ESTADOS_USUARIO, default='Activo')
    ci= models.CharField(max_length=10, null=True, blank=True)
    telefono= models.CharField(max_length=50, null=True, blank=True)
    direccion= models.CharField(max_length=200, null=True, blank=True)
    descripcion= models.TextField(null=True, blank=True)
    roles = models.ManyToManyField('rol.Rol', blank=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UsuarioManager()
    
    def __str__(self):
        """
        Metodo que retorna el nombre del usuario
        :return: retorna el valor del campo username del objeto
        """
        return self.username
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
	    return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
	    return True
    def get_permisos(self):
        permisos = []
        roles = []
        permisos_list =[]
        if self.is_superuser:
            for permiso in Permiso.objects.all():
                permisos_list.append(permiso.nombre)
        """ else:
            for rol in self.roles.all():
               p = Permiso.objects.get(rol=rol.pk)
                for permiso in p:
                    permisos.append(permiso.nombre)
            
            permisos_list= list(set(permisos)) """
        return 'Seguridad'
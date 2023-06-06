def userEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "first_name": item["first_name"],
        "last_name" : item["last_name"],
        "password": item["password"],
        "email": item["email"],
        "phone": item["phone"]
    }
    
def usersEntity(usuario) -> list:
  return [userEntity(item) for item in usuario]
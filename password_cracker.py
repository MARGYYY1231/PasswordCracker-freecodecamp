import hashlib


#Hashes password with SHA1
def hash_with_sha1(password):
  return hashlib.sha1(password.encode('utf-8')).hexdigest()


#Get top 10,000 passwords from file
def get_top_passwords():
  with open('top-10000-passwords.txt', 'r') as f:
    return f.read().splitlines()


## Get known salts from file
def get_known_salts():
  with open('known-salts.txt', 'r') as f:
    return f.read().splitlines()


def crack_sha1_hash(hash, use_salts=False):
  passwords = get_top_passwords()
  salts = get_known_salts()

  #If salts are not used, only check passwords
  if not use_salts:
    for password in passwords:
      if hash_with_sha1(password) == hash:
        return password
  else:
    #Combines Passwords and Salts
    for password in passwords:
      for salt in salts:
        #Append
        if hash_with_sha1(password + salt) == hash:
          return password

        #Prepend
        if hash_with_sha1(salt + password) == hash:
          return password
  return "PASSWORD NOT IN DATABASE"

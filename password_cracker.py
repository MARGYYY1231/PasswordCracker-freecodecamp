import hashlib


def hash_with_sha1(password):
  return hashlib.sha1(password.encode('utf-8')).hexdigest()


def get_top_passwords():
  with open('top-10000-passwords.txt', 'r') as f:
    return f.read().splitlines()


def get_known_salts():
  with open('known-salts.txt', 'r') as f:
    return f.read().splitlines()


def crack_sha1_hash(hash, use_salts=False):
  passwords = get_top_passwords()
  salts = get_known_salts()

  if not use_salts:
    for password in passwords:
      if hash_with_sha1(password) == hash:
        return password
  else:
    for password in passwords:
      for salt in salts:
        #Append
        if hash_with_sha1(password + salt) == hash:
          return password

        #Prepend
        if hash_with_sha1(salt + password) == hash:
          return password
  return "PASSWORD NOT IN DATABASE"

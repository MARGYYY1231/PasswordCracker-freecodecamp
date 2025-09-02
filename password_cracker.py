import hashlib


def hash_with_sha1(password):
  return hashlib.sha1(password.encode('utf-8')).hexdigest()


def crack_sha1_hash(hash, use_salts=False):
  return True

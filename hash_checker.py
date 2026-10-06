import hashlib

def calcular_hash(caminho_arquivo):
    sha256_hash = hashlib.sha256()
    try:
        with open(caminho_arquivo, "rb") as f:
            for byte_bloco in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_bloco)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "Arquivo não encontrado."

if __name__ == "__main__":
    print("--- Verificador de Integridade (Hash SHA-256) ---")
    arquivo = input("Digite o caminho do arquivo: ").strip()
    
    ##  Remove aspas caso arraste o arquivo para o terminal
    arquivo = arquivo.strip('"').strip("'")
    
    resultado = calcular_hash(arquivo)
    print(f"\nHash SHA-256:\n{resultado}")
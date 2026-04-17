#!/usr/bin/env python3
"""
Script para converter o guia RFLog de Obsidian para MkDocs.
- Converte wikilinks [[arquivo]] para markdown links [texto](path/arquivo.md)
- Copia arquivos para estrutura do site
- Ajusta caminhos de screenshots
"""

import os
import re
import shutil
from pathlib import Path

# Caminhos
SOURCE_DIR = Path(r"C:\Users\rodri\OneDrive\Documentos\claudianos\RFLog_Guia")
TARGET_DIR = Path(r"C:\Users\rodri\OneDrive\Documentos\claudianos\RFLog_Guia\site\docs")
SCREENSHOTS_SOURCE = SOURCE_DIR / "mapeamento_rflog" / "screenshots"
SCREENSHOTS_TARGET = TARGET_DIR / "assets" / "screenshots"

# Mapeamento de wikilinks para arquivos
def build_file_map():
    """Constrói mapeamento de nomes de arquivos."""
    file_map = {}

    # Arquivos na raiz
    for f in SOURCE_DIR.glob("*.md"):
        name = f.stem  # nome sem extensão
        file_map[name.lower()] = f
        file_map[name] = f  # também com case original

    # Arquivos em 03_Modulos
    modulos_dir = SOURCE_DIR / "03_Modulos"
    if modulos_dir.exists():
        for f in modulos_dir.glob("*.md"):
            name = f.stem
            file_map[name.lower()] = f
            file_map[name] = f

    # Arquivos em 04_Referencia
    ref_dir = SOURCE_DIR / "04_Referencia"
    if ref_dir.exists():
        for f in ref_dir.glob("*.md"):
            name = f.stem
            file_map[name.lower()] = f
            file_map[name] = f

    return file_map

def convert_wikilinks(content, current_file_path, source_dir):
    """Converte wikilinks para markdown links."""

    # Padrão para wikilink [[Nome_Arquivo]] ou [[Nome_Arquivo#seção]]
    wikilink_pattern = r'\[\[([^\]|#\]]+)(?:#([^\]]+))?(?:\|([^\]]+))?\]\]'

    def replace_wikilink(match):
        link_target = match.group(1).strip()
        link_section = match.group(2)  # seção, se houver
        link_text = match.group(3)  # texto alternativo, se houver

        # Nome do arquivo alvo
        target_name = link_target

        # Texto do link
        if link_text:
            text = link_text
        else:
            text = link_target.replace('_', ' ')

        # Determinar caminho relativo
        current_depth = len(current_file_path.relative_to(source_dir).parts) - 1

        # Verificar onde está o arquivo alvo
        target_file = None

        # Procurar na raiz
        if (source_dir / f"{target_name}.md").exists():
            target_file = source_dir / f"{target_name}.md"
            if current_depth == 0:
                path = f"{target_name}.md"
            elif current_depth == 1:  # em 03_Modulos ou 04_Referencia
                # Subir um nível para arquivos na raiz
                path = f"../{target_name}.md"
            else:
                path = f"../{'../' * (current_depth - 1)}{target_name}.md"

        # Procurar em 03_Modulos
        elif (source_dir / "03_Modulos" / f"{target_name}.md").exists():
            target_file = source_dir / "03_Modulos" / f"{target_name}.md"
            if current_depth == 0:
                path = f"03_Modulos/{target_name}.md"
            elif current_depth == 1:
                if "03_Modulos" in str(current_file_path):
                    path = f"{target_name}.md"
                else:
                    path = f"../03_Modulos/{target_name}.md"
            else:
                path = f"../{'../' * (current_depth - 1)}03_Modulos/{target_name}.md"

        # Procurar em 04_Referencia
        elif (source_dir / "04_Referencia" / f"{target_name}.md").exists():
            target_file = source_dir / "04_Referencia" / f"{target_name}.md"
            if current_depth == 0:
                path = f"04_Referencia/{target_name}.md"
            elif current_depth == 1:
                if "04_Referencia" in str(current_file_path):
                    path = f"{target_name}.md"
                else:
                    path = f"../04_Referencia/{target_name}.md"
            else:
                path = f"../{'../' * (current_depth - 1)}04_Referencia/{target_name}.md"

        else:
            # Não encontrado - manter como texto
            return f"[{text}]({target_name})"

        # Adicionar âncora de seção se houver
        if link_section:
            section_slug = link_section.lower().replace(' ', '-').replace('_', '-')
            path = f"{path}#{section_slug}"

        return f"[{text}]({path})"

    return re.sub(wikilink_pattern, replace_wikilink, content)

def convert_screenshot_paths(content, current_file_path, source_dir):
    """Converte caminhos de screenshots relativos."""

    # Padrão para ![](../mapeamento_rflog/screenshots/...)
    # ou ![](./mapeamento_rflog/screenshots/...)
    # ou ![](mapeamento_rflog/screenshots/...)

    pattern = r'!\[([^\]]*)\]\(([^)]*mapeamento_rflog[^)]*screenshots[^)]*)\)'

    def replace_screenshot(match):
        alt_text = match.group(1)
        old_path = match.group(2)

        # Extrair nome do arquivo
        filename = Path(old_path).name

        # Novo caminho para MkDocs
        current_depth = len(current_file_path.relative_to(source_dir).parts) - 1

        if current_depth == 0:
            new_path = f"assets/screenshots/{filename}"
        else:
            new_path = f"../{'../' * current_depth}assets/screenshots/{filename}"

        return f"![{alt_text}]({new_path})"

    return re.sub(pattern, replace_screenshot, content)

def process_file(source_file, target_file, source_dir):
    """Processa um arquivo markdown."""
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Converter wikilinks
    content = convert_wikilinks(content, source_file, source_dir)

    # Converter caminhos de screenshots
    content = convert_screenshot_paths(content, source_file, source_dir)

    # Escrever arquivo processado
    target_file.parent.mkdir(parents=True, exist_ok=True)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("=== Conversor RFLog Guide: Obsidian -> MkDocs ===")

    # Criar diretórios de destino
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOTS_TARGET.mkdir(parents=True, exist_ok=True)

    # Copiar screenshots
    print("\nCopiando screenshots...")
    for f in SCREENSHOTS_SOURCE.glob("*.png"):
        shutil.copy2(f, SCREENSHOTS_TARGET / f.name)
        print(f"  - {f.name}")

    # Processar arquivos na raiz
    print("\nProcessando arquivos raiz...")
    for f in SOURCE_DIR.glob("*.md"):
        target = TARGET_DIR / f.name
        process_file(f, target, SOURCE_DIR)
        print(f"  - {f.name}")

    # Processar 03_Modulos
    print("\nProcessando 03_Modulos...")
    modulos_source = SOURCE_DIR / "03_Modulos"
    modulos_target = TARGET_DIR / "03_Modulos"
    modulos_target.mkdir(parents=True, exist_ok=True)

    for f in modulos_source.glob("*.md"):
        target = modulos_target / f.name
        process_file(f, target, SOURCE_DIR)
        print(f"  - {f.name}")

    # Processar 04_Referencia
    print("\nProcessando 04_Referencia...")
    ref_source = SOURCE_DIR / "04_Referencia"
    ref_target = TARGET_DIR / "04_Referencia"
    ref_target.mkdir(parents=True, exist_ok=True)

    for f in ref_source.glob("*.md"):
        target = ref_target / f.name
        process_file(f, target, SOURCE_DIR)
        print(f"  - {f.name}")

    print("\n=== Conversão concluída! ===")
    print(f"Arquivos processados em: {TARGET_DIR}")
    print(f"Screenshots copiados para: {SCREENSHOTS_TARGET}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

# Ejecución remota:
#   curl -sL https://raw.githubusercontent.com/nipegun/ia-scripts/refs/heads/main/Modelo-Transformer-MaxContextLenght-Mostrar.py | python3 - 'Modelo'
#   Ejemplo:
#     curl -sL https://raw.githubusercontent.com/nipegun/ia-scripts/refs/heads/main/Modelo-Transformer-MaxContextLenght-Mostrar.py | python3 - 'Qwen/Qwen3-0.6B'
#     curl -sL https://raw.githubusercontent.com/nipegun/ia-scripts/refs/heads/main/Modelo-Transformer-MaxContextLenght-Mostrar.py | python3 - 'Qwen/Qwen3-0.6B' --noenv

import sys
import argparse

def fEstaEnVenv():
  return sys.prefix != sys.base_prefix

def fMain():
  oPreParser = argparse.ArgumentParser(add_help=False)
  oPreParser.add_argument(
    "--noenv",
    action="store_true",
    help="No comprobar si se está ejecutando dentro de un venv"
  )
  oPreArgs, oRestArgs = oPreParser.parse_known_args()

  if not oPreArgs.noenv and not fEstaEnVenv():
    print("ERROR: este script debe ejecutarse dentro de un venv (use --noenv para omitir)", file=sys.stderr)
    sys.exit(1)

  import argparse as _argparse
  from transformers import AutoConfig

  oParser = _argparse.ArgumentParser()
  oParser.add_argument(
    "vModelo",
    help="Modelo de Hugging Face (ej: Qwen/Qwen3-0.6B)"
  )
  oParser.add_argument(
    "--noenv",
    action="store_true",
    help="No comprobar si se está ejecutando dentro de un venv"
  )

  oArgs = oParser.parse_args()

  oCfg = AutoConfig.from_pretrained(oArgs.vModelo)
  print(oCfg.max_position_embeddings)


if __name__ == "__main__":
  fMain()

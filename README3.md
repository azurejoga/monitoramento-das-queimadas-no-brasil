# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c2e5938-e383-3ce5-958f-a1c375d5180c | -7.5705 | -45.4786 | 2025-09-19 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 830a2e55-8691-3048-bc8f-8e17e9c5d99d | -17.2369 | -45.924 | 2025-09-19 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3aacf19f-5e05-3848-9a1e-64bb13dc2dff | -9.1747 | -45.2907 | 2025-09-19 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 03d9a3be-68d5-3f3f-86c8-9e863a968dc2 | -17.2169 | -45.9282 | 2025-09-19 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 176.4 |
| c9c5e7b9-8202-369e-8546-c9e3bcde562d | -17.2363 | -45.9476 | 2025-09-19 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 127.4 |
| c7502897-0075-3c53-92e7-6f1ce74333cc | -8.1381 | -46.771 | 2025-09-19 01:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6ee5d436-df8e-3eba-80ea-4138b79c7813 | -9.1744 | -45.3135 | 2025-09-19 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8f347c49-cdb7-3f27-bb77-d7ad372a5274 | -9.1933 | -45.3114 | 2025-09-19 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| b1c0d8ce-57dd-34dd-9950-c214a77c382d | -10.9152 | -45.6461 | 2025-09-19 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| ae681615-7a6a-3a91-87e4-0c7e0c2b2617 | -20.8052 | -47.2273 | 2025-09-19 01:20:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b9e434bc-e232-3eab-a0bd-45151754c2b3 | -20.7846 | -47.2323 | 2025-09-19 01:20:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 88a6210e-e5e0-346b-aae8-de4d3de49a4a | -22.10388 | -55.23427 | 2025-09-19 01:26:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 81817c42-a08c-3ba1-bd55-16d234fd51e9 | -22.10131 | -55.2192 | 2025-09-19 01:26:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 35.9 |
| a44f4e88-64fd-3fb5-abdb-c1159ea43fbe | -20.53414 | -55.18189 | 2025-09-19 01:26:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6d482269-939c-34b2-8742-be9263ad8f61 | -15.8004 | -59.40443 | 2025-09-19 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8557b5cc-3588-3007-a18f-cbe5754350ce | -14.74701 | -60.20095 | 2025-09-19 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5cbae2b2-4ccc-3bb1-9519-509fac04383c | -19.57538 | -57.74558 | 2025-09-19 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| c8c01daf-5325-3b6f-b3a7-96465696e010 | -19.5894 | -57.83629 | 2025-09-19 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 0fb44f48-fd47-3dc1-8624-cd06b4555ea9 | -15.78107 | -59.38248 | 2025-09-19 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 054affe2-7245-3e56-a630-a4e3071014ca | -15.79488 | -59.41157 | 2025-09-19 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ad7e585-6d8b-33db-a72d-5737586007ee | -14.83587 | -60.24051 | 2025-09-19 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e610740d-3ca8-32f3-b83b-cfabc5f53ac4 | -19.57801 | -57.82672 | 2025-09-19 01:28:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| fdc44291-0362-3530-8940-322c2cf3e3a9 | -15.79339 | -59.40148 | 2025-09-19 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7c4bd6b8-dec3-38eb-8013-1686cae7c3ec | -15.78257 | -59.39267 | 2025-09-19 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3d5b81c-1e55-34eb-a7b6-7de6db6da06e | -15.27722 | -56.83698 | 2025-09-19 01:28:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 25a1e099-73bb-3583-8565-4e74f21454cd | -15.80192 | -59.4145 | 2025-09-19 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0670cd99-c701-3a0b-b5d3-8952f11fd03e | -14.84492 | -60.23902 | 2025-09-19 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b39be9a0-a5f0-355b-8ea6-610e4efcc554 | -14.8268 | -60.24188 | 2025-09-19 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b3ff88f4-1040-3e8a-9cf3-897969b79a28 | -15.33361 | -59.41066 | 2025-09-19 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bd8461f0-6761-356c-b484-240f84cdd3f3 | -17.2169 | -45.9282 | 2025-09-19 01:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 102.5 |
| ade5a201-a52a-388a-8156-b74c796034ad | -9.1933 | -45.3114 | 2025-09-19 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 1582ee88-fda1-3933-9889-a297881d5d3f | -10.9155 | -45.6232 | 2025-09-19 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d482d6fb-68d4-31f3-a239-0b0fa33fc665 | -7.5705 | -45.4786 | 2025-09-19 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| da47262d-3f65-3c48-be06-b5d585f0c9f8 | -8.019 | -45.7072 | 2025-09-19 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| eaa39592-7e10-381b-8e3a-6f8437ede2d6 | -9.1744 | -45.3135 | 2025-09-19 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 224e65f9-e973-3372-91c1-f504e3ab22f9 | -6.2732 | -43.9225 | 2025-09-19 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| b01d287a-ca4b-3465-be69-9436eab08ba2 | -8.0379 | -45.7054 | 2025-09-19 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 65442e9d-ee05-3e32-9a0e-fa42b42765a3 | -20.8052 | -47.2273 | 2025-09-19 01:30:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 58fdc81a-5c21-3948-a359-14b8dfad69fa | -17.2363 | -45.9476 | 2025-09-19 01:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 82.1 |
| ab4a944d-368f-36ae-9eaf-b10aadcdf462 | -17.2163 | -45.9518 | 2025-09-19 01:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 905b68e1-4a1a-3b3a-979c-9d0f2865a5f4 | -22.3449 | -46.7648 | 2025-09-19 01:30:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 0a793cac-0e83-3758-a9f2-caa1955005f3 | -14.2666 | -51.3479 | 2025-09-19 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 2655fbb6-ef58-37b5-99ad-7bd5f915c5e9 | -10.9148 | -45.669 | 2025-09-19 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 72573834-3e20-3bd1-a6e5-779aae88d262 | -10.9343 | -45.6436 | 2025-09-19 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b14b4ad8-b1b2-3c5e-989a-13aa04f9c100 | -8.0564 | -45.7262 | 2025-09-19 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| a51d9eeb-d896-360b-82cd-726b85d9101c | -6.2544 | -43.9241 | 2025-09-19 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 8d5ea47c-76e5-3d61-af5a-9af52bd3a725 | -10.9152 | -45.6461 | 2025-09-19 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 91b1cafe-222b-33e0-88c9-5bd03bb8464e | -6.2547 | -43.9009 | 2025-09-19 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 46cc293f-2fd2-30a5-a4cd-91f1c9aae040 | -13.2996 | -54.2 | 2025-09-19 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5b0de47e-ee6b-32dc-b8b8-f4644d7a8799 | -8.0376 | -45.728 | 2025-09-19 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 23a9e98f-fd69-3cf0-a036-f2bfbd5cbf8a | -13.85077 | -59.36216 | 2025-09-19 01:30:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 82edaeeb-e328-3efa-b186-cabb222bed19 | -17.2169 | -45.9282 | 2025-09-19 01:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 36aa81dd-c1fc-34de-9d85-a201c81495bf | -5.8996 | -45.8628 | 2025-09-19 01:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| f8e76554-b437-351c-957c-68dbe8321e46 | -9.1747 | -45.2907 | 2025-09-19 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 4fc181bc-2ac4-39f9-9846-3022cbce93e6 | -6.2544 | -43.9241 | 2025-09-19 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 3e97368e-9ecb-30fd-90bd-f6db99770f94 | -8.0379 | -45.7054 | 2025-09-19 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| b71f9a28-0964-386b-88cb-6181e0614bf6 | -17.2163 | -45.9518 | 2025-09-19 01:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 224acf69-7b60-389d-afd8-c53fbb3f5b0f | -10.9343 | -45.6436 | 2025-09-19 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 399f199e-9716-3ffa-9760-15cbadd9e53e | -9.1933 | -45.3114 | 2025-09-19 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| a7b492ce-078b-3c75-9f3c-60761aa1af3c | -9.1937 | -45.2886 | 2025-09-19 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 5a12be73-3eb1-3f5a-bde7-4b2dd1a0184f | -10.9155 | -45.6232 | 2025-09-19 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| d5a9bfa2-af27-3518-ae89-d5771d71ad64 | -20.8052 | -47.2273 | 2025-09-19 01:40:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 648c17aa-ca98-3436-bcaa-79913bacb8fb | -20.7846 | -47.2323 | 2025-09-19 01:40:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b573421d-26cf-3753-b0c3-96a928c89586 | -10.9152 | -45.6461 | 2025-09-19 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 34c822a5-6d9e-34dc-acf4-677e596142b2 | -9.1744 | -45.3135 | 2025-09-19 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| f72f332c-ac06-373a-8716-202e2a61159c | -6.2547 | -43.9009 | 2025-09-19 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| aeaee0ef-c7d9-3aa2-ac75-9b75c9295fa1 | -8.019 | -45.7072 | 2025-09-19 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 69c00394-f751-3090-bcb9-875650480a34 | -6.2732 | -43.9225 | 2025-09-19 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c827ea18-04d7-3ea3-a718-b35e5093d092 | -10.9148 | -45.669 | 2025-09-19 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5e3125a4-7c64-306f-9586-a36207ba4b23 | -17.1669 | -44.7823 | 2025-09-19 01:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 5011ccbf-9e7a-345e-adba-628a4e7aa49e | -9.1933 | -45.3114 | 2025-09-19 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 544ad9d5-d54a-3788-95fd-f0eb6c25fe7b | -10.9148 | -45.669 | 2025-09-19 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ad79c5a4-cbc9-3913-9ede-875697dbdc9f | -9.1747 | -45.2907 | 2025-09-19 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| de73d7d9-07eb-33a8-a8e3-761df4b5156a | -6.2544 | -43.9241 | 2025-09-19 01:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| eb419ec9-945b-3e2e-9cfd-fb308a341f0b | -10.9343 | -45.6436 | 2025-09-19 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 2165ef21-853d-3b76-8056-a5b479dcef06 | -9.1741 | -45.3364 | 2025-09-19 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.6 |
| a6aa4aed-fd0a-3b19-b6d4-8f39d2244db1 | -9.1744 | -45.3135 | 2025-09-19 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 7457d9ba-8476-3f48-8e21-37c731dd8857 | -10.9152 | -45.6461 | 2025-09-19 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 862584de-83b2-3ee8-8e1c-01055ce20b32 | -8.1381 | -46.771 | 2025-09-19 01:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| bf24fcda-109d-34cc-9eb1-3afbf75789ae | -6.2732 | -43.9225 | 2025-09-19 01:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| a349ac65-5851-3924-9e5b-2ba43dd56726 | -9.1937 | -45.2886 | 2025-09-19 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 88f09d5a-4922-33e7-a529-3999744165af | -6.2547 | -43.9009 | 2025-09-19 01:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 88a02b63-1df3-3bd2-a365-27bb4b55521f | -17.5939 | -40.2245 | 2025-09-19 02:00:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 110.5 |
| 20cea606-c62d-3d7e-9e16-f6c14b5818a4 | -12.8969 | -50.5398 | 2025-09-19 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ae60a0aa-88f2-378b-affd-274fa292dc1a | -10.9343 | -45.6436 | 2025-09-19 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1b9f1d7a-6557-3aa7-9090-97b1ff75c2d2 | -20.8052 | -47.2273 | 2025-09-19 02:00:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 71af9fc2-e1cd-3ef7-9ad3-703c9253fd0c | -9.1933 | -45.3114 | 2025-09-19 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 15197d3d-ed09-3a88-a40f-5f563d5d4ab9 | -6.2732 | -43.9225 | 2025-09-19 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 24f727f7-1696-321a-9d3c-7eeab03e6250 | -9.1937 | -45.2886 | 2025-09-19 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 10a74c4a-c4ad-3ed4-8f50-463c78d8df7f | -12.9161 | -50.5374 | 2025-09-19 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c5966b63-93c6-3cd5-9566-6f225dafd034 | -12.9157 | -50.5589 | 2025-09-19 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 0ad8c49b-0e42-3bea-9655-0a3cf5edc384 | -9.1747 | -45.2907 | 2025-09-19 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 7b1b2860-eb53-322f-ab80-3ddc03d96583 | -10.9339 | -45.6664 | 2025-09-19 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 12ea56df-9431-34bc-9497-c8bf96bdf3d9 | -6.2544 | -43.9241 | 2025-09-19 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 2fa4cfa9-341c-3a67-974d-85fac7f71363 | -8.1381 | -46.771 | 2025-09-19 02:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 94df1b8a-17a4-3d55-b3db-1f8881f470ee | -12.9164 | -50.5158 | 2025-09-19 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 84589a36-0c77-3190-8800-b8d7ea099bfe | -17.2163 | -45.9518 | 2025-09-19 02:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 101.0 |
| eb3aa5b2-a824-366c-b1fa-db0a94e138a9 | -17.6141 | -40.219 | 2025-09-19 02:00:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 138.8 |
| abcc64be-ffa7-3804-a66f-7f38747ddd4b | -9.1744 | -45.3135 | 2025-09-19 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 8854890d-ffbe-3a2a-a61f-61b6e5cf5fb0 | -6.2547 | -43.9009 | 2025-09-19 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |


[Clique aqui para ver as próximas entradas](README4.md)

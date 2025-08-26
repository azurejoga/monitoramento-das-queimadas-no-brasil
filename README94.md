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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e7bd92e-7508-31f9-ba01-35138a5e62a5 | -9.24127 | -60.92277 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02a76c05-7134-3f9e-a8f9-3f7df3f8fa02 | -9.31307 | -63.44027 | 2025-08-26 06:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 94f1fb29-e832-3ea0-b79d-74ad7cd62674 | -9.24174 | -60.91904 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c96eee56-186a-34c3-9f00-ee80c1d059d6 | -8.55008 | -62.63305 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29238db5-8662-358c-be7a-81f1ffe58a2c | -10.09694 | -68.97974 | 2025-08-26 06:03:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee30390c-ebb0-3e33-b0b1-36d0a29856f0 | -8.87507 | -62.45593 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33bcd19e-50ec-3546-a4e4-ab5be6eefae0 | -7.39237 | -64.34972 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4c12c6d-b83f-3475-8c05-1609947da7ea | -9.15574 | -59.4607 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0055f586-dc3a-35af-8937-3865734434bd | -9.02262 | -65.69949 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eff9b426-c685-338c-a74a-28c82c388c85 | -9.15406 | -60.78784 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc025f1f-a905-3d68-a38d-244261b28065 | -8.11901 | -61.46413 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22240bea-a6bf-3b5a-9d61-074d0a00ab0a | -9.1658 | -59.52718 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 471804a1-a28a-3fa7-96ef-2aea8addcb5c | -9.17009 | -59.54177 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a895c75a-1dbc-368e-b3d5-bb7114c529ce | -9.18024 | -59.51079 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5e60287-1529-388f-93ab-9449bf6df271 | -7.62429 | -61.03848 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1698594b-e535-30ca-a52d-440f280d19b5 | -8.86665 | -62.44326 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0584a778-75a6-3db2-ada0-46d27d5030d8 | -9.18245 | -59.44553 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86438e9f-fd70-380d-ad94-61d47af5827f | -8.11877 | -61.46411 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a817c3da-329e-3924-bc04-3c3647d6afc7 | -7.37845 | -64.3558 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b4ac27a9-482c-3551-b4cb-aeed62932347 | -9.04503 | -65.72632 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4543bbc-7338-3589-a414-b169fb17940d | -9.07674 | -66.06164 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a05440c9-bd3a-3f0d-8bd2-cf883326faf2 | -12.33986 | -64.22684 | 2025-08-26 06:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5b91cf07-3848-33a5-bc24-b3c71ec4cff5 | -7.50052 | -63.50698 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f547482d-7f73-3185-b267-5666e16d51c9 | -9.18854 | -59.44642 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5baf537-6d67-35c8-b7d7-72374c133635 | -9.19611 | -59.53119 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ca2fad0b-69a6-371c-8967-9dd7d23770a7 | -8.99992 | -65.40314 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aac1d4f8-5083-389c-baca-d20322f023f8 | -7.88497 | -63.01707 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3d2d1004-e3f6-3087-ae02-b6a3a665b057 | -9.02001 | -65.70155 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0dea7fa-069a-3ad4-a881-e5e49f6c604d | -9.02075 | -65.69633 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d514477-2bca-3c2f-ae56-ed2787aea580 | -8.98515 | -65.41932 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d565ea39-da36-3010-9d9e-2a2e9a551cc9 | -10.64934 | -65.31714 | 2025-08-26 06:03:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ba6c56e7-3bef-34cb-bb81-8761d30ee23a | -10.01585 | -62.38839 | 2025-08-26 06:03:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f016b11-d7b2-3629-be02-9a154b3b5010 | -9.17459 | -59.45855 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 224d4c81-1084-3329-94ca-fa75758dbee6 | -14.29335 | -60.35372 | 2025-08-26 06:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77e66b72-35ea-3091-9f5a-003fbf1b3c3f | -8.352 | -62.94112 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 068243e2-d87f-3cb0-9142-88f1c400b334 | -9.16242 | -59.45687 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d963a1c5-6bcc-37f3-98f4-65b1a937f0c0 | -8.63377 | -67.24994 | 2025-08-26 06:03:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15fc4bef-8cad-3f77-9571-466d6779ac6b | -9.16755 | -59.51353 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e13cc176-556a-3dd8-8126-0993c90a944f | -9.23526 | -60.92564 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e64349e9-2965-38eb-8ca1-72166b3304e6 | -9.00044 | -65.39954 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e92f1389-ede4-3a14-9b09-a32ab5974140 | -9.1973 | -59.52203 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca80754a-e04f-39d9-bf23-7d3da42470b0 | -9.18516 | -59.52054 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9040b655-5cd8-3292-b23b-f4a49f40cf2a | -9.16639 | -59.52259 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e4467e1-ee60-3fec-bcd9-8b87ca42ec6a | -9.9995 | -67.80251 | 2025-08-26 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 306da810-88e2-3626-a275-d3c78c560304 | -7.38976 | -64.34979 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76e3f4ab-2337-3275-8b9d-d3b40adebebb | -9.00451 | -65.40015 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57df7f31-8c0b-3317-8f05-49a95cb4a7a1 | -8.11191 | -62.88199 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9d3d1f8d-690b-3548-bf66-13c8799abe67 | -9.15456 | -60.78409 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ced23c6-6cce-32ee-ab77-8d43dd2f51ca | -8.86016 | -62.45384 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2edfd6a2-9a9f-38c0-b311-89dd6437b2e9 | -9.01311 | -65.70866 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af33b110-4d01-33b4-9510-7514a4586165 | -9.00762 | -65.37843 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d6204385-0239-3710-b529-9b557b8e3ee8 | -9.88552 | -67.66136 | 2025-08-26 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 153fdf66-4eb3-3551-8398-aa6f122c0a8e | -9.63595 | -59.63998 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a06dd4c-61d3-30e7-9918-32f275df7146 | -7.61797 | -61.04449 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b6e36a5-c664-3e40-9d7f-b04f15fd5131 | -7.38857 | -64.35775 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb983649-5e96-34ef-b5bc-d6f33216d5b2 | -10.90625 | -68.43445 | 2025-08-26 06:03:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d17674fb-e3b1-3099-b05c-2a2c61966307 | -9.1623 | -59.55453 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5cd76a30-2e54-3acb-bfbc-3d94048dac24 | -9.64313 | -59.63218 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9651f622-1253-3f3d-9417-7eae2d71e936 | -8.97904 | -65.43306 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34b77aa8-e8b5-3680-b21e-5f80d319cbae | -12.22366 | -64.22909 | 2025-08-26 06:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 359eb1c9-62a9-3889-9eb3-bfe222ef61cd | -14.29183 | -60.35992 | 2025-08-26 06:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 438df166-ea7e-3b74-b1e7-74c6969f2a13 | -8.24157 | -61.45964 | 2025-08-26 06:03:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58f8a154-ee38-309d-a770-4dd9de4e4310 | -8.57449 | -62.63654 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c49cc35d-2f73-39c7-a09c-c382f9b7fce3 | -9.158 | -59.53999 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bd7e06ad-4675-36f5-869c-cbcf3c9a8432 | -9.26186 | -59.79572 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0e53afa-2c6f-3591-b404-23074f95a1ff | -7.3598 | -59.66515 | 2025-08-26 06:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cef9c94a-c1ef-3abb-9efb-5d05c10edcd0 | -10.18086 | -68.16032 | 2025-08-26 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b3bd283-2549-3c19-b916-77ff93e4a675 | -9.80975 | -64.28876 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 892a1cd2-75d6-32b4-8995-71ebc8730ef4 | -10.25495 | -59.10717 | 2025-08-26 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4e9fa10-77ba-3296-97fd-13eb33cc1a3f | -9.23083 | -60.92051 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ec7b065-cc70-3aab-8c48-9ff803395478 | -9.80572 | -64.25243 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53962d95-01c6-3783-8528-b7c1caab1fca | -9.01749 | -65.69048 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db8adada-dbc8-3383-9026-7dca7328eeb7 | -9.07897 | -62.67471 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b400413-8ca9-3e08-948f-21b6a96c1c7b | -8.34706 | -62.93902 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 68b0e2c8-21c4-3d7a-b658-0688f4258244 | -8.97498 | -65.43246 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e71be1ad-8078-33e1-836c-cae6c849bc3d | -9.16149 | -59.51265 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c33c6ee5-37cf-33c8-b23d-1bcd67e67270 | -9.0171 | -65.70924 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 399f6ef3-2ead-370f-9fa9-c7dcc2f86b31 | -10.41727 | -64.38099 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e225ae19-bfc7-3ac4-ac88-b0f63785f504 | -9.01602 | -65.70097 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83658523-73ca-3aa3-ba43-eff7527496fa | -8.12768 | -62.87383 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45746d24-de1a-3d64-8a91-fa5d88e62f2e | -7.38384 | -64.34846 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa5996fb-e49d-3e8b-8328-c087afcd30e9 | -9.8148 | -64.28506 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5fcbfcc-de15-3092-9b33-f58fbe50b10e | -8.57035 | -62.63053 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3048563-2510-3d1e-a098-4182c9b285d7 | -7.56027 | -63.85591 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fda2ff2-a14f-3adb-9654-0481736daa34 | -8.55834 | -62.64527 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39079e67-e321-3535-bbe0-369ae81da496 | -8.84448 | -62.45109 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 04d0344f-800c-3cf9-80d7-6028a27609ab | -10.18145 | -68.15631 | 2025-08-26 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2ee361a-6a66-3b95-99df-f290693f5793 | -8.8567 | -62.44188 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7316bdf2-7139-3c0e-b36d-523c7a768416 | -9.19005 | -59.53038 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 601746c5-5dc2-370d-9dfe-747356c42588 | -10.10082 | -57.76785 | 2025-08-26 06:03:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc7099ec-9811-3bcd-a7d2-75777937fe5d | -9.27509 | -56.90757 | 2025-08-26 06:03:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cdec055-a7d0-39aa-893e-c89c27ca5c53 | -9.27135 | -59.78608 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 874387d1-32e7-322d-bfdf-7c651fe1d81e | -9.17068 | -59.53722 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12e32c35-4e0d-30ef-8856-2a972dd39b70 | -8.6111 | -62.64275 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2c7a230-dbd2-3b29-9d75-3ee2a3875ae2 | -10.10764 | -57.76874 | 2025-08-26 06:03:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d13b8c1-2a6f-3445-97ca-943ee975c7d1 | -9.18826 | -59.54414 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85880bc2-fd4e-3e8e-9032-2a9953bb9bce | -8.98109 | -65.4187 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e376c06a-f4d8-3aaa-a981-f0df2492380e | -8.24197 | -61.45667 | 2025-08-26 06:03:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82ab5f2e-5967-3011-a0fd-2cd796feae4b | -8.57601 | -62.62573 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d09b905e-2b7c-3204-a2c4-cb5339c9348a | -7.38123 | -64.34855 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README95.md)

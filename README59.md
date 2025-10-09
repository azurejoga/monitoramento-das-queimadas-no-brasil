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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcd6c185-6a0c-37f3-8453-5239d0372e44 | -3.75745 | -51.38799 | 2025-10-09 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44735928-644e-379b-bac7-9b90be6742b0 | -2.88186 | -50.73229 | 2025-10-09 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60a4d6b0-5eb5-3a8a-b49d-348a0a7b151c | -3.3932 | -50.14478 | 2025-10-09 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c8d3f4b-a601-37f1-9129-e9018cbcc868 | -2.19017 | -54.46575 | 2025-10-09 05:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81c29cf5-dd78-3c6e-a8e1-5db8858afa74 | -3.39167 | -50.14803 | 2025-10-09 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ac16b41-5f66-32b4-a4fd-f77292ede73a | -2.88841 | -50.73333 | 2025-10-09 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 704ad604-837f-3ed3-b5c3-393ae2dfb7fb | -6.79355 | -50.49282 | 2025-10-09 05:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 759eb134-461e-33b3-8ae6-caab4fc2dac4 | -3.59299 | -49.35297 | 2025-10-09 05:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1097dff-83d7-32b2-aefe-f20664b3c718 | -2.88724 | -50.73385 | 2025-10-09 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f837c6-bb45-383a-a197-72f1e55fbd8e | -2.88925 | -50.72777 | 2025-10-09 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6957bfbd-819d-31da-bae6-2d39d09777cf | -3.58586 | -49.35155 | 2025-10-09 05:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36e3eda0-509b-3f7a-900e-6a0d9bdb2352 | -2.8807 | -50.73279 | 2025-10-09 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11a10a28-fe0f-363f-84cf-6f822f1e39b9 | -3.69904 | -49.57049 | 2025-10-09 05:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61baa796-5857-34ec-9b88-bd2a63ce3e1f | -12.15355 | -63.059 | 2025-10-09 05:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d663776-0a5c-363a-810b-47333a8a5c8a | -9.93751 | -64.76855 | 2025-10-09 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75ef59ef-17b9-3abc-b9f7-bae57c975bb4 | -12.39543 | -63.88159 | 2025-10-09 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08a4935f-5857-30bd-9dde-3c2f026df940 | -9.6832 | -67.45009 | 2025-10-09 05:40:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b2bcaf3-bede-30f1-af6a-de0d6c7551e2 | -12.39937 | -63.87847 | 2025-10-09 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 448c6f1b-3f63-3071-9fed-09d3519c36e9 | -9.79728 | -65.05585 | 2025-10-09 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccd2dd04-853e-3bae-81b6-6d669538dbb7 | -9.92501 | -66.76782 | 2025-10-09 05:40:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97443231-2203-3889-8a56-30f6481eb221 | -9.8168 | -65.01929 | 2025-10-09 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fb9d90d-7440-31b3-b390-10051fbd9973 | -10.27785 | -67.40651 | 2025-10-09 05:40:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f3672ba-5357-3362-a019-4f2765b22bd9 | -9.63299 | -64.87767 | 2025-10-09 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c0795d9-8f77-34f3-89eb-7df5b2f12add | -11.00193 | -62.64249 | 2025-10-09 05:40:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b802312-c98f-3276-8723-ffe4c190987e | -12.15298 | -63.06283 | 2025-10-09 05:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e44cddeb-cbea-363a-80a2-8aaeddc0eb07 | -10.14844 | -69.07196 | 2025-10-09 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f56b686f-319e-3fdd-93f5-ab2075bb9f85 | -9.62414 | -67.51656 | 2025-10-09 05:40:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83a882a7-8cb5-3c30-9f40-1025c79d81c0 | -10.05534 | -64.98898 | 2025-10-09 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1055343-a9c8-3773-a054-2b3af53c290c | -6.61996 | -62.87915 | 2025-10-09 05:40:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f43550d-894a-31dc-96d8-6a788fd3c5f6 | -10.16923 | -64.73727 | 2025-10-09 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c611447c-7851-3dca-8613-0524920fa94e | -9.57921 | -65.71381 | 2025-10-09 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8769e462-e4cc-3836-9433-a72a9f76f821 | -10.15127 | -64.25239 | 2025-10-09 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f4ceb2e-ac26-35e3-ad22-dca462c3fcf0 | -9.55338 | -67.86907 | 2025-10-09 05:40:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f80e761e-f9d3-375a-9d46-5835b5401a0d | -6.62331 | -62.87967 | 2025-10-09 05:40:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea5f45ef-aa46-3668-bac2-ff9eee1ac015 | -9.57979 | -65.71021 | 2025-10-09 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae206369-571a-3b18-8669-648d919a70b9 | -10.91033 | -68.25916 | 2025-10-09 05:40:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e20c0190-b9db-3b3f-8c2c-92e297e5b459 | -9.23522 | -65.74012 | 2025-10-09 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52609fd7-0122-3408-a728-0cb56ec47bc4 | -10.15182 | -64.24888 | 2025-10-09 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abad1e20-5167-3d6c-bc44-ed104f2e08f1 | -11.87304 | -62.76938 | 2025-10-09 05:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc29f61f-c2e9-3a5d-802c-883a16f0a82a | -9.68677 | -67.45072 | 2025-10-09 05:40:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 771435c1-8316-33a9-af32-f19a9ea8d2f3 | -12.39881 | -63.88213 | 2025-10-09 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da7810a2-4249-3890-bb8b-6b19ace3eeb1 | -9.62344 | -67.52071 | 2025-10-09 05:40:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ed7351c-e499-3062-90e6-8e14c5c782cd | -9.80672 | -64.48542 | 2025-10-09 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1af5caeb-3239-3d73-b191-7c0a841b2d11 | -9.85262 | -67.21082 | 2025-10-09 05:40:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a585cc7-e536-3280-83fe-2be9d8aeaa53 | -9.8034 | -64.48489 | 2025-10-09 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c92639e-1cb3-3fb1-90c6-d537de2b313c | -10.15515 | -64.24941 | 2025-10-09 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 195dcc7b-1574-3483-85ae-427cd7573e40 | -16.00465 | -59.54455 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee795164-9ac9-3dd4-b57a-ac96b8dfa593 | -14.94241 | -59.42113 | 2025-10-09 05:42:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4e6883d-93a9-3d6c-b07c-638f5d70ba47 | -17.83232 | -57.64325 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 396b35b4-c3b8-3315-936b-a3faf054301f | -17.84349 | -57.58972 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1f4594bf-82c1-3b7a-8b9b-adbdc077a79b | -17.85515 | -57.57895 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 840abb0c-bbed-3a71-8040-d92612d0b83a | -17.91171 | -57.5074 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 51e341ca-d97c-3c46-8957-9b0c55cfcf0a | -17.92562 | -57.52459 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2da5c537-e0e5-31b0-8068-64b1ab1fd2a2 | -17.84819 | -57.59444 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0fd2546e-6d1f-38cd-a209-3cff7839c3c8 | -17.92113 | -57.50618 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e7cd0759-d673-3c14-9cfb-bdf0a0ea3ad8 | -18.02626 | -57.56325 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ef6b5703-7a1a-3df5-a3da-eea4221d7736 | -17.82804 | -57.63486 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d659d68c-13df-31e1-a568-f5c5e4ec80f9 | -15.97822 | -59.54079 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1974e9d-ce77-304c-af38-ec94aafaaba9 | -17.82556 | -57.65723 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 56074ce6-e904-3a96-a27b-07000ef17e8e | -17.84727 | -57.64913 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f3c31fb5-11b1-3efe-b6ca-8283a3bcd4eb | -17.92444 | -57.52288 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 68d22c42-a223-3308-9925-2bf9213dc35b | -18.01256 | -57.49951 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| beef84f6-10d3-3340-9230-af7e5960db89 | -17.91635 | -57.502 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 9263ceb1-2c72-3aba-bb67-9f52feb4873e | -17.8493 | -57.58451 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 062b9c40-ad03-3693-b4e2-64a988bb0710 | -17.95963 | -57.50202 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 642084e1-9e9f-350c-a9ff-25860c52b8b0 | -15.97884 | -59.53912 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8180cd11-a825-3cf2-af86-13ada5980546 | -17.84313 | -57.59295 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1f05379a-e5a9-3e42-b56f-b38f471528c5 | -16.59977 | -58.16144 | 2025-10-09 05:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 0c35f08d-0d92-3869-b376-8cf46c7259e8 | -17.8475 | -57.60063 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d279ecd2-ca24-3581-89dc-aacb7ccc1655 | -17.82343 | -57.62944 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cfeed79a-3b85-3e2f-9431-668b7a974202 | -16.60464 | -58.16211 | 2025-10-09 05:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b4fc9028-cb18-3a02-a0fb-a6387f43b966 | -17.88775 | -57.65934 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 65a338c3-16ec-3cb6-8d79-73d598da4f74 | -17.91645 | -57.51221 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 2592da42-04ad-385a-9b2c-7b8a44e41a73 | -17.89764 | -57.66383 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 582d1054-9d5f-38f3-97dc-d507cf82e5d6 | -17.8289 | -57.62712 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b668db54-e8d2-3877-ab95-d3dd5a15ebb4 | -18.0593 | -57.55606 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0d62ead2-06d3-3407-885e-f45355c40138 | -17.92256 | -57.50425 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cf16686f-e6bb-3f93-9349-abfff975c7a7 | -17.84716 | -57.60367 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5638e43a-4370-35b7-9b52-a700a0f35b8e | -17.97519 | -57.50407 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b665d36c-3622-3606-9e09-5eb3f2268054 | -17.82062 | -57.6549 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 754c3e6d-637d-3142-b047-de3a3b44304d | -18.0609 | -57.5416 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3cb719fb-94c3-3c8d-ba87-e90aeb77ce2e | -17.92037 | -57.52456 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2984c930-b6df-3c3c-9a0c-f06f512eeb2f | -17.89252 | -57.66317 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f94843af-67c8-3749-9a05-e2533dcd1927 | -17.91733 | -57.50397 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| add95f91-ca04-3ba8-b72d-0a5a27391d0b | -15.97774 | -59.54458 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 703bb5d0-cacc-395a-9647-eb2683cda2b9 | -17.91252 | -57.49981 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| f80c9702-dc91-3102-a546-cefd17f32cbf | -17.82616 | -57.65181 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 704999a5-5730-3bfa-b2db-000c6da377aa | -18.05958 | -57.55352 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b82aa01b-484a-32ed-9ae6-98dab87cfdd3 | -17.84969 | -57.58108 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ce75b8d0-1316-31d6-b21c-ef2b1e424c8a | -18.00738 | -57.49875 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 729e5416-20db-32e7-a6aa-b023979fbab8 | -17.91543 | -57.50997 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 22c999f3-f076-3504-8dcf-12c6e0be2eb7 | -17.85254 | -57.60224 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d88c1c67-3d53-35a5-82c1-a502a5f8e0df | -16.02016 | -59.52832 | 2025-10-09 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54b86b9c-8b95-348a-ba88-8f819780e177 | -17.88228 | -57.6617 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 80480e46-2818-35d6-b971-d163a554a23d | -18.00773 | -57.49569 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 333cf8d6-6fbf-38c8-8edd-d8d7f746394c | -17.85213 | -57.65225 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5346c42c-586b-302c-95e0-9e55856d3e68 | -17.83749 | -57.64353 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 63411ae5-57f6-31df-9bf5-ca256985a7ae | -17.82034 | -57.65746 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7c0aa495-aeb7-3fbd-9d49-282c6eb9c798 | -18.0129 | -57.49654 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2674dee9-7208-3b55-b3db-acb7d67b326c | -17.81557 | -57.65353 | 2025-10-09 05:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |


[Clique aqui para ver as próximas entradas](README60.md)

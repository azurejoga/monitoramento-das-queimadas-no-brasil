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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29b3568a-6c18-3705-b2ae-10e6861ee9a7 | -8.9213 | -60.7489 | 2025-08-09 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 58b6dc88-6f5f-30ac-bc54-9147e6bda970 | -14.1103 | -45.4077 | 2025-08-09 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 242aba2a-2f56-3b72-baab-51342528710a | -8.9213 | -60.7489 | 2025-08-09 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| e89cf5c3-e915-3809-a363-965a9fdf283c | -14.4849 | -52.1086 | 2025-08-09 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 51130575-4468-3e80-a4ed-7869c9459df8 | -12.5902 | -47.1781 | 2025-08-09 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 90b53d5f-7340-334e-9fc5-c1e49d567db4 | -7.7202 | -45.5325 | 2025-08-09 12:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f28d53aa-0abc-3dfc-b056-2df3552ded47 | -14.1103 | -45.4077 | 2025-08-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| f07eebe0-7211-3017-8a48-8a15dd570447 | -14.4849 | -52.1086 | 2025-08-09 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 2b63da54-271d-3d5d-a3ef-084b64405953 | -8.9213 | -60.7489 | 2025-08-09 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 224d48ba-4952-3092-8e7f-60834c5d31ad | -8.9213 | -60.7489 | 2025-08-09 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| d31ffad4-8754-3169-83f8-4022de7ce4bf | -8.9399 | -60.7481 | 2025-08-09 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 4b8ecb65-4920-34df-9d81-3da849e57145 | -12.5902 | -47.1781 | 2025-08-09 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| b0909e6e-ffc7-3650-a016-ad710f1d1112 | -7.7202 | -45.5325 | 2025-08-09 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 40df144b-45fb-3d1b-ae3d-645a4ff51346 | -7.7014 | -45.5342 | 2025-08-09 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4a0180ff-0e1e-353a-947c-b2b1c6a7950f | -14.1103 | -45.4077 | 2025-08-09 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 74b22d1c-f3fd-3081-93b3-0b0052f3433b | -14.4849 | -52.1086 | 2025-08-09 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 252.7 |
| dfc2b08c-ebae-3f19-9114-d0c1342091d0 | -14.4849 | -52.1086 | 2025-08-09 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 8ea6a7bb-9de7-3514-b5d7-5930a0c6898c | -14.1103 | -45.4077 | 2025-08-09 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| ca21d254-a7a4-3c7e-9792-4664182140fb | -12.5902 | -47.1781 | 2025-08-09 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| a43ff2d8-9c0c-3e7a-baf0-4a6929ab2a1d | -12.5906 | -47.1556 | 2025-08-09 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f7bffcc7-c143-314f-8895-4ceba89368c8 | -12.5902 | -47.1781 | 2025-08-09 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 210e0fc3-3f69-30bc-a63c-abbd1a97b430 | -14.4849 | -52.1086 | 2025-08-09 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 177.5 |
| e41e3f8d-1147-31a2-a256-579e353a7ea3 | -12.5906 | -47.1556 | 2025-08-09 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 09c69674-7a34-38a3-ab01-f25c63392ed3 | -12.6595 | -44.4882 | 2025-08-09 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 4043fb60-ac8f-34a3-929b-98f6e868b547 | -14.1103 | -45.4077 | 2025-08-09 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 1e3a254d-b6b5-37d3-b6d9-9456ba463045 | -7.5829 | -44.405 | 2025-08-09 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| b3ab05eb-e8d9-3e87-9dbc-69c2689f4d15 | -8.7822 | -46.4174 | 2025-08-09 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ff189b91-3cfc-37f2-88ae-fe764ee6b758 | -12.0293 | -47.5026 | 2025-08-09 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 4861b097-e8ae-3d52-84cd-b6220eff59d7 | -12.6595 | -44.4882 | 2025-08-09 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| d8fbd0e4-ac5e-33d3-bf2f-337d545a0fd1 | -12.5902 | -47.1781 | 2025-08-09 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 6ddca18e-1aea-3f9a-b0e4-4238d8684115 | -12.0484 | -47.5 | 2025-08-09 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f7b615d8-a02b-38d5-93b2-faa0edbe5617 | -12.5906 | -47.1556 | 2025-08-09 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 346b0c34-a191-3769-b749-30fec12a8935 | -14.1103 | -45.4077 | 2025-08-09 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| fd18dfc3-0f5e-32cb-9d92-4bb4b0dc578a | -14.4849 | -52.1086 | 2025-08-09 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 90c62f69-ec84-31e0-b6dc-de8e0b8e1a72 | -7.5829 | -44.405 | 2025-08-09 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 97aaf8a3-6725-3d4e-8640-86a7a5f6f9c4 | -8.5086 | -45.7033 | 2025-08-09 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d56ffa9c-15aa-37a5-95be-88552fa82a81 | -7.5829 | -44.405 | 2025-08-09 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 222.4 |
| 7df47607-2ea8-3b81-b6a8-86ba65d04296 | -12.0481 | -47.5224 | 2025-08-09 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4e4262c2-41f6-3a8f-839c-a0dbf9579acb | -14.4849 | -52.1086 | 2025-08-09 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b684a4a2-d187-3e2a-8cfa-852d850af4c3 | -7.5826 | -44.428 | 2025-08-09 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 25a6e6cb-33e5-3cbe-8403-fec685b7ec53 | -8.7822 | -46.4174 | 2025-08-09 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a7cd369d-c2e4-3f09-a5f2-ccaa9fccd83c | -12.0293 | -47.5026 | 2025-08-09 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 2854be2e-a883-3cf0-a7ee-74c3a2f50364 | -12.6595 | -44.4882 | 2025-08-09 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 69b0a7a5-5bf6-399e-90f0-4214cb62dbcc | -12.5902 | -47.1781 | 2025-08-09 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 3ab31ff5-679f-3e52-88b4-f1c132a4f023 | -12.0289 | -47.525 | 2025-08-09 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| c8396fdd-3031-3390-bc5f-9dd2c106c352 | -12.5906 | -47.1556 | 2025-08-09 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| aa698ae9-9fad-3fc7-82c2-76c78f321444 | -12.0484 | -47.5 | 2025-08-09 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 7313f261-6451-3e29-badc-b09879190f61 | -12.0293 | -47.5026 | 2025-08-09 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 763d4be4-9519-322e-a906-91d647b3a2c1 | -12.6595 | -44.4882 | 2025-08-09 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 1599ab94-cb5d-38d4-ae7a-3b1639879026 | -7.5829 | -44.405 | 2025-08-09 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 352.8 |
| 78b5d075-cc54-396f-bd5d-61bd8888f3b3 | -12.0484 | -47.5 | 2025-08-09 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ae80dc7c-c123-3557-893b-15c0d96c5d9b | -12.5906 | -47.1556 | 2025-08-09 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| b7027503-6f45-35f6-a24c-8c53fb804396 | -14.4849 | -52.1086 | 2025-08-09 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| fd51adf6-a650-33de-8af1-40679a60cb56 | -12.0289 | -47.525 | 2025-08-09 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 82e1850c-74d7-3495-9b82-b9e5e9f2b6fb | -8.7822 | -46.4174 | 2025-08-09 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 40ea944b-7733-3125-b340-dd0718de1558 | -7.5641 | -44.4068 | 2025-08-09 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1d3673ea-52f8-37b9-ad2e-90340198eda5 | -12.5902 | -47.1781 | 2025-08-09 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 6bcf24dd-2fa7-358e-87e5-251bae46e487 | -7.5826 | -44.428 | 2025-08-09 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 40f6114d-baf2-39f4-9b69-1c7c5fd8b267 | -12.0293 | -47.5026 | 2025-08-09 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d738b2b7-0f73-30ed-8101-63a915a03068 | -14.1103 | -45.4077 | 2025-08-09 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 23163e8d-b2e4-34f8-8211-904a05bb808c | -8.7634 | -46.4194 | 2025-08-09 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f89644af-060f-3059-8a9c-86f24ec59613 | -12.0289 | -47.525 | 2025-08-09 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8d433f6a-5499-3bb7-8874-2c1d4e51c347 | -12.0481 | -47.5224 | 2025-08-09 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 2b14e067-763f-30ff-9edd-061650152109 | -12.6595 | -44.4882 | 2025-08-09 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 1a65f15e-f097-3b26-99d8-29c6e20bcd87 | -7.5829 | -44.405 | 2025-08-09 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 274.9 |
| 8c861b12-4dbb-349e-830c-b20f0756db30 | -5.4165 | -41.2266 | 2025-08-09 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 6ff53d69-6135-3b01-98e4-337c73416d57 | -7.5826 | -44.428 | 2025-08-09 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 00f8c90c-a725-311f-bfcc-9657c94a6229 | -12.5906 | -47.1556 | 2025-08-09 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 422416e7-c45e-37bd-9b12-27ac4ec03a6b | -12.0484 | -47.5 | 2025-08-09 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| ca77482f-b220-3787-be81-1cb3a52fcca3 | -14.4849 | -52.1086 | 2025-08-09 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 8c650f23-6193-3c6f-8e93-cbd09985ca7a | -7.7202 | -45.5325 | 2025-08-09 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 64966fdc-7a48-3f33-b5e0-d12bb9c28ca2 | -8.7822 | -46.4174 | 2025-08-09 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 557ea91f-f759-3775-a80a-23a01aa43882 | -5.4353 | -41.2251 | 2025-08-09 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 273fe2dc-ef1d-36c4-8f86-bc9fc6100d17 | -8.7634 | -46.4194 | 2025-08-09 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 0b935b03-939a-3a43-aac8-417464d31eaa | -14.466 | -52.0899 | 2025-08-09 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| f9df44d7-e69c-3762-831f-022bafff013b | -7.5826 | -44.428 | 2025-08-09 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 91c588fe-7dbd-3feb-9553-225eaff2a3a2 | -12.5722 | -47.1134 | 2025-08-09 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a6b0cd5c-8b88-333c-b77b-1059523272d0 | -6.9873 | -43.8606 | 2025-08-09 13:50:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a4745213-9b5e-3e50-b781-a6d564834444 | -5.4353 | -41.2251 | 2025-08-09 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 116.3 |
| 7c115b54-eb85-3ca0-87da-b638ef8295ca | -5.4165 | -41.2266 | 2025-08-09 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| bf1976df-5c2c-3aef-8ede-9446b5c9d0a6 | -12.5902 | -47.1781 | 2025-08-09 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| df564ab5-022e-30b0-851c-ecba697ccc51 | -12.0289 | -47.525 | 2025-08-09 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c07aae66-9150-35c1-9395-43b2bb55851b | -14.1103 | -45.4077 | 2025-08-09 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 960374de-8393-3266-a700-30e9ef76e36d | -7.5829 | -44.405 | 2025-08-09 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 3ee78dd2-b36e-3179-90c2-486640fd4160 | -14.4849 | -52.1086 | 2025-08-09 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 2612ba8c-4fac-38e1-a31c-8dc7cca645a8 | -7.7202 | -45.5325 | 2025-08-09 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 29944507-32ab-3452-a9ce-ac5353c5ca4e | -7.4835 | -44.8729 | 2025-08-09 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3be2f15b-b63f-30c5-b45a-6148797be117 | -7.7205 | -45.5098 | 2025-08-09 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| bee8a874-e0f3-3e53-bdb3-10b4f8708eda | -8.7822 | -46.4174 | 2025-08-09 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| b189f73e-13cc-3ce0-9847-cc5896a75795 | -12.0293 | -47.5026 | 2025-08-09 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 7d2fbe2b-864e-3c3b-9ebb-46b8df6256c9 | -9.4822 | -46.2971 | 2025-08-09 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e1383250-2d6f-39c2-b6b0-1bf34af79c2c | -12.0484 | -47.5 | 2025-08-09 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 24d13e78-73cf-3712-817f-04e6c663c192 | -12.5906 | -47.1556 | 2025-08-09 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 760293ee-29f9-3cdb-a2e1-e85abb8a4b16 | -12.6595 | -44.4882 | 2025-08-09 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 283.3 |
| f63cf677-4d7f-3e19-a6de-23da54251e94 | -12.5137 | -47.1667 | 2025-08-09 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 47ffe8bf-5b02-33fd-a25a-124d83ccd803 | -12.0293 | -47.5026 | 2025-08-09 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| c88dbf3b-434f-32e1-98ba-219857b5ca21 | -12.5906 | -47.1556 | 2025-08-09 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| bd846823-19ac-3c6a-9999-dce0b96bd910 | -12.0289 | -47.525 | 2025-08-09 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c60414f9-26fe-3371-9ce5-47d03f800cb9 | -14.6175 | -47.1551 | 2025-08-09 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 107ea7ae-3600-39f7-aeb5-7a860d596478 | -7.7014 | -45.5342 | 2025-08-09 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |


[Clique aqui para ver as próximas entradas](README33.md)

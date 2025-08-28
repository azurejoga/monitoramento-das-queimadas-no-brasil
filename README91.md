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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39ff3904-9809-3ca3-8259-a08fb1504acf | -9.1155 | -65.7699 | 2025-08-28 12:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 56aec906-07c7-35b2-9f73-2a0c1a3d4fc1 | -9.1339 | -65.788 | 2025-08-28 12:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| cdf550fe-1e7e-3891-9a63-0d5b864b166f | -9.1154 | -65.7886 | 2025-08-28 12:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 281.3 |
| 0a057b09-d6ab-3a00-ab5f-e26d60e92f67 | -6.1593 | -44.0703 | 2025-08-28 12:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 77321ff3-9ae5-33b7-bead-858cdd616cfc | -6.1595 | -44.0472 | 2025-08-28 12:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 179.4 |
| ba204226-47e9-3c7b-8066-fc47c09f59b4 | -9.9712 | -46.5106 | 2025-08-28 12:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e43b5ac5-7f8e-3778-9b22-403fdf9840a0 | -9.2632 | -65.8959 | 2025-08-28 12:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 499f0b36-11a3-36aa-8073-56f24787106d | -6.1593 | -44.0703 | 2025-08-28 12:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 8819ff5b-6cb9-3518-9f70-1855d351fa4c | -13.7373 | -51.9077 | 2025-08-28 12:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| ee2bef69-b409-331f-a175-c8bcba1ead75 | -9.1154 | -65.7886 | 2025-08-28 12:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 442.5 |
| f042bc80-9a54-3abb-b11b-a61bdadf89a2 | -11.5703 | -46.3978 | 2025-08-28 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 9c7be185-c9b9-3076-a2e3-59b309b47bcd | -11.3521 | -43.5423 | 2025-08-28 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 9016c2d8-e4da-3abf-b483-e281e2a9a383 | -6.8772 | -43.6152 | 2025-08-28 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 152fee03-7ad2-3ab7-89d3-c4b34a2073ff | -9.1339 | -65.788 | 2025-08-28 12:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| a117f401-eb03-3f8e-8c1d-45233b036a4a | -11.5699 | -46.4205 | 2025-08-28 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b5bf92e2-f71d-3278-976a-c5216aaa0a7b | -11.5894 | -46.3952 | 2025-08-28 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 89323a10-927a-3daf-8cfe-021b18256e2d | -6.4543 | -44.5749 | 2025-08-28 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 2df68154-e826-328d-9cfa-b2f30228f6fa | -9.1155 | -65.7699 | 2025-08-28 12:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 3d080b6e-12df-3e0c-a975-26ed703e76d1 | -13.5576 | -46.8972 | 2025-08-28 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| e275eba1-e576-3117-9aa8-6fd095bf1cb7 | -6.1595 | -44.0472 | 2025-08-28 12:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 244.3 |
| 8e777e4e-9bbc-3a8f-8e2d-ba3de8b2288b | -6.8769 | -43.6385 | 2025-08-28 12:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e6c299ce-4431-3bdf-9aa9-3e4bb3654a69 | -9.1154 | -65.7886 | 2025-08-28 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 572.4 |
| a5d4433d-bdc7-3a26-ad23-363899018eca | -12.8224 | -48.1489 | 2025-08-28 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 45479ca8-1600-3b25-b207-1448190741a6 | -11.5703 | -46.3978 | 2025-08-28 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 253.5 |
| fa00f194-1820-320d-bd50-37abe5e9f86d | -6.4355 | -44.5764 | 2025-08-28 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 23c1f0f1-a2fd-39fb-907c-75ccc7be58e0 | -12.8228 | -48.1267 | 2025-08-28 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 0c636dbb-62c3-35b5-a078-cefdf490468b | -6.1593 | -44.0703 | 2025-08-28 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 49ec68d1-74d5-39c8-8e43-dfb1117c2ece | -6.4543 | -44.5749 | 2025-08-28 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 88d3dafb-57fb-3cdf-8b55-d2a49c279a0d | -9.1339 | -65.788 | 2025-08-28 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 2d5a29e3-6831-385e-8436-b0c7c7a49c7a | -11.3521 | -43.5423 | 2025-08-28 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 4e495e0a-dfda-3443-8416-6ab95c5e6f25 | -9.2632 | -65.8959 | 2025-08-28 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| eb2344d6-1bad-3f95-971a-566480218752 | -11.5894 | -46.3952 | 2025-08-28 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| d09f7690-24f7-3f18-801d-0fd31f83cd54 | -11.5699 | -46.4205 | 2025-08-28 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| b6215dd0-8ba7-30ab-ac91-4a2bd4fffbec | -6.8772 | -43.6152 | 2025-08-28 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 0dce7b63-582a-3924-a22f-4667a1152d20 | -9.1155 | -65.7699 | 2025-08-28 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 31c58568-484c-3a35-9027-454df9de1c0a | -6.8769 | -43.6385 | 2025-08-28 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 999626ca-a330-3214-8af1-7cdd08f45347 | -9.134 | -65.7694 | 2025-08-28 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e9f26cd5-22e8-3b36-b294-4b55762bc8b4 | -6.1595 | -44.0472 | 2025-08-28 12:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 447b3ed7-bc4b-3887-a467-b5f4c6cf959e | -6.8583 | -43.6169 | 2025-08-28 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c5d4b5db-d5d2-3591-be3a-4b87c2f7c7f4 | -6.8769 | -43.6385 | 2025-08-28 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 245f1663-1e8c-3d6d-9921-0cf6c72ba5c1 | -9.1155 | -65.7699 | 2025-08-28 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 215.7 |
| 263e4f39-8ffb-3f3f-a823-cd8f69781fd3 | -9.1153 | -65.8073 | 2025-08-28 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 8772b198-736d-3a3c-92db-6564dea47db8 | -9.2632 | -65.8959 | 2025-08-28 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 6f9a422d-8647-3735-91aa-3154f5749aa5 | -12.6878 | -48.1677 | 2025-08-28 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| dd0c5b4b-4223-3936-908e-42129ab6197a | -6.4355 | -44.5764 | 2025-08-28 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5f4ebdcf-9980-3feb-98b4-804b3d85bf4e | -12.5125 | -47.2342 | 2025-08-28 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d1d08603-31a0-3bb3-8547-308de30ea9de | -11.3329 | -43.5452 | 2025-08-28 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b77aa84e-e4c4-3b74-9c3d-1b53c1c55980 | -11.5699 | -46.4205 | 2025-08-28 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 76bacf61-265f-3499-92c7-2321c8b0ec60 | -11.1523 | -54.3104 | 2025-08-28 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b82951fe-f4e9-32cd-89e1-55a0a669e978 | -11.5894 | -46.3952 | 2025-08-28 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7efc7bb5-fd4e-3473-badd-d16acd140a0d | -9.134 | -65.7694 | 2025-08-28 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 21195ef2-4f81-30ed-b028-c74d36a41f69 | -6.8772 | -43.6152 | 2025-08-28 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 161.3 |
| ddfd46b0-e85d-3feb-8aa4-5d5e54c95429 | -6.1595 | -44.0472 | 2025-08-28 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 244.2 |
| 2edb7393-703e-35ed-a45c-3958b4f32ed9 | -9.1339 | -65.788 | 2025-08-28 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 328.2 |
| 92f9cb4e-bd2f-375a-9abd-734c09a673ed | -12.8224 | -48.1489 | 2025-08-28 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 0ff6427f-090e-3bdc-bba1-c10b23f8d9a1 | -11.5703 | -46.3978 | 2025-08-28 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 16850640-242c-30cc-8490-d066d038fc0e | -6.1593 | -44.0703 | 2025-08-28 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 0de14a14-d08b-386b-9187-448e68dc32ac | -9.1154 | -65.7886 | 2025-08-28 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 670.7 |
| 8f964068-3dd5-3f0e-9577-7ea1fd9b0267 | -11.3521 | -43.5423 | 2025-08-28 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 714d78d9-8bf3-30f8-8d3e-1422c01d272e | -5.8133 | -44.78267 | 2025-08-28 12:34:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e61d4756-d7d2-331a-b6ed-dba538a28acb | -4.79153 | -48.72311 | 2025-08-28 12:34:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2c7a2c2e-597e-3fb8-8e1a-bc2a26aca322 | -6.87958 | -43.63091 | 2025-08-28 12:34:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 981bee11-4db8-32f0-9094-2f571ae763a7 | -11.56404 | -47.60815 | 2025-08-28 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 8cb699e3-6040-3518-9055-2dbe181e5125 | -6.43304 | -44.56375 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5e36081b-c762-3006-923b-b5c585c7815b | -9.45138 | -48.31234 | 2025-08-28 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| f9348e82-361d-37ce-a2aa-39643eb037d8 | -9.68695 | -47.05912 | 2025-08-28 12:34:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b8aadb77-6d76-3693-b24c-bba0efcbcd11 | -8.2736 | -45.15994 | 2025-08-28 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 511b1ef5-6f3a-3ddc-bac9-25785604a9ee | -6.08744 | -43.9987 | 2025-08-28 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 56d66ddf-a7bd-367a-a2c3-e0ad3f2f3c10 | -8.55381 | -45.788 | 2025-08-28 12:34:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f73d1a8f-29f5-39c5-ade2-a82f33841b01 | -6.44069 | -44.57697 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e9d3ccbc-6066-34c9-913d-19158757135e | -9.78938 | -45.70744 | 2025-08-28 12:34:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| aca27f6a-7832-363b-adfb-f95d4648a54f | -10.38014 | -45.15797 | 2025-08-28 12:34:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 0651321d-db6b-3fb6-b7c3-40a914b6db79 | -9.64569 | -45.58942 | 2025-08-28 12:34:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 80814a4e-51b4-3410-8fe2-0971f42ee4ee | -12.09074 | -44.7153 | 2025-08-28 12:34:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 41693bd7-7bb6-393a-9e76-3513a021a7c9 | -12.09914 | -44.72308 | 2025-08-28 12:34:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| bf30d0f9-e7ea-3c36-aa1f-3889815c4129 | -4.8145 | -43.24953 | 2025-08-28 12:34:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 3fd12c46-b916-3bde-b583-b1fd93d6f23b | -7.04185 | -45.88132 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1edadb8b-2672-37c9-88df-9090995c43c6 | -6.08735 | -44.69533 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| b8ea5362-0f35-319f-a3ef-5875a15bdec9 | -7.00426 | -44.37774 | 2025-08-28 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| fff3aff8-90b5-3530-b550-329e127ecf91 | -6.39262 | -45.59533 | 2025-08-28 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| f375f3e0-2bc8-34f5-b6da-598a7fe8f221 | -6.88242 | -43.60896 | 2025-08-28 12:34:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| c625c40c-a8ea-34fa-9f4d-8cc7c3aba435 | -5.81557 | -44.76574 | 2025-08-28 12:34:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 316c90a1-f5d0-360c-99c3-7ea4c7880283 | -5.83269 | -46.35632 | 2025-08-28 12:34:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fc34fb0b-2f32-3851-860c-8b87bac90e3b | -9.68129 | -47.06614 | 2025-08-28 12:34:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 057ed994-d399-3685-9d07-9944f1330a39 | -10.08774 | -46.6035 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3b169946-aa0a-3a2d-b5fe-667b693ffdc2 | -11.93132 | -46.69995 | 2025-08-28 12:34:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e9c84ec6-3e88-3146-b8f2-6ebaeaf338d7 | -11.35277 | -43.56033 | 2025-08-28 12:34:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| fcb387ae-dc6c-3cad-957f-f0a7bea433a2 | -6.4432 | -44.55862 | 2025-08-28 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 0cbfcd2d-6bbf-32a6-a80d-f65f1393470a | -6.1609 | -44.03474 | 2025-08-28 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 8f764452-3511-3940-ab06-d0d63717da15 | -10.53675 | -46.6759 | 2025-08-28 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 54d040d5-cc8b-3b1d-9f45-043e0a1816cd | -4.96931 | -43.14596 | 2025-08-28 12:34:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| bdf75320-b9b1-3998-b8bc-5a1ef6cf7f0b | -9.45285 | -48.3014 | 2025-08-28 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 48655241-ca32-31a3-93c2-c8f1c4dfd8a2 | -11.56929 | -46.39207 | 2025-08-28 12:34:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| c1076c49-ae8a-35c2-90f0-add1d710e34f | -12.08802 | -44.73736 | 2025-08-28 12:34:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| be62f169-04a8-31ce-9581-58e80e0c2cef | -11.34133 | -43.53154 | 2025-08-28 12:34:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d1d8de0c-c907-3417-bdaa-a9bc0472a5dc | -11.55969 | -46.37449 | 2025-08-28 12:34:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b81284eb-539c-3ac2-9189-ac28daedfa45 | -11.57294 | -47.62246 | 2025-08-28 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ab511646-60de-3bbd-9cea-4845ffb454f7 | -4.80061 | -48.72436 | 2025-08-28 12:34:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 33527d92-6fb8-3077-9ae9-09de325e286c | -10.10862 | -46.53136 | 2025-08-28 12:34:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| dac1c33f-555b-302d-b4ac-300aba5fc7fc | -8.08714 | -44.99634 | 2025-08-28 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |


[Clique aqui para ver as próximas entradas](README92.md)

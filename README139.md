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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe0b515e-13d9-33ab-b2ad-e3685d6d31e8 | 1.52152 | -55.82984 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34421a0b-58d3-3d8c-a2ea-520c9b9a814a | 1.74775 | -55.86321 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9430bdc7-3673-3038-9089-3ce242147eb7 | 1.78522 | -55.82188 | 2025-10-03 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04b34ac3-a4d4-3631-917c-7b34ee5b93c7 | 1.52262 | -55.83668 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22ba01b0-c6e4-33f4-ba29-f3d0f8fb735c | -1.07878 | -53.68005 | 2025-10-03 05:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4597ffe4-c465-30d1-99f4-0ade21023d82 | 1.52098 | -55.82644 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03ed23d0-51b7-3271-9486-9e3fe3b1469b | 2.71302 | -60.18787 | 2025-10-03 05:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b7e3b41-67aa-34b9-bcee-31d4bbab84ed | 1.52207 | -55.83326 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d37312c3-c17e-3045-b872-50697fcfee04 | 1.52372 | -55.84351 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a3ef471-d6f4-3343-880b-85f0e148be88 | -3.68598 | -64.4465 | 2025-10-03 05:50:00 | NPP-375D | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a5cfe05-b703-350d-912f-e18cef36a6a2 | 1.75313 | -55.86224 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 893cd7a5-98d3-389d-b5d9-5b85b2e999e8 | -1.08531 | -53.68073 | 2025-10-03 05:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f7f31b17-9cc3-3aa2-ae2a-ddb698e991b9 | 1.51935 | -55.81633 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93a5aebf-0e1c-3b53-a3ad-7e59fed29cdb | 1.52043 | -55.82305 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f064668f-53d2-3747-8869-a826a8134595 | -1.08446 | -53.68624 | 2025-10-03 05:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82366866-f42d-366a-b909-d5f510a4a180 | 1.78578 | -55.82525 | 2025-10-03 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 983451df-ed84-36eb-8153-c68445ef7f05 | 1.52317 | -55.8401 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a0c66a2-1a8b-3799-8cdd-cc8954aa95d3 | -3.68541 | -64.4502 | 2025-10-03 05:50:00 | NPP-375D | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 867b457a-f0da-3b9f-a7c1-aba790942df8 | 1.79006 | -55.81755 | 2025-10-03 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d526b11e-e018-33e0-8562-3d78f834af4f | 1.52426 | -55.84692 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48d1e24a-dee6-391f-9a58-5b4270b3ad02 | 1.51989 | -55.81967 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b79cad67-f7db-30c5-9076-a4a7053c88a8 | -9.28347 | -60.53929 | 2025-10-03 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 014a6fe0-c06f-3968-b6b6-8b20c6a1804a | -16.16625 | -57.59586 | 2025-10-03 05:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8240878b-7740-37bc-bb1f-1f3fa037516c | -16.17192 | -57.59372 | 2025-10-03 05:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 14cd5cb3-5600-3d40-93a1-7c606d879e19 | -16.1658 | -57.59235 | 2025-10-03 05:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 12f003e6-148f-33f1-9d10-63698fe6aeb0 | -9.98412 | -57.82306 | 2025-10-03 05:53:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13b597e5-9625-3432-85b5-e3a38f834c95 | -16.16618 | -57.58865 | 2025-10-03 05:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fdf34371-4ae4-34ce-acba-481a09933d35 | -16.16665 | -57.59214 | 2025-10-03 05:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9489bab5-892e-3d49-83c9-67b7cd1d4324 | -10.70471 | -59.19527 | 2025-10-03 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad55cbad-9c84-3dda-87c4-4d3352da0115 | -9.61604 | -57.87671 | 2025-10-03 05:53:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2e39c96-fea8-304e-b484-d604277164b1 | -9.93528 | -59.80578 | 2025-10-03 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff96ac16-8d50-3fb0-b4c5-342eadddd342 | -9.98975 | -57.82384 | 2025-10-03 05:53:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0d01aec-9325-3ddf-95b2-03b7be085457 | -16.17764 | -57.59895 | 2025-10-03 05:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3b1a71e6-5300-3036-96a0-646a2886df80 | 4.55735 | -60.7066 | 2025-10-03 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 19e9b360-1bf5-3621-beaa-1eec765cd58d | 4.55329 | -60.70572 | 2025-10-03 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8dc70ee-c3f3-38eb-85eb-bf3a77f1fb2d | 4.5539 | -60.70934 | 2025-10-03 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 676065fc-4af1-3d4e-b6c0-6dc96f700ed0 | 4.55175 | -60.7076 | 2025-10-03 06:10:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 174fb951-cbdf-3eab-9ed9-e9341f3ec6ec | -3.33439 | -52.04927 | 2025-10-03 06:31:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 69724260-a4c7-3f2c-899c-051622b3d74d | -1.08602 | -53.67944 | 2025-10-03 06:31:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7e3d3888-225f-3914-bc67-4b3b7da60867 | -3.0975 | -47.01629 | 2025-10-03 06:31:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| fa50052e-b1af-343b-8630-e383349f5129 | -6.23564 | -45.34332 | 2025-10-03 06:31:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 004e2fab-f007-3643-8e26-84e182c1270e | -2.24637 | -47.88448 | 2025-10-03 06:31:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 8c42bb6c-9eed-33b5-bb48-bd400f6aad87 | -6.23785 | -45.3513 | 2025-10-03 06:31:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c77ee438-b1e3-3374-80ea-139f059a81b6 | -1.0772 | -53.67818 | 2025-10-03 06:31:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d3fbf5e9-455d-3398-adb5-e7e85ff3ea22 | 1.51871 | -55.81892 | 2025-10-03 06:31:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 935d1058-1604-34b4-a96b-57842f909315 | -2.24937 | -47.86332 | 2025-10-03 06:31:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 16544820-20a8-347a-ab21-ce909538929d | -2.24984 | -47.87771 | 2025-10-03 06:31:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 3bb8b423-8674-3c12-9ef0-7a27d42b9265 | -1.08735 | -53.67062 | 2025-10-03 06:31:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e7a53086-f084-38dd-825e-dbe1cb39fa18 | -2.9213 | -48.29877 | 2025-10-03 06:31:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 016cb228-2cc3-33d9-b0ed-9360266112c1 | 1.52169 | -55.83857 | 2025-10-03 06:31:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 637ebc4b-1abe-31a8-ac61-8cbcca34d527 | -11.09115 | -47.84925 | 2025-10-03 06:33:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 07c88e62-b5fa-3616-b994-b6e17e593e76 | -9.91457 | -50.49208 | 2025-10-03 06:33:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| aa428c3a-e463-3d65-9582-6fe8d0ff2d5b | -8.60964 | -54.96935 | 2025-10-03 06:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d026a5e1-963e-319e-9e20-d25d5a7417cd | -10.61202 | -48.68795 | 2025-10-03 06:33:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e7aed3af-c9bc-388a-8358-1ff7d31df085 | -11.91762 | -46.25914 | 2025-10-03 06:33:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 30724eb8-a157-3b3a-a496-b5ba2d849a4a | -11.11977 | -47.85722 | 2025-10-03 06:33:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 014f2218-85e1-30c2-8913-c7bba2a9e6c8 | -11.08927 | -47.85368 | 2025-10-03 06:33:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 3004a6b6-899d-3bb3-ab49-2b8346c91f28 | -12.75564 | -50.56415 | 2025-10-03 06:33:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| ff172a81-6b9f-337d-8d59-b44c32f3a0f6 | -10.93059 | -46.71696 | 2025-10-03 06:33:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| ed012f75-0354-3fb1-bb0a-4d30ca2d9e15 | -12.61325 | -46.98243 | 2025-10-03 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 240.5 |
| dee6922b-3b30-346a-8e8e-00e5bf2c7db5 | -10.58992 | -48.70641 | 2025-10-03 06:33:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 280d66f7-7ac0-35d6-b5c1-26c57956ddae | -10.60904 | -48.71286 | 2025-10-03 06:33:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 153.0 |
| a4ecb07f-85a9-36dd-8b07-5408b0ba067c | -11.11802 | -47.88146 | 2025-10-03 06:33:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| e1019642-0c66-3fdf-9994-cb52db725243 | -13.11724 | -47.8833 | 2025-10-03 06:33:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 47d68bb5-d2ad-3382-95a7-9063570cdbaf | -8.62476 | -54.99008 | 2025-10-03 06:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ae0a3dc-d414-3885-ab2a-ce0daedcdb42 | -7.00486 | -47.17345 | 2025-10-03 06:33:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 3746c2e7-fb9b-3f51-af0e-fc78ddf0b598 | -11.91283 | -46.30025 | 2025-10-03 06:33:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 736.9 |
| 0f91cd5f-bec8-3137-958b-13d77a182729 | -7.7062 | -46.2043 | 2025-10-03 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| c6e2b543-00ac-382f-a807-6be61b144ae6 | -12.6299 | -46.98419 | 2025-10-03 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| f1602804-3206-3834-842a-9441e9ee313b | -7.00404 | -47.1781 | 2025-10-03 06:33:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9f37febe-4b8a-3262-aa17-138a4f876024 | -13.12123 | -47.85006 | 2025-10-03 06:33:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| b0d2beac-c2b7-3dbf-82a4-96b4e7de6c5f | -12.63408 | -46.94777 | 2025-10-03 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 8c6eae25-a829-30e2-b51c-a9b571cd226d | -7.76712 | -46.24809 | 2025-10-03 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| e275b333-65aa-3e02-aaab-d5760eb3f2ea | -10.97043 | -51.05869 | 2025-10-03 06:33:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1d0b6456-d4fd-3700-acd7-0e370879042c | -7.75052 | -46.24784 | 2025-10-03 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 91c3f3f7-5562-3ed3-8842-2ac049d0cd97 | -10.8942 | -56.19934 | 2025-10-03 06:33:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 300bf374-66aa-3ae4-af12-c19d95f33c6b | -11.1217 | -47.85242 | 2025-10-03 06:33:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 96b3ae20-4b4e-3d0f-9bec-ea1d8db2b465 | -10.01699 | -50.21854 | 2025-10-03 06:33:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c920300c-a951-3309-90e5-a632167cf02a | -10.94212 | -46.71066 | 2025-10-03 06:33:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 89f0a1e3-b356-3f45-81d4-0e866f40f4c0 | -10.96831 | -51.07521 | 2025-10-03 06:33:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8cfd8b61-dda7-31c8-8a2d-ad7ccbaaa9e8 | -7.76245 | -46.28343 | 2025-10-03 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 91e40f7c-23f7-3c61-be7a-b36e9ab18381 | -11.5544 | -47.65376 | 2025-10-03 06:33:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 4cfd5fdb-00a0-30ff-bc29-f67b7e1e3352 | -11.91412 | -46.30718 | 2025-10-03 06:33:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 566.9 |
| 657b251e-ca00-3621-864e-7872e2f74904 | -10.00461 | -50.21692 | 2025-10-03 06:33:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 4d11da5b-18ae-3686-8ddb-16e5d03f52c8 | -8.6261 | -54.98101 | 2025-10-03 06:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e7a152b7-8b6d-3df6-9e77-e7683db9caf6 | -7.76131 | -46.21807 | 2025-10-03 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 13e207f5-3672-3f76-935b-0e847389ce41 | -11.90823 | -46.33968 | 2025-10-03 06:33:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 2017b01c-fdf2-362a-bc91-e5bdf473bfce | -11.54903 | -47.66037 | 2025-10-03 06:33:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 4c10603f-3c08-3bf7-9f54-c42387f22ed6 | -11.89645 | -46.30866 | 2025-10-03 06:33:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 04942bf9-cfba-339b-b227-f57ab9cb838b | -10.60738 | -48.68195 | 2025-10-03 06:33:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 86b01445-6db3-38e8-bbad-a210f5b77922 | -12.75814 | -50.54469 | 2025-10-03 06:33:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4db62657-5a56-3fe5-aca7-f97a42702ce8 | -11.08756 | -47.87823 | 2025-10-03 06:33:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| f2efed5e-89dc-301a-b9a7-78f932bda2fa | -12.61946 | -46.98774 | 2025-10-03 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 200.9 |
| e41c9485-2034-30b2-a14b-0039058e900f | -11.91857 | -46.26668 | 2025-10-03 06:33:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 4eb5112d-0a71-3648-a633-1892c3248cd1 | -7.75656 | -46.25637 | 2025-10-03 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 172.1 |
| ef29c3d6-40ea-369f-9ab6-0bc8e470a4a1 | -12.61741 | -46.94582 | 2025-10-03 06:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f35a24a7-38a9-3326-a54d-b802b229ea6f | -10.9735 | -51.06903 | 2025-10-03 06:33:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8f43e926-73cd-33be-b746-3643cba1e150 | -10.60418 | -48.70718 | 2025-10-03 06:33:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 263.6 |
| e80cbbeb-6a46-3fd2-87b7-4b37375c2e8d | -8.61854 | -54.97065 | 2025-10-03 06:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 708f96d5-406e-31e4-bacf-90de6dbd7b8d | -11.13507 | -47.85854 | 2025-10-03 06:33:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |


[Clique aqui para ver as próximas entradas](README140.md)

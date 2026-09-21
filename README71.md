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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a210e147-49f8-390d-9645-741ea9ede57e | -10.9254 | -53.94251 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e1b59da-e170-3404-a2da-a46d2b3c1fd9 | -13.03593 | -46.97086 | 2026-09-21 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 243f0b06-d0ad-3e14-824f-fdc914183a0f | -7.25093 | -55.59082 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9800b065-e778-3273-b672-bbb64fd9dc93 | -11.41887 | -51.44806 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c310ab87-a4af-3d24-bf9e-0ffad7bb24bf | -10.47881 | -50.27689 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 15d1d300-cff2-31a2-a79f-4e989e0ed7c2 | -12.11243 | -47.04806 | 2026-09-21 05:06:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ae80256-8fbc-3c8c-88d7-8bdc208cb92d | -11.16999 | -54.12291 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e2b8a96-ebad-3825-8954-25912197e0fa | -11.80726 | -49.81193 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 81646d6e-3979-30f1-b5cb-d846bdba28f1 | -7.31968 | -55.60921 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 585a7ba4-a788-3ff5-ad9c-f71b47c50d31 | -10.90151 | -53.98117 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd254a2f-a17a-3246-b6aa-acb7f702a8c1 | -8.75792 | -44.27969 | 2026-09-21 05:06:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1b040101-5521-319d-8467-3a349f578827 | -9.27294 | -46.21946 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c350a4c-5646-3918-9dec-02790e4331bb | -10.85777 | -56.21154 | 2026-09-21 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf682887-3d7e-3730-87e2-475c5e49b30f | -10.39603 | -50.22676 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 587badb0-d006-3bf8-a216-ad3504ad3762 | -7.57682 | -57.6578 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60f8ff94-ea86-3f9e-b476-ccfd47d99601 | -13.59441 | -51.47121 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d80d075-eb0c-3c33-b21b-1a998c0c50e1 | -9.82897 | -65.0108 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8393cd22-57fb-3afe-8e21-e44a8e6d6162 | -8.76507 | -44.27511 | 2026-09-21 05:06:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4d89374-17dd-3f02-b05d-7c65a0b89828 | -9.81543 | -48.30762 | 2026-09-21 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d44849fb-6bd8-3463-b570-de4cc2ca77c4 | -10.45321 | -50.26408 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 61fb96db-1d03-3dbf-a505-9342152232cb | -9.71058 | -47.10719 | 2026-09-21 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b1e8f01-755e-3be1-af58-cb098a0cf7c3 | -8.07892 | -55.33627 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49b04154-1944-3eee-9cb3-fc797d0f34e3 | -10.88896 | -54.09276 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07b433b6-3786-3e98-895b-aea3abceb618 | -10.5897 | -57.49614 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b4340c1-c5ca-369b-bd1a-5a4c2ef2f358 | -6.45347 | -59.97622 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 130f1ec4-28d5-3bed-bda3-b7dbb409bda6 | -9.8288 | -48.31591 | 2026-09-21 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee20810a-c1bd-3f18-92b0-717b2d2d31b5 | -10.67687 | -50.73095 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 774296e2-23ad-3c34-9e44-86ee3c80135e | -11.62209 | -47.78097 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57140f5e-12e5-3138-979b-2d5f966a7b5c | -8.33485 | -50.83339 | 2026-09-21 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dd769091-e427-33f1-b119-db52eda2c240 | -9.41134 | -65.92007 | 2026-09-21 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8f3dd19-ea7d-3844-a0c0-687b01e7fabb | -13.87539 | -48.57729 | 2026-09-21 05:06:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65f348ce-1344-3f40-bb4b-7d45df6d8455 | -10.42195 | -51.86933 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ab2ea528-b61e-3d59-b210-9bd8262ec896 | -11.09584 | -48.31098 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8ab1c46f-0dbf-3abf-a958-581a7fbed321 | -6.69231 | -60.0118 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c07faa8-0e80-3879-9c38-e811d0329458 | -11.95606 | -46.50573 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c824908e-e688-368a-8c07-49dd07b2d6dc | -8.16011 | -54.82483 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5ee93a7-ddfb-3a4a-b848-3c10a69d83d9 | -9.56542 | -66.04993 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b0f1c5b-c29c-3fa1-a83e-283bd59f987f | -7.32907 | -55.61423 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dab3c7cd-9979-3a9f-aae8-b4adaed59f46 | -11.94476 | -46.50889 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 271a0bb0-6387-3252-91ac-883860fa3c89 | -7.49094 | -63.72729 | 2026-09-21 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba2eb627-2904-3733-9b57-ce143e8b2b65 | -8.78855 | -48.75048 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0fe0b7e8-638a-3c97-bb6e-bbb03b4cba55 | -7.246 | -55.60075 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 270efb8d-fe0a-37ed-b6eb-74ac0b0a7c58 | -8.77047 | -61.39167 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ddb81b2-497b-38d1-a567-9430f4741518 | -8.10516 | -54.85761 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6b9c6c6-a9ef-3cef-b98f-bad9fc0028da | -10.39155 | -50.22612 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| faa39e7e-830b-3248-9ee8-d03fc6022565 | -11.04549 | -54.9121 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d0aa8ad-b44e-3acd-99d0-0ab369c05acd | -10.79572 | -50.82493 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a35f8f2a-f378-3b44-9e8b-7cc54b538fc3 | -9.55514 | -66.01614 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df4ed150-b1c0-35e7-a72b-e9cf19576609 | -11.95174 | -46.50043 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 57a0c1be-a457-3056-a308-2eaf1ebb56b4 | -10.48024 | -50.29992 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3026e8ba-debd-3c72-a06f-f605be901961 | -7.81307 | -61.80705 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 807ee455-4b90-383e-991d-4059ea942327 | -8.78033 | -48.73853 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 991bdcd5-612a-3e3b-8073-5dba0550fbca | -10.9248 | -53.94666 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db188f65-3a0f-35b7-8ae8-70dd4c65452e | -8.14879 | -54.80826 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06fcb488-d9e3-340e-bce3-aacdfc75d5d9 | -7.57791 | -57.67274 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 662c2b92-caac-3085-8771-52cf23e9f1f6 | -7.57563 | -57.68716 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a358c88e-a7c6-318a-8788-d90edf1a5c02 | -8.15956 | -54.82846 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d5e3745-81ea-3dc8-8a08-a27a94877072 | -10.80467 | -50.75776 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a657f88-73e4-3dd2-b95d-d59ba0f86ac2 | -10.143 | -45.5596 | 2026-09-21 05:06:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65d98856-6df1-3973-8f5a-d3e95afc6ad5 | -11.34145 | -51.35072 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| db43db9e-c135-3b3b-8e04-c442c84ce6f7 | -11.10635 | -54.01374 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3626956-f58c-34c5-aa74-ed0ac7ef4b47 | -10.75786 | -50.79636 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 7f73cb87-f4bb-3782-9596-2fda30190c3f | -9.37902 | -49.88873 | 2026-09-21 05:06:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64b5cf64-7c32-3bb2-b5dc-cbe44bd5658c | -10.80677 | -50.77524 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 53481ade-d888-3cf5-b18d-b3b2368b0f42 | -9.02555 | -51.53279 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6bd1574-bc59-3361-97c4-ea140f96ef63 | -10.46541 | -50.27498 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 187662c0-ec73-36cb-9806-d65cd711af33 | -10.92239 | -53.9632 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7e25eb8-5691-3acd-8f58-8529781059d6 | -8.18402 | -54.73534 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d7be0f1-de41-3279-b4c8-f1f55e8ad97c | -11.83671 | -46.82349 | 2026-09-21 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3146d48e-063f-3b17-8780-f98ccf7bc8a0 | -10.74863 | -50.7993 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 977167c4-1eed-37ed-9a2c-45303d71b735 | -8.54847 | -54.71159 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e63ea1c-42be-3dd0-a844-beacf9a11339 | -8.4224 | -54.73412 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92d31bd8-9e4c-33bd-ab41-23dd4d69f795 | -12.09969 | -57.19447 | 2026-09-21 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b763a3-f193-3845-8e6a-40014818c37a | -10.75613 | -50.80892 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e11a18b-cf1e-32e9-bcbb-5991b6041a0b | -6.83555 | -58.98517 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eaece32-1320-3f94-8ab8-3f432b06e2cd | -13.02561 | -46.95861 | 2026-09-21 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c65264d-2143-3756-9fd0-d8775f78b10f | -8.77992 | -68.84862 | 2026-09-21 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ebba547b-bace-3b63-8707-8b11160388d0 | -11.02618 | -54.14511 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f179db52-dcb8-3a84-a50f-60634bfa2417 | -6.45049 | -59.9683 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 61a4f02b-e0d4-3559-b780-19872607271d | -10.44874 | -50.26344 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c6fb9865-4a74-3625-8b80-f3c75f530e29 | -11.02973 | -54.14563 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 723bbb86-7ccf-3c99-ae63-02dc2386a350 | -8.18077 | -54.77965 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9af6622-30b5-3c19-886a-fe3bb73a6a68 | -11.47848 | -47.76872 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37ea274a-d27f-32ae-88d0-ae4199c877bc | -10.8778 | -56.23619 | 2026-09-21 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 968df95b-f40c-396d-a9fc-b7cfc1588f80 | -10.83418 | -50.89822 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 174407f7-b453-3b8a-847b-e677d7d4a4ed | -10.58916 | -57.47807 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e9291c7-316e-3d29-8911-18b45bbc516b | -9.02695 | -49.83152 | 2026-09-21 05:06:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 308f2a2b-2db5-3264-96d4-34d84b352eb7 | -10.76478 | -50.81014 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91b82cd3-8076-32aa-b16a-6122a989e19a | -11.04205 | -54.91161 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83cb5f80-c617-3696-8960-899f834eb3a6 | -10.40884 | -50.23318 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| a022bb70-2c76-312d-81a2-6232287227ff | -10.88481 | -54.0963 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11d48d4e-6fe0-3ee4-a9e8-3171d57ce1ef | -7.37816 | -55.56116 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1ed7243-d8d6-3969-a9b8-bab7afdd2d59 | -9.44895 | -45.41019 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2244911c-2542-3a18-92fd-a6a2327800dc | -9.46715 | -45.41351 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 86bc940f-6a0d-3dfc-84b7-e45c6d0da249 | -8.17063 | -54.77808 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 346690fe-02aa-32f8-8072-76309474e1e7 | -9.53183 | -45.39765 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19c410f7-dfee-3e0b-9642-a52830aaa7c9 | -10.80299 | -50.7704 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 49d072b5-41f7-3a09-8a68-803f80da171b | -10.88127 | -54.0706 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d61c907f-6719-39ad-a820-c8406608c070 | -10.92062 | -53.95024 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe2c1840-c21d-3e8a-9f00-11435e01dd81 | -10.42548 | -50.24472 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README72.md)

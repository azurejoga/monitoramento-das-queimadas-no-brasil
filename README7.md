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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ba9f0a8-86dd-3292-ae11-00c574d69228 | -2.6388 | -46.7597 | 2026-09-07 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 753c48ab-782b-3f89-ae5b-ea14ccb4b096 | -9.7328 | -43.4168 | 2026-09-07 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ccf666fa-2406-3b8a-97c5-7812eacea12a | -3.1462 | -60.6506 | 2026-09-07 01:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4abba7f6-97cb-3349-9669-bd228e197dd2 | -9.7328 | -43.4168 | 2026-09-07 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8d69d223-ffe8-3d5a-ad2a-07280dfe387e | -3.1462 | -60.6506 | 2026-09-07 01:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 07e382d5-89b0-3d78-8ff8-3ee126ba7047 | -3.1461 | -60.6696 | 2026-09-07 01:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 086ded76-c10c-32ac-b5aa-50e6ff765457 | -2.9645 | -48.7036 | 2026-09-07 01:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 62c3bb5a-6e6e-32f8-9643-5df5fbb947b5 | -2.8655 | -50.4434 | 2026-09-07 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8c773512-7186-3fb8-919d-a85e4ce92f94 | -2.8839 | -50.4428 | 2026-09-07 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 9e3f99ad-4664-3668-ae81-9019e080b836 | -15.9331 | -41.9772 | 2026-09-07 01:50:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 75.0 |
| faebe908-12fb-3946-924c-091fac9b4e24 | -2.6388 | -46.7597 | 2026-09-07 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 95f18a8b-20e0-31f4-a538-8788ce1ef91f | -2.6387 | -46.7817 | 2026-09-07 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 0a60d99a-ff2b-36ad-99df-8c1ef9946949 | -6.0002 | -57.7079 | 2026-09-07 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f817c8d2-0d42-3e70-b173-05efd3530929 | -9.4968 | -40.2839 | 2026-09-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 167.2 |
| 2020de0d-2383-3be6-a4d3-7d9e16521a88 | -3.6215 | -60.566 | 2026-09-07 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 75c6d5a2-3fba-3d05-add7-4d833bcec730 | -9.4972 | -40.259 | 2026-09-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.4 |
| ce495e48-1db5-3add-b1ce-45f94c273305 | -6.0004 | -57.6884 | 2026-09-07 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 3766cb24-aa85-32bc-8284-278dcc392274 | -6.6513 | -59.9642 | 2026-09-07 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 817826d4-e25a-33cb-bfc8-45d6ee37b0a3 | -9.4781 | -40.2618 | 2026-09-07 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 271.1 |
| a3b520a3-41e8-3f67-b861-d6b1a64b2e97 | -2.9645 | -48.7036 | 2026-09-07 02:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d605ce2c-d1ba-3f78-88c7-32461f17cb77 | -2.6387 | -46.7817 | 2026-09-07 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| c13b52d5-366f-3ba4-ad37-33c88aa713c2 | -2.6388 | -46.7597 | 2026-09-07 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 34ae53bc-d4eb-3699-baf9-a76c7b148e00 | -9.7328 | -43.4168 | 2026-09-07 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c132da3f-3763-30e1-a671-4addb39fee0a | -6.0002 | -57.7079 | 2026-09-07 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 525e319f-b972-3f73-bc5a-3826c44d997f | -9.4968 | -40.2839 | 2026-09-07 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 323.8 |
| 80223043-44fd-3edd-aad5-8260fb86626f | -3.1462 | -60.6506 | 2026-09-07 02:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 55666a80-2a80-32c1-8bca-e6f78d214579 | -2.8839 | -50.4428 | 2026-09-07 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 5827bd78-8036-3624-9892-d5576b09db30 | -9.4777 | -40.2867 | 2026-09-07 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 251.0 |
| 72bab1aa-3acb-3d44-90f6-f32d744be502 | -6.0004 | -57.6884 | 2026-09-07 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 69bc61f1-8553-38c4-9736-9174d0dafe03 | -6.6698 | -59.9443 | 2026-09-07 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 89f5165b-083a-3b55-90b6-fe7166d6bd5d | -2.8655 | -50.4434 | 2026-09-07 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c9702a7f-c93f-31a5-b315-9f53132cffb1 | -9.4972 | -40.259 | 2026-09-07 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 321.3 |
| 8280ca43-d566-34db-a8a2-471514eac35d | -3.1461 | -60.6696 | 2026-09-07 02:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 36c8aec0-c096-3789-a0c8-fbb1192ff6bc | -6.6514 | -59.945 | 2026-09-07 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| c893469c-0e42-3f0a-b409-d56b16df2dba | -2.6202 | -46.7822 | 2026-09-07 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 85c597e6-191b-3222-881f-b90c9dda71f3 | -3.1461 | -60.6696 | 2026-09-07 02:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 034dbbc0-30f6-334b-baa8-3bad99107ea5 | -2.9645 | -48.7036 | 2026-09-07 02:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a2fe5715-bad3-3585-8446-ac416b2309b0 | -2.8655 | -50.4434 | 2026-09-07 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 0877a3e3-8f2e-3274-92fb-f815a3d21755 | -2.6203 | -46.7602 | 2026-09-07 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| eca15d9f-2151-3f08-a603-d08845a48700 | -13.3009 | -45.2209 | 2026-09-07 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 616e5c6a-94de-3b79-b372-fb6e7895b4af | -6.0004 | -57.6884 | 2026-09-07 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9aa22eeb-6528-305c-afdd-82a677b6015a | -2.7831 | -47.7823 | 2026-09-07 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 130a4bf6-2332-30d3-9942-aa3c403c98d3 | -13.3198 | -45.2409 | 2026-09-07 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 448be74a-1633-3041-a168-6fc5835cb0ad | -2.8839 | -50.4428 | 2026-09-07 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 66b54187-1954-3429-9a4c-bdc59feae122 | -13.3203 | -45.2177 | 2026-09-07 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| ffad497a-fa84-3003-825d-af2fa60637e6 | -2.6388 | -46.7597 | 2026-09-07 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c1591f0f-4f67-322b-bb62-9ea8fceac432 | -3.1462 | -60.6506 | 2026-09-07 02:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 4eecf542-5631-35dd-9643-378947504ef7 | -9.4968 | -40.2839 | 2026-09-07 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 3c65c1f8-fd8e-3a8b-9221-e5888af552d9 | -6.0002 | -57.7079 | 2026-09-07 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 7a14f70b-d20e-34da-9a6b-e4450d84d6ae | -2.6387 | -46.7817 | 2026-09-07 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| f3710c09-58c8-37c6-bfb2-fc1567791000 | -13.2477 | -61.7342 | 2026-09-07 02:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 23131a5d-5413-38d4-a8fa-33294840e421 | -9.4972 | -40.259 | 2026-09-07 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 5d194b8c-0d33-3983-b889-408cee5c086d | -9.47 | -40.26 | 2026-09-07 02:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7ccd8cba-ec66-30f3-bb54-3aae2b5de905 | -9.47 | -40.3 | 2026-09-07 02:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6bf39a14-cf79-31d2-89ff-df854b520a49 | -9.5 | -40.26 | 2026-09-07 02:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 74a31da6-0e20-3e0f-ba84-0ceb810991b9 | -2.6387 | -46.7817 | 2026-09-07 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 3f9f8339-45e6-3158-b3b0-1218d325d3dd | -3.1461 | -60.6696 | 2026-09-07 02:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| fa7d3cf2-471e-31ff-b795-68e99b6d88c5 | -6.0004 | -57.6884 | 2026-09-07 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e6dcb279-e418-3c35-83ee-e77ec03eb082 | -2.9645 | -48.7036 | 2026-09-07 02:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 883b8e70-f0e6-3cab-9626-d211cbf3b147 | -6.6513 | -59.9642 | 2026-09-07 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 414d4011-6441-3e40-b66f-3d3b24658d49 | -13.3009 | -45.2209 | 2026-09-07 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 857d8e28-c86d-39d1-88f7-979ac8be9649 | -13.3004 | -45.2442 | 2026-09-07 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 6638c9a0-d1ad-3892-8f89-27617fd68bcc | -2.8839 | -50.4428 | 2026-09-07 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 0de723c2-528c-326f-890f-664e14c66d68 | -13.3203 | -45.2177 | 2026-09-07 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| c52109fe-ab5e-37b5-b589-84ef64b5fe76 | -9.4968 | -40.2839 | 2026-09-07 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.6 |
| b7865a94-545a-3fdd-b3a6-1462d4e80cfb | -3.1462 | -60.6506 | 2026-09-07 02:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c4529fbf-46a6-384a-8d09-f7ad8d11f957 | -9.4972 | -40.259 | 2026-09-07 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 4a26ef64-5e12-3991-a3ab-5d3c0d245ba6 | -6.6514 | -59.945 | 2026-09-07 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 1eb0d092-bb28-3b21-b6d0-3ac4657aa95a | -6.0002 | -57.7079 | 2026-09-07 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2d9e59de-e138-34fe-9b46-12c6e56b3c5d | -13.3198 | -45.2409 | 2026-09-07 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 5f739caa-666a-3d15-ab34-dfc8301645e9 | -2.6388 | -46.7597 | 2026-09-07 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 24d1b42e-4da8-33d1-a6ab-71b3551be658 | -15.9331 | -41.9772 | 2026-09-07 02:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9ecbd59a-7c3a-3f75-96b0-ec282bc9a175 | -2.8655 | -50.4434 | 2026-09-07 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f6c5599b-f0b7-348d-8e32-b70b4dd4da51 | -9.4781 | -40.2618 | 2026-09-07 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 131.2 |
| c0c6c039-f43b-3c2c-b208-a501a1702919 | -9.4777 | -40.2867 | 2026-09-07 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 121.3 |
| 0a65c609-8e38-3f09-91bf-d2c39eead16a | -13.3004 | -45.2442 | 2026-09-07 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 30839053-e2fb-3cc0-8689-22c3a9ad7fe6 | -3.1462 | -60.6506 | 2026-09-07 02:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 541f7501-07c1-39ed-a3be-68485228c634 | -9.4968 | -40.2839 | 2026-09-07 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 229.9 |
| 06ae8805-7a5f-3d58-9c6f-f7a08cab43da | -15.953 | -41.9727 | 2026-09-07 02:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c8487673-bf60-3999-beb5-2183702cfa5a | -15.9331 | -41.9772 | 2026-09-07 02:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 73e8f823-82a0-38a4-b1e3-f3520db21fb4 | -13.3198 | -45.2409 | 2026-09-07 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 67a48b0c-eda8-31d7-8e4f-db6a43596713 | -2.8839 | -50.4428 | 2026-09-07 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| ab74743d-d90a-37d5-8fcf-d2f24c7a892f | -2.6202 | -46.7822 | 2026-09-07 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| becb0ff9-3995-3de4-ad4a-551e74916c6c | -2.6387 | -46.7817 | 2026-09-07 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 3bf03906-31e2-3df9-9d4d-089bb9c89522 | -3.1461 | -60.6696 | 2026-09-07 02:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 99c644a3-4850-341b-918b-5637db0efe56 | -6.6514 | -59.945 | 2026-09-07 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 616f81e9-8681-3e7f-9684-59f3e3f3ae98 | -2.8655 | -50.4434 | 2026-09-07 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 917dfdff-5c4f-3912-b3be-b344fcc50f1d | -13.3009 | -45.2209 | 2026-09-07 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| f7a3cf0f-99e4-3927-84f9-5ba386cd8df7 | -9.4972 | -40.259 | 2026-09-07 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 237.3 |
| 602696b8-f953-333f-bcd4-936452e0f8a0 | -6.6513 | -59.9642 | 2026-09-07 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| bf34bedd-f812-3600-8779-b8eba47b0a0f | -2.6388 | -46.7597 | 2026-09-07 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| ee59f5ef-1327-3717-bfac-17318f2308f9 | -6.0004 | -57.6884 | 2026-09-07 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ebde7bad-6b2e-3dee-99a3-ac2cf31a396b | -13.3203 | -45.2177 | 2026-09-07 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 3ed30ed7-9487-3e55-9329-1e2a669d0b6a | -9.4968 | -40.2839 | 2026-09-07 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 3fabdace-1fbe-36a0-aee9-c3e25b2e5a0c | -2.6202 | -46.7822 | 2026-09-07 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a354c7b5-739b-34ff-8330-6e747ce4a3b6 | -15.9331 | -41.9772 | 2026-09-07 02:40:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 993dc4cc-56c0-3f18-811b-cefb410ade4a | -13.3009 | -45.2209 | 2026-09-07 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| ce85736f-ca30-3492-b900-af4b5aa3c315 | -3.1462 | -60.6506 | 2026-09-07 02:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| eb4759b2-3edd-3f0b-a7d3-f69939dfd6e9 | -6.0004 | -57.6884 | 2026-09-07 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d5f7c2e9-9caf-3e00-bb68-8eff091c0006 | -15.953 | -41.9727 | 2026-09-07 02:40:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 72.8 |


[Clique aqui para ver as próximas entradas](README8.md)

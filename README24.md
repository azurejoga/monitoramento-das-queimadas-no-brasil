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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 626a7396-6aac-3ab3-9b49-e0d3934b607f | -11.68348 | -44.42544 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f157e7da-0f68-33d6-9d26-e17d53fe0477 | -11.70267 | -44.34603 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 65aa271e-ecb3-3677-821e-9aad0fbc81a2 | -11.50685 | -46.92505 | 2025-09-26 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 858d0c8e-b039-31f9-a5b6-34f87dd66e52 | -12.07016 | -44.86541 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee0ea15c-cd4c-3a98-91bb-e3bbf2db1ded | -11.42999 | -44.97673 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 10c93eea-5e99-390a-bb63-133d37563624 | -15.38334 | -46.12137 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c88c41f8-8a58-31b8-b310-de4856a08076 | -13.29335 | -39.85928 | 2025-09-26 04:17:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 46e361bd-e7fa-39ae-b2d0-0541d201d0f0 | -14.86064 | -50.94869 | 2025-09-26 04:17:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7e9c3b8-0362-3d03-bb6f-1412fb2b0d04 | -15.13003 | -46.4242 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 947aed13-6964-3cab-afad-d02e0e7ae211 | -11.01949 | -44.34284 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bf96de8-f235-3588-a7d9-4d13a2aa2d81 | -15.02373 | -46.93851 | 2025-09-26 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41ce20d9-35c7-3d49-87c5-a5272d4b227a | -12.14361 | -47.9573 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 24e40920-e1b0-3bdb-84a5-07c880f20412 | -13.80285 | -48.39185 | 2025-09-26 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd4b063e-0f09-3901-907f-040e206e98a2 | -12.05309 | -44.86625 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aacdeb69-e2a5-3a30-a43c-2a3fe22a8964 | -11.61749 | -44.43635 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 535f7f1f-1a07-3315-8281-ebfa8f674578 | -11.22859 | -45.55301 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd7c400d-711e-3a89-8d49-bdd0be6c0d6b | -11.43943 | -44.93867 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1461330-0e06-3ea6-9be7-99501c2ee7bf | -21.00428 | -50.00581 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6fdc6c13-5a63-38f0-9374-e2bafbe09009 | -11.38292 | -44.95102 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a348ef8f-56fe-3dae-a924-e53140e6bf45 | -12.13633 | -47.95604 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9422ba7a-90c7-3dc4-9b54-de56971c810b | -15.13946 | -46.42955 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb362602-2846-3190-910f-9f279332c9f2 | -13.85049 | -45.61692 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea9a95be-ddbd-3e9c-8e51-bcf32a319ecf | -15.52146 | -50.42656 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fb5bb3a4-17cf-3de2-ba1f-41d7a2d3c9de | -12.07374 | -47.99114 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f7a3d0e-8ef0-3c61-a1ce-cf98a7fdbaff | -22.61057 | -49.02661 | 2025-09-26 04:17:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3b5e0a9-e9af-3981-927d-1fe07c8f58ee | -12.18662 | -40.40995 | 2025-09-26 04:17:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4ade096-2dda-3e3f-8163-a64ed0be9b6b | -14.88019 | -45.54087 | 2025-09-26 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 409103f2-cff5-3214-ade0-1e6c31bacf39 | -12.14437 | -47.95284 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 55d74246-1368-3164-9be7-c7b0be5446bf | -12.87391 | -44.68727 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c468161-6925-33f4-a12f-1e319479e137 | -11.39064 | -44.94508 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4da1db1c-685a-33a0-aa83-b6fb8137153d | -18.22066 | -45.05424 | 2025-09-26 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adcd7c18-8a31-3d5e-94f1-4fa0ec8799a2 | -11.42888 | -44.98373 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 93b0f469-d76d-37bd-bfff-076c155467d6 | -13.41099 | -48.55099 | 2025-09-26 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 377edf56-2102-372c-9f13-b1285e446ce1 | -15.98656 | -49.55827 | 2025-09-26 04:17:00 | NOAA-21 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ded3cb8-0e9f-3b92-be01-d6f0ebb4c0a1 | -15.99863 | -49.02888 | 2025-09-26 04:17:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 5a36c92f-59ea-3cbc-b0c7-a040a2d7a0a5 | -11.97748 | -46.62715 | 2025-09-26 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5e210a5f-3295-3312-87a3-1e0a3a2ba7be | -11.43055 | -44.97322 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb11aa33-d9f1-36a8-8696-1c97fc1486f0 | -22.40865 | -49.63482 | 2025-09-26 04:17:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b0bd66a-60bb-3e76-86f9-05ff9fbcf6f2 | -12.38346 | -44.14659 | 2025-09-26 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68568a95-bd60-3a19-bebe-842afe1e490b | -13.85494 | -45.61035 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ee9efbd-9d70-305b-a272-7dc38caf9c7d | -12.07155 | -47.98184 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 314a1952-ae21-3dc4-9e0e-d66af4a20c2f | -15.88842 | -59.33574 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e559671-f985-31de-8f19-90e9d4d05dd8 | -15.90209 | -59.33907 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bea9822-ce62-3142-ab52-30cdbb252261 | -12.37356 | -44.145 | 2025-09-26 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e9c6c90-2275-3b22-a4a7-d284f86efc88 | -12.73997 | -47.07533 | 2025-09-26 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fab7693-ca6c-3cd5-b65e-f58391a083a4 | -15.89517 | -59.33777 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c71ee0c5-da1d-3324-881e-69eb8421d1c0 | -12.55805 | -45.8431 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1c9c958-b862-39d7-9c64-e8808b08090d | -11.00466 | -44.35119 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b49fcbeb-2873-3b54-b4ec-b4e81cb51bd0 | -10.4889 | -49.36911 | 2025-09-26 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bd4e374-e5af-3e25-9b77-a7326d32a907 | -17.94252 | -55.87061 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 94da50f5-201b-309b-aa8d-9d4d40ad484e | -18.54718 | -46.96493 | 2025-09-26 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af065a9a-1534-3eef-a0d4-a9314ed96ab8 | -19.9616 | -43.4154 | 2025-09-26 04:19:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 82b5c5ca-4044-33ba-847d-f5fefbbf7b89 | -27.49181 | -52.67759 | 2025-09-26 04:19:00 | NOAA-21 | BENJAMIN CONSTANT DO SUL | RIO GRANDE DO SUL | Brasil | 4302055 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0d90a569-8774-34f6-90ca-b1ca737ae9c7 | -17.94328 | -55.86695 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 52a3864b-9497-3302-8745-ce432e7a7c75 | -20.42383 | -43.3634 | 2025-09-26 04:19:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 48927a8c-e6e3-3a8e-97dd-0ce58209d125 | -18.55383 | -46.96611 | 2025-09-26 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33c37c71-f1dd-37fe-b859-3a9512c3ea68 | -19.92919 | -43.62179 | 2025-09-26 04:19:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 72629854-4c4e-36e3-94a9-f1283ac32a61 | -17.19141 | -56.37255 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 963f6b3c-89b2-3f8c-aeed-29c3835ea4ed | -17.20074 | -56.36722 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8d898997-8e0a-38a2-aecb-04418e9a9c99 | -18.47656 | -50.37921 | 2025-09-26 04:19:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 22dc3662-c70b-39a7-a89c-7754bbec1646 | -20.42738 | -43.36403 | 2025-09-26 04:19:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 5ed99d72-8370-3f15-8426-b71d79b714fb | -30.38988 | -54.25227 | 2025-09-26 04:19:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 064a0bf1-f13e-3daf-8d71-33ae82663993 | -19.7485 | -48.15092 | 2025-09-26 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 95e0982b-a125-396d-8482-623259e7d160 | -30.39373 | -54.25321 | 2025-09-26 04:19:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 0747b6cc-1915-3050-aec9-4299179c01d7 | -17.17904 | -56.35813 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 219f05df-a035-32ac-b865-b14a158cc2e6 | -17.18098 | -56.36591 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6056e72d-6cdc-3848-b882-d812bb8dd068 | -17.94429 | -55.86924 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 30183d92-bf74-3fdb-bbd4-a83d878f9251 | -17.18468 | -56.35939 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 63f658aa-49f6-3107-ae62-f23f3a200459 | -17.92863 | -55.85592 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bdb4e34c-5db5-349c-8f33-c6c5ecfcb568 | -18.51335 | -46.96275 | 2025-09-26 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af1dde46-c73e-32a5-9020-cadd03f98aae | -17.5851 | -51.81888 | 2025-09-26 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 354e7d44-e46b-344c-9afc-e7e319a92fc7 | -17.17817 | -56.36213 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7448e64c-1bfe-3ff2-9288-640d9f9a89b3 | -20.46563 | -46.50413 | 2025-09-26 04:19:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a657634-e155-35dc-abe9-bed7699d1d27 | -17.19422 | -56.37001 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1bf1c3d6-c0e2-3115-bfa6-abae39891eda | -17.81935 | -51.96669 | 2025-09-26 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dadba43a-9b8a-302f-ac54-b5e20e23e701 | -19.51597 | -50.60379 | 2025-09-26 04:19:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2eafd1fd-9579-39a6-8d32-9e5306f98384 | -17.17618 | -56.36058 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 94da9023-197f-3a2b-8cc4-8a1562d21d7c | -18.18521 | -53.33141 | 2025-09-26 04:19:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d29bb73-a578-3974-a5cb-9762ae38b30f | -20.01595 | -44.24102 | 2025-09-26 04:19:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6da6de4a-6705-3140-bba5-1e75ea8a7ca2 | -18.55442 | -46.96243 | 2025-09-26 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36201270-4610-362b-a086-56f4c8f705bb | -17.92938 | -55.85228 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dfd55902-3403-39eb-a2c2-dd918ed3e9fa | -19.74962 | -44.31723 | 2025-09-26 04:19:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 897ee2c8-b937-3620-9f11-8c98b72651fb | -18.2937 | -57.10025 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 674faa51-2d28-3f9e-9ab7-95ab405860c5 | -20.56958 | -47.17902 | 2025-09-26 04:19:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87e75a9d-0aca-339a-90c3-dfea2978727f | -17.18381 | -56.36341 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f2236a04-4338-3a08-908a-d55e8d668757 | -29.47772 | -56.33682 | 2025-09-26 04:19:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 68c71517-f698-33bd-9416-a29b5a957373 | -20.428 | -43.35958 | 2025-09-26 04:19:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| fe36a7ae-9fa4-3812-baa2-041a96c09429 | -19.13286 | -44.41912 | 2025-09-26 04:19:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9fab9070-f9ec-3958-a9c2-46072c986a28 | -18.29947 | -57.1016 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 05740192-55e7-3714-bdf9-c12d83356aac | -18.31102 | -57.10433 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c33fb0f2-5ef7-308d-b849-5f8a1e73f2be | -18.4719 | -50.38341 | 2025-09-26 04:19:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1c32ec4b-4e9a-38bd-88bb-692413afd1f6 | -17.19875 | -56.36573 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 87d34e0a-fb0a-328c-99ef-43abec80bcb9 | -18.56347 | -47.28744 | 2025-09-26 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b942d6d0-3396-3960-8311-89176d3fddca | -17.1773 | -56.36617 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 61401f8a-7593-30fa-8e90-9d76e857df54 | -20.35612 | -48.78543 | 2025-09-26 04:19:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea82e690-1d96-378e-a333-fe0710ec1ff0 | -18.66132 | -47.47405 | 2025-09-26 04:19:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac8b088a-a551-37b0-8971-b5334f1718a9 | -18.4757 | -50.38413 | 2025-09-26 04:19:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c21d9db5-0999-30ed-9186-e87a2e6aaf1e | -18.29853 | -57.10593 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 3714293a-556b-33f1-938e-3d298f5dd7b9 | -17.18577 | -56.37126 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 001ae899-5a8a-3049-b254-ea5e1f33958f | -19.92511 | -43.62527 | 2025-09-26 04:19:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README25.md)

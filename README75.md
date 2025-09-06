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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 466f0e53-d576-36b5-b28c-66b2c9205c5f | -12.94254 | -46.56992 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fe54b314-db23-3f32-9d5b-dde58d8fa51e | -12.69177 | -44.9703 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 63e897aa-c3b4-3d83-8ec2-f4b4851454d2 | -9.99089 | -51.62532 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcb82247-4b25-3190-832d-989e5763bb40 | -9.20566 | -57.0893 | 2025-09-06 04:40:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41f1f195-a577-3557-b17b-e1d3272149bf | -13.28718 | -46.81605 | 2025-09-06 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aec09920-27d0-319e-b80a-2f28833dab1d | -13.87867 | -48.0267 | 2025-09-06 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa2b7f35-6187-3ea8-a608-fb0802622a2e | -14.37681 | -53.02467 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75478a1c-5ea8-3887-adbc-aa1b9bf47b2d | -10.77318 | -48.27806 | 2025-09-06 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01fae470-7044-300f-b839-bdaf2b2d06bd | -11.06493 | -51.99464 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cae5699-7ae0-30f5-9ea0-07f32a02b27b | -13.00579 | -54.8217 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1f59b1a8-0b3c-3bba-a266-c6db552d28ee | -12.4922 | -53.85582 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6798e0bc-36a7-3631-a71e-9c8e76cfa8ca | -10.2203 | -49.7263 | 2025-09-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9076e2cf-1e53-31f2-9f75-c1a93bfb1450 | -13.56662 | -48.11678 | 2025-09-06 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db9c18cc-3cf0-3697-8cdb-8715ff9112b6 | -15.7272 | -53.60186 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb4de964-8b8c-346d-9eca-3602d24461f4 | -11.68832 | -52.19482 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e17ee2ea-62c9-3979-97b6-781e718feb74 | -12.5373 | -48.06887 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c7bfa11-c041-3233-83d0-ecb8a893f02b | -9.21932 | -57.09196 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc9a4cf0-4220-3702-aec0-779381b539a5 | -9.45795 | -60.51634 | 2025-09-06 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7910a75-5793-32f2-ad59-dc1c3fd2fae7 | -12.97067 | -54.82487 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a76f1532-c1b6-33f1-a2cf-92f79894450d | -16.30346 | -45.69055 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47b7a6d2-6cc7-32ef-8ce3-d3a6ba35101b | -10.06528 | -48.05666 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17aa92f8-0e59-36fb-bf6d-82d0c3d1f413 | -12.91674 | -48.01891 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46a27434-1eaf-31b6-8eb8-c51df2a7e70b | -14.34319 | -60.32349 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e96fb0b2-afe2-3bcf-aa3c-27bf6da26d0d | -12.86435 | -48.00316 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf5261d4-435b-35c7-8ec0-f3743e2708ad | -13.26877 | -51.79602 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d43ae880-d29d-3968-bdec-901d73987282 | -12.98479 | -54.83208 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14f4d762-4704-3d2f-9cca-ee3ccb063333 | -9.8033 | -48.3323 | 2025-09-06 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fc0f3d7-03c5-31ed-9224-a5a5e1ca99e0 | -12.4915 | -53.85997 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 838c3077-01b2-39b5-853e-d267b5ccc57c | -10.77918 | -47.77539 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e711625-bf37-3a3d-b3f5-f59f76d65fa0 | -10.13643 | -55.15705 | 2025-09-06 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e90cb8b4-58fc-3a66-9575-5d02effae365 | -14.78643 | -48.15111 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 561bc27e-f263-389a-811c-ceafea8a4af0 | -13.48832 | -51.82541 | 2025-09-06 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eb45654-f683-30d6-b58b-c605f3b85d3f | -15.18257 | -48.03671 | 2025-09-06 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27fb379c-66fe-3f7a-8647-f5a6eaed2649 | -9.98869 | -51.61752 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ffa5539-dc5b-3e1c-b94f-3f82088d1df7 | -14.42799 | -48.4407 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd3fe40f-ed30-3b68-8633-4cb75d209c8d | -15.078 | -48.11648 | 2025-09-06 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d902c28-8251-3e70-a398-808278d776ed | -12.9595 | -54.82285 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdfb9957-308c-385c-a0a5-e10ffb27b5bc | -12.62291 | -56.98576 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4384097-83a4-38db-9ee1-133b4b3b4bdf | -13.92375 | -53.99467 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec5bd74a-a2b9-3433-bf02-4a809529fd93 | -13.31443 | -51.63908 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4847f4c-b14c-3e60-a928-212a7b417533 | -13.85201 | -46.26604 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 57ed7682-2ba4-35b1-82a1-954ee4fef24b | -9.98475 | -51.62056 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 762b2f0b-4a4c-38ca-a1f3-8c2b822a563a | -11.63557 | -54.54319 | 2025-09-06 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d58d791-c99b-31f9-b342-a4df580d5b3d | -14.75442 | -47.49559 | 2025-09-06 04:40:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb7b5f03-c556-37ff-847c-6fb82309b6a0 | -13.01707 | -46.6555 | 2025-09-06 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71ae7128-83f9-3830-bb3c-a4fba87d8784 | -11.39833 | -43.57529 | 2025-09-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa1862ea-0733-3b48-8ba3-7495569b9e86 | -10.88587 | -55.72955 | 2025-09-06 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1efd1e04-dfc9-3cd8-ab91-799f8eda0410 | -11.47739 | -55.55011 | 2025-09-06 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 07d47724-ba7f-3a07-9ddb-e65e0dae1287 | -14.55919 | -54.5419 | 2025-09-06 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b78e7a75-6d82-3d4d-bad0-735cf59a6f1f | -16.33541 | -52.96105 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ed48899-e5b3-3b6e-bacf-d921158078ce | -13.23994 | -51.80977 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad96c896-a3c9-3c9c-8def-98ee80c98d53 | -16.32037 | -52.93628 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50cab737-02dd-3f58-afc9-bf4c099c6e36 | -14.79965 | -48.10983 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3440c346-62cc-3e30-bcf0-268016b93883 | -12.9768 | -54.81177 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18fa6411-d0e7-323a-8532-29cb295bbe7d | -9.55555 | -53.58337 | 2025-09-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f10f5a0-4017-3dba-b605-1022db51aff9 | -12.47577 | -53.84448 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5279178d-4ef3-320b-94e0-16f770b10fce | -16.30191 | -45.70289 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbebbce5-ac66-393e-9731-e534f92ba889 | -9.23639 | -57.07551 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96459119-f1cf-332d-b8e2-df0059f50cb1 | -9.71033 | -49.49062 | 2025-09-06 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 85f14acf-2b91-3d09-b5fa-fd4f3242633d | -13.72934 | -46.90995 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c27ec76d-73b5-3cb8-be97-9b76ce69181e | -15.98236 | -42.38462 | 2025-09-06 04:40:00 | NOAA-20 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e43078aa-4742-3038-b73c-479c9b3a8885 | -12.96219 | -54.78563 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abf7aed5-f27f-3a97-ac5c-24b221c89beb | -12.98851 | -54.83275 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d748fdec-f41a-33e4-9aef-5b5794e34f18 | -14.7095 | -60.25957 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e790402c-59df-3020-8c00-3482906553e1 | -12.01042 | -47.77824 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad7693ff-d4ca-3b06-b07d-743d4952fdd9 | -12.92146 | -48.03644 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd9b5ec7-8544-32ce-9780-33d384be5325 | -12.50221 | -53.86181 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75f8b7da-34b3-32f9-a098-7bc759904b65 | -16.32776 | -52.94468 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e7f2a2f-35a6-3d88-b92c-0417e92c0bd4 | -11.25828 | -46.40182 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f14ca9c-8102-308f-a73d-7228dc169b49 | -13.01026 | -48.06914 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 366550e3-2d51-3274-9f65-141758f07c09 | -10.29724 | -46.34954 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ffd3f1a-0337-3bcd-9543-4d057a118bec | -11.01483 | -45.943 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0079f6a9-2ab0-3abf-8522-8a927bfd7541 | -15.84251 | -52.2939 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f10cf968-238f-3d6a-a1e7-4b5b3f656c22 | -13.85347 | -46.25569 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70833d3f-7d3e-33cd-badc-c06dc9968793 | -11.40491 | -43.59571 | 2025-09-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 375d30c0-4325-33f2-a813-c6aa6ec9fb3b | -11.59757 | -52.19125 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91b6f91a-687d-3fdc-a0fa-5f5e8226900f | -16.30032 | -58.11053 | 2025-09-06 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8c3986c8-7289-372a-927b-8030bd50e00c | -18.53755 | -47.41804 | 2025-09-06 04:42:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e158b508-8977-332d-b2fc-a07584000e8f | -23.83766 | -47.7551 | 2025-09-06 04:42:00 | NOAA-20 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 916023dc-9041-3630-915a-ba5ef7073a6d | -19.97617 | -43.39732 | 2025-09-06 04:42:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3a8a9ad2-bfa0-350d-873f-a007d59c4d03 | -22.85024 | -47.2237 | 2025-09-06 04:42:00 | NOAA-20 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 70da3728-d63f-3523-bb97-ecd0f2414807 | -22.25357 | -48.74723 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b89caa7a-6c00-31ac-8ef7-5decc74dc838 | -17.91317 | -45.90408 | 2025-09-06 04:42:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dad65bda-f0ed-3f3c-aff2-3bd2d31f2c38 | -19.40386 | -44.30757 | 2025-09-06 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fe9ed5f2-4bb3-36b0-be64-0d42923e960c | -19.76452 | -57.95815 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2bc1322d-cc1c-3c79-8e1e-ec1f753828be | -19.80869 | -57.94755 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6ee6445f-0de4-3f45-810f-e4d6ff5248cc | -22.2529 | -47.30548 | 2025-09-06 04:42:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ba6ccf4b-c6c9-300b-938a-df6f228e4678 | -20.23753 | -51.31023 | 2025-09-06 04:42:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d7d3f67d-747d-3309-9cbd-36eec0075dab | -22.25709 | -47.306 | 2025-09-06 04:42:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 34c7904b-4f9a-3550-b020-600b1d8ce9cb | -22.24511 | -48.76405 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 6574ea24-c7f0-33e4-a9ec-040a69521516 | -18.44542 | -45.93688 | 2025-09-06 04:42:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bf56177-8fef-344a-b7f0-a5eb6e01d7bc | -19.80539 | -57.94298 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 99e719e6-afe6-326c-bb31-667d1adadf6d | -21.49097 | -46.196 | 2025-09-06 04:42:00 | NOAA-20 | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2792b13f-8ef3-3ca4-9da1-6de2dbe938de | -19.7612 | -57.95355 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9a11eff5-45c3-346f-afc8-29cc0bddc214 | -22.25742 | -48.7477 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 106a6b97-069e-33f3-8a23-7f0e9b043dcb | -18.43674 | -45.93577 | 2025-09-06 04:42:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 452b4596-081b-31a5-84fb-78c4a9b65822 | -17.9175 | -45.90456 | 2025-09-06 04:42:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abd387c6-95a8-39f4-8508-4dee31b51dc2 | -19.90385 | -57.92922 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c8ae7306-8540-3184-b9f4-d5ed257a54ca | -19.89322 | -57.91925 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 04d597d9-670b-3ab0-8938-e19a7342b117 | -18.26793 | -43.02068 | 2025-09-06 04:42:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README76.md)

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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e79fdd5d-8dfd-3435-af05-89089e3357db | -3.69732 | -50.2341 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5fca0bf-9965-36dc-b536-3d800197ad97 | -2.60553 | -48.25686 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc39057f-9040-30b4-9123-9b4b4af3b795 | -3.78287 | -46.69308 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ae810cf-7e5a-3ee3-aa80-79cb69b3983a | -2.84377 | -54.07668 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 49250c56-77ff-3801-801d-45b65f962717 | -3.60817 | -49.98222 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 773b9f7f-4181-3d73-8c75-18d3293dac92 | -2.77355 | -55.33785 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ebb4f74-7d0b-3c9f-805f-146c0dc8d317 | -2.70929 | -48.6817 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 433fee7e-5474-3211-aff3-9aa11d052f89 | -3.46289 | -48.92978 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d5fcfc4-1902-3129-b79f-9054653d70fa | -3.20044 | -46.57585 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 117e4922-e619-36a5-8c81-f03c82851a5f | -4.04602 | -48.33129 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69a5520e-61ee-3e0b-9fee-ece6a4aad63e | -3.46073 | -54.56894 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6084930-f70c-3fd8-a896-616093bdc2bf | -6.37948 | -44.75665 | 2024-11-30 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9769beb-0818-3fa4-a07d-5c5c7d03f023 | -3.27362 | -50.61813 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02ae23dd-bedc-30c6-8bce-4c34076d3557 | -7.86201 | -45.9194 | 2024-11-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2f5f0cf-b67b-3aa6-935b-f433501f0618 | -2.32156 | -50.64406 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d98566c-4f59-3c9a-9414-b24ad3ad3caa | -3.28047 | -50.5525 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0dc92ff-6aa7-3d16-afed-53b73aa67f18 | -2.85374 | -48.10334 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 922b8183-4667-3031-9cfd-c714db1cca4e | -1.13389 | -53.39251 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 726e7e51-8ec2-3afa-b122-0561048e0d84 | -3.05241 | -54.05055 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bde2baa-46c9-359b-b0a2-1f16718a4019 | -0.76402 | -52.45825 | 2024-11-30 04:40:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d31e5ade-ab69-3474-b4dc-280262ae339b | -2.58702 | -48.20028 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aab680d1-ebb7-3862-b68a-7cf5278726ce | -3.82907 | -46.56392 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96882668-8740-3bd8-87e7-b7e7f1cd3037 | -2.62867 | -54.06482 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 567c1c3d-98d7-3a6f-8522-6e8ccbbc37b8 | -3.30241 | -53.69281 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9fab6572-3a42-3680-98b1-860d89aa288b | -3.40399 | -50.65739 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 37a29f44-0d5a-340c-8001-396f62a07bff | -4.9833 | -47.85192 | 2024-11-30 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56042f37-8bbe-304e-8a87-bd10c7c5084a | -2.86718 | -53.98129 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c3a29235-ebef-3a2a-a59f-923d4d861980 | -2.32543 | -50.66692 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca357aa-94af-3a87-93eb-653dc304a2ba | -4.42123 | -46.14671 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b2551bd-ad7b-3b3e-8d08-c7048067f24e | -1.19879 | -51.74973 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 22efd82f-e3cd-3963-a2e6-7c805a706318 | -1.30595 | -52.86396 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f9cc4368-dbd5-323d-99b5-56d51b002ab2 | -3.41423 | -50.24056 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc90f17f-e3dc-3d71-836c-adf9dd4e26cd | -1.98359 | -48.67019 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4853829-f87e-39d7-9b73-3bf8d631788c | -2.58989 | -46.20924 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97a45ae7-2328-32a6-bdc9-9a4ac2272c5b | -2.71965 | -48.65868 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb4eb10a-653b-3775-8e7e-f2cc0089e686 | -2.63206 | -46.0742 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2476b1af-2f1b-35c0-be35-8930b2719124 | -2.37235 | -50.3937 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2423bd2d-836e-3cdd-a459-3e09800eab93 | -3.02366 | -47.79681 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 777952bf-4ef5-3bf2-938b-97d99ce23d2b | -3.70435 | -51.42781 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 442bece4-0d83-37f6-8e73-33a9d97ecca3 | -1.75676 | -53.64626 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 701c686b-265b-3e2b-91e8-3c541a46cc42 | -2.66743 | -48.79828 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1e70e1f6-27b1-3c21-af90-02e21a4b5de4 | -1.00067 | -51.72111 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bcf5abfc-2405-3555-a37a-1eb828fe2142 | -2.34005 | -50.57509 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 082c4023-67f7-364e-bbea-3dbdf22beb60 | -3.38328 | -50.11579 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec9a24c6-0e22-377d-8186-eb3ae07227c6 | -1.30143 | -55.73924 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df426ba3-cf6b-38e5-b259-51dfd9d5046f | -2.44051 | -53.62421 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 511f2468-a090-3b9b-ae0e-321ca90abf90 | -1.09033 | -53.6367 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0738a0df-2431-332d-a627-1b857994da4a | -2.7978 | -54.12881 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 111ae9f6-c4e9-379f-a0e5-f86312e81b2a | -1.99604 | -47.40683 | 2024-11-30 04:40:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4757870-c114-3f56-b8f3-b31ae3d1e32b | -3.32712 | -50.25554 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b30b126-a2b4-3331-8f7d-e4544192df99 | -2.89147 | -48.27603 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 213da935-cb9d-3fc6-9556-1324da22f774 | -3.17803 | -53.64054 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af9bd66b-2b08-3ef9-8e48-657c1ad288dc | -5.65616 | -51.4705 | 2024-11-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f19e498-4fdb-3176-a7b1-bdee470710ea | -2.45625 | -46.53643 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da3aecad-92cb-3db0-b781-b3e82488c4d8 | -2.32484 | -50.67061 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab5a3bcc-c4f2-3217-83b7-8af8ff25131c | -1.30597 | -49.17322 | 2024-11-30 04:40:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1c24248-ee7f-3c2d-b96b-1d6f18204cd4 | -3.06729 | -50.56801 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de13d169-307a-340e-bc41-655be7606248 | -2.87066 | -53.98549 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc64822a-73d4-32f0-bbd2-59e108bdeb40 | -1.85733 | -50.80892 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80e5ced3-4fdc-3b53-b315-ec8e164b24ee | -3.82285 | -46.5962 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdf64038-a735-3aea-919a-33b9b4574202 | -2.84598 | -53.03142 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a0c9fc2-f74d-3851-a9f6-4d11435726fd | -2.70757 | -46.12513 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acefa1a9-1f91-3994-8141-fa8000097d89 | -3.36453 | -51.06575 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48e63574-9014-30a8-8697-60d2f6a42f37 | -3.8772 | -46.67099 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9610725-aae8-3af5-822f-2324f9dd2761 | -4.00925 | -50.34832 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cff10fd5-0175-3616-a2cd-419fc0dc2827 | -2.98711 | -53.28282 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3db47c90-a84a-3f2a-9e4b-74fd83784bc1 | -1.65177 | -52.48831 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 926024c3-ab5b-336c-872b-88a58bc11009 | -3.53395 | -50.19381 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fa9addf-2c70-3493-917e-64ebba7e1242 | -3.30643 | -50.27784 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 243c33c2-faaf-3f62-afa2-50f71f7d75e1 | -2.86757 | -48.10191 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e6f839-13ed-3aad-a596-f2c2515c4ab2 | -3.68181 | -50.11938 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 702401c4-5f60-3a79-9f44-8fd126d3fc9b | -3.22711 | -48.742 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08fed93b-621b-3f9f-9d57-6c1c137ee9f9 | -5.38955 | -42.95985 | 2024-11-30 04:40:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 627faffc-ebb1-30ac-8899-de9004613efb | -4.06803 | -49.06351 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8578f7cd-22a0-3aa8-8e47-16dff531513b | -3.55307 | -50.40023 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4946186-0e59-300c-8e03-0d26851a5d3f | -3.32654 | -50.21552 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6e0a6a9-5ff6-3e6f-ab15-5da99c747be1 | -3.81647 | -46.59116 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3d1d3df-7019-3abf-ac9a-db016c0e735d | -3.26848 | -50.65082 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46b21073-2d96-3e45-b671-ad2a5e368194 | -3.79137 | -50.13688 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2566e753-dcb5-33d6-ad8a-876a9dfa4bd2 | -2.93996 | -48.33715 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ed8c5ff-1455-3f34-8bac-d4e9a10cb017 | -3.29629 | -53.83194 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47b9498a-b4f2-3e8b-b4e3-2232e7f4197f | -2.20439 | -48.34218 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4da0ee8c-f8ad-3beb-9705-03ca65487deb | -3.23692 | -50.18 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aee8fd5f-9f22-3df9-9799-8d5de90d7455 | -2.89791 | -54.15545 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9de79135-2691-3cd0-93eb-2a76d61089f5 | -3.03792 | -54.03733 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e06e759c-f8cc-3701-b14b-c67e24f1f36c | -2.80446 | -53.05123 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c4626168-5c8d-3d92-ad7c-8b2b2ef2b683 | -3.93785 | -46.89142 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c79a929-a759-31c6-a1a6-553a7d5c599e | -4.40358 | -47.26315 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a86c1d2-aafe-3085-a1f1-645d95902556 | -3.43587 | -49.47505 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bab9a1a0-3ea9-32cd-b62b-6e82316f0c25 | -0.98018 | -51.75668 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f3e285cc-f612-3553-a168-348869c2cfa4 | -4.45059 | -46.354 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5768ee5a-c7df-36b1-a0b3-839d765a673f | -3.19754 | -46.57151 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df6dd11d-3ffe-3070-beaf-7190d0899c5c | -2.03459 | -53.49788 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f219aa1-2734-337d-a99b-d0b614c73544 | -3.03047 | -51.53995 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8596c235-ee23-3f59-817d-b8f0f3b9cd53 | -2.42063 | -55.23464 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d86b751d-e5e2-3336-8bbb-a4e2a267fdc9 | -2.6753 | -46.14573 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93ed1334-6ff2-3674-bc1c-e001176f0904 | -3.80681 | -46.53771 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae31ef52-7976-3c1b-a5a8-08c71cd59aa1 | -3.83194 | -50.13609 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6eda9dca-7368-3df8-9682-493522254c8e | -6.91569 | -43.54404 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 3e866c0a-5e79-3e19-8315-b3ea48ad6bb4 | -4.04895 | -46.82961 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README56.md)

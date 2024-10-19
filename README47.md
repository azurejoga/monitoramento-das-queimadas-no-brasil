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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c86f05dd-35ae-386e-b6e3-aaf7f33fb608 | -7.44608 | -64.46504 | 2024-10-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 151a9808-355c-303f-8fdd-d873e2e4dfbe | -3.14293 | -67.98781 | 2024-10-19 06:08:00 | NOAA-21 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd09adf2-1263-3ec9-af73-2b900998b0d1 | -3.14265 | -67.98698 | 2024-10-19 06:08:00 | NOAA-21 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f126494e-9cd4-3fc8-b144-e0d0db683fa3 | -3.39198 | -68.34419 | 2024-10-19 06:08:00 | NOAA-21 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d72dd43-7f7e-3658-953a-294b1057eb46 | -5.7171 | -68.68404 | 2024-10-19 06:08:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b0f19ffb-a5ed-3d6b-90b5-33ab6bd0558e | -5.71296 | -68.6875 | 2024-10-19 06:08:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5425f839-673f-3241-8c3e-4b5933911de3 | -5.71649 | -68.68804 | 2024-10-19 06:08:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1aa6fa9f-1036-375b-af3c-d146f2ae0678 | -5.71357 | -68.68351 | 2024-10-19 06:08:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9272bfe2-82d1-33d8-9903-876d3c9029a6 | -7.84398 | -70.12024 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 764b086c-3ccf-34fc-91a0-2e5f20483e4d | -7.79666 | -70.06045 | 2024-10-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 253c9c7b-10ed-3e88-8e80-11d5d297b923 | -7.79382 | -70.05621 | 2024-10-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a63c3fa-440d-33d9-90d2-602f2272d3ed | -7.79041 | -70.05567 | 2024-10-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50cd767f-050b-3ed0-a266-9f7c7823c653 | -7.72225 | -70.06794 | 2024-10-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d9aae64-35f3-30cc-bf2a-6bf8212b3991 | -7.66594 | -69.92989 | 2024-10-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66206dca-7026-3353-b353-6e7a6eb8860b | -8.6769 | -69.96848 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11998429-9abb-3da4-a979-b1f65d97142c | -8.65315 | -69.60548 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd53759e-f67d-38c3-9546-e157590c1350 | -8.65235 | -69.60248 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b537249-d6db-3650-96d9-c64323b436c1 | -8.65175 | -69.6064 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e1be7e4-e68c-3c6e-81ff-124bdeb1b1a9 | -8.64945 | -69.59803 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea015ef8-519f-3b05-97fb-599415a03e17 | -8.64921 | -69.75239 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29785f61-6628-3444-a4cb-3a3a6638658f | -8.62173 | -69.73331 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d416f93-c762-324f-9538-672ae27d5b92 | -8.56777 | -69.92531 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adf5a038-ddb5-3804-a3a8-8123103a4192 | -8.56364 | -70.09106 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef747041-ec25-3a57-9567-794e39ab9a79 | -8.55855 | -69.98607 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26fa1d07-b239-3884-abe1-247c0ab6f76e | -8.55511 | -69.98554 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce56a694-1d57-365e-8e02-bf5b8b03cc96 | -8.50501 | -70.24628 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47b84850-f257-3354-890b-efd4d187bbb6 | -8.50276 | -70.26112 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2749ef33-6580-3184-946b-a7a88e114d0c | -8.41853 | -70.12254 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5aa27db-b9d3-3d2c-8988-22d77dbc30d0 | -8.41051 | -70.08302 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef1fd140-dd5a-36f1-8533-959c6c438da7 | -8.32256 | -70.19975 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c59d53e3-2e1e-3b9e-aa8e-f7a17d203905 | -8.31915 | -70.19923 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9514946-d458-3b87-ba3d-40321752f0c2 | -8.14466 | -70.19574 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6a12c53-e4aa-3a6e-8984-0b792fb9bc21 | -8.06167 | -70.16453 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83ec3f2a-1949-33b8-b3ce-1c7a391af0f7 | -8.05826 | -70.164 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d0aee8b1-5e81-3171-80ed-ee6f4d795eea | -8.80744 | -69.00394 | 2024-10-19 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edc31b01-c531-3828-8712-badacd9cd152 | -8.76995 | -68.88192 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88e7b334-294f-33bf-93e3-3ca46c076ac5 | -8.76934 | -68.88614 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f8442e1-f0a9-3f70-aa0b-f6df34725439 | -8.76784 | -69.51003 | 2024-10-19 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 38f6703e-d261-389e-98a8-cb3403d2190d | -8.76571 | -68.88559 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 892ed678-9eaf-3786-a7ba-02372b061bbd | -8.61825 | -69.7328 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dec141da-6432-3d05-abb1-6395cd717869 | -8.56719 | -69.92912 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0cbe0e0-c591-36b5-aeea-8de5dc3cfe63 | -8.50842 | -70.2468 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8484071c-98e9-3848-ad99-920cd83ee7fc | -8.50786 | -70.25052 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14445165-d602-3555-b20d-dfd128faccc0 | -8.39914 | -70.11189 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6236494-5e62-36d4-b867-859a3e40ed4f | -7.2879 | -70.01415 | 2024-10-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18fd1253-dcc7-37a8-9f27-a0728dc1ea93 | -6.6846 | -70.0388 | 2024-10-19 06:08:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cf3857d-e4d3-3994-903f-4bcd4faca824 | -8.03739 | -70.2099 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 163fab9b-d264-317f-b223-e2084dbbda54 | -7.96278 | -70.16826 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4b6bb8d-8db4-320e-886f-385abbdaa219 | -7.28867 | -70.01382 | 2024-10-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6fe4c90-2ed6-3153-8214-4e79e7285291 | -7.28449 | -70.01364 | 2024-10-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62620d21-1c30-3b2f-982a-f1549b474a28 | -7.83965 | -70.60017 | 2024-10-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a8f47b8-fa9d-3661-856c-8757fa66198c | -7.83238 | -70.60271 | 2024-10-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17487d5c-ed5a-30a5-a6d0-2ea272d0213f | -7.81734 | -70.63342 | 2024-10-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b76ac944-5c38-3023-9441-7436c5a5bd35 | -7.81678 | -70.63701 | 2024-10-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c4274c1-7566-3150-ac71-5d58a2b574d4 | -7.62984 | -70.46096 | 2024-10-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23e3854f-1984-327f-9276-5a8dd52a9402 | -8.50329 | -71.43104 | 2024-10-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a54f33b-7a27-333a-bf49-5738c92064b2 | -8.49997 | -71.43052 | 2024-10-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f599458-ef34-30d7-88ef-279dd51abca3 | -8.45192 | -70.34395 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27634ff3-b35a-358c-9eb0-e4ccfe337b19 | -8.44542 | -70.4556 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eef8a91-b6d1-38be-99ad-2596c3ff0b60 | -8.38996 | -70.53638 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc5fb474-e3b9-3c8c-b64a-90d81641a26e | -8.24515 | -70.34246 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47ef0094-eb69-3785-afd7-330b10788dfc | -8.22522 | -70.23841 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a65a6baa-77ba-38e0-af55-33b71ef76e58 | -8.15264 | -70.21207 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce5c94fe-88ac-3bc5-b98b-34bc081720a0 | -8.15092 | -70.20047 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ede868f-82aa-3f5f-b7a8-c8abedcca075 | -8.09236 | -70.23727 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fb18bfd-9b6f-3749-83fe-65f037a5311b | -8.19802 | -70.23421 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02d0315b-bf97-31f2-ae90-ad50f99e7cc5 | -8.15605 | -70.21259 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9b2a332-0cb2-3e05-a13f-306d2648ae6c | -8.09293 | -70.23358 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f9352a9-6b78-313e-b596-bb1905f46344 | -8.56243 | -70.49188 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61e26cb3-d2e7-3ec1-9208-1a612a2d66d4 | -8.45677 | -70.809 | 2024-10-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75b3cd30-84bc-3904-b4ee-faa8bb428648 | -8.30967 | -70.56482 | 2024-10-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da5f319c-42ba-30fa-93e3-80a7766d3a99 | -8.1735 | -70.61841 | 2024-10-19 06:08:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a54a8759-9811-3161-98fa-886ba8bd5f49 | -7.38759 | -72.59804 | 2024-10-19 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0250489f-a8dc-3de3-89d9-8e196a8caf5e | -7.37237 | -72.95228 | 2024-10-19 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c97baead-e465-382c-bc35-0b44edc99747 | -7.32159 | -72.75627 | 2024-10-19 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac62e545-be8d-3210-a390-d714be084bb6 | -7.17735 | -72.72202 | 2024-10-19 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3b62893-874e-3f1c-b113-e836e036d5ef | -6.92753 | -71.49905 | 2024-10-19 06:08:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0a14466-c378-3a2e-a54a-f245bf10ffbe | -6.92699 | -71.50249 | 2024-10-19 06:08:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5650a9dc-7236-33ff-9849-da58ee406514 | -7.86033 | -72.92181 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0ef31e2-1bb7-3454-929c-65ecd866e23e | -7.84124 | -72.7639 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a13555f1-1fbe-33b9-8e45-8222ddf3afaa | -7.8245 | -72.84756 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9991af0-41c6-3f41-b86f-eb9fdbe60cbe | -7.82395 | -72.85108 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a910d1ad-820a-3d13-a0c8-911b8d81c8ce | -7.81507 | -72.86408 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 734228ec-382f-381f-b10c-5e6d3b894e1a | -7.81285 | -72.87814 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b90b9a65-d3ba-3b0c-8d1e-b03f6878674f | -7.78201 | -73.09421 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a74f285-b4c9-3ecf-9623-663d86fcee0c | -7.70754 | -73.04598 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51c777ba-1a7f-32cd-96ee-281a9a612fe6 | -7.7042 | -73.04545 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3cd7a4c-5689-3d8a-8fd0-33c70299319a | -7.70143 | -73.04138 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 687dfa7f-302a-3c34-9f8e-a3d550ad6910 | -7.70087 | -73.04491 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53a046e5-1cde-36d4-9dc7-9dbc4b1a9d63 | -7.7003 | -73.04845 | 2024-10-19 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a90863e-ce57-3dec-9dce-7094892581ff | -7.63624 | -73.111 | 2024-10-19 06:08:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 019e8609-64c7-3af6-9aaa-e1ecd51e9f0d | -7.6329 | -73.11046 | 2024-10-19 06:08:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7780a3fb-86e9-32bc-b29c-19795d28132e | -7.37181 | -72.95583 | 2024-10-19 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 542fb10f-1d57-3ae9-ac0e-57db7206e83e | -7.32103 | -72.75979 | 2024-10-19 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6b68436-c3f0-3fe5-b21d-dae85d7d086b | -7.2506 | -72.47556 | 2024-10-19 06:08:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9e9ace5-c6ff-37e9-bc41-bd60121bf43f | -7.65875 | -73.24268 | 2024-10-19 06:08:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d7b6587-d207-3744-ba2b-57bad496ca91 | -7.65481 | -73.24573 | 2024-10-19 06:08:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20ea13b9-d7cc-3676-8917-8cbe27e39b12 | -9.3792 | -66.70038 | 2024-10-19 06:10:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07b35409-bf7a-30a6-96ce-43631b857182 | -9.82966 | -67.21532 | 2024-10-19 06:10:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11766910-87cd-3128-b414-100fa2fc972d | -9.45277 | -67.14698 | 2024-10-19 06:10:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)

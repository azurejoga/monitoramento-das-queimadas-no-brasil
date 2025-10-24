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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cc2fa3c-ed89-3acb-808a-34299d0248b3 | -2.87187 | -50.71748 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb78865f-8db7-3a62-b23e-c2cde644c0d7 | -2.80727 | -51.34971 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38ab0cc4-1872-3ce3-bc7e-d2b01ce9284d | -2.26637 | -47.8459 | 2025-10-24 05:27:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8cb72e90-97d5-3c7f-a6b1-8dc8cc3d28c2 | -3.32825 | -57.62748 | 2025-10-24 05:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88844adb-74a6-39a5-b5e0-fedcf776fff4 | -4.82374 | -48.67866 | 2025-10-24 05:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40acb752-4de8-369b-8458-bd773b644564 | -3.14217 | -50.62128 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d01757eb-ddc8-3123-a963-ee0f1a8343be | -1.54555 | -55.40774 | 2025-10-24 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 323089e8-e9b7-3c8b-a12b-26d2df11bbba | -2.63993 | -54.86491 | 2025-10-24 05:27:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98e4b482-6d22-37cb-b35f-f19468c87c9d | -2.81664 | -49.13971 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2a816300-e750-3c42-a8a1-089fc44d69d7 | -3.02507 | -49.4498 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6ba2398e-9bde-3efb-8a84-dacfe3dd4eb8 | -2.33343 | -60.06339 | 2025-10-24 05:27:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83bf3989-5a56-3ba8-b081-7bf23142513c | -2.9558 | -49.14693 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54205bac-1dfd-32d3-8802-9d0d8983c669 | -2.25945 | -47.84478 | 2025-10-24 05:27:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ad64247e-960f-3c7c-b64c-557f5c54badd | -3.69898 | -49.5651 | 2025-10-24 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56af8b69-096a-35c5-b8c6-7628d16ef863 | -3.40558 | -50.80725 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 102f34c7-8799-39d2-85d8-487c26976960 | -3.12161 | -49.1009 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ec3719c4-6c38-3f7d-a897-bb8f8fc63e92 | -3.13566 | -50.62445 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fa92c62-7e2e-34be-866f-ad1bfc702e24 | -3.02274 | -49.44911 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 16aa69ec-f8bb-30d0-a1fb-6c79f136b647 | -3.12083 | -49.1062 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 386e8b6a-0fd1-3947-a3eb-d94431ee3c9b | -2.80054 | -51.35637 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56cae5ec-25ea-3d65-852c-6cd180935581 | -3.2398 | -48.7563 | 2025-10-24 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fcfe76e4-2d2e-3ca3-8edb-51ae8b0e0c1b | -1.54199 | -55.40321 | 2025-10-24 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7ae5913-7d9d-3868-800d-47e3775fe356 | -3.1463 | -50.62231 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 22a57ba1-5fde-3bd3-89aa-b3f7e6526cbe | -4.81769 | -48.67197 | 2025-10-24 05:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a75da73-ec8b-3d67-886c-dc57a2a445b5 | -2.33288 | -60.0669 | 2025-10-24 05:27:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77803c41-38c5-38ed-834a-ef28d6f1e2e0 | -3.13983 | -50.62536 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 113001bb-9749-3caf-bfde-dc904acdb8a3 | -1.42308 | -60.4008 | 2025-10-24 05:27:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eea53720-2177-3271-9895-f85ac514e4a2 | -2.63977 | -54.86717 | 2025-10-24 05:27:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 328c00fe-89b6-3dfe-aba2-5ed67bac88b8 | -4.24064 | -48.55417 | 2025-10-24 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd6195b0-a1d1-3819-aeea-c0cda3252acc | -3.23891 | -48.76223 | 2025-10-24 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a65499e-fe58-32bd-9b0d-00cbba568ea3 | -2.87248 | -50.7133 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bbaf37a-9afd-3704-9e5b-6136e06381c3 | -3.13631 | -50.62008 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5a25b9c-ac65-3d3a-9f61-e58d4deb3d8f | -2.26611 | -47.84821 | 2025-10-24 05:27:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 813bebbc-3b19-382e-bea0-29f73909978f | -2.41677 | -48.44032 | 2025-10-24 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7aa26c70-7cdd-3e9a-8d3a-59bffcb92720 | -4.24833 | -48.54897 | 2025-10-24 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd4552cb-a7ef-34ed-944b-532d2108c704 | -4.27753 | -48.34061 | 2025-10-24 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 783d37ed-aca8-3bd9-bede-25430fe0df87 | -3.29401 | -50.19396 | 2025-10-24 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7834f1c-1ba0-3e8f-92f1-cf98b6946b01 | -2.86602 | -50.71657 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bac72466-bbd2-34df-b958-bc88bb859cff | -2.43937 | -51.91024 | 2025-10-24 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0195cd6-982d-3993-bfeb-adb53c1b5ad3 | -1.46104 | -55.17071 | 2025-10-24 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9ea0487-074c-31c4-80a0-9bd9c01412f7 | -1.59401 | -54.30679 | 2025-10-24 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 070a4054-6ddc-30ff-9f14-908035df9663 | -3.14281 | -50.617 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef9313f6-eca8-31f4-828d-3b9d782e422b | -2.80218 | -49.1483 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46e689e8-2035-36dd-bf11-bc7e243d4f4d | -2.42391 | -49.28075 | 2025-10-24 05:27:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a142d487-4f21-3de3-b99c-bf047f550f4e | -2.80427 | -54.38184 | 2025-10-24 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c60bfe09-b9d4-31e1-88cf-6063efe1ee0f | -2.81585 | -49.14504 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8b844f72-24c8-314e-b05a-92e5e0fe8c0d | -2.86541 | -50.72076 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 54e881e0-48f7-3b1d-95bb-fcde7d1a9a60 | -2.44769 | -57.92359 | 2025-10-24 05:27:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49c17f4b-de5c-3c30-acfb-4417d75e119c | -2.87125 | -50.72165 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f643f809-2fbb-3248-a271-d2c7cb8267c9 | -3.12809 | -49.10195 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7dcfbb6-8c3b-3783-aa03-c6a24d08638f | -4.2191 | -55.74766 | 2025-10-24 05:27:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9222cea0-7d11-3c86-8d9e-d35f72da8329 | -1.9248 | -52.14248 | 2025-10-24 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fde0e1a-7d37-3014-bd9e-5407af4a5fc1 | -1.54496 | -55.41155 | 2025-10-24 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a56b3f2f-bf43-3889-98fb-f8fd094e0e29 | -4.31363 | -48.23463 | 2025-10-24 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9185166d-5241-3a7b-af9f-838cd4bc2e77 | -2.47777 | -49.22544 | 2025-10-24 05:27:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ddf836e9-940e-34b7-9516-c8c4dab95dfe | -2.81667 | -49.14506 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fb9ebdc4-ddeb-3c05-a39f-074dc8fd34a8 | -2.8102 | -49.13868 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b5d6f53a-4ce3-359c-b440-54865b39834f | -4.34625 | -50.59447 | 2025-10-24 05:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc082811-ebc4-36f2-90ce-83d8c1d6afcd | -2.81101 | -49.13321 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d559480-6b38-3568-b072-d07683c1d92f | -3.14156 | -50.62539 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c32ad5f-655e-3b4c-b975-e7fb1bf36007 | -8.44834 | -49.5746 | 2025-10-24 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb8e91cf-93cc-3fe4-98bc-09a6d6a8736c | -9.46416 | -63.22934 | 2025-10-24 05:29:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e1367e5-a464-33e1-b25a-71fe4556b7d8 | -11.36307 | -55.12868 | 2025-10-24 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 102e3e74-13eb-3c12-9770-65a2ba7578c6 | -10.99597 | -54.25722 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a06bf16d-ef17-39ce-a51e-4304e059cc08 | -12.4217 | -54.36354 | 2025-10-24 05:29:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5782b743-c67a-35a4-acbd-24be5bd079eb | -9.6904 | -63.30491 | 2025-10-24 05:29:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 14b58402-6b0e-3491-9693-8a016a5da02a | -9.83043 | -58.06873 | 2025-10-24 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1a99add-46e8-3ead-a82a-1f0c0f06231e | -12.39894 | -54.16238 | 2025-10-24 05:29:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11cb0b0d-8868-381c-991c-3dcb6bc4c350 | -10.60666 | -53.99869 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a11cfbf5-adda-3997-9cd5-908741feb95b | -12.38875 | -57.52409 | 2025-10-24 05:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dde4d12-722c-3b17-9e24-da8fabe9bb04 | -10.47196 | -49.10361 | 2025-10-24 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f43457c-2bc6-3899-943f-afc0ed9de398 | -9.23378 | -51.82442 | 2025-10-24 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1091faa4-3f27-34b2-b176-1d312ddcbaaf | -12.39777 | -62.1251 | 2025-10-24 05:29:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae5636d-99f6-344d-906b-1aed345575cc | -12.39299 | -57.5247 | 2025-10-24 05:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a6eb9c3-2804-3680-af7f-c3a7ff3d001a | -10.99731 | -54.25801 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a53b8478-e5ea-3f0d-ba75-67c89a644d9c | -12.42251 | -54.3568 | 2025-10-24 05:29:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82c2680e-27e6-325d-b7ab-1122c2bba19c | -10.05367 | -64.98991 | 2025-10-24 05:29:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b976644b-cca3-3996-93f8-15770b6f155b | -10.976 | -54.24818 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86aa923b-8f76-37f0-9ae9-839d93dd520a | -9.98714 | -59.95604 | 2025-10-24 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdec0298-21ad-301a-ba74-fc504d75c281 | -11.10151 | -54.39077 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39533eb5-23b2-365f-a450-3c82f8873efc | -11.09844 | -54.39002 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8f3dea5-ec41-38dc-8ba7-c232a2bd6f7b | -12.81232 | -50.95334 | 2025-10-24 05:29:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df2a5290-b7dd-3748-9f2f-37588abb8d5d | -9.12134 | -64.27479 | 2025-10-24 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e51fc08b-f6f2-3edb-b0af-4746d69869c5 | -9.64851 | -64.10391 | 2025-10-24 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6e3c707-a73b-3a69-b36a-5d636537111e | -10.54897 | -54.8658 | 2025-10-24 05:29:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30c5b6d8-b70d-3b71-a94e-1217389804d8 | -10.99678 | -54.25095 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a33ccb29-be88-3d5d-817d-0d8e2459474e | -11.55306 | -54.51345 | 2025-10-24 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2406cc73-b61a-39d0-ae99-451f0411981c | -12.81766 | -50.96554 | 2025-10-24 05:29:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0bc7407-73d6-3ff9-8464-ecd0e5b4b43f | -10.96823 | -62.42311 | 2025-10-24 05:29:00 | NOAA-21 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6adbdaf2-0a62-3d15-8366-ae6f345350e4 | -9.4444 | -56.64944 | 2025-10-24 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8c6e941-50a8-341f-9b35-a2e7411322fa | -9.58483 | -63.49979 | 2025-10-24 05:29:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f122fbd5-abe6-32a6-b5ce-dfc16102c990 | -9.75803 | -55.34486 | 2025-10-24 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 096f698c-4846-3513-aa38-b93424856d78 | -8.60993 | -64.09905 | 2025-10-24 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f60e9f1-38c0-3924-b5cd-ab3327e66270 | -12.41625 | -59.89854 | 2025-10-24 05:29:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcc9d687-266e-3150-8007-f3a1b15bc839 | -10.66717 | -54.31487 | 2025-10-24 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1a339df-b108-33e5-b641-41be4ea4dfcf | -11.56294 | -54.51805 | 2025-10-24 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2155c98d-cc90-3226-87e2-f77c354e5fce | -12.81294 | -50.94761 | 2025-10-24 05:29:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ee6e559-9363-32c7-9a06-a2de824c79bd | -9.23659 | -63.61301 | 2025-10-24 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9da72f9e-74c5-3773-98d8-04e9f6fc7a72 | -11.33571 | -56.20554 | 2025-10-24 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba6d2f51-d16b-3524-bb9a-6c7ddd0a521a | -9.58152 | -63.49927 | 2025-10-24 05:29:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README53.md)

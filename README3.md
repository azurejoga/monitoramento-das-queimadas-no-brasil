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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a167393e-5258-361b-bc5a-869526e9a71e | -1.3501 | -46.991001 | 2024-12-28 00:21:00 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fec1a98-f2f9-3dee-8e38-e36c9f2ef3cc | -5.2364 | -41.2649 | 2024-12-28 00:21:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 997495a4-0f1d-3024-b43d-8d5aafa7b76a | -3.9606 | -49.431801 | 2024-12-28 00:21:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b333a8a-27ee-3588-b6c8-ba03ca417e84 | -3.8886 | -47.007401 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67bae671-25d7-3521-9927-1f449c407fb6 | -3.9896 | -46.680401 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f7aa24f-4a58-3c68-9b49-e0510cfd248b | -3.9169 | -46.905102 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 70b02768-396d-3ca9-9edc-844768a47ca3 | -3.854 | -46.673199 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b60bd617-4b66-3008-8472-1983e867cc44 | -4.2593 | -45.423 | 2024-12-28 00:21:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7815b0a5-1836-33c9-b503-8ab187832197 | -3.7231 | -41.689701 | 2024-12-28 00:21:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 903e8e0b-64bd-399b-bdd7-ecb9db86a245 | -3.8328 | -46.625401 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a0859dc-8ba8-3c1f-8cad-4815c472cc2c | -2.4672 | -49.292301 | 2024-12-28 00:21:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20ee1807-78f0-33b9-9e8c-10b30f71862a | -3.7339 | -47.1889 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ac3d55-72d5-364a-a985-fe9c0364ea25 | -2.2531 | -47.657398 | 2024-12-28 00:21:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f4a628-87bb-3224-bdbc-19d81aa55bee | -4.2674 | -46.361198 | 2024-12-28 00:21:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ecd4b1fa-e73c-3a4b-9054-c6b9d7bff11d | -6.9954 | -47.075901 | 2024-12-28 00:21:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 476a81ae-30ce-39da-acb3-242a0fee80ae | -2.0554 | -46.557301 | 2024-12-28 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed97bed5-eb90-3336-81e1-9c11e9de6f4e | -4.7214 | -43.452499 | 2024-12-28 00:21:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8604f2e1-ae2b-3896-a1be-d49c1e11cdb8 | -2.0571 | -46.564701 | 2024-12-28 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99cd2316-5fe8-39b8-95de-aea82d4b1a1c | -3.7729 | -47.224098 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc9c1d36-a65d-38d5-9145-d9926798dfad | -2.7248 | -46.012901 | 2024-12-28 00:21:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0323cf0d-4605-39b0-ab53-5d36c06fbb6d | -3.7587 | -47.343899 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8fdf75f-c173-35fb-8933-b09bffb67651 | -4.7168 | -43.432899 | 2024-12-28 00:21:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d3b8b6a-384a-361b-baa1-165fafdb6bfb | -3.9098 | -47.010101 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5143d81-301a-3031-89e0-ea88c9e797d8 | -2.0098 | -45.587002 | 2024-12-28 00:21:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6a0beb-1603-340d-a61b-fffaefb0807b | -3.9798 | -46.682499 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 05964746-d5bf-3cf5-9b85-4202e3e50570 | -3.2239 | -45.4911 | 2024-12-28 00:21:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 47683f2e-a7be-3ba9-8fe2-6010b0a127bd | -11.2581 | -44.469002 | 2024-12-28 00:21:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1dc2a8a-7c64-3cb7-8cfe-07d07a303e7f | -4.1948 | -45.321602 | 2024-12-28 00:21:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5ff0185-dee3-3a96-b8ee-d9d8b1e746a8 | -10.0582 | -36.175201 | 2024-12-28 00:21:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2f8d9fdf-42ec-399d-bd69-c1608d0364fb | -3.9749 | -46.661098 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 260770bd-228a-3cf6-8ded-4b3b5cac5e22 | -3.2627 | -48.067402 | 2024-12-28 00:21:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85314d0c-6bfd-34c9-bc41-b3f6cff7e05f | -4.0484 | -47.030499 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0adb1a8c-5bdf-30c9-b234-4b8e1843b92d | -3.5883 | -50.667801 | 2024-12-28 00:21:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a2286d2-d547-328a-9a93-c4ce8db2b970 | -4.0108 | -46.683102 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa2f0fa9-1403-3de3-908b-e70bb1175c76 | -3.8939 | -46.939899 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d6de60a-fb5e-3d00-a864-fd83d6640561 | -3.2046 | -45.993198 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8bd5a48-bed6-3c00-a897-1c3c98e970e9 | -3.8278 | -46.694099 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0c050c4-8684-3f0c-a546-b799165f238a | -3.9313 | -46.968399 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b421a0fc-3019-3ceb-9676-7ffdfc20cd0e | -4.0009 | -46.730202 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04fdb06c-66eb-305d-af1b-7de1cbf8291b | -4.0581 | -46.7099 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 804231c0-170d-3852-a461-506ebca13e77 | -3.9782 | -46.6754 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a71078c-6df2-3772-9780-d81952f70dc3 | -3.2104 | -45.477299 | 2024-12-28 00:21:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b954c5d-707f-3786-bb9f-65babe1b8950 | -3.9117 | -46.972801 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d21fb894-298c-3530-b21c-3d754aaf1046 | -4.0434 | -47.053699 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7bae7f3d-8ab2-31c0-a2a4-131fe0263461 | -3.984 | -46.882702 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b50a746b-b5ed-3e2c-a897-540a19f9456e | -3.811 | -46.847198 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac7560de-5978-3479-ae94-ddd657f14e04 | -3.7201 | -41.676498 | 2024-12-28 00:21:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 797654d4-ebd6-3a98-8fbd-cbf361046cec | -4.8239 | -42.3493 | 2024-12-28 00:21:00 | METOP-B | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b838f7d-030f-3130-9f63-f26919c3275f | -5.321 | -46.054901 | 2024-12-28 00:21:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3799c9a8-fabe-3913-83d5-f1f69ac07da8 | -4.0255 | -46.702301 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8ae6c83-0adf-3bf2-8ac4-f33640afc456 | -3.7133 | -43.411499 | 2024-12-28 00:21:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 731eb11b-f108-328b-9e79-f2900e38b9fc | -4.1299 | -46.708698 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ea47579-4827-32d5-a591-fba9c0960f33 | -3.8295 | -46.701302 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 266c2fde-8edf-300b-8202-1f84438c589f | -3.8312 | -46.618198 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64e5b4cf-ca45-3b4d-8bf3-79481907afb4 | -3.2027 | -46.120499 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f94fdc1e-23b6-3008-9ead-ce22f82c5efa | -9.2697 | -40.9491 | 2024-12-28 00:21:00 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 99eab102-e6ad-33a5-ba4d-2dc31986a604 | -2.6407 | -46.095901 | 2024-12-28 00:21:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b892fb3e-789f-3e39-8456-6b0c00eaa5f3 | -10.0646 | -36.199902 | 2024-12-28 00:21:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b36fa42-7797-3e2b-b0f4-ad7eed8c1d49 | -1.6464 | -52.607201 | 2024-12-28 00:21:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a9f6799-2718-3072-a1b2-287fa9b96bc9 | -4.0598 | -47.035301 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8d4030c-f70a-3635-b11b-bfd8f4145c6c | -3.7262 | -41.702801 | 2024-12-28 00:21:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 43fa2bfa-733c-3e09-a7c8-eac87571440e | -2.3032 | -45.563599 | 2024-12-28 00:21:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3daace-3fef-3728-b059-8c261a9adacf | -4.5714 | -45.976898 | 2024-12-28 00:21:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee29534-e12c-3213-b6e2-4c266dbfff8c | -3.9114 | -47.017101 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2391bb3b-0b07-309f-82e6-62e2d0faedaa | -4.1415 | -46.6688 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae0ea6bf-d145-3fdb-9092-becf59e25f40 | -4.7266 | -43.430698 | 2024-12-28 00:21:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 914ec2e4-37bc-35b6-99dc-ced3fbbddf81 | -1.6423 | -52.5891 | 2024-12-28 00:21:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fca56ef6-b0fd-3605-af77-18a590209888 | -4.0597 | -46.716999 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 592ee598-e633-3b13-b624-02a85264728d | -3.2612 | -48.060501 | 2024-12-28 00:21:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4b11bd1-d0fe-3c25-9769-12e1d420ea91 | -5.586 | -46.132301 | 2024-12-28 00:21:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37684ff6-fff5-3ee6-a2a3-50a6faff9468 | -4.7426 | -44.656601 | 2024-12-28 00:21:00 | METOP-B | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1237d5c-a7fb-33ee-94ff-2a26405c51ac | -3.9308 | -46.648499 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e22abdf-67d2-3be0-89c7-16cb33e782b2 | -2.9215 | -54.4659 | 2024-12-28 00:21:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b12b92d7-7d6c-32c8-984a-2c1716f0dd89 | -2.5597 | -46.872601 | 2024-12-28 00:21:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8badd8af-d280-3e46-bf00-2fb9f3f06131 | -3.8788 | -47.009602 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86e7d29b-69ad-3e99-947f-ab3b6857cb5c | -3.5866 | -50.660099 | 2024-12-28 00:21:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d86231d-ee61-3ed0-a4e2-edc6bbb8ed23 | -3.7697 | -47.210098 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc4917b6-30b6-39b8-beaa-f6a6dbfa042e | -6.7602 | -39.396599 | 2024-12-28 00:21:00 | METOP-B | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ca276961-84f8-3c38-be36-c68175ba8284 | -12.18158 | -41.3597 | 2024-12-28 00:24:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| a28bc21e-5a49-3518-9c47-049f1a78f938 | -6.76502 | -39.39986 | 2024-12-28 00:26:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| ade0a0aa-dffd-3611-9eeb-908043a3e26f | -5.94617 | -39.67636 | 2024-12-28 00:26:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c5976f4d-ad35-3a57-85c9-6f77a0b6637e | -5.587 | -39.52983 | 2024-12-28 00:26:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e37a37d8-aa52-3562-b730-1947959f3a4e | -4.73601 | -44.64413 | 2024-12-28 00:26:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 346.9 |
| 730f5a1e-7f3e-322e-be48-1abb5ca2654e | -5.22456 | -41.27282 | 2024-12-28 00:26:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2ebcdccb-8a3d-3b30-b022-c35b41e4f81c | -10.06116 | -36.19047 | 2024-12-28 00:26:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.2 |
| 21f04b4f-da56-3bc5-8b6e-21e77701875a | -5.91004 | -43.47932 | 2024-12-28 00:26:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e74f5d8c-15c9-3b36-a6d9-f86cec856290 | -4.73736 | -44.65382 | 2024-12-28 00:26:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 379.8 |
| 2eee0885-03b9-3573-8474-4b7bb32efb3d | -4.70261 | -44.47119 | 2024-12-28 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6ee6488f-965a-3223-99d2-95349f4af2ef | -8.78315 | -35.76678 | 2024-12-28 00:26:00 | TERRA_M-M | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 64017cc9-fa0a-34ca-9fdb-430f1b08aaf4 | -5.94772 | -39.68715 | 2024-12-28 00:26:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 21a4ab08-8a34-350e-a96d-60903a68563d | -8.7939 | -35.77178 | 2024-12-28 00:26:00 | TERRA_M-M | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 769c4bf1-e583-3147-b931-4bb24e866ff7 | -10.17168 | -36.51498 | 2024-12-28 00:26:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 17.8 |
| bb486101-a724-3e81-8684-4f5d066f013a | -5.22587 | -41.28205 | 2024-12-28 00:26:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 569e6fce-ca5a-3c7a-a361-d4f4254b62ec | -10.05852 | -36.17405 | 2024-12-28 00:26:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.3 |
| 824b318e-f7ce-37fb-91fd-13fb3d3caaab | -5.0915 | -40.5862 | 2024-12-28 00:26:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| fac310d6-f0a3-35f2-8935-ac87e52f0867 | -10.04678 | -36.17598 | 2024-12-28 00:26:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 47.8 |
| c4d28eae-e1f3-33f5-9eef-f93672f74a88 | -6.4409 | -40.62529 | 2024-12-28 00:26:00 | TERRA_M-M | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 4faf502a-ddc1-3f5c-9b9d-f18ad4d0bcad | -8.11909 | -43.14395 | 2024-12-28 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 0903af8e-ee20-3e37-858d-01c5ef3d1cf2 | -4.71181 | -44.46987 | 2024-12-28 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| b16e75cf-6968-32ad-a396-d446f9735248 | -5.23361 | -41.27147 | 2024-12-28 00:26:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |


[Clique aqui para ver as próximas entradas](README4.md)

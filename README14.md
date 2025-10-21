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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bfe6796-b393-3246-9f6c-92e709a27470 | -5.67243 | -49.79806 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 541d5da4-9a46-3ff2-982f-087f95cf9b58 | 1.71398 | -55.687 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fcce730-8702-3b65-b6a2-98789a2a664b | -5.44756 | -50.04168 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1b5bd67-8288-3607-bb9b-cce52b38909d | -5.6691 | -49.79755 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee30db36-d888-3409-af73-50b3368d654e | -4.87204 | -48.65606 | 2025-10-21 04:44:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef551e66-fe3a-31e0-8c26-fa8c718ce89a | -5.59852 | -52.17517 | 2025-10-21 04:44:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8add54f9-1da7-3a7a-ad11-b29c97898266 | -3.08747 | -49.51005 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afaf80d7-601b-3231-9f60-c5cc76573cbc | -3.24154 | -50.02755 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e36d07fb-03d8-3ded-ab43-1a089670b4fb | -2.88573 | -50.73476 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60e51eca-751d-3453-a7bf-6e867d625a1f | -5.29366 | -50.56907 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78d4b4a1-8f7b-39fb-8993-c94142e9484c | -1.76098 | -47.26191 | 2025-10-21 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae974ce1-8da9-36bd-8dce-8782d7ba5e73 | -3.66505 | -51.94794 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74ecda07-eddd-308a-8a9a-73e54c7ae27e | -4.84376 | -43.0064 | 2025-10-21 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 60f4318a-4574-32b2-b233-6a580f949a4c | -2.87538 | -50.71118 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2be0f40f-4cdd-3ac6-983f-82e01aaa6f0f | -2.272 | -51.92203 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0f9e08d-a317-34d0-8789-2363be8824e8 | -3.32935 | -50.2277 | 2025-10-21 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c88ae284-5359-3bc5-bd8e-4df56af352fd | -2.9331 | -48.30428 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 973dee2a-a926-3e9a-8c61-bc91013fd176 | -0.74135 | -50.29837 | 2025-10-21 04:44:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86fc55fe-7044-3859-b161-ef1a40d61c54 | -3.15416 | -50.45625 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d56a71d1-44fd-3f20-92e5-ef67d8d4ab86 | -3.85592 | -48.96373 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ff8b80a-25d1-3e66-aa24-07722cd73406 | -2.57408 | -48.3956 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc7efa04-791c-36c9-a17b-b0bfbc65d068 | -4.55325 | -50.60712 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe5749a1-025a-3cfa-9263-c148b3f41a5e | -5.67297 | -49.79455 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84429305-5766-34cf-8f0c-adb1683ad9ff | -4.56873 | -49.65499 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1765515a-3496-3026-b8e5-c7442d874340 | -2.7201 | -48.83286 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc226d9b-fe22-3c42-858b-f7c52d7503ef | -3.58762 | -55.44658 | 2025-10-21 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b53df97b-ed16-33ec-a829-e2b81b1462b0 | -2.87322 | -50.72496 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80d9af67-2c94-3667-aeb5-102aeba20a7d | -2.0292 | -48.50844 | 2025-10-21 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff676904-4100-3ea5-9ea9-aaeddfd61fcd | -3.12057 | -52.72303 | 2025-10-21 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dca6ffe0-2301-31e5-b982-c1d0f708db4b | -4.87235 | -48.40344 | 2025-10-21 04:44:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 077b9017-a24c-30c6-9cee-ac33c129d969 | -3.50471 | -45.82607 | 2025-10-21 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0856f193-b6ed-323e-a827-06ee222282e1 | -2.88904 | -50.73528 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bded7dd-2693-342f-9d65-1152b4bcc4ba | 1.70639 | -55.71777 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42c6029a-4a5a-3749-bf07-e1da5ec209b0 | -6.89135 | -43.61863 | 2025-10-21 04:44:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97d91f3a-83e5-36a4-aab3-2a2fafd5e9d5 | -3.12742 | -45.26916 | 2025-10-21 04:44:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3f99c9a-5b3b-3e14-bdff-ede29c9548fd | 1.69439 | -55.72873 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8daaaf66-9eae-340f-9637-1f5e3854c146 | -6.24132 | -47.32137 | 2025-10-21 04:44:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e666efa-a27d-3de6-a53f-5463bdc18e9f | -2.85092 | -49.54382 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08c638ed-9817-3975-80dd-b8b8ab8491d2 | -4.18435 | -48.92931 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cece7aec-38f3-3795-94d8-13ea3fad6c3a | -3.32606 | -50.22718 | 2025-10-21 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 112b0c4a-11cc-3e40-a90a-712976a6aff9 | -1.76516 | -47.16566 | 2025-10-21 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a180bbad-0b31-38b9-9f44-cc127f84d989 | -2.38995 | -51.99731 | 2025-10-21 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a993e6c-c615-3df7-86d0-e3760674f206 | -4.38447 | -49.68023 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7887dbf-60df-38b7-840e-b0489ff9b329 | -2.45012 | -47.18989 | 2025-10-21 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d527624c-97b2-33f4-848e-94ed777c417c | -3.81292 | -48.65018 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4033db5d-6c6e-34b7-9aef-52e1ac123a7d | -5.5859 | -49.0117 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edc3ab04-f18e-30f1-a86f-263671673a7d | -3.81501 | -51.40394 | 2025-10-21 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 491b4d68-dd63-3dfc-a094-2881e9094694 | -4.00466 | -46.96243 | 2025-10-21 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f80dddc-69c5-305d-8d6b-145c20dbd9b0 | -4.49484 | -46.47504 | 2025-10-21 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c43ab9c-b53b-3171-b00d-fb9fc7cdcd85 | -6.07565 | -45.8138 | 2025-10-21 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54efb4b3-a83c-38e1-98d0-5827dd41a610 | -2.99605 | -49.59437 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22b5a252-6dd5-309b-b540-71ba8d0a1369 | -2.92952 | -48.29988 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1a94fe4-5c0c-31c5-865a-ca1bf11af706 | -5.5308 | -50.05437 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaaf5df6-ae10-32cd-baf1-44c1ea3f32ff | -7.02025 | -46.43173 | 2025-10-21 04:44:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae41e35-9d15-366d-bc10-360cc73c56e7 | -3.11465 | -51.20375 | 2025-10-21 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b586ec4-366f-3a55-aa66-2799b4943535 | -3.2267 | -46.78234 | 2025-10-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 26098b28-b12d-396b-89be-1b212eb58296 | -5.48122 | -50.04333 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf36ad1f-2be7-3164-a32c-e389bcc7dd63 | -3.97 | -48.06019 | 2025-10-21 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de305294-e07e-30fd-864b-74412165fe4a | -3.15463 | -48.59497 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c553f5a6-a471-386f-a9a4-54d90cd4c9ae | 0.35312 | -51.32762 | 2025-10-21 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| deedb864-c121-3c59-a11a-0b990b46e9ff | -3.0218 | -50.44954 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cda7544-b635-3150-a02a-7d80f1bac43f | -3.59681 | -55.26448 | 2025-10-21 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fd7cee4-db77-3eb8-a516-40bec1aab543 | -3.50083 | -45.82547 | 2025-10-21 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| aaaedcde-50ec-379c-89bf-e22cd2cbbf3a | -3.19768 | -53.07745 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5389ef3b-f480-3339-9226-4834d9e1d21a | -3.3367 | -50.74556 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8274bd86-e53c-3762-b0b2-03a331f73656 | -3.50256 | -51.18316 | 2025-10-21 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2543f695-c1a6-3bc6-957c-587005cc5869 | -2.87268 | -50.7284 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e60ca1a-91fd-382c-9e7c-4dac38135471 | -3.09132 | -49.5071 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 025316cb-b7ff-31b6-9dc4-08eadd0b9c97 | -2.25485 | -51.91582 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 029f9fef-3e37-3ad6-96a6-a295e9293da9 | -2.86061 | -50.74066 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15e16e46-444d-30a2-94ff-fe3b5bc4a427 | -4.74138 | -44.43208 | 2025-10-21 04:44:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afb040d7-cd30-3756-927b-bf72c4101481 | -4.27359 | -48.87636 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edf84f5b-7721-38d2-85df-453c2b1cf264 | -6.07161 | -45.81324 | 2025-10-21 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 100a4ce8-06c0-3d8a-bcae-dc06a46904f6 | -3.44858 | -41.84794 | 2025-10-21 04:44:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90bf0add-7f4d-34de-a2d6-d2e6af7e5417 | -1.85873 | -50.64029 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0000a727-73ed-3e87-92fe-331a934c7e5c | -6.72858 | -44.15171 | 2025-10-21 04:44:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1b0ce2f-6fc0-3ca9-97d9-203ae238fc29 | -4.17113 | -48.19091 | 2025-10-21 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e15f7022-c4ea-38c9-a659-e081ef743a14 | -2.4451 | -49.3744 | 2025-10-21 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49bce765-04c6-3f3d-a017-aaaf7477d031 | -3.33319 | -50.22478 | 2025-10-21 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5a729791-5e5b-3452-8fa4-93852c287bb4 | -4.87068 | -48.45712 | 2025-10-21 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f143fd88-cfc8-373e-8c19-a3f7c7146d5d | -2.8573 | -50.74015 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bded02b7-c3ca-306f-b9ab-30ecc9ae459f | -1.6382 | -54.05465 | 2025-10-21 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfbdd4b5-f74d-3d4f-9f97-ae039d74d1c5 | -3.13347 | -53.00227 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3d5fe29-d4e0-36bb-8d05-5d0443c5aa6a | -1.97767 | -50.81488 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 42e1dd41-86c5-312c-81e9-ada5774599e2 | -3.60323 | -48.99046 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19bf50ab-9d2d-31dd-8db0-9e60248a9094 | -3.97289 | -48.06454 | 2025-10-21 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ce44e31-b942-30ed-b1bb-632a68b40122 | -3.7157 | -52.14213 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e96a8c6-533b-3c72-8655-da0219d23697 | -3.72831 | -49.08569 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7db4342-8eff-37b3-a4c6-17780e8cb59e | -6.90981 | -43.59017 | 2025-10-21 04:44:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9177cbe6-28f2-3444-bd1c-35a16d78319a | -5.63292 | -50.03163 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c14e89a-d0a8-3e31-a247-1dd69afc8381 | -8.06361 | -41.05162 | 2025-10-21 04:44:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 71c88240-98b6-386a-8b8b-f8d9cbb92a3a | -2.86884 | -50.73134 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3539033d-564e-35ed-927a-9d065c6a562c | -3.22604 | -46.78664 | 2025-10-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d8d48866-cee1-35ca-bdb6-3199e74b6dbb | -3.12994 | -53.00172 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd3a4e59-def8-3012-b4e1-0761cfa56179 | -3.97231 | -48.06837 | 2025-10-21 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b74aae63-107c-32ba-aec2-97f8f129b715 | -6.42876 | -47.2991 | 2025-10-21 04:44:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d84dc56f-8796-3cde-8d7b-04baaaf96429 | -4.57205 | -49.65551 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 61f08bf3-1d60-38b8-9a0d-0d55950c0e7d | 1.71864 | -55.71796 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 237f62a6-fc90-373f-97b8-0279dcbebecd | -2.25428 | -51.9195 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ec1312c-1cc8-3ae9-a946-60ebb88cf136 | -3.50008 | -45.83036 | 2025-10-21 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |


[Clique aqui para ver as próximas entradas](README15.md)

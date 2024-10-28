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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 314cf508-c6a0-3dfd-8203-a83733879434 | -2.51994 | -47.44835 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c49682bd-a001-36ff-9b7f-0b3031850742 | -2.51121 | -48.31287 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb4d8586-d924-38bf-a570-e12e4c948ffe | -2.5072 | -48.31226 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a994520-ebcf-3269-aeec-90ea218bb5e7 | -2.19217 | -48.82054 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92b190f1-7821-3fd6-b913-957c77af9225 | -2.19099 | -48.81306 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d6df17a-472e-322a-a868-98de99cdc2cc | -2.19027 | -48.8179 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93b1bc6b-ecea-3dd9-9297-216577f3aa6c | -2.18906 | -48.81512 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a84a76a5-b7f2-31cb-aa2a-2eec777350fe | -2.18747 | -48.80003 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32e52c16-91ac-3831-b27d-61624d5af74b | -2.18724 | -48.72534 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 227ee702-44da-3c15-9c76-090a51c3bd33 | -2.17286 | -48.81755 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d682680-ce69-3895-9e89-9384b0b1a13f | -2.16824 | -48.82178 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 716ce13a-0801-3d21-9e40-85b8dc81a209 | -2.81766 | -48.43768 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51d6b6da-c6e1-30e0-ac02-00780375e036 | -2.81714 | -48.44112 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5a0232f-bf69-304a-a353-686722d6e70a | -2.81315 | -48.44048 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 836a4439-078a-3ae4-b5d9-2ac5f5bcf493 | -2.8093 | -48.70658 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4e37222-d202-3497-80b0-7a89ae1dbfdb | -2.77758 | -48.65034 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f75caa92-6c7b-3a9c-bb43-aa3a0d5f25a8 | -2.77473 | -48.69609 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27e09841-20bf-33e5-bcb5-eb8bc8d139c2 | -2.7708 | -48.69547 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9334ced8-f09b-377e-9e0c-7b6147c805af | -2.76387 | -48.71489 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e71baad-fb01-32a5-acca-4e4d63d17356 | -2.76313 | -48.71985 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09c0bf3d-cbc2-33d2-8430-9fbbc0e6c036 | -2.75995 | -48.71429 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fd2cda9-4748-3059-a301-a3444eccf2c7 | -2.70004 | -48.63183 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed23d1f5-8280-3fd0-984c-ea641b64ea6e | -2.68988 | -48.64566 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68e5fc88-9f48-3f78-83af-401e593de690 | -2.68595 | -48.64505 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f407db1-a35f-391c-866f-addf3966020c | -3.10981 | -48.60216 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25db5042-6e21-3215-8ece-8f66f43f191f | -3.1093 | -48.60557 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64c0d3a1-730d-3097-b135-7a4be010dd8e | -3.10584 | -48.60154 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9346e797-bfb4-341b-b2dd-31cf63ebdf7f | -3.10534 | -48.60494 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6398e6d9-f441-336b-b463-054a9fddb8a7 | -2.94385 | -48.74523 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55e402db-183e-3370-919b-d94c0b8e353c | -2.92409 | -48.96001 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39c75e00-2ea0-33ef-acbc-436de6d0b26f | -2.92275 | -48.95815 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91d2eda1-4b00-32c1-bfbc-ca2a4fd70ef3 | -2.91923 | -48.04084 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71b7546f-39fb-34a8-a679-157ae9dd81a7 | -2.89144 | -48.27682 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67e7d6ed-2906-32cd-a905-f884407a4c67 | -2.49934 | -48.06076 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 93266360-335f-3330-9889-09e5b5fdf104 | -2.49582 | -48.05651 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c967bff1-6f38-3d5f-8662-5b2d904d51db | -2.49526 | -48.06012 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f3d55ab0-54ae-320a-89f6-8f71944dbbd9 | -2.49471 | -48.06372 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 475e3757-2210-3823-a699-afd01c162d87 | -2.49286 | -48.04862 | 2024-10-28 04:57:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd04312b-95eb-3b12-9768-a3037dbfd10a | -2.49175 | -48.05584 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0551fb5a-dce5-3d85-af01-87e4de88e4b0 | -2.4912 | -48.05944 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0df473ac-a077-3d4b-b45d-0fb1a96ff622 | -2.39246 | -48.1038 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c3f544a-6395-30cf-9aa3-c63f73d7f6e1 | -2.37012 | -47.66926 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 681fc558-c8d7-30cd-9d66-7e89acb806ff | -2.3687 | -47.66934 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 102b3205-8319-35ec-85fc-b8b3cba5d349 | -2.36595 | -47.6686 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8564441a-4152-3110-8e2e-43e4f0e8e700 | -3.01059 | -48.0964 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c9d2c8d-4bea-3a98-ac32-81d1cea07208 | -3.01046 | -48.75698 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da7acf31-27ec-3161-a72a-18ddeff8a308 | -3.00649 | -48.09575 | 2024-10-28 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac347164-cace-32bd-8825-e4ce5592ae47 | -2.95966 | -48.96056 | 2024-10-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1baa4fe-e745-3142-8ecd-398fca86596b | -2.48828 | -48.49169 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de0510c9-4509-349a-979a-77950aa9e408 | -2.4575 | -48.50783 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b26d8bc7-b19f-3f70-ab4e-3492a7637b00 | -2.45735 | -48.4817 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86ace88c-1f43-375a-ab2a-2526e1c771a6 | -2.45477 | -48.47966 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5597397c-452c-301d-a82b-e168ca9b9580 | -2.45338 | -48.48111 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4a6ce74-e19f-3a4a-9b92-65afe2c92e84 | -2.44605 | -48.50956 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dbd3e8d-e644-3064-9ffd-b02cfbe74a0a | -2.4421 | -48.50893 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 503dadf8-540a-3e35-b20c-7df15e9b0515 | -2.40819 | -48.54516 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e219dc4a-20c1-3a2a-9da2-c7b609c49fae | -2.40741 | -48.55019 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 63d82327-aa52-32fe-8ae0-4f95bb54444b | -2.40424 | -48.54455 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f37ccee6-23df-34fd-9468-68020f727427 | -2.40347 | -48.54958 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d516eae2-9e41-3317-9acc-59b05cc7f1a8 | -2.4003 | -48.54393 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f0466f5e-828d-378c-a4c8-a0d5e84e9e63 | -2.39953 | -48.54898 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b53340e-eb06-3515-abc0-0311023ed287 | -2.39636 | -48.54332 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a90fefdb-c4ee-3442-b86d-a4956ad71c9f | -2.39559 | -48.54836 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e04761b6-e098-36d6-9be7-028edbfbe635 | -2.3902 | -48.58354 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c7a3efe-a787-3a07-bc53-5608e1afe23b | -2.38867 | -48.5935 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec48943b-e651-3997-9b9c-efbb7e5f7a25 | -2.38627 | -48.58293 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9684c72-24c8-30dd-bb34-d9592bd09175 | -2.37982 | -48.54589 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 68c17af9-0016-3357-a8ea-4629fab8523e | -2.35043 | -48.42638 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 914f4226-960a-3243-8173-9a73d59605e5 | -2.33983 | -48.57056 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2acc258e-8e5e-3a99-83d7-eed7415c50db | -2.33941 | -48.57422 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| db3262dc-e531-3924-b811-f8c54dd1365f | -2.33908 | -48.57558 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f58986ea-5753-3839-83e1-2d5be2864704 | -2.32972 | -48.58435 | 2024-10-28 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a6c90f7-c505-3ebc-8ee2-397b43a7a774 | -2.30539 | -48.402 | 2024-10-28 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96d40428-1296-3aa6-ae1b-024499811a6b | -2.29511 | -48.81596 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7338731d-68a6-3cd8-a715-88b43a27dfd3 | -2.29379 | -48.81413 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fbb5bcd-b1fd-332a-8b13-62dfd5bcea55 | -2.29124 | -48.81534 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8b5eb89-1fb2-37a6-a6aa-c52ad04ec271 | -3.46032 | -47.67124 | 2024-10-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aca05cd0-4b69-392e-9cd7-be3d97fbe049 | -4.29879 | -48.64787 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb8eb83d-e934-32db-bf4f-3618846f3fa4 | -4.29828 | -48.65134 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a567293f-b0ee-3715-ae16-1f5e732d9a3a | -4.29776 | -48.65483 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15512dcf-7540-3b97-9f3f-d0460a83e36f | -4.29646 | -48.60773 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daffdd9f-5cfc-3876-8ac5-79ff39e5e190 | -4.29542 | -48.61481 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e20eff15-c498-3926-b995-152ed4569877 | -4.29489 | -48.61839 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10017dc2-9456-347a-8b47-793234ed1611 | -4.29191 | -48.61063 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9df082ea-2138-35a4-81a4-9c15e2567449 | -4.29139 | -48.61418 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81f2400c-d89d-3ad5-bad2-804a431c1862 | -4.29126 | -48.64309 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8323b94b-6530-3553-9b6d-7dd0919840b7 | -4.29086 | -48.61774 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69047423-3fd2-3b63-850d-0c8967c9674d | -4.29075 | -48.64658 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8bb903f-ff31-3464-b5d9-cfb20a214d71 | -4.28972 | -48.65354 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff680de1-cbe8-39da-bd02-fd78415b5d0b | -4.25033 | -48.55067 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5109317e-fdf8-36fd-af99-25b7e17bbafe | -4.24979 | -48.55424 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e16cc9f-79d0-39f8-be6c-91e28f0c70c8 | -4.24574 | -48.55363 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 673c515f-5693-3f88-8188-5e50dd8cd629 | -4.23658 | -48.55956 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6172506-af0c-36dd-b26a-2fcfe57e7db3 | -4.21791 | -48.04673 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f28477c2-19d1-38af-878a-d7d2c6c6bcae | -4.21431 | -48.04219 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03d8aabf-c284-3600-b7a0-ae16e38b79e3 | -4.21318 | -48.04967 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec39f188-d2b2-3095-9206-216131da6e75 | -4.209 | -48.04906 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6feb7c7d-cd84-3959-a65c-aa0068315ac1 | -4.20426 | -48.05214 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98a701e4-bd21-377a-841c-b7378d9ce40e | -4.18281 | -48.05256 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 086fbfc7-337b-38cc-99ab-8f51bc690114 | -4.15102 | -48.76103 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README52.md)

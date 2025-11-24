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
| bd407132-83e7-3f04-8223-1910746caaf2 | -4.53801 | -45.50386 | 2025-11-24 00:34:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 8b7ba0d9-292a-3bbd-9cd3-2a23bd8c49ba | -1.4924 | -45.87387 | 2025-11-24 00:34:00 | TERRA_M-M | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fea8d4d7-a774-3597-b662-20e26220060b | -1.21949 | -46.39072 | 2025-11-24 00:34:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 85666e04-4288-3291-8a9b-9f3854033dde | -3.33994 | -45.64411 | 2025-11-24 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9ca76225-86f2-3015-973a-705d407c70dd | -2.28399 | -46.02661 | 2025-11-24 00:34:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 25e33f1e-d6bf-3d0c-80e6-9944c3cd08a5 | -3.72695 | -45.9235 | 2025-11-24 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 068effbc-67e9-3caf-bed3-342e86c359fb | -2.55906 | -45.62819 | 2025-11-24 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 90cf9966-db7d-3dea-8860-288885d3fd8b | -2.12704 | -53.42904 | 2025-11-24 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 20dc5549-3dbd-3d9f-9388-b00799741eb0 | -2.87958 | -48.99949 | 2025-11-24 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f559087e-04e0-3c0f-b129-5da851198766 | -2.56733 | -49.08219 | 2025-11-24 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 38ab7457-dda2-3363-b901-9407f4646397 | -2.28021 | -53.80851 | 2025-11-24 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d28e89e-9289-3326-9a56-bac5f7693dfc | -3.17306 | -50.24989 | 2025-11-24 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ce2e079b-b572-3828-b48f-d542644e54e5 | -2.7351 | -45.90791 | 2025-11-24 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7d55941d-8da5-3d68-bf5c-b3ffc6665d90 | -2.79433 | -45.34685 | 2025-11-24 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 68682f1d-72aa-3bef-9873-a1e614ec8a58 | -3.93168 | -45.37873 | 2025-11-24 00:34:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a65b6d52-1868-3149-945a-77ad616507fd | -2.13215 | -46.42126 | 2025-11-24 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 3688fa35-d6c5-351e-95e3-aca4ad4658f9 | -2.79685 | -45.36443 | 2025-11-24 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 15fe81fa-ff37-3e64-9ee2-d9caf2ebe847 | -3.20858 | -45.75833 | 2025-11-24 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7910bf1f-560d-3859-85b1-62fe40431f20 | -2.28619 | -46.04246 | 2025-11-24 00:34:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 27ac6c6d-6605-3b1e-b917-1d23393af850 | -3.27863 | -45.4388 | 2025-11-24 00:34:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2a90ed60-bd80-3929-848b-06088a4487ba | -3.27207 | -46.03681 | 2025-11-24 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7024442b-f751-36bb-9ff0-a2587230109c | -3.2662 | -50.98492 | 2025-11-24 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8504eb18-695b-35cd-a23f-ffe7ceb7aad6 | -2.87186 | -51.80577 | 2025-11-24 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 3f1a2362-5956-3761-8417-743bcae5207e | 1.00973 | -51.31425 | 2025-11-24 00:34:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2b04e974-f6f1-3f60-b08a-36995119060f | -2.14244 | -46.41309 | 2025-11-24 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 9ec4536a-f658-30f4-a34f-2003e7d8e2ad | -2.87815 | -45.29258 | 2025-11-24 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| de8c957b-f777-39e4-8ff5-a53f86ef87ce | -1.71461 | -46.47521 | 2025-11-24 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 691ef201-5740-3aef-ab2a-4c08c45c11fc | -2.13005 | -46.4063 | 2025-11-24 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 11b6c115-914e-30c4-9cbc-a172c797ed86 | -2.14342 | -46.41953 | 2025-11-24 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| d1278cc3-9752-3db6-a9b6-b235d1c46072 | -4.71188 | -46.46373 | 2025-11-24 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 156.2 |
| dd6cf862-ba55-3579-80b0-47d7a23cd90a | -1.87468 | -52.58937 | 2025-11-24 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9af49938-4557-3b85-9ef0-b85b8aba4c42 | -2.12604 | -45.34247 | 2025-11-24 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| afb38031-17ee-3fac-a5a8-88588d301faa | -2.88781 | -45.27294 | 2025-11-24 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a99b8595-256e-3d1e-8347-45adb3773a83 | -1.82946 | -45.57362 | 2025-11-24 00:34:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 17139fdd-564b-3cce-bbc6-99ec8c761f49 | -3.72699 | -45.93257 | 2025-11-24 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 6d7afb90-ab83-3607-8b4e-89fc270b5b9c | -1.33116 | -53.18513 | 2025-11-24 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2f848bbd-61f2-36e8-a502-0733b4cb3c52 | -6.5725 | -47.88982 | 2025-11-24 00:34:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b7d39cc8-cb22-39e6-8042-868fb78da236 | -1.71676 | -46.49006 | 2025-11-24 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 58afd318-ac58-3dff-92e3-b6b4dc30a09c | -3.04541 | -45.09047 | 2025-11-24 00:34:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| be0d4d7b-32ab-3046-a6e7-bd70bee3b69d | -1.36422 | -53.16499 | 2025-11-24 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 202ce26b-080c-33c2-abbe-5383ff8c01bf | -2.88198 | -51.81344 | 2025-11-24 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 602bcac7-a4df-3b76-8209-a6e0ea814212 | -2.88322 | -51.82236 | 2025-11-24 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 865e3859-bd96-3de0-aa4e-a9150519ca32 | -2.7618 | -48.95127 | 2025-11-24 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0d490f24-2e11-33ed-af50-93c746e80cc8 | -2.12342 | -45.32433 | 2025-11-24 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 58d9546e-1e3c-3781-bdc0-d23f5507f121 | -3.72912 | -45.93881 | 2025-11-24 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e5877a1a-f50f-3fdb-a9a5-472b93c98b18 | -1.22217 | -46.39698 | 2025-11-24 00:34:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 07eb2230-5913-37ea-afa6-f6cea09acd04 | -4.06476 | -47.30692 | 2025-11-24 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4b3a6d5b-1b05-3b39-8fe0-83cb6a14b4d3 | -4.38758 | -45.73037 | 2025-11-24 00:34:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e90d32d9-f168-3065-82ef-df94fac78dc5 | -3.82476 | -48.98705 | 2025-11-24 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4c040223-9b0a-3e2a-83f5-5bcfd62bb25a | -2.8676 | -45.2607 | 2025-11-24 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1d190c6a-d694-33b9-9ad7-6033f7b621de | -3.2175 | -45.9423 | 2025-11-24 01:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| b4707907-8ab6-3925-9a24-a9554729f9c4 | -4.7204 | -46.4497 | 2025-11-24 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 011218d9-8dca-3a3e-87f8-a42df4779d7b | -4.7203 | -46.4719 | 2025-11-24 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0087f3e8-091f-3eae-9c21-f89b118f1e9a | -1.4921 | -45.8795 | 2025-11-24 01:10:00 | GOES-19 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3a3b28e9-85cd-361e-9595-1a2480fde645 | -1.7131 | -46.4744 | 2025-11-24 01:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2c13d718-8199-35ce-91cd-45c73d9b2858 | -2.8862 | -45.26 | 2025-11-24 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ba661d88-3843-39a1-83c4-d7e892d5c360 | -4.5213 | -45.6131 | 2025-11-24 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| caf2f496-aa4e-3709-bc1a-e7c9965e8d87 | -9.53874 | -35.69279 | 2025-11-24 02:55:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d69d0dd1-b7a1-323a-91c0-5e68daf2bf43 | -7.03514 | -35.00343 | 2025-11-24 02:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8f9fd8eb-5073-35e9-92af-b073513cdfcd | -9.54806 | -35.68864 | 2025-11-24 02:55:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4e190ac8-bc92-3081-bc07-d9f86ac23c93 | -9.60359 | -36.11194 | 2025-11-24 02:55:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d0eb0a86-ec56-3ba7-9b67-f344ca4e67c4 | -9.53764 | -35.69829 | 2025-11-24 02:55:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0db32fa6-4631-3fa7-a939-0b7416d81bde | -9.60699 | -35.8648 | 2025-11-24 02:55:00 | NPP-375D | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9f4cffe2-4082-3e65-a334-e756c11b00e6 | -9.60578 | -35.8597 | 2025-11-24 02:55:00 | NPP-375D | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 381f62a1-b53f-3b10-ad29-82c4d08c6cc8 | -9.54155 | -35.68731 | 2025-11-24 02:55:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| f8950c21-78d9-33eb-9ddd-ebfba836b8ae | -9.7608 | -36.39368 | 2025-11-24 02:55:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 630acb67-9741-39ca-aaaf-0ffa6f294f4a | -9.60467 | -35.86522 | 2025-11-24 02:55:00 | NPP-375D | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 7c656384-22e1-3ac0-a3aa-74d25cc1256d | -9.75958 | -36.39977 | 2025-11-24 02:55:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 65e3218d-9450-3a09-a044-a44e6481b5aa | -9.76758 | -36.39494 | 2025-11-24 02:55:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 2b3de84f-c897-39cf-ad74-7863017aa299 | -9.61028 | -36.11318 | 2025-11-24 02:55:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| deade15e-051d-3caa-902f-2af0dbf959f0 | -9.54048 | -35.69284 | 2025-11-24 02:55:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3559d1b6-92a5-3b9b-92fb-2be58db410fb | -7.0341 | -35.00898 | 2025-11-24 02:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e48bf3e8-265f-391d-81ee-3a6dc4a6858b | -9.60807 | -35.85924 | 2025-11-24 02:55:00 | NPP-375D | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| cca1f43b-1aba-3085-99e9-17efa36ac723 | -9.53983 | -35.68731 | 2025-11-24 02:55:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 101da34b-e943-3a97-8d0d-bac0aba61830 | -9.54637 | -35.6885 | 2025-11-24 02:55:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d48b5f93-6f33-306e-8cdb-c2f62fffe3cd | -9.61143 | -36.10738 | 2025-11-24 02:55:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0df6eaf7-338e-3ad0-b69a-94b6b5a98ca8 | -10.07454 | -36.3569 | 2025-11-24 02:55:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a4ce0c3a-c01e-3151-956e-c864f2f2e350 | -9.53942 | -35.69839 | 2025-11-24 02:55:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 890fc3ad-1187-3d05-9515-49161d3c3db0 | -9.76634 | -36.40115 | 2025-11-24 02:55:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 7334c5c5-0ea1-3658-839f-58803cd85fe9 | -4.26573 | -40.86495 | 2025-11-24 03:17:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 154d1233-20a8-30cf-8697-f1485e877b53 | -10.07157 | -36.35667 | 2025-11-24 03:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ea68f697-f8cb-30a7-9212-2ca2d12cd57f | -4.26468 | -40.87087 | 2025-11-24 03:17:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e67d0f17-a03a-38c7-9eb4-6b46c03de85a | -7.37407 | -35.21144 | 2025-11-24 03:17:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 76dbf337-3476-3a09-b5d7-76aedcd909d5 | -10.07602 | -36.35751 | 2025-11-24 03:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1e4025d8-f7c4-3977-8e7b-fe143119486a | -7.37048 | -35.20656 | 2025-11-24 03:17:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6ba1973c-062c-314d-b7ef-9bfa8950b149 | -5.69935 | -37.95095 | 2025-11-24 03:17:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9089d1c4-34c2-3dfe-96f6-06b21ec6db52 | -5.69993 | -37.94757 | 2025-11-24 03:17:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 771d0515-535a-3562-b198-8bddeeaeebdf | -7.03811 | -35.00167 | 2025-11-24 03:17:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 90f2c870-4aa6-38eb-9579-8dd41d14b9df | -10.07236 | -36.35223 | 2025-11-24 03:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 4f32c6d4-22c8-3d0e-abbd-77f1e8287974 | -7.3728 | -35.20842 | 2025-11-24 03:17:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2ac0d1bb-b0b6-35f2-9f0d-9ac6aa70d5ed | -7.37209 | -35.21267 | 2025-11-24 03:17:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a3100547-f77d-3f4c-94e3-f89dcd3c2a36 | -5.70302 | -37.94894 | 2025-11-24 03:17:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cbfa9dc3-4d41-3ff7-9e44-1e63bec88445 | -10.0768 | -36.3531 | 2025-11-24 03:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 13.9 |
| b1490740-7b05-31cb-b136-8bf68ec8756f | -4.0299 | -42.08531 | 2025-11-24 03:17:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 241e96a3-db25-3aee-81e1-4315713a4e1f | -4.39181 | -40.68174 | 2025-11-24 03:17:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 157f9a4e-15d7-3971-b2ef-f87f780596bb | -10.07315 | -36.34772 | 2025-11-24 03:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 1a3a8026-44f8-3b42-8edb-a819c3c9632f | -7.83286 | -35.22309 | 2025-11-24 03:19:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e4fc7df5-d1a8-3a43-a699-77b3065b5c6c | -8.22358 | -37.38899 | 2025-11-24 03:19:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d91936c-a47a-3e14-bfa1-6251a20a8b56 | -7.83356 | -35.21908 | 2025-11-24 03:19:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| edfb6196-e0b9-3087-80c5-e7a45383266b | -7.83784 | -35.21978 | 2025-11-24 03:19:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)

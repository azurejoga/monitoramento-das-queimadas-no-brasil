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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c6a3173-d727-3edd-99b5-620db219187d | -9.08945 | -65.74008 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9b36ee21-8ca9-3216-8bc4-545dba4a4c6e | -7.34805 | -59.65812 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4deaa9af-917b-3a6e-8622-07904902d85e | -9.16156 | -59.55305 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06110f23-0e71-359b-adc9-946f7f4f160b | -10.32592 | -62.62085 | 2025-08-28 05:25:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eed63ad5-f735-3d59-93a8-f3757816d504 | -6.92426 | -62.94289 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa554b25-aca5-3c57-b1bb-ee7d93d378fd | -9.11408 | -65.78616 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| fe549d8c-1e02-38b2-8303-4c480175519b | -7.56385 | -63.85851 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8937dc96-7f0d-3935-ae7f-5a11c5ec7610 | -6.92901 | -62.93571 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46a75eea-1d13-38ba-b7f3-4f1d67557f32 | -9.2669 | -59.77456 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1287a729-ea8a-3c7e-a354-7afdcab5e4ea | -10.80441 | -60.77479 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6176513f-ad92-3702-b28f-335a007186cf | -9.696 | -61.28249 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 018ac89f-d543-38e3-ade2-4cb3f9163c6b | -7.34861 | -59.65458 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d1df3ff-9c72-3b0f-a006-4a3e65f9b2df | -10.46718 | -57.95535 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 804a4ef8-177e-3d33-a4ec-9e16c7c6cf57 | -8.63685 | -62.6513 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e1b12bc-9cd4-3f88-af29-7b6e29d62ad5 | -7.54494 | -63.83815 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1a3ff17-5cae-3224-9a3b-59c79dd9f983 | -9.45488 | -51.9531 | 2025-08-28 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d8754993-382a-39bb-9efb-ddae7e6ab9ea | -7.55217 | -63.83935 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65e7847c-02c2-3d4c-8762-928b86d2b5fc | -8.84906 | -69.11091 | 2025-08-28 05:25:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e47574ab-7bfe-34bd-9714-b7a2696a28b2 | -9.19021 | -60.80391 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b127065-d391-3394-9421-bb13d1518bd1 | -9.79094 | -64.25576 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15b57502-78e2-3024-924e-c6b1e9df7c6c | -8.91403 | -60.71342 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51f94e58-1e25-322b-ba54-035ff0760b45 | -13.00458 | -56.90437 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c338ad70-18a3-3995-bbbd-c6bb431aa2f9 | -9.46077 | -51.94981 | 2025-08-28 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 165ce274-864a-3173-82d1-660ec6e1ca8a | -8.94012 | -65.95197 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1bf9983-1c13-32d3-923c-50b14e72bd69 | -9.40823 | -60.57588 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 855d99d6-b445-3260-9bf9-f9cdf92b0b54 | -9.80403 | -61.20293 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92fab0ad-62ce-3a1b-abee-ff9436bf92d5 | -9.06701 | -66.06093 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b40e07ab-0748-3a63-968e-6a777a7e95c9 | -10.07831 | -62.89933 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5441ee45-82c1-3b2e-a5cb-3e2a1125b2d4 | -8.57494 | -63.93017 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84de19be-a49e-3e98-948e-012782fb00c0 | -10.81608 | -60.76575 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea7a07c0-a17e-3d15-93eb-6198df4deaff | -9.50695 | -62.78018 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c501709f-5599-3f00-b43a-d6f95e014ae5 | -9.66631 | -48.31628 | 2025-08-28 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce6f5e0b-bcc9-3068-a6b6-38160c61debd | -9.47266 | -57.84213 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b568be4-6f57-3e1d-adfe-010488d809fe | -7.27784 | -60.29399 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9063f8c-6ffc-3b12-a9d9-20a5ac4e4bc5 | -13.6026 | -48.21675 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a521bb1b-f2a2-318b-b908-a4fce2db91fa | -9.1186 | -67.70634 | 2025-08-28 05:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7db86dbd-cdc0-3bfb-aee2-cb3b2eb08129 | -11.37642 | -54.34796 | 2025-08-28 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a437c878-bfd8-3e34-8173-d32a17fd618b | -10.2781 | -64.49089 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d43001e6-866d-3abd-bd42-ba26aa70d9c6 | -9.02433 | -65.70042 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f0d667a-fa0e-3c18-88a6-42b8dbfa0784 | -10.80328 | -60.76008 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47e00e80-88c6-3785-8aef-c6bd3aa31220 | -9.65944 | -48.31619 | 2025-08-28 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e87ba874-27a7-3822-9c44-931fbf9b4f40 | -7.28449 | -60.29504 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e1d6d4f-fbc0-35f8-8ad6-90f5e11509b8 | -9.7356 | -64.90214 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41ce0c2f-457d-36d4-9a25-6ef7b00612b2 | -9.41148 | -60.53313 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc06506-70f2-3f2f-b8a7-96f3d88bb2cd | -8.34827 | -62.93901 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf121123-df81-3850-a1b6-a55cf9d7ad60 | -8.10504 | -71.25016 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3364680f-0cbe-3574-b4d7-76a086bf7682 | -9.12285 | -65.78249 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 56ffe8d3-616d-3b3f-a5b4-32aaf67e1f27 | -9.13731 | -65.76926 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b95bbfc3-7acf-3380-9371-496bd65a01af | -8.94936 | -65.94633 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38b3eed1-84a4-3719-98b8-446b82c59abf | -6.9004 | -62.93501 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1084b137-6dda-3843-9b81-38bc7580f450 | -10.46974 | -57.93785 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a63ca57e-3f66-3862-af5b-ab1e6ee85798 | -8.09832 | -71.25459 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab758666-4c2d-3d80-a134-2e2398ac8a64 | -9.00683 | -65.70782 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f818ea5f-b06f-3ccf-998f-661a0544426c | -12.44347 | -48.70985 | 2025-08-28 05:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6602a6b5-501e-3131-9845-d6a1123ed4e4 | -9.5525 | -63.20964 | 2025-08-28 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b0040f2-6e7b-31be-9b8f-28db9dca0052 | -9.13645 | -65.77438 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55c869a6-f575-3d87-b43a-b33ea1fd9c24 | -9.16608 | -59.56881 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23c92f73-b8d6-3853-808b-7be5b85f8d4b | -10.1888 | -68.42645 | 2025-08-28 05:25:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65265d3a-54a6-30b2-aadf-cd9314b06e44 | -9.25689 | -65.90508 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12d77b00-9401-3b27-8298-3df31737fa29 | -9.41705 | -60.54123 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d69389fb-3e1c-3749-9a64-edd05d4434fe | -7.46721 | -61.38843 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 050b8e8b-a88c-3571-a5a3-51e0be9725f0 | -9.64569 | -59.62733 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 223131d6-3a61-324e-9054-71959755a18d | -13.73045 | -51.9087 | 2025-08-28 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f95aa441-e761-348a-ab0e-a39115239040 | -8.2417 | -61.4548 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 527c4b22-3de2-3a5b-8bb7-2e6f9743ccb2 | -8.34482 | -62.93843 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e01117e-8cea-37b8-bc37-5bd14b1554dc | -8.57426 | -63.93431 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e9ab0a4-0662-3858-97ac-fe6469622353 | -7.43512 | -60.02524 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac5b0392-56ea-3e95-90c2-d40aac79a7a9 | -11.23409 | -55.06281 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7a4adda-b6d4-3ecd-9e6a-fc0568469716 | -7.5704 | -63.8639 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e7484cf-8e93-3805-ba37-7743590be149 | -9.47428 | -62.37875 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87b52d46-21d9-3e2d-a886-30cfa5b7b011 | -12.81908 | -48.14432 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad721487-6186-344f-a91f-7facf8ef5359 | -9.10561 | -60.3266 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7eaf29e6-910d-3b1d-b7e7-3c3f5cc56776 | -10.42503 | -64.37333 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa6d0b29-9246-3300-8452-6d37ec4c18b5 | -8.68849 | -62.87001 | 2025-08-28 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1e01797-2402-3a75-976c-202bfd1a18af | -11.22136 | -55.05651 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 110e915b-3a76-32ac-af7b-638fc41c59fc | -12.70514 | -48.17115 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 330e9be3-4ad4-38d1-958f-81a8610797f1 | -9.82638 | -64.28751 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b62f607-19db-3f3d-a003-27f60e9b3e40 | -6.9074 | -62.93615 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96c29d0b-f628-3558-96c1-5d4f3d29d05d | -8.25781 | -61.46101 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76fb0391-8a95-376e-8bff-523efd7baed2 | -9.1421 | -62.35811 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a58ae0-4ab7-3080-868d-631afef97c23 | -9.15535 | -59.57082 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e245bc45-482e-35e6-8ccf-f784afda47b2 | -9.14305 | -60.77853 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f10953c-4484-3e3a-b051-bca810426dfd | -11.23855 | -55.0634 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b782d48-e9c0-34a0-8b5b-58e84390d8b6 | -7.34709 | -57.62863 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74be48e7-3155-3518-af7a-fcbd2da7fabe | -8.69436 | -63.83913 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.7 |
| a9f8ab36-6d25-3908-9168-51daff327f54 | -8.57495 | -62.6039 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac56dbe1-05aa-3003-a4ae-1dcdbbe38a0a | -9.50916 | -62.78809 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14e297fe-f7fc-3074-8f7e-6d0acefaf750 | -9.10524 | -65.7428 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 003636d9-6b4b-36b1-b9c7-5bbc2176337f | -9.09032 | -65.73502 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| df855618-dcb7-3618-907c-8dba5a06eecb | -12.99652 | -56.90308 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0f2d31c5-bd29-3e9e-9ab2-a76420a4f144 | -9.12112 | -65.79266 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b07c7663-1dd6-3bb0-84b3-6ae53ca7706c | -5.91645 | -61.30409 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db752ab8-80e9-3a6f-8a7f-1314c15f62c8 | -9.05781 | -54.94024 | 2025-08-28 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68895a06-b0ef-374d-a094-ee455f607f36 | -9.10227 | -60.32607 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2287e46-3dac-3386-bb9f-723da45c4b9f | -9.22013 | -60.80872 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ca3e808-65df-3dd4-a8c9-47a32b3b7b63 | -12.79563 | -48.16211 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f78f4621-c625-35ab-afc5-8bf575757f79 | -8.93393 | -65.94009 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b49e2eb-3135-3397-a440-63c7f005e51f | -8.60639 | -64.07907 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75e5587a-2d5a-3773-a8df-934bd4ecdf17 | -10.80107 | -60.77426 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 577df8dd-1282-3a59-a664-2d4b6ec501f4 | -8.26472 | -61.45485 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README72.md)

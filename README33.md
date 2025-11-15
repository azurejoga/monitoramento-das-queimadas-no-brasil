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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2383d15-2eb9-3e98-9d77-f21562c27c2c | -8.74543 | -48.32052 | 2025-11-15 04:25:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c76a9f85-a9e6-3844-bfca-6c86469700f2 | -7.54961 | -47.25302 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 980bb07c-f74a-36f2-8b26-9867377f3ad9 | -6.81952 | -48.82481 | 2025-11-15 04:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7139e7e-2240-3c45-8429-c10b8e885dcf | -7.35794 | -47.28305 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6536a64c-a9d8-3a8e-8b14-83e50e0309d7 | -9.12656 | -47.12408 | 2025-11-15 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e90ba5e0-a855-3db4-b36b-2f3e3e042547 | -3.76166 | -47.74777 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a25db74-0252-3087-82ad-f7c3930f3086 | -5.56299 | -46.54005 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e883f76b-74a1-3cf9-9e1d-e2d38a461393 | -4.01302 | -49.01603 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6420d1a-0bd4-3b61-8367-d0d9b9c9b836 | -4.85866 | -43.25547 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7eb7a611-be26-3679-81ad-9410cf4c66fb | -9.0142 | -44.17854 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca8cb8bd-225c-3632-8a88-a9d06d530844 | -5.22611 | -44.06753 | 2025-11-15 04:25:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2579302-ff01-3a4d-bf9e-b2e7bdf33564 | -3.69382 | -44.16473 | 2025-11-15 04:25:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01bdc1d2-cdfc-3b87-b141-d46869b02cbe | -5.59436 | -45.80312 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 697b36bb-14dc-37a7-b719-1d2e8fc2d85d | -5.09931 | -37.78406 | 2025-11-15 04:25:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6105c4c7-a616-3f3a-931c-3a3b03ea1b4b | -3.26329 | -50.09139 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bf4e12a-4720-3f10-a732-dd3ae07b1ba9 | -7.53364 | -47.2039 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce368753-e266-3926-a19c-dcd281e50110 | -6.65633 | -44.26608 | 2025-11-15 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eedd033-8f6b-3227-b514-40ddb21ba136 | -4.46661 | -45.65004 | 2025-11-15 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3764adef-571e-35da-947b-0d34d401e27e | -7.52812 | -47.19585 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73ec8533-cbfe-3090-b0ff-7a699968c3d3 | -3.70644 | -42.75077 | 2025-11-15 04:25:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a941c8b4-bf26-3967-85d1-66d45a522c6d | -3.7554 | -45.87239 | 2025-11-15 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46e12954-809f-36f6-b893-9abc32730dbb | -6.33116 | -47.26313 | 2025-11-15 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ed8eec6-75a7-3f60-becf-35411f93f82c | -7.73896 | -44.57983 | 2025-11-15 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd0972e3-6b78-3bd5-a601-925b98466440 | -2.86533 | -51.4779 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ded523bb-8f93-337a-8862-7e7ff883a2c6 | -1.91539 | -47.91409 | 2025-11-15 04:25:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0691273-dca8-384b-9106-0d509eebb5eb | -5.74937 | -42.72199 | 2025-11-15 04:25:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fbc562e3-2571-39dd-b54b-d97d99218666 | -2.39022 | -48.18361 | 2025-11-15 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4070e590-a89a-3741-824b-4e713f4bf556 | -4.64259 | -43.5803 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90a58ba8-5249-3470-b2cc-54fbef40b8bc | -9.80692 | -42.20802 | 2025-11-15 04:25:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d456082a-ce0b-368a-8dc8-e7a9027cb21b | -4.86482 | -47.38409 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c17764fb-617e-32f5-ad19-b8818aed6212 | -3.2835 | -45.45987 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09bfea70-565a-35dc-a59c-a71a8a8e498e | -6.15125 | -48.04888 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 605b16a4-ed9e-3add-915f-541a7df8504f | -3.05573 | -47.11493 | 2025-11-15 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c94a1f1-d68d-3aef-8b0b-191544654586 | -3.85866 | -49.13637 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d15914d-2d1c-3987-ac14-cc31d92c3083 | -9.14018 | -47.76507 | 2025-11-15 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb746280-7e5a-3d6b-ba72-1369a9d0a89b | -9.2595 | -45.19584 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1f0eadd-2287-3242-b6e0-34c143a7b564 | -8.31958 | -45.40261 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4eec02fa-c30f-3a37-91ec-10dab2fe2683 | -1.62182 | -54.71693 | 2025-11-15 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe1c3a71-e784-3cfb-abf1-3d72302fa59d | -5.58104 | -47.10709 | 2025-11-15 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f56b581-6ec9-3a98-bd40-d86172f40c45 | -4.81039 | -41.61501 | 2025-11-15 04:25:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6e8db6f8-c06d-35c6-a3f6-f1420cf19155 | -4.91702 | -43.29966 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 525bd230-c277-3735-8c7c-5197cd2981dc | -4.87664 | -45.70047 | 2025-11-15 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7761f708-fbd6-37c8-8fb7-8df21d7550c4 | -9.19984 | -45.6996 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f27b5266-efde-3b4f-bd39-d4ded7e8b5b7 | -4.39328 | -44.0822 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45c50f47-cc4e-357c-b0d5-49cef65d6f9a | -4.27103 | -46.84245 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03a90413-cbbc-3e2a-8d6e-61ff266985ee | -4.18161 | -50.42552 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16fc35bc-85ce-36b1-bd70-97e9cc49d87e | -3.26248 | -50.09633 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32cf3098-177b-34bd-a6fc-d805b4762099 | -4.29643 | -49.20961 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 098e0ca0-9fdd-3095-a1e3-97719a882053 | -2.43145 | -48.03964 | 2025-11-15 04:25:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 884e2608-0991-30ca-a118-50b5bfc13783 | -4.60953 | -43.2994 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96a15418-84b2-373c-b080-6e603bee9d37 | -8.06288 | -47.16702 | 2025-11-15 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb06a986-1356-374b-9928-dbe45d4df78b | -3.37165 | -41.16903 | 2025-11-15 04:25:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fe86bc0a-713d-368b-b57b-4cf16bb25734 | -7.26589 | -48.03097 | 2025-11-15 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f6c4cc8-3216-3513-ae8c-1195484ff6be | -8.32239 | -45.40669 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d47d3f4b-03f9-3f39-8998-ce4cb20228ad | -3.70613 | -46.03391 | 2025-11-15 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf56075a-3fad-3d5a-8751-85b93dd53f3d | -4.88043 | -44.96136 | 2025-11-15 04:25:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c48ee3f-09c5-31d5-834c-1ebd1bdfd35c | -6.10032 | -41.71283 | 2025-11-15 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 707850e7-6a31-3a8b-b72d-3d655ecf5c4c | -4.3541 | -46.49063 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2a87c55-5829-36a5-a3a1-bd0ce2661a25 | -2.74127 | -45.30088 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2372fce1-f956-352a-867f-4a841ea761f4 | -4.6448 | -45.42369 | 2025-11-15 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aec9a36e-14f4-31ca-a82a-08516cdf9d2e | -7.6697 | -47.20395 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db02585d-7ebd-3666-a7aa-27eb57729a80 | -5.0884 | -43.29134 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02141796-385e-3bb6-bac5-872bb2b11bcb | -2.95516 | -48.58679 | 2025-11-15 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 318b1edc-330c-30a6-abc2-5bc6cf4eb3f0 | -4.54287 | -43.21411 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| ac397de1-bee6-3323-acf1-15c45ee3f89a | -3.52356 | -56.31921 | 2025-11-15 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab992288-d167-36cf-9e23-4ef1ea754923 | -3.78232 | -42.45086 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 395b3cac-4988-37f4-9e2d-aca48c72a6e3 | -4.66896 | -45.0542 | 2025-11-15 04:25:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6a7579d-044a-3ec5-bc7b-88ec386dddf0 | -2.79864 | -52.97015 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08df0c7b-ea00-3fb2-86dc-42e137e652b7 | -6.49725 | -43.95969 | 2025-11-15 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d619e156-82e3-371d-8b7e-658de5f0e9d5 | -6.11293 | -44.22292 | 2025-11-15 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eccaaa97-a4d1-357d-a584-4c0dd1244eb5 | -3.72889 | -50.60719 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd89f109-6327-307e-a66c-4d9e92c46d88 | -8.64698 | -45.46006 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d57ba657-889b-301e-9624-2a3e35439de1 | -8.19142 | -44.82667 | 2025-11-15 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c70c9edb-f818-30b5-969c-7576c6fbae72 | -3.90581 | -45.80093 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f909ade4-ad54-3635-9929-85ba59c6bbbb | -4.32419 | -46.37933 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4bc890c-fe6e-3cdf-9279-486d0010e59d | -3.47609 | -50.03778 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c413b090-340d-3e19-ab5a-2b094b728bda | -7.4414 | -42.76787 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 514e2967-8e1a-34b0-8141-c50d699a7e4b | -4.24956 | -48.20403 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a4b041ca-d504-3c00-bb7c-c9e5732bc2f7 | -4.22383 | -46.09085 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02744fe1-77bc-3a55-b66a-17c2d81d82e5 | -5.23098 | -44.35069 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 93802eea-cba6-333c-b97c-43e4574b8c4b | -8.84825 | -47.33615 | 2025-11-15 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bafd2c25-905a-341e-968b-b656caa1db29 | -5.60624 | -45.18578 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0dd711b-a877-34d6-99df-c6b5492b6802 | -9.85366 | -44.16906 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 448a9d0d-70e9-3866-9e12-382afd006c72 | -4.72626 | -47.16039 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e65959a6-6ba8-336a-b5c8-66e230ccd2da | -6.23885 | -46.3927 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5678bf72-6f2b-3c22-8a0c-44e13e8713b0 | -7.39312 | -48.65933 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0e11424-0fda-3c65-a000-828883dd5030 | -3.73615 | -39.59805 | 2025-11-15 04:25:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 018991c3-fac7-304d-a314-9cd86ae48d6d | -6.3284 | -47.25907 | 2025-11-15 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa1784bf-ac57-3e57-9742-8e4fbcb79f5e | -3.98706 | -44.26464 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ffd34ee-4c64-3006-9041-67d7a68b8b90 | -3.5301 | -50.87697 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db60ded3-86cd-3745-a248-5af6641adac1 | -4.2783 | -46.06763 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f930eab4-b3d6-3ce0-8fea-f08efe2afff5 | -4.91112 | -44.04359 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f23e654d-635d-3ec6-adf7-8f3741f0db2d | -7.33261 | -46.15499 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c103544-08f1-3b99-8ce1-800f91858e76 | -8.32184 | -45.41023 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3933aacf-78dc-30f5-9c5c-ab217bc473e0 | -7.87844 | -48.4142 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca39ef97-8f08-3ce9-8475-0a26aa2599f5 | -5.75671 | -42.72284 | 2025-11-15 04:25:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ef845738-a0e4-3523-b01f-9f30cb51d49d | -8.46155 | -45.14301 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2f59faf-0f77-3112-811a-99419022387d | -3.76913 | -47.74512 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c85521dc-4009-337c-9c2c-f5b5e80e9864 | -7.72397 | -42.34632 | 2025-11-15 04:25:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39c49d69-73d8-3ffd-a33c-a6098322f2dc | -5.57951 | -47.09967 | 2025-11-15 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README34.md)

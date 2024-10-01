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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd3ec1e5-d4a0-34a7-bd9d-f80ea4df1fe4 | -16.46319 | -57.34973 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6a01c842-a6e5-3114-9666-bdf105e8647d | -16.46033 | -57.33319 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| eb2b17a6-1798-31ba-83df-ac53db946541 | -16.45409 | -57.42131 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 082b624a-8cda-38c7-b702-4d70ad3b2388 | -16.453 | -57.4263 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| ac9ffef2-0518-373f-aabe-9760a2e17b3f | -16.44793 | -57.41978 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2dfa25e3-b8ef-3e2d-aec3-4e5db33e23ac | -16.44685 | -57.42476 | 2024-10-01 04:17:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 4afcc213-11f2-34a2-95a2-110225a2c973 | -17.10164 | -56.73405 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| e648798d-774d-3016-b7f0-e20d5cb9d715 | -17.10068 | -56.73847 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| da2e5a24-b168-320a-afbf-e8e1898eaee8 | -17.09875 | -56.74734 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 595621ab-ec58-3ca6-bfbb-c0b30703dc09 | -17.09764 | -56.7341 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 82f9a342-b46e-3190-8414-c98cc7e486dc | -17.09671 | -56.73854 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a4b3087f-c913-355c-a690-55be283c21a1 | -17.09579 | -56.73266 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 78642844-f264-3a0a-bf74-5c509138d1af | -17.09483 | -56.73707 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f17b24cd-782b-3420-8ddf-e324adf6a162 | -17.09386 | -56.7415 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 17222c34-5390-35fe-8586-0d7f6dd2d139 | -17.09289 | -56.74593 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d7d59a74-282f-332b-83b2-c5536f9dbee2 | -17.09192 | -56.75039 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4babd1e8-83de-3691-8da6-ad1ae7711804 | -17.09179 | -56.73269 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d45340dc-c95c-3c34-a753-8cf96b020013 | -17.09095 | -56.75482 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b79e2e95-87b7-3e72-880d-064dcedc56f0 | -17.09086 | -56.73711 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| dd473866-96a8-3d70-a53d-6a9c6de09799 | -17.08992 | -56.74157 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 34838262-81be-36fb-bc9c-066d98d76df0 | -17.08898 | -56.74603 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8c35034c-7926-35f6-b2e6-32321b8b481d | -17.08897 | -56.73567 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ff52dbad-d42a-3f2c-952f-f6da4ca9db8f | -17.08804 | -56.75047 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 364a2c13-7fe2-3eb2-9875-06d9e436c741 | -17.08801 | -56.7401 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5889a10a-16a4-3d0b-a31a-c9b5069aadc0 | -17.0871 | -56.75493 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 67ae440f-275c-3a3e-bc83-28ccfb6aeff7 | -17.08703 | -56.74454 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 65d2d0e9-b582-3361-bf8c-48ea9d2f2111 | -17.08615 | -56.75941 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 46c97ad4-0a54-3d6a-89c4-aae4e8373f5b | -17.08607 | -56.74897 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f2845bfc-3b16-3506-a339-c50ad52672d6 | -17.08509 | -56.75341 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 83866eb1-66e9-3cb4-83ed-265c620333f9 | -17.08501 | -56.7357 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 313e78bd-3198-3eee-9755-859959a38163 | -17.08412 | -56.75786 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2cab02df-10a2-38fd-a6a3-a169dbb04c60 | -17.08407 | -56.74014 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5bbcc670-9755-3790-b3bf-ec654ae46d49 | -17.08315 | -56.76231 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 23e728f4-0825-347d-b5f5-457c4585cdf6 | -17.08312 | -56.74459 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 70578d1c-7e26-3595-b21e-dca1f951bafd | -17.08312 | -56.73428 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 36efd60c-db05-3c17-b241-2fdf0b733d05 | -17.08218 | -56.74905 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0b9b1dfa-e2ac-3ad7-930f-79e13c453004 | -17.08215 | -56.73869 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ea6cb470-3b80-3dc0-b98d-1ead0a60acac | -17.08124 | -56.7535 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 38fb1766-a6bb-3dc4-a959-fcdb296a2c95 | -17.08118 | -56.74312 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 64191f88-6bd0-3255-ab0c-afe5cba53f28 | -17.0803 | -56.75797 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6ecfa083-7bc9-3707-a078-1b443329faae | -17.08021 | -56.74756 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4a504247-e42f-3b3c-9dd3-836a887df14a | -17.07924 | -56.75201 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7d227b63-eb40-3346-a7c0-1b7f99c7ac74 | -17.07915 | -56.73429 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1e39021c-b4aa-3b1c-bc6e-ee492e844b55 | -17.07826 | -56.75645 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 18eb1dad-a4ef-3e2e-a791-4dab6675c172 | -17.07821 | -56.73871 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 08904029-ec9b-354b-9ac8-0a28f9a04c21 | -17.07729 | -56.76089 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ef13b3d0-7ce9-3715-8753-36cb09d549be | -17.07727 | -56.74316 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 946a59c5-ec1d-3b19-a3f2-189d8ce2396f | -17.07727 | -56.73288 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| afd3ec41-2f07-31fa-9a12-37ac8a4d5aea | -17.07633 | -56.74762 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 477adaba-f6c2-3f6e-9491-5a165554b164 | -17.0763 | -56.73729 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 916f51c1-e9dc-390d-a4ec-993ea3c85b79 | -17.07538 | -56.75209 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 78122751-4ba7-3d84-b9f8-a545422f68f9 | -17.07533 | -56.74172 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 746a6732-abe8-3e70-b964-9aab0fd8bac8 | -17.07443 | -56.75655 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 56628ab9-ff38-3caa-b0e8-f8c77c7c77c6 | -17.07435 | -56.74617 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8f904f4e-1a96-3368-a00e-5d02f75b2983 | -17.07349 | -56.761 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 52f1c902-852c-3acc-982d-591d67e55bdf | -17.07338 | -56.75061 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c02b24ac-e157-30fe-ace5-c1a1cfca4116 | -17.07331 | -56.73286 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2311b2cc-d156-3d37-be3e-cc0bce0ca4dc | -17.0724 | -56.75506 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a523009a-f3fa-36d1-92c3-f7c6fe16c3ba | -17.07236 | -56.73731 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 26dea6ba-9894-34fa-8cdb-d012008513a4 | -17.07143 | -56.75949 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 82ac72bd-f0c1-3e65-b014-b7e5f098daf3 | -17.07141 | -56.74176 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0dbfbcb1-9347-3a8c-bb73-3cfeb67f0faa | -17.07047 | -56.74621 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 86b9cb76-30e4-323b-882f-dfbe15f5e8f8 | -17.07044 | -56.7359 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 55b5bc62-58d6-32c8-9ac4-692d95408318 | -17.06952 | -56.75066 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a519af4c-797a-328b-a804-3a9231026599 | -17.06947 | -56.74034 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 75343061-7139-33c0-ae67-23a4ffea6a1c | -17.06849 | -56.74478 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 188b4de3-1d2f-3bb7-92b5-f03b9d798336 | -17.06763 | -56.75959 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 37a5f843-abe5-39c4-b847-d29194f67ec0 | -17.06668 | -56.76406 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6b46e393-5efa-3d2a-bb85-4c99b15459f3 | -17.06651 | -56.73587 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 573a70b5-5d97-3055-8c52-1ff8f7a924cd | -17.06556 | -56.75811 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ffaae81f-f3be-3747-abc5-8ea0201b080c | -17.06459 | -56.73449 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fd247231-4e91-34ea-bb18-66b43b897b6f | -17.06458 | -56.76257 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bff050c4-9c32-3544-8ede-80f10236e145 | -17.06359 | -56.76704 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3521a90c-531a-3ff9-bd96-d97c3d47fc2a | -17.06261 | -56.77152 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 57ab480e-d536-3d9d-9f40-b9fa69265a8f | -17.06081 | -56.76266 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e5994aed-1e6d-35cd-8977-fa5e995d5776 | -17.06066 | -56.73446 | 2024-10-01 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0c61d854-b7ce-3851-8d26-f07a425e898a | -20.34778 | -40.36207 | 2024-10-01 04:17:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6fb8b99e-a72d-323b-b2f4-d22159eadc71 | -19.47555 | -40.60015 | 2024-10-01 04:17:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 32608a98-ca01-368a-bc82-ac48bfbac1e3 | -19.43656 | -40.57979 | 2024-10-01 04:17:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9454d987-4425-355b-bd58-49dab6523c88 | -20.50044 | -41.06333 | 2024-10-01 04:17:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7b1afe80-6df6-30e3-b0c8-56a96db39205 | -22.30501 | -41.88227 | 2024-10-01 04:17:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8df63d5f-027b-3b64-b8c2-c09203a6b8d8 | -21.93214 | -41.55304 | 2024-10-01 04:17:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1bb1f39a-d739-3eef-a0be-cca5e0f55c8d | -21.93144 | -41.55856 | 2024-10-01 04:17:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dfdaa1fa-c738-383b-a14e-5d0a765d25d2 | -21.26517 | -41.7835 | 2024-10-01 04:17:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6480d7cf-ca8f-3d83-aab3-381af2f34a20 | -21.26129 | -41.78292 | 2024-10-01 04:17:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dbc7ab84-014a-3801-b50c-e9b168d239c9 | -19.04682 | -42.94528 | 2024-10-01 04:17:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 06ad9c92-feae-3f7a-a81f-74c390480c9f | -19.04622 | -42.94956 | 2024-10-01 04:17:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 226a4299-ee7f-3457-80dc-ec24c0046709 | -19.04978 | -42.95014 | 2024-10-01 04:17:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bddc38f6-c211-381f-8f0e-49cdf62902a5 | -19.49644 | -42.33722 | 2024-10-01 04:17:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e5ec094b-2ac1-3756-8f97-49eca3cbba29 | -19.49586 | -42.34143 | 2024-10-01 04:17:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d8fac247-84f5-3fef-ae25-8e114eff5987 | -19.49528 | -42.34566 | 2024-10-01 04:17:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1f1d8919-427f-34aa-b98a-5d7b9f40d56b | -19.49217 | -42.34091 | 2024-10-01 04:17:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 811b5ed3-64aa-30ac-9f22-ab46beee7bc2 | -20.4621 | -42.95133 | 2024-10-01 04:17:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| da1c3e11-2bdb-38ce-8937-b19eb540d131 | -19.89554 | -43.16484 | 2024-10-01 04:17:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 2a366978-b75d-37ed-ad35-65201499fb8f | -19.89198 | -43.16435 | 2024-10-01 04:17:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ffd22c17-48ac-3f7a-be1f-d457972ccc78 | -19.88842 | -43.16383 | 2024-10-01 04:17:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b83f7fec-fd9e-3351-b439-2607850c7bb7 | -19.88486 | -43.16329 | 2024-10-01 04:17:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8b948d4c-80d2-3dd7-84de-f4765314156b | -19.87296 | -43.17045 | 2024-10-01 04:17:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d41f042-3f91-37bb-abae-20d15d646d3b | -19.78784 | -43.16246 | 2024-10-01 04:17:00 | NOAA-20 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 24f09ddd-d9ce-30d4-84d1-b3defc80b58f | -19.54139 | -43.11897 | 2024-10-01 04:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README90.md)

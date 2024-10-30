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
| 38cf62c7-2b63-35c6-86b2-6a3a006fb1ad | -3.8539 | -51.3793 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 007be490-d195-3a61-883a-501661abc88b | -3.85239 | -51.1339 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b51474c-11f7-37de-8c1f-75d1d39ceae9 | -3.84941 | -51.12499 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89484a76-1115-3821-a367-a93b9c155a74 | -3.84881 | -51.12901 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 770e2fff-035f-32d6-9612-aa3068242624 | -3.82527 | -51.05448 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aabd9e9d-07c3-3740-adb5-703d84efc92b | -3.80462 | -51.16067 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 215f4b1c-f46a-3616-8f60-1e44386b4417 | -3.80402 | -51.16458 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecbf74b9-5814-3f77-953e-abc378a54718 | -3.80344 | -51.16835 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 143b8255-0fa3-3353-b82b-0f3ffdeec162 | -3.79346 | -51.96325 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f16a013-e2cd-30b1-aadc-41fd05888c81 | -3.78948 | -51.96265 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cfca9e2-fa21-35af-86e2-9ad283164662 | -3.7588 | -51.06511 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 573df322-f5fa-36a4-a8b4-b8245e167278 | -3.7206 | -51.34883 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8bdca43-3eaf-3dcc-b6a6-86c3bad23ee9 | -3.71646 | -51.34822 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28b97fb5-06b1-38e9-9684-4fcff2ae50f3 | -3.71588 | -51.35209 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dd2aa5b-0395-3a54-838d-2100a9252c83 | -3.696 | -51.83932 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e40f5dd-f978-3367-a602-e8457770d2f3 | -3.69546 | -51.84284 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 649c454d-d97b-3504-b541-562d1924de64 | -3.69091 | -51.84573 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b08ee02-86c0-3d06-b842-faa34b86afd5 | -3.68983 | -51.85278 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6850339c-49e8-39a2-8e90-7b999e4d13c0 | -3.6893 | -51.85624 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aa805eb-1bb7-3957-bdb2-e09fb0147038 | -3.67066 | -51.38385 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05edc809-b3ae-3c50-910f-4032f9f9e531 | -3.6242 | -51.54921 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8445d038-4256-308e-b6e8-afe297c1c368 | -3.59973 | -52.01728 | 2024-10-30 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f3b1116-de6d-3cb2-bf12-5e9aa297b33e | -3.80915 | -50.75701 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43089627-f20f-34e1-8f09-a9187e6374ff | -4.66629 | -50.97906 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25e26c7d-a773-3636-82d0-cea87188923c | -4.66568 | -50.98311 | 2024-10-30 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1401a1a2-d397-3828-ba65-842915e64f3f | -4.0507 | -51.07837 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40f3b194-3fa6-30fb-9101-a810331dc56e | -4.04653 | -51.07836 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f23d47c6-a521-313f-84d3-ed14cc5e4f2b | -4.04644 | -51.07784 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58fad9d4-5376-3167-94b4-8f024a8614fc | -6.26124 | -51.70112 | 2024-10-30 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 347a492d-2db8-3352-9954-bc0aa025e530 | -7.00409 | -52.05363 | 2024-10-30 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 447876a6-2553-3b10-b55f-433e12e7f6df | -0.70299 | -51.98885 | 2024-10-30 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a67fcbf7-d2f7-3060-b448-e48b65f96e75 | -0.70226 | -51.99352 | 2024-10-30 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62e2da9a-bada-3a52-aac5-e6741d998114 | -0.69533 | -51.68094 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d3140c0-0fad-3399-b406-cd6ccc0c1325 | -0.39692 | -52.06236 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e4e5659-3869-3fe0-978b-c1a148149630 | -0.39314 | -52.06182 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c2715b48-bff6-32d8-9173-a247bdca20d0 | -0.1706 | -51.6725 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce2f953-01d6-358b-917f-c36f3a97d473 | -0.16986 | -51.6773 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f8f130e-8ed6-33cb-8d2e-4b98fd0ca9e9 | -0.16838 | -51.67486 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f2eaee7-efbf-30d0-9cbf-1eb18ae60561 | -0.1668 | -51.56119 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39b5b2e9-2be9-3b4f-8204-fd468ebfb9d2 | -0.16674 | -51.67191 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf39d8bc-ac9b-325a-8ed1-82126c96824b | -0.16601 | -51.67671 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c04ef77-ed33-39ab-b866-9a0174f90b76 | -0.16453 | -51.67427 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61ed8aa0-7578-3050-a39f-6b4aaec0c9f4 | -0.16376 | -51.67906 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6496806f-de57-382e-986f-966c3a36b024 | -0.16216 | -51.67612 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fdbb540-146a-3b96-ac3d-e898b41cdc4b | -0.16215 | -51.56544 | 2024-10-30 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 681f543d-ed4b-309a-ac84-02e0d637caf9 | -2.15065 | -52.36794 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0e830bd-4d36-318d-b78b-e256511c9136 | -1.76489 | -52.30879 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad93f4b3-90fa-36cc-be3e-70f86f4f6294 | -1.76417 | -52.3134 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a857c9b-21dc-3fb8-94f2-86eecb012881 | -1.76111 | -52.30822 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84142825-56b7-3d4b-8fbe-4ca0c04e744c | -1.75353 | -52.30705 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01d86dcc-2826-3d3f-bbb7-d095bedb565c | -1.74974 | -52.30647 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74e42a94-4e52-389f-91dc-2afc655423cd | -1.74403 | -52.34326 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82eece3d-b8ab-33f9-a4d2-e4f1e1990201 | -1.74332 | -52.34785 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40d5faab-339b-38d0-b48e-ed835d09b3c0 | -1.74261 | -52.35242 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b95a9a70-6b59-38e5-9307-23106f118f2c | -1.73954 | -52.34727 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0876288-9641-33f9-b041-3ed6299ba623 | -1.73341 | -52.33694 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e32c80fd-5daf-32be-ab59-03003ebffd48 | -1.69483 | -52.51213 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c044e53-2b5d-326b-a6bc-65a046fbb831 | -1.63541 | -52.2436 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b72a579-684d-3230-bb33-21c1b5a23fc4 | -1.55893 | -52.03752 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02e7e213-d934-3433-817d-05374a782ea6 | -1.55162 | -52.08485 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c6c8bbc-dd90-38a5-8e15-ef4d42e2bb87 | -1.54779 | -52.08427 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70f64d0e-33cf-3a57-8576-2c2a4ab55e5b | -1.54054 | -52.1313 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b29155c7-5a05-3637-a8d8-7e929da05e37 | -1.53982 | -52.13599 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a266e491-d91f-344c-a301-473e9f30d154 | -1.53961 | -52.11193 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efdf76cc-4789-3a22-94c0-452c7a3412ad | -1.53889 | -52.11663 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b50c7d6-4feb-3ce7-830a-30920b5ba2eb | -1.53579 | -52.11134 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 435ce66d-ec8d-3209-8283-12d75df141af | -1.53422 | -52.01914 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3de9af7d-64b6-39f1-9f0c-3a6d818ee16c | -1.53197 | -52.11076 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a096481-b5ce-3bd4-bd11-8b639d08fa40 | -1.52887 | -52.10548 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ebed403f-6d16-3c5c-a5fd-0d63a7a8b1a5 | -1.52649 | -52.09548 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1faafc99-2a57-32ad-b01a-861c8a2abe63 | -1.52577 | -52.10019 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d42b91cc-cff4-3493-acb8-4672c37c3915 | -1.46769 | -52.3284 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e7be112-8598-3ae7-af64-0b36dd6fa0a2 | -1.46561 | -52.34208 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efc204b1-a5ee-3998-97f5-9bad28b09063 | -1.4621 | -52.31145 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ede9fd50-7346-387f-aade-e7a231254087 | -1.45833 | -52.31087 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ce81045-f8db-3094-aee2-c22ceb48e33b | -1.40172 | -52.22708 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0441ced3-b507-3294-847b-7acce9660aa4 | -1.23137 | -51.76896 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8daa4b9d-7e57-33a9-8786-44ae20b00ce3 | -1.23085 | -51.76677 | 2024-10-30 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22bf8c07-6548-3360-98f8-bcc1a1970d8e | -0.77659 | -52.33463 | 2024-10-30 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dabefd59-a0b7-3e81-83f2-e1519907796e | -0.77589 | -52.3391 | 2024-10-30 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 613f2415-1996-34e5-8af6-01ea9393b1a7 | -2.00793 | -53.29612 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e107a108-e1bc-319c-a88f-8a6694d92a93 | -1.89505 | -53.00811 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28e8668f-b995-336c-8692-669237929fb9 | -1.68495 | -52.72346 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59188a1a-ad88-39b9-8e69-1e6680d3997b | -1.68427 | -52.72783 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29714675-07b2-3af3-bddc-9f7a96bfd308 | -1.68126 | -52.7229 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a077de3-2612-3f20-bfdf-5e994950ccff | -1.64934 | -52.65968 | 2024-10-30 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd91ee8e-5def-3aa9-95b2-b61fb1adb791 | -1.59722 | -53.19237 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb73b9bb-5160-3c39-b1f9-1cec7144f188 | -1.58119 | -53.1048 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9bd3c30c-644d-3523-b957-b565ba7cc94d | -1.57757 | -53.10426 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ebafada3-8a58-35c9-82aa-dba9f50d3b0b | -1.57693 | -53.10842 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e17a818e-d27e-397c-99b3-b6b8d335c5d2 | -1.57332 | -53.10787 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d779df7-5838-3820-a11c-77f6ab5f1c18 | -1.44696 | -52.85806 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b788069a-7829-37ef-8fef-178a8d472be4 | -1.07993 | -53.16913 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87a4c1ee-6dd2-39be-be26-112ef3cfb3fa | -0.82808 | -53.06189 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfbf804c-ca24-32ce-8257-86f037859a2c | -3.22506 | -52.18596 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 42cd3b67-971d-3c6e-b72a-5e29cb99e0c3 | -3.39881 | -53.68644 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d8fe04d-477b-354f-9963-23d142d23bcf | -3.31297 | -53.37276 | 2024-10-30 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bfee74f-b1f2-309d-b403-ba1e3fb356ac | -3.68049 | -52.28108 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f181e677-8d56-36f2-9398-dda454dcd13d | -3.67808 | -52.27064 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a87157d-555d-378b-ba77-e3e3f687124e | -3.6279 | -52.30642 | 2024-10-30 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README90.md)

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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b25b91f7-f008-3b71-bffb-68b9b010c5fd | -2.74073 | -51.65396 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca1e241a-26d2-3cfc-b6ec-babc9a4ff489 | -4.15776 | -54.8076 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11290cbd-f37b-3937-9129-88d772d3ed6a | -2.60388 | -54.21846 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46849f34-1f5a-3a0c-a376-f00431631504 | -3.11103 | -53.9845 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6fd537fd-efa8-3622-adf5-d8269f96ffa4 | -2.98508 | -53.88741 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf819ff8-079c-37e8-b091-1ea39fc0bcdf | -2.59699 | -54.21259 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f44cb0f-30fe-3e28-be8f-33b6d1325d48 | -2.88283 | -54.11326 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92257bb9-652d-331a-a6f1-121f41238f35 | -3.23374 | -53.62585 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4110162d-cc9a-3187-9e86-bbb91d6e6482 | -3.50367 | -50.49989 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fde90b25-116e-3fda-b6c5-ec9bee7d3f93 | -2.26159 | -53.46876 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d8df80e9-2e70-3bfe-82b2-dd5b045b9eb7 | -6.37158 | -45.69505 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1ff33ebc-00a7-31a8-99d3-9f155a71e56d | -2.85887 | -54.02438 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82ea2568-e4a4-3704-b045-d33cefc2ce8a | -2.87765 | -53.98936 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0adfd46d-2d43-360a-9f79-5f71520f7bef | -3.03533 | -54.03025 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12cdeb6c-32d2-3e44-a610-5d5fb7bc1bc6 | -2.59876 | -53.97031 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ddc72156-31f4-3c93-ae8b-8fc9387ca0da | -3.68465 | -50.87693 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e584691a-ba28-3eba-a7ad-59d1e5819330 | -2.728 | -48.8933 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7ea64d33-69bb-39d1-b97a-4938094b9412 | -1.99183 | -53.29435 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 222f8911-21a7-3891-bfd9-24ccd5b52329 | -3.04304 | -48.51135 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce0ebd71-247a-3974-96a7-a132f9cf63fb | -3.10401 | -53.81583 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 05f9564e-6353-3fa6-8598-52d79e6d1e45 | -3.53133 | -50.75782 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35fe5a03-0885-3458-afc4-127fc5a47eaa | -3.3801 | -50.11574 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebe6d385-db33-3a2c-be95-1d0fb7cc054a | -3.80594 | -52.35918 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b0baf24-295d-3bbf-b647-701e50e4b79e | -6.38541 | -45.68701 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb196214-a311-3ef0-8ff1-9b24d0990a0d | -2.98363 | -53.89724 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6f51f94-3c78-3076-8084-22a00bdc871d | -3.5337 | -50.1908 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc7c425e-e279-3571-8ccd-7c6eac5c35e0 | -2.60295 | -51.79166 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6fc8be0-2a9b-349f-8a08-a74b4ec36ce4 | -2.54425 | -53.9913 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10f037cf-8e2e-3bf0-9937-828caa53d95d | -3.34277 | -50.50932 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f403519-9287-3ae0-826a-c0762820d4db | -3.25012 | -50.61143 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb6b854f-9528-3dfb-9d8e-27dc50576223 | -2.75154 | -60.2334 | 2024-11-28 05:18:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd5ff15d-ea85-3446-bb7b-f3cfbeec1297 | -3.59667 | -50.38568 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37d695e7-192b-34c9-8fb1-df7970f0f10c | -2.25826 | -53.75041 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3328bc92-ee23-3f60-8b51-05f2453f81b1 | -3.38097 | -50.10981 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6922211f-7ef1-3f62-a771-8b2024b18a8b | -3.2006 | -54.63017 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab5907aa-22e0-3767-a4be-6ff5d9959259 | -3.80654 | -52.35508 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9e9002ec-b688-3098-b8b5-b03a9091342b | -2.69899 | -51.99127 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67145b12-ab14-314f-94c1-ff12de6b14e7 | -3.11383 | -53.2649 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd99c465-f6ce-3d18-9bb7-11d22d8254b3 | -2.74563 | -48.66037 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 809508aa-9184-3df0-9f03-1a039e60f297 | -3.32931 | -50.21656 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9f5c629-7788-3c35-9810-f107f2c6982f | -3.09401 | -53.25807 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d15cc96-db61-3297-af4b-6db977d4d9e8 | -3.09974 | -53.81796 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3559baeb-c31e-3c7f-8646-7cf0443b2298 | -3.60997 | -51.1579 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e072aed-789d-3873-99cf-16e709912434 | -4.35634 | -50.87001 | 2024-11-28 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b90d4f2-40a0-34a5-b289-a9de668938af | -3.10967 | -53.75343 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3009e967-befd-3b65-9f8d-6a61a200390c | -3.3213 | -50.91921 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 574c080e-282f-3f53-9e2c-1a627eaa5708 | -3.76946 | -51.64931 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fab32500-95ae-3f6d-aac1-48dda3365a1d | -8.12837 | -47.98801 | 2024-11-28 05:18:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cc5fac6-d849-340c-99be-78d352051dc0 | -4.00792 | -54.33941 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f90aeb5-f733-3864-8d23-d7fafee8d806 | -3.35756 | -50.51175 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11ef2cf7-54e9-38f6-bb0d-a15540a59fee | -2.73337 | -54.13435 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 968df026-c091-344f-a242-953cd082254e | -3.04934 | -54.04232 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 865b6b9e-4a85-39e6-8c9f-89ceaa0fd504 | -4.74058 | -46.50435 | 2024-11-28 05:18:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8583168-50f3-37af-bbf1-95f167dd0039 | -2.73346 | -48.89416 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f3d0cbd3-481a-33c4-b2ce-ba4d1ce7e928 | -2.93828 | -51.59037 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d9c3262-ece8-3838-a7dd-83e6e077661b | -3.4132 | -50.24169 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1037eb15-16c7-3221-9bbd-5228e271e14b | -2.82978 | -54.0593 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4bda4e80-8770-3041-b4fd-4ad4050e333e | -2.79732 | -53.96032 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 164d8905-4111-3d8b-8186-e1c99fa6367c | -2.18608 | -53.77907 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d60b4b3-a32d-3fd3-861a-7d1e40f106ff | -2.59103 | -53.96914 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4fc9278d-a106-36e1-9c52-41d8143bcf02 | -2.6517 | -51.77195 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c7cf1e4-fe32-3609-99a5-ab1e5484f93f | -3.69615 | -59.8482 | 2024-11-28 05:18:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 85e12105-6af2-3074-b9de-d53c564cda94 | -3.2443 | -50.77285 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6852aebd-fdd6-3e3f-a1af-88d70e04af66 | -4.21092 | -50.8905 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b13ad36-d3bc-36f6-a2ef-da5b784c6e66 | -3.23875 | -53.93463 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1091d0ce-1283-360d-aaa5-81aaa3f959ec | -2.60788 | -54.24292 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 56a00749-e423-3a14-abef-8db34b9150b2 | -2.77293 | -54.07021 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b72c5194-7a88-30bf-8ac8-9ce74c36f629 | -3.07883 | -50.25026 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8d4f29c-dfdb-3846-86ec-29df181415a7 | -3.5766 | -54.52198 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db2d8d0e-1eb1-32ab-bdfc-d16904bcec99 | -3.15865 | -50.58622 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ceef72ea-0649-34c1-a78e-c7acd4f90321 | -2.77555 | -54.02637 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b4a9012-0df0-30c7-a4e4-4c5eb5024d8a | -2.80557 | -51.59355 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c9137da4-c1b3-382e-bfa4-7cd9b1c09bad | -3.27743 | -50.6122 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faffcf4b-b29c-388c-a26b-fc2fe750ca91 | -3.32995 | -51.63687 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bc81ad6-d979-358c-b70e-249bc83fb6ad | -3.51363 | -54.52902 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99c201a2-2641-3d54-b7e2-8725531d7a38 | -3.53282 | -50.19666 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08907e1a-3f53-3155-a077-70eadd432da8 | -3.30518 | -50.27914 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7c2e5110-ac75-3054-bc1e-82c082f7020d | -2.54033 | -53.64143 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 734f363e-272e-3ef4-ab34-0ad85eba2816 | -3.1342 | -50.25631 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50aa3ca9-e3f4-3866-8692-f4a3a6a52835 | -3.15617 | -50.58566 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5e472329-dd78-37cb-8bea-6d728038f106 | -2.8296 | -54.03468 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c7141aa-ff39-309b-8099-e314f7fc677c | -2.23542 | -53.69139 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a87de46e-f3f4-38e8-b11f-076b113672ca | -3.39111 | -50.11148 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 19ea39fa-accc-3a98-8e5c-9399c9652298 | -3.68485 | -49.57088 | 2024-11-28 05:18:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3af4746-0e7e-37bf-9cfa-827761489da2 | -3.16668 | -48.43427 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbb47db0-61c1-3c0a-a8b5-0de1c771d1f9 | -3.70772 | -51.81097 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc04d487-3eaa-3cf2-ba94-8c60f70602f4 | -3.04234 | -54.0363 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17e61111-a8f0-3637-a668-5fc715eda47f | -3.06295 | -51.29399 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e345345c-524e-3cec-b254-2dcd599e8c46 | -3.11673 | -53.75672 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ff48cbc-d960-3801-955e-a3ff51072b3d | -2.75173 | -48.65749 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22b546eb-8f9b-37f5-adb1-f6f2d805de29 | -3.32985 | -50.21793 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a4e1edfa-5779-3f9a-9a88-e01a301be00f | -4.05407 | -50.86555 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c709986-12de-3adf-bb27-2eacca6789cf | -3.60287 | -52.53901 | 2024-11-28 05:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0af76a40-bab6-3a89-9cc8-fecbce0ef429 | -2.91165 | -51.58139 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 514d4bff-e2d5-33fb-88da-9daba6fa683b | -4.09381 | -54.76723 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15ca48d6-2b4f-39e3-89ce-ddeb7b46c5fa | -3.25078 | -50.77156 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4c3ab10f-9913-38cf-983b-0edd8defc45a | -3.10897 | -53.10785 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ca21066-5e6d-3347-b0de-2c9cf10409d9 | -2.83034 | -54.02986 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1bd2d22-772d-3ed0-b9ce-88541d4b90c3 | -3.96643 | -48.07613 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f0acab13-1809-3a4e-be22-c048f7964c6d | -5.50853 | -46.25944 | 2024-11-28 05:18:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README89.md)

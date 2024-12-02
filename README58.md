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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74581cc2-375c-35c0-9a83-5c1d5bceb62c | -2.63465 | -54.19721 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88da6355-70ac-36d2-8720-4fc874f6f1a7 | -2.16981 | -50.12399 | 2024-12-02 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 151c0fb3-54fb-3bf3-ac58-0c3c7cd541b6 | -2.83779 | -54.08524 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fe3ce9e-5229-3618-8cea-8377f8f4e906 | -2.45821 | -53.63323 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b13f383-f722-3822-8a40-61694575e20e | -3.25163 | -53.64838 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f03875b-5948-3522-9d7a-87fbf0ae4c50 | -3.74807 | -52.27734 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7701e746-71d5-3639-a26b-b4d7598ec03e | -3.49781 | -50.32313 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a56bd881-3ea8-3134-a38b-1f5eda3c72b0 | -3.5104 | -53.82898 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea539dae-5493-3949-8c02-337f62923533 | -1.98862 | -53.30045 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f49ceed-af19-3bd3-adee-2f2dfb49c95a | -1.53209 | -52.04627 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9c5541e-8257-33e1-afed-bbcbdd029a2c | -3.0969 | -54.13643 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c71e8485-5cef-3da4-87d0-2c34189a3b11 | -4.51997 | -47.87454 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f410261-5578-375d-b569-7a4f39970e9b | -3.36475 | -51.17275 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47a9bbf0-fb1f-3fc1-92a4-c0013f52180e | -2.46667 | -53.71074 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a1f2414-606f-3df8-97d6-f0e122a17f52 | -2.45594 | -53.62531 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 793ccd29-a388-3854-a445-ca7afa7c4b11 | -3.63752 | -54.67476 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aac10c9f-49da-328f-87ca-88108ae97f87 | -3.10337 | -54.0511 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e11651b7-3cd2-3277-b0f2-6d238ec1bd18 | -4.62768 | -48.03088 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69f17a95-6550-3f9c-9cce-0f689088d2ab | -2.60904 | -51.80937 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec244b81-f9b6-35be-bd1c-f2393807117c | -3.85809 | -52.31263 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa64b7b3-a02f-3167-97ac-2bb3f7c361ce | -3.2818 | -53.35117 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e341b321-5cf9-3bee-aae4-0a8ff999b279 | -2.6773 | -46.60857 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c67aa44f-2dd2-3662-a3a6-6e2f43d1eb4a | -3.53302 | -53.50929 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0681717-0069-315f-b847-1c14ded1bf23 | -2.85457 | -54.09183 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ba8e4db-4d2a-3f4c-abad-7b40572a02be | -3.09296 | -54.04951 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 542250e3-c84c-337c-9225-e371591bd823 | -2.41114 | -53.66397 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e182ef6b-9ee3-3724-8c8e-4ea266608afa | -2.31641 | -51.96406 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a6eb6cd-25b4-3c25-a927-9eafeeda853c | -5.00834 | -44.1701 | 2024-12-02 04:48:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59224570-8098-3cbc-98e3-5f5ca1b2e7f8 | -3.0383 | -51.47879 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0375eeb7-f9fd-3825-98c1-a0d69669a287 | -1.08719 | -53.39308 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9b7b73b-da8b-3740-9936-9bb543bee4bf | -3.35844 | -53.74851 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a7aac28-9ac7-388f-90bf-1f3c01207fd8 | 1.0971 | -56.02037 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 2cd3fcfe-5760-3d09-9dc4-1db601caca6f | -4.32476 | -45.92556 | 2024-12-02 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04d3217f-37d1-3d3c-8c85-e301ae1088d9 | -0.60655 | -51.68948 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e88c6c03-1829-34ed-86c8-185a2e5f1701 | -1.99435 | -53.28636 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68b78cee-48e1-3d19-99c1-89a78e3ae46a | -1.69377 | -52.63636 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a600d81a-2108-320f-b05d-0539692be69b | -1.38699 | -55.18483 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1cbc11b5-dbb1-38d6-8cb9-ef435e66f5b4 | -2.53888 | -54.00421 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af305ef0-41f8-39ef-962d-3f904d1a7c53 | -2.52803 | -53.98299 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eaba35b3-0cb6-32fa-b77a-ce8856c6ac9c | -3.5058 | -53.83588 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c07591d-53ab-30ae-9a5a-d7fc8649b7e6 | -2.56262 | -46.57068 | 2024-12-02 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27ec4597-e17a-3251-ac7d-71dc0dd6cc68 | -2.99347 | -51.33032 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b069a461-e6ae-3d84-82c0-450591eaa019 | -1.68931 | -52.62119 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2f13313-1f0a-3293-aae8-95b0c002522d | -4.04223 | -46.82851 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c67b042-8c0c-39b2-bf70-6fc8d3175593 | -2.99293 | -51.33377 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5d9346f1-d442-3379-bc01-c59dbacef17b | -3.61888 | -52.49431 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c30b7fe2-0a9f-3093-b67b-44d070da99f3 | -3.85999 | -50.89571 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1f02972f-a51f-3019-84cc-c231a766294e | -2.40372 | -53.86752 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a9578ef-8bb8-3d7c-9f6d-e555309c30a8 | -4.32024 | -48.09341 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7967014e-f331-305e-b942-21ac696f5e18 | -2.69084 | -48.85754 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 337d9362-d683-3153-acbd-29030576339c | -3.12822 | -45.9875 | 2024-12-02 04:48:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaedcc58-5ba8-39ad-9a14-fdf2a7e39ee5 | -2.90282 | -51.58414 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbb6f1b5-4165-3fe3-9f16-bef16abe7181 | -1.49767 | -51.94176 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0346e0c7-c425-3fac-85e1-dbe872dd8909 | -2.95046 | -49.4499 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f427ad1-2139-33aa-859a-14447b9fa912 | -2.72395 | -54.13869 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 288bb962-e8b8-3871-abf9-f704a6ce2571 | -2.97706 | -53.87306 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce6f6e4b-cab3-35e7-bbfc-4f87a1bbd6cb | -3.75053 | -54.5134 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 661d0146-d5be-3b3c-8a83-36c7a39241a7 | -4.02775 | -49.93314 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 894ce5e1-0d93-3426-b16a-b2b4e9fa4c84 | -3.7996 | -50.00553 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f478021c-7ae7-3908-8d66-f8913c8ad84d | -3.3685 | -51.12716 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d71781d4-bd38-3298-abc5-59bfcdccd895 | -3.70818 | -52.18643 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf42572f-17b2-37cf-8b4a-1dc644c8bf44 | -2.83532 | -54.10059 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 687d7d7b-9514-31f5-84f4-89466dfc8ef6 | -2.80728 | -54.0415 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f7120b9-7e0a-3ebe-8c18-f984281bbf57 | -1.41263 | -51.14323 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23380bdf-f27f-3f81-929d-f5e275082e9d | -3.2582 | -54.11819 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d3ae206-7dea-31a4-8682-45782fd41c30 | -3.08137 | -54.12203 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19a1bf3a-c8d5-3e6e-99f9-9cd5ada7768a | -3.65362 | -50.22077 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ceb22b89-520d-34c9-9134-1c270616d425 | -3.24827 | -53.93413 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcb5df65-7fce-3136-9e7a-1257479fdd4e | -3.77608 | -52.03491 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b6ae615-12ef-3fc4-a443-df322c1c6b18 | -1.62218 | -53.86611 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94ce0b41-8faf-342a-924c-3041ce14dceb | -3.62431 | -52.50226 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dbe6b3c-a3c9-35be-a0c8-60c7ed8cda96 | -4.6338 | -50.8993 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8762a0eb-fe42-3fe2-9025-5a0d60ed5584 | -2.91129 | -54.11654 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb9bc48f-2f37-3d64-81b8-660763653e12 | -3.1188 | -51.31135 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f2a2ee2-6611-3ff3-b1ff-f9516dd7c241 | -2.8347 | -54.10442 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c736b588-7ec3-34ac-99d2-e1106d0340ef | -3.07555 | -53.80825 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caa4f760-f2c5-31d0-b368-a8c6548959bf | -3.95676 | -49.75747 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dba05510-8337-3916-bf14-e94c808f6581 | -2.85956 | -48.56069 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d41be6bc-535c-3612-ae0b-8f9c707bec14 | -3.85028 | -46.53078 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78c37345-01f0-3463-bffe-714cd179b12b | -2.97028 | -54.45338 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b855a18c-1c3b-3fdb-93f4-9d7b6b7b48c1 | -1.27094 | -54.55074 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c9b8f0d-8acf-30aa-bd2f-b7c167821da5 | -1.18553 | -51.76584 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49afd729-1c19-365f-ba95-a0daea99ab28 | -2.23907 | -50.7912 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 247870ce-2bf6-33f2-899d-99ec6b0410a7 | -2.70181 | -47.74232 | 2024-12-02 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 710a7aa2-db9c-32ec-8531-7b5eaea14e0b | -3.75851 | -52.44918 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 816aeeeb-c69c-36f2-bf9a-c949633a718c | -2.10712 | -50.59225 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa0321b3-69de-3f09-bfba-fc79ee72e6f2 | -2.04921 | -54.66906 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa2171bc-fceb-3f73-a642-0916eb5ef66f | -1.64116 | -52.75156 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaa9433f-af92-39e3-9523-bc8b23b3d0ae | -1.54316 | -55.94055 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e910741-f8e6-3c8e-b552-1db289be0210 | -2.57219 | -53.97404 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c7dae3d-a0b7-3608-aa47-94366d962504 | -3.25594 | -54.10987 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86851b23-c31a-3c57-8978-61c4ac41f0ea | 1.12521 | -55.98654 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89024731-c574-3012-af38-a0077ba8b5f8 | -3.64043 | -54.67926 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| feeb091c-4f74-3f7a-9f15-66e6084bf830 | -4.11203 | -50.49774 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b96bbec1-4f80-3a2e-8077-df667259cd9a | -2.55379 | -53.4062 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4837b5dd-bda7-3dee-8126-139457d09b3c | -3.22255 | -53.83003 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba4c0da3-cadd-3170-89d8-86560f31a00c | -3.09621 | -54.2986 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 173000e0-9b31-371c-8359-a9db1ad8e474 | -2.76445 | -48.56911 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19b27145-5373-39c9-90b5-b69d132970b9 | -2.96935 | -53.89894 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edf7b735-50eb-3598-b9e3-2caaa4b59bce | -3.11305 | -53.99035 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README59.md)

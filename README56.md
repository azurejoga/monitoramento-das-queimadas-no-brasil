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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b0e236f-9549-3704-aed9-8c876db0339e | -3.3801 | -50.10467 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72f4796d-b987-35d9-96b9-f76877a75e4e | -3.5918 | -50.35639 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9380ee51-565b-3881-ad01-0296269a9923 | -3.38394 | -50.10175 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 162191d6-3dcb-361c-a5ae-f21516d1b25a | -3.50369 | -53.81231 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 27205f57-a5d4-3bf7-b03e-2c1785c97c38 | -4.32934 | -45.89009 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90c22c4c-31f4-3c48-821c-aec871e72ede | -4.29311 | -48.20284 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91d3b896-1537-3399-a5b8-87eb89bb6666 | -4.29135 | -48.21428 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c059cf0f-fd59-3ec1-9587-d2833157bb52 | -3.27148 | -48.76043 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d14109a-d140-38a8-a2c4-80031c8be3c9 | -3.23366 | -50.19445 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03bd2503-9520-32b2-860d-dad96f9fdf04 | -1.69843 | -52.38207 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ffa7556-c24e-391d-8b68-647137197c03 | -5.02643 | -47.01685 | 2024-11-27 04:42:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad9b2bf7-5ebc-39aa-aed3-4fcaf8bde8f8 | -4.05594 | -48.33368 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59ec07d0-047c-3ff7-8a46-89627f850b3c | -2.7254 | -51.74001 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1954f67-2c38-3d8f-9859-86f5fa502c30 | -3.97089 | -48.06523 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ea41c4-533f-36ec-8ba9-f9a8b7c77aae | -4.2078 | -50.89058 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 950f7b4a-495e-3d5b-becd-a48ab4de562e | -3.72721 | -50.18714 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3384bb1-eaea-3908-8e24-c4b76c87ef22 | -4.05178 | -46.83704 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fa4307f-df4a-3fcb-a031-04ece1ccebbf | -2.65597 | -51.74024 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 404c565a-87dc-33c5-9354-2492f2e7746e | -4.27999 | -48.60713 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13be3cfb-c71b-3aaa-8b85-8c46a22e1520 | -1.7792 | -52.74115 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 815e5a4c-cc4c-3c41-a3b5-87b7ad9a3e97 | -2.46708 | -48.79779 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ae6228f-ba71-3567-b4d2-e41d4c02b8d9 | -3.15279 | -48.53476 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 477c8085-d90e-3285-8357-896b5afb9c6f | -3.57594 | -41.96483 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac87755d-c5fc-3c1e-bb79-9af9c31973ba | -0.88165 | -51.71964 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb273c48-4c70-338c-8159-a42bc6cd3621 | -2.79897 | -52.90856 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5cbb79a9-b30a-3d34-94b8-9a9fed70a289 | -2.59499 | -54.05568 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 83938640-1926-3479-9be3-d940764d5df3 | -3.78568 | -50.13994 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e2db635-b8ce-33d2-ae3e-a4e1e397f7b9 | -3.0665 | -49.20082 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ebc7ccb3-4b73-3e6f-921e-2045a0543da8 | -1.95439 | -54.13368 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c313c40-6321-36f5-bfdf-f1d2fa030bab | -3.97378 | -48.06959 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90e1086d-e1e7-36b0-b4d7-8a3733ec30ab | -3.58266 | -53.25936 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ca4d8bfe-a302-336a-96f2-c4ffa0208331 | -3.72667 | -50.19058 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8235943f-197c-3e86-9fd9-b0b3fc139be1 | -2.57269 | -53.97424 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9a141eb-681a-343a-a3b0-27756bd1c800 | -2.44947 | -53.68409 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 722b8ad3-685c-30f0-860f-e326f9635c4a | -5.75697 | -46.25945 | 2024-11-27 04:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 28340afa-eb49-34ea-b02f-e7b5df946288 | -3.4116 | -50.38104 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f940e7a4-8262-37b8-89bd-e3b4ad452907 | -3.81538 | -46.6034 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fad834f-85ca-32f1-8996-57a6917c3dc7 | -2.59541 | -54.00109 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fd3c5fa6-d000-38aa-8be1-ec5b5b055d98 | -1.51021 | -51.15114 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c3a8da0-44ee-365d-af96-2c2d5376af91 | -3.49573 | -50.45057 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 796508dd-adae-3b82-a771-7b46cb47981f | -3.52598 | -52.15512 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca8bb446-9309-3221-a00e-802c4877041e | -2.50694 | -48.36236 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6af3d95b-ba62-32d3-ba3e-32c7fa7efa13 | -2.81126 | -52.37387 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf7a94f9-a859-34d1-9dcb-b96b8946fb35 | -2.09783 | -46.56199 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac09f164-5e0b-3c48-831a-a199ab698272 | -3.50733 | -50.46294 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2d0441f-a9b5-3289-be00-068fafd8f03a | -3.05989 | -51.05823 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 375165b0-7154-39f2-98f0-0ad8841aa925 | -4.49601 | -49.63688 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bddfdd7a-4b74-3c75-8d8e-324ed4431069 | -3.61078 | -49.89054 | 2024-11-27 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4455afda-5556-3f34-9a64-4cb6f0282df0 | -3.30526 | -50.49437 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5da2056-530b-36ab-9b40-fa326adaca44 | -1.78275 | -52.74172 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5618b04e-6a3c-3912-802f-20c8b98f302a | -2.72171 | -46.28433 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e378dc8-2ca6-360c-95e8-4fd512603cc9 | -2.93952 | -48.5987 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb7ca1aa-edab-3bd7-b211-d06d81a5b324 | -2.76083 | -50.90803 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0d65f7f-a932-3d7d-bb32-acca37cb1027 | -3.08854 | -53.24906 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8377f1d8-e959-31c4-a442-fbb6dfeecc32 | -2.40542 | -53.68321 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 306ca00a-8ab8-38b8-a014-d62eef38ab91 | -2.73162 | -51.72246 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee7a1129-4144-396d-b021-364e897a4507 | -3.28681 | -50.61139 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15585183-b859-39ac-8ef4-bf76b014a19f | -2.89129 | -48.27776 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 308ff0fd-02da-39f8-abc1-b142194f1d2b | -2.62956 | -48.42971 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92d462f2-45dc-3640-ae8d-ecba11b48f3a | -4.07349 | -50.03691 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95143ecc-a0c1-3868-bffe-03deb02f80f8 | -3.25156 | -50.62001 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 054ef31f-17e5-317f-9c0b-af555bf58a2b | -1.18419 | -51.97589 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12c35d13-2b22-31eb-886b-a856364b1d07 | -3.97144 | -48.08491 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44e6b4d5-2013-35a3-99b9-11a89ad6c736 | -3.0993 | -53.25074 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3ed35a65-2fcc-358b-8a06-834dfad08787 | -5.90805 | -43.40678 | 2024-11-27 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 288a72d1-62bb-3d4d-bd72-61f48126275a | -4.04907 | -48.30951 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd39efb8-4f75-3fd7-9ac2-97dc36c95f73 | -1.86455 | -47.85038 | 2024-11-27 04:42:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3f059ca-2373-3627-87ac-18e98b71fb82 | -2.80602 | -54.14125 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83d9ddd1-acd8-3adf-9619-18c23814978b | -1.95666 | -50.57908 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05badb5c-10d4-3c4c-a0b7-3a6d4b50f241 | -1.54923 | -48.43504 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d5d7a45-4f6b-3f3f-991a-d4f969e59380 | -4.35061 | -48.12943 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a39b7a3-19b1-327b-b66d-b425c278cfb4 | -1.87913 | -52.65789 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af0d18df-4764-35fd-8c24-d781fdbac83d | -0.95195 | -51.65044 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31906bd0-d266-3a02-8bb4-670fa3d31cdb | -4.24526 | -48.67339 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aae70fac-6f09-3283-93f0-9d6cd1347ba3 | -2.71436 | -48.67167 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d9e9c3f-00eb-3e26-be17-a65042332625 | -3.97433 | -48.08927 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0fdfabf-8549-3c0e-be30-6a5a54f67cf7 | -4.3023 | -48.23534 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e710a261-4e9e-3d98-a3e8-27be3e6606ee | -3.91206 | -42.4193 | 2024-11-27 04:42:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| a9348b74-7c18-35d0-96aa-f5240332d096 | -2.05524 | -51.1853 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4bc5103-6e4c-31a0-8060-9d76e45cf3c3 | -2.57787 | -53.96581 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cd8d116-7c98-3ca6-8f3c-fb203723b6cb | -1.61315 | -52.46189 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee145383-6f08-3cbc-8101-5d4676a62274 | -2.49913 | -52.15324 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76e6278c-2487-30df-b6a4-c169077788b9 | -1.36706 | -52.55361 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d43f1e0b-415b-36ef-8820-89947f3b27a6 | -1.12383 | -53.72939 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2379895c-103f-3382-a5a0-9f59485552fa | -3.04392 | -48.51462 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| ac1e133c-4762-349e-a22d-b08ba5f2d8d0 | -2.5887 | -47.4514 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36ce03e8-c8de-38b4-b2d0-4ee0cc55a063 | -3.77148 | -52.39843 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0f04a00-380d-3af1-bbf3-7b6dd3e1aa61 | -3.54458 | -50.39832 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5ee209b-fd30-3309-88aa-51d0fa6761d6 | -3.94339 | -46.69817 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b91d2126-7ebc-3c6d-b9f3-f8cfa0fadfee | -2.49569 | -52.15268 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ecf19bc-d339-3b04-be03-6819ae154dfa | -2.60157 | -53.96792 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d25eb964-f187-3187-accd-f95f4da47d23 | 0.69796 | -51.44186 | 2024-11-27 04:42:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb249b9e-921c-337c-9385-9344c389c77a | -3.05684 | -53.28602 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5942550d-fdaf-3236-961d-3c0df6acd698 | -3.2884 | -50.27687 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99e1147a-295b-3ce6-960b-8a713854013c | -2.01393 | -51.18608 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4d9b014-ba7e-3db7-b952-881f685d49d3 | -3.2298 | -50.77918 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac9f3a23-3ad6-336f-86bb-b5bfa4d7185c | -3.96914 | -48.07671 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 82f9605b-3760-3a55-b9b0-83c7e54ffa90 | -1.71765 | -53.06131 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bea03d8-bc84-3f2f-a323-9471a5ce31fe | -3.5377 | -44.93018 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45ba021b-4839-3daf-991a-6fdc5d26867c | 1.94803 | -60.85889 | 2024-11-27 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README57.md)

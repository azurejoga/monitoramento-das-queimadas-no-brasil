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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7223712a-ea02-3a60-880f-ee2bb4ce90ea | -4.20813 | -47.87104 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5e13861-faa7-3f7f-9ea4-75b9511089c6 | -2.42189 | -50.48633 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c65494aa-017d-36df-a65e-793c3990c2c1 | -3.23278 | -50.28544 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a9ba7697-f855-33ad-b8de-11022cbebaf2 | -3.169 | -49.10388 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9827f742-f805-395e-a84f-efaea41baee4 | -3.37951 | -43.79823 | 2024-11-10 04:38:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d133ea9d-d328-35bb-b6e9-e647dcad3fa2 | -4.93161 | -48.24549 | 2024-11-10 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d834887a-1da4-3a99-9ebd-decb21170abb | -2.4902 | -53.99442 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ebaf575-ea8f-35bf-b647-9c7358e5d7bb | -4.72656 | -50.38058 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdb9a80-4128-3777-b8f0-25e8a42f059e | -2.57688 | -48.1809 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ff21350-e35b-3ba3-9521-478aef176060 | -3.60776 | -49.62325 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbbe43f7-0af0-364e-a69f-74a69e0122ae | -8.39127 | -44.15078 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65968cdb-904d-3a9e-8779-687514b693e7 | -2.11779 | -52.12097 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8264818-7201-3260-b5d2-ca864c473e4f | -3.08393 | -50.56493 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bbd83ab-d3de-3ea5-9040-44ce80decdc0 | -2.23878 | -50.03513 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9de160da-ed98-3d29-b074-48ef415d59d4 | -4.1088 | -48.2743 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39819e80-e5d6-3314-9608-132564498a2b | -2.83702 | -48.46127 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75b0b197-f4d5-301c-a08e-4782c2136c55 | -7.42994 | -39.76488 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 53e86415-a108-39a8-a8f1-36c643d16d4e | -4.43938 | -44.62806 | 2024-11-10 04:38:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3008c992-5823-3cd2-8fdb-a3c780c91313 | -2.80688 | -52.5442 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f3251ec1-6367-355e-884b-22710efe9589 | -3.55493 | -53.31184 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a3309c7-d5b4-326c-930a-700da3b88627 | -2.91338 | -49.24214 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0860622b-02f4-3b1a-bf33-e74724a77d50 | -4.13027 | -46.84348 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3b24303-d318-38e3-b7b6-9fe4ca3f31ce | -6.09924 | -47.05313 | 2024-11-10 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdd533d4-d7de-3beb-bc8e-da3375708f55 | -3.17529 | -51.30659 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d213e2c4-c247-3a01-b1f4-7f1f9bdfeccf | -2.57157 | -50.68312 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32acfa85-3dca-32b6-8ace-a451c9e7cbb2 | -3.70687 | -51.41051 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7587d875-fe2c-31b2-a874-4ac05ef1c127 | -2.74416 | -49.17958 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c0944dd-dcf3-3411-bb87-8594f8a5930d | -8.41261 | -44.12223 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9c3c33d-6ae4-3031-92ec-92673f51d70c | -2.62139 | -51.29368 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0288d8a-2038-35ea-8e54-6abf935913e8 | -4.20908 | -50.62409 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80b20fba-479a-38b4-b014-35f73bdaedc3 | -2.65058 | -49.90224 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0648f894-bc10-351d-8fff-fd7488284bc0 | -4.87777 | -48.58986 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8986387-b250-349e-8b4b-0bc8fff30751 | -2.92888 | -48.30957 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd8e56ff-2334-349d-93f9-9efa1388ba29 | -3.98314 | -48.16578 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 516d9372-ad17-35e5-a3d4-fe6c0ef2fcd4 | -3.24011 | -50.30532 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 96df5081-c64e-381c-b865-c2c796f25afe | -7.43076 | -39.77143 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c6cd3919-eb5f-3b82-8378-c8d39604863c | -4.88237 | -48.64735 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6cdeb4b7-d415-3b46-8eb0-3eea4a0342a6 | -3.13523 | -49.12346 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28e06ba1-1c31-3507-87a7-6eabcd25a575 | -2.6445 | -48.63244 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59e8f64d-7c82-3b39-ac91-861ee2c1d4e0 | -8.39239 | -44.14301 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4990c625-99a0-343b-81eb-f14ac52cff94 | -3.2419 | -50.27196 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a62d5f41-14e9-3244-8dc3-771d285558c8 | -2.92763 | -51.47981 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1059a37d-6473-3fe4-8810-fe395274ece5 | -2.24073 | -53.79702 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 587941d9-1bf5-3088-8a29-f74ca74c8fad | -4.72388 | -48.77139 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7bd01c6-1a88-3ee1-8123-3c3e90fc9ab4 | -3.25036 | -46.45919 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4424e089-129a-3c91-905b-215438e93150 | -2.85246 | -48.44955 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b651365e-9fc2-34e0-b259-8d3bf79afd6a | -3.10385 | -49.42885 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d286c648-2285-35bb-92c5-cc27cf3372d2 | -2.84115 | -49.231 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2fd86a9-7369-3ea9-b6b5-f0c3294513c7 | -3.13188 | -45.96387 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a8d900b-0f85-3040-a77c-e326214df2c0 | -3.14219 | -50.44102 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 8c4d6268-18d6-3106-adcb-7de45d07c663 | -2.3841 | -49.80218 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2c9f363-752f-39bd-bc46-0fece54f6ad3 | -6.24897 | -43.56635 | 2024-11-10 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f489034a-e411-3ac2-9959-db1c41e91862 | -5.73587 | -47.21911 | 2024-11-10 04:38:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d92e82d0-d2e8-3181-887e-c96158f44145 | -3.09445 | -50.23439 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb44a06c-ed36-3efc-8928-ec15380675d6 | -2.22337 | -50.8939 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3029a777-f8f8-314c-9e6d-5545e75078f2 | -3.78872 | -47.46585 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cdd95b7-2b22-30a3-9101-b75ccd250e6c | -3.20886 | -50.30413 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4f3582c-f3f8-3c10-b9a8-be796aab38a8 | -2.43843 | -50.51585 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 790901e5-95db-38ea-a75d-bd5145ac332f | -4.25895 | -45.85411 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa17f4e7-dd56-3d8b-a4a0-509f1dab5e2a | -3.60944 | -48.9498 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 102cb374-7f75-3683-9ca7-0a0cb7be9ed2 | -3.2423 | -48.7472 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87c4fc88-1e5c-3e2d-a839-c71e106aac62 | -5.6013 | -47.93672 | 2024-11-10 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf4eb73d-bc50-35ca-957e-00422e60cc03 | -5.14588 | -47.7172 | 2024-11-10 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d665a343-284a-3052-bf24-f7ebd242f90d | -4.28087 | -48.18713 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b67451c-430d-36e4-988d-3161bb9ac8e4 | -2.45833 | -50.30143 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30aa3cb0-eb2e-327a-bb2a-5ec2b2f023d7 | -3.04739 | -49.53533 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb286b1b-61a7-3df0-9c1c-f1ed6839eec2 | -2.11732 | -50.74744 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdf5d20c-338e-3839-8dea-e76aaf169838 | -2.27601 | -50.67698 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 129028b5-be07-3e4b-ac74-bb628c94a81a | -2.73138 | -49.17402 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f323913b-d1a5-34a8-a869-41b34d21aef7 | -8.3952 | -44.12355 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 057a41f6-7f1d-32e8-b6f1-0d22517331c3 | -2.88735 | -49.40614 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d3b8e02-3e87-3b09-a5b4-f3640aef3f4e | -3.18078 | -50.59098 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ec72dc0-810b-3e24-ba06-bb4427ba7582 | -3.57508 | -45.8232 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 86d0a4ea-95f1-38aa-9509-02ff3a396334 | -3.23953 | -50.30897 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 3413fb08-2236-3fae-a5f3-4cdba3f7f2a3 | -2.38286 | -53.74324 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c94ad657-2e37-3819-b513-0a8862424816 | -4.09453 | -48.32182 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52ba21f6-a5c0-384e-b53e-2f17a248801a | -4.1147 | -46.87552 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba1bcd1c-8598-37af-890e-8ea7c9746d36 | -2.51062 | -49.88441 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 913febae-750b-3c6c-b572-0f9f98718f48 | -4.93627 | -48.52082 | 2024-11-10 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb36a3ab-fcae-3b8f-819d-303b1dd7293d | -3.19344 | -46.49284 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3557fb7-9569-3fdb-bdbb-4740e001092c | -3.00391 | -51.44891 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abda8ac3-e90e-3acd-b3d7-e426564f5b84 | -3.96968 | -48.12095 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15ea3437-42fb-31b1-bb95-15a283651f54 | -3.54686 | -49.98338 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce86ab7c-10b8-3692-8c4e-e4a8d889a6cf | -3.11178 | -50.1477 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e8403fe-0844-3584-b2c2-77306475ca1b | -5.51223 | -49.19987 | 2024-11-10 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3485f622-c1a3-3fc7-952a-997d3cfffd11 | -3.54528 | -43.55683 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9bcbe520-97c8-30b2-9d0a-5d526dbc5fff | -3.08382 | -49.55498 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bc72376-1c10-3b94-bb7c-90fc54100dc2 | -3.54472 | -43.56047 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c478a0c1-c8a0-3062-a6c9-ab2cf61e911e | -4.36572 | -48.14672 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92944ac0-2281-343d-8c5a-5c586c05508e | -2.92699 | -51.48387 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 909ec8d8-93ea-3ffa-b8f2-af0d93782075 | -2.53407 | -49.56333 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f68b5c7b-7175-3306-98a6-2e013d24bc87 | -3.91599 | -47.94839 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d79ba62-cea4-353b-993d-d5d43bca7e05 | -5.44883 | -43.27134 | 2024-11-10 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55b8b4b8-6d6d-3564-a305-759e506901fe | -3.32917 | -46.40913 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fe77f76-3c33-3537-8793-144018777145 | -2.93165 | -48.31353 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f51b847-c361-3e87-88a1-11353dff69a8 | -8.39968 | -44.15206 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bd7e582-256f-3b1d-b5ad-3b22e3e087d3 | -2.93739 | -51.05721 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5eac763-58f9-3165-afae-4092e3ff94cd | -3.5346 | -49.25735 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76706f2f-4e67-3569-aa3f-f10b62c54c94 | -2.20453 | -51.94281 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4b97b84-29a3-34b3-9104-da96f82b8710 | -2.31643 | -54.3955 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README99.md)

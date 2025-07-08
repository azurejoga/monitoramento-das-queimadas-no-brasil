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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c68f29c-e8a4-34dd-9436-678cb1ae6e96 | -6.88773 | -45.23825 | 2025-07-08 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2def9d3d-c469-3795-9daa-79b53292fa99 | -10.34579 | -49.92281 | 2025-07-08 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ba98f4d-91d7-39dd-8af0-ec7e3ab4f461 | -10.13151 | -57.7761 | 2025-07-08 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4013f1ee-7bbd-3dfc-aa6a-715a0d225887 | -10.97209 | -45.11698 | 2025-07-08 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dcd56a54-e831-3ece-8096-632a7db82992 | -10.82306 | -54.02024 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35abffa8-d91f-3ae8-a652-ae7b62147fcd | -13.0157 | -46.2962 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67c24863-b223-3dbf-a59e-bafff29f0b04 | -9.00813 | -48.72237 | 2025-07-08 05:04:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 564c402e-5c00-3009-90dd-1d2357c169e7 | -9.34882 | -58.84101 | 2025-07-08 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64cb2d29-582e-348a-b663-6ad9c5a9f083 | -10.62614 | -49.45438 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e02fdf40-5035-34e9-b91a-7c6a63ed9b2d | -6.67431 | -43.77058 | 2025-07-08 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8a2cdaf-69fc-3bee-b7ab-cf2df9920517 | -7.18661 | -43.12726 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 14896484-5291-30b1-a26e-8ca866bac0af | -11.43625 | -45.11782 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d8c14263-1a10-3fc6-b7c7-849d4caefe1f | -11.02088 | -56.25291 | 2025-07-08 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4de52bf-de0d-36f1-a398-b0900379155e | -7.19798 | -43.13459 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 76c99f05-e340-3669-a239-d7b3d1041866 | -9.86802 | -48.46929 | 2025-07-08 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2e284bd-2f9e-3914-ba60-5b9b331a9d55 | -10.41877 | -49.76587 | 2025-07-08 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7456486a-4531-37e8-a2e2-22a9adbdede8 | -11.42989 | -45.11705 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 077c8449-a79a-3964-918b-db3baf385407 | -12.98737 | -44.87882 | 2025-07-08 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 288aa738-7fd5-3dd5-9dd5-764484288288 | -9.17902 | -50.17593 | 2025-07-08 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f7f9c562-7f18-3607-92c7-0e658a132d80 | -13.03689 | -46.2903 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13c276c7-8ff8-3cfb-b633-ff8005a023bf | -8.06595 | -43.11623 | 2025-07-08 05:04:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 8e13a044-3936-3e32-b9de-34f25aac7940 | -7.192 | -43.1276 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 951ab64e-16fa-3423-af9d-bfb8f5e39240 | -6.88436 | -45.2396 | 2025-07-08 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34cf7526-c0cf-32ae-9a9e-0dd283f8a85e | -7.24913 | -43.07283 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b0ee3745-6400-33f7-9dd9-62176419212a | -9.17841 | -50.18028 | 2025-07-08 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a1687c38-069e-3d38-9142-1bea38d8ceff | -6.34101 | -43.74171 | 2025-07-08 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5df0ae9e-0010-3a1e-b2d9-3d76022e9a5f | -8.7029 | -50.01719 | 2025-07-08 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51318ac9-69c3-302d-9e41-0bb0aec1e6fc | -8.71414 | -50.00092 | 2025-07-08 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b71f2e4b-0c2f-3d89-8100-cf16ac0b04f2 | -7.63681 | -45.36211 | 2025-07-08 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 841be893-49e0-30a9-b012-0db1151f76a6 | -9.42784 | -63.45718 | 2025-07-08 05:04:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f72fc47-ddfa-3c1b-88a1-6791ae7a870c | -10.82266 | -49.5525 | 2025-07-08 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9338b16-7ffc-394d-9733-65f7429962bc | -12.33111 | -49.32318 | 2025-07-08 05:04:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 00dbb297-234f-3c55-ba20-adc9a75ccfba | -7.23246 | -49.59779 | 2025-07-08 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 123ec0ee-5ef7-3b66-b7d3-f678171e2617 | -6.67475 | -43.76946 | 2025-07-08 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd01b5f9-f2ea-31d8-93d3-edb9b8b31d66 | -10.4135 | -49.77006 | 2025-07-08 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 422581f1-b13a-3ea8-a11e-3874f6ad91cd | -8.70358 | -50.01525 | 2025-07-08 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c505ea12-ebf2-3573-8b22-f7f5d95ce67b | -13.02222 | -46.29277 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4097a6c2-79df-329b-90f6-3efd9effff84 | -13.02402 | -46.29607 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e89deb4c-2d36-3452-a1a1-1ecef602e347 | -9.7037 | -56.18494 | 2025-07-08 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 782d6014-05c3-38ad-bf07-06886a4c1cdc | -10.63661 | -49.45776 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8c342003-ce55-3f46-acc3-cfeec7fdb73e | -7.18521 | -43.1266 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5d63efd4-3cd9-38f8-8682-aefb776f0cd5 | -9.87342 | -48.46711 | 2025-07-08 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c398471-1623-3c14-8a1b-bfb83e6639b2 | -10.82367 | -54.01616 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fef0729-a314-36dd-ba40-ea28ec91302f | -13.03463 | -46.29119 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb669031-3792-3e94-a9e1-47e136d34615 | -10.82429 | -54.01208 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad1cec1d-6c12-3db2-af64-74f50c0914ea | -9.00513 | -48.72056 | 2025-07-08 05:04:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 681ef006-f106-33f7-a930-21e34eabad34 | -11.19705 | -48.99981 | 2025-07-08 05:04:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f57b8a77-3942-3dbe-98a9-419e789eb3ca | -9.02278 | -61.22998 | 2025-07-08 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99971eac-d74c-387c-908e-eeff4e787a15 | -10.34663 | -49.92033 | 2025-07-08 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea520874-b5a0-3ae5-bea1-da744898be5e | -10.64001 | -49.46852 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6bbb2e5d-9506-348c-9d8d-181da60df3b1 | -6.82327 | -43.5944 | 2025-07-08 05:04:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f040652a-cfcf-3019-b782-93f78d63cf53 | -9.21792 | -48.59158 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aea79352-0a25-3e5a-919b-ff7071224ca3 | -12.98521 | -44.88965 | 2025-07-08 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6124e151-b1f3-345a-9bf9-87693ecee62c | -10.39465 | -52.17202 | 2025-07-08 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62f63b4e-8b29-3bb2-bb08-848eed51e50a | -9.21966 | -48.59308 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 245f47ce-73a0-3c91-a094-8505db4b3356 | -7.91085 | -55.40066 | 2025-07-08 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15afaf95-6c2a-3a8b-adc0-7d5ebda79c71 | -7.19879 | -43.12861 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c5da33a3-ffca-345b-b6fb-6b635fce3a7f | -9.22949 | -48.59442 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0a2a3a37-5e6e-36ff-8138-ca2bdeb348b9 | -11.32819 | -55.21534 | 2025-07-08 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fb71abe-a6df-3209-bfc6-3a04bfb1badd | -9.92556 | -59.90573 | 2025-07-08 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6dc6e04-c2e4-34e3-8225-72c9d6115a23 | -7.25512 | -43.08014 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c337a31d-6d61-367c-9485-b12d9ff9e7ed | -12.98583 | -44.88392 | 2025-07-08 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eead0dbc-504e-31d4-8c23-a4e8cd8ec0c8 | -9.28615 | -57.82922 | 2025-07-08 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 519dccbe-7f8d-3f9c-9dd4-053f867b48da | -9.58028 | -57.39642 | 2025-07-08 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1bb33c7-355e-3706-ab5e-42b657c0b9d7 | -7.19963 | -43.12243 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5a2a2951-4fa3-339c-a066-a6e9f7601dc5 | -8.71432 | -50.00339 | 2025-07-08 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 063dd6c7-03f8-307c-b1c6-9a0d4fad7d0f | -10.47957 | -55.58474 | 2025-07-08 05:04:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94738fae-b7a0-3935-8f83-b390ad5516a2 | -9.74729 | -53.29486 | 2025-07-08 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be77abaf-2450-3dbe-bdc7-6e655cfdaf41 | -10.95104 | -49.25161 | 2025-07-08 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcc27e22-e811-353f-869e-c03c510e5500 | -11.43173 | -45.10147 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 239e1afb-a185-3449-9652-a65f5966ad06 | -10.97472 | -45.11904 | 2025-07-08 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| df82a778-999c-3454-a296-841f55bb934a | -6.16878 | -48.05927 | 2025-07-08 05:04:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b25053f-241a-36ab-b3b6-abebaf0bb4d1 | -9.02197 | -61.23086 | 2025-07-08 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8079f86-0069-3df7-ba3b-8b51baa4938a | -7.57641 | -45.22178 | 2025-07-08 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62dcebaf-7f7f-3574-89fe-edae321ed715 | -7.72395 | -55.14011 | 2025-07-08 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eee575e7-23a6-3f31-9e4d-8154328adcc3 | -10.63256 | -49.45195 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0e94f5f8-667a-30a9-a685-2d771beab223 | -8.70295 | -50.01962 | 2025-07-08 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36166705-8cad-3fd0-8fc2-065603bc213e | -9.80916 | -48.25494 | 2025-07-08 05:04:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60ed5a0d-8e25-353b-9219-975eab965312 | -11.32763 | -55.21909 | 2025-07-08 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d68d9d37-03da-3d64-b71b-52c3769e3b5f | -10.96343 | -48.20451 | 2025-07-08 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 023f22c4-0e3e-34b0-bb23-d3b504606f8d | -9.60948 | -63.46439 | 2025-07-08 05:04:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39f38752-9b8c-3dfe-8e33-961402869ed9 | -7.19263 | -43.13432 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 17a5c49a-e8e2-3ddc-ab75-5f30b9223344 | -11.46935 | -47.92083 | 2025-07-08 05:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ef31ece-bb65-3a8f-aa55-ad2c465e8e63 | -10.65013 | -49.46475 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c95c1701-b6ee-35f9-b248-d2292efa2f94 | -10.82073 | -54.01154 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e2bd1b3-452c-3e29-9b30-5439dedeab22 | -7.09935 | -44.1578 | 2025-07-08 05:04:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac787df6-902b-3728-bb4a-579440d5ceec | -9.22208 | -48.5977 | 2025-07-08 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cd74ffdc-4043-3dcb-b5fa-70d8c636aaed | -10.82662 | -54.0208 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a628cd2-0d0a-36a5-ac72-d9f165be2cad | -11.45021 | -45.10896 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6f6cd83-b1dd-3261-acc2-f7b2328e4c0c | -5.12496 | -56.11451 | 2025-07-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f02eba90-4a25-328f-9b41-fc74ab59e4e4 | -10.22746 | -56.7659 | 2025-07-08 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50e47012-a94a-3325-a6b3-dff7a280a4ba | -10.82723 | -54.01672 | 2025-07-08 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc3adbde-e683-3467-8e4d-52b1ad414770 | -9.35038 | -58.85311 | 2025-07-08 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 346bdf8f-64d3-3c71-b383-0fac62881749 | -11.4305 | -45.11187 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8f7ed060-07d0-3d2c-b909-0856086a510d | -10.57804 | -49.12492 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 1fba1cc5-eb8b-3ae8-a297-9861f07ffd9c | -10.6454 | -49.46413 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 61f1c48f-3ebc-3ec5-8a9c-374285fa3175 | -12.96735 | -47.82315 | 2025-07-08 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c2347b6-82b1-37d9-a6e2-7e64fed6cfe6 | -12.98645 | -44.87808 | 2025-07-08 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44d9e36d-2266-3038-9d9e-30a8cd518b95 | -10.21274 | -52.15682 | 2025-07-08 05:04:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ad1cd0b-93d8-357d-ab2e-ed0e5fa7f164 | -12.96581 | -47.82694 | 2025-07-08 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)

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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 311ed403-5444-3cc7-bbb9-00f19a365d44 | -13.65758 | -43.92599 | 2026-09-14 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47730d57-25b3-3b19-9800-2dc575a45c0c | -13.58753 | -47.89652 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| aef06eb0-9540-3265-89c9-500bc40d014e | -16.23289 | -52.6505 | 2026-09-14 03:57:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5beba6c6-e94f-36ae-8356-120ed0dbe166 | -17.26616 | -41.50589 | 2026-09-14 03:57:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a1e2e8d6-4fa2-331c-90fc-9c338f2e28c3 | -14.83363 | -48.15517 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec0e1dc2-2251-3ded-8948-82ade0bb67d4 | -13.43884 | -48.47656 | 2026-09-14 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c2da25ab-5d99-362d-88ff-fc9acc60fded | -13.58626 | -47.90049 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1692d10c-9fc2-365e-a7f0-ccd175c81cd5 | -18.18667 | -43.8905 | 2026-09-14 03:57:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6569666-2bf1-35f5-a7f1-e743ac153c0d | -17.98699 | -44.33628 | 2026-09-14 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb8c95c0-1f91-3235-a22f-e284e1f6df5d | -13.58341 | -47.88925 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9d0ef676-8890-3c3e-80af-9de2e318a2fd | -13.46696 | -48.46331 | 2026-09-14 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 83246c1d-0860-3970-9ff8-40bcef3d2457 | -4.1333 | -60.6882 | 2026-09-14 04:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 395ca70a-1974-35ce-8878-b7d7765b9d79 | -6.1111 | -57.6645 | 2026-09-14 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| bd9360c8-595f-3845-90e9-a95e618831e3 | -6.1109 | -57.684 | 2026-09-14 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3d634cc4-9d22-31ef-93e7-d1e1ed5f43bb | -4.115 | -60.6886 | 2026-09-14 04:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4c59ccdc-ebf2-3865-b9b1-9fe506139ed9 | -2.6967 | -57.5501 | 2026-09-14 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| c650542c-8f97-3963-8ea4-bcbca1d69082 | -2.88 | -50.45 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8b9d57-d946-32db-8a0c-23213fd862e5 | -2.91 | -50.51 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34f158e4-621b-348e-b548-f4aa7aebb5f8 | -2.88 | -50.4 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7882626d-19b4-3150-9d91-b467d8dba656 | -10.66 | -54.12 | 2026-09-14 04:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 856bb71a-ea22-3e94-9eb8-fbf9a65acdde | -2.88 | -50.56 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bad10d0-66e3-391f-a6f0-37fcad34c82c | -2.91 | -50.56 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96585e3a-5e2f-3ba3-94d8-75f40f7849df | -2.94 | -50.46 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82f91588-5c48-3a17-b70a-fe75b1de6941 | -10.69 | -54.13 | 2026-09-14 04:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d13f43ad-863d-3d08-a2a4-1d6c40d4f7cc | -2.94 | -50.51 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93e613b9-7860-36d1-9130-a6c6c0765419 | -2.88 | -50.51 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 469cea68-2787-3f71-bf08-ca5de6172b9f | -2.91 | -50.35 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0ec11b4-c598-36dc-82e2-9d8862d0e759 | -2.91 | -50.45 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19851995-4791-32e9-bff8-81860e49b96e | -2.94 | -50.57 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66651943-3c38-375d-bd12-adc0e29c74ae | -2.91 | -50.4 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e07386b-3f3e-3942-9873-f44d9cf2c73a | -2.94 | -50.4 | 2026-09-14 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56fbe569-f8e9-39ca-9792-d7a4d2a1d7f7 | -1.19924 | -54.12429 | 2026-09-14 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdd69f21-f062-3bf1-a5d4-372a53b41f0c | -1.2226 | -54.12962 | 2026-09-14 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89db476b-beab-351c-8124-1d19be8c330d | -1.22319 | -54.12597 | 2026-09-14 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0412d1b1-dc5a-3f63-ad40-5db1ec80d071 | -2.06 | -45.9816 | 2026-09-14 04:29:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 265aebb6-ec71-3587-856a-011e475e3d64 | -1.19335 | -54.12327 | 2026-09-14 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2294c272-715c-3f6f-967e-582559b08831 | -1.8573 | -47.9808 | 2026-09-14 04:29:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 535be65a-f0fb-31be-9595-dedc2625b50d | -2.06061 | -45.97779 | 2026-09-14 04:29:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf3513ff-ebc2-3804-b657-bd116c3105ae | -2.06348 | -45.98216 | 2026-09-14 04:29:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3862f863-4362-336d-a689-c95dc82d2c0b | -1.86117 | -47.98141 | 2026-09-14 04:29:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5ed2ad03-4d3a-3630-93c0-a23dd990193e | -1.22195 | -54.13366 | 2026-09-14 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9adcb10d-519d-3d88-b885-88447eab7cbd | -9.54526 | -45.43491 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20e042fa-4470-3ba1-8b66-b34bff04a567 | -2.91251 | -50.46832 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0cb3f4a-0307-3a8a-b596-be3f79167237 | -9.31605 | -44.35923 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c79f6096-2ac1-33f8-9021-26402a23ceb2 | -3.22097 | -50.58606 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39212b5c-65a6-3a99-aaf7-4dd4c15977aa | -9.46794 | -47.32577 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e199fa8b-30ab-3171-9280-563b8c048ba6 | -2.93262 | -50.43078 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3cd4c442-e3ba-37bb-85b6-2e67f9a99a9a | -2.93343 | -50.41411 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 574765ff-fbf3-3430-8136-4a4838090e32 | -6.5964 | -58.85759 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4e80e4a-8adf-373e-8209-4cf63b05e064 | -2.92286 | -50.39423 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ee1fa938-d7ba-38db-9817-105f2103e59c | -7.09089 | -41.79317 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a737c1f-6b9a-3300-9ac5-3d7308b099e2 | -4.39453 | -55.20696 | 2026-09-14 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 890160cb-b315-3a18-b25a-7804aa561d50 | -2.92543 | -50.43543 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 54b13cd3-bea6-3a54-bcc8-f4825ce13577 | -6.2899 | -55.28208 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87413f18-ae0a-3d4f-9b7c-33a7062b2a8f | -2.90234 | -50.43616 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c92d7a90-b41b-3f24-8b9f-7aabbb8cb8dd | -2.69358 | -57.54049 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbc518d1-f1e1-3f2d-bf81-598d724c317a | -6.29202 | -55.27005 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2115434b-726b-334c-a1fe-a0e30c5f2a0e | -2.69043 | -57.53675 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80554f6b-196b-3ead-9e17-7607c0760072 | -7.16199 | -42.10357 | 2026-09-14 04:32:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 60f19d26-58ca-30ed-8aae-669f34ecb18d | -2.92896 | -50.41334 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 46a4c485-2755-3803-8659-eb86a17f6916 | -4.5508 | -50.45909 | 2026-09-14 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53bb0fa0-bc51-3832-85ca-cfea324ee2ff | -9.43059 | -50.12971 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bbce6b57-467f-36ff-b46c-e54ac4490ddc | -3.74252 | -40.42121 | 2026-09-14 04:32:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 48cd7cbc-0b16-382d-b212-631ad9e58c41 | -3.41083 | -58.21819 | 2026-09-14 04:32:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d880e80-b9ef-3e2c-86f7-dd7606519366 | -7.16137 | -42.10759 | 2026-09-14 04:32:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c74aef92-39c6-355f-b74e-5c472393b5ae | -6.33569 | -43.36218 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bb9e2745-a676-3b35-89a3-4cefbe671938 | -9.36734 | -50.11865 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a24c62a-d02c-3c35-9e5e-d2470dd8f23e | -3.54407 | -53.98263 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c717e83-3f7b-323d-a810-20d2a797427c | -2.92991 | -50.43614 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 84d3bce4-ec00-3759-ac86-6e7fb583de89 | -2.92144 | -50.4426 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 24083a0a-51b7-37b7-93ad-1324febe20f4 | -2.96828 | -50.40953 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4d83250-c3ca-3cd6-a8b0-7a857ecd89f1 | -6.53437 | -44.09048 | 2026-09-14 04:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2c3b1a3-2039-36a8-a9eb-1e0b338a4aac | -2.91698 | -50.40229 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 02952b37-3c59-30ec-bccb-3e4797936ce1 | -2.66683 | -57.54663 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2e5105e9-1f2a-3f57-8978-e520cc0d465f | -6.69369 | -43.14173 | 2026-09-14 04:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07f139cd-263c-3e54-89bf-f897f0c89269 | -6.11286 | -57.67505 | 2026-09-14 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1755fe07-9322-35de-968f-1dd18da7095d | -6.69334 | -43.14616 | 2026-09-14 04:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92f7a534-7ed4-3307-9d6c-dcc6ae34f0c3 | -4.14007 | -54.01851 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c859576f-6473-3f94-88c7-e58a66d44c63 | -2.90144 | -50.41332 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 639dbab7-acb7-3b48-a0da-6b79ff0c4028 | -8.38898 | -42.21808 | 2026-09-14 04:32:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52dd3118-a4b5-3bd4-930c-732bcd2d299a | -7.08302 | -41.79631 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7fc0a9cb-325c-3cce-9254-79f05c9acfff | -4.59186 | -50.98699 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbe20dd9-ac1a-3ceb-b9d6-fd58ac38b113 | -2.95262 | -50.39347 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec135216-3f11-3324-a1ab-6cc872954196 | -6.10902 | -55.66839 | 2026-09-14 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86f55280-40c8-3ed9-82e8-0a72dce37ab4 | -8.8284 | -47.17649 | 2026-09-14 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b74067b7-f053-369e-bc3e-d5fbf6257c10 | -7.87169 | -54.72461 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7815da1-248c-39cd-b8ba-5757302ca893 | -7.08707 | -41.8181 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc369fb0-3d94-3ef3-8a9c-ab033d07f9fe | -2.91576 | -50.43842 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d327c4ff-7ce6-3f2c-a55b-85549a57f533 | -2.90609 | -50.44139 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 41a175b2-7595-35dd-a10c-054f45a155a9 | -5.35661 | -47.37767 | 2026-09-14 04:32:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 534b1af2-3a00-3a76-8a06-7f22e5d192ec | -6.27964 | -55.27167 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd378f81-4c5a-34ad-8d43-f6f2352df1ba | -8.11746 | -54.8015 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1750ca7c-602e-324c-8b62-46d9cf748272 | -7.52411 | -47.33626 | 2026-09-14 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56dcb1c6-0e07-3b21-a595-eae8e5a47ca2 | -5.12249 | -55.95108 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5b78359d-454c-3f0a-96ab-17efef60e513 | -7.11758 | -41.79115 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5b243eb1-185a-3d0f-a905-bdffb0460bb5 | -7.08408 | -43.55078 | 2026-09-14 04:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4335268b-74ea-3362-8323-c2009ffd7900 | -9.45138 | -47.84566 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07345f95-641f-39ea-b56d-a3cc5bfe9f0e | -5.28705 | -45.2692 | 2026-09-14 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad1a310f-bab1-3dc6-9394-325134eea7fc | -9.13693 | -51.57778 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5c0df46-5239-35bc-b9b6-abac1a74f0cd | -5.08105 | -56.25394 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README17.md)

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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23e684c5-920e-3df9-b97b-7f7ce30b51fa | -9.2215 | -48.5826 | 2026-07-12 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1748d0a7-f43a-3f83-a113-f49e3635e240 | -10.13411 | -50.15546 | 2026-07-12 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cebbbe1-3546-328e-b38c-7ed48d7d4a88 | -10.05641 | -48.20766 | 2026-07-12 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 028431e4-f4d0-3b2a-a673-ed008cd3033b | -6.94509 | -43.71452 | 2026-07-12 04:51:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81b9f9bc-19e0-3d20-aee6-e1a37a6d666b | -10.12729 | -50.1544 | 2026-07-12 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1fb300a-3317-3e9f-9082-50e57494a643 | -10.84987 | -45.0352 | 2026-07-12 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38483c4c-6615-3654-b69b-1ea292a6f761 | -6.99826 | -42.90657 | 2026-07-12 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a778e1bd-1b8b-3922-859f-276dbe521d8a | -6.4906 | -42.22311 | 2026-07-12 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b44baf80-afb8-3efa-ac1d-b064bb5aff5e | -4.80589 | -45.77285 | 2026-07-12 04:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 320ade6b-e593-396f-a757-dc7257a94f61 | -8.10199 | -47.09842 | 2026-07-12 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 67f84ec2-b977-35df-a132-33712f7c29a4 | -10.47817 | -42.42059 | 2026-07-12 04:51:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d42c65bc-c0b3-3988-ba4f-000c07dd0dc1 | -7.91436 | -48.24924 | 2026-07-12 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d271920c-f271-38c5-a5d1-5b14c5346ba0 | -8.71997 | -47.83132 | 2026-07-12 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc452ed4-004a-3613-87a4-c0b6eb49febc | -13.7401 | -54.06318 | 2026-07-12 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bddd666b-a0f0-33f3-b1db-d2a07b3e4622 | -13.47818 | -44.04344 | 2026-07-12 04:53:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fee406db-5e31-3266-a685-638809413761 | -16.81212 | -49.20037 | 2026-07-12 04:53:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f60d123-9479-3209-96ca-8d5faee5404a | -15.89117 | -43.48014 | 2026-07-12 04:53:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f416197-9f88-3a83-8b9d-db6a1b58c065 | -11.84803 | -49.18225 | 2026-07-12 04:53:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a316358-d732-3915-834f-f1ae38779ced | -18.22395 | -43.64698 | 2026-07-12 04:53:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2be74932-d8bf-3860-afae-aaed5af2cb7c | -15.89726 | -43.47722 | 2026-07-12 04:53:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cfe58f6a-d222-388e-8b4e-2845f57383bc | -15.89686 | -43.4809 | 2026-07-12 04:53:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d6d26911-7ace-3af4-b2cd-03256618acf6 | -18.27021 | -51.2118 | 2026-07-12 04:53:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bdd45649-3e21-3b01-904c-8575afcde720 | -16.6928 | -51.37704 | 2026-07-12 04:53:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35ad2f71-1d70-3e0f-adf6-1d61c8d1ff36 | -16.69339 | -51.37314 | 2026-07-12 04:53:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c9ac030-7c5d-3509-9a29-bbdf111bc476 | -18.22995 | -43.64377 | 2026-07-12 04:53:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 832af581-9012-3074-987e-bae6887ea6dd | -13.74345 | -54.06375 | 2026-07-12 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f550327c-1c85-358a-a10d-60bac62de0d8 | -13.7468 | -54.06433 | 2026-07-12 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 81d3911f-f3e8-3675-8db1-b230d91dc066 | -15.89668 | -43.48082 | 2026-07-12 04:53:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0394ad4a-3165-36df-99f5-16fcfed4069f | -15.89646 | -43.48457 | 2026-07-12 04:53:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 151f20cb-005d-3ffc-83bf-2846d8c384b1 | -16.05251 | -56.95935 | 2026-07-12 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d763458-f4bc-3cad-8964-a52aebcabbf7 | -15.89134 | -43.48022 | 2026-07-12 04:53:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d0ac6ec-550f-3c3a-a704-91c64fe8cccb | -18.22568 | -43.6476 | 2026-07-12 04:53:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50f3737d-5fdc-392c-bd18-2c39c960cf05 | -13.75014 | -54.0649 | 2026-07-12 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fe721811-3834-3882-9c7f-14cce2a06a09 | -13.75349 | -54.06547 | 2026-07-12 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 95ab0e8d-ded7-3f31-afc4-1e3c8f22d4a9 | -15.89626 | -43.48447 | 2026-07-12 04:53:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 095be266-6a69-358a-a7f0-d3bf35f3a037 | -15.89711 | -43.47715 | 2026-07-12 04:53:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1a85cdf6-03ce-36b5-b5ba-972bf7c578ce | -18.23172 | -43.64435 | 2026-07-12 04:53:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da89c281-0ebc-36d4-91ff-68479c8d4cd2 | -10.1292 | -50.1475 | 2026-07-12 05:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| fabd81a4-e161-335f-bcb7-cc25d5c3e443 | 0.8748 | -59.70442 | 2026-07-12 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ade23a4-ffbf-3da1-a740-59da14e0034d | 4.32536 | -60.79421 | 2026-07-12 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b36a047a-bbef-33f1-8af1-96890f5c5252 | 4.3292 | -60.79715 | 2026-07-12 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07bfd5cf-eb60-3548-843b-413f68bd6342 | -10.1667 | -50.165 | 2026-07-12 06:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| dfa7d594-ec58-3238-9842-1e24b95a0a4e | -10.1664 | -50.1864 | 2026-07-12 06:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6fc46f40-e9a9-3976-89fb-a0f725dac7f5 | -4.33896 | -47.76062 | 2026-07-12 06:14:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 41ab8972-55a5-3c9e-b26f-f2a68e54eee2 | -5.11942 | -43.23666 | 2026-07-12 06:14:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9a5124bf-ced0-3f27-ae69-abb230fc61c3 | -4.66748 | -43.22424 | 2026-07-12 06:14:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e42ba2b7-0d54-3d19-b21f-96d3e00d6d9e | -4.02833 | -44.13247 | 2026-07-12 06:14:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3ad97e96-4f3b-3303-8d07-11f60b06ee31 | -4.34088 | -47.76629 | 2026-07-12 06:14:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0e9a3858-01ae-3ae3-9458-2b2ca54dda52 | -4.02996 | -44.12195 | 2026-07-12 06:14:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d7407339-9bef-32f7-adf2-d40975220f75 | -10.1664 | -50.1864 | 2026-07-12 06:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 1a6493b3-e191-394d-b904-5ecf0dd701d0 | -10.1667 | -50.165 | 2026-07-12 06:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 584834c6-1772-379a-b6af-38ac166161a6 | -10.1667 | -50.165 | 2026-07-12 06:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 2df20bae-76af-31b4-a667-69da68350601 | -10.1664 | -50.1864 | 2026-07-12 06:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 5f069d88-eb64-35f5-b3d4-2acd42b4e977 | -13.374 | -54.3365 | 2026-07-12 07:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| a2486007-7cf1-33a1-af9d-65d830b70239 | -13.3743 | -54.3159 | 2026-07-12 07:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5863bdd5-5d1f-3f55-afa2-b423511eb4b1 | -6.91905 | -51.93488 | 2026-07-12 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e19011e8-bed5-334a-a00d-809937f08f1b | -6.91859 | -51.94095 | 2026-07-12 12:23:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 07ae5ddc-eeb5-3c36-ac5f-d820ac5011aa | -2.8997 | -42.2843 | 2026-07-12 14:40:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |



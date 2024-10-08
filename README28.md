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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d6e215e-af00-32f2-a729-f42c6724397c | -20.3732 | -43.9468 | 2024-10-08 02:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.0 |
| be73608a-6f01-398e-9d03-d8e1b2c6cf0e | -20.3938 | -43.9412 | 2024-10-08 02:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 225.5 |
| 039e2791-0c9f-3cbd-a63a-a5de1f7f0899 | -20.3946 | -43.9163 | 2024-10-08 02:46:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| b1ff179a-1667-340d-b206-d16faa2dedc9 | -20.4144 | -43.9356 | 2024-10-08 02:46:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.7 |
| 3576f1d8-ad18-3822-84b2-e8e47e0ddae3 | -6.74866 | -35.1215 | 2024-10-08 02:51:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5aa814bb-4353-3a68-a2ad-9c87c2222c86 | -7.19542 | -34.98682 | 2024-10-08 02:51:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b33c9fd7-f22d-345c-bfa4-74294e4d460c | -7.19557 | -34.98824 | 2024-10-08 02:51:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d3445b32-61f2-31a2-82ce-b73c72de0bf6 | -7.03598 | -35.51125 | 2024-10-08 02:51:00 | NOAA-21 | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cdf3b02f-7a6a-3b6d-8c3b-edac6c6cb617 | -5.5716 | -44.8927 | 2024-10-08 02:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d26f16ff-1750-3c7d-82c2-594eded9d49c | -5.5718 | -44.87 | 2024-10-08 02:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2d0eb18e-6d0d-3ccc-a27e-e015486ef06e | -9.4087 | -66.5438 | 2024-10-08 02:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 7cb71a41-20ee-3884-8f69-e9878af52377 | -9.445 | -66.7289 | 2024-10-08 02:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 1c33f0b7-e1da-31d0-9079-14decf9754c0 | -10.6256 | -55.9154 | 2024-10-08 02:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| dd30ff33-952f-3db5-9cf1-155bf2c8bb49 | -10.8754 | -63.9169 | 2024-10-08 02:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 2c3f65a5-c808-3985-987c-8e4b829d5819 | -10.8755 | -63.8979 | 2024-10-08 02:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 1090ca4e-57ad-341f-b201-8beaee5e07bf | -11.3081 | -51.0676 | 2024-10-08 02:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 7542c3e3-c225-3219-8ab6-d39ac6436ca7 | -11.3271 | -51.0656 | 2024-10-08 02:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c9ed0b33-0eed-3d15-b35c-45d619cf50db | -11.3461 | -51.0635 | 2024-10-08 02:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| b6b07470-6bd5-3cc7-8ccc-0df2817f8bf5 | -11.5233 | -65.137 | 2024-10-08 02:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 86ecd1a1-0764-3dae-9118-65590c608d8e | -15.0434 | -45.4718 | 2024-10-08 02:56:30 | GOES-16 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 168cffd9-3608-3717-a4cc-981989293127 | -15.6874 | -59.4344 | 2024-10-08 02:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| b5d0aae4-8428-32fc-8db8-cc36c6b7cb66 | -15.7066 | -59.4526 | 2024-10-08 02:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b1e52562-54be-3894-bb4c-63345e080a18 | -15.7068 | -59.4326 | 2024-10-08 02:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| bbeb5c1f-0e6a-37e4-8b60-55dee2fd6715 | -15.6872 | -59.4544 | 2024-10-08 02:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b3b9fbfb-4bd4-3d4b-83c0-aed41df35418 | -16.1683 | -49.4927 | 2024-10-08 02:56:37 | GOES-16 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e312b518-b2f1-3f0b-a6dd-40623a93c229 | -16.5897 | -46.4979 | 2024-10-08 02:56:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a35b22a0-c457-3b9d-9674-24c297e4b31f | -16.5902 | -46.4746 | 2024-10-08 02:56:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| bdc20350-bffd-3c36-ba44-aacfe2289be5 | -16.4365 | -57.2575 | 2024-10-08 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 91fdb2a8-cc1c-3bf5-a461-52e059982baa | -16.5556 | -55.9079 | 2024-10-08 02:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 32.8 |
| 6d735244-8bdc-34fd-90c3-2fc71aa1c537 | -16.8048 | -57.4197 | 2024-10-08 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 894d03fa-d383-3e48-bd3f-b39fbc091f32 | -16.9211 | -57.4881 | 2024-10-08 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 0275498d-ddae-3bff-b111-19738de52cc0 | -16.9407 | -57.4859 | 2024-10-08 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 7789c5ff-2953-3436-850f-16a22feb1bd5 | -17.0982 | -57.4267 | 2024-10-08 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 64a61840-8fee-3aed-9af9-78f8bc415eba | -17.0992 | -57.3651 | 2024-10-08 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 07d0562a-06a3-3f02-a33e-8ba7ddd5585a | -17.1178 | -57.4244 | 2024-10-08 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| d39fb889-c859-3dc0-8afd-77800a907c76 | -18.6192 | -57.2603 | 2024-10-08 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.2 |
| fd86c96d-6b52-39d7-97f8-5e4f4b6b9e5b | -20.3732 | -43.9468 | 2024-10-08 02:56:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.2 |
| 056d38d9-b9b0-3a7d-839a-73ec7767041b | -20.3938 | -43.9412 | 2024-10-08 02:56:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 163.9 |
| 1ed8ea56-3e2b-3ddd-8fa1-921062dded8f | -20.4144 | -43.9356 | 2024-10-08 02:56:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.0 |
| c460f5b8-1645-3e57-b663-c0526cb3881a | -20.4 | -48.87 | 2024-10-08 03:03:28 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d6a58a84-31a2-3844-937e-45abcabd097c | -20.4 | -48.82 | 2024-10-08 03:03:28 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fbcbe661-bddf-3a8c-bce1-7ca5d8fc17d1 | -20.43 | -48.84 | 2024-10-08 03:03:28 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 372034f3-45c6-33be-8a3f-a087009608f6 | -20.34 | -48.84 | 2024-10-08 03:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b3ba103c-af9e-316d-8fa2-66dfb7e2e43b | -20.34 | -48.78 | 2024-10-08 03:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 349731b0-9110-3be7-a76b-c209a9f2665b | -20.37 | -48.91 | 2024-10-08 03:03:28 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0722228f-3360-3c0b-9e96-31778aaee18b | -20.37 | -48.86 | 2024-10-08 03:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bf5dfd62-e211-3d5c-848e-8b44e8421d3a | -20.37 | -48.8 | 2024-10-08 03:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7efda0db-7275-30a9-a088-b4cec6b875a9 | -16.67 | -57.13 | 2024-10-08 03:03:52 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a20752b4-d8eb-3bb5-8b53-39593aae178e | -5.5716 | -44.8927 | 2024-10-08 03:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 7cbc3c07-691f-3370-9ef2-3adf4344f0ea | -5.5718 | -44.87 | 2024-10-08 03:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a3b3f77a-67d4-3c9d-a542-73f438da6f10 | -9.4087 | -66.5438 | 2024-10-08 03:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 68cb0617-f72c-3fb2-aa4d-b88b3793bebb | -9.445 | -66.7289 | 2024-10-08 03:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e8632b4b-4b88-39f3-8a00-1e70f9bf7ae6 | -10.6256 | -55.9154 | 2024-10-08 03:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 1360cd0b-a474-38f0-aef3-0de9d8481593 | -10.8754 | -63.9169 | 2024-10-08 03:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5c2f50db-7b16-3195-ba0f-551cf87e7a1c | -10.8755 | -63.8979 | 2024-10-08 03:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 544204e9-4d56-3964-aec9-48e7af1be808 | -10.8941 | -63.916 | 2024-10-08 03:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 2cf3c63c-2bd9-3c27-9e8d-9300a10066d5 | -11.3081 | -51.0676 | 2024-10-08 03:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 78793d4d-4b01-30f2-b42d-c011495f25df | -11.5233 | -65.137 | 2024-10-08 03:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5a843211-e8d8-3206-80f3-811bfeef4262 | -12.4605 | -62.9977 | 2024-10-08 03:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 780562ca-de60-3fc7-884c-cdf90f9bfcd8 | -15.6874 | -59.4344 | 2024-10-08 03:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 8b860cac-b5c2-3055-8874-aec37805eb3e | -15.7066 | -59.4526 | 2024-10-08 03:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 9f4560f9-e34e-3ef2-b455-4f7b2e55763e | -15.7068 | -59.4326 | 2024-10-08 03:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 1d07243a-69c5-34ec-93d7-923c17fa2b28 | -16.5902 | -46.4746 | 2024-10-08 03:06:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 9baedc22-4839-3f91-b907-e9b1ffe2a7dc | -16.5752 | -55.9055 | 2024-10-08 03:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 40.6 |
| c64df32d-a7bc-3df2-9b8e-845cda18b83e | -16.8048 | -57.4197 | 2024-10-08 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 4a54e878-b756-39c5-b507-084b617d7b7a | -16.9211 | -57.4881 | 2024-10-08 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 7c9c051a-69d8-3c1f-9846-c0a819326407 | -16.9407 | -57.4859 | 2024-10-08 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| 9ee56ec0-f86d-3410-8cf4-d7db9b3247a3 | -17.0982 | -57.4267 | 2024-10-08 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 9cd53158-54ec-3733-897e-b2697f89b3a4 | -17.0992 | -57.3651 | 2024-10-08 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| a72026e1-d0c0-3d27-b5bb-df8cb0f9202e | -17.1175 | -57.4449 | 2024-10-08 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| da21938c-99e7-3b40-9635-694c6f1947bb | -17.1178 | -57.4244 | 2024-10-08 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 88771675-5d58-3104-a407-c16765191bc4 | -18.5993 | -57.2629 | 2024-10-08 03:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.9 |
| 93964b10-d11c-3f36-91e0-240b0e98e64a | -18.6192 | -57.2603 | 2024-10-08 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.2 |
| de546580-a7d7-3d7b-a33d-ca8a8618a177 | -18.6195 | -57.2396 | 2024-10-08 03:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.2 |
| 8807f5f8-3c06-3ad2-a3a7-2611b344c76a | -20.3938 | -43.9412 | 2024-10-08 03:06:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 140.6 |
| cce76d3c-8c6f-35bc-82a5-5a07f7aa6129 | -20.4144 | -43.9356 | 2024-10-08 03:06:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.7 |
| d0e55f9a-be78-353f-8366-b038d5844a57 | -6.2647 | -41.88166 | 2024-10-08 03:15:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ef8f0dba-461d-3dc5-ad59-a2c331bebc56 | -6.25773 | -41.88092 | 2024-10-08 03:15:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 27c9a873-f485-3556-aa2f-cabadb31f7c0 | -8.80737 | -41.04044 | 2024-10-08 03:15:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e27ded5-d2e6-3518-8d3e-08ade3dd2a8c | -8.80112 | -41.0391 | 2024-10-08 03:15:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6443adfe-7de0-3854-ab32-26575cd8c9c0 | -7.78408 | -43.08454 | 2024-10-08 03:15:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2e6edce3-53da-36d6-9606-cd26c7e1e0f4 | -7.78264 | -43.09188 | 2024-10-08 03:15:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bf4a01df-d68e-3aac-a61c-72f2991d42db | -7.78216 | -43.08429 | 2024-10-08 03:15:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ce0408f8-c045-3b10-836b-b555b2a48e3b | -7.78078 | -43.09158 | 2024-10-08 03:15:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bf1357ab-f95f-3f80-92c6-785e3f56f387 | -7.6583 | -42.49109 | 2024-10-08 03:15:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 87409d2e-1484-3313-a0fc-e8e77db3caec | -7.65702 | -42.49765 | 2024-10-08 03:15:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c9d67e05-341e-3b87-833b-407c4bb429dd | -7.65572 | -42.50428 | 2024-10-08 03:15:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a27572b8-b157-3365-88f9-16480a04957c | -7.65311 | -42.51768 | 2024-10-08 03:15:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d75e1979-0800-34bf-8aac-c81845378f7f | -7.65178 | -42.52448 | 2024-10-08 03:15:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1cdca79f-7fa3-3d3b-a89f-29052249f9b9 | -6.83826 | -42.80445 | 2024-10-08 03:15:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0f2b4431-0477-3fdc-b563-1128a8204040 | -6.83629 | -42.80594 | 2024-10-08 03:15:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 83da6886-8b00-35b6-836a-94fd6d2f8c0d | -6.83098 | -42.80363 | 2024-10-08 03:15:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 09687da5-80aa-319b-b3b3-ba35784fa32c | -6.83036 | -42.79795 | 2024-10-08 03:15:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a3e7c761-02cd-380d-9660-318bc554aed5 | -6.82903 | -42.80505 | 2024-10-08 03:15:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac7db6e3-ab2e-3501-94c3-59a5ffa23379 | -9.53306 | -42.99342 | 2024-10-08 03:15:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7d2c0d89-9d51-3640-8cd8-d8f4a6be50c8 | -9.52616 | -42.99176 | 2024-10-08 03:15:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 23fa5f9f-26f1-31de-a4c9-8bbbff546016 | -7.03903 | -35.51246 | 2024-10-08 03:15:00 | NPP-375D | ALAGOA GRANDE | PARAÍBA | Brasil | 2500304 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8a47c05d-edd6-30ab-9a45-027f18baa40a | -6.60407 | -35.24828 | 2024-10-08 03:15:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e2112e9-abbb-36be-868f-d4477308d6ca | -6.60162 | -35.25052 | 2024-10-08 03:15:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| bd31bc72-52cd-33f3-ab60-c8299296e0b0 | -6.59958 | -35.24767 | 2024-10-08 03:15:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 11.6 |


[Clique aqui para ver as próximas entradas](README29.md)

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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f2592f5-d8f0-3678-9827-a41611bf6e03 | -4.02574 | -44.12991 | 2026-07-12 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d4974889-27ca-338c-bfa0-826968cee53b | -3.4981 | -48.03971 | 2026-07-12 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 10323e40-f492-3f4d-868c-c1f3d4f05fd0 | -4.25476 | -38.69656 | 2026-07-12 03:53:00 | NOAA-21 | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a09d88cd-fbbe-374e-8639-62d8b8c8dc2c | -4.02546 | -44.13142 | 2026-07-12 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 364d8862-ddee-382b-bf77-ae128681bf01 | -5.01383 | -38.67334 | 2026-07-12 03:53:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 70902139-dadc-3440-88a9-499aefbfd11c | -5.12439 | -43.2402 | 2026-07-12 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| de07aa98-6e7d-3622-89eb-41b61befb430 | -9.34104 | -40.68151 | 2026-07-12 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37f8d4ac-34ea-31c4-9dd0-cfe9b70ae90f | -10.48093 | -42.42187 | 2026-07-12 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b4aff63c-757a-3f85-a5da-3f8af07519d8 | -10.48024 | -42.42608 | 2026-07-12 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cfbc4010-892c-3511-aa7a-9939a82ef12a | -8.72299 | -47.83121 | 2026-07-12 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e420286-9b23-3ef6-80a0-c798378181e7 | -6.94276 | -43.71729 | 2026-07-12 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f762ae3b-1b12-3669-8dcd-93fc88479b9e | -10.47733 | -42.42127 | 2026-07-12 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7a2d4f23-0d8c-34e4-a5dd-3beb05416f77 | -10.28959 | -44.9468 | 2026-07-12 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5fcb2b8-d76a-3129-8e80-cf7a3a50b180 | -10.47373 | -42.42067 | 2026-07-12 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a916d691-b44f-3af7-abf2-2aeac52bfb01 | -7.58538 | -46.15832 | 2026-07-12 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21d9a9cb-9386-3a8f-8c07-6df459eda0e7 | -10.8493 | -45.03513 | 2026-07-12 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8949896a-d9df-351b-a9bd-749f14dcb5a7 | -6.99857 | -42.90744 | 2026-07-12 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8ac9f676-ec47-3e85-9948-6e2db7736978 | -10.84859 | -45.03908 | 2026-07-12 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df20ac21-79d4-34ea-91f5-71dfe5cc76c2 | -9.59425 | -40.35306 | 2026-07-12 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64723fb2-33ba-3a7a-a237-7ffb777ea995 | -4.61175 | -49.05268 | 2026-07-12 03:55:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eea8d750-a3b7-3c60-964e-76c36c5f7549 | -8.05124 | -46.92739 | 2026-07-12 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9281da76-bce9-3161-a800-5cdd3a59a019 | -5.67509 | -43.57226 | 2026-07-12 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 594790f7-63f1-32f6-9598-20d5e4b9792e | -7.91122 | -48.25043 | 2026-07-12 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f32cd8c0-6423-378c-9ebb-5c7ae9c6a6b1 | -11.9698 | -41.33323 | 2026-07-12 03:55:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 685760aa-b6d6-3d93-bafc-ad4cafecf24f | -10.28539 | -44.94606 | 2026-07-12 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9374f06-71f6-3b0c-a485-19fbaf51ae93 | -5.98073 | -43.61835 | 2026-07-12 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e94f647e-00e5-36aa-bdff-4c5497b3a9b8 | -8.13777 | -47.16795 | 2026-07-12 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c72849df-370f-3789-81cd-6284fc2972f1 | -8.72358 | -47.82798 | 2026-07-12 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3fc1462-58ae-3011-ba4a-eac584d0e7a0 | -4.61255 | -49.04821 | 2026-07-12 03:55:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a10fdc04-208a-3d70-adbc-dde5a8e822c6 | -6.94338 | -43.71365 | 2026-07-12 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11b66d57-e05c-3a52-975a-6da92fe9c469 | -8.10465 | -47.09105 | 2026-07-12 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b70afcab-8ca9-367e-8e62-f010cc3a31b1 | -10.9943 | -37.69174 | 2026-07-12 03:55:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 626477ef-65fe-3cc2-895a-2fe8f76ceeaa | -8.10361 | -47.0968 | 2026-07-12 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f46398a7-bfcc-3049-b211-7583a98c6114 | -7.90991 | -48.25764 | 2026-07-12 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35446eb2-8374-3185-948e-54012fe4bfe0 | -12.74211 | -45.89362 | 2026-07-12 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1b6a63b-d30d-3d0b-acb1-ab69dbe7274d | -8.09857 | -47.09599 | 2026-07-12 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33cbbdb3-09b8-32fa-97e2-de08197de4c8 | -9.42262 | -48.1195 | 2026-07-12 03:55:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2af0374-2769-36aa-bdbb-ab2e0cf8cd5e | -7.2103 | -44.26381 | 2026-07-12 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85f3865c-ceb7-39d3-9917-b8c265794022 | -7.09122 | -41.68484 | 2026-07-12 03:55:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aeeb092a-ff66-34b4-bc10-8ad629c9bbc5 | -8.10305 | -47.09994 | 2026-07-12 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8d7c7dc-d5bf-32eb-a549-a2dd53c92a33 | -8.72941 | -47.82566 | 2026-07-12 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db766924-bab0-33f6-bd8b-6952f8b146dc | -12.74383 | -45.89394 | 2026-07-12 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56b10263-1ec9-3d65-9f17-8270fb8805e7 | -6.22822 | -39.79988 | 2026-07-12 03:55:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8be312ef-05e8-31e1-932a-ce47931b9f3f | -7.20536 | -44.26734 | 2026-07-12 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2f969d6-fb42-38de-80f7-740fed4e4db3 | -6.71085 | -41.12303 | 2026-07-12 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7da8275a-fa51-34b6-8c23-652642b41216 | -9.00607 | -45.71506 | 2026-07-12 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0f86c50-7bcb-3de7-a4da-8f4def40b1fa | -8.05071 | -46.93035 | 2026-07-12 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6894e69e-fdc8-3fe4-9770-589ae8662cc3 | -8.10414 | -47.09386 | 2026-07-12 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48697802-c376-3885-ab6c-96de6a504dee | -9.48397 | -43.03991 | 2026-07-12 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a7d0e6af-5edf-37dc-8f13-a52cdc745d0e | -6.94684 | -43.71798 | 2026-07-12 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f47c8fa9-d750-30ba-8d4b-1adcc7b16a3c | -8.72883 | -47.82885 | 2026-07-12 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38514b1d-ca5f-301c-bb6b-09e1fa988af6 | -7.91057 | -48.25402 | 2026-07-12 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| caebc283-0fad-30ab-aa8c-74bf04974bc0 | -15.89522 | -43.47786 | 2026-07-12 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 95070b66-fcf1-323b-9fb6-93cfdeea2c7b | -15.33765 | -42.90732 | 2026-07-12 03:57:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed332800-8473-36a8-a660-5d339e26c089 | -15.89463 | -43.47712 | 2026-07-12 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2f10fc17-975f-3ca1-acd5-e779347f7f1c | -20.06481 | -41.96849 | 2026-07-12 03:57:00 | NOAA-21 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b2b91649-0808-38aa-9fef-4bbbc8887028 | -19.3567 | -42.7284 | 2026-07-12 03:57:00 | NOAA-21 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 48164790-0cf7-3529-b9e5-962c5d74c424 | -15.89819 | -43.47776 | 2026-07-12 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a5b01806-4a12-36a9-8307-117b6c4bfc69 | -18.52407 | -48.24959 | 2026-07-12 03:57:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfcdbb94-753d-319d-8a4d-6a2448d91b34 | -15.33626 | -42.90733 | 2026-07-12 03:57:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8805a4d3-762e-3fb8-8355-1c83d0a2417f | -12.68446 | -48.19875 | 2026-07-12 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb431ffa-0028-3007-9441-2988c264450a | -13.76315 | -46.2567 | 2026-07-12 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6de161db-bae5-3466-aa3a-d737d7bcf2ee | -13.47684 | -44.04224 | 2026-07-12 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 83cae41a-13b3-3e8f-bf71-68ab708d9b40 | -15.89391 | -43.48131 | 2026-07-12 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 92dcd3ec-f887-3985-a92d-13a137758d48 | -19.49784 | -44.80573 | 2026-07-12 03:57:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59c05561-be46-3908-a159-3a9a59a8cd14 | -15.87936 | -41.80762 | 2026-07-12 03:57:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c68035f-a09d-3068-987d-420a69e3ab2f | -19.77145 | -46.67638 | 2026-07-12 03:57:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ad4dc9b-7442-3059-8bb2-2586be81a843 | -15.89451 | -43.48206 | 2026-07-12 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 39.2 |
| c92105f4-75ca-3a2a-b11e-6fb559297754 | -19.77212 | -46.67278 | 2026-07-12 03:57:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65ef15df-8675-3b43-a16e-d6959c6d24d3 | -16.24947 | -48.51627 | 2026-07-12 03:57:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c63820f-e3d1-3653-9271-5ebe9624e88e | -15.89746 | -43.48195 | 2026-07-12 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 505f2e78-84c3-3ef8-8bbe-c2966ed1af90 | -20.54493 | -41.8377 | 2026-07-12 03:57:00 | NOAA-21 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5fb9dd16-ee44-3a44-b4fb-1af96da4b95e | -13.76741 | -46.25781 | 2026-07-12 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de542e26-54ee-3b77-a421-84188f3987c0 | -13.82758 | -44.97226 | 2026-07-12 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a8e6049-3c04-303a-80fc-c16c88bcead8 | -18.22219 | -43.6461 | 2026-07-12 03:57:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43b72765-583f-3c06-9abe-5007adf04bbf | -15.08245 | -44.01405 | 2026-07-12 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6300ea99-6100-3d0f-95ae-c712b7c66a1d | -15.96193 | -42.35233 | 2026-07-12 03:57:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8b6ebe43-f899-3809-9b44-4906044be2d9 | -15.95791 | -42.35553 | 2026-07-12 03:57:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 47e08b6f-e675-3d3d-9962-dd51030b6f03 | -20.59897 | -41.75308 | 2026-07-12 03:57:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 662077a8-398f-35b8-8dbb-5ebe84d29ba1 | -19.30778 | -41.39806 | 2026-07-12 03:57:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| adcce164-6951-3d9d-8408-8a705d6b2436 | -18.22985 | -43.64329 | 2026-07-12 03:57:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d3fae6b-8ba6-3eb0-9b57-a5fe76906c3c | -15.23457 | -43.98477 | 2026-07-12 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83caec5f-3f14-314c-9f52-266069e22103 | -19.30448 | -41.39749 | 2026-07-12 03:57:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 85f00b61-d823-3751-92da-a6a15cc2d1a6 | -13.62256 | -43.71515 | 2026-07-12 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| de099dbf-cd34-3e62-8176-6a6d3149a37a | -15.89674 | -43.48615 | 2026-07-12 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| d2d338ed-dfd6-3373-8829-b3efb43244d0 | -20.61578 | -41.71083 | 2026-07-12 03:57:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 120d0d94-18d4-336a-a533-df5c3d259240 | -15.89877 | -43.47851 | 2026-07-12 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 09f3d186-c450-35b0-b249-04e62f8b8e40 | -18.22918 | -43.64728 | 2026-07-12 03:57:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61246b8e-b3a1-351d-8b6f-61f797446dc6 | -20.54551 | -41.83403 | 2026-07-12 03:57:00 | NOAA-21 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d8a9a262-9d75-34a9-930c-72169f5794d5 | -15.89807 | -43.48271 | 2026-07-12 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 39.2 |
| ce37811b-bf94-3fe9-b20a-4ecd268bd7d5 | -15.85688 | -41.72017 | 2026-07-12 03:57:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e8fc6c4f-c6e2-3299-875c-fcc8b4ac3085 | -20.61247 | -41.71025 | 2026-07-12 03:57:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 708ce31f-f828-399a-9cdd-3267b8185e21 | -13.83153 | -44.97303 | 2026-07-12 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6bb3a25-8891-3d4b-88c7-755382e8dd08 | -18.52155 | -48.24652 | 2026-07-12 03:57:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 347a47c0-3b59-3f7c-89a5-87cddebfd446 | -15.8949 | -43.4766 | 2026-07-12 04:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 4539b03f-f1bc-32ec-a169-0d43e233bd43 | -13.3549 | -54.3386 | 2026-07-12 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 8f229a44-f0e7-38c0-8e5e-963ae40633b4 | -13.374 | -54.3365 | 2026-07-12 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 50334f16-6c39-35d4-81d0-bd7918f12740 | -13.3743 | -54.3159 | 2026-07-12 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 05221110-7595-341a-9134-d6e451d6e0e3 | -13.3552 | -54.3179 | 2026-07-12 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| f893a586-0e6d-38a3-b5d9-07bc8ede219f | -13.3743 | -54.3159 | 2026-07-12 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |


[Clique aqui para ver as próximas entradas](README3.md)

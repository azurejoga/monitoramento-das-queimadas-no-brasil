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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 640a3aa2-b664-3287-ae4b-c8e0cfb2c714 | -19.98644 | -49.99294 | 2025-11-28 03:46:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 3f6219b6-2e03-3689-b02a-dec47b8ca532 | -21.64866 | -48.62558 | 2025-11-28 03:46:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b89ed216-e7a1-3914-b680-059669a9cb7b | -21.69029 | -47.957 | 2025-11-28 03:46:00 | NOAA-20 | AMÉRICO BRASILIENSE | SÃO PAULO | Brasil | 3501707 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4061fa70-33a5-3845-ac59-2b6d7133176e | -22.47075 | -49.12477 | 2025-11-28 03:46:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0da00bd8-c8f7-385c-8fa1-b634f77e1d6d | -20.46612 | -47.47975 | 2025-11-28 03:46:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbabc57f-a5bf-3d34-a1d0-d663f3a1d2d0 | -21.65469 | -48.62329 | 2025-11-28 03:46:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4504c9e-4895-3224-9eee-2d5f8b6d46a8 | -19.98419 | -49.99101 | 2025-11-28 03:46:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 57acc88f-d512-373e-a0ca-a215e533636c | -21.6853 | -47.9556 | 2025-11-28 03:46:00 | NOAA-20 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4bce1ad-757c-3e5d-835a-3059a6ce8354 | -21.64946 | -48.62198 | 2025-11-28 03:46:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b71b472-1877-3245-be23-7937feca95e0 | -19.98538 | -49.99769 | 2025-11-28 03:46:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 3f4ecf3a-947b-39eb-bc86-7a8087436894 | -19.98056 | -49.99148 | 2025-11-28 03:46:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 9e94768c-ab89-3f31-8cff-d880612dca22 | -22.47347 | -49.12594 | 2025-11-28 03:46:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8ad0338-89fa-3f4c-b9e2-d8b4705af2f0 | -21.65023 | -48.61844 | 2025-11-28 03:46:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 701356b1-80c8-399a-81db-6db4d60c8eb4 | -20.82892 | -47.2095 | 2025-11-28 03:46:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ce8c440-6c77-3c24-b527-58b01d1bcb67 | -21.33268 | -48.57206 | 2025-11-28 03:46:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f7df4c29-f555-318a-963f-eae8f3e2e35d | -27.38034 | -51.40194 | 2025-11-28 03:49:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf625a34-f596-3750-88fa-bbb4bfca7bcc | -27.68674 | -48.75248 | 2025-11-28 03:49:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| aad957f4-ea66-3c97-8cef-1d343870daac | -27.13218 | -51.20695 | 2025-11-28 03:49:00 | NOAA-20 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ebbd161a-b159-32ac-8f6d-ecc7697bf98e | -28.14195 | -48.80065 | 2025-11-28 03:49:00 | NOAA-20 | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ddc22fce-6c24-3fea-973e-92ab9fd139e2 | -24.62343 | -51.53295 | 2025-11-28 03:49:00 | NOAA-20 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e6e76dd1-c99d-3b81-8a40-fb51788bb79a | -27.38121 | -51.39836 | 2025-11-28 03:49:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b5f374be-2aa9-31fe-909f-b59f90b69217 | -22.95586 | -48.69558 | 2025-11-28 03:49:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa5908f9-da9a-3e5a-bb60-e56fb1190835 | -2.6181 | -47.3521 | 2025-11-28 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 26a60885-f1db-3402-ab3b-19dacc4ab6bd | -19.9973 | -49.9861 | 2025-11-28 03:50:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 789ae52f-db51-30cc-aa3c-864d86ba0c5a | -31.47387 | -51.25074 | 2025-11-28 03:51:00 | NOAA-20 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| c27a760d-444e-3937-87d2-65618b00a278 | -31.47307 | -51.25408 | 2025-11-28 03:51:00 | NOAA-20 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6ab70601-8ee1-3975-88d3-b9a349f1d2ff | -3.7694 | -46.96 | 2025-11-28 04:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 28315c82-1e01-357e-aad4-187bd5a46d27 | -19.9973 | -49.9861 | 2025-11-28 04:20:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| a40503d9-9e37-3666-a738-5d2b93066951 | 0.65845 | -51.53905 | 2025-11-28 04:29:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0f0ee7b-1f76-37aa-b936-fbc16a92c25b | -6.5631 | -51.1126 | 2025-11-28 04:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0e6f1c10-e288-32d7-b3aa-ec9d6f9c2e85 | -2.93873 | -51.4235 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f887f39e-1304-378f-8618-65446a950802 | -3.76322 | -46.95642 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d6bcdd3-48aa-3cfe-acd5-682a9a8751dd | -4.79886 | -45.38782 | 2025-11-28 04:31:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eef2e6f-9031-312c-a887-50e5ee9fd51e | -3.45283 | -50.21585 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41c02f8a-773b-3bfe-a1c7-88eaf778b83b | -2.73032 | -51.83752 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3342bfd-6ab9-396e-9040-2babec76a7fe | -4.0081 | -42.3121 | 2025-11-28 04:31:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6621b759-bdd1-3045-81ce-08e19a494843 | -5.43318 | -49.30268 | 2025-11-28 04:31:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cae391f-9559-325c-819c-954fa7ffa158 | -3.38884 | -50.2577 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35ef58c1-fc55-3033-baa5-6ea858b55fd1 | -2.42897 | -45.78432 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03b5c53f-c293-36ec-93ae-d9c037ee9fec | -3.07844 | -50.35146 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 290756a0-91ec-3347-bad5-ed934e2e531a | -2.62564 | -47.35482 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 80773a9b-7b02-3006-86f2-1e157d668aac | -3.5277 | -51.63383 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05b23f64-1f2a-3c46-a328-4ee8ceb6d02a | -3.17362 | -48.60357 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fff915c1-ffc2-3343-9285-d1183242db21 | -5.53486 | -46.97923 | 2025-11-28 04:31:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afd646a2-df38-3911-9fc3-1cec6e8b8b72 | -3.51382 | -43.67867 | 2025-11-28 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 417e3130-2be2-3345-b2c7-6d934f8e77d9 | -3.76045 | -46.95247 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ead8f63-cd27-3259-b6b9-666f425fe362 | -2.64857 | -46.97139 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f31fae4d-eb66-3481-90eb-305aba0cf54e | -3.73959 | -50.03546 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13af6a54-0213-3c54-a58c-0703af394a56 | -2.43619 | -50.26204 | 2025-11-28 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e90af1b4-03a7-31a1-b141-264dd7b72b84 | -5.05109 | -47.4412 | 2025-11-28 04:31:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d34bdc61-cab0-3a2b-a3c8-b1ce54704d89 | -2.84076 | -49.52902 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45097b06-897e-31b2-bbc0-5d9b0a6f2391 | -3.41055 | -50.95002 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5aab329-0dbb-3507-8628-0d3f4e3e8537 | -3.66999 | -45.40745 | 2025-11-28 04:31:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e494f618-d028-38fe-be5f-5b49690601b2 | -2.61902 | -47.3538 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f80356c-f53c-359a-8daf-bb8bf32a70e7 | -2.23129 | -47.50491 | 2025-11-28 04:31:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 417080fc-1af2-3dd5-add4-34a25994d429 | -3.32382 | -44.16514 | 2025-11-28 04:31:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c777ee3f-8329-354b-ad5e-5366c1476f54 | -2.64634 | -46.96403 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78937882-cc29-3239-8fe4-6bc162c4006f | -4.71021 | -46.28851 | 2025-11-28 04:31:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e90ac48-34f7-35b0-85ff-b830ac05393a | -3.22144 | -50.79548 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71c50c05-5636-3ed3-bfcf-3222f0f89c0f | -2.84015 | -49.5329 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16687ee9-e94b-3e6d-8134-20bccdab8dea | -5.75475 | -45.11174 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c8996b0-7340-3381-8aef-4ee128d829ea | -3.51316 | -43.68303 | 2025-11-28 04:31:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebe09bba-4545-3f38-ade5-4f9eea1efb37 | -5.36047 | -47.55018 | 2025-11-28 04:31:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b008ba9-a573-3cda-8fd0-af669a9f5ac7 | -2.61518 | -47.35673 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 013bdc60-5b9d-3658-8739-75fbd0bee851 | -5.43553 | -43.0518 | 2025-11-28 04:31:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 983f4dae-1ae6-32ca-9e21-578aa422c6fd | -2.42217 | -45.73988 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e97a570-07aa-37d6-b09b-27467d88834b | -2.41072 | -47.59643 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ec5301e-0a56-3eb3-8722-ce0b4f9780ec | -3.89281 | -47.23428 | 2025-11-28 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21493794-06c4-33f0-aa69-66aa1725b9f2 | -2.71692 | -45.21837 | 2025-11-28 04:31:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92ea3171-8d04-3afc-8c2c-73184ca1bd1c | -2.93742 | -49.44843 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d8354a8-1daf-332f-b90f-1322913b7967 | -3.23394 | -50.59647 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e21e3a8d-2020-314f-b7df-83501f2ae110 | -2.80106 | -51.90533 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8adfc4ac-84f1-39be-9d07-ae5a2cb93ef1 | -3.86444 | -40.64375 | 2025-11-28 04:31:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0d33fda-eb05-3c83-bc50-628e9aa5c349 | -2.62287 | -47.35087 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a8f7464d-2791-3867-bf3a-496144768b2e | -6.50084 | -47.41559 | 2025-11-28 04:31:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e1301d5-d38a-356d-afcc-7893fac88590 | -4.67455 | -43.25357 | 2025-11-28 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 642acd53-9e7b-3cbe-b7f4-e4f2feffa810 | -0.86354 | -47.65772 | 2025-11-28 04:31:00 | NOAA-21 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d47bf79f-61d8-3531-bd90-85941dd9640c | -4.01211 | -42.31275 | 2025-11-28 04:31:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a5cc08ff-465c-38fd-8af4-f372f5bb9db2 | -3.85525 | -47.04186 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b856a80-2670-3d25-83ac-63c20dc50258 | -5.44974 | -44.68612 | 2025-11-28 04:31:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 50af684d-9f73-31d3-af6b-0fb60f6f5eb3 | -1.34539 | -55.44799 | 2025-11-28 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7692585b-04b4-3aa4-b54c-49a6a8823e9b | -3.71915 | -50.44998 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3eaa4a8-253d-3d9a-9d6e-fd3f3872e281 | -3.86662 | -42.27657 | 2025-11-28 04:31:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30e57d3c-7bb1-354c-b68f-b4f506268479 | -4.71076 | -46.28497 | 2025-11-28 04:31:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea071340-b455-3716-b82c-6f5113b6ed44 | -4.2397 | -48.57372 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ffe02d-4f7e-3475-a235-4b3e825b438f | -3.67044 | -43.56234 | 2025-11-28 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c75d81c0-6a6d-3cdf-b5d6-05aa70704daa | -2.61187 | -47.35622 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a212358b-163b-3a7d-b7bf-86c3b06f01da | -3.29812 | -42.4233 | 2025-11-28 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6933b051-d23d-38cb-afbb-372c348c8a16 | -5.74118 | -47.98887 | 2025-11-28 04:31:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19ca6cc5-8e40-3539-b3db-40730de24a7e | -3.6761 | -46.51146 | 2025-11-28 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35ea966a-cfeb-33b2-86e3-6263618bc5ae | -4.54844 | -48.64349 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59fa4c1c-36d1-3e53-a12a-889b94a1cce6 | -4.39841 | -45.80146 | 2025-11-28 04:31:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ea96d8c-ca51-347b-a7b8-c303f680f2bf | -4.24396 | -43.67444 | 2025-11-28 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e59042ba-6225-3c5a-bc04-68806db04ccf | -2.96552 | -51.0193 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e968ed57-f367-3393-be94-f1563a359f4e | -3.15483 | -50.17621 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b92aac49-a4ca-3e92-ade1-041278361727 | -2.8406 | -45.16623 | 2025-11-28 04:31:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 383299e5-b3c9-3723-9167-257fe0280a94 | -3.33937 | -45.16187 | 2025-11-28 04:31:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0972c4c1-7e2f-3e59-9234-74d17dad42c0 | -4.37321 | -55.71722 | 2025-11-28 04:31:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ba4ba76-5c72-37f5-9fa1-9f4290e8a1bd | -5.53432 | -46.9827 | 2025-11-28 04:31:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11f06923-a0db-341d-a2d1-208bcce7fb18 | -3.72535 | -43.45303 | 2025-11-28 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README9.md)

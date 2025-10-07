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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67d6dc4f-c838-3141-8ab1-8bd9618c98d9 | -5.22595 | -43.79587 | 2025-10-07 04:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d455b2c0-e4c4-3a11-a514-1bc64aab1a67 | -8.20037 | -44.18025 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb487b89-0c52-395c-a775-06633353000c | -2.53837 | -54.7399 | 2025-10-07 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e334f87-fca2-3ce5-b519-161a122b7b1c | -5.57753 | -43.57307 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4a5c8bd-bb3f-39e5-8d66-c6620a18d9f0 | -1.08815 | -53.70056 | 2025-10-07 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8003572-4a16-3967-8d30-66803ca7957c | -4.44049 | -43.23377 | 2025-10-07 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa16344a-9148-3ae5-a323-5c5456e783ad | -3.09388 | -47.02908 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e07eeb63-057f-3e84-93c3-6c7d473884af | -6.64632 | -41.98587 | 2025-10-07 04:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 43fefe60-4c1a-3dfc-9209-7d3a7ea928f3 | -3.13849 | -50.44948 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ade8e7b-cc22-31d8-93c7-f719f1080c0b | -5.49238 | -43.07584 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5acc4f5a-9d22-3f8f-8b2e-85f27aae3e5b | -6.07611 | -42.55935 | 2025-10-07 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83806e8f-03c8-39da-8492-cd770470e15c | -8.20557 | -44.18507 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7441bb75-e117-3f62-914e-03c7d27b0244 | -7.72337 | -42.40417 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3147d4e6-91c4-3107-97bc-816e31e05a81 | -5.48642 | -43.07506 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4e964101-4c3a-3142-865e-1f3c5a2acc08 | -5.7991 | -45.21613 | 2025-10-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 291fa7fa-3602-3639-9a72-096f64c8d10d | -2.73999 | -54.68605 | 2025-10-07 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5dbc742-7a03-3f05-a968-39b8bb15a6f2 | -5.49835 | -43.07655 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 52240edc-e9bb-3f90-813c-ef3edd87aa13 | -6.10786 | -43.08971 | 2025-10-07 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 688b11cf-b397-341b-b1d6-276355b52d37 | -1.3418 | -55.47153 | 2025-10-07 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e287b643-8644-34bc-b05e-0492616f2edd | -3.19891 | -51.01428 | 2025-10-07 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f12f3976-5d30-30bd-abab-5d5689c445d9 | -3.10392 | -47.02189 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cc198b7-c74e-36a5-a65c-66a354b623d7 | -8.19831 | -44.20347 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e0e6aad-1732-33de-96de-de450ef0c386 | -3.20901 | -54.95845 | 2025-10-07 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd1b43a7-045f-3845-8650-ff82ebadcd41 | -3.08875 | -51.24992 | 2025-10-07 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 993899fa-d0a2-38f8-ada6-2d907300be49 | -3.08675 | -47.01647 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b88dc24-10da-35df-a0dc-2fc0c639c65c | -3.20238 | -51.0148 | 2025-10-07 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e29d9d3f-09cd-3cba-9417-2d7ceb67bf03 | -7.88357 | -47.81879 | 2025-10-07 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b13dd695-4ba4-34fa-8a63-166879ef30b9 | -6.98366 | -42.86489 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| a2ee74af-de63-35d3-a134-b31846fda690 | -7.72181 | -42.4012 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8c86a26a-6cc2-381f-96a3-63e3c8032e78 | -7.68316 | -42.41348 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ef395a47-f866-3810-8c5f-e92b84458cfb | -1.56528 | -55.43377 | 2025-10-07 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afd210d0-9b93-30ec-8cce-d95920c4b8ca | -3.08577 | -50.58035 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cf1ac938-37cf-3805-a03e-6cc52e5fa175 | -6.74777 | -49.04066 | 2025-10-07 04:55:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9daba67f-0527-33f5-8381-cec107fb36c0 | -4.56669 | -55.9618 | 2025-10-07 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19fdd5c5-5c08-3318-89d2-ad4781ab0a33 | -4.6872 | -45.8361 | 2025-10-07 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e1a50957-c766-3def-a262-916cab244551 | -7.01863 | -42.78753 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0623c69e-cc53-3415-a08c-43d5bb9e7adb | -4.87434 | -50.89882 | 2025-10-07 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f2e06c0-9098-3e4f-b4c2-9b61f84fad68 | -2.89208 | -50.73311 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5779ddb1-cdbe-3d9d-9688-20489c136b70 | -4.69135 | -45.84192 | 2025-10-07 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 35.2 |
| c2fbd6e3-697b-3ed5-bb6c-1bd06f2fdbf9 | -6.07544 | -42.56409 | 2025-10-07 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b740913-b6e7-3cf8-8a07-c87682a54416 | -8.20393 | -44.19716 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6866b575-9c25-3a35-b0f7-546116870ba7 | -5.10003 | -56.15855 | 2025-10-07 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 496750f6-7231-3da8-9e25-c395c88c7665 | -5.75795 | -43.3889 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f52a8c6-9c68-3ee5-b970-4d9c27d1e3cd | -4.58858 | -47.03448 | 2025-10-07 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8514c83f-8a0c-352d-a51f-f78182eecdc0 | -5.4954 | -43.07283 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f035185c-4739-3cea-bcd1-9cc73b252525 | -3.09514 | -47.02054 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| a012eb19-038d-327f-91ac-caa2d4a2c0b0 | -7.68443 | -42.40336 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7a50767d-bc38-3155-b949-9f820d5093ea | -4.44806 | -43.22234 | 2025-10-07 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dfc1d6be-c5d8-331c-aa36-c7f5f3158cae | -5.15027 | -49.84823 | 2025-10-07 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| da61e096-2022-3429-a79e-2543e54a60c2 | -5.25067 | -46.56865 | 2025-10-07 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3dbcf9d7-1b41-33d4-abea-92dfe2e0d106 | -7.02298 | -42.75427 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 60c6402c-0dcb-3066-b930-063f43c26010 | -8.20666 | -44.18403 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6b21fd2-e77a-32c7-a850-fc9ebc2d3c4a | -7.69016 | -42.40948 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| fe55cb8a-872e-3b43-9d9c-4ee324e1ecbb | -5.76882 | -45.74458 | 2025-10-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 312f3569-0489-3ade-898d-015e113bf474 | -5.50198 | -43.06932 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| fd740689-79ab-3a65-85b5-19cbc2cef43e | -4.57077 | -55.95853 | 2025-10-07 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49883735-47d5-3d27-bbcf-797e625977da | -5.70929 | -44.83325 | 2025-10-07 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6526367f-7fca-3a89-adf1-dd2f6009cfd0 | -5.33125 | -49.3268 | 2025-10-07 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c88eafa-c0c0-3e5f-b0d3-a35bd12fabf9 | -5.22541 | -43.79967 | 2025-10-07 04:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18b5a633-7971-3ee3-9bfe-8ea327eda6e7 | -5.48819 | -43.08073 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4a876eb3-2f2d-3ce5-853f-df55fb5643e6 | -5.75657 | -43.39124 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f5784c6d-151b-3fbf-8ca8-b2c4acf38078 | -7.69848 | -42.3952 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4a1269d9-7748-3de8-b78c-e0c613027720 | -7.7211 | -42.40643 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7853ab0b-9109-38ac-888f-d56c8abf9dbc | -5.65539 | -43.19053 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b004f50e-789c-3932-af09-ab5ea2453522 | -5.55104 | -42.68707 | 2025-10-07 04:55:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| eac66e39-319c-31f2-97a6-216e755dbe6a | -3.81623 | -51.86342 | 2025-10-07 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b434d880-f1fc-3fb2-b0e8-2b9b11378d71 | -7.70333 | -42.39331 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 67dd2520-1b31-35ad-9c40-a3a7895e995c | -3.81265 | -51.07358 | 2025-10-07 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27974b94-4b2c-3120-a056-2bda80815b23 | -6.69551 | -42.87027 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 28381966-140a-3651-aee1-d460a88c7898 | -6.71609 | -42.80893 | 2025-10-07 04:55:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45e20c05-d516-309b-ab5d-3476d6d471ed | -5.09654 | -56.15799 | 2025-10-07 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b2988d3-0e41-37db-965f-54901cdeb58b | -5.39326 | -40.98806 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 5593733e-2f52-311c-aa84-fe29a7b717db | -3.08833 | -51.24867 | 2025-10-07 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 54728797-fd16-3512-90ed-ed32e357693f | -5.03321 | -45.56279 | 2025-10-07 04:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92b225e5-bbb5-357e-ae2d-361b6fca502a | -5.75601 | -43.39539 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 028cd0aa-f1a0-320b-84c5-a3d5bc332d5d | -7.02017 | -42.78221 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4361128c-d441-3ea9-824d-cacddd175521 | -5.48222 | -43.07999 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4bf8d1f6-428e-328e-beb4-b78e51f7e581 | -5.74109 | -44.98795 | 2025-10-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a408ec9-04ac-3359-a443-082951012aee | -7.71632 | -42.40842 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 17f48fd5-9edb-3995-84c8-19c73b083943 | -8.06395 | -48.48129 | 2025-10-07 04:55:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a0b5212-abb1-3ae5-9ec8-e9506c9b4416 | -3.08636 | -47.01917 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15889e6e-fe17-350a-8f9f-418760169322 | -7.07151 | -55.45343 | 2025-10-07 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fc2a515-a0f3-399f-9149-d013b88dd679 | -7.98565 | -49.95967 | 2025-10-07 04:55:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27d3bd97-a123-38ac-97be-d27d1f7184b9 | -3.4746 | -52.7652 | 2025-10-07 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae793e3b-853b-3ee1-bdba-99cccde15cc0 | -3.08991 | -50.57696 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f660c59-7af8-343e-a6d0-640376014c66 | -6.98235 | -42.87449 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 6c0a7044-83fd-303c-94d3-60a926847688 | -2.89763 | -52.86933 | 2025-10-07 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1470ac82-70fc-3320-8bc7-b0b6728401e6 | -3.08776 | -51.2524 | 2025-10-07 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10fb0729-f702-3bcd-b036-140da428273d | -5.49479 | -43.07707 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 893290a6-e470-345f-9fff-ad56e6f416dd | -8.20009 | -44.22539 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 887d3c39-69d0-30f5-9b03-61cf52be72b2 | -5.50076 | -43.07775 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0c3ca767-f0dd-32a4-bcb9-359e7771f15b | -5.49354 | -43.08566 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6ce1336c-fd98-381e-93a8-7fdd35c8e95c | -3.09225 | -50.58534 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 308c93d9-3d88-3370-a12d-6d880ce81994 | -7.02922 | -42.75483 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c8bc0d37-d722-3eed-8432-9f36132f987b | -3.40598 | -52.72607 | 2025-10-07 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09a7e45b-f68f-35b8-b43e-a5bc09c16747 | -5.37657 | -50.8996 | 2025-10-07 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 338c2af0-7a2b-361a-b309-410d722b784b | -3.09641 | -47.01201 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 797fa760-8d8c-32a5-b3da-0463e02d872e | -8.20448 | -44.19311 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 389a230a-650f-34b2-b010-6b6c89ffeff3 | -2.88857 | -50.73257 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77dbb4b8-d6f6-3d8d-9cd1-8c5d5e2293e5 | -5.98623 | -44.14909 | 2025-10-07 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README84.md)

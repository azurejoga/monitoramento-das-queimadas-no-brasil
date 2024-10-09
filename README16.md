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
| 3a019ef1-6ddf-3750-a032-d8465db10035 | -6.6741 | -43.9617 | 2024-10-09 00:41:10 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc4930fa-ae7a-38e0-bc45-1af59a150143 | -7.8552 | -49.645199 | 2024-10-09 00:41:11 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 335c5885-4ebd-3dfc-9e4d-115e05e4feb8 | -7.3164 | -47.373402 | 2024-10-09 00:41:12 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edc9ac8c-831e-3e9b-ac73-c93f991e9d4c | -7.4164 | -47.861801 | 2024-10-09 00:41:12 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f321ae68-2faa-3c4a-ae2d-3765877d0679 | -6.187 | -42.598099 | 2024-10-09 00:41:12 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2b9e4a38-2477-3cf6-9235-35e5e552dd17 | -6.4878 | -43.870998 | 2024-10-09 00:41:12 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1667b2a-dcaf-3f6d-bb9b-eaf118fdff42 | -6.478 | -43.873299 | 2024-10-09 00:41:12 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40775a6b-8530-341f-835a-0d78bad68f54 | -6.3189 | -43.373001 | 2024-10-09 00:41:13 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d27a782-31f9-37df-8f28-2564a24ab6bc | -6.3092 | -43.375301 | 2024-10-09 00:41:13 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02393a48-7b37-3584-96d6-71486c706bda | -7.434 | -48.352001 | 2024-10-09 00:41:14 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ffe09937-bf4b-31ec-ae3b-e0974201a9ae | -7.2018 | -47.686199 | 2024-10-09 00:41:15 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30840221-e061-34a1-a53c-1cf89cf07ac6 | -7.2033 | -47.693199 | 2024-10-09 00:41:15 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3c0a0c1-3e63-3438-bca3-7aa41bd87c67 | -7.2049 | -47.700298 | 2024-10-09 00:41:15 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cc75d32-6116-3c1e-b413-d7d155834744 | -7.2511 | -47.996201 | 2024-10-09 00:41:15 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 681755e3-649e-36a3-b934-1fa5156032b3 | -7.2527 | -48.0033 | 2024-10-09 00:41:15 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00e52bd1-f90b-3ab8-868e-cc9285f49562 | -6.4181 | -44.587399 | 2024-10-09 00:41:16 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63cc633f-9ce3-3ea5-978a-720131ff41f3 | -6.4198 | -44.594898 | 2024-10-09 00:41:16 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 298ffe46-5383-3bc0-bc7d-9f6215527e71 | -7.0867 | -47.860401 | 2024-10-09 00:41:17 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b03dc668-b397-3c24-86fb-652da6e39109 | -7.0883 | -47.8675 | 2024-10-09 00:41:17 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe179c26-4311-39c4-b99d-e58ca3c8b8dd | -6.1685 | -43.697701 | 2024-10-09 00:41:17 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e4987ef-34db-3a71-bdb9-411211d77c20 | -6.1704 | -43.705898 | 2024-10-09 00:41:17 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb03b1db-80c7-33f1-a35b-b747aa24e4a0 | -6.1606 | -43.708199 | 2024-10-09 00:41:17 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ae9a0e8-41e3-3cd3-85a4-bf1619bc72da | -6.1583 | -44.0061 | 2024-10-09 00:41:18 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e1e1ce6-8dce-324c-ab2a-1ff2219d4e62 | -6.1387 | -44.0107 | 2024-10-09 00:41:18 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96665458-55a6-3315-b39f-83759aceda38 | -7.4308 | -49.6763 | 2024-10-09 00:41:18 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 010db824-9070-364b-8868-fac08aa7fa6c | -7.4326 | -49.684601 | 2024-10-09 00:41:18 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71af2d2c-04f5-37a0-8022-25a3717de9e5 | -4.8535 | -38.651001 | 2024-10-09 00:41:18 | METOP-C | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4f9a0403-9f17-3bea-8190-c248e825cb6d | -4.8578 | -38.668598 | 2024-10-09 00:41:18 | METOP-C | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 79d28131-1def-343f-a88a-8697a9aeeaf4 | -5.9667 | -43.192299 | 2024-10-09 00:41:18 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| f607de69-3cd0-3815-ae7d-99d2dc6b44bc | -6.1564 | -43.9981 | 2024-10-09 00:41:18 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 936ab8bd-65ce-3891-bc9a-3b1b80d0ed0e | -6.1876 | -44.263599 | 2024-10-09 00:41:19 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b86f863f-ccf8-30db-8fce-e152c6112bd7 | -6.1894 | -44.271301 | 2024-10-09 00:41:19 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a55018e6-00e8-3282-a06a-172080acf701 | -6.6652 | -46.325199 | 2024-10-09 00:41:19 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 547fd2ef-559d-30ac-b7ff-60791b656373 | -6.6668 | -46.332001 | 2024-10-09 00:41:19 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a726bcb2-b037-3781-a706-d110e2d6b3d5 | -6.6684 | -46.338902 | 2024-10-09 00:41:19 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9edd5052-d570-3a4d-898c-b84557952714 | -7.0468 | -48.049099 | 2024-10-09 00:41:19 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eedc20b9-6657-32a6-afb9-03ebe87f4b74 | -7.0484 | -48.056301 | 2024-10-09 00:41:19 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38512616-6700-3e1b-8559-cc842c92350e | -7.05 | -48.0634 | 2024-10-09 00:41:19 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d88047eb-4e11-39ae-947b-f8d7e6267174 | -6.2522 | -44.805801 | 2024-10-09 00:41:20 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fcbc25e-fc5b-3016-8156-b250bcfb7a66 | -6.2539 | -44.813202 | 2024-10-09 00:41:20 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f3abf89-a5e5-3556-a2be-d0b59dc77094 | -6.0585 | -44.020802 | 2024-10-09 00:41:20 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4994d58-8c3d-3824-bdec-0fe8ecaadaef | -7.2641 | -49.480202 | 2024-10-09 00:41:20 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a2ccc1c-eac3-3476-b445-5c214aae8774 | -6.7256 | -47.2215 | 2024-10-09 00:41:21 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e2983d5-fc78-330b-9003-726f36ccc50b | -7.0127 | -48.5382 | 2024-10-09 00:41:21 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cffb784-97b7-383a-bde4-7c496ffbe22f | -6.6664 | -47.097099 | 2024-10-09 00:41:21 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf7850a9-5e49-3baa-b929-3d606df36b11 | -6.668 | -47.104 | 2024-10-09 00:41:21 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c4dff3c-6989-3cc2-b7a4-a71b58147d65 | -5.818 | -43.217701 | 2024-10-09 00:41:21 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21335e47-77e9-3508-b9f1-e9bc53281ab9 | -5.8201 | -43.226501 | 2024-10-09 00:41:21 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09827b82-e9ca-3c3f-aef4-049d1ab6d491 | -5.8221 | -43.235199 | 2024-10-09 00:41:21 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb715a38-2f99-32b6-979c-716859c595c5 | -5.8083 | -43.220001 | 2024-10-09 00:41:21 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7a6a3e5-1f29-3752-92f3-d5c51cbeebb9 | -5.8103 | -43.228699 | 2024-10-09 00:41:21 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a591015-fe3c-3e65-ba18-d531f4de6271 | -6.6582 | -47.106201 | 2024-10-09 00:41:22 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 098af91c-ebc1-3e63-badd-a8d3d3e25f08 | -6.3293 | -45.716599 | 2024-10-09 00:41:22 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 823c15dc-0d1a-3958-aa3b-5347a2a76ceb | -6.6193 | -47.071499 | 2024-10-09 00:41:22 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11378758-4514-3592-943f-2abf0786ddbe | -6.6209 | -47.0783 | 2024-10-09 00:41:22 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1882ddc7-2ce3-3d69-80e3-cdfcdd666d2f | -6.6225 | -47.085201 | 2024-10-09 00:41:22 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ddc4e80-918b-3830-8f8d-0b5ab6895837 | -6.009 | -44.514702 | 2024-10-09 00:41:22 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0066eb4a-a789-39ef-8e0c-f3f2ed3280fe | -6.0107 | -44.522301 | 2024-10-09 00:41:22 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cc1e498-56db-37cd-acf9-0ded98158415 | -5.8477 | -43.737499 | 2024-10-09 00:41:22 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd4308dd-0cd4-3aeb-974d-84bdb95c86b7 | -5.8496 | -43.745701 | 2024-10-09 00:41:22 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d055aec9-cb81-3655-bff0-2fd50d3a99a0 | -6.0025 | -44.619701 | 2024-10-09 00:41:23 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c46da5e-da30-3c5b-ae53-8dd73857e2db | -6.0042 | -44.627201 | 2024-10-09 00:41:23 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a241adf-6653-3290-9464-c8cacca037d6 | -5.9927 | -44.621899 | 2024-10-09 00:41:23 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8781fab6-6104-33eb-884d-96ea15b0ccb5 | -5.9944 | -44.629398 | 2024-10-09 00:41:23 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 711d6def-d188-367a-bad8-9c33d3ecac0e | -8.2976 | -55.096199 | 2024-10-09 00:41:23 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ece1e7a-d669-3f6c-a734-587078e9b8f7 | -5.9626 | -44.5812 | 2024-10-09 00:41:23 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cbdae1f-2888-3e7c-9038-7b6150c63f07 | -8.2839 | -55.079201 | 2024-10-09 00:41:23 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7105a365-a106-3a6a-bd55-0be6ae3ca00e | -8.2879 | -55.098202 | 2024-10-09 00:41:23 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66086e15-c9b1-373a-94e1-0f1b56a11271 | -5.1816 | -41.279301 | 2024-10-09 00:41:23 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ecfe068-7655-3be7-b2d7-0f8d882a7767 | -5.1844 | -41.290901 | 2024-10-09 00:41:23 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 476fb5ae-96f5-325d-906c-88ee77d2f8d1 | -5.9511 | -44.575901 | 2024-10-09 00:41:24 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b9d5c36-07c1-3dd4-9699-42b3fe20e457 | -5.9528 | -44.5835 | 2024-10-09 00:41:24 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 854db64d-056d-3584-9a85-23bee90a29ea | -6.344 | -46.318298 | 2024-10-09 00:41:24 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ec54718-24bd-35df-9b7c-7ffca1ee7dd1 | -6.3456 | -46.325199 | 2024-10-09 00:41:24 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b67c5ba0-bb47-377f-acbf-4de6541dc9d8 | -6.3472 | -46.332001 | 2024-10-09 00:41:24 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4af901e-1844-37e7-8a2f-742900c9b1de | -5.8115 | -44.111301 | 2024-10-09 00:41:24 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f01d051-0a1a-348d-90b7-73e892098f15 | -5.8133 | -44.119202 | 2024-10-09 00:41:24 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1785f230-4eaf-3503-a5e1-a4076752dc09 | -5.8152 | -44.127102 | 2024-10-09 00:41:24 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bc75b07-b0b5-3a7a-b4ed-d15adaca0dc7 | -7.1218 | -49.8577 | 2024-10-09 00:41:24 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62e7ef38-efe9-3b6b-8676-ed9543489c6c | -7.112 | -49.859798 | 2024-10-09 00:41:24 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 538d3bfe-6a33-3779-8f95-df3bf47bf31e | -5.9109 | -44.624901 | 2024-10-09 00:41:24 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ee23ff8-98a8-38b7-9529-fb5aed494725 | -5.9126 | -44.632401 | 2024-10-09 00:41:24 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41ad79cc-32ca-33a9-ad03-ee8e5b623570 | -5.5869 | -43.243801 | 2024-10-09 00:41:24 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bc9336e-c94e-3b06-9df4-45969efba538 | -5.589 | -43.252602 | 2024-10-09 00:41:24 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcc12cb5-ae74-3ed7-ac3b-69f52016881a | -5.8091 | -43.969101 | 2024-10-09 00:41:24 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d798aca9-31bb-351f-907a-05273f53a88b | -5.5771 | -43.246101 | 2024-10-09 00:41:25 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4fa4ea5e-f4d2-3df4-b060-cd0c359c3399 | -5.5792 | -43.254902 | 2024-10-09 00:41:25 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdda1eec-a5c5-37c4-93ea-6148b835276b | -6.2907 | -46.986401 | 2024-10-09 00:41:27 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04af7240-87de-3cb3-8f78-27a5f93dbf22 | -6.0929 | -46.3027 | 2024-10-09 00:41:28 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2db4489-4bb3-31f9-a752-1d90f3c2a7e6 | -6.0818 | -46.4786 | 2024-10-09 00:41:29 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ead5103c-81f7-3bc7-bd19-2121681300ee | -6.1044 | -47.028198 | 2024-10-09 00:41:30 | METOP-C | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abb243af-96a8-3be4-9522-8cb671aa8368 | -5.5834 | -44.857601 | 2024-10-09 00:41:31 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fffbaf63-2ecd-3e65-8bf8-0f2a4af5c717 | -5.5851 | -44.865101 | 2024-10-09 00:41:31 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 442cb388-3464-3dd0-8ddc-fe8c2fe590a3 | -5.5868 | -44.872501 | 2024-10-09 00:41:31 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bd837f5-13f4-3bca-a872-c0e7cb91f472 | -5.5885 | -44.879902 | 2024-10-09 00:41:31 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d695734-bfa4-36be-ace5-049757b1e87c | -5.3175 | -43.7206 | 2024-10-09 00:41:31 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fba4b457-6e33-3420-9422-bb2b5dbb6ca7 | -6.6439 | -49.787201 | 2024-10-09 00:41:32 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b1c9dca-419e-3017-8ad0-4112ca7924c8 | -5.2333 | -43.8013 | 2024-10-09 00:41:32 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8414ac33-946e-3407-b015-3b83d5036c94 | -5.2352 | -43.809601 | 2024-10-09 00:41:32 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8968fec-c4bd-30cf-9b49-a4d6bceb5970 | -5.2372 | -43.817902 | 2024-10-09 00:41:32 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)

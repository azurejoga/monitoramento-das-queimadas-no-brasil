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
| 2160ee76-1708-3a71-9aad-458c50b020d2 | -11.7401 | -43.2928 | 2025-10-14 01:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 241.4 |
| e78e0436-07c2-3fd7-97a8-d16fd2107d50 | -12.8181 | -50.6786 | 2025-10-14 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 2281208a-2e1f-34eb-afc5-4e38c035ede2 | -7.9253 | -44.1169 | 2025-10-14 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 4b34a34f-7dc2-3989-b2af-ea2bb8893901 | -4.1048 | -50.0647 | 2025-10-14 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 4a630e32-70b1-3a0d-8976-5e23b33e29f1 | -4.1235 | -50.0428 | 2025-10-14 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 4d82c52d-8787-397b-81b5-df475a8d096f | -7.9251 | -44.1401 | 2025-10-14 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 5dfddd6a-b900-3778-91cf-c1eb891e7683 | -11.7406 | -43.269 | 2025-10-14 01:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 6e750013-b43d-39e4-813b-68aa90775f68 | -11.7406 | -43.269 | 2025-10-14 02:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 4e7fb70d-3ec5-32a5-9c6b-12357fc0aec9 | -5.4937 | -43.0761 | 2025-10-14 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 5d53cdae-7763-31ef-814f-354f7ad71647 | 1.8952 | -55.6829 | 2025-10-14 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2fbb1eea-567a-3aa9-9c8f-b8dc7de1c687 | -4.1235 | -50.0428 | 2025-10-14 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 7f4384c2-056a-3c6f-b548-c12c4c7f466c | -4.6696 | -43.1326 | 2025-10-14 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f1e32733-fc1c-3be7-8d86-0e9e704ce56b | -11.7594 | -43.2898 | 2025-10-14 02:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 160.5 |
| 2017bd3e-ba5c-33f2-b1f6-f62b9a745a17 | -11.7598 | -43.2659 | 2025-10-14 02:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 1864425e-638d-3d87-b2c3-68715dc88869 | -5.1181 | -43.1964 | 2025-10-14 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 25704810-b98a-3000-9f3d-d928d42d34c2 | -5.0994 | -43.1977 | 2025-10-14 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 75c9ff83-633c-3687-9639-3adc2fc7d40d | -4.6698 | -43.1092 | 2025-10-14 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 03539910-2fce-31d9-a2de-832553a33a2c | -4.105 | -50.0436 | 2025-10-14 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| afebade1-604e-30c8-ac07-126c918f1638 | -7.9439 | -44.1381 | 2025-10-14 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ab4e25cf-f5a8-3edf-9d5d-e14f065cc6f4 | -5.494 | -43.0526 | 2025-10-14 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 07f4f4ee-86ac-35e2-a534-98d0261d409c | -4.1048 | -50.0647 | 2025-10-14 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| ce9d9423-c1e7-391a-84c9-e1676688d906 | -4.6694 | -43.1559 | 2025-10-14 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 44086d5c-ce36-39d1-b9a0-fe3d7480b0fe | -7.9631 | -44.113 | 2025-10-14 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 6e725411-ff62-3da5-9fab-9981808db186 | -4.6509 | -43.1337 | 2025-10-14 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 6e7c6e8f-c1b7-3db3-beae-a00e7cb54bad | -4.6321 | -45.7639 | 2025-10-14 02:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| c156eaa5-c715-39eb-a892-7def01122a91 | -7.9253 | -44.1169 | 2025-10-14 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7cf24daa-f62b-30c6-89f1-e8e7f9083e10 | -7.9442 | -44.115 | 2025-10-14 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 149.6 |
| f8b674bd-44e0-3c93-a52e-30d4163382e7 | -11.7401 | -43.2928 | 2025-10-14 02:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 182.5 |
| 1a4ad0b6-5049-323b-8dc3-f2521189f1d1 | -4.6319 | -45.7863 | 2025-10-14 02:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 726a7b12-8bc0-3ef7-8990-7d0ab6f43885 | -4.6883 | -43.1314 | 2025-10-14 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| c4ba967e-d966-3afe-835e-cfb60ca61d9b | 1.8768 | -55.6832 | 2025-10-14 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| c7b5f479-bb51-36c3-9b9a-c3c829f4bff2 | -12.8184 | -50.6571 | 2025-10-14 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 39699b00-ab44-33c6-99ff-5120a79fbc86 | -12.7993 | -50.6595 | 2025-10-14 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e31e572b-bb29-3bab-82d9-b56b27f2fb79 | -7.9628 | -44.1362 | 2025-10-14 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1c057e9a-7755-3a99-85ac-e175dc866a79 | -7.9442 | -44.115 | 2025-10-14 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 22163b05-3402-318c-8154-2dbfeb9df68e | -4.1048 | -50.0647 | 2025-10-14 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 590b902f-2b4b-334e-914d-af000b8e6d51 | -12.8184 | -50.6571 | 2025-10-14 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 5bdb3471-a797-33ad-abb6-6f507627c33a | -4.6694 | -43.1559 | 2025-10-14 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| ed9a391a-dd42-39e9-a5a5-78cd0dd2431d | -12.8373 | -50.6762 | 2025-10-14 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 02239c73-8353-37fd-a2f8-4f8605651a37 | 1.8952 | -55.6829 | 2025-10-14 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e77d3ebd-1384-375b-9044-d005ab421540 | -13.0064 | -50.8694 | 2025-10-14 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a5debebd-0b4c-3cf7-8240-608a1cf8b692 | -4.1235 | -50.0428 | 2025-10-14 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6e45a93a-b1c0-39a7-959a-11b9f0a02a6e | -4.6696 | -43.1326 | 2025-10-14 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 970f9997-2f9a-3dab-a5c5-63eba0167f6c | -12.8376 | -50.6547 | 2025-10-14 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| f288e9a5-3570-3724-9047-f99ec647c783 | -11.7594 | -43.2898 | 2025-10-14 02:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 700969d8-929f-3e9e-8ef8-8eec01e94f4e | -11.7401 | -43.2928 | 2025-10-14 02:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 221.9 |
| 7510ab28-8442-3490-a00e-b501b5c28708 | -12.7993 | -50.6595 | 2025-10-14 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 16af78fa-bfbb-3253-a643-8f30bae6d593 | -13.0256 | -50.867 | 2025-10-14 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| cb9bba5e-8fc8-3da3-bbf4-9c64c17fc4a6 | -12.8181 | -50.6786 | 2025-10-14 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 09cc712a-1388-3711-9e77-0ab7cb6836dd | -11.7406 | -43.269 | 2025-10-14 02:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 5ff81f09-432f-37a8-91eb-5cfce988cf55 | -4.6134 | -45.765 | 2025-10-14 02:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fd8281be-4e7d-370e-8617-debdbf10c9e2 | -4.105 | -50.0436 | 2025-10-14 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 717a3aad-37bc-3b72-9154-dee1504eba43 | -4.6319 | -45.7863 | 2025-10-14 02:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b91637d0-8ec1-3416-bef1-b5b059314d31 | -4.6698 | -43.1092 | 2025-10-14 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| bec4bcf8-4f1f-3e96-8def-98f998371315 | -4.6509 | -43.1337 | 2025-10-14 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 46502988-82da-3bdf-9536-f4919e319302 | -7.9439 | -44.1381 | 2025-10-14 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 4acf608d-d0fb-34ff-a5ba-b4f826ae9cc9 | -5.1181 | -43.1964 | 2025-10-14 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 7852bd0a-a2c2-31e1-9f9a-9203b5d68027 | 1.8768 | -55.6832 | 2025-10-14 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| c56940f4-7bfd-342f-b043-ec9742378f79 | -7.9253 | -44.1169 | 2025-10-14 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| dfe05d4f-c47b-3451-9d49-4e08548cc701 | -12.8188 | -50.6356 | 2025-10-14 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| d0410384-c934-3e4b-92db-3f619a181d2c | -4.6883 | -43.1314 | 2025-10-14 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 1c445437-de48-339f-a18a-b44f4901e4fc | -4.6321 | -45.7639 | 2025-10-14 02:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b0a145e3-a580-32d6-944d-c7017eb0678e | -11.7401 | -43.2928 | 2025-10-14 02:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 145.9 |
| 36f2fbe4-849c-3689-8d3a-e706c4a756b1 | -4.6509 | -43.1337 | 2025-10-14 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| f79996b8-1ef2-325a-b79f-956aeac12073 | -11.7594 | -43.2898 | 2025-10-14 02:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 111.1 |
| cb991c1e-1d4c-3694-8c9b-d8729af1d110 | -7.9253 | -44.1169 | 2025-10-14 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 222d7232-7f1e-32dd-8b80-d7d8c6b5ab1c | -5.7405 | -40.7628 | 2025-10-14 02:20:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 84.0 |
| c6365aa3-3050-3ee6-8123-3619eb5f746b | -4.6696 | -43.1326 | 2025-10-14 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 9aa0a419-aa8e-3c11-95a2-8bfd2032541f | -4.105 | -50.0436 | 2025-10-14 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e3d43d67-3929-34cb-aa97-a9cf78628af7 | -4.1048 | -50.0647 | 2025-10-14 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 286d28c2-4b6e-3c74-947a-9f3f49e1ae30 | -4.6321 | -45.7639 | 2025-10-14 02:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7fc98d57-fa1b-3b13-9df0-27b0fea24554 | -4.6694 | -43.1559 | 2025-10-14 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 277f7aef-f498-3ff3-bc23-6a5c8228bb91 | -4.6319 | -45.7863 | 2025-10-14 02:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| eaac3919-2c61-3ef1-a998-5f78a01fa23d | -5.0994 | -43.1977 | 2025-10-14 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 101a7792-dafe-327e-ae0b-8c2c522edee8 | 1.8952 | -55.6829 | 2025-10-14 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ea4d7d38-db40-3cfb-a27f-b3d54a916fb5 | -7.9442 | -44.115 | 2025-10-14 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 202ed190-c0c5-3308-8443-f9131363a4e5 | -4.6698 | -43.1092 | 2025-10-14 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 528a1338-662b-36da-b338-86d52c4697e3 | -11.7406 | -43.269 | 2025-10-14 02:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 561cdb85-cac6-3f81-8ffb-6bf60d37a275 | -4.6694 | -43.1559 | 2025-10-14 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 00642978-a813-3091-bec0-a59960eb1dc5 | -4.6696 | -43.1326 | 2025-10-14 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 1bf5d65a-9e77-309f-95ab-3ecb3406aa44 | -4.6321 | -45.7639 | 2025-10-14 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d8bec93c-c08c-3527-a7b0-629f05759e73 | -7.9628 | -44.1362 | 2025-10-14 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 6d244190-7937-3524-98c0-24583c02fc92 | -5.7405 | -40.7628 | 2025-10-14 02:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 143.8 |
| 62501346-12a2-3ea6-98de-3d9b01c0ad2e | -5.7594 | -40.7612 | 2025-10-14 02:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 103.2 |
| e7e6e6d6-c226-3040-897a-d8108d6bca5e | -7.9251 | -44.1401 | 2025-10-14 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 94c6d9a6-0941-3ed5-ad2a-acaeebdc5e9c | -4.6698 | -43.1092 | 2025-10-14 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 7761ed21-eed8-3a2a-a209-dde14cf04b19 | 1.7667 | -55.8031 | 2025-10-14 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 396353ee-c964-3134-8cac-5547d7e6b001 | -5.4937 | -43.0761 | 2025-10-14 02:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| e4034b11-1cf5-36c3-b5d4-2edb6cdd6da9 | -4.6319 | -45.7863 | 2025-10-14 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c1f675ba-d5d9-30ee-8812-fe5f4c0128c8 | -11.7401 | -43.2928 | 2025-10-14 02:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 131.7 |
| 7aa97b0b-aede-3b5c-8001-ca11e6c6768e | -4.6509 | -43.1337 | 2025-10-14 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 392d1d7e-9b38-3830-bb4c-55b68e7a2d77 | 1.7667 | -55.8228 | 2025-10-14 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b8534d56-02b2-3950-af3b-9b4ba0327335 | -7.9253 | -44.1169 | 2025-10-14 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| f29b0d2d-298a-3ed9-ab99-e8cd3132ba51 | 1.8768 | -55.6832 | 2025-10-14 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d128fca2-42ff-3117-a7ac-3369b3d40aa7 | -7.9631 | -44.113 | 2025-10-14 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b07a9765-375b-3710-85db-f35b27c7eab1 | -5.7403 | -40.7872 | 2025-10-14 02:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 1c718095-20b9-3c6d-93af-c51aac5600b4 | -7.9439 | -44.1381 | 2025-10-14 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 16e8a3aa-79d8-3cf9-9934-67ab006430bc | 1.8952 | -55.6829 | 2025-10-14 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| adae90c0-ce33-3cab-9415-7257ef48d863 | -11.7594 | -43.2898 | 2025-10-14 02:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 615b2294-2da9-3002-9a32-8350bf5f4d25 | -7.9442 | -44.115 | 2025-10-14 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 181.2 |


[Clique aqui para ver as próximas entradas](README5.md)

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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa7b62a0-25ac-328b-a531-46dd505281b9 | -5.23703 | -47.49893 | 2024-11-21 12:48:00 | TERRA_M-T | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1acf0a0b-afde-3d30-a65f-3f144e2cdcec | -4.74505 | -49.88464 | 2024-11-21 12:48:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c5648977-a5df-352e-94e8-e5b63c12be9a | -4.00979 | -49.92675 | 2024-11-21 12:48:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| b7b88559-5c16-3a1c-abce-461428357a51 | -3.85868 | -44.53439 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7aa141d4-f1c5-3ec5-8263-f308cd1b0329 | -4.40796 | -43.0407 | 2024-11-21 12:48:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 4b06a9d6-b73e-345b-a0cc-e9063b6b3230 | -4.16446 | -42.02654 | 2024-11-21 12:48:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| b5c8ec7a-4d5f-3fe1-b00d-91ba158650d7 | -5.45254 | -43.22965 | 2024-11-21 12:48:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 8e8881b8-1482-38ea-bf3b-640cabec692c | -2.87513 | -45.63441 | 2024-11-21 12:48:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fc0818e1-2c87-3179-9cec-9ad050b70901 | -6.35389 | -42.87008 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 8c0be853-286d-3459-bc96-8cb703538e09 | -5.11221 | -43.16621 | 2024-11-21 12:48:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 486c966b-487d-3d5a-8593-a8328a059bc0 | -3.54706 | -50.19237 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 30e46c4e-29f9-3788-80fa-a2189c604895 | -1.84965 | -47.06401 | 2024-11-21 12:48:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 20a851e9-0445-3d86-bfdb-ecbb2d4593b5 | -6.94892 | -47.84448 | 2024-11-21 12:48:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 120c19cd-6832-3b70-940d-f55f2c2f2fcb | -3.69082 | -50.21558 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ce3ba717-ff82-34bb-825e-166e7913b138 | -1.45912 | -47.91376 | 2024-11-21 12:48:00 | TERRA_M-T | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9b3610ae-fca2-34af-af22-3b4e8c42596b | -1.96197 | -49.92073 | 2024-11-21 12:48:00 | TERRA_M-T | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c9a8024f-d245-350d-bf01-e7a87ce7a6d4 | -5.28576 | -46.17596 | 2024-11-21 12:48:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 374944c8-6557-3593-92f8-ff8f4f8a1999 | -2.71966 | -49.34374 | 2024-11-21 12:48:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e4001aae-60cb-35c1-9c3d-26de4daeb8a6 | -4.48678 | -43.31469 | 2024-11-21 12:48:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 2ae61c2f-e93c-3c7f-b62c-7764f721c597 | -4.55464 | -43.5755 | 2024-11-21 12:48:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 9b7e3f2d-29e6-3f49-9245-00193f4a49de | -4.58101 | -48.02084 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 46e6e313-c69d-3cc9-a976-1dd817af2ca4 | -4.56636 | -48.51212 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 68c6126f-4fe1-3768-8c0a-895721305b4e | -3.39371 | -44.57104 | 2024-11-21 12:48:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 22.8 |
| a32f1188-8daa-317d-af59-4f38f86e5656 | -1.86804 | -46.42683 | 2024-11-21 12:48:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ae0e48ae-9ac5-3ef6-ab45-e61fa4afc98d | -1.54584 | -47.31424 | 2024-11-21 12:48:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 68de60b7-80a7-3246-aaa0-bd98e56b81e5 | -4.63753 | -49.54377 | 2024-11-21 12:48:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3e14e256-edcf-396a-8abe-e055fa764c90 | -0.04842 | -51.23883 | 2024-11-21 12:48:00 | TERRA_M-T | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 67236c2e-3372-31cd-94d8-46b3e9bad308 | -6.21629 | -46.17711 | 2024-11-21 12:48:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 93470679-64d5-3512-932d-6ce87371157c | -1.04778 | -47.95664 | 2024-11-21 12:48:00 | TERRA_M-T | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 682f9f06-0b48-381e-83fe-8a1af67a66ee | -4.1628 | -43.92108 | 2024-11-21 12:48:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 0858e76d-d950-39dd-9818-05aa75cd2b85 | -1.67946 | -47.028 | 2024-11-21 12:48:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| f27bcdb8-8dea-38a8-a481-2ff5655dc889 | -1.85452 | -47.48178 | 2024-11-21 12:48:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 86b2ad2b-0b36-3bf4-ac79-37013288a365 | -0.90118 | -48.20717 | 2024-11-21 12:48:00 | TERRA_M-T | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d0d0a1cc-3596-3cde-b786-1a51b74e0e09 | -2.6274 | -48.06841 | 2024-11-21 12:48:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4aac85fd-2a1a-307e-be67-814c33331998 | -3.3357 | -50.49113 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 65362c77-5511-315d-a7e0-d25ac41703d9 | -3.53172 | -41.97593 | 2024-11-21 12:48:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 46.2 |
| 64b0f836-811e-3b2d-bf51-5df2a9d6dd6f | -6.94762 | -47.8538 | 2024-11-21 12:48:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a7b0e222-4d6f-3ce1-bfa5-67b6ecc45178 | -3.64491 | -42.00356 | 2024-11-21 12:48:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 12948366-8aa3-3995-b3b3-9fa0bbca57fa | -4.55754 | -48.51089 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 523e3a51-c93c-3af5-9f95-d7f54d94b834 | -3.40574 | -46.23671 | 2024-11-21 12:48:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 06e04fe1-c6fc-3de1-b6d2-73f685fd83e3 | -3.21948 | -43.68172 | 2024-11-21 12:48:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| ba51a4ab-09e7-3e23-830a-b4d76ffe1429 | -6.91988 | -47.52635 | 2024-11-21 12:48:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 396032d7-1138-30f3-8765-078376460931 | -1.61074 | -47.62786 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4cba7852-3445-37d4-b16e-0f8aa36a8aec | -3.48308 | -50.30999 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 19f175d8-ee38-3cbb-895e-fbdc10b7a490 | -1.98334 | -47.47905 | 2024-11-21 12:48:00 | TERRA_M-T | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 3823be07-d1ed-315d-9076-11475b984b56 | -4.22954 | -43.0046 | 2024-11-21 12:48:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7f77ffb6-25db-3257-b2e5-3b582741539f | -2.20353 | -48.95974 | 2024-11-21 12:48:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8e4c1b92-ddbe-3685-ad46-3b1223f225b5 | -2.32805 | -45.66217 | 2024-11-21 12:48:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9d69c92e-937a-3b38-a129-22248602d926 | -3.25326 | -50.55346 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 97c064d0-417d-3a64-8b63-88ac7f2d2266 | -3.53005 | -41.98141 | 2024-11-21 12:48:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 51.2 |
| 90a9040c-788f-3fef-8b50-9c47c0d6be66 | -2.64263 | -47.96299 | 2024-11-21 12:48:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9bcae05e-f50c-36e6-b21c-fb78a5239dc4 | -4.92846 | -48.49792 | 2024-11-21 12:48:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 97ed5577-949f-3fe2-928f-4e0ef8cd9197 | -3.51706 | -44.92819 | 2024-11-21 12:48:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 39318cd6-d4d9-3e2a-9be0-07bec81c1d8b | -6.21021 | -46.22063 | 2024-11-21 12:48:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 00286ade-701c-3336-ae94-770657f16011 | -3.51169 | -42.02015 | 2024-11-21 12:48:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 1fd90d90-e8ea-3037-b0f7-a8a5ea16461e | -2.94308 | -44.08521 | 2024-11-21 12:48:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 5162585c-dd1d-31fb-892e-9b62fc78f67c | -3.29394 | -53.85241 | 2024-11-21 12:48:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 56bebd44-6d9e-33e6-86c6-b039cad833b3 | -1.47649 | -52.51978 | 2024-11-21 12:48:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 45c7dc12-4780-3c82-9d1d-1ed870580114 | -3.04312 | -49.46959 | 2024-11-21 12:48:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 7705687f-e8cf-300e-9be4-f0d964da8b14 | -4.40274 | -50.52301 | 2024-11-21 12:48:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 967eb48c-f49e-339e-af6f-f4bc0576f31e | -1.42922 | -46.00974 | 2024-11-21 12:48:00 | TERRA_M-T | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c8e04f31-3c6a-3ce5-842d-3e7c5cc948c5 | -3.72795 | -42.53188 | 2024-11-21 12:48:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 4a0130e9-1553-3933-9fb1-35370a6c6c1d | -4.49434 | -50.1465 | 2024-11-21 12:48:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| d9e64beb-3c6a-3344-903c-0637a2659cad | -4.15379 | -42.01861 | 2024-11-21 12:48:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 282ba572-6979-3fc4-88b4-f071cb798fb8 | -4.50046 | -48.84356 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 277e2d65-ff8e-35cf-83ae-06e395c2ce7f | -2.95389 | -53.71735 | 2024-11-21 12:48:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 94bfe2e3-48cb-3de9-8d89-5a15ed6cb38c | -3.30755 | -50.87635 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6123c724-b5fa-3ed7-bd3b-3fda255fd461 | -3.27772 | -50.51662 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a5a941f4-ac9e-324d-9298-858f4f6075a9 | -3.5425 | -50.53311 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b2e4b787-5ac8-3a0b-a82e-000b685b9f7a | -4.27922 | -48.0057 | 2024-11-21 12:48:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 14d0378f-9e6e-3ddc-ae5c-85e3fc891617 | -2.23098 | -48.38166 | 2024-11-21 12:48:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9cb07ff3-2155-316b-aebd-44c411e66972 | -2.566 | -50.63756 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 18a6864a-6803-389c-b923-769483168b8f | -4.34456 | -48.31856 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6422e6a3-176c-3d45-a590-0136ebb66dc4 | -1.71728 | -47.40495 | 2024-11-21 12:48:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c5c18d62-44c2-3b67-9a34-1ae56d51c3cf | -1.2618 | -47.23813 | 2024-11-21 12:48:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c1741a17-546c-3cb6-88f3-75efb1ebd727 | -1.46946 | -47.5927 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d9b2e02c-3b6f-3ff1-8e43-1b415f62d420 | -2.82059 | -45.29839 | 2024-11-21 12:48:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f5417eae-88fb-35f3-982f-7c715a7da361 | -4.5823 | -48.01193 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d91baa0b-7a42-3562-9c32-718ee115e1fe | -5.07362 | -46.8268 | 2024-11-21 12:48:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 91f6bc02-dee7-399d-8aa2-d7450007bc74 | -2.61087 | -48.24503 | 2024-11-21 12:48:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5165fa3d-595d-38c1-9760-e15ce858c47c | -3.72989 | -42.53888 | 2024-11-21 12:48:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 0a74fd1d-3805-3955-8a91-6092ccee6185 | -0.90245 | -48.1984 | 2024-11-21 12:48:00 | TERRA_M-T | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d4c79c16-bb33-326a-bbe5-388daad0a0fc | -3.47154 | -50.01207 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| be7bf11b-ee2d-32b1-9ed4-5c2b499a4e8b | -5.10764 | -43.15897 | 2024-11-21 12:48:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f156679c-a8b8-3d10-a92c-c5fe54be534c | -3.87 | -42.27369 | 2024-11-21 12:48:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 7aa95af6-0c4f-335f-b5e7-fddc591ca96a | -1.46697 | -47.54737 | 2024-11-21 12:48:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 6868e3b5-99d9-3765-9e19-35f91b5e94e4 | -4.06129 | -43.9835 | 2024-11-21 12:48:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5a930e41-c098-3897-b538-2d4d652209d9 | -2.31001 | -46.87893 | 2024-11-21 12:48:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| d8de9df8-f84f-3a1e-b4b0-810c4345622d | -0.91907 | -47.81911 | 2024-11-21 12:48:00 | TERRA_M-T | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e6ed2106-5eac-3b31-bb8f-32863b85e1c6 | -6.23232 | -44.8121 | 2024-11-21 12:48:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 83dd2c7f-fe7a-30f5-ad99-6482413b80c0 | -2.38923 | -46.01188 | 2024-11-21 12:48:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 641d840c-cc7f-33b5-b3dc-6d125130cf31 | -5.45694 | -43.23687 | 2024-11-21 12:48:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| d5a85f36-d745-3414-8d70-c8f61b3259f8 | -6.12726 | -42.50208 | 2024-11-21 12:48:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 0b112d96-7981-3d48-8257-79b10ccfa562 | -3.27626 | -50.52654 | 2024-11-21 12:48:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 74fa29cc-7400-30fe-932b-eb3254802dd7 | -4.67236 | -46.53893 | 2024-11-21 12:48:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 7ede2ef6-8975-38fb-adde-9b0015ecbde6 | -1.19417 | -53.67763 | 2024-11-21 12:48:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 470ca8bc-aa05-38cf-9d53-a841f47c160b | -1.37597 | -46.51057 | 2024-11-21 12:48:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b658027d-b70f-33e3-8b0a-6624c3c6df1b | -3.29113 | -53.84136 | 2024-11-21 12:48:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| be986548-c96b-3c3f-9d3e-637bad7988db | -3.367 | -43.44693 | 2024-11-21 12:48:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 299cfa62-2fd6-3b07-9b99-cabb2cbd9adf | -4.2721 | -49.96378 | 2024-11-21 12:48:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README82.md)

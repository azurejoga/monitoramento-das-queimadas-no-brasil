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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8df4b738-c261-3593-bf23-d247b4edc54b | -5.02231 | -43.79571 | 2024-09-27 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 506a1fd8-bf69-376a-a0a4-cd14e4f2aafc | -5.01821 | -43.79514 | 2024-09-27 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 309d1a33-e925-30c0-a05c-612a1e41d514 | -4.82779 | -43.70324 | 2024-09-27 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c3f5b3a-4424-300d-86de-6c6f9122a86a | -4.82725 | -43.70695 | 2024-09-27 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e27a8132-65c2-3ec5-88b0-a5277251bf18 | -4.80381 | -43.30514 | 2024-09-27 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88dbf8a5-b18a-34d4-b105-4eb8c3494621 | -4.78512 | -43.71293 | 2024-09-27 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a0ae4075-d3c4-3ed2-9587-d30354146515 | -4.78456 | -43.71664 | 2024-09-27 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a69fc993-05b9-3c9f-a5be-2f2450fd18a2 | -4.78046 | -43.71599 | 2024-09-27 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a5cffed0-e24b-36c3-91fd-61a56708d7e2 | -4.82004 | -44.35256 | 2024-09-27 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 253be503-70dd-34fc-a034-91a10ae1bb2b | -5.99039 | -43.97848 | 2024-09-27 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8602089e-5066-3cb3-b670-a622d2ae5efb | -6.16409 | -44.29919 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3621bac2-b00b-3b96-a24d-9ee80610fcf4 | -6.10152 | -44.69723 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48b41f42-8379-3c35-b87a-b750a8522509 | -6.1008 | -44.70213 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc870fe5-c84d-37a3-9cb1-bdf4e8e24f72 | -6.0976 | -44.69664 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 380bcf48-b26f-3fac-8aaf-87d509d373f5 | -6.09688 | -44.70156 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 276ba65d-12df-3e5e-b914-f1cd3974854a | -6.09296 | -44.70097 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db4407df-c9a3-3807-879d-c1a9993d5c2b | -6.09006 | -44.72071 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95272d6f-afd6-32fc-8b74-f2df7082d11f | -6.08904 | -44.70035 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| baedca6b-82a9-385d-a7e7-665bb977e161 | -6.08513 | -44.69972 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8fd46ffe-ad59-351b-bbde-cf3a2404b0ff | -6.0844 | -44.70467 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 852617e4-2133-3cc2-89d1-a1593bc6b414 | -6.08049 | -44.70404 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a7dc103-6545-3f79-a809-32b29ae679d2 | -6.07976 | -44.709 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4bacda2-202f-3215-83ae-20423b53499e | -6.07585 | -44.70835 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a543575-a64b-3deb-8e68-2724ea8714b5 | -6.07513 | -44.71329 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f572083-b1c2-38d3-ac99-1786c44af315 | -6.07123 | -44.71264 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c9d11f4-c543-39fa-b5df-58f50627e4aa | -6.05883 | -44.02224 | 2024-09-27 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93ac24e7-6f25-3af4-9e84-414edbb6d614 | -6.05831 | -44.02588 | 2024-09-27 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 898eabf0-a4f0-316a-880d-c72ab8e7877e | -6.05779 | -44.0295 | 2024-09-27 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 90dbcfaa-309c-3ae9-a3e8-6bba15171312 | -6.04375 | -44.54655 | 2024-09-27 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cc33c31-f36e-3c24-a889-18b969e3b07e | -5.88568 | -43.86846 | 2024-09-27 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19ab570a-f1fb-359e-b69d-c3b0305b7ac6 | -5.87688 | -43.87104 | 2024-09-27 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1241c8a2-ec55-3f55-a467-182cf0764289 | -5.87634 | -43.87479 | 2024-09-27 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47ba5199-47d8-3195-aaab-ab601af61a2a | -5.87275 | -43.87043 | 2024-09-27 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98af9a08-d88e-3b7f-be97-c190a69337ba | -5.56082 | -43.69493 | 2024-09-27 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2cab233d-2dbb-399d-80f8-6b310cf9b070 | -5.40428 | -43.42953 | 2024-09-27 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 07277fc3-977c-366a-adde-ba37d95dd784 | -5.40372 | -43.43341 | 2024-09-27 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| bac3249d-b74d-3bc7-ac40-f783aa440959 | -5.40316 | -43.43728 | 2024-09-27 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 4952ecaa-1501-33da-8427-26ffd18fdb07 | -5.39951 | -43.4327 | 2024-09-27 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 554dbd11-057f-3629-96d7-86a2b0afae73 | -5.39895 | -43.43657 | 2024-09-27 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1637007e-2941-3930-918c-825e3fb8e507 | -5.76594 | -44.00451 | 2024-09-27 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3737c0e6-5848-325a-add5-9df4a55699d8 | -5.7175 | -44.81744 | 2024-09-27 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| baef566f-3ac4-31f1-8a91-e5417ab80dee | -5.71558 | -44.81464 | 2024-09-27 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dbde4b34-dcb8-3580-b82d-85ac9e9aa072 | -5.71488 | -44.81948 | 2024-09-27 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81781b9b-788d-3e99-8d21-bb8761bdd738 | -5.71362 | -44.81689 | 2024-09-27 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0cd748e9-88f4-3ecb-9ba0-c997479ba3f8 | -5.57691 | -44.41703 | 2024-09-27 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12c203d4-7ce3-3d10-9c7b-bc107570c97e | -5.4528 | -44.31327 | 2024-09-27 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee6945ac-e1ef-366d-b80d-ee8cff6b94c6 | -5.20633 | -43.48044 | 2024-09-27 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e7bda94-bc42-3f15-9a83-4eb9df968694 | -4.61762 | -45.76608 | 2024-09-27 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 420d2ba0-63cd-3d65-9ee2-1ea05927bfd3 | -4.61462 | -45.76148 | 2024-09-27 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38547f63-1364-363d-9c14-0420d765097c | -4.61399 | -45.76562 | 2024-09-27 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d6c3fd6e-dc14-3235-b645-5415e0afc7fd | -4.61338 | -45.76971 | 2024-09-27 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1c36d829-e97d-37fd-a0ed-9d84ed1c5600 | -4.61099 | -45.76101 | 2024-09-27 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54f91cda-43fe-3fd8-bce9-aabcce55f0ef | -4.61038 | -45.76509 | 2024-09-27 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32acd0c0-20ec-3243-bf21-6752dc725ec1 | -4.58434 | -45.68534 | 2024-09-27 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9ae170b-9217-359f-b12a-b89002067236 | -4.43026 | -44.71868 | 2024-09-27 04:38:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49ad177e-ab27-3008-ba06-449753541319 | -5.09155 | -45.21041 | 2024-09-27 04:38:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2507201-2841-3af3-b0f7-a30343cb9d0f | -5.01805 | -45.54374 | 2024-09-27 04:38:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1415d754-c035-3051-b193-193279b2d7cc | -4.92726 | -45.67482 | 2024-09-27 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25aa0642-8e6b-3b11-8584-301adcb63eaf | -4.92656 | -45.67596 | 2024-09-27 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b54061a-8113-3a44-84ad-10054f161b2a | -4.77249 | -45.75458 | 2024-09-27 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8d2911a-6c1b-3bf4-872e-9b0a1b77dde7 | -5.25156 | -45.95673 | 2024-09-27 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58332bf-d392-3d10-a053-ea9676684ad0 | -5.25093 | -45.96087 | 2024-09-27 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbf0b85a-2b16-32ef-bc2e-0375e33c2e2b | -5.24274 | -45.44393 | 2024-09-27 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 35e97730-86ce-3a8b-a482-3b5d217c9408 | -5.23971 | -45.43889 | 2024-09-27 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 04766965-e698-3040-bcbf-9c9bfc54a895 | -5.23904 | -45.44336 | 2024-09-27 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0169aac2-fd27-371f-ade7-b8a39e38dd3c | -5.236 | -45.43833 | 2024-09-27 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 060377f1-9f72-3401-bc58-a6b64d8e57f2 | -5.1982 | -44.94034 | 2024-09-27 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ac6d5500-e9c3-3d90-bd60-4fe497a71ad4 | -5.1944 | -44.93971 | 2024-09-27 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df0430d7-6aef-3343-8c35-4190e9870fcc | -5.11262 | -45.98772 | 2024-09-27 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 593d3faa-c928-3ae6-9366-ea5dba4389eb | -5.9017 | -46.162 | 2024-09-27 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45ed5a72-7822-3206-bf56-d163571b7d83 | -5.84267 | -46.38328 | 2024-09-27 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c61b942-5b1e-380f-a572-4124722311bd | -5.83912 | -46.38273 | 2024-09-27 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da315919-d9ab-32a4-83e4-3a809400c2e0 | -5.76192 | -45.79873 | 2024-09-27 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50f52b76-0e52-3544-add6-e0fb8bc6433a | -5.76128 | -45.80297 | 2024-09-27 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16ede540-189c-3d95-b5c2-ff47e8e9cf3b | -5.75762 | -45.80239 | 2024-09-27 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78aadcb9-d825-3348-82b9-60551c6f6418 | -5.75332 | -45.80606 | 2024-09-27 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03bd7855-d2be-3096-92d6-67b72092b18f | -5.73026 | -46.45661 | 2024-09-27 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82de690d-bd51-3fc5-bcce-e7085152cfb3 | -5.70549 | -46.45294 | 2024-09-27 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e9a4829-fd8e-3b00-9e79-bf09da12d80d | -5.70195 | -46.45242 | 2024-09-27 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 639d79c8-d79d-34a5-91d8-11c5a22cd9df | -5.58124 | -46.15068 | 2024-09-27 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2185965b-d080-34b3-b7b5-b9c14fdf94de | -5.57765 | -46.15017 | 2024-09-27 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15c5ca38-46c7-394f-8f97-0bf17c908e6b | -5.50703 | -46.37609 | 2024-09-27 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e25441f7-124b-30c6-8a2f-6c794fc5b555 | -5.50408 | -46.37157 | 2024-09-27 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1447ed60-b228-3d73-a29b-2373fc824d35 | -5.42458 | -45.47648 | 2024-09-27 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 59c7e079-3e84-3605-abe1-41b08e42344c | -5.42087 | -45.47593 | 2024-09-27 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 34bc6158-a9c4-3b30-9859-930a27a720c2 | -5.32291 | -45.40462 | 2024-09-27 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd6bc6f5-5c84-3344-b838-ba956d87f7f4 | -2.957 | -47.36061 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a614c9b2-4d51-3e4e-9c65-3e4f3968c135 | -2.74855 | -46.73168 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 854750b1-9fa5-3b13-9655-0fcabd38904a | -2.74401 | -46.71598 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1e7b589-f4e6-3074-bbd9-60eb53e6a14f | -2.74117 | -46.7793 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ca3deb0-f869-361e-b491-7dfe3dbffa45 | -2.73834 | -46.77512 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cddfce3-49b0-31f7-8c1c-1623f24f26ae | -2.73777 | -46.77879 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8193f0c3-8880-31ad-b502-ef95d602ce75 | -2.73324 | -46.7631 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc36aadf-8ff3-361e-bb2a-aed82febf3ac | -2.73041 | -46.75892 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e672f99-b5b4-349b-bc96-27df1ce82f84 | -2.72984 | -46.76258 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21d640ce-63f3-347d-8504-f87ee041df8f | -2.72928 | -46.76623 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35933045-706c-3cc7-ab16-71e9cac6bcba | -2.72926 | -46.7212 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b74287-2238-37e8-b2d7-1253edc713f4 | -2.7287 | -46.72486 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40ae3ecd-a8c2-3c73-bc1b-4102e89c726d | -2.727 | -46.73586 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c8a15f7-47de-33ae-b052-2d76cbab8e9c | -2.72644 | -46.76205 | 2024-09-27 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README72.md)

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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4bdd12e-34ef-3cd9-89ea-bc9c980157c3 | -3.9555 | -43.7542 | 2025-11-11 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 3c497c4b-8d9b-3f16-a9fa-9fd2636055a0 | -2.9232 | -45.3037 | 2025-11-11 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 516cd24f-70e4-3fb9-894e-ff6139fe93cc | -2.8855 | -45.4175 | 2025-11-11 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| deaff6ec-73d0-3d4e-b22a-5d34c96cb849 | -3.9554 | -43.7773 | 2025-11-11 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| ab8460c1-0617-31dd-a9de-e03eddf3ab85 | -2.8854 | -45.44 | 2025-11-11 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 40ac9eb1-339e-3b37-b4f9-1e076308332c | -10.5076 | -44.944 | 2025-11-11 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4f32b5d2-f719-3428-b068-5606638e9331 | -3.7837 | -47.7677 | 2025-11-11 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6825fa77-0e85-3644-b864-4673c5de2519 | -3.4316 | -44.0787 | 2025-11-11 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 0bbee1c6-49da-3fef-a904-233b3c24d9c6 | -3.974 | -43.7763 | 2025-11-11 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 098f3877-7e8a-37e4-a5fe-28a0fdc8dc1b | -10.4889 | -44.9235 | 2025-11-11 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 55121a48-33a9-3cf3-94ef-48b2f35e984c | -9.3794 | -35.9228 | 2025-11-11 00:00:00 | GOES-19 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.6 |
| fe5ee3e0-45c7-304a-ae4a-26cdc4fdf6cd | -2.867 | -45.4182 | 2025-11-11 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| cca48e35-f65c-3aa1-91c1-2299f551edc1 | -2.9046 | -45.3044 | 2025-11-11 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| bebd222a-b0f0-38f0-976a-bc02a9b2bf2f | -10.508 | -44.921 | 2025-11-11 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fbd8aa16-9df1-3cfa-9866-9550a26b6100 | -19.7223 | -58.0491 | 2025-11-11 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 58ad20a8-098b-3f48-96c1-20deea725db7 | -2.9233 | -45.2812 | 2025-11-11 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 9d716449-ffe8-3689-8bf7-c626c7c894b2 | -4.7204 | -46.4497 | 2025-11-11 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 6943379d-68e0-3e23-a711-abc8c8207ff4 | -19.7424 | -58.0465 | 2025-11-11 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 56f5dbda-2dfe-3704-bbb3-85e8f10a4510 | -10.4885 | -44.9465 | 2025-11-11 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 99ed1fe8-20c4-3da5-a847-c110be1900ce | -2.8669 | -45.4406 | 2025-11-11 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.3 |
| d14bd5c9-96ba-319d-936d-3581dc406ba6 | -5.4226 | -44.8348 | 2025-11-11 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f6fd7a45-ce18-3e56-9471-45adee96340e | -9.9828 | -44.4581 | 2025-11-11 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| b68eaaac-4e44-3f6d-9da2-05b467dcfa13 | -4.9036 | -44.3208 | 2025-11-11 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 0ead8e3f-828a-37fd-93fc-66983c4def67 | -2.9047 | -45.2819 | 2025-11-11 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 1319c889-438f-3296-9b02-2b715a16b2af | -3.7838 | -47.746 | 2025-11-11 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a416140f-ffc2-38e4-b064-eacef346d330 | -3.9622 | -43.787201 | 2025-11-11 00:02:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1654577-6ede-322b-8b28-f38657195a96 | -5.7505 | -40.805199 | 2025-11-11 00:02:00 | METOP-C | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 628d3f27-3de7-3e9f-a10e-fd7c7270605d | -3.0117 | -39.941101 | 2025-11-11 00:02:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 074015a5-fdff-31cf-9b91-91d992385054 | -5.5176 | -47.717701 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 853008eb-a241-32ff-bd73-0ced8f72ec37 | -9.1796 | -41.0322 | 2025-11-11 00:02:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c4609c32-366b-355f-8643-4a90079411c9 | -6.1005 | -41.5448 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4e94e0b8-886c-3a12-b4a2-8463b3750a11 | -5.331 | -35.546001 | 2025-11-11 00:02:00 | METOP-C | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 9c0e99ca-e34c-33b9-8894-22b744c364b7 | -3.9451 | -43.756802 | 2025-11-11 00:02:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06d2bb60-b585-3b3b-bdcc-9588791504d2 | -7.0692 | -39.665501 | 2025-11-11 00:02:00 | METOP-C | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| eabe7213-54ef-3fc8-9291-18d70bbf6e5f | -10.4815 | -44.9375 | 2025-11-11 00:02:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 080d42d3-d9b5-3e5b-8256-921184bc5df0 | -5.6336 | -41.063999 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7854fa04-5be6-32b6-825a-1962e38e846c | -10.9333 | -44.016998 | 2025-11-11 00:02:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64dfabf6-18c3-3fb8-a002-5c4baeecbce9 | -5.3987 | -45.242901 | 2025-11-11 00:02:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b4663b6-5bfa-32be-aa68-72d51a18aafb | -3.4294 | -44.063999 | 2025-11-11 00:02:00 | METOP-C | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b1fe1a3-1e20-3839-88b3-ba0cf0438d06 | -4.7127 | -46.442501 | 2025-11-11 00:02:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e97bb34-3fe9-3d90-8086-3d348676bea9 | -3.8537 | -41.564301 | 2025-11-11 00:02:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aceec8f1-4238-3def-b993-81fec6c8d9fd | -3.884 | -39.924999 | 2025-11-11 00:02:00 | METOP-C | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bd1e79b3-5b75-355e-b41e-b6137f2a4c3b | -2.9348 | -45.148102 | 2025-11-11 00:02:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d870bc5-56f1-31e0-a709-36f483105071 | -3.8684 | -40.991402 | 2025-11-11 00:02:00 | METOP-C | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cede4a0d-efec-3b06-90cc-e512a1ffe225 | -2.8669 | -45.438801 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20ad9de8-67c6-3535-9b46-79c62a0d8f69 | -5.3212 | -35.548199 | 2025-11-11 00:02:00 | METOP-C | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 5cfda843-03bf-3be7-a5fe-7abf0e19738d | -7.1022 | -39.353802 | 2025-11-11 00:02:00 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 54fb461f-6adf-3254-811e-c3e6eb22cd06 | -5.118 | -45.5928 | 2025-11-11 00:02:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a12550fe-baf7-3462-a15e-81591ca967e1 | -9.3822 | -35.924999 | 2025-11-11 00:02:00 | METOP-C | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6d78dea-3375-3ecb-a950-a80fef943854 | -6.7123 | -38.540699 | 2025-11-11 00:02:00 | METOP-C | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 275db96d-8017-36b7-b7c0-f50276d2e467 | -2.9122 | -45.2757 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78c67981-64cb-39a3-a99a-96bb676c847f | -7.0423 | -41.531399 | 2025-11-11 00:02:00 | METOP-C | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9a0fd25-a0c0-3f50-b51f-382dc495abab | -8.4967 | -40.583698 | 2025-11-11 00:02:00 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f1e8a562-059d-36dd-92f6-af43c1684c6e | -4.682 | -43.243999 | 2025-11-11 00:02:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b49fb504-3e0f-3d6d-b9d1-c4895b13ba25 | -4.6722 | -43.246201 | 2025-11-11 00:02:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7bead07-12dc-34c2-b9f5-4b0fc89da6f2 | -5.7744 | -44.016899 | 2025-11-11 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b5ce4a0-21ab-30c6-a210-cb9f2d4c1ea2 | -10.9304 | -44.002602 | 2025-11-11 00:02:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28d2e63d-0798-381e-b55e-0d619dde6e37 | -7.1239 | -41.2505 | 2025-11-11 00:02:00 | METOP-C | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8e2788e7-25aa-39be-9bca-f63366ac63c3 | -6.8875 | -35.0103 | 2025-11-11 00:02:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2459a629-f0ae-32c9-867c-e7b967685123 | -4.8992 | -44.317699 | 2025-11-11 00:02:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e828c2bd-fb6a-3d91-9abb-37198f24dbf5 | -10.4946 | -44.9519 | 2025-11-11 00:02:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1be3401-8e31-3415-978b-9e6c7530ccb9 | -9.9738 | -44.441101 | 2025-11-11 00:02:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9592d4a7-2f4e-3eee-a49f-19404ee3df73 | -9.3805 | -35.917801 | 2025-11-11 00:02:00 | METOP-C | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfcc537d-4326-3e36-aa04-aeae3ffdcaf6 | -9.1875 | -41.021301 | 2025-11-11 00:02:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d548a790-1e9c-3df8-a5de-ee8b553ef2eb | -6.8894 | -35.018398 | 2025-11-11 00:02:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92028873-8aed-3204-b0ec-b265b0675dbe | -9.9901 | -36.0993 | 2025-11-11 00:02:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05bbd89c-fd04-3132-8317-09e48d9f7e63 | -6.8856 | -35.0023 | 2025-11-11 00:02:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1627e9e7-1048-3a18-a31f-0648a47acd52 | -10.488 | -44.919201 | 2025-11-11 00:02:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f946f3b8-1746-3b04-94e3-f6fe0c6b5976 | -5.6434 | -41.061798 | 2025-11-11 00:02:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 906633e6-e4d2-3658-abd0-c155ff70403b | -10.501 | -44.933601 | 2025-11-11 00:02:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 336e6db3-9c07-3bc4-875a-776dd0e5c61c | -7.5897 | -43.6689 | 2025-11-11 00:02:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 25e7b68c-d11a-39db-b4fa-1c39d3c4293a | -5.1147 | -45.5779 | 2025-11-11 00:02:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4823dc4c-fba6-3b1d-bd2c-1a8e949d0bad | -2.9024 | -45.277802 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3995e25a-ff6b-3d56-a979-6adf9393db06 | -6.7139 | -38.5476 | 2025-11-11 00:02:00 | METOP-C | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| de89bc77-fe13-3f9d-a385-21fa766b8827 | -9.3788 | -35.910599 | 2025-11-11 00:02:00 | METOP-C | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b0d7807-055f-3eab-80d9-e2a5a75bbf2a | -3.95 | -43.7785 | 2025-11-11 00:02:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9860ce4a-9c01-3e13-8f61-9d44575e2309 | -6.3355 | -38.923401 | 2025-11-11 00:02:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 21907861-2b84-32d2-87fe-8b7e86eac1af | -9.1777 | -41.023399 | 2025-11-11 00:02:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 940ffe48-daf0-3d1a-bbd4-a1300b37e0da | -6.0847 | -41.5662 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 631c58bc-007c-3770-ac0a-bfa6fb77342d | -10.4913 | -44.935501 | 2025-11-11 00:02:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1580817f-8083-37be-92ef-6e3e7d969ece | -7.0383 | -39.757198 | 2025-11-11 00:02:00 | METOP-C | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| aad19b6c-92d7-3632-8110-290a791c02c5 | -3.4319 | -44.0751 | 2025-11-11 00:02:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b408621-f0ed-359a-8545-0f440c8bbf0d | -9.5111 | -37.978298 | 2025-11-11 00:02:00 | METOP-C | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| a2a08b67-6a93-3774-aae3-6ef3df219258 | -7.8853 | -42.480202 | 2025-11-11 00:02:00 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0a156e2f-63e4-3653-8dd7-961066c927f1 | -4.2093 | -42.918499 | 2025-11-11 00:02:00 | METOP-C | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 98dcc8b5-249e-3083-a794-17162cd2c070 | -6.4585 | -43.215302 | 2025-11-11 00:02:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 568d18ba-c82a-3552-9536-84eae57946b9 | -2.9376 | -45.1609 | 2025-11-11 00:02:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 229b881f-4907-3d78-97e6-6f05e3c5a8ba | -5.4185 | -44.819599 | 2025-11-11 00:02:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1771ab28-b02f-30d5-a093-bfc7aaf3abd7 | -6.334 | -42.8339 | 2025-11-11 00:02:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| d34497a8-b133-31d1-833f-b4482b21dfbb | -5.6274 | -41.082199 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2d22ce9-f277-3af8-aa3a-5efc4399dace | -6.2964 | -39.524899 | 2025-11-11 00:02:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b122042c-6616-393b-9cc3-6231cd89acba | -9.9641 | -44.4431 | 2025-11-11 00:02:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b9c2fe59-8aab-3aee-aa0a-e375358e9a83 | -6.9271 | -41.847301 | 2025-11-11 00:02:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 465112b6-9c76-310d-8866-572c4482dc1a | -5.0682 | -39.060101 | 2025-11-11 00:02:00 | METOP-C | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3e3626ea-d5d7-3290-89f9-6a8c5e1da8f9 | -5.4214 | -44.833 | 2025-11-11 00:02:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80a2cb16-c025-3c8f-92f6-2e99d0dd1491 | -7.883 | -42.470001 | 2025-11-11 00:02:00 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 55eb4c38-19b4-3384-90a1-299149078be9 | -6.7153 | -38.236198 | 2025-11-11 00:02:00 | METOP-C | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 1c910e20-cca8-3255-bbe8-d14fa3b90fbb | -2.8707 | -45.409801 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1808a3a7-4c61-35be-a1d1-f2dcdbf90413 | -3.6626 | -40.901001 | 2025-11-11 00:02:00 | METOP-C | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 13e70371-b84b-345f-9eb6-f6a8bb3440f7 | -5.3014 | -40.911999 | 2025-11-11 00:02:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)

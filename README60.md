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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f6dd15c-37c9-3e75-a99a-f1b5d89b947e | -6.1796 | -35.296 | 2026-10-09 03:42:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9f75f2c3-5b36-3b6f-80a8-6b18b07ba2ef | -6.82412 | -39.31509 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fda7e3c2-f012-3e36-9802-82422d8aee75 | -3.56457 | -38.88041 | 2026-10-09 03:42:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bb82bb29-d424-3835-992b-b3fb3f2331fd | -6.15871 | -39.44569 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| e06bb2be-9d51-353b-9da9-190778b6f424 | -6.8324 | -39.56693 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77ad563b-9cfc-319f-8d7f-9447a5a48de6 | -5.87612 | -43.41125 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fa3960f5-a687-37dc-b7ce-0764214019d3 | -5.88034 | -43.41981 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e3880b84-888a-3215-a842-1c04612f1c5e | -6.25016 | -45.32992 | 2026-10-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92458fba-27a5-3746-84dc-1f4efc9c8c5d | -5.09876 | -46.21884 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 150ba5f4-d0d2-38f8-849c-7143769dd9ef | -5.9962 | -40.93793 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 121bcb38-bda0-301b-b173-0044ae1fef4b | -4.82108 | -45.84137 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d1637f82-0e55-30bc-8340-e00565456aad | -5.09209 | -46.21764 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20cc94b6-aaf8-397d-9c37-cefefc38e235 | -6.15384 | -47.27904 | 2026-10-09 03:42:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4f56b037-5ae4-34a8-873c-7237627343fd | -4.97938 | -46.03869 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1246a9b3-d32f-3ff7-b24c-c265230eb1ee | -5.24543 | -37.58132 | 2026-10-09 03:42:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 065ed6bc-6492-31d8-b752-2bffa56d6457 | -6.15803 | -39.44963 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b2d28c9e-d1f7-34fc-858b-a6700ae412b1 | -5.18755 | -46.22286 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd23e903-d93e-3516-9c48-6de67bc28bb2 | -6.00596 | -40.97849 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 16d1d366-bff1-37dc-96d8-c34771807c64 | -5.96205 | -40.91236 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 58697615-476e-31a2-9bd2-30e20a67d539 | -5.88472 | -43.42189 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbfaca67-aff6-31e3-986c-2a130a97a666 | -5.36396 | -36.84989 | 2026-10-09 03:42:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6fe9eb3b-215b-3d63-a33f-8e5efca3388b | -6.16712 | -39.44724 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 4f87f5b1-6c40-3899-9487-9fbed610c5ba | -5.61537 | -44.37901 | 2026-10-09 03:42:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27e3d48c-6ade-3fce-b062-e4551a5ddf05 | -5.34527 | -45.1792 | 2026-10-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1ac31e4-53a5-3922-a7ba-33c18a2678f2 | -6.82884 | -39.5624 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d2afcab2-15e0-3af2-839c-1ab4a91ebe56 | -6.84681 | -39.55842 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 59ecc874-2f27-3033-be7a-44f9256fc478 | -3.21849 | -42.9646 | 2026-10-09 03:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bee532d-c665-397f-9a0e-2e79ae77e67d | -6.00302 | -40.95472 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 36.3 |
| a42c834c-6b39-36ac-aa08-08ffe5337bca | -6.21817 | -44.15276 | 2026-10-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab3f8893-8136-3f86-b090-f1f2738c0b83 | -3.03454 | -42.11048 | 2026-10-09 03:42:00 | NOAA-20 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0c6bca7-6384-3ecd-a99a-902a385d215f | -6.49563 | -44.36932 | 2026-10-09 03:42:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c100db96-4bf3-39f5-b060-18f632634d5c | -5.99485 | -40.98677 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b98ffea1-418e-39d9-b896-37deffc71aff | -4.80713 | -42.74281 | 2026-10-09 03:42:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c319ae61-5450-3d09-a7fb-0abeb7c3c3d0 | -6.00051 | -40.9697 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 21bff612-dc06-39cf-8d85-b64ce725975c | -6.1683 | -35.29519 | 2026-10-09 03:42:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f629814a-75f6-371a-a204-e85074ace8c2 | -7.0569 | -40.95078 | 2026-10-09 03:42:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1f106838-1628-363f-9f8f-b2285edcc8b2 | -6.19706 | -40.80365 | 2026-10-09 03:42:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bc7b97b0-cd45-33e6-a8cf-5da1ab4547d9 | -6.85345 | -41.75371 | 2026-10-09 03:42:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ce97037f-d49b-3ad4-ad41-3d41d2ca317e | -6.14752 | -47.28297 | 2026-10-09 03:42:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 89a29335-dda2-3413-9999-1a26693481a4 | -6.5015 | -44.37012 | 2026-10-09 03:42:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48366c46-3f91-37b5-a233-aa4cb8567ad2 | -5.99751 | -40.95882 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 29ae7167-fa3f-3a5d-9491-9ccc7f2d37c7 | -6.00304 | -40.96759 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 132.0 |
| cf488ebd-d0dc-3efc-83fc-3e8edca8f9be | -5.61287 | -44.84178 | 2026-10-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8322a9ff-e6d8-33b6-8a7d-4194d1b6c319 | -6.16292 | -39.44647 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 6006ae66-61e6-3957-ab9c-6f5cafa4e84e | -6.00519 | -40.97059 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 8978b8e4-d8a9-32a9-ba6c-2ac3e02c8916 | -5.99919 | -40.94882 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| fc3b8f7b-1da6-33e8-8add-fdc27711c867 | -6.24925 | -45.3349 | 2026-10-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 644060e4-6168-3082-ba6c-afe1d2d385f1 | -6.8582 | -39.46564 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| be7b946b-ca72-3b0f-81b8-add4b1d3a1f8 | -5.88587 | -43.42089 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| db1f1d61-291d-376b-b089-4976368cf615 | -6.88361 | -43.70616 | 2026-10-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f048e08f-59fb-3404-a3d8-d5409acda84f | -3.2129 | -42.96349 | 2026-10-09 03:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26dd2759-8468-313f-ab10-3d79072e128f | -5.08707 | -46.22636 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9764b402-32b6-33fc-a082-fa7ff6df6881 | -5.09775 | -46.2244 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b004649a-67b1-3d7b-a9ed-c26cc9911dc8 | -4.89092 | -43.34296 | 2026-10-09 03:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85922692-195b-39c2-9438-67707c440817 | -6.42607 | -45.94364 | 2026-10-09 03:42:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2cb92355-244b-3b7a-a714-60048c59350b | -5.88405 | -43.42558 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77d6d3c8-e1f1-3697-b502-fc12af836a74 | -6.8053 | -41.24086 | 2026-10-09 03:42:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43b815f9-0c70-3552-add0-84b28a3e5192 | -6.00435 | -40.97559 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d32b9d2d-028e-3388-9b3f-28fe062ac930 | -4.93414 | -45.72634 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7734fc5-15a0-3ae7-ad91-cdc9a2f2174a | -5.99667 | -40.96385 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ea01f750-42b8-3805-a332-7b772a795bf3 | -6.00391 | -40.9626 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 132.0 |
| 812ce4de-3116-3ab9-9fee-ca7533aeff4c | -6.01062 | -40.97945 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| e4474143-2dc1-3e45-bc9d-95b22a360439 | -5.09104 | -46.22336 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23487a4e-be1b-3e10-b9ca-8224e206eb4c | -5.96123 | -40.91715 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| babf73b8-7242-3e79-83a8-8a4c5279aeb8 | -4.50244 | -43.62236 | 2026-10-09 03:42:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c247ab1-044b-3d0e-aad5-2c1687698b9a | -3.03398 | -42.1138 | 2026-10-09 03:42:00 | NOAA-20 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c491e84-6fff-3851-824d-2cda1339dec3 | -6.57592 | -35.16368 | 2026-10-09 03:42:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 85b987cb-6b8e-31b5-a374-a885fa7a0175 | -5.99808 | -40.94092 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d73a1f7a-5757-3f6b-b2cd-ea980c7d5f72 | -5.7467 | -43.27512 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db9b31f1-b29f-3e95-9ef4-e909c32a521e | -6.00685 | -40.96066 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 36.3 |
| 06e49691-5eb6-3fdd-a610-a8165eda4916 | -6.00509 | -40.98346 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 059b4494-e532-35bb-ae00-72d58dad6604 | -5.95237 | -40.94081 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7155e133-040a-3de1-8174-c3669eb16147 | -5.74735 | -43.27144 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e28b94b-2cc1-352d-b6ba-5703c45b5e8d | -6.15452 | -47.28419 | 2026-10-09 03:42:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b3721642-f25d-3d46-81c1-c40bd7ae60d2 | -6.82345 | -39.31894 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3f3ca69-c3c9-34d2-afb6-8b8c04b3cccb | -5.87987 | -43.41712 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3be5c0b2-a64b-34e1-aa38-40f9dcfb4d91 | -6.00683 | -40.97351 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| e49219ab-de97-3e88-8dfa-a5ba9c09d11a | -5.99499 | -40.97388 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fb7fde4d-fbcd-3f41-aec3-d5c1e7f74cea | -6.88428 | -43.7024 | 2026-10-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9b605bf-60bf-362e-9789-b166e56fb1b0 | -7.1159 | -42.54499 | 2026-10-09 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2f1fcff1-dd25-3c5f-836a-4624e88d9caa | -4.02571 | -40.65122 | 2026-10-09 03:42:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a44239fc-ddc7-32c9-9da4-b21a7d650588 | -5.48768 | -44.30093 | 2026-10-09 03:42:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aa2cb42-98d7-396d-9941-27e07ac52cfb | -4.07653 | -44.11268 | 2026-10-09 03:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e35ed0b9-f580-3f6a-8170-3303993589e5 | -5.09209 | -46.21765 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93158269-4c12-311b-93e8-239d5df40601 | -5.08707 | -46.22637 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86e18035-802f-3a3b-8b3b-13e120354337 | -5.08909 | -46.21487 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f391ac2-e646-3c32-9f68-2ed214aa9496 | -5.36396 | -36.8499 | 2026-10-09 03:42:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dfe12134-56af-360c-b3ef-604142630b56 | -5.08806 | -46.22074 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59bbad0a-6be9-398c-81c8-035821f79a6a | -6.88428 | -43.70241 | 2026-10-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 136749df-3d01-3f10-b56f-3a078df277e8 | -5.98897 | -40.96525 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7d4d33b-c822-3dfc-b4da-5d2acaba40db | -3.20793 | -42.95873 | 2026-10-09 03:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0780e6eb-7447-3684-8c4a-57b94e6a1338 | -2.08478 | -46.57778 | 2026-10-09 03:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eda3d9bd-2f06-3510-b119-8438c878acf8 | -4.08688 | -44.12384 | 2026-10-09 03:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0932de4-201a-35e0-a13d-f7339d80bc48 | -6.01235 | -40.96955 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| bcbc7e79-0577-3d0d-9c11-40cae4251b78 | -5.88472 | -43.4219 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c1af1c2-dd0a-39a5-a045-02bfd4a968dc | -6.82097 | -39.55791 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3cdf48f-c12e-343a-a276-0055df539b9c | -3.21784 | -42.96843 | 2026-10-09 03:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfa982dd-3067-358e-a1ed-418bd0bbc9f8 | -5.43934 | -43.44853 | 2026-10-09 03:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ad2eed9a-9459-33e9-829b-79f8e55638fa | -5.99536 | -40.94291 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 02a5001b-034c-38ea-b1a5-6fb15a618a0e | -6.5745 | -35.10835 | 2026-10-09 03:42:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README61.md)

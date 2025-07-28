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
| e84b578b-4222-346a-a70f-d87d6a58aebc | -4.10652 | -47.92436 | 2025-07-28 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5601183f-44c4-3486-8399-c6f9a08eb922 | -13.11001 | -47.36629 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b04ca8a-7b5a-3cf7-8ff8-adffc487898e | -14.22356 | -43.95979 | 2025-07-28 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 932332c9-be6b-3950-9e0c-761d9b6ecf80 | -13.11142 | -47.37995 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aa9cc82-7042-3c5e-8302-317f65690fd7 | -6.02232 | -44.05822 | 2025-07-28 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07005068-5a4b-36cf-90f1-962f53457b05 | -6.23955 | -44.06636 | 2025-07-28 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23f0c861-019f-37f8-94a6-2b0227d892be | -12.665 | -47.03047 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a1f2201-f4ca-354d-87a2-2677d51088c4 | -4.30897 | -48.10153 | 2025-07-28 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b7a0fce-be89-38cc-96ac-98d3143e6474 | -17.35063 | -42.63946 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9e13900-dffb-3baf-8b40-dd498b5e5502 | -4.16683 | -46.8241 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 3cbd248e-1f48-3c0d-9e8a-79178e622b26 | -13.10375 | -47.30801 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21da8338-dc90-3631-8191-e8fab7c28b2a | -14.49641 | -48.64756 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 616a8605-80e4-3608-9cd3-c34fc79b5886 | -6.56554 | -41.5182 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bcb76098-8a6a-3f2e-b479-1c9e3b4c80b2 | -13.11777 | -47.3184 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d89545c7-1842-3ef9-b518-8d1be543a688 | -14.49525 | -48.65602 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64df85b3-2237-30dd-8c6c-a8a8e59c18f9 | -4.1566 | -46.81393 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cff595c8-ff3e-3e13-9a98-6bb2f33366c8 | -15.16141 | -43.95578 | 2025-07-28 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b265dd3-02cc-3a67-a107-0b3b7bae5f11 | -6.57012 | -41.5149 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5b607e78-ea36-3a4e-abd0-8d8976fb6713 | -4.1603 | -46.8101 | 2025-07-28 03:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 8764394c-c2d9-39a9-9866-d860188b90ce | -6.489 | -56.1941 | 2025-07-28 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 51e52f3c-4a8e-3cfa-936e-7b0978a97cec | -4.1601 | -46.8322 | 2025-07-28 03:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5aa11605-2777-3532-b01a-80f1e4013170 | -6.4889 | -56.2139 | 2025-07-28 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 34d121ac-8bfa-3526-81e5-687e5336c449 | -22.95123 | -47.19698 | 2025-07-28 03:51:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6393250d-41bc-39a8-ad80-56536273a606 | -19.96836 | -48.42763 | 2025-07-28 03:51:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3dcb7ed-87ce-3faf-bf3c-c9fb48173a90 | -19.27208 | -45.06613 | 2025-07-28 03:51:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cb814d2-6aed-39c7-b488-45fa4b83c760 | -18.24606 | -44.20927 | 2025-07-28 03:51:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2060ab6-eaeb-319a-870b-56a8f8966873 | -20.37741 | -42.15191 | 2025-07-28 03:51:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6304f96e-d094-3790-9ba8-1375c24067e5 | -21.85419 | -46.5466 | 2025-07-28 03:51:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a1d58c3-c1eb-39da-a732-54121368b079 | -23.61754 | -47.44904 | 2025-07-28 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 97d1e9a3-7278-3168-ac27-e3d5d75048ea | -20.70421 | -41.71229 | 2025-07-28 03:51:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7f7b976b-afbd-372c-a0d2-0fff48944b59 | -18.59402 | -46.55424 | 2025-07-28 03:51:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc5340a5-afa7-3fc5-9fc6-dff27204ab5a | -20.48076 | -42.3482 | 2025-07-28 03:51:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8ec8ed2f-e506-3402-8def-64dc4cf94518 | -19.3979 | -44.31807 | 2025-07-28 03:51:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0d4dbaa-afb2-3786-aeeb-c8c2d9bbb565 | -19.42523 | -40.72495 | 2025-07-28 03:51:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fc1fca58-86f8-3574-b0eb-063dc52f8330 | -22.75994 | -44.68473 | 2025-07-28 03:51:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7a7966de-acdc-3383-955b-7f5015227887 | -19.50746 | -48.47522 | 2025-07-28 03:51:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00e4d031-22fb-31ba-9423-498cc9ee4c5e | -22.54723 | -43.56633 | 2025-07-28 03:51:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 843ecc19-9cfa-34a2-8247-5b14e713c30f | -21.85835 | -46.54751 | 2025-07-28 03:51:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 425b44e0-feff-3670-b1a7-342a4f1fa7b5 | -21.67372 | -45.84203 | 2025-07-28 03:51:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20c3ad8f-97bc-3901-b363-cd26c0ba7ed3 | -18.25761 | -44.21149 | 2025-07-28 03:51:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac5377c2-545a-3687-b353-cb228228210e | -18.22333 | -43.57612 | 2025-07-28 03:51:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7707ff8a-1cad-34f8-a51d-f73beda7efa2 | -18.24515 | -44.21428 | 2025-07-28 03:51:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e75dff0-a4b5-33b0-945f-4b7f0abd64a0 | -23.49701 | -47.32843 | 2025-07-28 03:51:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f2513997-2b69-3ce7-be85-3e989da16c87 | -18.25376 | -44.21074 | 2025-07-28 03:51:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0feece6-4bb8-33e2-a5cf-1e90d9a0bb21 | -19.50629 | -48.48094 | 2025-07-28 03:51:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fc7b2a0-c10b-38b6-ae35-3ddf4da1038c | -23.61842 | -47.44461 | 2025-07-28 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 70c0840d-33bd-334d-8547-562064055fc3 | -19.96695 | -48.42326 | 2025-07-28 03:51:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fbab858-0a31-3bb5-95fe-221bc7b2033c | -19.96955 | -48.42173 | 2025-07-28 03:51:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d830a96-d4aa-34fc-9335-496a78c99214 | -22.9502 | -47.19487 | 2025-07-28 03:51:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 36d36f8c-7f01-3100-a474-2ecd890d32ab | -4.1603 | -46.8101 | 2025-07-28 04:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ae8e10cb-d6f9-3d6e-8393-7ac0d8926ad4 | -6.4889 | -56.2139 | 2025-07-28 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 5db769b7-787c-3dba-85b5-fca3b62f4bcc | -4.1601 | -46.8322 | 2025-07-28 04:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1a6c320e-6ef3-39ea-aad5-2e71ab94ac6c | -14.3166 | -54.1473 | 2025-07-28 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 622e2ac3-1d22-31ea-ae75-6a43c6a80292 | -4.1601 | -46.8322 | 2025-07-28 04:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 40aab0cd-b005-308c-9f1a-e917dc456cd2 | -4.1603 | -46.8101 | 2025-07-28 04:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 589ff6b1-c7c0-3f9c-b8e7-c2ab572f7f28 | -14.3166 | -54.1473 | 2025-07-28 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 443e2dab-4c67-36e7-9ea2-5f2f1b6eff4e | -6.4889 | -56.2139 | 2025-07-28 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| b6178e81-59ad-39a3-95df-28538b59f4ce | -6.5074 | -56.213 | 2025-07-28 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a931fc97-5434-3c57-9c42-9bc0e2cd05c4 | -4.1603 | -46.8101 | 2025-07-28 04:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 99b36b91-b0d0-3c5f-91ed-8a29b4f54dcb | -14.3166 | -54.1473 | 2025-07-28 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c5dac349-51a1-3374-abc8-9e9fcaa1ce4d | -6.4889 | -56.2139 | 2025-07-28 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 30693dc8-d967-340b-bc1d-fcf576ef9a04 | -4.1603 | -46.8101 | 2025-07-28 04:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b1dfa83b-b161-379d-8be2-c1b9a129425f | -4.1088 | -47.92479 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 395cabea-17a9-368f-a242-3f55f83933ae | -2.92158 | -48.23442 | 2025-07-28 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd267d50-01bb-3c6f-a206-32dec3eb2045 | -3.58527 | -49.42759 | 2025-07-28 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3bb79980-ebed-3b28-a316-7f2e1b49e345 | -3.50468 | -49.05197 | 2025-07-28 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb9c63cb-03ee-3644-9163-ee8b91befd4f | -4.11215 | -47.92533 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cdd127c9-2cc1-3e9b-8a57-f6b85f18c6c8 | -4.86049 | -50.76965 | 2025-07-28 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f8993b8-e89e-3d58-b863-18800e14c0a6 | -2.58394 | -51.92282 | 2025-07-28 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 252f8b21-93b8-3e18-910f-1fddf8034640 | -3.29894 | -49.1919 | 2025-07-28 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 05feb8bc-5278-38f6-a458-45b5c2849dd5 | -4.1121 | -48.12358 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 812b4adc-148c-3cdf-b099-ab81a9567543 | -4.30554 | -48.10343 | 2025-07-28 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f01f6afb-e688-3443-85d7-367d422f4fd0 | -4.22654 | -41.14563 | 2025-07-28 04:38:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7c6270b2-e683-3e1b-a46f-2f094d31793d | -4.16998 | -46.82308 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 156653fe-74ea-3fed-a287-3c2918d7530a | -5.00722 | -42.29662 | 2025-07-28 04:38:00 | NOAA-21 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a4d4f185-620b-3736-ac9a-1be3564e8112 | -4.30942 | -48.10043 | 2025-07-28 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 387958ce-9cfc-36e8-9b88-62bf67481b29 | -3.32906 | -48.71799 | 2025-07-28 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73505d9e-5e3b-33e9-8c21-be972db3a803 | -5.75128 | -43.98296 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc9c4ea4-de08-325f-bbe8-ec19b277cdef | -3.82884 | -54.12127 | 2025-07-28 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c70a2863-7d39-32ef-9fa4-ae43811798d5 | -4.1077 | -47.9319 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb6fca33-81d0-3869-9375-4d45fe42a12e | -4.04941 | -42.52757 | 2025-07-28 04:38:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 30402d8d-ed05-3b65-891c-8ef1d488a842 | -4.16362 | -46.81826 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 861cfd9a-5007-3d6a-876d-35ccb0837940 | -2.92062 | -48.67516 | 2025-07-28 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 066228c0-2b32-3714-a2c6-22c8f6ce447d | -3.2189 | -48.81342 | 2025-07-28 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b3e8363a-a3de-3432-a714-251e076534a3 | -4.86302 | -47.74846 | 2025-07-28 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32a5677e-a453-37e3-80ad-79a477079204 | -5.68448 | -43.66628 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b3d6ed2-dc28-3a73-8deb-e00e62b390eb | -3.88493 | -54.21564 | 2025-07-28 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57bca699-c573-3a42-978f-15bdffa51a65 | -3.48222 | -43.43432 | 2025-07-28 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2c10a6f-11f3-31e7-8ddf-14242a6f5eb8 | -5.86033 | -44.23804 | 2025-07-28 04:38:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf401d68-e74f-3e85-a0c7-4c9bed1a1e92 | -3.8025 | -47.50531 | 2025-07-28 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 57948484-0814-3153-8990-1ecadeba3973 | -4.15382 | -46.81279 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a6f4b72-62e8-3769-acf2-deeb3e83c6d0 | -5.74768 | -43.9785 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11647183-964d-33f1-a20e-78316e700256 | -5.7509 | -43.95608 | 2025-07-28 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c442d1d3-6c43-3f17-8189-c126d1029a9b | -3.88551 | -54.21202 | 2025-07-28 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e5c3b87-406e-31a7-b044-d18bd5b00b99 | -4.07432 | -47.94841 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 490c61bf-de05-3f56-9e1b-9006346ec2b1 | -4.15323 | -46.81664 | 2025-07-28 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5e2164b-4ed3-3021-b590-0e0a3d35a02a | -4.85712 | -50.76915 | 2025-07-28 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 807d7f9c-bbb8-3c4a-a77a-00d0cae78771 | -5.78826 | -43.60369 | 2025-07-28 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 844c86d7-3f40-3a3a-b43d-a1889ef2cd0a | -4.03527 | -48.06863 | 2025-07-28 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ae012b8-a22d-32b5-96ec-4c60aa95521d | -3.40285 | -47.49975 | 2025-07-28 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README9.md)

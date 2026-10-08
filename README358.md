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

## Dados Diários - Página 358

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38bef816-3995-3e8f-8d42-57ec3ac08ad3 | -3.7244 | -54.22584 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| dbc0eccc-9aa7-37d5-a3fe-6e280bdba21e | -3.58649 | -54.68592 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 9c7ec9c4-2e79-3b2e-b47e-44e0062234ce | -6.8633 | -52.18487 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa2f55c1-fe2a-36b3-95ed-84189ee907be | -6.84574 | -59.30357 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e4b12ada-f101-3554-93ec-54ca8f001ab4 | -6.33479 | -46.94344 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f9559716-1627-30c8-a30a-c564399ad4ba | -3.04544 | -57.49295 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c05dd309-b55f-394e-85ea-dcc780c893ee | -2.88913 | -59.19985 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| eaff6f13-74c9-3251-8434-c6f2ce63bf47 | -6.15162 | -47.93971 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0fb39815-de60-30c7-a54a-c38a742a0dc6 | -3.70681 | -46.01769 | 2026-10-08 16:39:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1473a0f3-5a8f-3b18-901b-3d5e1ab0c604 | -5.50244 | -42.85379 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 2a3fbdae-1b7f-356b-98d5-8249d00faf4e | -3.22152 | -54.29478 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 95114903-19dd-38df-8026-9070ddda2880 | -2.50267 | -56.0708 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6cb3fe0a-9b77-3164-a405-95e1b098d67b | -3.01548 | -43.34028 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b4a6719d-2262-3692-8bc7-fdd66a41f54b | -3.90176 | -58.94969 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 95de649b-ebe7-337d-8c0d-b27a242d022e | -3.44582 | -59.55693 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| d0ce899a-32eb-3036-9281-3776d2c5bff9 | -3.23044 | -53.38175 | 2026-10-08 16:39:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5a025a6b-fa13-398c-9e3a-e8e9505a2525 | -5.82205 | -53.83105 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 41e9e9b4-48c1-35c9-8fbe-520fec117465 | -6.16097 | -52.64868 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 5c5c8ef1-fce1-35f7-8c60-62ee82ae8bd8 | -1.20674 | -55.70218 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fc2bc298-d0e9-3ebe-b5bd-ab483723a7ac | -1.53393 | -54.82282 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 143dac63-fd6f-37ee-af8d-9b13cf8ef19b | -1.97708 | -56.06707 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5c6d624-1454-32ac-a730-c237d9ab6211 | -4.03556 | -42.59555 | 2026-10-08 16:39:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d7b1a8bc-8155-38ee-8e99-f7a69473733a | -2.49069 | -56.13914 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e3e87bac-1a24-3eff-b9de-b8c21ccf1825 | -3.37917 | -59.42958 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| eaed88bc-9fee-3289-96a7-f585d366bc2b | -3.93326 | -56.02581 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 78ba5502-e40d-35a2-8bce-3c6ba5b60167 | -5.48237 | -45.68892 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f8b19a9-74d6-3288-a1aa-14aa974f3f80 | -2.49811 | -58.07438 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 95a98e1f-f7c6-30eb-a204-e3401cc83005 | -1.38473 | -55.19606 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7bbe698e-4b0e-3181-a0f4-3e3da92c4496 | -3.80163 | -44.60981 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de42c8af-5a74-330f-b2ae-f95d9de1f65a | -4.51085 | -43.79539 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8be8db90-0d63-397f-92f6-4d6847e61260 | -5.96036 | -46.3745 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 241f68fe-5b1e-3261-99f2-13f14d78714f | -0.30992 | -49.44776 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8d2be35d-a9f6-3660-8a20-5e39e49860b6 | -6.20397 | -52.85759 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 25e558ff-72cb-3c98-b576-d013ac527fcf | -3.15441 | -57.6783 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 54eef9b0-dd76-333e-86a1-a3f6ffbb65ae | -1.53066 | -54.83437 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 8d9d1048-51bf-31e6-932d-eaa1b061dda4 | -3.25655 | -43.87679 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f1567601-d4c6-3ee7-8353-c746cf922f9b | -5.968 | -53.54906 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a22cd739-a7f5-36cb-ac9d-f83952d34576 | -1.15407 | -54.22146 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 5fd59ae5-80ec-344a-93cd-c89751c7091e | -6.16548 | -52.6481 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ddd8ebff-d0c1-3d4e-b2ff-6fc1b28a9466 | -3.80076 | -41.64874 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 63ad295c-46aa-3972-9da5-af75c3dc1f81 | -2.07963 | -46.58614 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 19444935-a0d7-34a0-9e2a-aefbae80be56 | -1.62513 | -55.1273 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6893fb62-ee7e-3157-a857-d7bca0bbaded | -3.0135 | -54.04253 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 83047666-62be-3dd3-af37-ff0ef87dd9fa | -3.09997 | -53.96181 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 119185a0-bec0-3e97-844e-a2582e023690 | -2.61341 | -56.47369 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0f3969c8-218f-3739-9801-4dba98090591 | -2.9083 | -54.02478 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 43fb6c4c-ceee-312a-a4a7-18d026c0e69e | -7.10649 | -55.72663 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b067768b-70e2-3f78-8188-c843ab5f012c | -3.29563 | -53.69361 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b6e464a1-a2be-3fe5-b7e8-ccbf9729a3d7 | -3.84802 | -58.89436 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b95478cc-4c7b-3f93-a42b-11f0f7f03558 | -3.79605 | -41.6706 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| af60a594-53cf-3bb5-8a3a-91aec0d73db0 | -5.41061 | -45.9065 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ce8a935-9639-3c43-ac5d-075087f6fd43 | -5.26852 | -55.95707 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b63232c9-b650-3421-afad-8f989274f4db | -2.07805 | -46.57581 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 5e992b6a-1285-3754-ba98-48729e1e29fe | -2.99929 | -54.76693 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 77d4942e-1aa0-3ce9-befd-da0e24004a76 | -4.0047 | -43.22853 | 2026-10-08 16:39:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 84012fc1-9bec-3d47-8d0f-b7c40897a46f | -5.216 | -45.17041 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6b412bab-71ae-324b-8884-ddcd2d866a45 | -5.32386 | -48.98689 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| be60c536-d96c-383b-bf17-17f0f8cd4cf7 | -4.19819 | -38.74015 | 2026-10-08 16:39:00 | NOAA-20 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| cccabd31-7b97-3f4b-899e-c7a2abb7cbb5 | -5.08219 | -46.22354 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de8e111b-ccd2-36ea-998f-6c901cca5bb0 | -1.82996 | -56.16782 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f62ba8f-9f07-313a-ad42-f772fd2e058d | -3.198 | -43.4079 | 2026-10-08 16:39:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dbbe0e8c-86e4-3b8d-b60d-539e6acf1e29 | -1.80804 | -57.11552 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dbacad36-6a06-367a-b3cc-fedf89e392e5 | -5.28897 | -47.6736 | 2026-10-08 16:39:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6144ef6d-46b7-3acf-88d7-2543042f7c11 | -2.8207 | -54.09705 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7ad06972-b240-3d2e-80d4-7a0c53f0cdc3 | -5.43276 | -47.93066 | 2026-10-08 16:39:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f147583-677d-3bbf-b7c1-dcf300e7d47c | -5.97075 | -55.34907 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9542a962-547f-3f68-aff7-f9722bbafbcc | -3.17093 | -50.59585 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 72acee8f-8e57-3d36-b7fd-193b2c50470a | -3.0328 | -54.07573 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9260519e-ab53-39fe-b53d-9d4d14ea7eed | -2.30842 | -57.08161 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d2fb72dd-0367-3644-a1d3-6fa644de42e1 | -7.23406 | -55.12667 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 8a8ab8ab-3a07-3da4-8204-cbaff1451c53 | -3.50262 | -44.26727 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 444068ad-d450-30d7-a6c7-29ac6b2da011 | -6.82006 | -59.1126 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a3b5e537-0583-3a93-8e9a-fef0b33c149d | -5.53096 | -45.21019 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e31c0f46-19ed-3b32-928a-ee2274bcd958 | -5.96725 | -55.36333 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1c039341-a2dc-3fc7-8946-30ba1f2f99d8 | -5.37726 | -45.86563 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3166ca75-9ee2-3180-9c80-db9cd156f03a | -4.96942 | -37.96779 | 2026-10-08 16:39:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 663a3031-0654-3b79-8da9-9abda1cfc37a | -3.56719 | -59.47134 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f9a32b84-f847-39a9-8159-94e61b83c09b | -3.09683 | -59.20002 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 02ba50ab-e92c-3df1-b525-4b489aac0b3a | -2.99929 | -53.89526 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cbbd8717-9e5f-303b-af9a-c39f296b1242 | -6.50443 | -55.38213 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| b2acd17b-40c4-37f2-a32f-ba7b2505ba27 | -2.84956 | -54.12895 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 0f3fa66c-a5a0-34d4-a66f-6d5365ebe72e | -3.09987 | -53.9432 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 521f304c-4eb8-35b2-ad48-eef135e03b51 | -3.25238 | -43.87333 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 547f64f8-17b9-34b6-a97e-c470acd73b12 | -5.69959 | -53.48387 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5022764d-4298-3fa2-860e-2a8e4c3b4258 | 0.67804 | -50.79353 | 2026-10-08 16:39:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4a6b4017-de0c-39cf-9c41-deb8b91e99fd | -5.92634 | -51.83583 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 07f6a5f1-9181-30b1-a12a-b14eddf8c47e | -6.14685 | -52.64617 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2c634327-a170-324c-bbcf-9a3b4575b245 | -5.78071 | -50.1009 | 2026-10-08 16:39:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 6012d157-90b9-3509-8182-83749820ee3e | -3.08259 | -53.95594 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4ff7efc2-6606-3140-8b40-57bfe03bd9ad | -4.6299 | -43.517 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 15f7a6f3-1b91-32ed-af0c-4a618db5351c | -2.58024 | -57.78751 | 2026-10-08 16:39:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 63411a21-b133-3c51-b3c8-abca4e0729cf | -4.38374 | -43.95823 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 781d059e-7e4f-328e-a1e5-5e369fca6644 | -3.78807 | -41.67184 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| a6e8ef75-f79e-3d26-b838-3ff900618ece | -2.83934 | -54.12527 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c2f68c35-a549-3884-a899-b528830fed7e | -5.95225 | -45.69922 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 307a2f5e-4814-314c-9229-c328c34222ed | -1.52985 | -54.82889 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 20abe7cb-d432-3ecc-a8d3-092820f588d6 | -3.06082 | -53.93874 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 45ffda0d-508d-3246-85aa-370eeb3004ec | -5.4862 | -44.60831 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 6aa342a1-d8b8-36df-9c59-5a5e8f86c0e0 | -5.89179 | -44.1724 | 2026-10-08 16:39:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fd739475-5d4f-35c3-817f-110515415528 | -7.20205 | -55.135 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README359.md)

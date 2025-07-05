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
| 1e1603e4-7759-3e13-b581-b3f12260d5fb | -8.38374 | -44.05218 | 2025-07-05 03:55:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5654039-6e60-3abe-bcf3-1a62068e1bf0 | -5.61006 | -45.17959 | 2025-07-05 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86320353-506c-3657-8986-dbda3652830e | -7.30366 | -45.36676 | 2025-07-05 03:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 435353b0-6645-3c09-93a8-78cde1ab7847 | -7.29459 | -45.36509 | 2025-07-05 03:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8af47490-a1e1-328c-bc98-4c1c1883487d | -5.72237 | -49.10675 | 2025-07-05 03:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff8a4855-e09f-3fff-b6cf-6252d433cd7f | -2.91951 | -40.41652 | 2025-07-05 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 010d36c5-9190-30a2-9de2-f4418d4a6900 | -5.99662 | -43.74263 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c61e54ef-ff14-3b22-8bbe-ff98963aa164 | -5.78519 | -43.61095 | 2025-07-05 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7eea0a94-2ebd-3332-a17e-bc49b56908d2 | -6.67503 | -43.87673 | 2025-07-05 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da383b7c-0e42-35c6-a03d-e67340e65d56 | -4.8181 | -44.35538 | 2025-07-05 03:55:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cead4a0-ad67-350c-af48-063c3b9063ad | -6.28658 | -44.23093 | 2025-07-05 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f27fd56-1050-308d-aa66-3073b804418c | -4.11236 | -47.93618 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a5583df-745e-394c-8165-dc822a448060 | -6.29084 | -44.23177 | 2025-07-05 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ecf595c-c23d-3933-92a2-510c51c20b44 | -7.18867 | -45.32501 | 2025-07-05 03:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd881664-9002-3da7-af8b-99defe7c7e7a | -7.28659 | -45.702 | 2025-07-05 03:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eac00b7-4aa6-3a41-be3f-674d4db6ad32 | -7.44991 | -43.08038 | 2025-07-05 03:55:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f92f52b-c398-3330-ba35-870abf3767c3 | -5.0493 | -43.85584 | 2025-07-05 03:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb263ea3-307f-3269-b525-cbbfaeda853d | -7.30126 | -44.69483 | 2025-07-05 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0df363ad-85fe-3e14-90d5-8e131a556a9e | -3.52851 | -48.42947 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1dd39de-b46c-3dfc-812f-3bc85e35c5d9 | -5.99306 | -43.73821 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3c9ce911-3497-365e-8f8a-7509763b2846 | -4.82183 | -44.35401 | 2025-07-05 03:55:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e16693d-db22-321f-89a6-21a1948dc7d2 | -6.77297 | -45.53756 | 2025-07-05 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5568237-e7fb-3fed-ae83-3229e4bad156 | -3.52178 | -48.43305 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56453cfb-4910-3755-8e59-bf91a4c622b0 | -3.4824 | -48.44851 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1998f6c6-ed5e-3deb-b9b9-a8596459bdc4 | -5.07139 | -37.71531 | 2025-07-05 03:55:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 00751212-5fbd-3e24-acb7-f16911646e72 | -5.04864 | -43.85979 | 2025-07-05 03:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7757975-ae4d-35c9-b8df-a2d6001381ab | -7.15741 | -44.32101 | 2025-07-05 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9625dee-07fa-3de3-b063-9c3cc44b3513 | -6.80172 | -44.75051 | 2025-07-05 03:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54f6d50a-817c-3665-8588-a97fa335c880 | -3.48315 | -48.44419 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38f84ff6-e65e-3dd0-8707-f7c919dd5cd4 | -3.81085 | -42.54411 | 2025-07-05 03:55:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e55f651a-d41a-3fc2-9c9d-c3cfb5102af3 | -3.48517 | -48.45078 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 813253d6-5df9-3104-a53c-a65e88344e74 | -6.76616 | -44.87104 | 2025-07-05 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e2fdf9e-842e-3812-ba2e-2cbb538fe425 | -3.61108 | -41.15485 | 2025-07-05 03:55:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 06dc287b-ba45-3ebb-b8a4-67aaab5d11a5 | -7.23171 | -43.09068 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f0fa7939-97bd-3d6d-ab05-13708eae485b | -7.29691 | -44.69412 | 2025-07-05 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a80990da-03a9-3c5c-b46e-71e282cde37e | -7.22081 | -43.08373 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ade4db80-06ce-3337-b1cd-31b4c4d724b6 | -7.34725 | -49.63244 | 2025-07-05 03:55:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 430bf7b3-1346-37a6-af6f-2a7b2645fc93 | -6.60695 | -43.89268 | 2025-07-05 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb2e5871-5425-3b13-a3d1-da9f55451d88 | -7.29913 | -45.36591 | 2025-07-05 03:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ca06009-15be-360b-a8ce-5c2e66b1650c | -3.61051 | -41.15295 | 2025-07-05 03:55:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84af41f4-e979-311d-ba79-8d9372d4364c | -4.00719 | -43.23526 | 2025-07-05 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfe32294-c22d-3c85-8aea-879bcdd9eb85 | -5.99723 | -43.73888 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de924e67-34d9-325e-b4f2-3d58f8452e5b | -7.09357 | -43.51323 | 2025-07-05 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ff318cd-ccda-3c9e-8921-1b3ab4972e29 | -8.0739 | -34.97455 | 2025-07-05 03:55:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d3a04a5c-3142-34f7-abaf-a672a68fd7e3 | -8.38311 | -44.05584 | 2025-07-05 03:55:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9338a7ec-faf5-3e47-b8d3-50fec4558cde | -6.80101 | -44.75478 | 2025-07-05 03:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a7698af-ac8d-3da1-ab39-1413c7445181 | -3.52103 | -48.43742 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82bf23b6-19f8-3a3a-abfc-f2376fa5eaaf | -4.10663 | -47.93538 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbcb7762-e248-3b9f-bdbf-cd4403c1cd92 | -3.99889 | -43.23389 | 2025-07-05 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8da3d807-003d-31ac-93a1-a36526294700 | -5.99797 | -43.74219 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fbb2139-0cfa-34c8-acc8-6f2b4bc538b1 | -6.64417 | -43.1728 | 2025-07-05 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90db9fb4-84e2-36c9-8d2a-616906e2299f | -7.29992 | -45.3613 | 2025-07-05 03:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 013d8f60-67fd-3c7c-9431-aec56f03daf7 | -7.11627 | -43.89983 | 2025-07-05 03:55:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 635bf834-d6ab-3dcd-a404-5af7d3b0cf14 | -6.77759 | -45.53844 | 2025-07-05 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f194b91-e044-3e66-8815-10e396074d24 | -5.99509 | -43.73403 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d60bde5c-ab52-3967-ae1b-06d57bc28f02 | -2.92308 | -40.41708 | 2025-07-05 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76815a52-2280-3663-8ef8-749f151e9855 | -8.38611 | -38.1068 | 2025-07-05 03:55:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ed252271-9db3-3dfb-9ca8-211b200fb9fe | -3.99829 | -43.2376 | 2025-07-05 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 768b6f22-ad80-3218-930f-18398f4a662c | -5.06606 | -43.72955 | 2025-07-05 03:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8e164f86-0d14-3685-ab88-dc80be341374 | -6.67566 | -43.87295 | 2025-07-05 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 857247ed-086b-3490-9a71-c2e0beab0135 | -4.11166 | -47.94017 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91a0ede0-e0b4-370a-b554-74785f7f7972 | -6.01546 | -44.52966 | 2025-07-05 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c8fe94f-a683-304a-b88b-4e32ca9f77c6 | -4.76904 | -45.3484 | 2025-07-05 03:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fb81f57-5640-30c8-88c0-af4a0ca6b57d | -5.00075 | -38.01261 | 2025-07-05 03:55:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8607b3c3-0c58-3963-a1b0-6c0f536c38ef | -7.70252 | -47.28407 | 2025-07-05 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01e44200-c881-3a4b-9389-d478397abcda | -4.68249 | -43.26018 | 2025-07-05 03:55:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 208c5e18-44bd-33e9-af2d-641d4dfd40e8 | -6.0162 | -44.52533 | 2025-07-05 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32fe37b0-12b0-3b9c-be7b-536c710ab367 | -7.45075 | -43.07544 | 2025-07-05 03:55:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ee5f102-dcf9-3cc6-a603-e215c6e2d542 | -5.72477 | -49.10521 | 2025-07-05 03:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d84d0e38-7a6f-3117-aa8a-efcd3c23bcf8 | -5.99861 | -43.73846 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a67727f-faec-3c16-b73e-2f33b11da262 | -7.24429 | -43.0877 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c60539bd-46ed-3f35-87a1-bac962e8a0c9 | -6.80052 | -44.75257 | 2025-07-05 03:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02566b0e-c298-3c8c-97f5-b06c5871ef87 | -7.24512 | -43.08272 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 51fd9795-88ec-37e5-93ee-b4673013e0c1 | -8.37902 | -44.05513 | 2025-07-05 03:55:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e89b922-0c33-39df-b95a-f3bbdf26bb93 | -7.22389 | -43.08933 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 65ac9a9d-7219-3c51-906c-79c1d2f0d72e | -5.60545 | -45.17876 | 2025-07-05 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9da7704c-9484-3c63-9da3-58a256874a4d | -5.99784 | -43.73514 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 113c3759-29d9-3c61-b6c8-1cb9f0a2c3a3 | -5.99444 | -43.73779 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 973873fd-fb4f-3ae3-bfff-ae862136b0d6 | -3.52701 | -48.43824 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da37ea70-ebf1-3723-b059-3e6cd1a1bebb | -7.15811 | -44.31688 | 2025-07-05 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8ca8e40-e2fc-3a70-825c-d59c170e5986 | -5.72836 | -49.10776 | 2025-07-05 03:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46316305-06eb-37b2-96c5-0f12c377b186 | -7.24821 | -43.08835 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 135d8c9f-054e-3bb2-bcbc-3bbe2f4e03f4 | -3.4859 | -48.44637 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3056cd0f-8406-3ccf-a373-78e17bd37705 | -7.34641 | -49.63694 | 2025-07-05 03:55:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ff5ed06-3971-380c-8be5-ef8bb099d3dd | -7.29127 | -45.70268 | 2025-07-05 03:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a5c3355-ef75-3424-9d4e-36af31aa6afe | -6.77552 | -45.53997 | 2025-07-05 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f9dc1cf4-5c3b-3776-88cf-d77d02047f29 | -6.28032 | -43.67872 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ee596c1-575b-34c7-bda1-874df4afeb32 | -5.996 | -43.74638 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e87e09b-b4d8-35ea-98f6-fbbee7df1ef5 | -7.70198 | -47.28708 | 2025-07-05 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2211ec0e-95b9-3bbf-9083-653ca28ab03c | -7.25212 | -43.08899 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b6479680-2b18-3049-8fde-21f8b11e41cc | -5.72399 | -49.10952 | 2025-07-05 03:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f114770e-0579-37fe-8fbf-7cfc9874eeeb | -4.11081 | -47.93785 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcc1a2e5-d35c-3394-b66d-3670f121a5d9 | -5.99368 | -43.73445 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3afa2deb-000c-3375-8ce4-0fe34a72895e | -7.19321 | -45.32582 | 2025-07-05 03:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d745a312-f899-33df-a387-e1e760239988 | -4.1051 | -47.93697 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 087743ed-1666-3c5f-8f87-aaf94327e99e | -5.61087 | -45.17482 | 2025-07-05 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 104bdda1-ff78-32f7-a9d7-e466d8ad5dbf | -7.22472 | -43.0844 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f4b57252-ba30-36a9-8a2c-5e35e1a918a7 | -7.34586 | -49.63186 | 2025-07-05 03:55:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b88993b3-f4cb-3691-8d16-bdbe77069ed9 | -5.99733 | -43.74593 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 406143fa-636b-3e72-bee4-4ce40164cfaf | -5.10892 | -43.15091 | 2025-07-05 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README5.md)

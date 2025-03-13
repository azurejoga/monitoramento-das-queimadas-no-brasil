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
| 87a50508-8f41-3853-a464-7343e611f911 | -6.4845 | -35.1164 | 2025-03-13 00:10:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 96.2 |
| d8b964fc-2136-3a99-b735-abf8c778f1e9 | -6.4842 | -35.1438 | 2025-03-13 00:10:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 98.1 |
| 3afc37ed-ce0f-337a-801b-d68607b0dc98 | -6.5036 | -35.1141 | 2025-03-13 00:10:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 2d48a94a-0d9d-3e56-88ee-2e0c013fd08f | -6.9586 | -43.0465 | 2025-03-13 00:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 69d724cb-542e-3ba9-a7a1-c15ff6f94f7e | -11.59987 | -44.84082 | 2025-03-13 00:56:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| cbed9875-6c6e-3d40-80f6-cea83bc9ea2f | -11.44207 | -52.91821 | 2025-03-13 00:56:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ad2b675-4174-3126-a696-78c52783b27e | -11.56755 | -47.61659 | 2025-03-13 00:56:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b9667b2b-ffe1-39e2-a90a-e7534e394286 | -11.59211 | -44.83 | 2025-03-13 00:56:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7581e9fa-16e2-3e9f-b843-cff01635cdf4 | -15.59675 | -42.39371 | 2025-03-13 00:56:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 4945306b-6cf1-38ce-b9f1-eb73ab8a076a | -11.56919 | -47.62772 | 2025-03-13 00:56:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 432955a6-2cb6-3b32-860a-2531f83531b6 | -15.58333 | -42.39614 | 2025-03-13 00:56:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ff81dadc-fe14-39a9-8ba3-c37b24a40d9e | -11.44342 | -52.92854 | 2025-03-13 00:56:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 01d5a69b-3cc3-378b-99b9-3c8792f94785 | -6.9586 | -43.0465 | 2025-03-13 01:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 21f1b5d3-2912-3a97-b5e5-eb66ff4c93b2 | -6.9586 | -43.0465 | 2025-03-13 01:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 0c9cade1-98ec-3d1c-989e-1d3cab045f22 | -7.4741 | -35.19153 | 2025-03-13 02:51:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| a972ff1f-46ac-3282-add5-2367e286705c | -7.47304 | -35.19718 | 2025-03-13 02:51:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| ee98c6bf-d606-302e-b116-6a117bbb9ddb | -7.47251 | -35.19114 | 2025-03-13 03:13:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aa2ff77a-33b8-3a92-9714-bf2d11d871d4 | -6.91784 | -35.15816 | 2025-03-13 03:13:00 | NOAA-20 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| be54bf2b-c715-31d8-b966-e3f21c5e7f80 | -7.56179 | -35.05825 | 2025-03-13 03:13:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 894cd55f-a12b-3954-99bd-b021324bd204 | -6.91746 | -35.15588 | 2025-03-13 03:13:00 | NOAA-20 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e6d11caf-7f24-3a7b-9fe9-bc9f5b2b64c1 | -8.71183 | -38.64268 | 2025-03-13 03:15:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f7824ed7-fdc9-3df3-a285-127362d3ac34 | -8.71246 | -38.63927 | 2025-03-13 03:15:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 986f78a9-0452-3ccf-9f97-9e425d9c20d1 | -8.72509 | -38.81345 | 2025-03-13 03:15:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb6bdc3b-1799-3d7e-9ebc-ac50f833e2f0 | -9.80243 | -37.95136 | 2025-03-13 03:15:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 619c3438-33dc-3444-8070-4fd4cc70cb68 | -11.43454 | -37.65682 | 2025-03-13 03:15:00 | NOAA-20 | UMBAÚBA | SERGIPE | Brasil | 2807600 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 774a8e9d-c9c8-3b16-b737-e8d1193afc6f | -10.83666 | -38.10651 | 2025-03-13 03:15:00 | NOAA-20 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 10a46183-33c7-361c-b5ec-e830e199a145 | -10.34398 | -38.47571 | 2025-03-13 03:15:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85cd020b-b6a4-3bb8-a2fd-64a24bc04736 | -10.303 | -38.75008 | 2025-03-13 03:15:00 | NOAA-20 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 86310f9c-e941-3ab4-ab2e-485ea3d95ef2 | -10.34459 | -38.47249 | 2025-03-13 03:15:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 255b7c16-7df7-32a0-a7e3-7bfa47f43aba | -15.59287 | -42.40211 | 2025-03-13 03:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ededa234-b0f0-3fa8-a6d3-2e34b388478c | -16.61051 | -43.33244 | 2025-03-13 03:17:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 844a6d71-42e9-361e-ad47-361feda1b811 | -15.68028 | -41.58316 | 2025-03-13 03:17:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8cd15bdd-6150-35d1-9bb0-f25dce3580ef | -19.92213 | -41.52143 | 2025-03-13 03:17:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c0d2336e-1496-36a0-8172-81b06c0064c2 | -15.59385 | -42.39743 | 2025-03-13 03:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd7335cb-3338-3dd8-8b79-4b007c2794c1 | -15.67877 | -41.58319 | 2025-03-13 03:17:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c0ecb33f-1442-3227-86f5-f336323e7cab | -15.58592 | -42.40533 | 2025-03-13 03:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 362d3ea6-b925-3f46-89af-20e83b314d42 | -16.61439 | -43.33372 | 2025-03-13 03:17:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12444b8e-433c-3ef2-b02c-a0f368d73be2 | -19.92287 | -41.52165 | 2025-03-13 03:17:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c71b1a92-95c2-31ca-af4d-956bd473cfbe | -6.22534 | -48.05656 | 2025-03-13 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74bd051f-171a-39c0-adf6-af838a10ae64 | -6.92352 | -35.13841 | 2025-03-13 04:08:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ff2e30ce-0c6e-3671-8a9e-fee5f43adcd4 | -6.95781 | -43.04391 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e318bc4-155c-34b8-83cd-95c6c45b352d | -6.9606 | -43.04802 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c700689a-14ff-36f7-ac05-ce3ab6d39d8c | -11.77825 | -44.71859 | 2025-03-13 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 621820cd-3ef8-3179-8e0f-b49cd64d5c0d | -8.11232 | -43.14399 | 2025-03-13 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7cf1631b-a18a-36a1-adfa-c1e2b0c6f612 | -6.96174 | -43.04085 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1e295c0-6fa6-37cc-9fd6-93f7d60e85f6 | -10.65269 | -44.40271 | 2025-03-13 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 362bd264-c8c4-3bcf-9c46-a62a33af1a42 | -10.87389 | -49.54923 | 2025-03-13 04:08:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1af8a40-a852-310c-86e5-79282c654452 | -6.9262 | -35.14187 | 2025-03-13 04:08:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 1ace4b73-137f-3438-8e8b-b571101566fc | -8.72644 | -38.81549 | 2025-03-13 04:08:00 | NOAA-21 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e351b988-5db6-3db7-9e5a-1c1651d06947 | -7.08352 | -44.81818 | 2025-03-13 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea5ff2c6-b82a-33fe-a865-71111765c81f | -11.5939 | -44.83607 | 2025-03-13 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a524e447-01db-36db-8213-dbffe2bf7659 | -10.66753 | -44.3975 | 2025-03-13 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c9fe9cf-4c8c-3d8a-af34-89bf4a34e537 | -5.44626 | -45.42802 | 2025-03-13 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f54d0b49-1f2d-3568-a817-d74787589bc3 | -6.95724 | -43.0475 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1f2fea23-e048-39b4-96d8-cbe013ff937f | -6.92733 | -35.14341 | 2025-03-13 04:08:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 149d1f82-f92d-3788-b6ec-5cfa45846257 | -10.39312 | -47.99748 | 2025-03-13 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa2f9ab1-f705-3267-a64c-a43c0fbe5440 | -11.49158 | -37.99722 | 2025-03-13 04:08:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07c41848-ca2f-3e90-80b2-b9c190f9d964 | -10.34775 | -38.47224 | 2025-03-13 04:08:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4660492b-e376-3c28-bf56-7cad6aa8d236 | -10.6533 | -44.39898 | 2025-03-13 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e43a88d4-2b4d-3d87-be74-3baacec444d2 | -10.66072 | -44.39637 | 2025-03-13 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0c26ad3-3645-3b3b-a6bb-43ad1c3c9f28 | -8.71502 | -38.63924 | 2025-03-13 04:08:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| ae024db9-6a21-3a2a-a06f-ed759ec00d89 | -6.92559 | -35.14629 | 2025-03-13 04:08:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| a3de56fa-9257-3fb1-898c-c6b2e1788953 | -6.92288 | -35.14281 | 2025-03-13 04:08:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 603e406b-29fb-36d9-9587-2573b354db67 | -6.07146 | -44.23878 | 2025-03-13 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 727fcdfc-192a-3037-85bc-42649dea8a5b | -10.84115 | -38.64529 | 2025-03-13 04:08:00 | NOAA-21 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52a3d60c-87c3-3b13-926b-f982fda4c346 | -6.96117 | -43.04443 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2a61a49-e1c8-30db-bcf7-32c6e88d3a1a | -6.22613 | -48.05203 | 2025-03-13 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2938e310-bb44-3593-82fe-281e5d3ec681 | -11.95911 | -40.60672 | 2025-03-13 04:08:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 570b6905-3556-3136-aaa9-3a30f1f89460 | -11.56334 | -47.62496 | 2025-03-13 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 763e73eb-fdf6-37a3-b0bd-6b1f37f8c35e | -7.0815 | -44.81839 | 2025-03-13 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2d79c55-b275-3ac4-840d-c0a82acfe669 | -10.39379 | -47.99361 | 2025-03-13 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f5463f2-c936-3085-a8f0-40d288dd33dd | -6.96232 | -43.03727 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5bcb9793-ddd3-3b8a-818a-e196970cc262 | -11.89054 | -45.28125 | 2025-03-13 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc0439a1-ba71-3e1f-a4c1-7d285dc4b62c | -6.93065 | -35.1425 | 2025-03-13 04:08:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 41c11162-642a-31a2-b393-898f6100b306 | -11.56821 | -47.62039 | 2025-03-13 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e8f6265-8317-3eb1-8126-e0313f16f4f9 | -11.89119 | -45.27731 | 2025-03-13 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71dcdf04-6c4f-32d4-8933-9a68dda25299 | -7.24431 | -44.77074 | 2025-03-13 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1c7d32b-4401-35e9-a286-8c5fda1b1fdc | -9.80372 | -37.95029 | 2025-03-13 04:08:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 527297ff-4f63-3d1a-8556-cedfdc6a5927 | -12.04843 | -40.47303 | 2025-03-13 04:08:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45359043-1f52-34fa-ae2d-02303b62c3d1 | -10.39448 | -47.98969 | 2025-03-13 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4b63aa5-3195-3565-b9ff-f8ec718438c8 | -8.11566 | -43.14452 | 2025-03-13 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2189dc4e-085a-3404-8d53-e24019752fbd | -7.24364 | -44.77483 | 2025-03-13 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56c2d314-bcab-3f8b-ab1f-e4cdf7f55e6b | -11.56425 | -47.61972 | 2025-03-13 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cf72112-8fe6-3659-8ddf-27a19e4cc456 | -6.96568 | -43.03779 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0e3e882-9188-3676-aa3f-4b10f53e2fd3 | -7.00085 | -45.61441 | 2025-03-13 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78ac40af-88f3-34ca-bdaf-86a66c2d34bf | -7.24231 | -44.783 | 2025-03-13 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37248356-f9c4-3e65-865d-0e9b50520d0f | -11.59452 | -44.83227 | 2025-03-13 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd1c8845-85b3-3eaf-9433-55f87a8e6f22 | -12.1086 | -41.32059 | 2025-03-13 04:08:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8cdafcc0-3411-3736-a69b-7de11db19249 | -11.49101 | -37.99851 | 2025-03-13 04:08:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85333119-2ae9-3d04-8b81-340cc033f19e | -10.3479 | -38.47512 | 2025-03-13 04:08:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d249f386-329c-311c-b883-1c696181e11b | -8.71439 | -38.64355 | 2025-03-13 04:08:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 99bca70d-b76c-380d-a817-067d670927d6 | -8.71831 | -40.52684 | 2025-03-13 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 671b3aa9-db07-3637-b801-eaf410f70de9 | -11.94446 | -43.93247 | 2025-03-13 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d2cf80c-36b1-3386-87de-3b6b2dd4389c | -10.66413 | -44.39693 | 2025-03-13 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa285659-fd14-34ce-8297-bd76ef62a65c | -11.59796 | -44.83284 | 2025-03-13 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af0bedfd-48b2-38f8-9f89-38827d486e35 | -10.6567 | -44.39954 | 2025-03-13 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d6e0c09-058f-340d-9a78-09528fc2eca0 | -6.92174 | -35.14127 | 2025-03-13 04:08:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 840e5f05-1816-35a0-8467-cb2fa0a3076d | -6.99709 | -45.61382 | 2025-03-13 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7805aa65-1a53-3b47-bf8f-44d621b1cf93 | -11.59733 | -44.83664 | 2025-03-13 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19a8957a-d8d1-39da-8eff-182ac865cff7 | -6.95387 | -43.04697 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README2.md)

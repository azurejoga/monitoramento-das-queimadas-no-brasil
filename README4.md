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
| 9c5ce554-6527-30c5-9482-3b7f046767f5 | -6.6115 | -43.8709 | 2025-07-04 02:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| bbdfafd3-6fd9-3fbf-92d4-07928c96807e | -10.5586 | -49.1337 | 2025-07-04 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 59bae2fc-1d33-3fff-a86e-c17b607eff8b | -6.6112 | -43.8941 | 2025-07-04 02:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9e10a79c-d022-35d2-baee-366af3551b01 | -6.6112 | -43.8941 | 2025-07-04 03:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| c77c9a8f-b446-3049-88bf-94cacb2dc978 | -11.932 | -45.389 | 2025-07-04 03:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 474898d9-e9e1-3a92-a8d4-05e8c4bf4050 | -7.2217 | -43.0917 | 2025-07-04 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| f343e1ee-4f73-3831-a9a2-073e0f08c32d | -10.5586 | -49.1337 | 2025-07-04 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d79c8500-1879-32c0-9975-36499bdb6358 | -6.6112 | -43.8941 | 2025-07-04 03:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9ab9098f-4668-383f-a39f-7929b9b00a85 | -7.2217 | -43.0917 | 2025-07-04 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 51.8 |
| ee89e72c-899f-3bcc-8c90-2610afdea608 | -10.5586 | -49.1337 | 2025-07-04 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 66dbfe47-66a2-39e3-8eb7-04a0f05afda3 | -6.6112 | -43.8941 | 2025-07-04 03:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c7e92a94-65e1-3537-a61f-170075d86227 | -10.5586 | -49.1337 | 2025-07-04 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 06c11927-30d2-3cfe-84d5-8b4e66e88076 | -6.6112 | -43.8941 | 2025-07-04 03:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d3b40887-8571-33f3-bb7c-2d3add6cf6de | -7.2217 | -43.0917 | 2025-07-04 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| d32e3a23-97db-3e9a-8940-4b9002d50bc5 | -6.6112 | -43.8941 | 2025-07-04 03:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 343ec8b0-7b49-3588-89b0-91538786907e | -10.5586 | -49.1337 | 2025-07-04 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c397a778-c567-3748-af81-b704262b8793 | -6.61027 | -43.88432 | 2025-07-04 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 1786951d-003a-3096-b485-bf5598054767 | -6.60864 | -43.89372 | 2025-07-04 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7bab8fb7-2188-3266-9228-f92d32655f48 | -6.7452 | -43.15454 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 545c4fa3-f0c0-35cb-8479-b9b1b18d75bf | -5.04454 | -38.53749 | 2025-07-04 03:47:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb11df70-c5d1-3b13-b082-b663012850fd | -6.66515 | -43.17069 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 57ad1d5b-b939-3542-9f99-91b50c232294 | -6.39119 | -45.3141 | 2025-07-04 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 385d19bd-0025-3809-b99d-5f391b9a24f8 | -6.74305 | -43.14109 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bfeaf30-797f-373b-b1cf-e0ef712aa21a | -6.38614 | -45.31324 | 2025-07-04 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8623777d-5fb3-37b3-9194-6803a097ec40 | -6.75065 | -43.04517 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ea8c8d2a-b17b-3c86-9d96-697c42e34874 | -5.06612 | -37.66935 | 2025-07-04 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a6faaf3-cf3f-3b76-83ff-1ebb01696913 | -5.9137 | -43.45008 | 2025-07-04 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdf8d2a5-b72b-3f28-a8f8-cfee781c5ebf | -6.66011 | -43.17409 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 69f295aa-242e-355a-abd7-ae4b6a7271e7 | -6.60946 | -43.88901 | 2025-07-04 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| ab4b9b3a-d59f-34ec-b323-c4bd8b5f7b30 | -6.74233 | -43.17133 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 70009b5a-3901-3c9c-8c05-e301e5d3d8f4 | -6.29265 | -43.94839 | 2025-07-04 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77d2cb22-c229-3864-b7c0-e4957c61889f | -6.60489 | -43.88824 | 2025-07-04 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c82c678-32b8-3a32-81ca-b0d587cf5681 | -6.2909 | -43.67833 | 2025-07-04 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01a937ed-f375-3bd4-b16c-5484a6900e95 | -5.92078 | -43.45053 | 2025-07-04 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1aab4c3d-a10d-30aa-8255-970299607e01 | -4.17528 | -40.72133 | 2025-07-04 03:47:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 87816463-30be-37b9-bfac-150093564743 | -6.66082 | -43.16987 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c187c6a6-9448-32d1-bc96-403c81e9a8a6 | -5.28437 | -45.16873 | 2025-07-04 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0084d144-3ac2-3d72-9b92-daa240283192 | -5.77713 | -43.62226 | 2025-07-04 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59523522-d72b-3ae8-9673-accdf308cc7c | -6.58902 | -44.19991 | 2025-07-04 03:47:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ebbaa83-fd47-37b4-9806-74ff27bfbc64 | -4.83286 | -43.34959 | 2025-07-04 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0621cf9b-c7ad-3681-9d2e-3f361f718add | -6.74092 | -43.17957 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 53c2bb2e-eb3a-3003-b79d-90e112fecad4 | -6.73295 | -43.14806 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 164a4316-4f86-3b19-912b-4499bb42d96f | -4.01351 | -43.23785 | 2025-07-04 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd67dd54-4929-332f-a544-32be95c3272c | -6.74737 | -43.14186 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6800d71c-6e6a-3578-af5b-9d43e60e96b2 | -5.28702 | -45.17199 | 2025-07-04 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 524d56ff-ebd5-3608-ac7e-98bfbd39bcd0 | -6.7402 | -43.18376 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 71af6c68-ea0c-3aae-a79c-e341281567e4 | -5.91708 | -43.44527 | 2025-07-04 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8c1e500b-6f2d-3c4b-80f9-36d6d72263fb | -5.28753 | -45.16904 | 2025-07-04 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a6bbdeed-e7b6-3bd0-8c14-6f659842f44c | -6.27655 | -43.68075 | 2025-07-04 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7a3b8ce0-e00c-324a-aa65-0219c3561290 | -5.74965 | -46.08425 | 2025-07-04 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13233231-5592-3969-8d3a-a0cb70ded1ef | -6.27728 | -43.67638 | 2025-07-04 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7110e0e1-cad8-3119-8682-528342d3e5d6 | -6.73727 | -43.14883 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3ad5a74-892f-30e6-b3a8-11769aaf407c | -6.28561 | -43.68217 | 2025-07-04 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 358e123c-55fa-3ff4-b3b5-4d86952c07db | -6.11413 | -46.18441 | 2025-07-04 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77ba7a56-948a-346c-95f3-995e9530a86a | -5.75023 | -46.08091 | 2025-07-04 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 853d8066-f9dd-35a8-bd40-e01c423447e7 | -6.28108 | -43.68146 | 2025-07-04 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7de99c1d-f568-36e9-b59a-c05bb96f3d84 | -6.02144 | -40.28863 | 2025-07-04 03:47:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dc1826dd-f9c3-3812-870f-8ff882a443c8 | -4.71893 | -37.77774 | 2025-07-04 03:47:00 | NOAA-21 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8de94dee-fdf8-3202-9fe5-9ee498dfbcc4 | -6.01006 | -44.53237 | 2025-07-04 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8b0c913-1f43-3951-b45b-4264b7fca515 | -5.9206 | -43.47844 | 2025-07-04 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b5b677f-d39b-3862-9a65-ac0f4f82c080 | -6.61401 | -43.88982 | 2025-07-04 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 4d39f05a-0860-33de-8524-184ce7d013e6 | -6.49941 | -43.64485 | 2025-07-04 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cbf26ac-7d69-3f22-a964-fb93b04dfe89 | -6.12545 | -42.53006 | 2025-07-04 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fa01003a-6ad3-3584-a84d-6b4be6df208f | -5.06667 | -37.66582 | 2025-07-04 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 194cf96c-830c-33aa-886b-5a4189d61b75 | -6.73007 | -43.1389 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e59191f2-a8dc-344f-b4b9-b3a9983c46d4 | -6.66444 | -43.17488 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f441c04d-2492-3f16-aa48-ecc2aaf2823d | -3.81217 | -42.54725 | 2025-07-04 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7bc7024-7063-3509-ab05-e0aa3164a625 | -6.7344 | -43.13961 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc986a9b-2103-3574-b3d3-4b0c758f61bd | -6.73654 | -43.15308 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f47e968e-8bfa-330a-86a5-493631d6eaf9 | -6.74162 | -43.17544 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e41a50d5-54d3-3fef-8855-435b38622121 | -3.94252 | -41.50165 | 2025-07-04 03:47:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2cb92c90-7b36-310e-8ea4-950895d22f78 | -6.74087 | -43.15382 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0e46aa6-a538-3648-af78-bfa1f1bbd59d | -6.73368 | -43.14383 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21bf184c-07f1-349e-bfa6-674d26b4eafa | -5.47444 | -36.52033 | 2025-07-04 03:47:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4977c94-348a-35fa-be88-7d5a54c54a18 | -7.42553 | -37.20708 | 2025-07-04 03:47:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a786ddbb-14a8-3731-83ec-1716f0c88c46 | -5.91445 | -43.44548 | 2025-07-04 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a25fe398-5a77-3fea-8a08-cbd01f00f07b | -6.49568 | -43.63952 | 2025-07-04 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ebb7f11-fbdc-3dd3-b3dc-d0048bad843f | -6.28183 | -43.67697 | 2025-07-04 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c9ff9427-3e62-3ab9-a24a-ad97be108ae0 | -6.72935 | -43.14311 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efb44361-ee0b-3c78-8cd7-bce7cee3f49a | -4.00895 | -43.23712 | 2025-07-04 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c15fe5aa-a35a-339e-a876-33d8c489b6a6 | -6.7481 | -43.13761 | 2025-07-04 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0b33341-44be-315b-bd5b-b6e7373e65c0 | -5.28947 | -45.16954 | 2025-07-04 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f486be82-55de-3b1e-bd03-2b95e062faee | -3.25981 | -43.26476 | 2025-07-04 03:47:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e1dc393-0c2b-3368-98ed-4f1bd6354ecc | -6.28638 | -43.67759 | 2025-07-04 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12ab1b2f-ee5c-3ae5-96f7-ab3b3c8d4197 | -5.9163 | -43.44981 | 2025-07-04 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 635d037c-409c-3f6e-ac49-7e2cc6d7ab44 | -12.57462 | -48.88676 | 2025-07-04 03:49:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f5b5c1d-9919-35f2-8dc9-4b9f44a3e562 | -10.55706 | -49.12897 | 2025-07-04 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7ae5d5a2-8240-32c3-ba0e-49fb926fafc6 | -8.99709 | -47.44271 | 2025-07-04 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9180a48-1ad8-371a-a95d-b0aec2833cc2 | -10.35091 | -47.29545 | 2025-07-04 03:49:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d176a17c-7233-335f-b392-438864a100a7 | -11.91566 | -45.38857 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c08eb5e-8e06-3e5d-a961-9ff8e290db36 | -7.22647 | -43.08779 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| c33ba515-6518-3fab-8701-5804b8f61e97 | -10.56214 | -49.13496 | 2025-07-04 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 80a2c3a3-a819-38fb-a5da-76f8a86937ac | -7.21723 | -43.09039 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 00a93d6c-e089-374b-bc5e-82186638b6ef | -11.92757 | -45.37553 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbf96108-3bb8-365b-b188-07a3b4fb4a80 | -11.47335 | -47.92566 | 2025-07-04 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a186e16-d278-3ee7-9deb-cdba503cfa06 | -11.91945 | -45.39391 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 72b5dbef-4cfb-324f-b72a-dbe3cb237c45 | -9.79713 | -47.75005 | 2025-07-04 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d433ac59-d66e-3301-87eb-64954881146e | -13.40313 | -47.83564 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dee38983-77aa-35f4-8f26-63939405d807 | -9.80267 | -48.25109 | 2025-07-04 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b18430d-d8d6-3d1b-b068-613dd44927b3 | -11.20506 | -49.00385 | 2025-07-04 03:49:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README5.md)

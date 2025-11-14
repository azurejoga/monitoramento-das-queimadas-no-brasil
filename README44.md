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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39d4665b-ccdf-3021-ab86-f7b240974280 | -6.16087 | -48.04431 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 382d3318-309c-35f3-b254-213068b5c73a | -6.88149 | -41.58144 | 2025-11-14 04:44:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 58b27d05-d921-349a-b762-a0e21e66fb48 | -4.40689 | -42.32948 | 2025-11-14 04:44:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33af787a-795a-38da-89a9-fc7f9357a015 | 2.75225 | -60.36842 | 2025-11-14 04:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ecb3bc50-1912-31fe-8910-2c618cedb2a3 | -5.78031 | -51.42502 | 2025-11-14 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f109a48-2a90-31c5-8db5-e9ef72383569 | -5.65818 | -47.83199 | 2025-11-14 04:44:00 | NOAA-20 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e4431c2-71a3-3b78-8eac-cc4ce11a4b62 | -6.2811 | -41.73652 | 2025-11-14 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 846c1481-4c66-3ee7-81c7-f58a3c8676c9 | -3.81999 | -52.33217 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3334bc6-f744-3ae3-9834-bb10303e59cb | -2.11539 | -45.36252 | 2025-11-14 04:44:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a3d6f68-a799-316b-beb2-5897597f5dbc | -2.46677 | -45.19126 | 2025-11-14 04:44:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ef983411-f27a-3990-828b-4b719cd8f732 | -2.83926 | -45.48107 | 2025-11-14 04:44:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a40c62ce-1bc1-36e3-9d9f-e146025694d4 | -6.56577 | -48.73466 | 2025-11-14 04:44:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a00789d-5897-3537-8487-be7df9ca6844 | -6.53198 | -43.40777 | 2025-11-14 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 1c7ec6d9-9eca-3c3d-88cd-66beebf380bf | -1.4277 | -55.31009 | 2025-11-14 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a100d27d-d3ab-3ac3-9c48-1e3bea7fd3b7 | -2.11144 | -45.36193 | 2025-11-14 04:44:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 904fe54a-d1f6-3f31-96bb-ff02c3ce73d4 | -3.11222 | -50.28939 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e841dbe-2b0e-3043-9948-f49bfc9f62e2 | -5.73885 | -51.04303 | 2025-11-14 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16778bcc-fea4-3657-b6f7-8c6722f20743 | -1.42358 | -55.30942 | 2025-11-14 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27dfeccf-44d9-3a31-aae9-3084d87517bc | -3.45396 | -49.23964 | 2025-11-14 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcc9004b-bfee-32e5-9d2c-0fc83cb2e382 | -6.13766 | -48.05297 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8a107f7-e2b4-3df6-9dc3-6f5155605ca8 | -5.376 | -41.04645 | 2025-11-14 04:44:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29ae7bf6-2935-3a19-937c-d1d13fa62b58 | -4.6833 | -45.8559 | 2025-11-14 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7801a101-e005-31a4-a56b-d2a3759868fb | -4.74883 | -50.60056 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e55ee76-1681-372a-bde1-e7f00ca0eea5 | -5.74461 | -42.73151 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6a08ed08-cd72-3b72-bf6a-c0417804c620 | -2.45379 | -48.81715 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85ddc68f-63b4-3ffd-b8b3-643c5bf35d2d | -2.98776 | -52.62838 | 2025-11-14 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87ba8b1d-546d-3781-99d5-ef40ed5a15e2 | -1.83515 | -53.80293 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c589a40-fd6b-32de-998b-f85f49002086 | -2.92036 | -52.51574 | 2025-11-14 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea7e87ad-85c3-3c0e-97dc-5f55a92d5dbc | -2.46784 | -45.18429 | 2025-11-14 04:44:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f1928a-8cc0-34c0-b14d-f548a9c5b4ae | -3.34462 | -48.3883 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1c9d9dc-cb7b-36dd-912b-683e92bc57b4 | -5.529 | -43.67995 | 2025-11-14 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ada6c79-681c-32d4-b3f7-224b6dd4a44b | -4.75105 | -48.83123 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70f9dcbb-2d79-3a01-8082-1ce7ba5df63b | -2.45267 | -48.82425 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cea6e3db-e14d-33be-b3e9-85cde86767be | -3.47578 | -45.6466 | 2025-11-14 04:44:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ef66450-cb6f-37a8-8f51-a69f613adea4 | -4.19527 | -49.34304 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e320b5f7-2949-3fd3-b7cd-5f63a271413a | -3.76565 | -47.74358 | 2025-11-14 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| aa8221d8-106b-30bb-83cb-a6e667feec0f | -7.10911 | -44.07098 | 2025-11-14 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 926f2d08-c186-33b4-bee0-e47ae80df41d | -2.54647 | -48.38131 | 2025-11-14 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd7843e2-af9b-3363-b474-783a4c9086a5 | -5.41446 | -43.26032 | 2025-11-14 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 73330197-80aa-316f-8a14-97f1ec7726f1 | -5.75545 | -42.72704 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f431fbae-7a4c-30dd-80c1-ef25f3701ba4 | -5.90053 | -42.74953 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ef1e848b-a5a3-38da-bcc5-522da692e340 | -5.58042 | -46.31053 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f59f59a6-aa7b-3d08-a0ea-16836b28893c | -4.99242 | -50.43458 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3e58862a-4ee2-386f-a347-dad8ee00f618 | -2.4686 | -48.23054 | 2025-11-14 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81e759c1-7d1b-3250-9f93-31c0268f6d07 | -5.75006 | -49.2585 | 2025-11-14 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d28a585-188f-3335-931b-fb8820ab8139 | -6.15606 | -48.05191 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7fb75bd-b1b7-3b32-903f-3833b66cfcdf | -3.52749 | -52.79658 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| affd6315-8ec6-3264-b4d7-7c7d6b6efdff | -6.881 | -41.58495 | 2025-11-14 04:44:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fa164a40-430e-37f0-88f2-819cff03626f | -3.34519 | -48.38459 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03ab6215-aa5c-3c34-b4d3-1a49479c59af | -3.36912 | -48.41105 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9d7c60a-eb2e-30b2-afef-9dd33ddf7e87 | -4.88161 | -49.38697 | 2025-11-14 04:44:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85c53199-62df-39e9-995c-1e385e65957f | -5.42586 | -46.08889 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0692347-a8f7-3a03-8236-e4d8273d7859 | -6.14122 | -48.05357 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0392071e-8ee3-3622-8223-2a31871ff6f5 | -5.36305 | -46.28971 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 362319a9-2cd7-30a8-a6c9-2b10728d7f22 | -2.2816 | -53.64254 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2188453b-d19e-3dda-9866-aaf3bb4168f6 | -1.29577 | -54.22002 | 2025-11-14 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 55b599d1-875e-30c1-b21a-f2e6813fa141 | -1.2694 | -52.84716 | 2025-11-14 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83c4bcac-1850-3920-8654-529af06b3330 | -6.10467 | -47.01019 | 2025-11-14 04:44:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 786f1344-e14b-321f-b68b-658f48616d49 | -1.92498 | -54.51154 | 2025-11-14 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0375cb86-8913-3d97-b3d0-b8f2b4a69801 | -6.01366 | -51.51892 | 2025-11-14 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77024f64-e50e-35ca-8db2-cbc570452d69 | -2.45043 | -48.81662 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 774568d7-c3eb-3b79-b98b-de639a09e08e | -5.63407 | -48.24672 | 2025-11-14 04:44:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d97f04ab-8b2d-3be0-8a67-6c62f925a2e1 | -4.30395 | -46.27385 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d3ef9b9-065e-35a8-8840-0d56d7e6b476 | -5.41967 | -43.2593 | 2025-11-14 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 32c7e745-6567-32cd-8e56-e66966a1c199 | -3.0891 | -49.46607 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76c4c0d7-b3a5-30d1-a08b-9eb2394a428c | -4.21559 | -49.12384 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dbb4f980-e8c4-3a29-a60b-cb7061cc666f | -4.83346 | -45.58305 | 2025-11-14 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3aeaed7-8bd3-3407-af20-f74492c7b8eb | -1.33921 | -54.60602 | 2025-11-14 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bc075cc-c75b-3396-8941-28e773c1edd6 | -6.06208 | -47.88371 | 2025-11-14 04:44:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 962203fc-2658-3381-b2cf-22eecdfe56a2 | -3.28624 | -52.11407 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5899bef-3524-346d-bdc1-d2ae29630b03 | -7.4608 | -42.57691 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 643a16bc-80be-300b-bc80-b7611cf531d5 | -5.19258 | -48.03775 | 2025-11-14 04:44:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c3de054-0ce0-3a4b-983f-e9e6129eb38b | -3.47655 | -45.64152 | 2025-11-14 04:44:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f183bd0-632e-3eeb-8571-11498d9daf02 | -6.65098 | -43.5326 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1fe9acce-6f65-3d07-94d7-89bed367908d | -3.01272 | -49.43306 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 921319ec-65ef-30d1-a18e-104f606efe60 | -4.12592 | -43.00942 | 2025-11-14 04:44:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8569f63d-bf1a-3e37-ac3f-a7971edecb32 | -3.45907 | -50.59037 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e51791f2-a2cf-3f4f-a5ab-aa6a55cdd512 | -5.75078 | -42.72404 | 2025-11-14 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be3571a5-5119-3be2-a58b-810fd93c77f3 | -3.31287 | -49.46906 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d59b3a61-a933-33d1-be07-d92cc6755167 | -2.46731 | -45.18777 | 2025-11-14 04:44:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8b85466a-f6df-3e36-bc14-5e2a95055021 | -3.78955 | -49.57165 | 2025-11-14 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77a0e104-f26e-346b-91ef-fcbab059bed0 | -2.72828 | -49.38499 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23f70c66-b866-3c55-9ec4-4c0702b229b2 | -3.36446 | -49.50915 | 2025-11-14 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c967ebe-76fe-3081-bb28-882d0c5292b9 | -5.75506 | -42.72973 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b3f7d5c2-28b6-3a78-99c3-f5f99fcfa4a1 | -3.45806 | -43.1824 | 2025-11-14 04:44:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5392b98c-c285-3836-9d61-1605b33c88d3 | -1.83443 | -53.8074 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08c573fd-2e14-3ecf-aec0-c809592b8b23 | -1.83889 | -53.80353 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87483854-5b56-3cf8-b10a-92dfdb90939c | -6.8822 | -47.24433 | 2025-11-14 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba908f1a-fd3f-3f5a-a572-dc4d96d5136f | -3.17014 | -46.57753 | 2025-11-14 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75829fec-0644-3392-a8f8-754f1c100585 | -6.71993 | -42.95326 | 2025-11-14 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5157f90b-5c48-343b-a3c8-074b294e0b7d | -3.83207 | -53.46344 | 2025-11-14 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a916d4d-ca5c-3a8a-85b7-6edb099e7a41 | -7.15027 | -41.26407 | 2025-11-14 04:44:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f49471a-d2d2-39c8-9148-8053ea442686 | -6.14539 | -48.05011 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1405cba7-9ef0-3723-9175-429a3666a13a | -4.26582 | -42.11048 | 2025-11-14 04:44:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 78865ca8-ba02-3f8f-b764-8b6863d83cab | -2.83453 | -45.48558 | 2025-11-14 04:44:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38dbfa7a-ab94-367b-8d8a-31238f4057fd | -6.1525 | -48.05133 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65439c41-46f0-380d-8d0f-64944116b9ac | -4.60814 | -43.38414 | 2025-11-14 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cdf0497-3ef9-3b90-9bcf-85f70c2c980a | -4.69746 | -44.37546 | 2025-11-14 04:44:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d02e590c-3496-3b2a-a978-eff8f852ffb6 | -6.10901 | -41.59418 | 2025-11-14 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba21606e-7860-342a-bcbe-823e61dec480 | -3.79636 | -52.04075 | 2025-11-14 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README45.md)

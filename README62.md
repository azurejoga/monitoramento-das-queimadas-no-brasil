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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7989af3f-b8ee-3e4f-bc59-5e94156d990f | -11.90299 | -55.89454 | 2025-08-23 05:21:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15a805c1-e745-3fd4-8da4-83376095547f | -14.76057 | -55.98853 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3db15343-2229-31f0-83a3-f171df0fc833 | -6.93097 | -62.89277 | 2025-08-23 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47c3754f-3108-3373-aba6-7f8154489e81 | -14.64837 | -54.91693 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91774579-9b20-38ae-b421-2ac695c58f00 | -7.72824 | -67.07269 | 2025-08-23 05:21:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3f77c4d-fe1b-39ff-ae43-030b9ae1f643 | -12.30651 | -49.98965 | 2025-08-23 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3ad9b5e-321c-30b1-8a72-3dbe2b9f3f1d | -9.17351 | -59.60825 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 993c3ce8-df76-3405-b9e2-c2fe9161fd0d | -9.20223 | -59.44809 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fa1ba0f-7a45-35ca-87b6-fa9b05934938 | -8.89167 | -62.41427 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8b96c64-4ca3-3c2c-b7a0-687ff77369bd | -9.52087 | -60.55339 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf3d0e11-f178-32fb-a929-25fb6b12f577 | -13.13252 | -57.11464 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb966492-d66c-35c9-9c74-a2e3e2b604ad | -9.15855 | -59.5951 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa7bef53-3ea1-3c32-918a-841ae24f11df | -12.9859 | -56.89669 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30c84097-2339-3481-a210-dbb7c0f833d5 | -8.85664 | -49.86874 | 2025-08-23 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 67eb866f-3e7a-390b-8e2d-b88582bed145 | -9.51416 | -60.5523 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84e68ab3-a6a3-3654-87c0-18f568a3ad7c | -9.18626 | -59.63533 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f7b9622-68b3-30e5-adc6-d8033844d358 | -9.94997 | -60.19365 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8bd93f23-6f97-3d27-858c-8f41027fa643 | -9.19235 | -59.63988 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22d816bb-4db0-3039-9f56-4681ebabc598 | -14.9149 | -47.31689 | 2025-08-23 05:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44d755fa-5178-384c-b7bc-d957393861d7 | -9.51808 | -60.54927 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb7d714c-6d22-3920-88d8-f06e8576b5c9 | -9.50924 | -60.51853 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 951df493-3b87-3691-9612-9b1d946a2a80 | -9.51038 | -60.5114 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b090681-bf11-3759-88b2-2d05d554a208 | -11.11249 | -62.66965 | 2025-08-23 05:21:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca4e180d-dd38-3802-b5c2-41e3ac5ddd48 | -14.99798 | -54.87197 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67b7ca38-ea10-36e9-baa7-895743d36b76 | -9.17517 | -59.61926 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 183da8c4-f177-39e9-80ac-273a565fbe94 | -14.37647 | -52.04322 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84afb654-58f4-3486-9a6e-dcf2b3b9e3c0 | -14.61226 | -54.79716 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 099af63d-cd35-34ca-b0f9-a8a2cd068ae9 | -13.46161 | -47.03042 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3c9abe5-ade3-3bdd-91f9-7e5610da2443 | -13.45474 | -47.029 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fb8ffed3-80c4-3f32-85c1-a7a4c21b435e | -9.64713 | -59.65213 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6de440b-1935-33d3-9d95-f0ffabed4e1b | -8.61793 | -62.6041 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30197f8f-2b85-3248-9232-94774bd26b49 | -7.78575 | -61.58118 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f157913-d579-3354-9fca-f946ca7efce0 | -7.57341 | -63.43999 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a2ac79ab-34bb-3850-b9a4-b468cc10ffe4 | -9.10633 | -61.43305 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 484ace69-8598-3e45-ac8a-cf6d4db12110 | -9.95888 | -60.18065 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 96e3db0e-5d47-3a95-a50d-df0cb167d4a5 | -14.32 | -58.55484 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95a74b4f-9275-3342-a72d-33ebbd0df6bf | -9.56134 | -68.57974 | 2025-08-23 05:21:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eede428d-7d31-3762-ac3f-6f639e0718e3 | -9.19734 | -59.65143 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27abce58-d2bb-3591-9eaf-a8562141e910 | -14.37684 | -53.35889 | 2025-08-23 05:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2544794d-dd68-35f4-9316-88b8f269048e | -9.17129 | -59.62222 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6d9ff34-9c16-3827-9b47-85c7b116593c | -7.42885 | -60.59824 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5338377-6dc1-387d-8c4e-6faf98576884 | -9.23216 | -59.75019 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbb92eb8-003d-3b44-928e-0829fb0e59c5 | -8.62099 | -62.6309 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff783e1f-b254-3b3a-8e5e-1cc95a728ada | -9.18349 | -59.6528 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91ad6e31-67f2-3dc3-bd3d-ea8e44d27d26 | -10.41019 | -57.68491 | 2025-08-23 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6eaa182-5bda-3cff-82f6-323686623d54 | -11.19775 | -55.02625 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 493a7445-b9d6-3e3a-83ec-9e3d42cef54f | -9.88432 | -60.29198 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caf63cee-21af-3fd4-bb1f-71971c73c1cf | -7.55663 | -63.8521 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d593565e-8ca2-35af-b481-aa7de0234a23 | -9.1956 | -59.46852 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9e6d208-21cb-375c-a018-1e66e86cf69e | -9.95277 | -60.17606 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c92409a2-6461-35df-ac92-34bbebcfc66a | -11.193 | -55.03089 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 147c2aa9-4a2b-35b5-9a98-cd91a565ec16 | -7.43095 | -60.6286 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fc011570-b30a-343e-a8fc-a2bda55a26c0 | -9.94165 | -60.18147 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 140405b9-39b0-3dab-a176-b004fdde3a10 | -13.48931 | -47.03397 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 923836a1-c789-3385-9700-f38d8270204f | -13.02732 | -56.83332 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 143e0d15-b894-3942-86a4-af2b2b6704fe | -12.30384 | -49.99527 | 2025-08-23 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9137f3f-fa44-3207-9522-5cc71c0523aa | -7.90016 | -61.52338 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 252673a4-5155-3754-b6f5-61e23ccd2c40 | -8.59182 | -62.62597 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f14962de-0444-3ab2-8c36-d42024217ff4 | -6.87966 | -59.81952 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2e85515-e6ca-3f0e-94bc-17ca8d698c76 | -9.42593 | -62.25475 | 2025-08-23 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4db3261-a5d8-3084-bca6-ed046dd800ab | -13.0389 | -46.32713 | 2025-08-23 05:21:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3748d588-d803-3881-aae0-77ed7f220d79 | -9.18238 | -59.6383 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de95728-95d1-3219-9388-49d879585fc2 | -9.2134 | -59.61464 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d764f29-d27d-35b9-8eec-a3cd6d7f2465 | -9.20556 | -59.44862 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 952581dc-f9b3-3418-9896-8647edad0604 | -8.87884 | -62.42489 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3652f7d-d0f0-3084-9e46-37e338d4bcda | -9.95109 | -60.18661 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a77a0d87-c9d4-3c2d-afb4-b6689729b289 | -9.38878 | -60.5102 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9445a3f0-4560-39c6-a78d-dd6327d8fd84 | -14.28101 | -60.38329 | 2025-08-23 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ccbe29f-f38e-3a3a-899a-efe18afd83c3 | -14.67958 | -56.61504 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 281dfb14-73f2-3a28-86d8-7d6dcb3aa88f | -13.03227 | -56.82497 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88319c2a-b4a0-3ff5-9791-16d9013feeac | -10.46256 | -59.13488 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5654041b-cce6-30f9-b439-232dd443cd09 | -13.03533 | -56.82994 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0426c58d-33c3-38b5-aa0b-eb6dd59d1f2e | -7.05472 | -59.82238 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58dac89c-9a09-3d6c-8ae8-06f75666ca00 | -14.33037 | -58.58022 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7de20bfb-507f-36ae-a9ee-d7b7ce94dbe4 | -9.96052 | -60.19175 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c4ec9827-2247-3967-a3bc-d5afcf1c6b4d | -11.61979 | -50.42424 | 2025-08-23 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fb798c2-cf4e-3c98-8015-a0e7e0d8b9ee | -9.20335 | -59.4626 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 526df37b-1a97-3375-be63-628b7d87f10e | -9.52486 | -60.5284 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8535ac94-b734-377e-b6d6-c488340fb384 | -9.65599 | -59.6392 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9c575fd-560e-3a6d-913f-3221e94593ba | -13.13918 | -57.12 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b70f499-2ea6-3cbe-8514-691603795002 | -9.51873 | -60.52375 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2236c34c-03d7-3173-9ec1-d419654b3207 | -13.38306 | -46.21482 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d237425-2a9e-32cb-a6f2-a4fa7914f2d3 | -14.72865 | -55.4177 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba428044-a1ef-3c36-9689-2d3738c7cb83 | -9.19069 | -59.62892 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf5ef96f-4cdb-3ee8-a019-4498cc417465 | -14.66215 | -54.91062 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ee16bd8-23c5-38c2-90f7-8eb48c1a3df7 | -9.50867 | -60.52209 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1ba497d-709b-3a45-9d6e-0f9ae32271ed | -9.18625 | -59.61387 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba96f600-7e9a-35ca-983e-d4df66aa81b4 | -9.21064 | -59.78267 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 865313cf-85f5-3879-87fb-71eb16246966 | -8.61735 | -62.63029 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f33beca-500f-3bab-b190-b44c0ac9a42a | -7.81109 | -63.55044 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9338a17b-949d-3c3c-b393-305b03c7990b | -13.02628 | -56.8264 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3ce1aea-afa9-3db1-b33b-1f9bcee943f0 | -9.21879 | -60.78483 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a83406b-623f-3916-9d98-d6c794752c67 | -14.6526 | -54.91751 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e81f092f-0120-3a16-83a7-7ee5172ab171 | -10.46535 | -59.13894 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4454f641-a720-3578-a8b6-f317b75c7392 | -10.84579 | -61.97093 | 2025-08-23 05:21:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d65e5a0d-1694-31b1-bc53-42d74347948e | -14.46859 | -55.94167 | 2025-08-23 05:21:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2a8779f-6e50-370b-ab43-d6333396d169 | -13.12769 | -46.89742 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ef25eeb-2820-3453-bc4b-9b27c39fdaba | -9.51973 | -60.56052 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f286965-90c0-3eef-8eee-aa29c34a0a3b | -11.32424 | -55.22218 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d737e6e4-cfb1-3732-9cae-d7700680bce2 | -9.65156 | -59.64566 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README63.md)

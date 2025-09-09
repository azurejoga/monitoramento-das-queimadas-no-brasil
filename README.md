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
| 2be83e15-6d21-34a1-9da8-bc319e69ee0b | -9.9498 | -60.1367 | 2025-09-09 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0a1fb6b1-3d66-395d-9136-865d96f1df04 | -18.1495 | -51.8375 | 2025-09-09 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 5e552a69-ec4b-36ee-b7bd-44373a779273 | -22.3261 | -50.8934 | 2025-09-09 00:00:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 272.5 |
| 99e1c713-31c1-337b-b36c-3b0f89a26c5a | -10.9808 | -45.1335 | 2025-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 59987dc7-36e7-34e9-9b91-7050b4a93373 | -16.3136 | -50.0427 | 2025-09-09 00:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 711fb13d-3255-3f62-959c-8bc2b6a3ee72 | -22.1213 | -47.2765 | 2025-09-09 00:00:00 | GOES-19 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.1 |
| 400187da-615f-3a75-b53f-0886b93c34e2 | -10.9811 | -45.1104 | 2025-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 611.4 |
| 80d4d06f-301d-3322-8d90-fd16be807d02 | -12.1991 | -53.8817 | 2025-09-09 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| b6a1875f-0be0-362e-bd91-6cd1e26edc0c | -12.967 | -54.7705 | 2025-09-09 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 128e49c8-6ae0-393b-9a8b-43fea07bf0c9 | -11.4277 | -43.6017 | 2025-09-09 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| f71cacf4-3e87-3d24-b725-e0aa893735c2 | -12.9482 | -54.7519 | 2025-09-09 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 5fbff095-643d-365a-9b72-f47d38163744 | -10.9616 | -45.1361 | 2025-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 294f3433-b339-3a68-af75-4611c8e1c3cf | -12.948 | -54.7724 | 2025-09-09 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ee7dfc2f-1084-3a51-a534-454d16c94e19 | -11.2196 | -54.9975 | 2025-09-09 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9169121f-4592-3802-bbfd-80e14c0b7217 | -9.0802 | -65.3789 | 2025-09-09 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 132e5f7b-a006-366a-b1bd-19e0286c7d19 | -11.2007 | -54.9992 | 2025-09-09 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0e8a5f9c-56ab-3177-b379-83e095500b72 | -15.5465 | -48.3727 | 2025-09-09 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 16a0b186-d7d8-3123-accd-d4955c6c781b | -10.9624 | -45.09 | 2025-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| abc7d9e1-11c3-302e-8ed2-67ca8f1d6f9e | -22.3463 | -50.9117 | 2025-09-09 00:00:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 512c573f-699d-3de3-aceb-4d9ad11dbf81 | -12.6153 | -56.9742 | 2025-09-09 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 71abb6a3-f18a-3618-b4b6-6950943cbb8d | -12.6343 | -56.9725 | 2025-09-09 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f358ac7f-01b0-35b8-bf8b-c104befe923b | -18.8179 | -49.659 | 2025-09-09 00:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |
| 68aabff6-006a-39b3-a334-8a9e69925a20 | -22.3475 | -50.866 | 2025-09-09 00:00:00 | GOES-19 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 591bbe63-a51b-320b-9ade-ed6be6638d98 | -17.2956 | -46.7497 | 2025-09-09 00:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4320aa42-15c5-3364-aa16-b1b2b2a4e34f | -22.3267 | -50.8706 | 2025-09-09 00:00:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 192.3 |
| ed014c3a-61f1-3536-937c-8e78b3798ae8 | -18.15 | -51.8156 | 2025-09-09 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 11444c9d-d1d4-3bb1-98c3-94b6dc06a24f | -5.6931 | -45.9891 | 2025-09-09 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 53fed39e-7eab-38fb-bb7e-ed07b024ef16 | -8.0606 | -48.6423 | 2025-09-09 00:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 84.7 |
| c8ad6189-ac9e-3d1e-977f-c82cd7725424 | -10.0111 | -64.9151 | 2025-09-09 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9bdc38d0-0b59-3807-aa58-36df4870626c | -22.3469 | -50.8888 | 2025-09-09 00:00:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 382.1 |
| 632547a3-0329-34ba-93f6-95be3cb38826 | -11.4281 | -43.578 | 2025-09-09 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b49933e7-53b8-31a9-b2e0-2ae33ff4c190 | -12.2178 | -53.9005 | 2025-09-09 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e619910f-d016-3b08-8aef-97ae699a992e | -17.2757 | -46.7538 | 2025-09-09 00:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 9195e0ab-fbed-331d-b509-47938e1f73fe | -12.1988 | -53.9024 | 2025-09-09 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 41c90174-2af4-3055-ac5d-239030f5ea99 | -12.9673 | -54.7499 | 2025-09-09 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 60c5dcc2-9c12-36ac-96aa-f8e97923253c | -8.0609 | -48.6206 | 2025-09-09 00:00:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 74.0 |
| dcc9d215-c510-33a7-a065-f437d944ae32 | -10.011 | -64.9339 | 2025-09-09 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| cf2d480d-8a40-3f3e-a7b4-57db76fc12fb | -5.6738 | -43.9 | 2025-09-09 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| ee3e8f2b-85fc-3168-8084-fab0d4d70912 | -5.6925 | -43.8986 | 2025-09-09 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 02db6b35-1179-3283-b0de-211746a0275b | -9.4436 | -60.5114 | 2025-09-09 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1f26892b-0e2f-39ee-b4f3-2038deabc161 | -6.3229 | -53.4146 | 2025-09-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8dbb838c-d97d-3b4a-acdd-33f235260cba | -9.2008 | -67.5525 | 2025-09-09 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 24c15e0f-a226-3150-8709-bff5df4bc0c6 | -10.962 | -45.113 | 2025-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 518.5 |
| 55db7d52-8f13-3cff-9fab-14e428f37da1 | -10.9815 | -45.0874 | 2025-09-09 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| c3a82e2e-3227-367f-9d92-0ac640a48f14 | -12.1991 | -53.8817 | 2025-09-09 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 5dddf88a-05a9-3b72-b5f1-b57174816af8 | -10.0111 | -64.9151 | 2025-09-09 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ecad9c5d-20ca-3b68-8ef7-13b279fcbaa8 | -10.9811 | -45.1104 | 2025-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 500.4 |
| efe1cb06-b33b-323d-bad7-2ca00c741697 | -12.8651 | -62.1074 | 2025-09-09 00:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 6146a53d-c612-3afa-b15c-ef816eb95e3d | -5.5703 | -45.0518 | 2025-09-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 03547a2d-bc6d-34d9-84da-24559a19d041 | -18.15 | -51.8156 | 2025-09-09 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 975f2313-7f15-364f-8b89-405ca4d3c610 | -5.6925 | -43.8986 | 2025-09-09 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 54946c01-0317-30b7-9f26-fb9ed8c9b00b | -5.6931 | -45.9891 | 2025-09-09 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c401a1d5-1fd8-3dab-8701-fa0b05c8abf2 | -5.6738 | -43.9 | 2025-09-09 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a7151a14-4e8e-3d04-b231-80c0ee5eaa81 | -12.948 | -54.7724 | 2025-09-09 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 5bce63f4-8929-3832-b53d-26e0ed14a62e | -10.9624 | -45.09 | 2025-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 5c723096-7f33-3f78-8dd6-5367e5f88156 | -11.4281 | -43.578 | 2025-09-09 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d994db92-5642-3e17-a31b-ec3e5865855b | -8.0606 | -48.6423 | 2025-09-09 00:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 62a48d52-efe4-3fb6-aa70-bc3e36af8765 | -12.9673 | -54.7499 | 2025-09-09 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| bb5c5a6f-6687-3728-ac2a-054fddec9d04 | -18.1495 | -51.8375 | 2025-09-09 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 14845403-4b3e-357c-900b-489bd39defb9 | -21.0165 | -48.4148 | 2025-09-09 00:10:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 2c3cfc07-4cba-38ee-ab98-95510539a9fd | -12.1988 | -53.9024 | 2025-09-09 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| c4b9073e-459d-33bf-984d-12d657101990 | -10.011 | -64.9339 | 2025-09-09 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b68adfc3-cc96-3f07-926f-2d3ea8b284b1 | -5.6933 | -45.9667 | 2025-09-09 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| d14e0067-63b4-39b4-91e1-6b9f8b546717 | -5.589 | -45.0505 | 2025-09-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 39e5839e-bf2a-3a54-b719-9446edc70e20 | -19.5865 | -49.4602 | 2025-09-09 00:10:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 110.7 |
| cada2c03-de1d-3e36-b16e-92242e50bf74 | -9.0802 | -65.3789 | 2025-09-09 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 403a1fae-1d3a-369c-b7d2-1178354284d1 | -12.9482 | -54.7519 | 2025-09-09 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 4b38b703-9962-31ca-ae06-511b6d93c721 | -10.9808 | -45.1335 | 2025-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| ecd5d337-dd16-332d-b42c-1dbaba1dab2f | -11.4277 | -43.6017 | 2025-09-09 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 61fcc15f-a6f9-347f-be5e-0a5585a0271b | -9.9498 | -60.1367 | 2025-09-09 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 06b69b54-c863-3551-84b2-85472af564db | -10.9815 | -45.0874 | 2025-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e7b0f0ff-c9f0-3922-99a1-ec10b2605ccb | -8.0609 | -48.6206 | 2025-09-09 00:10:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 689f29b1-8ae3-3969-8bc2-6d42350fadd7 | -5.5705 | -45.0291 | 2025-09-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 564b079e-dc43-37f8-97b0-50f8bdae00d1 | -17.2757 | -46.7538 | 2025-09-09 00:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 59b1a8c9-5ec1-3610-926d-5abe8f7aa01a | -12.8405 | -52.9413 | 2025-09-09 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c12ac6af-1553-3387-88ef-0591f8ad05fb | -10.962 | -45.113 | 2025-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 580.0 |
| 1fa580a5-b7e2-360a-921e-a91b9c592000 | -12.6343 | -56.9725 | 2025-09-09 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| daa889df-c43a-3c7e-8083-aa725547152f | -6.3229 | -53.4146 | 2025-09-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a611edc3-af3b-34e6-99fe-07ce7f360b47 | -10.9616 | -45.1361 | 2025-09-09 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 123bd31c-aa02-38ad-94d8-2b01be510b42 | -12.2178 | -53.9005 | 2025-09-09 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 11f1678d-43e9-3f4f-8b30-a6f061f9068d | -17.2757 | -46.7538 | 2025-09-09 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 3699b178-aa03-3257-8269-21122de550f5 | -12.6343 | -56.9725 | 2025-09-09 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a74688e7-3108-31fb-99df-c19081bcf34a | -8.0606 | -48.6423 | 2025-09-09 00:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e9b9b195-1fb6-38b9-98eb-d26c9970e37b | -10.9616 | -45.1361 | 2025-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| aa618b54-68c5-3a5f-bb66-834b59fc91ec | -22.1422 | -47.2711 | 2025-09-09 00:20:00 | GOES-19 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 5ab5206b-3699-3ee8-b107-c9c07d57cb1b | -11.2007 | -54.9992 | 2025-09-09 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f4c000a0-5e7a-329b-a728-df0dd1ea58dd | -9.0802 | -65.3789 | 2025-09-09 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0ddc87fd-44df-306b-bdac-8a8f5ee3d227 | -5.5892 | -45.0278 | 2025-09-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| d5e864f6-9249-3da4-b926-53d712eaf294 | -9.2008 | -67.5525 | 2025-09-09 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c3046450-72e4-3a1e-9bd3-df3f53228b7e | -12.948 | -54.7724 | 2025-09-09 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e8857837-8432-3b27-a104-4721689dfbb7 | -18.4808 | -49.5447 | 2025-09-09 00:20:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 559a394e-05ca-3697-a4c5-d06e533cf707 | -5.589 | -45.0505 | 2025-09-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 3b69af09-0ef8-354c-aaca-c50147c4e6f5 | -5.6738 | -43.9 | 2025-09-09 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 59d667b0-48eb-3f18-aa54-6be94643a1f1 | -12.9482 | -54.7519 | 2025-09-09 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| e05e5c54-6655-3701-a16f-cab0ae970fb8 | -10.9624 | -45.09 | 2025-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| ce92f60c-6069-3131-9825-4bfa0763e010 | -12.9673 | -54.7499 | 2025-09-09 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7940686b-0460-3c6d-b1a3-e77c760b3c09 | -10.9811 | -45.1104 | 2025-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 392.2 |
| 020f902e-24c1-3296-ab5e-6fc48a91677b | -22.3885 | -45.4223 | 2025-09-09 00:20:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.6 |
| 242ff3ec-58f9-34c6-a95e-0da05c2b19f0 | -10.0111 | -64.9151 | 2025-09-09 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| db0ff908-5a3a-3a7f-a606-1dce5a7d3a82 | -22.3893 | -45.3976 | 2025-09-09 00:20:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |


[Clique aqui para ver as próximas entradas](README2.md)

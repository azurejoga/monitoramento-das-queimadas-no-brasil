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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 936366db-2d90-3bf1-a317-818201e43fcd | -15.68461 | -47.05379 | 2025-09-12 00:09:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9095d228-a523-36ba-a012-61dd6ac90907 | -19.16304 | -47.99703 | 2025-09-12 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 63dd94c7-7950-31ab-9c65-9bbffd74eaa4 | -19.24148 | -48.04548 | 2025-09-12 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 3d6282b9-23ba-3259-9b3e-4a706a478af6 | -14.23401 | -44.25196 | 2025-09-12 00:09:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 89092862-8b2a-3d36-ab70-540d010098ff | -18.14502 | -43.23505 | 2025-09-12 00:09:00 | TERRA_M-M | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7cc52962-5ff3-3d10-be0d-e5331b591c27 | -21.33322 | -45.0278 | 2025-09-12 00:09:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.8 |
| 8b348c21-215e-3cf6-bee4-8dabffb8f767 | -22.48561 | -46.58637 | 2025-09-12 00:09:00 | TERRA_M-M | ÁGUAS DE LINDÓIA | SÃO PAULO | Brasil | 3500501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 067670fb-0434-3ea1-ad5f-81e83d6544f7 | -23.43442 | -47.02529 | 2025-09-12 00:09:00 | TERRA_M-M | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 2eea16db-b261-3ae0-89bd-a2d36d99955d | -18.65865 | -47.65999 | 2025-09-12 00:09:00 | TERRA_M-M | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 8085d5b3-0331-3383-9198-030e20673dae | -17.95882 | -45.28423 | 2025-09-12 00:09:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| cf867970-3022-3152-9adf-9da7a086b856 | -21.95756 | -47.5699 | 2025-09-12 00:09:00 | TERRA_M-M | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 586c2c3a-e644-3c63-b988-00f9c62d06e0 | -16.4309 | -47.62252 | 2025-09-12 00:09:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| bafe1ced-255d-38e6-bdaa-f654e49f468c | -18.14365 | -43.22453 | 2025-09-12 00:09:00 | TERRA_M-M | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 447e7cfc-85d6-3b84-a31a-d7acc13d36b8 | -15.5005 | -47.35013 | 2025-09-12 00:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a454bcf7-c25f-3201-925e-95ad5dd5b265 | -17.35543 | -46.7034 | 2025-09-12 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 95a1f84e-0bc0-3332-bd08-be8f4fc1588b | -20.15125 | -43.68092 | 2025-09-12 00:09:00 | TERRA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| fdd5fca6-cd1e-3963-be8c-254d5c073efe | -13.32771 | -43.59168 | 2025-09-12 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7cefcce5-5564-37e9-909b-af2c2bd0477f | -15.09654 | -48.03085 | 2025-09-12 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3c2f4243-2ef6-3891-a435-45d417f4064e | -22.88068 | -47.17731 | 2025-09-12 00:09:00 | TERRA_M-M | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 48f31e77-4778-3ae6-8f4f-d32ad378f175 | -20.01864 | -47.63486 | 2025-09-12 00:09:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 503998f8-7e50-337e-a4f6-3688cceb9841 | -19.75103 | -46.09141 | 2025-09-12 00:09:00 | TERRA_M-M | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 377e8884-9c50-3311-9784-df6fdc467eb1 | -18.0661 | -45.4373 | 2025-09-12 00:10:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 09df58ab-1a20-3f7b-a8b3-eb4460b8b7b6 | -12.8286 | -61.9551 | 2025-09-12 00:10:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 284.3 |
| 21df53e3-3460-3e4b-b079-6c5685d53d39 | -12.9292 | -54.7538 | 2025-09-12 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 5abb5316-beb9-3d81-995c-ad985fe74a35 | -21.947 | -47.5578 | 2025-09-12 00:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 4ebc03f7-f8e0-3ae2-8dea-5eb4995f9627 | -22.6404 | -53.0946 | 2025-09-12 00:10:00 | GOES-19 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 107.8 |
| 86aa80b0-1fef-3410-b143-598c79ee407b | -11.6828 | -46.5179 | 2025-09-12 00:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 1c9850ef-8223-332a-8d67-c6853a5c634f | -9.5137 | -54.6292 | 2025-09-12 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 88fe30c2-0945-3e16-82c6-22f5396d4320 | -15.8336 | -50.558 | 2025-09-12 00:10:00 | GOES-19 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 13fdd106-8473-3ea0-8b83-bf54a3a1f26d | -9.2287 | -59.3823 | 2025-09-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 16671205-554c-3491-af49-5aad19beeb1c | -21.9679 | -47.5525 | 2025-09-12 00:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 54a8bf4f-562c-33bc-9a23-c04121918a09 | -11.9717 | -51.1427 | 2025-09-12 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 389ef78c-5dbd-3b13-be5c-1b4eb5e44d9c | -7.4049 | -50.6367 | 2025-09-12 00:10:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f44e6174-0f36-3c87-ae0a-cbc77d6ad403 | -6.4696 | -44.916 | 2025-09-12 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 6abcc642-edf0-3a2c-b164-ebcf9f616bfc | -7.4236 | -50.6354 | 2025-09-12 00:10:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| cdced473-7a1b-3715-810a-408b4a737ca7 | -7.4234 | -50.6564 | 2025-09-12 00:10:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8f3cbc26-bc6a-318d-9541-0977631e1a57 | -12.8475 | -61.9539 | 2025-09-12 00:10:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 103228d7-fbed-392c-b989-b1e61bf4fe10 | -20.4052 | -49.1278 | 2025-09-12 00:10:00 | GOES-19 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| e2447f8b-e36a-3e2c-85ac-05bdf95ba115 | -16.6133 | -49.7939 | 2025-09-12 00:10:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ffd4ddb6-e6c6-3ece-aeb7-4add7458b476 | -23.1358 | -47.4859 | 2025-09-12 00:10:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| fefecb41-7d85-37ad-a1ee-373c641fb6fa | -11.7016 | -46.5379 | 2025-09-12 00:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| a7b70da7-5477-3f5d-b9bf-08f1cf16f5aa | -23.1146 | -47.4915 | 2025-09-12 00:10:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| d2947313-eb4d-33b6-96a1-85addb04d41e | -11.7012 | -46.5605 | 2025-09-12 00:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| adff7207-6199-31fd-ae7a-ce8ca006fecb | -8.8901 | -49.9236 | 2025-09-12 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 4dfde2b3-c1db-3fca-985f-28e9ebde669b | -8.9089 | -49.922 | 2025-09-12 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0f73178e-82e1-35e1-9d97-cc871afb125b | -8.1837 | -46.0965 | 2025-09-12 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3622c53a-c215-3464-94dd-a2bf75766181 | -9.2101 | -59.3833 | 2025-09-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 636313d9-0f4d-3b72-b4f0-306ff2adf8fc | -6.4694 | -44.9388 | 2025-09-12 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 349bbb2c-32a1-3f54-8c10-71f17abb8dff | -13.3238 | -44.0945 | 2025-09-12 00:10:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f4578d9f-17c8-35f6-8c97-0c36c6110782 | -11.1809 | -55.0821 | 2025-09-12 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 570c8530-9922-3b7c-9f08-a7c97a776f6f | -8.8899 | -49.945 | 2025-09-12 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 210.3 |
| b02c58cf-929f-3328-80d5-dc2451fbd7f4 | -21.9686 | -47.5287 | 2025-09-12 00:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 146.4 |
| d733f1b0-8e5d-3161-8bb1-fc9e6da81f37 | -7.4047 | -50.6578 | 2025-09-12 00:10:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 71333f5f-50cc-350c-b675-7dac332848d5 | -9.7307 | -65.1882 | 2025-09-12 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 61ac174f-14b2-33a7-93b3-3870ff85793a | -12.8287 | -61.9358 | 2025-09-12 00:10:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 143.7 |
| ecbe9ce4-1c89-3f16-80df-3fd159e54f46 | -11.1998 | -55.0805 | 2025-09-12 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| afcf25cc-a340-30e1-83ac-0e7ea8593076 | -6.48 | -43.8822 | 2025-09-12 00:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 5e863dca-11c1-32d9-a41c-4152cec2412d | -21.9478 | -47.534 | 2025-09-12 00:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 5639254c-5a63-3227-98b3-36c46d49ebd3 | -6.309 | -42.2311 | 2025-09-12 00:10:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 1f136153-e6da-3afb-9843-1daebeeb9350 | 2.5064 | -61.0201 | 2025-09-12 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 36.6 |
| e360514a-7b55-366b-9c02-9697576fcdad | -15.8144 | -50.5392 | 2025-09-12 00:10:00 | GOES-19 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 65ae9387-0b05-35db-bebe-227b910b25b4 | -12.8284 | -61.9745 | 2025-09-12 00:10:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d851493e-26a6-308d-89d4-fc75ac92a00c | -8.9087 | -49.9433 | 2025-09-12 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8bc4afe3-7809-3883-9cde-3062fdf3bd08 | -11.6821 | -46.5632 | 2025-09-12 00:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5ca153d3-5e9a-3a47-8658-aab5e988f7b3 | -11.702 | -46.5153 | 2025-09-12 00:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 7ab75692-9007-3e8e-a0b1-e6546abe11a5 | -11.6825 | -46.5406 | 2025-09-12 00:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| e4cd83b6-8d22-3ea4-9be9-548ad6f2edbb | -8.9563 | -46.0849 | 2025-09-12 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d8c6c710-7fce-3c88-bf0f-63ec257e56fd | -12.8096 | -61.9563 | 2025-09-12 00:10:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| dc7a5960-72b1-302d-b922-1c5911712587 | -23.1139 | -47.5156 | 2025-09-12 00:10:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| 4e57b651-c16f-30f7-9b63-caaf0fb4d851 | -15.834 | -50.5361 | 2025-09-12 00:10:00 | GOES-19 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 0f485dd4-e5a7-316e-ac27-3c4aa7f68b8d | -11.9907 | -51.1405 | 2025-09-12 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 20d3d434-149b-33f2-96c8-f04b761fd69c | -5.65979 | -43.8937 | 2025-09-12 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 37f7010f-6ea8-3bc9-b470-02bde23e2135 | -6.27344 | -43.66568 | 2025-09-12 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 78c7e637-3d85-3e86-a9db-c3934fdd7aad | -7.62186 | -46.5488 | 2025-09-12 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a5916414-2db3-33a2-934a-f6fa54b7dd1a | -12.88588 | -47.95531 | 2025-09-12 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c9721888-0da4-3385-bd8b-142f4ef3998c | -7.31759 | -44.16249 | 2025-09-12 00:11:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e39bc802-1dcc-3ee8-9a66-0a28e7a328fd | -11.48656 | -49.27068 | 2025-09-12 00:11:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 8ba3f338-c62c-3b49-9db1-e1431ee11135 | -10.33395 | -48.80367 | 2025-09-12 00:11:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 8f0ef22c-8220-342a-9a6a-6efb17ee24d6 | -6.21552 | -43.37763 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 4fd0f6c9-46be-3126-baf8-5041fda8eff9 | -12.59225 | -45.67989 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e79a6904-fb5a-3b51-aed6-13eb6e48c011 | -7.56875 | -44.37597 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 606d56a0-d7a6-34eb-a746-f8fe9dd2e68d | -6.8922 | -44.35345 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 80a6b72e-1601-358a-bb9e-b04b309d763b | -10.74308 | -48.17688 | 2025-09-12 00:11:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 1b4bb1d8-ad16-34c9-8641-456a689e6827 | -6.81969 | -45.65369 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 78dc0f53-8dfb-3d76-823c-00e7e9883cae | -7.17572 | -44.87548 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eb789ae0-8e02-36f6-8709-dd7c16c5fe3e | -6.20987 | -43.48314 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70d69a31-9de3-3ac0-a687-961f98744b1b | -11.69137 | -46.56285 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 26d6ff10-fe63-3fc0-aa2b-7fc8faccf171 | -11.68681 | -46.56975 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 163.2 |
| dfe9c00a-60d1-356c-a211-f931ff50c787 | -6.15753 | -43.3648 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cb997f98-49ca-30ed-b228-67dd87cb656b | -7.22097 | -43.98468 | 2025-09-12 00:11:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fd95c4b9-119c-3375-8fbd-a0781bbffff3 | -5.86039 | -48.1473 | 2025-09-12 00:11:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| db3dcae2-617e-3ad6-9b96-ed6dd6b8ac07 | -7.51897 | -44.68949 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 443ae79d-7c0d-3d23-9271-45791f6920db | -9.05346 | -47.03702 | 2025-09-12 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f88b55ca-fff8-30d3-9c31-571333dfe3f0 | -6.21109 | -43.49195 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 99df3a56-88b1-32a7-b2b7-a088ad0ff78c | -8.89495 | -49.92157 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 27fd1825-63f1-3148-b44f-513d4e2eaf64 | -6.24929 | -43.42674 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 4c37681b-89fe-3081-86d2-e757bb40b716 | -9.71504 | -46.88961 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9538d352-d182-3720-94e3-fbafe7fb8046 | -6.31099 | -42.2244 | 2025-09-12 00:11:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 37.6 |
| fa0281fd-0490-3eee-bb43-970b3b53c12c | -6.14872 | -43.36604 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a68e2e8d-9489-3faa-a9f0-af432e440295 | -6.29594 | -44.23609 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README4.md)

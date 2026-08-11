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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57a6d8b8-d487-3b37-a117-3d996bc08466 | -14.12805 | -54.00325 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe19baa5-28fa-3429-b46c-3be1588ebbc5 | -14.63313 | -47.66384 | 2026-08-11 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d46d36e-683e-3100-8497-16048f65c238 | -14.58248 | -46.16006 | 2026-08-11 04:36:00 | NOAA-21 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82f4e7ef-bccd-3b2f-bba1-96ad239e355e | -15.03031 | -46.58801 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8198827d-9263-33e5-9dfc-f4c6fb412b34 | -14.27986 | -45.3177 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9120d854-4973-369c-b826-32023fffccee | -13.85576 | -53.77958 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baad1e64-709b-3936-b625-e10ccc69888f | -18.49297 | -51.6707 | 2026-08-11 04:36:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 407c0b6b-9653-3b83-8521-23136a56d9d4 | -16.44636 | -46.68593 | 2026-08-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da50817e-df5b-3a7f-8e07-0bca56a5b22a | -14.28571 | -45.30347 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ba9a71e-d2b6-3857-af58-3705c9af430d | -17.45368 | -48.91024 | 2026-08-11 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc2e8171-c92e-38ca-8204-2dc2f8e402cf | -14.27347 | -45.30671 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e27a51e-5e01-3903-9323-16b6846a406a | -13.84412 | -53.69046 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 681d411b-79af-30ca-8fe1-2a95ae67c0ff | -17.13704 | -51.6546 | 2026-08-11 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e60f7ebd-c8f5-3897-9253-f14520c732c4 | -15.02667 | -46.58759 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ffa4c11a-8dfb-36d4-9110-bf7ae739950b | -13.83111 | -53.89825 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6248eae4-a106-30eb-9d37-6ec69357a64e | -14.46073 | -45.69234 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 604abbd7-05bc-38e3-9b2c-b662b549b281 | -17.45613 | -47.1492 | 2026-08-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 544d2198-b880-3106-958c-6d8606eaa948 | -13.86091 | -53.7948 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0026bfdd-5514-3338-99e3-1a3271a643a5 | -13.87255 | -53.77264 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c25e0a7-b522-3db6-9165-5e020a18fbec | -14.31199 | -54.92124 | 2026-08-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8861185-daa8-36e8-9ddb-5648928a11f4 | -15.00495 | -46.58404 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66315afd-6e68-36a4-bc19-bf3b5f0eb709 | -14.46315 | -48.96098 | 2026-08-11 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02562638-359c-30a3-bedd-ad2b5629bb34 | -15.00795 | -46.58905 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42b880a1-3320-3b0e-b3af-53f2b64f46d0 | -18.3958 | -55.54924 | 2026-08-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0e13989a-5611-3c34-b987-0dca7f84144f | -13.5095 | -51.80261 | 2026-08-11 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3dfb5bd7-5e12-334f-9801-4343aa8b86bd | -13.87469 | -53.78278 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ecb6be0f-df50-337f-9cc5-bfdf3ab4a2a5 | -15.98583 | -43.00714 | 2026-08-11 04:36:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f59d5917-8b0a-3f65-995e-39144ec87090 | -13.87551 | -53.77808 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8cae417-fa99-316b-bdc3-76c5854757db | -14.31327 | -54.9141 | 2026-08-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 343444c0-0d35-39d6-89bd-0b7a9c818406 | -15.00619 | -46.60149 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b9d3372-7c39-3d30-82d8-04c503fe38d1 | -18.49238 | -51.67439 | 2026-08-11 04:36:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68e25c96-6d5b-3d10-9ec7-3f0cf324677f | -14.76465 | -56.37105 | 2026-08-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bc6a4bf-a997-3129-a804-8d71c0221b36 | -13.63908 | -57.92857 | 2026-08-11 04:36:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aece267d-4670-358a-8a83-2cb2c2f69054 | -13.43973 | -57.04815 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 272479f2-cb75-375a-9175-e722729566fa | -14.99891 | -46.60069 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b0e7227-1f1b-32d7-b6a5-5b25b4101ef1 | -16.28417 | -56.59969 | 2026-08-11 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7f3f4b03-5751-37eb-bde9-373ea667a791 | -14.27667 | -45.31221 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af874a0d-82a5-33e2-92ae-27fe7f2dbd5d | -17.13585 | -51.66192 | 2026-08-11 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c1520e66-47d8-350f-834f-958c70d24dbc | -16.66117 | -43.63426 | 2026-08-11 04:36:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| b3b69852-7a93-37e8-a7d2-35aad0492b0b | -18.24747 | -42.38122 | 2026-08-11 04:36:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 07c1c9d3-0de5-3a1a-81b2-5250d06b7744 | -18.01461 | -44.41942 | 2026-08-11 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3391b718-82d7-3431-8d0b-7a9015d997db | -16.49113 | -54.65262 | 2026-08-11 04:36:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e997816c-3d8e-3a7a-8c00-5565d62ca200 | -13.87388 | -53.78745 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3090d38d-38cf-3253-9bdd-748f2d41f4f5 | -13.84493 | -53.68581 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 887520bb-2811-3f8c-bf09-8718356243b8 | -14.25959 | -51.96505 | 2026-08-11 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2228da3-e83b-3140-9b95-3da841655d43 | -15.52352 | -42.66809 | 2026-08-11 04:36:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 819df1a1-01ad-34aa-a244-5f82ff14a2f8 | -17.999 | -44.36896 | 2026-08-11 04:36:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cecb8426-8ec9-3c2c-be59-a35fb0d4d032 | -14.48119 | -47.98272 | 2026-08-11 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 693248c1-ffca-330e-8c80-6b3eb3fa6397 | -14.28118 | -45.30785 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37757bb8-6318-3f11-9fe3-778d7744908e | -14.4637 | -48.95739 | 2026-08-11 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 288b0fe0-74ee-3c2f-ad52-7d2402126612 | -14.24924 | -51.96326 | 2026-08-11 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa7c0a7f-cbde-3d95-a5f2-6892c186a11a | -14.47207 | -45.69402 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de3a94a8-3393-313b-a6ad-cb18c0b165d3 | -15.01156 | -46.58966 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9424d2e8-9093-3291-8d79-9f552f193512 | -16.27984 | -56.59885 | 2026-08-11 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9c853afe-7e37-333f-8268-8cb52b6e3e29 | -19.25743 | -46.45552 | 2026-08-11 04:36:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f38f636b-bb31-3bdc-9fd2-4e961b574f57 | -14.46322 | -45.70236 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0cd172ae-508b-31b3-876a-6e5e9fa0bdc2 | -14.2265 | -48.50895 | 2026-08-11 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e985d1c4-53eb-3ca8-8f65-1de6d0b0570b | -13.4313 | -57.04126 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 382247e6-8842-36cb-9889-d9bf4c1a1063 | -14.45318 | -45.69122 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47d5897f-2783-340b-9418-e09bc97de90d | -13.43506 | -57.04719 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59eab07e-5040-348b-b624-13ef70f7ffcc | -16.44927 | -46.68854 | 2026-08-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70ad6c8d-4478-3613-a5cd-751ea35a9b7c | -14.00432 | -53.98172 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 346a1c9e-4c1d-3f37-920d-16a163089cde | -13.42568 | -57.04548 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bd737e5-3697-3128-bb24-a6a5bb29320c | -13.83365 | -53.88375 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec6227e4-38cb-3aed-857c-d93482ac4ae4 | -17.04141 | -45.89512 | 2026-08-11 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f553b3f5-5af3-37e2-8f4b-5ed23b7af3a7 | -15.87166 | -50.13968 | 2026-08-11 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 688b5c00-9ecd-3906-9df6-28eaf6cd004d | -14.46516 | -45.68817 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 00f896b3-1897-3d87-9748-e715edf45948 | -14.12436 | -45.64042 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b579b55a-d44f-30a5-8940-8b1b162df4e9 | -15.03821 | -46.58454 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 915637d9-ecf2-3d83-bd5a-d240ba23f443 | -13.87686 | -53.7928 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04497b86-6cd0-3869-8966-19ea6b148187 | -13.86689 | -53.8053 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8adb607c-b6a8-39dc-aa36-5410a559d639 | -14.58319 | -46.16259 | 2026-08-11 04:36:00 | NOAA-21 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44a71e36-f133-3be1-9c5c-861f594b5459 | -16.66507 | -43.63935 | 2026-08-11 04:36:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 00316d5b-282b-3d78-b09c-de9100d5e3d3 | -14.63657 | -47.66437 | 2026-08-11 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fc14a16-da03-322f-b2a5-fcb45ecb09ad | -13.85197 | -53.77893 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e11dac89-2a9c-3346-83e9-422aa3c5fa87 | -14.61248 | -47.66049 | 2026-08-11 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfd5352e-abc3-334f-9623-3e46e224cd87 | -13.42473 | -57.05062 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4339c17d-408e-3353-b249-74f09c31ffd4 | -13.87091 | -53.7821 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f48b996-2d31-3c14-a376-7f655c73f496 | -15.03455 | -46.58421 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dd317aa-a694-340d-8fa7-5ea4cefdfd76 | -14.61936 | -47.66163 | 2026-08-11 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b36f0bc-8818-3327-b6c8-29313851da8f | -14.10544 | -54.02711 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a716add-7271-3b12-8350-827ce4862c13 | -15.01337 | -46.57685 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6086bad-faa9-3338-aed5-cbe039464571 | -15.00254 | -46.6011 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 413821b5-50e3-38a0-bfac-77eb0eb4f7f9 | -14.27601 | -45.31712 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf066daf-b36c-37b2-b6c6-fc82f3af320a | -15.77629 | -48.7182 | 2026-08-11 04:36:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35daee36-d1f6-3263-a8c4-c964669c2088 | -15.52979 | -45.91987 | 2026-08-11 04:36:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e01d89e-baee-315c-a575-d1887fe4d61a | -14.45511 | -45.67702 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f652fd83-cac2-3835-b730-b6b083bd2696 | -13.43412 | -57.0523 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 13064092-5afe-3855-8b86-513b641e7c09 | -13.43599 | -57.04214 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff4920ac-540d-3b1c-935e-234167b14658 | -14.99527 | -46.60026 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ee63022-ce30-3745-9057-06d6b696c50c | -13.865 | -53.77126 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47af361e-5365-349d-8abe-4e4f189b147e | -20.09796 | -44.31474 | 2026-08-11 04:36:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 613c1a17-0519-3d56-a7a5-3265a5021e39 | -18.4969 | -51.66761 | 2026-08-11 04:36:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbbe00c2-b5d5-3f84-b782-94fe253f159d | -13.86878 | -53.77193 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9dfed80-f504-346f-a02f-bf215c5690c2 | -13.8487 | -53.68643 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f86c77e6-a217-3d57-af7e-cec271107e4e | -14.28185 | -45.30291 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5c0cfba-4c42-3e13-bf85-23545b5e6f85 | -15.00434 | -46.5884 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24bcf697-baef-3c69-9da8-3837986da232 | -14.45133 | -45.67645 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9f26d16-4247-33f8-b183-85edd9965266 | -18.24678 | -42.38735 | 2026-08-11 04:36:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e0f18f86-c04a-3bd9-8172-57a7fbde8069 | -22.3465 | -43.04667 | 2026-08-11 04:38:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)

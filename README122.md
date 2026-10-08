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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea96bd9a-a36f-39c0-90ae-e5a3209c00c6 | -2.7797 | -54.0736 | 2026-10-08 04:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 6924dd13-a640-3f1c-ae8a-f2bc58c1823b | -9.0592 | -65.9209 | 2026-10-08 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| df063b5d-fff6-33a6-b632-eb1d454d5c05 | -8.6291 | -67.0296 | 2026-10-08 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 9538f748-e816-37e4-b4c8-4884e60ceeb4 | -8.6107 | -67.0116 | 2026-10-08 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7de7efc6-b2b4-33eb-bd89-9713ec489c0a | -3.5861 | -54.6741 | 2026-10-08 04:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| abe0bab6-3eb1-3bdd-bcfc-dcdf9f184b93 | -3.2577 | -54.0217 | 2026-10-08 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ed22079e-d4b0-3b57-bb39-b628a3c65408 | -1.5489 | -54.5556 | 2026-10-08 04:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 270411ec-abe0-3466-9bd7-d22f29fc778f | -3.3127 | -54.0604 | 2026-10-08 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 524759af-f368-3e8f-87db-13981db3ae87 | -3.1101 | -54.1661 | 2026-10-08 04:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| ea43039f-e5f1-39cd-bed3-03327505e865 | -3.11 | -54.1862 | 2026-10-08 04:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2481900d-0e0a-3cdb-9702-a1f6d915b173 | -9.0591 | -65.9396 | 2026-10-08 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 05ab050a-0e1c-3bc0-a3df-c35f9244c3a5 | -1.5306 | -54.5558 | 2026-10-08 04:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 2eaef3a1-595f-3026-85ad-0d4f79d7ae22 | -2.4987 | -56.1659 | 2026-10-08 04:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b9112aa9-5104-3ff7-b081-e3669cda63b1 | -8.6107 | -67.0301 | 2026-10-08 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ea96fd1f-2b4c-34b2-92e9-f9ffde41f1e1 | -3.2576 | -54.0418 | 2026-10-08 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f0b76172-6bd7-3661-827e-7dfc7826b807 | -1.5306 | -54.5359 | 2026-10-08 04:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b69e0c9d-385b-3642-af6c-4665f1a6ecd7 | -8.6292 | -67.0111 | 2026-10-08 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6d362eaa-6133-37ef-8f96-d521d8aad3c6 | -3.3127 | -54.0403 | 2026-10-08 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| eb835af5-0bd6-3872-ad02-17bf142c936b | -3.0913 | -54.287 | 2026-10-08 04:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 8d72a692-3e88-3742-aa4c-831fa4a16132 | -3.1114 | -53.7839 | 2026-10-08 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c5362e1b-5720-3fdd-b482-39f21665cd53 | -22.02415 | -49.57299 | 2026-10-08 04:51:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ae988bce-cdac-3d40-a868-a9c79c58d961 | -18.98739 | -46.57477 | 2026-10-08 04:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9255a514-fc48-3863-b9a0-d0ccd42e90f1 | -19.35739 | -51.5554 | 2026-10-08 04:51:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8e3039-d32d-3b30-aefb-b1eecd9a9842 | -18.09246 | -51.14733 | 2026-10-08 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a83c1b86-3eab-3204-9c00-aef4a8a677dc | -18.01616 | -46.20525 | 2026-10-08 04:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92760da7-fe73-3f0a-ad55-86650237368c | -18.90327 | -54.72594 | 2026-10-08 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d3ffea7-8bdc-3918-a4b2-3bd963f67d1c | -18.02091 | -46.20583 | 2026-10-08 04:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9de57007-6435-374a-940e-e7863c1c2e88 | -19.99727 | -49.0873 | 2026-10-08 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf0dd5ee-1cbe-393d-bea8-b0fd4875c0b8 | -18.72194 | -49.50902 | 2026-10-08 04:51:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc293666-d0a7-36c6-a497-e7ad46b8ecbb | -18.0304 | -46.20708 | 2026-10-08 04:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daef3ef8-ff9b-3b35-ba0b-68d947ec6ded | -18.71603 | -49.52386 | 2026-10-08 04:51:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb7fc63e-f5b7-3fa4-8070-a5302ad52802 | -22.99231 | -48.65647 | 2026-10-08 04:51:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f741a939-3f8f-3833-a3a6-c8c8794d6ae3 | -18.02565 | -46.20647 | 2026-10-08 04:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eb6d6a8-ce16-36cb-bbd6-246fd61c5d42 | -18.26683 | -50.52545 | 2026-10-08 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eee7abd6-fd94-3585-9630-96311c2a77dd | -18.98502 | -46.5739 | 2026-10-08 04:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 800894cd-63b6-3bb6-91db-0e6cf818ac42 | -19.99324 | -49.08666 | 2026-10-08 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51bd9d52-c293-3309-9a01-92005eabcafc | -20.74718 | -51.66075 | 2026-10-08 04:51:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 636ddee8-ec6a-3b41-98c3-7585fa85c580 | -22.02865 | -49.56968 | 2026-10-08 04:51:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6187950f-6afa-3931-8f9f-6f970917ab16 | -17.44603 | -52.00596 | 2026-10-08 04:51:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b2c1101-7256-331d-9214-75b1604593ed | -18.98682 | -46.58003 | 2026-10-08 04:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31df8211-639d-3486-903c-94a08b46e09b | -18.22356 | -50.02828 | 2026-10-08 04:51:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d61f0d4-3799-3831-b82b-7c76ce66bdd8 | -18.98909 | -46.57979 | 2026-10-08 04:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2d71a13-2ee0-3aa6-98f3-4706f6510873 | -28.9789 | -52.56217 | 2026-10-08 04:53:00 | NOAA-21 | BARROS CASSAL | RIO GRANDE DO SUL | Brasil | 4302006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b27c6567-600d-3792-b3bd-83a91e738d7a | -3.0 | -54.04 | 2026-10-08 05:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd09ab8-24c7-334f-ab00-a406b124df91 | -3.0 | -54.11 | 2026-10-08 05:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38926e21-9bff-3cab-a966-3b2c69828cc2 | -3.02 | -54.11 | 2026-10-08 05:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1e0d269-e4a4-3bbe-90be-748c5b5fb767 | 2.44119 | -50.8176 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3da6833b-3ab4-339f-83b5-fa2e9cdc3872 | 3.12778 | -60.64365 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b888c48c-f1e3-39f5-83c1-98a75ad8acf9 | 1.98785 | -59.93233 | 2026-10-08 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9999877c-48c2-3c50-b22f-7f0575573a62 | 0.73117 | -50.65907 | 2026-10-08 05:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6988cc1f-9ee8-3ee9-b55b-340a95fe6487 | 1.6901 | -55.64175 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc0b6205-359e-3876-b093-b6086f8c625d | 1.03869 | -50.02126 | 2026-10-08 05:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1537dbbe-7b9a-3653-96f4-4e086ffb1cae | 2.11823 | -50.82561 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a56a77b0-d41c-3396-97bc-9711a523189a | -0.08582 | -49.48179 | 2026-10-08 05:21:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26ad4da6-0c0b-32a7-9c98-ecb0edfd771f | 3.74304 | -51.6247 | 2026-10-08 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bb1409ab-e331-326c-89ad-429d6cb66a18 | 3.15784 | -60.61563 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82a70f16-e9c6-30b6-9904-b7a260f110e2 | 1.77247 | -55.54417 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5956515-7b6c-359c-a62a-1c561f5117cd | 4.2782 | -60.02398 | 2026-10-08 05:21:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 226c5823-fd97-34c5-808c-f8416d8169c3 | 0.92557 | -50.2614 | 2026-10-08 05:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2ae24a2-108b-387c-aca4-045d1a6abfef | 0.92084 | -50.25835 | 2026-10-08 05:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9167d6b-f2eb-3df0-a2a3-59e598c8f6f0 | 0.56619 | -50.79591 | 2026-10-08 05:21:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4ee98f8-27da-34bb-ad25-61050d486818 | 1.33947 | -50.82973 | 2026-10-08 05:21:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0a56f30-ccb9-3d73-85e2-195dceb87c8b | 1.05795 | -50.0338 | 2026-10-08 05:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9613170-7b4c-33a9-8b1a-4e65e9756eba | 3.07098 | -60.55461 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21169f36-9d7f-3524-8a38-36fb595ae091 | 1.69873 | -55.61578 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bcbea0a-dc32-3c59-b1b6-80916a4ea950 | 1.31413 | -50.84928 | 2026-10-08 05:21:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5427e924-f6f5-377a-a130-77ca413067e2 | 1.7425 | -55.59126 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05492003-16b3-3d06-ae86-a0932ce6a91c | 3.545 | -51.2784 | 2026-10-08 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33815b19-8871-3535-a25e-8e708d4ad571 | 3.31277 | -60.05385 | 2026-10-08 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04b20ccb-89c4-3cc1-9888-81f78e2d4903 | 4.27876 | -60.02767 | 2026-10-08 05:21:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac047f01-78cb-3185-a59c-dadf1b0a7f16 | 0.73174 | -50.6626 | 2026-10-08 05:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41324aa6-e739-3888-b659-2a5f16bd36aa | 3.07515 | -60.55396 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c61c6e65-0185-3295-9851-eb54b48deb65 | 4.31516 | -60.35223 | 2026-10-08 05:21:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32126731-da23-3b5f-a39e-1e96be088d27 | 4.31634 | -60.36004 | 2026-10-08 05:21:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b15168ec-7ed7-3a78-9500-b0552d120c9a | 1.36325 | -60.36892 | 2026-10-08 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9d2097f-0d3a-3cb2-8692-61af48965532 | 1.62001 | -51.06128 | 2026-10-08 05:21:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccf09439-f9eb-369f-8035-809dd5b5feac | 0.94279 | -50.19839 | 2026-10-08 05:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db33c3ba-3a69-3333-9207-810fb03b60a8 | 4.42886 | -60.93178 | 2026-10-08 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec3cf55e-57a5-3758-8eab-1eb55d8678eb | 1.77856 | -55.53968 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a7e80979-0f15-3ac8-87ff-0c6734a9b626 | 3.54572 | -51.28286 | 2026-10-08 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 217cebf1-30e5-309b-83ed-4f207679680f | 2.44137 | -50.82085 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2b3f3b0-9d98-3e25-aee0-2809e80fda24 | 4.08843 | -60.56157 | 2026-10-08 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b7661fa-8e66-32a4-af2b-49d906d212fb | 4.43744 | -60.92964 | 2026-10-08 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 138974b0-ab01-337a-98ed-5b4a8b549b6a | 1.7076 | -55.60732 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4fe2b87-21e1-3755-aa6a-ccfa988c924f | 2.12529 | -50.81937 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 395e2534-a516-3e18-90c1-c3a23b4e762c | 4.2712 | -60.033 | 2026-10-08 05:21:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fca04b17-f97a-3f63-9c9c-316319a77889 | 4.31574 | -60.35609 | 2026-10-08 05:21:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68f8dea9-dfdb-34e7-ba56-24aed2b5e454 | 4.31931 | -60.35139 | 2026-10-08 05:21:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6de0b192-c3bb-3755-b9b5-308b4a75fc2e | 1.65163 | -55.78569 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b1b7c59a-9818-3a5e-a3ca-89c05e1a2580 | 2.43728 | -50.81823 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 20a24877-0e22-30b9-a884-abf854935cf6 | 1.32205 | -50.84802 | 2026-10-08 05:21:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6979fa5-93d0-316e-b22d-d235df8357a8 | 4.44177 | -60.92883 | 2026-10-08 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d74a86eb-3bea-351a-9402-2d0a7bb24c37 | 2.43356 | -50.8221 | 2026-10-08 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ba1b5e80-9880-3505-9bfd-a1090dcdd09f | 1.71647 | -55.59887 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81a14ef7-f8c2-39c7-a806-841312ececb1 | 0.94111 | -50.19784 | 2026-10-08 05:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 191ea46e-6044-3cb6-98cd-bf12068704bf | 1.34459 | -56.13587 | 2026-10-08 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 368d12b4-e943-3fef-9f68-a9f2cc3319eb | 3.12739 | -60.64257 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b800202-abf4-3638-a0fc-de61612275bd | 2.12152 | -50.82317 | 2026-10-08 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7452962d-3f81-3d4c-a90b-2358065f89b4 | 3.12359 | -60.6443 | 2026-10-08 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8690ddef-ced2-307f-998e-ce30afe734cd | 1.74973 | -55.57246 | 2026-10-08 05:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README123.md)

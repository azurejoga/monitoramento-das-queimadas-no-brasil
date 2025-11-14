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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccf474cc-ff35-3df2-add0-872532ef2dcd | -4.32559 | -48.6382 | 2025-11-14 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e056932-1ab9-34aa-9395-d6743930093b | -6.88924 | -42.85142 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 557c6dba-563b-33a3-a1dc-11123f7e9287 | -7.14768 | -41.70651 | 2025-11-14 04:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 94c08c34-78e7-38c4-ae22-ee975024a842 | -4.70394 | -46.44714 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 98cbfe70-667e-32a2-a114-2e355e40214b | -5.52924 | -41.7529 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f8aac69-f2ec-348c-b2b6-21c1e384e473 | -17.54395 | -44.70313 | 2025-11-14 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ba6a46-0e6f-30bb-9dfe-defd9f261031 | -5.5792 | -47.10408 | 2025-11-14 04:25:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 719cb013-b2ba-399e-a302-79291f62c1ba | -14.70149 | -46.61244 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a352c565-a608-3bcc-9940-59b535ceeef8 | -5.5379 | -43.68196 | 2025-11-14 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd54fb1f-d041-3d96-a536-568e02cf4a31 | -6.07948 | -41.62591 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dbbc1a0a-8c39-3e8d-ab9f-b2ced3a33c79 | -7.11807 | -42.72297 | 2025-11-14 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af919a9b-48f5-3e15-9a6e-fb4dd78eafa1 | -5.74349 | -42.72569 | 2025-11-14 04:25:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 41b18595-002e-3707-8adb-eab5019848e5 | -15.65026 | -46.16952 | 2025-11-14 04:25:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9863ba86-587c-3865-a6ff-855fbf213b77 | -6.13631 | -48.05253 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a3bc581-324d-31cd-9fc5-88eab2a91bb9 | -4.77956 | -47.88308 | 2025-11-14 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca8e6415-5733-349f-87dc-549bd304878f | -5.31016 | -47.49353 | 2025-11-14 04:25:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ec25adf-98d2-3691-b847-99f9eeebb0c4 | -11.6033 | -45.11688 | 2025-11-14 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5eae55d8-c252-38af-b5d3-f0bb17e29dd5 | -5.09504 | -47.692 | 2025-11-14 04:25:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2989c8c-f1cf-342e-b9f2-ac99415daff5 | -6.06681 | -41.56504 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75a0cbf7-5fe6-30eb-96ee-0f6b384fa88a | -11.92482 | -46.19617 | 2025-11-14 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 103b6e50-8c7b-3047-8d75-f90d1f136f8d | -5.52213 | -41.75182 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 86977a79-f31f-3d8b-b2cf-7bd5fceddc21 | -15.30282 | -47.38162 | 2025-11-14 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ceca84b-abb6-3f29-99b6-716387e94fa4 | -5.30081 | -45.07443 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60970c80-45cf-34b0-8207-520a5d925ddd | -6.07892 | -41.63741 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 87f63aab-9fee-316e-bca7-2db485a158e3 | -4.56036 | -46.68793 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7507b139-c218-322d-8e3c-3e149b02687b | -6.28433 | -41.73216 | 2025-11-14 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43e310a0-32a6-311e-b333-30cd80a73116 | -5.52364 | -46.37205 | 2025-11-14 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6ae4ec0-84c9-33cf-a542-61e986c4d055 | -6.111 | -41.5709 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cf47b3fe-2518-3701-abda-f0335de92961 | -6.88341 | -41.58451 | 2025-11-14 04:25:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d802050b-d248-380b-84c7-73ce220217a4 | -12.66518 | -46.75005 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8ac6922-86fa-39fd-a97b-2e43ce1fb8cc | -10.33942 | -49.92037 | 2025-11-14 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd2b9acd-fb44-36cd-b073-3f6e5551c7a1 | -7.36953 | -41.74361 | 2025-11-14 04:25:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97a0f086-8a76-3c8d-af0f-3fa8b3dbb750 | -3.84655 | -50.20677 | 2025-11-14 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8e22b3f-03f2-3aa9-bc00-d905c589f9b5 | -13.4713 | -46.49354 | 2025-11-14 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 490e1771-03c0-37d3-9f67-bd6f837125b8 | -15.2531 | -47.94407 | 2025-11-14 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f853c094-a1b9-3fef-beb3-d1dfc342a6f5 | -4.77781 | -46.45121 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 129b7833-bb19-3d37-a176-42579f6bc607 | -4.81385 | -44.87589 | 2025-11-14 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51d95ff5-e470-38a7-968e-8ffab0b9237a | -16.963 | -52.38307 | 2025-11-14 04:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ed57051-eaba-3473-939a-f29325a22799 | -14.39205 | -43.97896 | 2025-11-14 04:25:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd04dab4-a651-3e68-91ae-1b745f77178b | -7.14913 | -41.27794 | 2025-11-14 04:25:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 665a372a-0872-37b2-8af9-8134afe4f934 | -11.74382 | -48.52758 | 2025-11-14 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc360454-aec5-31fa-83f2-940558e818a7 | -11.74734 | -48.52818 | 2025-11-14 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 035f9f48-b240-3b03-bc5a-7d22e4fc3cdc | -16.2388 | -45.6379 | 2025-11-14 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1dd02ff0-5f26-321b-b122-1de1bc64e63e | -4.75876 | -44.45915 | 2025-11-14 04:25:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f46a6e7-aaf3-3df8-aeb5-eeb48a1fe79c | -5.54147 | -41.8157 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7c5da2f0-1e23-3571-bd14-b34e6ad426a4 | -12.00518 | -46.76937 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a22ef30b-2956-3676-aaca-10db464fa27b | -6.15544 | -48.0509 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7d4cc57f-28be-306f-914e-6fea3c38f6cb | -5.13162 | -42.59953 | 2025-11-14 04:25:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19f8a5a4-db74-3615-b19f-e3200beca775 | -6.43782 | -45.66487 | 2025-11-14 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53a1001e-157f-3b8e-80ba-029c627881ed | -12.71261 | -45.42508 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 833fd023-9d69-3516-984b-18b60a608ecb | -12.09363 | -46.47409 | 2025-11-14 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad483434-d6b8-31e1-b0cc-e389cbb1f961 | -11.73392 | -48.52176 | 2025-11-14 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5608dd9f-5a36-36ff-af80-49fbac03cfcb | -17.9833 | -42.9284 | 2025-11-14 04:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1edbb07-654d-36b4-accb-2e6883bbb4cf | -6.0632 | -41.56451 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ba45eab-536c-3b4c-a461-4a6d8367d8b6 | -4.21582 | -49.1189 | 2025-11-14 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 79375671-0103-3a06-a845-86ada1d62c71 | -4.77709 | -46.44651 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31d2a24a-3336-3d00-945b-2eb3fd19dcc9 | -4.6991 | -45.67731 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46caab92-80fb-37ae-b276-fa36b534c650 | -18.32318 | -46.65111 | 2025-11-14 04:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 026810b8-8f5b-30d7-bad3-3306b7ea2a82 | -12.7026 | -45.42347 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 355c5071-e5dd-3ca2-800d-b383c451b638 | -5.7522 | -45.10293 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e30b9ac5-fc8a-3713-8ce9-9f0af263c354 | -6.08494 | -41.62178 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b41b10e6-cc5d-3841-ba79-5af05b8bb921 | -15.07623 | -46.46204 | 2025-11-14 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa39db99-c347-3db8-96dd-6cc34cf7c24a | -3.86574 | -50.92686 | 2025-11-14 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c6b165d-5551-33bd-8c55-8ef621801ac5 | -6.13786 | -48.05038 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 769fd419-bad8-39a6-b81b-1a374b2693d2 | -10.81016 | -48.12748 | 2025-11-14 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1000cbd7-a5e4-3ef0-838d-d386d9093b1e | -14.98833 | -42.41338 | 2025-11-14 04:25:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 64761987-5279-3f51-8ce7-7562cabb8097 | -5.75553 | -45.10347 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 342a0cf9-a740-324f-bf9d-d830592883e9 | -5.4953 | -42.16442 | 2025-11-14 04:25:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94b4dfad-c2e7-34a9-8f7e-80923098670d | -6.28311 | -41.74029 | 2025-11-14 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34d7cde9-483e-3eb0-a1b9-dacc10edb404 | -4.73123 | -44.73477 | 2025-11-14 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2724032b-6ed7-314b-845f-c04b4a7ead57 | -13.72789 | -49.13227 | 2025-11-14 04:25:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9df3dfe4-88c7-3c00-afca-65620d4f289e | -3.60537 | -54.71537 | 2025-11-14 04:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7df303c8-0c14-38f5-b37b-f90d33058de4 | -6.90416 | -42.08776 | 2025-11-14 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3fcca11-c8c1-3257-9ff4-841c6c5df30d | -4.63366 | -45.16248 | 2025-11-14 04:25:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d72fde7-3b12-3fb2-8209-20ec75683809 | -5.49441 | -41.9108 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bcaa6b5a-7d11-3d43-82cb-c7ee544f3bd7 | -15.54867 | -43.17618 | 2025-11-14 04:25:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e807d14c-1c85-36bc-ba00-5ced7b947351 | -5.1601 | -44.66036 | 2025-11-14 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f7b844b-4f24-3143-81c2-b82763fe6394 | -16.24161 | -45.64216 | 2025-11-14 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4101de83-ded0-3de9-97d6-b16746ea7165 | -12.62256 | -47.01427 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3365e078-a805-3228-8767-85ba46fea787 | -4.97723 | -43.09583 | 2025-11-14 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcc99b08-ce84-3b29-9382-c2d3cadf9fd0 | -5.42557 | -46.08889 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c4689f5-9a04-318f-8b86-730c6d387ba5 | -4.96088 | -49.566 | 2025-11-14 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7546db52-eac2-3444-ade7-66bb24152904 | -6.41014 | -39.74943 | 2025-11-14 04:25:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ca661fdc-934a-337e-b208-11042ae5510e | -14.67834 | -46.56467 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4ab73c3-87b5-3510-b9ef-8080fb13d697 | -5.75721 | -42.72761 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 84402c5e-716f-30b5-a0bb-1b8f059a5efb | -14.13941 | -44.20504 | 2025-11-14 04:25:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07fc8075-eb91-3ee4-89f1-31128686528f | -4.60998 | -46.55781 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2b2a130-875b-3a73-be19-98a2304ca72d | -3.41167 | -52.73058 | 2025-11-14 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ca500ec-d336-3e47-8ebc-09f1f8545c44 | -5.98015 | -42.5936 | 2025-11-14 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ca33bb17-5b6f-3dee-8e78-44fe2dce1486 | -12.66908 | -46.74705 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 929e3e4c-040f-31fb-aab6-e77e03e604fd | -6.72009 | -42.95518 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c90f5f31-f4b1-3cfe-99c7-da98d22b4a9c | -11.99169 | -44.21681 | 2025-11-14 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c90c8270-5b9c-33dc-9a51-0842abd4f7d6 | -5.46021 | -47.1019 | 2025-11-14 04:25:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04208a8a-de38-3c00-9d57-39b2260362dd | -13.76614 | -43.16506 | 2025-11-14 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc8fc38d-3542-3db3-814b-a4fd8d2c064a | -6.23939 | -46.24271 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b57aa012-608e-3568-91db-ab9f9484b1ba | -17.20907 | -47.65297 | 2025-11-14 04:25:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b581fe93-3132-37f7-92ca-40b50e0b3933 | -5.33674 | -41.85934 | 2025-11-14 04:25:00 | NPP-375D | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f0e2d5d7-7ab1-3655-8db8-8a7d86257ce3 | -6.89177 | -42.07365 | 2025-11-14 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bf628543-47b8-3ada-9aec-1aa68c38dbc8 | -5.97479 | -42.76442 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5e9c5888-7a8b-3a4b-a463-724fa689bf86 | -11.24615 | -47.50088 | 2025-11-14 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README35.md)

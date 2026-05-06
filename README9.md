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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 083b035e-9f67-3bd3-8693-6c127ae2d100 | -21.70841 | -48.41955 | 2026-05-06 04:55:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 363c165d-3915-3e68-a038-012ae2309ae5 | -16.75673 | -51.87084 | 2026-05-06 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85f32fbf-47b1-394f-a1d4-308ca8042d7c | -18.43502 | -54.706 | 2026-05-06 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| af14640e-fcc3-34a2-aa7c-c2c8a88047cb | -18.78518 | -51.93509 | 2026-05-06 04:55:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 137da77a-f916-3c89-aadd-1e09d8f09c46 | -21.29763 | -56.10718 | 2026-05-06 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb58c4e6-0cd3-361c-9a10-7590aaf0eb6c | -16.63847 | -50.13854 | 2026-05-06 04:55:00 | NOAA-21 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47e86918-2d95-3b5d-b9cd-7573c2f2ffd1 | -22.609 | -49.56447 | 2026-05-06 04:55:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b493078-8398-38ae-a94a-5f014b9024e7 | -21.29821 | -56.10349 | 2026-05-06 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bf62779-b253-35a9-bd59-6a7118600d38 | -22.8033 | -49.3423 | 2026-05-06 04:55:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e82e2c04-1c4a-3eb1-9e37-bb454f999878 | -16.49246 | -52.72344 | 2026-05-06 04:55:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd643555-8405-3712-94cd-a0c14489f13c | -20.20734 | -50.64639 | 2026-05-06 04:55:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d53ff603-a352-3c31-90c8-bb1667c9b5c1 | -18.78215 | -51.93008 | 2026-05-06 04:55:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c6c13d7-a9c7-38ff-9950-b8cea759d421 | -20.21062 | -50.65241 | 2026-05-06 04:55:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 978de872-3a3a-354d-9e96-bb59e365dcea | -20.79662 | -51.65626 | 2026-05-06 04:55:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| 2e7f7d69-19c6-3017-9e5e-f4434085bce5 | -16.5979 | -58.23715 | 2026-05-06 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7c856351-844b-3c91-8596-ed57db51cfde | -16.11144 | -49.23289 | 2026-05-06 04:55:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37afa101-db89-3343-912b-5b68157c82ac | -16.16313 | -58.4914 | 2026-05-06 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 735ebecb-4d35-34c9-8d92-dba6770726e0 | -17.8084 | -46.71518 | 2026-05-06 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4c299ce-3229-345f-bf3f-ebf850078cf6 | -19.94668 | -54.38128 | 2026-05-06 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e69123fb-a74b-3c17-a162-b5f0e34fee6e | -18.07493 | -46.36987 | 2026-05-06 04:55:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b19b142-40bc-3157-84b9-4a93b0b49f57 | -16.63837 | -50.13976 | 2026-05-06 04:55:00 | NOAA-21 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef5a6737-9ee0-3ef6-b61a-4e1f15daf4b5 | -18.50011 | -55.51416 | 2026-05-06 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9aa6832a-2c2b-3fdf-9b88-fe49a29cbce6 | -18.50068 | -55.51054 | 2026-05-06 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fbc19822-0013-3115-bdae-1674eb633c37 | -18.48709 | -51.68483 | 2026-05-06 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5a5a4d5-3c89-3722-9755-cc33e9b4eb8a | -21.97807 | -57.58986 | 2026-05-06 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7ed3b3d-b1c7-372f-93f0-5264f9fba3c1 | -16.42784 | -54.91553 | 2026-05-06 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 38361a48-e700-3e67-9f48-adc116ca19f9 | -20.53267 | -49.24614 | 2026-05-06 04:55:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 07dcf748-1255-326f-828d-7982b4aafd4d | -18.4339 | -54.7133 | 2026-05-06 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 012d6bbb-4717-3efa-b777-b993b17bb351 | -18.43446 | -54.70965 | 2026-05-06 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 014e4fcf-f42b-3c65-964d-7f6f30c78763 | -18.43834 | -54.70655 | 2026-05-06 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 64d4e97c-5aba-36de-87fa-525c51273d58 | -18.50399 | -55.5111 | 2026-05-06 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5a4b2a45-7a0b-38ac-8e5b-b143414549d7 | -19.95004 | -54.38186 | 2026-05-06 04:55:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06ff5484-6ac7-3992-9d0e-e57c752b436a | -16.7603 | -51.87135 | 2026-05-06 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8deaf59a-0c5a-3f2f-adcf-bdc91255b742 | -16.4284 | -54.91194 | 2026-05-06 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00711528-f49d-355c-a815-6badd53fd25b | -16.59715 | -58.24155 | 2026-05-06 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 76ef07e4-7385-33ed-acce-e1f1d23502a7 | -20.7145 | -52.08102 | 2026-05-06 04:55:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c1bd504-43bb-377f-b7a8-afc6f37fda5f | -23.56052 | -48.5724 | 2026-05-06 04:57:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7637cccb-b3ec-3805-98fb-3aa49bd79323 | -26.87746 | -52.83473 | 2026-05-06 04:57:00 | NOAA-21 | ÁGUAS FRIAS | SANTA CATARINA | Brasil | 4200556 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 74cd046f-b584-3ee5-babd-04d89761fb09 | -12.5033 | -58.4781 | 2026-05-06 05:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b2dce021-7844-32d5-8c07-0e8276da1542 | -12.5033 | -58.4781 | 2026-05-06 05:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 05af7d6e-54a9-3ecb-907a-a530204fb56b | -12.5033 | -58.4781 | 2026-05-06 05:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ae4329dc-0d2e-31c5-9d0c-1f83a2c7d812 | -5.78931 | -45.12801 | 2026-05-06 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c982a81-12ec-329f-9cc2-3b4b76901c67 | -5.79024 | -45.12106 | 2026-05-06 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01b8300d-b0b0-377d-a440-d773cc327f2c | -5.78795 | -45.12616 | 2026-05-06 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10b2823b-68ee-3421-8975-de8038fe9e97 | -5.78893 | -45.11922 | 2026-05-06 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dc57bee-90a2-36ec-b84c-6295541ae41c | -11.30044 | -54.02844 | 2026-05-06 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24bf9f47-5f58-3335-90d3-b8835a4ca0fc | -11.63839 | -54.16597 | 2026-05-06 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34a46148-2bb2-37de-a442-f54c9cf975be | -10.48572 | -49.36029 | 2026-05-06 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02fd49f6-bb35-3784-b4c9-4dc63bd4e595 | -12.34595 | -54.75937 | 2026-05-06 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcea6723-a539-38ed-a07b-097052e412c8 | -11.44129 | -55.10172 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55452f42-f430-39db-b7fe-8ac322e8380b | -11.63897 | -54.16178 | 2026-05-06 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e836005b-60dd-3836-b0ed-7b9a7ac39e5a | -12.12234 | -54.66978 | 2026-05-06 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c3b0493-0488-3af0-a853-90dcdf00caed | -12.34844 | -50.01556 | 2026-05-06 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db2574ab-213b-3f36-b060-07ed0071952a | -12.345 | -54.76184 | 2026-05-06 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f39d1c07-9771-37c7-a555-62e39f1ffe05 | -11.4683 | -55.11687 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 347b2d9e-81b1-33e3-b615-f669e994bc63 | -11.43361 | -55.10427 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e3c8e95-72fc-37bf-9519-a6948cd8e497 | -11.61574 | -48.06176 | 2026-05-06 05:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a601922c-997b-301d-b295-372989aeab17 | -11.61641 | -48.05628 | 2026-05-06 05:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3c1cbcb-75ba-3fb6-ba5b-3b0bc64456b0 | -11.43722 | -55.10112 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e71d3d48-043e-3b7c-a80f-dd91dffbb444 | -9.72302 | -60.2037 | 2026-05-06 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d4b9901-f7ae-334a-b873-c44f19cf933a | -11.45301 | -55.1072 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7827a8d-2b1f-3805-827f-d08343e04ef9 | -11.46066 | -55.11205 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6ea6aea-d9ca-34c6-a02e-7c12be09085b | -10.48517 | -49.36455 | 2026-05-06 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 170dc1ed-5470-30b4-abbc-4b8c8639cd93 | -12.34796 | -50.01964 | 2026-05-06 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa332992-37bc-3d29-ab5c-9897767ee400 | -11.43768 | -55.1049 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8c61ecb7-153b-3893-a189-bd45e1261c7d | -11.2917 | -54.02723 | 2026-05-06 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e21d738f-403c-31fc-80bb-1356d7b084be | -10.48848 | -49.3623 | 2026-05-06 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 994bda2b-e352-351e-9f02-773317cd8aff | -12.38799 | -46.32444 | 2026-05-06 05:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 747ba24e-0674-38dd-88fc-9af63e9fdf79 | -11.55116 | -48.27118 | 2026-05-06 05:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 366835e7-7b1c-3350-954d-a048f626032b | -11.45658 | -55.11145 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24ce6fcc-2976-3b1f-87c4-7c2dee4aa303 | -11.43821 | -55.10126 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14e0c49a-2819-338a-82a3-1c07736680a0 | -12.46133 | -54.44835 | 2026-05-06 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4016967-8451-33fe-8555-20856c8f9f4a | -12.35279 | -50.0286 | 2026-05-06 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 115d37d9-48f9-3810-8187-02eda0a3b660 | -12.34313 | -50.01062 | 2026-05-06 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d58e6bae-a01a-3978-a5de-c1ea1d221b09 | -11.29607 | -54.02782 | 2026-05-06 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aef71746-6e18-3278-8be0-35f6154af13d | -9.47051 | -47.80291 | 2026-05-06 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 365eac31-0cd7-3c19-a05e-810af7402ef6 | -11.44894 | -55.1066 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e73a5bb-41f3-3ae4-abcd-f0823dd84cc8 | -11.61599 | -48.05766 | 2026-05-06 05:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bad1fc3a-f335-3c10-bfcc-9a5a0eb310ba | -11.44228 | -55.10186 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c45e2163-736a-316a-8c13-e90edf110af0 | -12.34264 | -50.01472 | 2026-05-06 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 815bd62b-c286-3b85-ae7d-c59f7fb3d588 | -11.44175 | -55.10551 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 47439424-488a-34bd-bd0a-a96f0df7a772 | -9.83172 | -56.3474 | 2026-05-06 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ffd1dae1-fc96-3e0f-b460-c751cf15e383 | -12.39521 | -46.3257 | 2026-05-06 05:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0f2aea8-70ff-3bbf-8ec3-8c890d6e2ac2 | -11.55757 | -48.27207 | 2026-05-06 05:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6912a78-9549-35e9-8f69-039914458c50 | -11.55221 | -48.27279 | 2026-05-06 05:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eca37345-93cf-3c1f-ad93-d6712e5bd2b9 | -12.34747 | -50.02373 | 2026-05-06 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0328970-5049-304c-acd3-e693af5541f0 | -11.46423 | -55.11629 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff9b1588-cb5d-3272-a2b1-d38503c46444 | -11.44537 | -55.10232 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d96e137b-b781-30e5-9a0b-d5326bb29ff8 | -11.60926 | -48.0608 | 2026-05-06 05:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40dae31d-ce7b-3688-a7b1-a0e880a0893e | -12.12657 | -54.67043 | 2026-05-06 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b936f47b-698f-3b1a-91d5-168ef27d2f6a | -11.44079 | -55.10538 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4e170e19-5479-3055-a91e-a32acebcea8d | -12.38981 | -46.32336 | 2026-05-06 05:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb1ccedf-fd7e-35d3-af97-64e0d1111fc9 | -11.60888 | -48.06215 | 2026-05-06 05:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84a2f27a-0384-3f04-b814-0ed0799853ab | -11.63403 | -54.16543 | 2026-05-06 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60bf66de-56e9-3140-9958-a61d0d639696 | -11.79674 | -56.96163 | 2026-05-06 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9829ecbd-a245-38e6-be43-be205faf6765 | -11.43672 | -55.10476 | 2026-05-06 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30468036-50fb-3300-b205-38e89b4c0763 | -9.46986 | -47.8081 | 2026-05-06 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 900d8c00-ee1f-36ca-b8bb-060a941f7370 | -10.48258 | -49.36139 | 2026-05-06 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7030de2-f620-302c-bd5e-facea1e28d17 | -9.46343 | -47.80718 | 2026-05-06 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2437511-38df-3a83-a375-aff967a1fcd5 | -14.08466 | -47.63297 | 2026-05-06 05:27:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README10.md)

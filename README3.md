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
| 2ca7cec4-9413-39eb-a812-1579ce4f4b14 | -8.90335 | -47.77018 | 2026-06-08 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd8aa8b2-633d-34be-982e-835ea7776ec4 | -12.48511 | -46.26329 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c95bf465-f57e-33a9-b665-e700b30fae88 | -7.31845 | -47.06424 | 2026-06-08 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37498ae9-5da0-38d8-9949-7dc5e480ceeb | -10.47661 | -47.93145 | 2026-06-08 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ed6f1a3-42ce-31d6-8d97-c642524b528c | -12.5194 | -48.28992 | 2026-06-08 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb72bf1b-0f77-3c1c-80a7-4e125d3085bd | -11.03559 | -48.91296 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00c0f6d6-d190-3548-96f7-943ddf390130 | -9.34116 | -49.14819 | 2026-06-08 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f664fdd-5a94-345b-bd4a-685fb693bf80 | -14.02836 | -47.38359 | 2026-06-08 04:34:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b1ca19a-093d-3648-86fb-f46c5bdabf74 | -10.9025 | -49.34668 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8990df92-9846-3346-b6f5-578bda20a309 | -12.8509 | -44.39202 | 2026-06-08 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cb0568eb-c15a-3572-a5a4-072cac5026d4 | -12.22714 | -51.3444 | 2026-06-08 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5daeb7be-310a-3e52-ba84-3a8b74dedb9c | -12.07033 | -48.42562 | 2026-06-08 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7179ed83-c1c6-3e8c-9b25-f37cf961edb3 | -12.48811 | -46.26751 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8d106e0-7815-3478-b7c8-5949e0b07349 | -10.86033 | -53.73381 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa59bade-d783-36c3-b74c-23b0a0511b53 | -7.31181 | -47.0632 | 2026-06-08 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ea1cda0-5dbf-333c-b6d6-dc3c1643382b | -12.85188 | -44.39067 | 2026-06-08 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6de2a874-2835-3e2c-927a-c2bdd7c8b16d | -10.9047 | -49.35424 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef264778-5707-3a21-9c6b-e8568cbf8248 | -8.98963 | -47.85117 | 2026-06-08 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1194bb0-fa68-31e7-accc-5be1d6e96be0 | -12.5116 | -48.27409 | 2026-06-08 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8f5f62c-1326-35b1-8692-178500429bdc | -12.48548 | -46.26082 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33fde6bd-196d-3a66-a0c0-e05d828ad96c | -6.91287 | -51.16383 | 2026-06-08 04:34:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee648e11-13a6-382f-88d1-c7eeb841c11a | -10.857 | -53.73951 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df44663e-df96-3192-81cb-2ea77fd6c861 | -7.89906 | -47.09272 | 2026-06-08 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf7351e8-9493-31f0-b22a-fdfd6f406f18 | -8.99016 | -47.84768 | 2026-06-08 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d766a946-f841-33da-8093-7f245de71426 | -12.49409 | -46.27621 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba2bfeef-9e08-3304-8be1-5189c973d36b | -12.32027 | -46.07685 | 2026-06-08 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8f5fffc-bd35-39f6-bc58-dc073a549110 | -10.85972 | -53.73727 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b418ef4b-7aa6-3114-9ff0-ca70271a2109 | -6.46693 | -46.89605 | 2026-06-08 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30398784-f567-311f-9564-b8c3c4b157c8 | -11.84688 | -52.51334 | 2026-06-08 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a988b29-7126-3cd1-a9a2-45483bfb7282 | -9.41455 | -50.67508 | 2026-06-08 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 733d00b9-0137-39da-8d76-c384a6c4ce99 | -11.3405 | -53.97601 | 2026-06-08 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9c8bc94-fbe2-3e54-b346-bd31dd4b0e30 | -12.49352 | -46.28019 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2844e274-95d3-32fb-8766-3886d88424d3 | -8.90389 | -47.76669 | 2026-06-08 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34607cd4-dbd3-3dcb-859f-1eb4fe76b3b7 | -10.90526 | -49.35073 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d89692c-f56d-3b1a-a317-767d8cc10149 | -10.38228 | -47.32276 | 2026-06-08 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 119d4a53-c9f6-36d2-9af4-b40d662cc380 | -10.3864 | -49.44704 | 2026-06-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43e85b66-5d8f-3126-a0f2-7cfa97d38472 | -14.30375 | -49.24496 | 2026-06-08 04:36:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 89b7f53e-4c2a-3cbd-8167-5e78fe1a396e | -14.73784 | -52.68443 | 2026-06-08 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b599eae5-4b79-378a-9fc0-06ca34cc8180 | -14.97424 | -47.78584 | 2026-06-08 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dce55228-f50a-30d5-ad77-1daa1e8550b5 | -18.46296 | -54.70307 | 2026-06-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afffc86b-4bc0-3712-a0fd-56c70b250627 | -14.35009 | -58.45125 | 2026-06-08 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f755f99-a20b-35c3-b4f0-5d9b59688fa6 | -14.35072 | -58.44808 | 2026-06-08 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5eaf211-30c8-3495-bf46-c2ef31f5e5aa | -20.6326 | -45.21807 | 2026-06-08 04:36:00 | NOAA-21 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef9fdab9-de52-3b0b-8264-ad0539a08fd1 | -15.23998 | -48.56788 | 2026-06-08 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b6cfe29-a347-3ea6-a259-425754d14dd1 | -20.32461 | -47.7345 | 2026-06-08 04:36:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6e3f0c0-2cb8-3b2e-987f-cf0ca672ad1b | -14.301 | -49.24088 | 2026-06-08 04:36:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bcc1be9-c211-3b56-81f1-05b7a08888dd | -17.10918 | -47.18734 | 2026-06-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 766099ff-e5aa-3577-aa56-4d3f94da558f | -14.73706 | -52.66713 | 2026-06-08 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d07d10d-eb5d-37d8-9e2b-be9e9759a91c | -16.66352 | -49.44296 | 2026-06-08 04:36:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06d4e707-a067-3af7-95c1-481b5bb65dfc | -14.33381 | -58.46673 | 2026-06-08 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 028f9ec2-a919-328b-ad6e-c5fdf393d974 | -18.46671 | -54.70378 | 2026-06-08 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d6c7b8d-4794-3aee-8f08-1fc760c596cf | -16.39413 | -49.93488 | 2026-06-08 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d8d109b-bc72-3545-bfa1-e6c7c4f84197 | -14.73428 | -52.68377 | 2026-06-08 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dea625b3-0ae9-37b4-b6a7-045c86930b13 | -14.35278 | -58.45077 | 2026-06-08 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e50e7707-ac40-374b-a2ac-6a86ebbf327d | -14.33319 | -58.46995 | 2026-06-08 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be794317-13a3-3d77-b1f6-d3d8e7e9c252 | -14.73568 | -52.67542 | 2026-06-08 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1c7e1cc-df69-3e83-9bc1-1c6ef74b1a32 | -14.73498 | -52.67958 | 2026-06-08 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3375dca6-74dc-3c05-baa6-d902d0a98824 | -14.32993 | -58.4593 | 2026-06-08 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1717a83-12b8-3893-801d-15fb67b999a3 | -14.33443 | -58.4635 | 2026-06-08 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b2a9e25-b1ac-3770-a49d-3096aecbdd57 | -14.73854 | -52.68023 | 2026-06-08 04:36:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79b89493-db99-339f-9432-c589057178ae | -14.3043 | -49.24142 | 2026-06-08 04:36:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4fc4919-1416-321d-9f9e-cf6b32dae338 | -14.34769 | -58.44965 | 2026-06-08 04:36:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c182147-50ea-3834-bfe8-835075bd7d6e | -18.91238 | -47.43705 | 2026-06-08 04:36:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50a5699b-0bcd-366c-a616-523e00556e34 | -18.91298 | -47.43275 | 2026-06-08 04:36:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08a43faa-5d88-3550-9251-edf7d286c563 | -14.30045 | -49.24442 | 2026-06-08 04:36:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 36a5b6f5-7235-3f5f-b324-544e1e4f14e0 | -20.3282 | -47.73505 | 2026-06-08 04:36:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 477cd2ac-9381-39e6-81cb-5ee72cf78d45 | -18.90878 | -47.43656 | 2026-06-08 04:36:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8618313-b5e9-305f-8036-ac700d639ba0 | -14.97473 | -47.78511 | 2026-06-08 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69127415-6671-3958-99f6-4ac8485077b0 | -15.99257 | -42.22766 | 2026-06-08 04:36:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0981cb3a-d3de-3d6c-a0d2-51d257cbfcb0 | -19.54537 | -45.31464 | 2026-06-08 04:36:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 135cfc33-e45b-3fc0-9722-ca99162fde57 | -21.98875 | -57.61201 | 2026-06-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 98a56133-c229-3290-9c6f-a9fce1d101aa | -21.98458 | -57.61101 | 2026-06-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d986109b-e65f-390a-8eb4-62f1994cefce | -21.99295 | -57.61295 | 2026-06-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbe32149-82a9-39cf-a350-4ba01341ea1b | -21.98952 | -57.60808 | 2026-06-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ddc41662-f22d-33c9-b7d1-729c6a68cdd2 | -21.29649 | -49.0434 | 2026-06-08 04:38:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| b4bf0879-0c7d-38bd-866c-32d7a0ed2299 | -22.38545 | -49.78802 | 2026-06-08 04:38:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 150c2c8d-25b1-306e-9092-badc55575645 | -21.99371 | -57.60902 | 2026-06-08 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ab5aeacb-0b82-38cc-95e9-6fd7d4a9be87 | -23.8246 | -48.71279 | 2026-06-08 04:38:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c11dc17a-7b25-3cbd-8970-50bcd97038c2 | -23.42969 | -51.45023 | 2026-06-08 04:38:00 | NOAA-21 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf4925b8-da7c-366d-be0a-7206048551f5 | -22.36029 | -50.64132 | 2026-06-08 04:38:00 | NOAA-21 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 602f6fc0-1e65-3f2c-807e-8f603a7347c1 | -20.89838 | -48.96138 | 2026-06-08 04:38:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 76a96b9a-106f-3bc1-9006-a56acf1626b7 | -23.239 | -46.65042 | 2026-06-08 04:38:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fac33990-229c-3ac4-951e-8e0d16a6e972 | -21.3062 | -49.0415 | 2026-06-08 04:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.6 |
| a9b21a20-2b28-3d10-b16e-ae2de8587314 | -3.49633 | -48.03923 | 2026-06-08 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 336b98a7-65a1-3aa1-8e24-a85732372dff | -3.49691 | -48.03533 | 2026-06-08 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d409dae3-a98a-399e-97a4-0940defd96ec | -2.65437 | -49.2165 | 2026-06-08 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3fa67480-6b0a-3d2a-871f-a83870fa6a8b | -3.49384 | -48.03625 | 2026-06-08 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 06062f8f-85f5-371c-ad6a-313dccac8a99 | -3.49807 | -48.03703 | 2026-06-08 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2ce742dc-7dd5-3df0-b29b-12badd085876 | -3.49446 | -48.03228 | 2026-06-08 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48e48f86-5504-356d-8656-cc0b5f6486b5 | -12.06974 | -48.43018 | 2026-06-08 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d60fc621-9d55-33db-9535-143e1f2a7665 | -11.08707 | -48.26829 | 2026-06-08 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3bbfb352-4836-3e0e-8c81-8bc6bf03eedc | -10.84927 | -53.74288 | 2026-06-08 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8301d7-3497-3650-8138-5f3e76533a42 | -11.08499 | -48.26662 | 2026-06-08 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 731756c1-a2ad-3fff-9232-6f412ebf69f7 | -10.82497 | -56.60311 | 2026-06-08 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da586da1-515c-34b4-ab67-d7a2644f78e0 | -10.9025 | -49.3491 | 2026-06-08 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f6527b5-b52f-3688-87b0-253c493d945d | -10.82555 | -56.59951 | 2026-06-08 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f5ec80-1045-30cd-87ad-6ad8608b68e0 | -10.57097 | -57.32304 | 2026-06-08 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 816d7e07-1b06-36fc-a16f-e261d769414c | -6.84749 | -47.90749 | 2026-06-08 05:08:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ddc4464-e34e-3cb1-afea-df91c0eafa7d | -9.30799 | -48.966 | 2026-06-08 05:08:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6194ec9-aa3c-3b47-9773-9b3688fb8beb | -9.25057 | -48.238 | 2026-06-08 05:08:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README4.md)

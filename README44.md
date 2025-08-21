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
| 3c00061f-c627-325c-9c6d-4fbc608fdb7a | -10.40302 | -59.37647 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c07e912e-8ad7-31d2-8120-855e95080dd2 | -12.90632 | -46.09459 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baac8609-8063-3688-a28c-c03141b15933 | -17.34058 | -47.15745 | 2025-08-21 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3872d9ec-5885-36df-b51d-e56460276c26 | -14.46353 | -48.36697 | 2025-08-21 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8abd3225-71a7-3b86-981a-bb3b2e500df5 | -13.33384 | -54.40071 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c59ef3b0-e516-3c0f-b375-845d27544d9f | -14.05879 | -43.53549 | 2025-08-21 04:40:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd2cb777-de99-30a4-85ff-422459a3e020 | -13.15293 | -46.90589 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38cbeb40-62b2-3983-8071-85ba47be84d0 | -13.0294 | -45.21285 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4aa5b76b-c486-3955-8351-da1a7a5df8d4 | -12.94548 | -46.18122 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72b1de3f-f30c-3052-b653-d604e9be20c3 | -13.53506 | -47.04465 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b09acfd-edbb-358f-9ba4-5b817383d27a | -8.86861 | -62.40455 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| cb186fa8-677d-3b57-b1dd-68d01be732df | -11.32141 | -55.21631 | 2025-08-21 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff0fe204-1bc7-3717-b3bc-c986bfcdc2fc | -8.37372 | -54.99761 | 2025-08-21 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 053d6853-9773-3cb3-813e-ab51211bdad0 | -9.35023 | -50.25687 | 2025-08-21 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1abe8919-91ac-3774-bddd-6356add401b6 | -14.8474 | -47.94897 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7fc74be2-fd1f-3345-9423-823fbbd3b41b | -10.45879 | -48.80734 | 2025-08-21 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d66cf6c-83a8-3a9a-b62a-a627f9ca525c | -15.57057 | -50.32242 | 2025-08-21 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4e5cb3b1-1327-3ce1-8109-f77777e9d32b | -16.10496 | -48.01018 | 2025-08-21 04:40:00 | NOAA-20 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 812470b9-aa32-3ef4-a989-37e291767bec | -15.00243 | -54.84861 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ef74d8f-5f04-3e54-a363-2248c1912d7a | -13.02 | -45.18715 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 143b8159-398e-321e-b5c2-a0c6b8baae33 | -10.28533 | -46.76384 | 2025-08-21 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94917c20-1008-34cf-af84-e61dc8dc5bd6 | -13.33022 | -54.40009 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb1f1b35-9034-3ed6-a348-cc3d170e18b4 | -13.53937 | -47.03778 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 34378e9a-7809-384e-9d5f-855e5f4250c5 | -13.86955 | -54.06284 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3495a80-d4d7-3899-8adb-d1d8b3293ca4 | -9.91245 | -62.14888 | 2025-08-21 04:40:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ffc5a1b-e3db-3c09-8665-dd6d1813c144 | -13.02479 | -45.18372 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d21e3433-7d5f-3e50-949d-33a840683e3b | -12.95271 | -46.24564 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59cb4631-ef06-30ab-9b79-c1831221169a | -11.1759 | -46.13899 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d8208e4-03df-3da4-b163-ebd25023ec8d | -14.65695 | -54.87205 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 51fd575d-e42e-3084-9ab5-ffc103709d23 | -8.37431 | -54.99408 | 2025-08-21 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a642f85c-43e4-3497-8805-d6300eba221e | -15.00318 | -54.84423 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b5b78c1-c70f-330f-9f52-1041a341e282 | -13.32584 | -54.42587 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14ee3363-136b-3ed8-bb3d-60c8e5d9c808 | -12.8919 | -46.08156 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f22cbc1-a1b6-3269-ae2b-652194e3fe57 | -13.02219 | -45.17115 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 7b10c600-33be-39b4-a75a-7225bbec5601 | -11.17662 | -46.13403 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eff64e0-13e9-36dd-befd-c75ab059763e | -10.27923 | -46.77975 | 2025-08-21 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b672cc95-38e5-3b2b-a652-268a1db7dc16 | -13.01372 | -45.16994 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 9af8fb77-1d2f-3374-b900-19fc5962eaf6 | -12.95812 | -46.23576 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 637d02d1-0ac9-3f40-989c-2d78a64a0f25 | -10.71803 | -48.22975 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07f9a406-3e78-35bc-aec8-7617430de471 | -8.83747 | -52.06153 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7128d846-3bee-379b-95f2-6ac35cb49d92 | -12.98184 | -45.21432 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5131f0b8-50b1-3400-bbca-6bdb4f4c94ec | -12.49513 | -49.89788 | 2025-08-21 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4ecc51f-0ce3-3518-965b-3e24a0318826 | -13.58954 | -47.0115 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07d02a4a-27b4-3ca0-a6c6-daf65c95e3b6 | -12.64029 | -46.87691 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b504bd96-f4b4-3886-b0db-bd6a2c5546f0 | -15.51178 | -48.04877 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 416207d6-52be-3be0-a80b-09a43dbf5d49 | -13.03437 | -45.17683 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1231933d-461e-3032-9887-b4b01c51cb2e | -11.35666 | -51.2497 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cccaf15a-bca5-3116-8d98-9cc94efcf420 | -13.03418 | -45.20947 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 05bc7a5a-fc15-3ce1-b5cc-95f7ea8a6c90 | -7.5427 | -63.85203 | 2025-08-21 04:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4679f7e9-e16e-362b-8b74-751a6018776a | -14.85228 | -47.94091 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0989b94-4b13-3ea1-8b00-20f64cbb792f | -13.65136 | -45.71437 | 2025-08-21 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57ead0b0-8943-3236-9f86-7c8ebe550812 | -14.5726 | -51.93777 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c79a2be2-0fda-33a3-9219-a54dc7d495c5 | -8.85898 | -62.41943 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5a124a2b-ecee-3c92-be2b-00ffe048dc49 | -8.86221 | -62.40307 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| db8b6c5f-d030-3f91-9c65-fe2496f33da8 | -9.69882 | -47.93877 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e46ff20-b72e-3d86-bab5-4b1ade548a0c | -11.51914 | -50.54463 | 2025-08-21 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ecaf174-4e50-37a0-9fa0-db371f97eb4c | -9.55605 | -48.11746 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07992f4b-cdf5-3516-a66e-9f7d6c594d34 | -15.57786 | -50.31975 | 2025-08-21 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ad44c3b-fe00-37e5-aaeb-568d16998371 | -13.54265 | -47.04577 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ac9c4a8-eea0-3e54-a861-ec7d2b67e13b | -14.64741 | -54.88377 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8cb7920-3613-3f57-834b-882fd50b805b | -12.63723 | -46.8712 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77c8e6ce-761b-34e4-bbd1-5531b8ea5bf5 | -14.36934 | -51.97692 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7e2c2fa-1067-35cf-8c9b-3a87ac38eadc | -14.12467 | -45.39114 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78cdc0f1-c3e7-3c2a-91fa-b69c358074d7 | -13.33817 | -54.39709 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b3d6970-5b02-315e-900c-d5c7d0d8d767 | -16.04641 | -54.64359 | 2025-08-21 04:40:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62430523-4625-3e8f-a462-3d68dc2f749d | -13.34902 | -54.39901 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7584d6e2-62f4-3591-bf67-218ab615de0e | -9.66258 | -48.38361 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 561383e7-45c7-3791-a693-379957429483 | -12.9494 | -46.24048 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97aba9e0-a9a2-3255-b122-e778429ff1bd | -11.81036 | -44.25964 | 2025-08-21 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1eae6aa8-3e4e-3e12-8453-03dde07f5819 | -8.87504 | -62.40588 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 185cfe5d-f6ba-3d45-811f-310798c289e5 | -15.92162 | -52.21211 | 2025-08-21 04:40:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e708e36f-dab1-3d51-bb6a-8af422e2c3d7 | -14.53658 | -51.90991 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eaa58e92-9663-32c1-a8a9-8fb2f46c0362 | -13.53885 | -47.04521 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6990149d-ebee-3dd6-9092-610370591544 | -13.0288 | -46.82677 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b39c8472-8447-3604-a646-bb58f60d71ca | -15.57169 | -50.31498 | 2025-08-21 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed74dfbf-fdf0-3492-8a7c-d6623a4304f6 | -8.85822 | -62.42197 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 24.7 |
| a8f63751-67e5-3519-ae72-66ec34a83c90 | -13.03535 | -45.20083 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 937e43d3-9b80-33ca-9d44-9c2f2270f3a6 | -13.03695 | -45.18939 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1a3c2a0-449a-3d5e-bc77-d8f0382aa2c6 | -9.91224 | -49.24523 | 2025-08-21 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 882fef1e-ec5f-3e7d-b001-7ab2e9a766c0 | -15.03244 | -54.85178 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b30c9b3-53e3-3c11-813d-bb09dfd647e8 | -15.428 | -46.71466 | 2025-08-21 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a19dfa3-807e-3d3e-b265-9d410c8266da | -13.01427 | -45.16594 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30bee011-a808-3a26-ae3a-ee28226471e5 | -11.81478 | -44.26026 | 2025-08-21 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 733224ec-7017-30f0-8daf-39f835ce5d0e | -13.01154 | -45.18594 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b6cb9ac-1cdc-31ca-9200-7f62e26cc67a | -14.12255 | -45.37431 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08695c3c-9c96-3e44-b788-40a5a6e9601e | -13.15854 | -46.89349 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ea4354c-1421-3d54-b827-5d0b10fe563c | -15.0163 | -54.83293 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f703aee-0477-33f2-a177-1237f0e8669f | -13.1491 | -46.90551 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8296f9d-4bac-37e5-9d7d-8a83bf767a1e | -13.04286 | -45.17789 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c2a1a24e-4fbc-3908-95b1-00eeda48b554 | -11.63518 | -51.59008 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2d85c3c-9000-350e-acf4-148d5dbb8e19 | -12.64099 | -46.87197 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f647fedd-6cca-355e-8152-5ae6ec5ea3e3 | -15.19514 | -48.69878 | 2025-08-21 04:40:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecc54b41-7fde-310a-9077-9a78c5d90603 | -13.18344 | -46.90987 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e5b6355-f6d3-3d98-899f-2c4e9cb218b2 | -13.54879 | -47.05369 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d863a71-270c-369f-81ef-661e24df403c | -14.90043 | -48.0741 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7d9cd54-0535-3749-a9ec-c26ed1962eaa | -12.98237 | -45.21036 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf183f48-930d-3f6b-aaef-4d183943f973 | -10.57946 | -49.16498 | 2025-08-21 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 071717d0-944b-3942-970e-1f07925b89df | -14.62788 | -54.86639 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1f6a785-968c-31a2-9d85-5a5720522ac9 | -15.88607 | -49.00983 | 2025-08-21 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2e7c093-93ff-3bd3-9384-0babf52f540d | -10.98726 | -55.23814 | 2025-08-21 04:40:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README45.md)

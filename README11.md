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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a229351f-c203-31a8-894f-16e28f998897 | -6.76076 | -63.03946 | 2026-08-30 00:48:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 41fe9dee-4f3e-300c-92fe-ae96169b96d5 | -9.88632 | -60.26816 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ab0e79af-94cf-3cf8-ae00-e8a770916660 | -9.01985 | -65.40453 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 3a881098-b719-3b25-a1a1-0f931154e138 | -6.65569 | -59.4399 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 94af3ecd-c1c1-3e6b-bf82-ef00ee1ceb86 | -6.88737 | -59.44393 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f6e22896-d87e-3a4d-8edf-52ee776ac676 | -9.93061 | -60.52686 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e919fe0-7c05-3daf-82e2-044d1de044f3 | -5.98266 | -55.72828 | 2026-08-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c1735593-6fe5-3ba8-9821-6e62cadbdbcc | -7.236 | -60.62995 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| b684003c-f32c-3826-b9de-d555e9687023 | -7.52287 | -55.32572 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| eca3c7bc-1441-3604-b24c-b9f81a888015 | -6.77173 | -63.04864 | 2026-08-30 00:48:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 62a7ad99-58a8-374d-9745-ec604f74851a | -7.33793 | -55.16092 | 2026-08-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 99ae7549-68a4-384e-a47c-296dc8ca2395 | -9.71131 | -60.73571 | 2026-08-30 00:48:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0a069dff-ca04-36bd-a53a-343cdeed087a | -6.93626 | -55.71873 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 265.4 |
| 64d9e121-a51f-34a6-9ed1-b2670a349478 | -5.87396 | -52.09737 | 2026-08-30 00:48:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 9b127b6c-8f39-3393-82d6-fa533e4ab973 | -6.84236 | -59.45633 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 43178dae-e752-3f7a-8e4e-88278ae686c1 | -9.01296 | -65.4117 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 07384c59-e278-3925-b0c4-58a32d09dc7c | -8.57976 | -66.95914 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 0d40de5d-1293-39b2-a756-ee31c725054f | -2.90827 | -54.11323 | 2026-08-30 00:48:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 8d71018e-9d96-3b9a-a5cd-3f5edc323986 | -7.23479 | -60.62112 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 21315916-cfcf-3229-8dc2-0e9e30f7366c | -6.78057 | -55.67375 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 58cbe283-2178-397b-8b61-0c3d9fed720f | -3.93825 | -59.32512 | 2026-08-30 00:48:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6499ef8f-25e9-3b3c-abc5-0ba17276eaaf | -3.64849 | -61.70487 | 2026-08-30 00:48:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c90739e3-e7d8-3101-aa61-e87dbf16d4af | -7.06502 | -59.73263 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8fae5529-bac4-3ca3-adaa-417243d958eb | -6.84362 | -59.46537 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 64444262-c61b-39d7-a186-f94284b11d25 | -9.84223 | -60.27443 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e7f32e68-3af0-332c-8c9a-7c4bb00701d3 | -4.6979 | -55.67508 | 2026-08-30 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c4a357f7-c3ca-3784-b32d-275e27a14b7a | -5.87294 | -57.77316 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| dc4b0cdd-3099-30c1-8980-0700023567fa | -5.97235 | -57.68521 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| fefd4b8f-9340-36c1-86bd-852b763bc168 | -9.15465 | -59.51026 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 508459cd-80d3-3a9f-b707-32e2fa3f4cd8 | -9.66583 | -55.10292 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 8facc83c-8205-37db-9321-ee16af6786eb | -6.70968 | -58.57014 | 2026-08-30 00:48:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a656b314-b162-3a39-a7ce-1f2482e8ae51 | -9.05521 | -65.40009 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| a482ac4d-91c3-35c1-8065-24384be463fa | -4.95375 | -55.84862 | 2026-08-30 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 61fff115-3854-33ea-9256-4ecd967b5847 | -6.86574 | -59.4839 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7cb91767-9217-3da8-9179-a6f9359d7f3d | -5.98819 | -57.79441 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3eac70d3-f74b-334c-afca-1cb840b82e4b | -7.30804 | -60.61342 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 12c23aac-fb27-31e3-b053-7239788a4a28 | -5.86943 | -57.76849 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 047b1f23-1ec5-336c-ae40-4acea1c8628d | -7.5582 | -61.30914 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 488e75fd-294e-37bf-a371-7b096810df56 | -6.64291 | -53.1812 | 2026-08-30 00:48:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0c512ad7-bb64-37a3-9f9e-1e974dedd9ec | -3.93957 | -59.33463 | 2026-08-30 00:48:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7058e978-6008-3d38-9e81-68a4416da856 | -10.47908 | -64.50919 | 2026-08-30 00:48:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3f79efca-2db5-3bb4-ab08-4920e70f3f4a | -5.88266 | -57.77175 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 294e93f0-00eb-3cdd-9d8e-e2b90efb15a4 | -7.30683 | -60.6046 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ef172482-04c1-3a35-b141-18203c8119c8 | -10.48817 | -59.60716 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| d288090a-094b-3606-8aff-439fa449848f | -7.29924 | -60.61466 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3ccb0200-d89a-3160-ba05-2a08301e687f | -7.5725 | -61.33788 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9016c4df-b5a1-3261-80b2-cd5b75bda71e | -9.17186 | -59.63474 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f2ab4f0f-678a-3079-8502-3ab5598e9eb8 | -7.2448 | -60.62871 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5585b1e4-d294-387a-8945-fce854cd3825 | -4.15529 | -60.69761 | 2026-08-30 00:48:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d5e31b93-dfdd-3112-ac6b-11d60a94a1c1 | -9.88757 | -64.99323 | 2026-08-30 00:48:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 55bbaf72-959d-322f-8e4b-b47219601e0f | -9.16818 | -59.60809 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 45217b0a-510d-3bb8-b3fe-61ae1826c8af | -7.32442 | -60.60212 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 624900bb-02ea-3bfc-b0cb-a709bc9adf61 | -6.95879 | -55.70862 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| bb2bfd52-78a0-3430-8a19-22df6683252f | -7.52511 | -55.34083 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 82af40ad-8f20-33fb-be93-a542098c4f65 | -5.89084 | -57.75967 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 31731376-7723-3c41-b607-2d41464dc75d | -9.64809 | -58.93777 | 2026-08-30 00:48:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1cb18061-d6e6-3780-8c7a-d460d88bf689 | -6.89121 | -59.40643 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3ff6191a-8c27-38f8-b78c-1c2dc40d3b25 | -6.76217 | -63.04993 | 2026-08-30 00:48:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b9b585bd-7527-366f-b656-18f2f6b39437 | -6.80023 | -59.6093 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fdee1348-c995-3d40-9fce-f3af0df102b3 | -7.4052 | -60.58485 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9c1d5743-f849-3ae3-aafc-5148ecfb079b | -9.67249 | -55.07197 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e74d0e2b-8155-3f45-b48b-0b9a811c564c | -9.89599 | -64.98576 | 2026-08-30 00:48:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 57d0d8e4-09b1-3e5a-a129-1b4eb07a3c87 | -8.61295 | -54.7711 | 2026-08-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| e1e016a9-596c-340f-8f62-fe3ab3bb07fd | -9.18348 | -59.63585 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 577c8200-0a51-36d5-9e75-cdb0b9ac71b9 | -9.01083 | -65.39514 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 19f5dc01-63b8-36f9-9846-c2cf4060729e | -9.88754 | -60.27708 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 13ae991d-0ee8-35ac-af36-6abda6ebaef8 | -9.93947 | -60.5256 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 8faaba95-389c-31f8-98cf-c624572da1af | -9.00541 | -65.44647 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 8a9c553c-1772-3aa0-9346-1697edf445e0 | -10.57135 | -59.60738 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 9585d856-4a50-319c-9cfa-579f6c6d9de5 | -4.95419 | -55.85775 | 2026-08-30 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3c01d1bd-abbd-3cb6-89cd-3d5e84c97605 | -5.87454 | -57.78408 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 7ccc37ef-1f51-3d1b-86d6-4b34f32f1511 | -7.01848 | -59.65728 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e35389cb-a5c5-3a71-8713-7a60041dd808 | -7.32563 | -60.61095 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fcd09d3a-c87b-3c1a-bb69-97d1b9e62a53 | -10.50336 | -64.52119 | 2026-08-30 00:48:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f1d96ba1-862e-308f-8a9f-d6af781539b8 | -9.85105 | -60.27318 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 5301d91e-672d-3c60-a03b-48006e7e4df9 | -6.99829 | -59.64199 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ced27cd7-77f9-3784-84a5-45ce14352ca1 | -5.86186 | -57.56018 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 983e862f-64c6-3189-81d6-2866ce2c67fc | -6.94523 | -55.70235 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4811f70d-8ecf-30a1-8aa7-fad4315d9444 | -5.48573 | -57.15333 | 2026-08-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 74984938-caa1-3af5-bd2f-4bfe04ab6d55 | -8.50743 | -55.29025 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b25009a5-b239-3d03-a030-a137030ae287 | -6.91272 | -59.49558 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 342b126d-436c-3eb4-b307-685c11c88b46 | -9.16617 | -59.51141 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| cfe98d88-ad8f-338b-bec9-cffb6f00f4b5 | -8.95687 | -62.39949 | 2026-08-30 00:48:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 385482e4-0d84-3548-85e9-6e7af83979d1 | -7.8414 | -62.31555 | 2026-08-30 00:48:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3be4bec3-8d67-35fa-9247-526a7cf296af | -5.87165 | -52.0909 | 2026-08-30 00:48:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 0a4aff4b-68c5-31f8-a796-7e1c5ef1e446 | -3.48679 | -54.6659 | 2026-08-30 00:48:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9e280634-0092-3dff-b7ec-ca741d5b393b | -8.65676 | -62.83996 | 2026-08-30 00:48:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4494d075-c252-3579-bf52-7080c9b2b085 | -10.55218 | -59.61606 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| db9952a3-b999-38e5-b362-5654fd828da5 | -6.79755 | -59.71931 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a70ceccb-431f-3e74-bab6-e2e2600a0e65 | -8.2292 | -61.42808 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e5cc7e73-8587-3972-b5b5-e7486366d844 | -6.16206 | -57.78958 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b1a1652c-a6d3-3146-a417-a38852a8c054 | -7.49795 | -55.31425 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 6265da91-c5e4-338c-a70a-2f7ad81e85bd | -9.79026 | -59.43921 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ac2cb58a-4bb0-39b8-bda6-024a998b6206 | -3.63919 | -60.55832 | 2026-08-30 00:48:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 11273689-a4f5-30e4-a9c1-444aee43ac66 | -8.63431 | -66.54358 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 693e674b-4678-3f41-b882-2489dd5c0b46 | -7.33485 | -55.15588 | 2026-08-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 786da690-be06-3a78-9a6b-2ab2033bf01a | -8.63883 | -62.85327 | 2026-08-30 00:48:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 1308c28a-bffb-3dc0-82c5-5198892c735b | -5.88427 | -57.78278 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| e46dab2d-ab08-3a9c-9e24-be3601d65cf6 | -6.86447 | -59.47488 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f90feacd-6d8e-3046-b848-70fa3f18aa07 | -3.76558 | -59.34249 | 2026-08-30 00:48:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |


[Clique aqui para ver as próximas entradas](README12.md)

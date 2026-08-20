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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dca0043f-f600-328b-bae1-115a5ee281e9 | -3.10398 | -61.22044 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 255d5849-e2e9-3f79-8605-3891cfc1f20a | -6.7989 | -59.58386 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30e54e75-b4e5-3850-955f-5ece00a07e60 | -6.59176 | -58.96372 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba39c89-8ca5-3cbe-8c93-645d39318918 | -3.09743 | -61.19384 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d4051a1-ff13-3d43-9a91-e694f9f4d091 | -6.85816 | -59.0322 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42f99b33-c1c4-3f24-80a8-b84e06816257 | -6.13251 | -57.87833 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70e0d8ef-5877-390c-8a64-9d00b596c001 | -7.53277 | -55.58251 | 2026-08-20 05:59:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20724a07-447f-38bb-bc8c-b0980b6468b4 | -6.69615 | -58.93867 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 93ca5dae-d61c-3b62-916b-9f4f3b428ac4 | -3.09946 | -61.21976 | 2026-08-20 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f329f75-7bfe-3690-9678-d093b1695d8a | -6.69706 | -59.09528 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2eec884-4ba2-3af0-a82a-f1648df16ca3 | -5.80514 | -55.72907 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4971ad60-05e0-3aac-88d4-5135c4636175 | -6.38763 | -54.94186 | 2026-08-20 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5767482d-ad20-3d0c-b7ac-b52970a4dc94 | -7.53266 | -55.57574 | 2026-08-20 05:59:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99950af3-32fa-3715-b49d-615c9535f461 | -6.76838 | -59.14979 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 667b2a20-4359-3ab1-8e07-fc3449c5df13 | -6.58975 | -58.97822 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13ff16f4-99e8-3be5-a313-759c8c7fa0d8 | -7.09993 | -59.7691 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef44fc4e-1036-3269-aa8c-c85846d89b3a | -5.80592 | -55.72323 | 2026-08-20 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b6bb21e-a48a-3645-905b-c89f29d1063c | -5.49366 | -60.13353 | 2026-08-20 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 373706d6-0c6d-3ce9-bd75-a399495b7f10 | -6.92072 | -59.35374 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d1a0da50-5f40-3e7b-aae7-9541b323da2b | -6.84005 | -58.99978 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e01c407-1469-30ed-9c9f-eeee9e5e14c0 | -7.10524 | -59.76987 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc98d682-4451-3a53-96a0-d612bc452379 | -6.09032 | -57.92111 | 2026-08-20 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6934d53-3b72-31fc-9786-363594c308fb | -6.57862 | -58.9768 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6b24409-8de6-31e9-aae7-32a9462df0b4 | -6.38301 | -54.94857 | 2026-08-20 05:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 884062bb-806a-312a-ae9a-f5a7d3ff5f41 | -6.7474 | -59.18012 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5460ac2-6466-36f8-8ca7-2bbfa9ff2fdb | -6.74307 | -59.04601 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b4c98b6-669b-37bc-b412-6fabd7f13e9c | -6.79 | -59.58578 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21792f6a-31b7-3ac0-b305-04be17c1a5fe | -6.87034 | -59.02633 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e6410ec-2a2b-3bec-a3cb-eb36f359f47e | -4.39151 | -55.47716 | 2026-08-20 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2612d44e-9a48-3b99-9137-5375c552aa97 | -6.70917 | -59.08922 | 2026-08-20 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 984c9046-1765-3cd8-a196-3b7b52bad667 | -17.3365 | -43.6383 | 2026-08-20 06:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 4a833364-7ae3-3d1b-aae3-a8500c189e5d | -17.3372 | -43.6139 | 2026-08-20 06:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a9aae5bd-3d72-3c4f-a9fa-24e7f725d7d0 | -9.21553 | -60.7792 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 109be0c7-2b93-392f-9270-ba007239232f | -9.39327 | -60.56541 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3b78fe7-0612-3721-821a-1167aa8e0657 | -9.11922 | -61.60693 | 2026-08-20 06:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb619e43-8ab5-3d00-b7ba-5e2415823baa | -8.28936 | -62.90131 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da1c884-e293-37e9-9445-504c979c53fd | -11.82712 | -58.83578 | 2026-08-20 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 23920d25-ad11-3f4a-b962-7c9a257ad8a5 | -11.83313 | -58.83657 | 2026-08-20 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bdf0cce0-0006-3f15-a653-927e4ce55be6 | -8.285 | -62.90066 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66c22b1a-43a0-35f8-b24f-da394f87fa53 | -9.15691 | -59.55611 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b072ed0-5d19-34ed-94f0-493f766c9403 | -8.28995 | -62.89708 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67569043-3c89-3bb6-88e4-175ec4c79f5b | -9.38848 | -60.56163 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8234ee96-ab02-31f4-96e2-f9eb594c6ab8 | -9.38976 | -60.55215 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8222127-8edb-3fd7-9d5e-317b13d4d7b4 | -9.21041 | -60.77856 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0c3a650-def5-39f8-af83-05955069861c | -7.8672 | -63.76508 | 2026-08-20 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3871256c-4538-369c-84bb-840bfe687f9d | -13.43499 | -57.06311 | 2026-08-20 06:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98ea4449-67d9-35cb-bd2f-9f863a6d4ded | -11.82111 | -58.83496 | 2026-08-20 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 785bad54-1402-35f0-a683-3a0fee479a1c | -9.10346 | -60.93377 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5dc6016-68bd-3f98-9222-45c6174f1dc5 | -9.08127 | -65.38326 | 2026-08-20 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2355085-d0fa-3188-8a4a-ff7db501f79b | -9.10386 | -60.93079 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2e8d54b-e441-36f4-8b50-2a489f51d7b4 | -11.82657 | -58.84038 | 2026-08-20 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f6b7f671-65b5-3ee4-a9f0-95e2aadcc968 | -7.87537 | -63.76628 | 2026-08-20 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 220bf94e-0f63-3aee-8c90-a119a20a9ab2 | -9.17894 | -60.83499 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1000849-88d7-3631-8714-9214d772cf88 | -13.44117 | -57.07027 | 2026-08-20 06:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d81fac7a-446b-3d63-82d5-f25215f9f84c | -8.64433 | -62.8355 | 2026-08-20 06:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66717b3e-e83d-34fe-81eb-dcf14f73c709 | -11.8381 | -58.84607 | 2026-08-20 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c415372-d691-353f-8357-b67e6beece24 | -8.64616 | -62.82262 | 2026-08-20 06:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04ce615a-861d-321c-81fd-df50031c3c7d | -9.02299 | -60.49832 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c91b3b1-da70-3ffc-be37-42928f28c9ea | -11.83259 | -58.8411 | 2026-08-20 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e8244d8-f4d3-369f-895f-8645c3497b44 | -11.83205 | -58.84561 | 2026-08-20 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 031d0124-6f78-3d1c-b16b-913f628eb32f | -9.40018 | -60.55347 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d72ef179-3cdc-3511-831e-4b6449e3e91f | -9.10426 | -60.92781 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 57cae9b0-9531-3743-b43b-7009b4b2995b | -9.38891 | -60.55848 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af34e024-43f4-36ed-9a03-2f2f523b7a56 | -13.43946 | -57.07623 | 2026-08-20 06:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b529f5c5-6a5e-38cd-8c23-cb56f3b8b286 | -9.07731 | -65.41065 | 2026-08-20 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bab876e-d27e-3017-b3d9-148dee91b059 | -9.08017 | -65.38496 | 2026-08-20 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ac64b9f-ba0a-3cf6-84a4-54e1500b12cd | -7.87129 | -63.76568 | 2026-08-20 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9597ff6-e159-35b6-98e4-feb29b17b88c | -8.4033 | -62.69818 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a011d4c-b2b6-3204-bec7-51f51d446c2c | -13.44054 | -57.07635 | 2026-08-20 06:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37d3550d-0395-3023-bd59-a7ebb8c4cadf | -10.39838 | -61.20432 | 2026-08-20 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56ec2bf8-79fc-3027-9b30-f233db47d338 | -9.1144 | -61.60621 | 2026-08-20 06:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f2af4a75-635d-32dd-9ff2-d1614902ff33 | -8.40651 | -62.70753 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e85a357-1ea0-3cb0-9c0a-993b89f09ba5 | -8.40773 | -62.69881 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a69dd1bb-276e-368a-b1de-36ec73986c71 | -10.39798 | -61.20729 | 2026-08-20 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d59ac7d6-7c16-3853-8842-b5114a2966a6 | -11.69517 | -62.7534 | 2026-08-20 06:01:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 841a2cd1-fcb0-3233-a751-b64d06f0611b | -13.44012 | -57.07016 | 2026-08-20 06:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57dd9417-47a9-3b1d-a59d-c3ee0234e6c2 | -7.85904 | -63.76387 | 2026-08-20 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ae8c291-96b4-3936-832f-6b11c1c84235 | -13.44628 | -57.07706 | 2026-08-20 06:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2f0df42-c6af-3a9a-ba35-75277640e035 | -7.86365 | -63.76082 | 2026-08-20 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5e16edb-78d0-3f46-89b4-687693c444d1 | -9.39454 | -60.55599 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58c5c324-b810-36ed-9333-816ede812d0d | -9.11993 | -61.60173 | 2026-08-20 06:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 57bc4848-bda1-3ff0-bb80-71dda1a8bfa0 | -9.22173 | -60.8107 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef5d7f8-97a4-37d3-8cfa-f590dbf6c510 | -13.43331 | -57.06924 | 2026-08-20 06:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 491fc416-d0c9-347a-8da9-9e1a8e1f4887 | -10.39254 | -61.20951 | 2026-08-20 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f352d11-8121-325b-a5c1-c8573e016763 | -9.54098 | -63.56258 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9b27b4b-74ef-32e2-958c-25a573c2976d | -7.86312 | -63.76447 | 2026-08-20 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86519676-ed59-30bf-8d0c-047d2bf3027a | -9.17733 | -60.83256 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a9aedf5-ad29-3d92-91d6-ec12871b0915 | -9.39412 | -60.55913 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f75936c8-1107-3293-88a9-899ffd667405 | -9.11511 | -61.60101 | 2026-08-20 06:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 54e1a972-a380-3766-9244-2715e30412bc | -9.02341 | -60.49516 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7904eae-a2b8-336d-941d-47d20bbb0599 | -8.40833 | -62.69446 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 050978d5-5b72-304e-9a88-e01113819f4a | -8.2856 | -62.89645 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc947bf-3aa4-3a2c-9237-3318c84b016f | -9.22091 | -60.81683 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c340887-eeae-33e9-a88c-afd7ee8bbcb8 | -9.08061 | -65.38784 | 2026-08-20 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd4b32a6-c37b-3f73-9c45-52ea1e5b68fa | -9.17935 | -60.83197 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26622824-a15a-3431-9613-8da594e8df40 | -9.39497 | -60.55284 | 2026-08-20 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b456cfae-3828-3f20-ac75-8b8249030866 | -11.82056 | -58.83958 | 2026-08-20 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27eefaf7-f2a1-3474-b1fc-16afaf05dac0 | -8.40712 | -62.70318 | 2026-08-20 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46be9e0a-cf5c-3523-96aa-ae4ab78b344e | -9.07948 | -65.38951 | 2026-08-20 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6cda87f-2db8-3fc4-9991-20e55ea34454 | -9.22132 | -60.81376 | 2026-08-20 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README69.md)

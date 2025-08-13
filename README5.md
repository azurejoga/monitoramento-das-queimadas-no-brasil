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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ed12d2b-0e49-3423-8c48-98441ed04702 | -15.0791 | -51.3424 | 2025-08-13 00:20:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| f638efba-2e91-3f25-944b-0fa60ef949a2 | -18.5303 | -46.0414 | 2025-08-13 00:20:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2b68cd9a-87a9-31b1-b900-3d2c9a420842 | -10.9689 | -49.5856 | 2025-08-13 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 0643767c-c1b1-35c4-9763-0cb9ee9b5c6c | -9.1892 | -59.6752 | 2025-08-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e624cd9c-291c-3013-a016-125fdca13fc1 | -9.723 | -49.4806 | 2025-08-13 00:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7b59aba5-a2c7-343b-84df-26defb959922 | -11.7508 | -48.1825 | 2025-08-13 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 4715aa80-066a-3522-8f40-223b958a0106 | -15.0985 | -51.3396 | 2025-08-13 00:20:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9199379c-750d-3861-960b-a18e078c498b | -9.208 | -59.6548 | 2025-08-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 6e4df334-f567-3496-90fa-118740fbcd39 | -10.9693 | -49.5639 | 2025-08-13 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 479d927a-dd5b-3f67-92e8-f5bafb962b22 | -22.3877 | -45.447 | 2025-08-13 00:20:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| 9c1bac26-ac92-3d61-926b-97a52e7418cb | -7.1483 | -60.1174 | 2025-08-13 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 3584cf94-9fa8-397a-8a17-95e72a1f56e7 | -15.0787 | -51.364 | 2025-08-13 00:20:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| bd973ee3-e2fe-33a9-9f8a-aa1ff7b3ccea | -11.7504 | -48.2046 | 2025-08-13 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8e07e8a8-dc68-3a5c-865c-3fcf75a97e71 | -11.7695 | -48.2021 | 2025-08-13 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 7f06bd91-987a-365c-b946-866c21a64d83 | -7.1482 | -60.1366 | 2025-08-13 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1c9c6732-cf8d-34c3-9bcf-0a9f118f79d4 | -10.2412 | -50.2429 | 2025-08-13 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ec170d33-a26b-32ad-8c3a-b49f23cb73a0 | -9.052 | -60.6658 | 2025-08-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 44fd55b2-e68a-3a0b-8e39-a9e9883dd0d9 | -8.1247 | -55.549 | 2025-08-13 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 4639361c-17f3-3221-9003-6045bd87cea8 | -18.5297 | -46.0651 | 2025-08-13 00:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 13d58bf5-9d82-3543-9977-c0726df6f700 | -7.2746 | -60.6294 | 2025-08-13 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| fcb32265-e791-3677-9d64-f28d537e75db | -12.5746 | -46.9781 | 2025-08-13 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c7473f77-7170-3aca-bc23-68c8ce3a0f7a | -11.9938 | -45.1496 | 2025-08-13 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 06d0e154-23b1-3382-a7cc-e0bf33ab4682 | -9.0521 | -60.6466 | 2025-08-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0e083eb1-bc00-3942-8539-b85b40cb7246 | -8.1061 | -55.5501 | 2025-08-13 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 07d55308-fdee-3d6a-9c83-61b6b41c81ec | -11.7699 | -48.18 | 2025-08-13 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 1c007646-6c71-39b1-9cc8-5a6fe49ef9b6 | -12.5361 | -46.9837 | 2025-08-13 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 67dae498-2fee-3eca-aa67-f7b8120ee9b7 | -8.106 | -55.5701 | 2025-08-13 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 7260eb0f-1a8c-3bfb-b023-6f765d1fdb2e | -7.4636 | -59.8931 | 2025-08-13 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 56fd6002-e841-30d4-b297-33a4aeb9ac21 | -16.3153 | -52.9201 | 2025-08-13 00:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 46d92f9f-e9fe-3abd-be01-b8ced6bee5ba | -9.1894 | -59.6558 | 2025-08-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 9d6e62fb-afff-3605-8034-c3a34d19050a | -7.2562 | -60.6302 | 2025-08-13 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 63af2dcb-0103-3fbd-b980-39908f0971fa | -7.0935 | -60.0237 | 2025-08-13 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 548c30d1-aff2-3309-930f-47538528d353 | -15.0981 | -51.3612 | 2025-08-13 00:20:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 918ba0f8-6356-3fa0-9cf1-e00f646fefc0 | -7.1298 | -60.1374 | 2025-08-13 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.0 |
| e262ec7a-31a9-30ec-b785-3a73eb2e4cb9 | -12.5365 | -46.9611 | 2025-08-13 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 54024cd6-e0d2-3ad4-8dfe-adf01739af08 | -22.3869 | -45.4716 | 2025-08-13 00:20:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 152.4 |
| 23ae905e-2834-31d0-9d29-7a9c9bc29554 | -10.2415 | -50.2215 | 2025-08-13 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 5e239da9-284a-3904-bcd5-3967da221f02 | -8.1246 | -55.569 | 2025-08-13 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 9f77498d-c3e5-3d77-8121-c229c1115f0c | -22.4079 | -45.4657 | 2025-08-13 00:20:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.0 |
| e30f2a5f-c9c5-3e38-bb42-779e27a27246 | -7.1299 | -60.1182 | 2025-08-13 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 870dc3f4-6b04-3735-8475-a44c98bf61b0 | -7.1298 | -60.1374 | 2025-08-13 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 7cffbe85-9701-3af4-8dfd-aa6d56be99d8 | -10.2415 | -50.2215 | 2025-08-13 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| fb4d9e9a-797d-3b6f-b8fa-2f6bd34f8e75 | -11.7695 | -48.2021 | 2025-08-13 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 77a315a4-27ed-317e-9995-28424ad5e3eb | -9.7041 | -49.4825 | 2025-08-13 00:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d5c46c96-42ce-31bc-8b1b-64b471253033 | -7.1113 | -60.1381 | 2025-08-13 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 47def39c-a169-3ec0-abe1-e8a1c505cdc2 | -18.5303 | -46.0414 | 2025-08-13 00:30:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c031bf28-5b49-3774-9142-c3608548e203 | -7.0935 | -60.0237 | 2025-08-13 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 1613c102-1352-31e7-aea5-88a95b8e48ca | -15.5484 | -43.1637 | 2025-08-13 00:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 61.2 |
| a02d2201-5d6e-3559-8465-87344152ec77 | -9.0521 | -60.6466 | 2025-08-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 60fe790c-3f0f-36d9-99f6-08069f2e8b3b | -7.1482 | -60.1366 | 2025-08-13 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ae6e9f1d-2829-3c81-8504-ec25a7d45686 | -16.3153 | -52.9201 | 2025-08-13 00:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c511996a-d39c-3ab2-bb7f-0cdb63482019 | -9.0707 | -60.6457 | 2025-08-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 25467e90-1b6f-3ed5-98fb-25c5ab0d0964 | -9.208 | -59.6548 | 2025-08-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c809f5b3-af11-308d-a018-10ba5b6a6c53 | -7.2562 | -60.6302 | 2025-08-13 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 446816a0-7783-341a-9b41-788268b61f9b | -8.106 | -55.5701 | 2025-08-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 268c8549-4428-3031-b31b-2009ca748ca7 | -15.0981 | -51.3612 | 2025-08-13 00:30:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 90671b97-72ee-36b4-9d18-fd0649393b13 | -7.1114 | -60.1189 | 2025-08-13 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1869564a-5e78-39f3-99de-cd9e53c37efd | -6.6115 | -43.8709 | 2025-08-13 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 2cb498fb-855a-397a-b97b-c8c771da6c7e | -12.3229 | -46.0409 | 2025-08-13 00:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 84aeb945-51c2-30ba-b4bb-8e3bd18c3eeb | -8.1246 | -55.569 | 2025-08-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| f832a49c-6f2a-3fd7-a0d1-06fa433da77c | -22.3877 | -45.447 | 2025-08-13 00:30:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.5 |
| c982384f-88b9-365f-ac85-22a8b5339c37 | -9.1894 | -59.6558 | 2025-08-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 8e5cb3e6-788c-3732-8006-13ec18b3ea99 | -22.3869 | -45.4716 | 2025-08-13 00:30:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.0 |
| 5e74bc46-41fd-31c8-b586-21b771303b2c | -9.4383 | -40.3668 | 2025-08-13 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 149.7 |
| ed7d7b0c-b43e-31e7-9ff5-7a1c54a6e873 | -6.0992 | -59.9267 | 2025-08-13 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 882d3090-e96e-30e0-9259-30ce8788e95c | -15.0985 | -51.3396 | 2025-08-13 00:30:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| f159ec1a-064b-344b-aca6-16ac648dfcdc | -8.1247 | -55.549 | 2025-08-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| f211d4ca-a7b0-3aea-a142-afb3b316fd2c | -10.9689 | -49.5856 | 2025-08-13 00:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| c9c68d92-b8d8-3a9b-9c7a-c72244ba9d3c | -12.3225 | -46.0638 | 2025-08-13 00:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 36827180-04a1-3509-b786-17446e602ca4 | -9.1892 | -59.6752 | 2025-08-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e74699bc-67d8-3ad9-bfec-eb023aa86547 | -10.9693 | -49.5639 | 2025-08-13 00:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| cd016fac-feba-393a-a8ad-7a12159727c9 | -12.5746 | -46.9781 | 2025-08-13 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 68b76628-49b9-3ebe-8939-d09753dde3fc | -11.7699 | -48.18 | 2025-08-13 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 5e574afb-c7e4-328f-8479-c573525ee6a5 | -7.1483 | -60.1174 | 2025-08-13 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 3c6b4c50-f2b1-364b-8605-ac3ba574177b | -11.7508 | -48.1825 | 2025-08-13 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e0124616-f64f-343b-b4b1-e8b6cd15e63c | -6.0991 | -59.9459 | 2025-08-13 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| b783e838-a705-3f54-b0b4-10a4ac5e9416 | -6.6112 | -43.8941 | 2025-08-13 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 19f07356-2192-37f9-903e-eabe164f250f | -7.1299 | -60.1182 | 2025-08-13 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.9 |
| cb647609-4001-3d8e-9b48-d2dc26a510c9 | -8.1061 | -55.5501 | 2025-08-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 259e2c21-b7ad-3c83-b0e3-19f3a9533c8b | -22.3869 | -45.4716 | 2025-08-13 00:40:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 273.8 |
| d7ffd289-7d1e-3ec7-a0ad-5598dd8a9e6f | -8.1247 | -55.549 | 2025-08-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 9a43b9f3-b3dc-39c2-bace-20635c22811d | -8.1058 | -55.5901 | 2025-08-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 88df054d-a7fc-3168-aa5c-7f9f9352df9a | -9.723 | -49.4806 | 2025-08-13 00:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 79935a4a-dc2a-3c23-b48e-e28bc51040d5 | -9.4383 | -40.3668 | 2025-08-13 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 267.0 |
| 9a77e326-6b2f-3bc4-9706-a79546a5202f | -9.4387 | -40.3419 | 2025-08-13 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 0373616a-daaf-3934-9a67-b30e712437b1 | -22.4079 | -45.4657 | 2025-08-13 00:40:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.9 |
| fc3b8401-8c32-3088-bc79-0fd185ddfe23 | -9.4574 | -40.3641 | 2025-08-13 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 88e6b876-61aa-3376-8884-da32b6ffc4f0 | -9.1892 | -59.6752 | 2025-08-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 88032ef5-114b-3cf9-b1cb-943611b4e42f | -8.1246 | -55.569 | 2025-08-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 6b053a03-cea0-3da8-be17-483cc9184e05 | -9.0521 | -60.6466 | 2025-08-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| db872f23-382d-3599-b9f6-3d2aa3ec8ce3 | -10.2415 | -50.2215 | 2025-08-13 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 6464e753-948a-306b-9f73-3c4406abc298 | -10.9689 | -49.5856 | 2025-08-13 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 230e7429-246b-3ecc-85fb-c2414c0d4615 | -11.7508 | -48.1825 | 2025-08-13 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 222feebf-22d3-3972-990a-30896c1cf2b3 | -7.0935 | -60.0237 | 2025-08-13 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 95e71542-4087-3321-b2ae-3ea40205066b | -15.0981 | -51.3612 | 2025-08-13 00:40:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b266ed4f-1877-3a6f-b27c-7a7aab82d08a | -7.1298 | -60.1374 | 2025-08-13 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 438cdb48-f14a-3292-8cc8-be53e1a896b6 | -22.3877 | -45.447 | 2025-08-13 00:40:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| d95c86cd-c584-34f4-a10d-aee8a9e65758 | -8.106 | -55.5701 | 2025-08-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 217.3 |
| 9bc7a771-b59b-392b-a6ba-7dce6723eac6 | -15.0985 | -51.3396 | 2025-08-13 00:40:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 43.9 |
| d6db8559-42c1-31ec-9490-5a6f27b8c105 | -11.7699 | -48.18 | 2025-08-13 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 179.0 |


[Clique aqui para ver as próximas entradas](README6.md)

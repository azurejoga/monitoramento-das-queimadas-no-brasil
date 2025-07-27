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
| 4d063d9b-b75c-3db1-96d3-2abcc1d2698c | -13.09322 | -47.32883 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4bb67e4e-5c2e-3b0c-8cdf-cba847564748 | -13.09998 | -47.3585 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a600686-6fb1-39f6-a852-e0e15d1adbbc | -12.6905 | -47.0185 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab672fa0-e901-3b0c-b50b-b9502d856b03 | -9.20379 | -60.82725 | 2025-07-27 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d80bb862-9578-3ae6-b07b-f98c93407223 | -11.98157 | -46.71075 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f95856c0-ef49-38d9-8341-7d3d69c9b0b9 | -12.6818 | -47.01995 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff5ab418-1408-33d6-a71c-9f140d6d8b39 | -11.96587 | -46.70882 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9970ead7-6a5e-3730-8800-26a86807214d | -12.67936 | -47.02349 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1bbc538f-8b2b-3096-b89b-f011de356b1b | -11.30497 | -55.12001 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1919d020-ef7c-3479-af37-4811fb0756ee | -11.1112 | -45.12108 | 2025-07-27 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aad6aebe-91d3-3329-b33d-38bd5667b997 | -8.66567 | -63.85086 | 2025-07-27 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a54a1b32-d1a6-366f-a875-0a65acad309a | -9.02361 | -59.76374 | 2025-07-27 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13e4b1ef-0fd2-3d95-b06a-4c80f0c9a298 | -8.66521 | -63.85135 | 2025-07-27 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09cfd633-04cf-3b05-b7ca-0c62e27b47c1 | -8.66464 | -63.85458 | 2025-07-27 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61eaa370-ddf1-323c-bb28-c6193b8dbcb7 | -13.48727 | -45.50212 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 89a4d7f4-aa33-3f3a-b6e0-2697274a1341 | -13.12875 | -47.33434 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff9837cc-f009-3b00-b750-1db47b35a137 | -12.70889 | -47.01294 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 839ae562-30bc-30eb-b6a7-d814751cce0b | -13.72085 | -45.68776 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d74b76db-b394-332a-abae-1172b6b758fd | -12.68455 | -47.02398 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36e71e05-f91d-35d7-aa9f-15a83032d314 | -15.03885 | -49.2598 | 2025-07-27 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08f5458c-fcd4-38cc-b45d-394c4ad8b3ca | -11.3017 | -55.14105 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad9735ff-cdd1-3647-91d8-6eb2df156a31 | -13.09816 | -47.33075 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69a7996e-8569-3013-8186-fc769e98341c | -15.96187 | -49.15767 | 2025-07-27 04:59:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f014a7a8-a99b-3df3-940d-d64e25c2cf7f | -14.02528 | -44.61295 | 2025-07-27 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1057747c-7898-3e76-9bc8-2e45f10469a2 | -11.96505 | -46.71099 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 173cc81d-5867-35c5-9bf2-4a883e51bb63 | -12.68088 | -47.01146 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 60010209-4cd7-3a2e-ad0a-ab9a00c5aeb9 | -13.08714 | -47.33638 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0797cf26-da12-3063-8be7-1c216f35e21e | -12.67652 | -47.00433 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0540df8-dc01-3b62-9e12-2cfe6b44ac1b | -8.60395 | -64.04231 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e58fcc3-7118-3192-9978-91c099730ae8 | -12.67739 | -47.01287 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 15180376-b8af-3474-9c88-c67b438d3717 | -13.45378 | -60.97923 | 2025-07-27 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a06af60-b627-3ca2-a406-fea3f5d3d9d1 | -10.03703 | -59.10283 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f3bd7bac-a99f-3b4d-a6d8-1981ca63edda | -7.90138 | -63.5285 | 2025-07-27 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae8fc8df-5a7d-3464-8e9d-c41d2898af64 | -12.68595 | -46.98492 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a228eb3-d8ec-30b4-a9af-b7342322c249 | -11.97633 | -46.71014 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78412702-36b0-3106-8ee4-1d2fbe231cd1 | -9.02667 | -59.7697 | 2025-07-27 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ee72d5c-6d5a-3b1e-8294-569196346c04 | -8.07409 | -63.86082 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8b1dbd6-30d1-3a00-bf62-e146e1d6f679 | -8.60515 | -64.03564 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e608be4-efd5-3df5-b265-8a88ba5354c2 | -8.97463 | -61.51006 | 2025-07-27 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3325a20-0c80-3e8d-b6b8-fb462e19cb09 | -7.95301 | -61.82854 | 2025-07-27 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f92aa79-8db1-36a5-9815-53bd31e1165a | -11.30225 | -55.13754 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6445c7a6-c0a8-31f9-b98f-e751c58d19d3 | -11.29835 | -55.11895 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3adb250-6c8c-38c7-80a4-36b6c601a0f5 | -13.12917 | -47.33086 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 618d5a7e-a0a8-3bee-884a-caf3f3c5691e | -12.6909 | -47.01535 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b979aa20-f59b-3bcf-8576-c507f9b2c7c3 | -13.09853 | -47.32769 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c72a2a1-ff88-3226-98c9-0d53c931d3de | -12.70923 | -47.01014 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7913c64c-4224-3d04-bdba-4f243864b126 | -12.04631 | -45.83879 | 2025-07-27 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1c6fb757-81e0-3662-b5a4-af29c0433806 | -15.03487 | -49.2543 | 2025-07-27 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51ffb1a8-a5e1-3b5d-b4de-2e127f6b7670 | -13.48679 | -45.50623 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 29df529a-4524-3340-bdd2-bf2d4b8072c0 | -12.67847 | -47.00372 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96560eef-8a12-3c33-8dfd-1d9ef7596e36 | -13.11982 | -47.36518 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2dcf094-653f-372a-a886-8e14aa6fc43e | -12.67774 | -47.00989 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31067f1c-6d9f-3abd-8869-cf4e3ca70281 | -13.10031 | -47.35584 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc8623ce-c125-364d-a360-0f8fbbde618f | -12.68289 | -47.01083 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a702bff-e270-3801-b34c-c14bc0afb0d4 | -9.20386 | -60.8268 | 2025-07-27 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 408bdab1-7e5e-38fe-896d-800578e9e808 | -14.96438 | -46.97608 | 2025-07-27 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3bd6b5f-71db-37a3-bfad-d217e18ed210 | -13.09284 | -47.33198 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b5bcb753-ba09-35ae-bd22-7172efaa1d34 | -12.6805 | -47.01451 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d3e4fe11-b0e5-3cc3-935a-6d8dec076d4b | -8.28804 | -62.891 | 2025-07-27 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64714fdd-0ac8-3b52-bd2c-977d7bf11923 | -10.0401 | -59.10069 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a9cca60e-7887-345d-bb51-dfaaada45ebb | -11.30556 | -55.13807 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3c2a069-84f5-3fd3-ab0a-198ccd3bf00a | -10.03935 | -59.10524 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1b12391c-8eaa-3691-a71f-0e4ab2f9e3c4 | -10.03999 | -59.10803 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d9987744-eed6-3aa4-81bd-61582f6e0615 | -11.98114 | -46.70978 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2297c9f-40f0-3ad3-b7b1-372e7ac4a6a1 | -13.20192 | -53.30481 | 2025-07-27 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46f22796-a60a-312f-928e-c16be0bc693d | -12.67628 | -47.02221 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5088eb1-76eb-38fb-9abf-99a393b8a35c | -15.18826 | -43.2787 | 2025-07-27 04:59:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9cfa2b4f-712e-3b98-a499-6769bf76ea5e | -12.69258 | -47.01761 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a89c9816-1490-30f1-aa1c-3edef42fa2b0 | -10.04772 | -64.98428 | 2025-07-27 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f6c6dc0-9357-3da8-88c7-da33e0b9d00b | -10.84581 | -46.68535 | 2025-07-27 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b5ea6d3-d134-34f4-83ed-631815ab731e | -10.04234 | -59.11046 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae34eb33-2fad-3c5e-b80b-d79026472df5 | -12.38698 | -48.7783 | 2025-07-27 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f172cfee-101b-30d3-8a46-efc565a73f47 | -10.34912 | -57.50674 | 2025-07-27 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35e34388-7e5f-33a1-b90c-f42bcd34c464 | -12.03987 | -45.84548 | 2025-07-27 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ec8241fe-f22b-387f-be4b-3daaf2f1712b | -12.04677 | -45.83507 | 2025-07-27 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2a4e7a2f-c904-3d16-b1dc-6b5acb8f229e | -13.48812 | -45.50294 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 717d1c80-2346-328c-bd9b-9bbdcfbccab3 | -10.2809 | -64.45914 | 2025-07-27 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4908ca76-debd-354f-81a0-044288985b5d | -11.96465 | -46.71414 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b9ce9fd-2e74-3102-b23b-3cf75b936cd7 | -12.68664 | -47.02335 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ab0187b-4558-3fbc-a69b-4920bd4a0ec9 | -10.03859 | -59.10982 | 2025-07-27 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f575f742-4853-329a-a37e-f84ee689d083 | -8.60455 | -64.03897 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fce09a26-f016-317e-b1e3-99040b6ba66c | -14.02521 | -44.61295 | 2025-07-27 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34639d2f-7295-31c0-b6d1-95aa40e53538 | -12.67825 | -46.9906 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6190a87c-d1e3-37a9-bc5b-a197c8c427c1 | -8.0735 | -63.8641 | 2025-07-27 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6951668-ac91-33a4-bb67-21e2ecb5b342 | -15.27211 | -43.07465 | 2025-07-27 04:59:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| be4b54ff-0c84-33bc-acad-cb7a9341a136 | -12.6781 | -47.00692 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0e46bf5-9779-3d43-ac29-7a1fa434e2e0 | -12.68252 | -47.01394 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 455e2321-69fc-30bd-8301-fb1ac66870e7 | -12.04586 | -45.84251 | 2025-07-27 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1237759f-76fe-3959-929b-f7643de92d90 | -12.7144 | -47.01089 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a8de6a58-cddd-385b-a176-014b86b0a363 | -12.71077 | -46.28496 | 2025-07-27 04:59:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff72ff61-a8f7-3d35-8d51-033e8c1c4fbe | -13.12119 | -47.35396 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5eee11a9-d7bb-3de4-93d5-e33b00b9d823 | -12.68366 | -47.00431 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| afc10623-9b31-32c6-8f08-ec903d15d4d2 | -13.7165 | -45.67482 | 2025-07-27 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c51c9e4-ba0c-3dbe-8542-3a3df650e279 | -12.68374 | -46.98878 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8e0d913-404f-34a9-8e95-15ad8d0cbd83 | -11.97671 | -46.70699 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e2b551d-45e6-3bbe-80f1-4d1fbe402a3f | -12.71576 | -46.99968 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de6db8f5-798a-3477-925e-cf3f59c8cc12 | -13.20134 | -53.30882 | 2025-07-27 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a1af3fe-4b09-367f-b66a-59ff93d0a5c0 | -12.68769 | -47.01459 | 2025-07-27 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d0123830-713c-321d-9e25-f99c6898b711 | -11.97146 | -46.70647 | 2025-07-27 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fe441dd-25fd-3b2a-9725-1926078c8646 | -11.29889 | -55.11545 | 2025-07-27 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README19.md)

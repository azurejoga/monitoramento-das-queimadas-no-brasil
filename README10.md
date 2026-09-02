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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76c87fae-26b7-36f9-b294-c917d5a619db | -14.0022 | -58.683701 | 2026-09-02 01:33:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8fc6b9c5-c1f7-3813-af8d-d11765fc2e00 | -6.8566 | -59.480598 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1b39b80-deac-3d7c-9785-c73570d19c27 | -8.2414 | -62.905201 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c68341ca-39dc-35a3-bea1-8cb5ec9bd7b4 | -9.0857 | -65.375702 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce95bc56-3aa0-343c-9643-4cc13b3e95ef | -3.6227 | -60.567902 | 2026-09-02 01:33:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfbd600f-14e4-3dd6-9b0b-765447593920 | -7.6231 | -57.615898 | 2026-09-02 01:33:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a80f957e-b251-3749-84b9-5dbf13974937 | -8.1313 | -54.952499 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 303c4157-fc1f-34e5-8bb4-cf6b3620a380 | -4.9735 | -55.8526 | 2026-09-02 01:33:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e06fdab-5ee7-3c94-8137-1e08c8d1fde4 | -6.8159 | -59.439201 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e31a0074-204e-3f6e-90f3-2729566dbd1c | -8.5705 | -63.1791 | 2026-09-02 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e09a2d09-2f08-37da-af5f-3556c947978a | -3.0725 | -61.222401 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 664cf74b-be91-33cc-9ca0-12ebb28b90b4 | -9.4428 | -64.565201 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27fc6084-8434-3e59-bceb-72b57113280f | -8.7581 | -62.592201 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a79f3632-45e7-370f-b8a4-3613e60f75e9 | -6.686 | -58.754299 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f379a5f8-6d0e-3432-99c7-1b141a016ad6 | -14.9725 | -48.096401 | 2026-09-02 01:33:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7d107e7e-839c-33e7-97c3-0907f4be24e0 | -9.4372 | -67.447899 | 2026-09-02 01:33:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c26111b-7e77-3911-a2af-9412c38fbb8a | -6.6901 | -58.771801 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3e36d48-e62c-3915-8e93-599cbf650bd7 | -6.6499 | -59.435101 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04a80ba8-7906-373b-84f9-e9ee6734922e | -7.7719 | -61.202702 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f68b654a-41cb-3126-bd41-28846e6f1630 | -13.9907 | -58.678501 | 2026-09-02 01:33:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 917a3633-86eb-3d5a-b05f-665acd63f277 | -11.6692 | -50.209599 | 2026-09-02 01:33:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bea87065-903b-3072-8259-8ead6b51f944 | -8.2704 | -62.759701 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d0192219-5026-367c-b9e1-5296de72b690 | -10.488 | -64.320801 | 2026-09-02 01:33:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4a72fe1c-6c60-39dc-a720-74e1d5c2fc53 | -6.5597 | -58.569401 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 130e5da9-0ec6-3e48-8e6d-70353bc78d48 | -13.9925 | -58.6861 | 2026-09-02 01:33:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38772cfd-9f5d-38f0-9d60-43ece009bb2e | -9.0838 | -65.366997 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b752081c-f40b-3992-accb-3fbd975dd2b9 | -4.9701 | -55.8386 | 2026-09-02 01:33:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 585bcc58-fa0a-3922-9e48-74f85dc40c4e | -4.9832 | -55.8503 | 2026-09-02 01:33:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9901cf6c-9b2f-393c-a03c-ec473f917e2a | -6.648 | -59.426998 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fa6b798-9859-34da-96a9-7ac59c866753 | -6.8664 | -59.478401 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd8f5268-2937-375c-837a-9d32da240558 | -10.4689 | -64.469002 | 2026-09-02 01:33:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d631b41e-a937-3bc1-a854-11c5e4f40b48 | -7.2067 | -60.675098 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 286e1221-64ea-301a-bf59-ac0a31c1cd3b | -9.1489 | -60.954498 | 2026-09-02 01:33:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d0aef0c-e8ef-318a-8e3e-b9f0bd8c83b6 | -8.5607 | -63.181301 | 2026-09-02 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3fe02f5d-6910-387d-a410-7f1660cf1b83 | -6.8094 | -59.1036 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3d0492d-bc17-3cd4-a527-27b1def87618 | -14.4952 | -59.837799 | 2026-09-02 01:33:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf413334-3051-318a-b031-815ea4fd90f2 | -3.1267 | -61.233398 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d742d52-8544-3561-87c1-e7f0f5d51429 | -8.2606 | -62.761902 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a015a5cc-2734-3be8-80b9-8f11add164cf | -6.2591 | -55.425201 | 2026-09-02 01:33:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dea540c-5643-31d3-98cc-8a32b1438375 | -6.8807 | -59.4072 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31202c53-1f05-37ed-8ca2-78011d765d35 | -7.7285 | -60.9687 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c659e233-7b4e-3b63-a52e-b7d48e44e429 | -5.3399 | -60.144798 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6479a512-e550-3c78-b9e5-d58e3b129222 | -9.0927 | -65.502403 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| beebd1d7-d4c0-3424-adf8-073726ad6dda | -9.0111 | -65.410004 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c81874d-1629-317e-8664-3da5d7bbbb51 | -5.9722 | -53.587601 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97222b6d-5f8d-351a-bcca-6ffbc252e26e | -3.1979 | -61.1399 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32da370e-27f2-3381-a8bb-c060b5804561 | -8.468 | -54.730301 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ab657f-f887-3575-ad2e-6ff3b1643ef1 | -8.9037 | -62.370098 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 697ac6be-e5db-30f2-865b-2f1de5791dfe | -3.6173 | -60.5448 | 2026-09-02 01:33:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee01d765-41dc-3e7a-9478-d6db3f523a7b | -8.8991 | -62.3493 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17a36bac-4023-3a1d-8c6f-bebad2dc4d96 | -6.6839 | -58.745602 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6665e2e1-eeb9-3de4-8467-f518ce3c5edf | -8.4547 | -54.717999 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12c3ea4c-b2d4-3e2e-9d01-121c0ff6e03e | -8.5721 | -63.186199 | 2026-09-02 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 49abf257-1bf6-3ccb-a9d9-355d3b7b9ba1 | -8.4619 | -54.747398 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73add776-498f-33dd-b24a-3d1b7b8e56e8 | -9.83 | -63.011299 | 2026-09-02 01:33:00 | METOP-C | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 261d599f-e963-3230-9c8e-d31ff4c88f2a | -5.5787 | -60.195801 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37e9dfea-64f0-3a19-838c-b844d664de90 | -7.2165 | -60.672798 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d802097b-2f2d-352b-8bf7-c48ff8105215 | -8.4473 | -54.688499 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc20149a-6292-3980-90e2-ffdf241d943e | -9.8288 | -59.476898 | 2026-09-02 01:33:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f5d44eb-4809-30bc-8ba5-10976fa4ae27 | -7.7589 | -61.190899 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6019c7c6-07f5-3110-b9ff-57ee073a085a | -10.9009 | -45.3509 | 2026-09-02 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| afae3e50-a5a4-3bbd-858e-bba965faa269 | -12.4727 | -41.3059 | 2026-09-02 01:40:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 34414f4c-7315-39ee-81e0-a5321ac202bc | -8.911 | -62.372 | 2026-09-02 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 606db499-b76f-38b5-963e-54c1024aa1e0 | -9.862 | -64.9771 | 2026-09-02 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 32e598ec-d59b-31bc-ad7b-abe045f93d3c | -7.2006 | -60.6706 | 2026-09-02 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 647d904a-4e93-3f26-860e-df4790e5363a | -8.7613 | -62.5869 | 2026-09-02 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 73e1202f-ac09-373b-9dc1-47fa9be26b41 | -7.2005 | -60.6897 | 2026-09-02 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| a67d83a6-7f26-3468-94e8-e94b98a7ca12 | -13.9853 | -58.6919 | 2026-09-02 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 4d630726-2bd8-38c3-a56f-1e7907154eec | -6.6948 | -58.7678 | 2026-09-02 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 86557d32-8bb7-313e-89bb-ae5671b2d403 | -10.777 | -44.7695 | 2026-09-02 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 1ac3b85d-0c47-343e-a805-3cd3f47a7b6f | -11.7903 | -50.545 | 2026-09-02 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| bed01cdd-a564-350d-a048-b7d2e4586dfc | -12.1516 | -47.0608 | 2026-09-02 01:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 086955ed-29de-349d-bccc-8df288600466 | -7.2191 | -60.6699 | 2026-09-02 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 3c3e015d-582f-3ec2-9dbc-f2b70b3fc4ef | -11.3334 | -50.618 | 2026-09-02 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 2743f3f9-1acf-30e4-9a76-a56299499326 | -11.7906 | -50.5236 | 2026-09-02 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| a985e94a-f18b-3afb-8f26-eaca28c8a48f | -12.1504 | -47.1283 | 2026-09-02 01:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 11829089-a71b-38e5-a892-ff4c7c55712e | -12.1512 | -47.0833 | 2026-09-02 01:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 39c49706-c2dd-34a8-a0dc-7a4b2d3579b3 | -8.5728 | -63.1807 | 2026-09-02 01:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 373c534b-6ab7-383a-994f-487d09819ca8 | -11.3331 | -50.6394 | 2026-09-02 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c55f6e18-9bf5-30a9-8f5b-7a17c23e4c9c | -10.9013 | -45.3279 | 2026-09-02 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ac0137f5-0e41-3553-ac77-d8f026938f20 | -11.3521 | -50.6373 | 2026-09-02 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 14e62ea2-0d6d-33cb-b54f-c5f36dc59522 | -9.8806 | -64.9764 | 2026-09-02 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ee144e99-9ba1-3bd7-b4b6-b067514f2c19 | -11.3524 | -50.6159 | 2026-09-02 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 670a196c-d5ee-3fd9-9e79-c47a6b74e181 | -14.0044 | -58.6902 | 2026-09-02 01:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a4c923b1-5466-3b90-8074-d509457de6c4 | -11.3048 | -45.1575 | 2026-09-02 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4561fde2-652b-3d63-8e6b-0ff3c9bad91d | -6.6949 | -58.7485 | 2026-09-02 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 8300d91a-1c83-3436-95d6-8fcfd4517bcd | -12.1704 | -47.0806 | 2026-09-02 01:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 508e43eb-97e1-3a5f-9bfa-1de72967b6ad | -8.4485 | -54.7048 | 2026-09-02 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 44840822-a283-3cd8-b138-d8bc37499ed2 | -12.1324 | -47.0635 | 2026-09-02 01:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4d76c812-8966-3818-85c7-046439d0ce28 | -11.7903 | -50.545 | 2026-09-02 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| e016d9c0-990f-3c88-ac50-223521c9e48d | -8.911 | -62.372 | 2026-09-02 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8a1836c9-aee3-3553-a0e4-4bbeaced5ae4 | -12.132 | -47.086 | 2026-09-02 01:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5c0fb90b-186e-340e-95a7-5c825628aea7 | -10.9009 | -45.3509 | 2026-09-02 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| ac298529-4500-39a0-90b5-d6822114272e | -7.2005 | -60.6897 | 2026-09-02 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| b71d82bb-c6e8-3898-a15e-91dca67ae1e0 | -8.4298 | -54.706 | 2026-09-02 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 1be4d621-3acd-3afa-9046-87f2210f7c4c | -10.777 | -44.7695 | 2026-09-02 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 2badfd97-817b-3851-a77b-58c1032df42e | -12.8843 | -45.8183 | 2026-09-02 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| e50e51b7-6b96-3f9c-9a2b-b42429ec435f | -8.4671 | -54.7035 | 2026-09-02 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 3e3f040b-d0fb-30af-9371-04e939002f64 | -16.1528 | -46.6517 | 2026-09-02 01:50:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| f0170a71-608b-3c2b-a916-718c61cb3637 | -12.1708 | -47.0581 | 2026-09-02 01:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |


[Clique aqui para ver as próximas entradas](README11.md)

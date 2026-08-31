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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65e0c78c-3a98-390d-b024-b4e7af28e650 | -10.14678 | -45.75633 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81b60d3c-72c3-38b2-8901-b57973b219bc | -13.45877 | -57.04273 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40eda344-5b63-33b8-9252-c06d5c7ad1d4 | -14.13289 | -52.80539 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bcea455-9ff9-3947-ad4b-ab8f8c4a18f7 | -7.57279 | -61.37756 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bfa712b7-c8ef-30c1-aa11-6cbbb4147203 | -10.79961 | -50.51299 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0746c95-eca0-3029-8d5f-981e910f35c6 | -9.71856 | -64.99397 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81b91084-29a5-3200-868d-c18d4fffb159 | -9.91092 | -60.15496 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7d56c40-e95a-3860-815f-d4c5052974df | -7.92529 | -61.33073 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d9f0e73-abc1-3b09-ab39-aa32ed58b8d6 | -9.88854 | -60.28622 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c54cd34f-a7aa-3c7b-9682-90ad510240f3 | -14.46349 | -52.19402 | 2026-08-31 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 090aa0f1-9909-3226-ba08-ddd92236bdf0 | -11.07625 | -51.51697 | 2026-08-31 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fd4cc30-116c-36ad-a6c4-cdd67d6fa955 | -11.90867 | -55.9005 | 2026-08-31 04:59:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c48d55c1-0a03-3588-a014-fed72869355d | -14.59204 | -54.09742 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3baf6c2-3978-30e1-9a8d-acd04ecc9895 | -11.08132 | -51.50841 | 2026-08-31 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4e58336e-983d-3e8f-9d1c-fd7580e4b451 | -10.74373 | -54.04336 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7d03ef50-63e8-3dfb-ac35-e9736fff6b81 | -9.84056 | -64.97813 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92d9d3e6-82d5-3f18-a6cc-ffb137a8c3c5 | -11.20576 | -45.05637 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 934e7ca9-7c07-34f7-80e8-b05bb334ae9d | -9.83572 | -64.97352 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c223ab42-de41-3a9e-ad62-54cf17390f89 | -8.94385 | -62.37785 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b1df1132-e504-3ae7-b371-80e6bb790773 | -14.1972 | -44.58473 | 2026-08-31 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f49d301a-0403-3d1e-8f4d-3e3c793faa7d | -14.30907 | -52.90729 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e499010a-5a56-3669-910b-86250b612246 | -11.21777 | -45.11344 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd17db8f-7a2b-37f2-a2fa-ea498989b7bd | -12.94377 | -45.91338 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1756fc73-e4d6-38c8-8e35-010a9ba00e6f | -11.49487 | -46.93325 | 2026-08-31 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11b9a41c-db8a-3229-be4a-4a7f5c90875f | -10.73756 | -54.03869 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b29f54ce-fc4f-3cf1-b9d9-fa705fae77d1 | -14.20282 | -46.56957 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ddcaed2-19a1-31db-ae71-72abf43905d4 | -9.2493 | -60.43232 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6cdf91b-ff2a-3f23-92f7-33d586fc7eed | -10.84454 | -48.34841 | 2026-08-31 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4559e0ee-b387-3268-bfd0-6b0f80ce7cf4 | -7.81049 | -63.25978 | 2026-08-31 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d0a8453-816a-3095-9d08-bb753e9f2e8d | -9.15392 | -59.53284 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ca393202-7f2a-30ff-8d23-ecbfa42aa987 | -15.08592 | -48.10266 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06b40f6f-030f-385d-9860-36e73f0659c9 | -11.49441 | -60.58206 | 2026-08-31 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9b5f3f7-e9f1-3ae3-b9a2-ce3c0a4313a0 | -12.09821 | -45.05947 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39d73b08-bd59-3503-b379-398c4e674919 | -14.59491 | -54.10181 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73ba8499-0315-3b42-aa7f-8c13b3cb550f | -9.836 | -64.97372 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7599f418-4a62-343e-ad1d-867ce3fdd42a | -11.03682 | -57.22631 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1008b144-29a2-36b5-9b88-157e051a160e | -11.49902 | -60.57929 | 2026-08-31 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f045db3-18bb-383a-95f0-488d99efc3e7 | -8.61211 | -54.77958 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12fd6fd7-4d14-3cd9-8836-bdbf8c68be8c | -14.20322 | -46.56594 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6833deaa-add4-33da-8942-b842ceb37286 | -11.22597 | -45.09355 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70fcfe49-63cf-3563-a246-a6f5dd1dedf7 | -14.57546 | -54.11441 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 670c0faf-5c47-3b1e-8771-b7a682f1a14b | -10.07821 | -48.7063 | 2026-08-31 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07133bd8-216f-30f6-a20c-6f72aba01376 | -11.92023 | -45.06569 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29ee7cab-9f45-3f7b-959e-ec7a9cd49f34 | -10.42204 | -57.22651 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2997c1c7-bb1c-3f6d-9d26-6a68c10858ca | -11.49783 | -60.58622 | 2026-08-31 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8530a33a-2058-339b-86c7-d0605456fa9e | -15.19194 | -46.23676 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfccfd5d-2986-37a7-b323-33866c61b33a | -8.60989 | -54.77211 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fc868c9-3eea-3020-9743-38e53e0338ca | -14.22093 | -52.8432 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f05d31fc-a245-3302-b005-150691f98550 | -8.80479 | -62.49403 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 586b2531-13eb-303d-9d88-1e130cfe096f | -14.14437 | -52.80281 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5d106d6-fb0a-3252-a9d4-111b44a22818 | -9.00873 | -60.6027 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c88eea6-8dfc-3ea6-9832-dc7c23404805 | -11.34689 | -45.21375 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7513e90-5749-3054-9c90-7edffcd15c7f | -11.22544 | -45.14649 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2345aa5e-b360-3882-9de3-169ebf565106 | -10.57206 | -50.36387 | 2026-08-31 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3e10b9e-ed41-3ce3-8feb-6ef1127b0315 | -14.60582 | -54.09947 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 704394e3-1ff7-3820-ba0d-d2cd9e707a77 | -9.19179 | -51.54842 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8eff5098-12db-3f1b-ab44-84a5fea20fb4 | -11.4938 | -60.58564 | 2026-08-31 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d42f013c-b160-3f24-bd0f-31b53b173b2d | -13.17932 | -55.66636 | 2026-08-31 04:59:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96cab3b1-2756-3ca3-a9c6-452e4195ccf9 | -7.34523 | -60.5964 | 2026-08-31 04:59:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 295a2ab4-499e-3f21-a9c0-2d76bf7e428b | -10.14969 | -45.76115 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a6ba5b5-4999-3c90-8622-c53c9666e618 | -8.61902 | -54.69176 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbce2e64-028f-33b0-b900-7d302921476e | -9.15309 | -59.53778 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f65d9191-c2ad-30e0-86a6-223bbc9a7b52 | -14.13166 | -52.81403 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c57dff44-d672-315e-bc24-d382e5a2fb33 | -11.37523 | -45.17199 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72611edc-1f41-3e82-b2b2-7ab6ba230f4f | -15.06641 | -48.00148 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b5b448f-90d0-36e0-9715-aa6148e762ba | -9.94497 | -60.51778 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee8162ee-820e-3835-b110-a52fa55a3902 | -8.6799 | -66.52485 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa3a45ff-cab6-325a-871c-478fa3d9c0d6 | -11.15494 | -50.57109 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f211369b-1542-3c1f-9db4-7f6895f57f15 | -14.1587 | -52.78532 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ff23a4f-9c48-32c0-82cf-6a276c8fc9c7 | -9.05444 | -65.41095 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbe9f100-2031-354d-a50f-44da27c6ff28 | -13.93981 | -54.41306 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcc46b93-c449-370a-abba-3ced42da92cb | -11.20862 | -45.33335 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 48455fe8-7556-365b-8bf5-ca09ba2e07ed | -9.89036 | -60.27555 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29a9d4d4-1312-3ff4-9c8c-82103de4845d | -10.14949 | -45.68944 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2bd79d6-5d74-31c1-84ef-bf7bedaf9b49 | -11.03658 | -57.24932 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e555d8f-8fe0-3e9e-b44c-c2cb098a5ebc | -8.61969 | -54.73096 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f290e01f-f7d5-331c-970e-9b60d5e62237 | -12.89452 | -45.84947 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a1eabfa-59f6-3b1d-a2c0-1c8adfba3f70 | -8.94566 | -62.36769 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6fc3fad-c83f-3409-9dd0-3e4ad1643a54 | -9.66934 | -47.93797 | 2026-08-31 04:59:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f649115-abb4-311c-a168-8d4ea4764679 | -11.67715 | -47.61879 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 541364fc-9b05-367e-96db-c9c28e1b60a7 | -9.20975 | -59.5609 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd63a9ba-2390-3c10-8d5b-0b3be4ac13c3 | -8.59377 | -54.72333 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c42a5a24-bdd3-33d5-a43c-6a68cf6b6fdb | -8.57696 | -66.96836 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb669f59-edfa-399e-9bc1-e775ae8ece51 | -11.37122 | -45.20451 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 985de8c7-3c23-3d3b-8112-87cac09e9f5c | -13.96575 | -54.40191 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da0b5cb9-ce3e-3e19-b202-a211f2e0dfa9 | -14.19818 | -46.56182 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10dd27ea-d23b-3f2c-9525-37cdf3f859e0 | -10.48542 | -59.614 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b6edcaf-76b5-3ffd-a3b7-bdb3da74f624 | -11.37216 | -45.2142 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64e7b685-c71a-3c91-9d8f-987ccf6cb0e5 | -8.80386 | -62.49922 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c6d90c96-09a6-3cd2-9add-539b353e03fa | -11.19847 | -45.06796 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 875518c7-0685-386a-97a4-ce91e4122196 | -11.03621 | -57.23003 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5be048eb-0e00-32f2-921e-ad14a666ffb2 | -14.23482 | -52.8495 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6b805470-42e5-3fea-b897-bd8a571ff706 | -8.79618 | -62.48724 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9be124db-59ef-3cb3-b093-518871ea59fd | -10.4887 | -59.60707 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dc20fc7-c68d-3714-9b3e-cd9a07d3fc1f | -15.66941 | -45.93282 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b35e687c-0e89-36a1-949d-337b5f63dee8 | -14.41115 | -52.52293 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e9c02042-2bd7-3167-a77e-6315932bae44 | -15.02687 | -48.16454 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 56a447da-827c-32ed-a398-43ebbae85162 | -10.32154 | -58.09064 | 2026-08-31 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89f169c3-36aa-3b98-b375-a3c3b14cb152 | -11.32607 | -45.1941 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b00ed07-8eb5-38b9-a167-3494abaf5f45 | -14.44991 | -52.54236 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README50.md)

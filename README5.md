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
| 4287a52a-1bad-371e-9009-52f560688787 | -10.77744 | -59.86509 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d24db4b4-53e4-3c4c-8a6e-c1135329478f | -10.01362 | -64.91881 | 2025-09-09 01:30:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 34e34311-a752-3527-8eb9-bd6cb23e8999 | -9.38252 | -65.94512 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 69037109-8c35-37e6-b807-705a3c34b54b | -8.77328 | -61.44481 | 2025-09-09 01:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4238df6-800e-3fac-a6c2-09574c37bbd8 | -10.01501 | -64.92934 | 2025-09-09 01:30:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 30.0 |
| c3157c93-4f96-365f-bc0f-eb30ce554cb0 | -10.57346 | -61.26323 | 2025-09-09 01:30:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d97ceebc-86c4-36ec-bff3-1f4dc93ec3f8 | -9.46928 | -65.51862 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d73a3600-6e7c-394d-9bd8-fa19faa322bc | -9.47492 | -60.48556 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| df89dc67-c406-3447-813a-9979d9a74412 | -10.42573 | -60.74783 | 2025-09-09 01:30:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8b6f039c-9711-336b-a318-c825a5afa107 | -9.99329 | -64.98596 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d63dcfde-bb38-3f8d-ab32-ac24a4b5bc35 | -9.05584 | -60.44687 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 606841e3-6971-31f4-801c-ffb17d3d923a | -9.22922 | -60.83047 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a3d88ece-465e-3bdb-a5c1-4ba32a46dfdf | -9.56434 | -66.73605 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e35c2907-c634-3bfa-bce9-a44b2298d21f | -10.09142 | -59.173 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9dfbd659-ffcf-36a7-82e1-c7d967cf6e4b | -9.06997 | -60.49974 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8f085ac7-c8ce-3463-ad2a-6bd998f671bf | -10.00409 | -64.92014 | 2025-09-09 01:30:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| ce8a633a-d178-3403-b5ca-4d93a9e27293 | -9.22006 | -60.83186 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b1834c0c-60dc-36cf-8b4f-4ce019789f88 | -7.8247 | -63.57362 | 2025-09-09 01:30:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 9f08c55b-0a56-30a9-9501-933d566628b9 | -9.75195 | -65.02586 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6d4776f5-d12b-3d5a-bdfd-8622310ce5ab | -9.19959 | -60.62621 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 26556324-f753-3a0d-90c9-04aeeb7a4fa0 | -9.37091 | -65.93467 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| acfeb1ef-1357-3e2b-bf2c-952cfcfa2a20 | -9.07793 | -65.4166 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| dbb3f500-0908-3dea-a393-aaa03a628e36 | -8.87292 | -64.02943 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2b7704f2-2f0d-3a7f-a8df-2adf3b67ce4a | -9.08618 | -65.40442 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 368b7374-357b-3174-a7fe-9bb53f770ba1 | -9.12961 | -65.96102 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b1855ab2-9dc3-3f72-9a5d-9ff9b4d37af4 | -9.21726 | -60.81257 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 69137e75-c5e0-30e1-b0a2-ba38fbd58db2 | -9.99467 | -64.99652 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4f2e2c01-4d31-3091-99b9-d8ec14c9fe66 | -10.14985 | -61.14021 | 2025-09-09 01:30:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 206dd240-f07e-3b20-82fa-2d3c94e775c1 | -7.88138 | -61.33231 | 2025-09-09 01:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55f2082e-75db-3789-8e5e-192133691fcd | -9.75056 | -65.01535 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 090a6a56-4531-3799-87ea-b9c97ec1ec7a | -9.13946 | -60.51987 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b3da65fa-ae1b-3d47-8f8c-1b74b652aa5c | -8.17663 | -61.20654 | 2025-09-09 01:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0140aab-9f78-311a-80c6-7b88997b52bc | -9.34837 | -65.45108 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b137064f-9f70-37da-b82b-9ac038cc8426 | -10.25569 | -59.38464 | 2025-09-09 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1419c7fc-9447-3b05-a514-72a1285b3208 | -9.9851 | -64.99785 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6dc02e94-7d5d-30a7-81c9-52f812ffb980 | -10.56953 | -61.23571 | 2025-09-09 01:30:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a0407ae3-a94a-3a96-84c9-1fdeda2f9e98 | -9.34692 | -65.44008 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c825557f-a505-3a44-94e6-63f184465869 | -10.00548 | -64.93066 | 2025-09-09 01:30:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| aff81a99-17c2-3403-8e6c-5e8b517e729e | -9.20853 | -67.55754 | 2025-09-09 01:30:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 734a5a56-22e8-3ffd-b54e-e96ca8fb43a5 | -9.83806 | -64.2216 | 2025-09-09 01:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5cdfb93b-ee1b-37bb-ae57-c4d936911f0c | -9.14088 | -60.52981 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 72d28a1a-5836-37fe-9560-daf5ed7a6c9d | -9.05799 | -62.34873 | 2025-09-09 01:30:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46c49285-fdc1-3aa4-9516-120758907cb5 | -9.39262 | -65.94381 | 2025-09-09 01:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8937ad65-298b-369c-8053-6f93a7fe647b | -9.18901 | -59.37394 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c6903120-fcb5-33b6-87ec-e07069c18c0d | -9.23886 | -60.43778 | 2025-09-09 01:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 14fd4822-4801-38c8-ade0-2ea0d6db963d | -6.91721 | -62.94363 | 2025-09-09 01:32:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 67f9ab17-366e-37c5-872f-0368e8b38806 | -5.49908 | -60.1289 | 2025-09-09 01:32:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6a818c12-2c00-3247-ba94-07d7b269f9ae | -7.39855 | -61.63368 | 2025-09-09 01:32:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb93ffa9-a6fb-381e-810e-2d7e8d84e03d | -5.50071 | -60.14037 | 2025-09-09 01:32:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c8034bb3-cb0d-3fef-a65c-3b67d52ed880 | -6.95389 | -62.9325 | 2025-09-09 01:32:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c03fc6e4-6a67-3e0a-a12f-96f2cf815061 | -7.50339 | -63.50946 | 2025-09-09 01:32:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b60e9ff3-de6d-3c99-9c50-d0256ecc4a04 | -6.39426 | -58.19667 | 2025-09-09 01:32:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c88e94a5-5880-397b-a691-25eea0d7dec3 | -6.39653 | -58.21199 | 2025-09-09 01:32:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4cb522ff-afbb-304a-98d3-669d29e25093 | -7.52294 | -61.66639 | 2025-09-09 01:32:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cca5353d-a6bd-342a-90c6-0f0151d005e3 | -5.6736 | -43.9231 | 2025-09-09 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 09313ba4-2136-3728-93b7-ed92480a7e9b | -12.9482 | -54.7519 | 2025-09-09 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a1e966cc-92bf-3d76-b703-86d25072b0ac | -12.0295 | -51.0935 | 2025-09-09 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e3860174-9419-3e57-843a-3ae49daeeb8b | -17.2757 | -46.7538 | 2025-09-09 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 08e34486-22c5-3b45-a755-820d73cf1dbe | -5.589 | -45.0505 | 2025-09-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| cf5bc79c-390b-38ff-880a-2afe3bb0df08 | -10.011 | -64.9339 | 2025-09-09 01:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 6ed8fc3a-c90b-32ad-8a8b-85b85d982c5c | -12.1988 | -53.9024 | 2025-09-09 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 543a1e32-6b40-30fd-8fa0-cf9596942099 | -20.339 | -48.5688 | 2025-09-09 01:40:00 | GOES-19 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 1527a674-e491-31ad-9474-845997179949 | -5.5705 | -45.0291 | 2025-09-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 698192f6-4313-39dd-b3a2-76bf621f1657 | -10.0111 | -64.9151 | 2025-09-09 01:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 0d09b454-029e-3906-92f5-32ed630d25ce | -11.4277 | -43.6017 | 2025-09-09 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| af587c88-a44f-344b-ba57-c74a34a07b39 | -5.6738 | -43.9 | 2025-09-09 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 73a8c149-97e9-3218-92c7-00940b83bcad | -5.6925 | -43.8986 | 2025-09-09 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 14e69444-0d14-3950-a9a9-b1ca30cd4ec7 | -5.5703 | -45.0518 | 2025-09-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 198.1 |
| f8e99863-8a1b-3ced-91f1-750960168e40 | -15.8275 | -48.9505 | 2025-09-09 01:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3ec279ee-75f4-3d65-aeb1-2ff91814eb13 | -12.948 | -54.7724 | 2025-09-09 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c2bd48f7-e19b-3af7-b3bb-4fe6c87c83c6 | -12.1991 | -53.8817 | 2025-09-09 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 7f7b91fc-ad13-3479-a4d4-ae8a494b9190 | -5.5892 | -45.0278 | 2025-09-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 1209ee5c-f89e-320b-8ac1-44d5caa96bf8 | -18.4808 | -49.5447 | 2025-09-09 01:40:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 2aeb7b39-074f-3cba-94cc-240512bc3c0b | -11.4277 | -43.6017 | 2025-09-09 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 99acd0e2-c120-3427-a49a-e70e6f02337e | -15.8275 | -48.9505 | 2025-09-09 01:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 11efead3-00a9-334f-968b-6f57ea234adb | -10.011 | -64.9339 | 2025-09-09 01:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 4934a219-0bde-3dce-bbae-1449ae0225be | -18.8174 | -49.6816 | 2025-09-09 01:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b1a74f20-fee4-3d6e-a00d-70d9515881d2 | -17.2757 | -46.7538 | 2025-09-09 01:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 686eecc9-2e25-3a93-a418-7b21316fb598 | -18.4607 | -49.5485 | 2025-09-09 01:50:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 0a1e3d54-96f0-388b-8186-105119cb2639 | -5.589 | -45.0505 | 2025-09-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| bd304c63-8309-3fa6-8aae-f2dbd8d88f38 | -5.5892 | -45.0278 | 2025-09-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 58e533fa-99cb-3ca4-959b-43a313fc5af5 | -18.4802 | -49.5672 | 2025-09-09 01:50:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 5fdccf28-968f-3802-890c-acf81a59736d | -12.9482 | -54.7519 | 2025-09-09 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 90168e54-9c7a-38e6-bb60-60ff9d774ff3 | -12.1991 | -53.8817 | 2025-09-09 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 368c0ed6-e0ab-3eba-913b-5321859accac | -5.6738 | -43.9 | 2025-09-09 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c8429f4c-720f-31cf-89c2-aa60beb9d69a | -12.948 | -54.7724 | 2025-09-09 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| edf98c66-5238-3aaa-8a87-e375c121b05b | -12.1988 | -53.9024 | 2025-09-09 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a0a63e17-c2e1-39d0-a4df-fa9c8e663d44 | -5.5703 | -45.0518 | 2025-09-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 56d656af-f50d-3601-bcc8-5aae89f9cbb3 | -5.6925 | -43.8986 | 2025-09-09 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2da2ef18-8ee1-3f4c-ba4b-6782c56b38af | -10.0111 | -64.9151 | 2025-09-09 01:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 05d97bf8-e702-3012-b78d-e22d5abb7a89 | -18.8375 | -49.6777 | 2025-09-09 01:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.5 |
| eaf99f94-179f-394f-9159-e8ba63bc314b | -18.4808 | -49.5447 | 2025-09-09 01:50:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 2c5ad722-75d4-35d1-90de-a4e597c7c12c | -5.5705 | -45.0291 | 2025-09-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 0424462a-5b13-30cf-9d2b-0b990d1bedaf | -12.0295 | -51.0935 | 2025-09-09 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 261cdac9-7787-36e8-9216-7b6acab8bb76 | -5.5703 | -45.0518 | 2025-09-09 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 05df4e4a-359b-3dcd-a18e-c35f14132fe4 | -11.4277 | -43.6017 | 2025-09-09 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e3a2855f-f299-3f57-8a06-745006bad8fb | -18.838 | -49.6551 | 2025-09-09 02:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.5 |
| d4d2f0cc-0d28-3ece-9624-ef0924f216ef | -5.6925 | -43.8986 | 2025-09-09 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e8534871-4cbc-31e4-93ca-e28427bc22ed | -12.1991 | -53.8817 | 2025-09-09 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| eb26c130-9e07-3078-a97e-b43de3f77e82 | -5.5705 | -45.0291 | 2025-09-09 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |


[Clique aqui para ver as próximas entradas](README6.md)

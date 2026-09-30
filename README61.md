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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e069ab6-bed6-381a-aa74-a2aeec6dba34 | -9.12071 | -67.83426 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ed79f07-ab8f-38fd-8ae5-587099b7fad0 | -8.04301 | -71.35014 | 2026-09-30 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 856f37ad-1bff-3e41-90dc-7c6862add855 | -9.35085 | -68.21185 | 2026-09-30 05:38:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 550b1cb0-a2f7-361d-96ce-bc1b8f06b461 | -8.78842 | -70.80594 | 2026-09-30 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb0bbec9-3942-30a3-a1df-325f494152b3 | -9.10377 | -68.20528 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77b96111-9782-37e8-8e3c-b483ed9b549d | -12.78511 | -54.0091 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e85d184c-0fef-37d7-8668-327a0da47967 | -9.11779 | -67.82944 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11689ecf-94f5-3e25-a8bb-6aca0aa62d3a | -9.32434 | -68.23467 | 2026-09-30 05:38:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f892002-13db-3227-841a-6178abb3dab6 | -8.77564 | -69.5332 | 2026-09-30 05:38:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 207dfc9e-eee2-36e4-9498-679fbc6a61c8 | -8.49042 | -54.90894 | 2026-09-30 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 196aed10-cbbf-32ab-b6b5-373549ae0bf2 | -10.07136 | -63.08765 | 2026-09-30 05:38:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0e0c6275-fe9e-32dc-98ff-a4e65ce61a8a | -8.2311 | -72.81306 | 2026-09-30 05:38:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7e361cb-99ab-36f7-992c-56138438b29a | -8.77824 | -69.4936 | 2026-09-30 05:38:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81cb958c-b838-320a-b863-a55bbf885970 | -9.13407 | -67.93281 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2425686-e91c-3c59-866c-4cdace347d5c | -9.12362 | -67.8391 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3e451aa-dc45-3d88-bc92-08b35e311981 | -11.54647 | -54.4987 | 2026-09-30 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd434456-498f-3a25-9370-4a75482c3d19 | -9.54911 | -56.16403 | 2026-09-30 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0229de9a-48ae-3d7e-9912-b89274da3bc8 | -12.123 | -61.14695 | 2026-09-30 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f00d7971-e838-3a6f-b6fa-e74b3335fa2f | -8.42931 | -70.23804 | 2026-09-30 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfbb64b2-c554-31e8-b3a8-3ccc00af2227 | -8.60514 | -70.20249 | 2026-09-30 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b8e380d-119c-37bd-b292-686e44b60d8c | -9.12433 | -67.83485 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d2dd07f-58fa-36ee-84cd-a8885ee040b5 | -10.07192 | -63.08398 | 2026-09-30 05:38:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f45f73ad-1e60-364e-be8a-48aa1fa624aa | -8.88066 | -62.38499 | 2026-09-30 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5d73c8b-bdcf-3209-8813-31cdedad8184 | -9.12 | -67.8385 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13655560-942a-38cc-9a1e-09b35c3040cc | -9.10936 | -67.82937 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4f96e01-7d46-3170-a60e-bc9f224cca34 | -8.77884 | -69.49007 | 2026-09-30 05:38:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2943b46-8263-3d53-a95a-35c3b74410ff | -9.10505 | -67.83302 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e9308b5-59f8-359d-90d5-2107ff8c4420 | -8.74364 | -72.83025 | 2026-09-30 05:38:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 016c6b78-6595-3a0d-a302-3cbad356a999 | -9.09934 | -68.20911 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bab4a686-cba0-370d-9cde-4937752c4a2f | -12.77845 | -54.01313 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2dc9d34-71bd-3b3b-8c17-d629111ee515 | -9.13307 | -67.84939 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 587019fe-75c4-39af-921d-12c49edc32b6 | -9.16787 | -67.72953 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 118d7915-6348-35b9-b760-c00932b2e794 | -12.78455 | -54.01389 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55f48ed7-4ed6-3aec-9c84-5a57b3e0dc78 | -9.16898 | -61.40286 | 2026-09-30 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03fb1001-2225-34cb-b9d7-659d09cf95fb | -8.74417 | -72.82731 | 2026-09-30 05:38:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfd8a16b-df5c-3619-ba5f-99a589477e94 | -9.1128 | -67.85914 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40fae3d6-e051-3d3a-80cb-f6e1e83d8bad | -9.16717 | -67.73373 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7580fb97-7a44-3e50-b846-620604d318cb | -8.06394 | -61.27303 | 2026-09-30 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6bc99cd-5f0c-36d9-9d93-911f068b78b2 | -12.65673 | -60.40548 | 2026-09-30 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60dccfb3-59d7-31ed-b87b-e861095a6590 | -12.12991 | -61.15273 | 2026-09-30 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97b302ff-fdfe-3612-b40c-9b929d33d830 | -12.784 | -54.01865 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ffc1b21-592e-3dab-9cf9-25b4a3524327 | -18.27823 | -53.05353 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5e2c135e-6297-378b-8c3a-203d31122506 | -18.28052 | -53.03786 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 290e4fd3-e71f-321d-985d-c35fc6481b58 | -18.27941 | -53.0403 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af5cf4e6-3c81-3481-bc4e-b457fd8b3eb6 | -18.25765 | -53.05143 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5502a9ef-f6be-3dd7-bf09-f5d1f959febd | -18.23349 | -53.0196 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80deb301-08e3-3d61-a522-def44c82fa9f | -18.25136 | -53.04418 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d18afe3-da46-3583-bd80-03998861db6e | -17.13038 | -52.13221 | 2026-09-30 05:40:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 17c5011b-83ea-36ef-a816-e5dc3d44bedb | -18.28684 | -53.04524 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 15097382-c140-3c6e-b128-d8637d285fc0 | -17.12978 | -52.1393 | 2026-09-30 05:40:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ea3818d6-6bd2-341b-bfab-00a215ee62c8 | -17.12265 | -52.13839 | 2026-09-30 05:40:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3cd134af-eb30-3db8-bb4a-2990670992db | -18.25884 | -53.04889 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c933649-757c-391f-b08a-ce8d0c91c607 | -18.26452 | -53.05207 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fedcae5a-d302-36b2-baf3-d37d510dee21 | -18.28568 | -53.04767 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1767fbee-4048-3a59-9214-e3c59e032d81 | -18.27887 | -53.05783 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1eb1381a-6c5c-3598-8fa0-f3615f8eb6a5 | -18.33346 | -53.07493 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 811d89f7-eb30-3bb1-b668-e1bfa4440a28 | -17.12325 | -52.1313 | 2026-09-30 05:40:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 73c7d4e2-99f5-3643-80c8-bacfdfabc033 | -18.28628 | -53.05196 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6478bf1d-fdb6-3257-ae33-299fe3b6f7bb | -18.25251 | -53.04155 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49fceb11-b55c-3dad-a990-6d17fdcbc11d | -18.23297 | -53.0261 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb035a5e-bee7-34fe-866c-ce4fa77fd2d5 | -18.26516 | -53.05624 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a6959ca-3c1a-3de3-847b-ecabd1212e30 | -18.27138 | -53.05276 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 56c8bbce-0c6c-3d73-937b-334bbf6793a7 | -18.26571 | -53.04957 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92e4a6cc-a8fd-330e-9d3b-3da2087ddc15 | -18.27202 | -53.05698 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c857d6b-b63e-3ef4-be07-f832ee9dc991 | -18.25823 | -53.04478 | 2026-09-30 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f74b868-94e6-3cb0-a450-c82facd6c810 | -5.7382 | -45.15587 | 2026-09-30 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 474da723-07f4-3ef3-b0ba-39b88b67ed31 | -6.2045 | -42.50429 | 2026-09-30 06:10:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 2731dd40-8c7f-3c7c-ae85-d8aeb6ec9934 | -5.75192 | -45.15828 | 2026-09-30 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| dcb45699-bd24-39ef-b0c5-d949f5231a21 | -6.20213 | -42.51884 | 2026-09-30 06:10:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| a7b5e5a5-cae0-334f-babe-fe851377a90a | -6.21551 | -42.50594 | 2026-09-30 06:10:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| f833e264-7cfb-3617-bb4c-c3b39046be46 | 1.80375 | -55.64144 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dffc51b1-2dd0-3e08-82d1-fc5d6964561a | 1.80473 | -55.64714 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e0e64f7-9343-39e1-b125-92232a1bf245 | 1.80636 | -55.63519 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e896686-4308-3983-ac79-58aa734bd46c | 4.08293 | -59.93428 | 2026-09-30 06:10:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41893ade-05c2-3af6-a080-f73026d1d29f | 4.09036 | -59.94877 | 2026-09-30 06:10:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 40fcff1b-bb50-32fc-aaaa-3f60b1a3f7f6 | 1.68377 | -55.90525 | 2026-09-30 06:10:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0b4e314-1f52-397b-99dc-aa43861a125d | 1.8073 | -55.64091 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30d5e1cc-1193-3d72-b57e-10fab105e5d3 | 1.81206 | -55.62835 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd5f960f-2074-3034-b1ea-7c51b59e6b0d | 1.80159 | -55.64764 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e149700-99e9-3bce-999c-bd7e8b37c683 | 4.078 | -59.93467 | 2026-09-30 06:10:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 634d3c68-9afb-3c68-ad15-6620d362fb61 | 4.08872 | -59.93908 | 2026-09-30 06:10:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 849c2568-c6ce-344d-bd19-43ddcc613351 | 1.80064 | -55.64192 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 945b35c7-e4d6-3442-8b62-8d730afe8250 | 2.54681 | -61.30553 | 2026-09-30 06:10:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43097573-7683-3c0f-93b2-5b367892eb5e | 1.8187 | -55.62718 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cd34b16b-0548-3a6c-b73b-02bc0e2853d3 | 1.82174 | -55.62678 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a36a0bb8-a42b-3607-91f6-bf03c353d0da | 1.81509 | -55.6279 | 2026-09-30 06:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b12a14f-6f01-3d1d-bfae-f9d2bbffb2b3 | 4.08383 | -59.93959 | 2026-09-30 06:10:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d40501a5-bd00-3f12-b103-5a931394c799 | -14.06638 | -46.3364 | 2026-09-30 06:12:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| b97425a1-2322-3bb8-b9ab-b52591910364 | -7.81423 | -45.82 | 2026-09-30 06:12:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ade15ecb-4125-3c9b-9863-df6bc80acec5 | -7.8324 | -45.79723 | 2026-09-30 06:12:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 32850c29-ff3a-35af-9027-e91bb59acb6c | -6.72076 | -45.58197 | 2026-09-30 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 7a91b238-5273-34d5-b8a3-b5e8691fd71f | -14.01321 | -42.90774 | 2026-09-30 06:12:00 | AQUA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| fe1a5739-797c-3354-af95-fa1ce6685a57 | -11.18758 | -45.14154 | 2026-09-30 06:12:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 301ef06d-ebd1-39cc-a873-24f361690242 | -7.84833 | -45.83042 | 2026-09-30 06:12:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| ecf16f17-dc5f-3477-aed2-da6068167d3a | -7.84218 | -45.82432 | 2026-09-30 06:12:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 1fd7e53e-21eb-31e1-a4ad-5af89ec498c3 | -6.71736 | -45.57391 | 2026-09-30 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 14857a71-9dfa-3f79-94e9-b7878b47535c | -14.19912 | -42.0701 | 2026-09-30 06:12:00 | AQUA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 81a54188-3281-310e-a8a7-d1861aaa1a61 | -14.11939 | -46.26157 | 2026-09-30 06:12:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2a3b81a0-9570-3619-8417-55d708a69174 | -13.43006 | -43.82219 | 2026-09-30 06:12:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6dc8c080-38c1-3dc6-8e01-7ead36eb9a1c | -11.3934 | -43.4688 | 2026-09-30 06:12:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README62.md)

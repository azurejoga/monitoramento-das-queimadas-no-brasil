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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c4cd268-41fd-3646-9165-8e15333d28b5 | -8.48026 | -47.29948 | 2025-09-10 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ed285d8-2cd2-3e37-a594-19060811316b | -12.85342 | -52.94856 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c0c4bf3-effd-3c5d-bb53-875eba1a0ddf | -11.80168 | -46.76689 | 2025-09-10 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76d04f38-bf2f-3aa0-a95f-fd6105bbdd2e | -13.00318 | -45.20808 | 2025-09-10 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc340ff6-46d1-3292-affa-0381d13a69ed | -11.56932 | -44.66332 | 2025-09-10 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 120a115f-d18a-36a8-9320-f35e36a6fc1a | -9.44868 | -46.73862 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e3efc51-6da5-398e-ae91-8810a617b593 | -11.44332 | -43.62359 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4f404c10-0ac1-3925-8d65-108e2e7cfdbb | -9.0645 | -49.83843 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a176be82-584e-393d-912e-24f07c6c17a3 | -11.33419 | -46.53024 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e148cb-38ce-3b86-8325-cbd1d48cede9 | -9.74994 | -45.40634 | 2025-09-10 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 92693801-79b5-3747-946f-c3ee7e96426c | -10.05191 | -59.36082 | 2025-09-10 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aed88b51-4c33-37c2-8071-9089406ee655 | -8.85705 | -47.23364 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d41060e-6d07-36df-baf5-6c9974e0b393 | -11.19733 | -48.38802 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45f5eb2b-7d7b-3706-9938-48c6ecc12360 | -10.88447 | -55.69477 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae67b746-5971-34ce-b961-96ff7aae3e55 | -9.04828 | -50.48912 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39cf617d-6da0-35d2-9459-1b53acec39de | -10.01416 | -51.67731 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| faf68434-b5d7-35e4-9d53-b0ecbd059b1f | -9.44642 | -46.70539 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ba9bc2c-7a56-3948-bc3f-77b0d7b1c92e | -10.3849 | -50.53909 | 2025-09-10 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 733c1591-3869-304f-9191-dfe950726676 | -9.13537 | -45.57019 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcbe57d8-f5bb-360a-ab74-6c19cd865f08 | -8.04624 | -48.6838 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 747368c0-299a-314c-8c0b-2a2e19e9fd7a | -9.09614 | -46.97783 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c8ddfadd-f27f-3046-9c49-bae4e32eb509 | -7.70002 | -47.2942 | 2025-09-10 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1cc8d3e2-e843-38b0-a981-d481d7ac064a | -13.19343 | -45.27728 | 2025-09-10 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e25ed7d2-6b4a-3612-a730-f7be44678ebc | -8.07349 | -50.18702 | 2025-09-10 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6243dd19-0c65-3c7a-a8f5-d6d4d0124c8a | -10.39067 | -48.8319 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47f4cf28-2046-3b7f-87ae-a7d6b2c644d9 | -10.38808 | -50.5481 | 2025-09-10 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47bd21ac-c61f-3b81-9c14-8fa9ee66e49a | -7.99864 | -46.33163 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b9d0d79-9751-30d5-9a79-623feb6dab16 | -12.01041 | -50.98692 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 4ba59f6b-980e-32eb-b8a3-a9a5181a6c3e | -8.09313 | -54.75218 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6576497-4fca-359e-9603-2416c42882a8 | -8.04893 | -48.69948 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f3a9a5d0-be8b-3483-878c-bde0fa72fac7 | -5.48156 | -51.22527 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a009779-3f39-39cf-bbd6-880370cfc0fc | -12.9877 | -48.0279 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 223eb7a7-40d5-35e8-b0a4-5f5c603d0bf5 | -6.8496 | -44.8976 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24130a5c-2967-3cea-b818-4e502be75e3f | -9.31387 | -46.73708 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eebc998f-5521-3c7f-851d-303204350d41 | -7.49397 | -48.23515 | 2025-09-10 05:04:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c96c4a8-8afd-354c-bb7a-6e095718879d | -10.01918 | -51.69936 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16fde3e6-9a16-397b-8db8-6360ebb7193d | -9.01871 | -49.78856 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4553bc3d-c8c4-31a6-ad8a-e19c30c4622d | -8.04485 | -48.69386 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 64c05d93-1d60-3292-903b-0b1a235398c2 | -8.52392 | -51.3859 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 566b1177-5edf-347a-9ae3-3d529f1fdd8c | -11.34364 | -46.54864 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4981d0c7-7a3c-3f67-83da-6cdfea935ab5 | -7.86998 | -46.02497 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5ee8a7f-1651-3036-baca-dcc269489952 | -6.64395 | -51.98877 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4d40293-193f-3299-aa34-6094d8759b3e | -8.49652 | -45.67007 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00465262-8dfc-34c9-baf4-db9aa453c4fd | -8.06765 | -48.63444 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fccc465e-8fce-3d93-b5fb-23a1677a749c | -7.19323 | -44.94064 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61467ddd-e393-3e56-8e42-9d8b41711017 | -7.48853 | -54.94851 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3da6fd5d-2ab0-36ee-b51d-bd3647a08e4b | -11.82723 | -46.74751 | 2025-09-10 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2112c381-ef1f-3cf6-98eb-5ee330ab5c4a | -9.30929 | -46.72901 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf319615-a429-330d-8dca-c901139e84f9 | -8.85854 | -47.23286 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bdabc41-66a4-3758-bd82-91d60a410a5c | -9.82256 | -46.05663 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf1aa046-310d-3dea-8125-d50f271ebb01 | -11.20442 | -54.98949 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2f83608-d05c-38d6-9299-cfe46832deb5 | -7.99361 | -46.32683 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7959228e-3558-3033-9106-f1a966b0ef40 | -10.8452 | -47.75592 | 2025-09-10 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d2b0bcc-1a3f-3754-bbde-454eb982c564 | -12.84189 | -52.94687 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d8c920d-c521-31aa-b011-35d3a665761d | -7.73825 | -50.75452 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c6ba7d4-019c-3ace-8fa0-9af1345a932d | -10.94943 | -46.80436 | 2025-09-10 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97d0bcfd-cda4-3db2-b7fd-cae34e4c32bd | -9.35616 | -46.50291 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d95ccb7e-2843-3363-a4a0-724b6e5daaf4 | -7.59231 | -49.28868 | 2025-09-10 05:04:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4431c20f-d1d7-3cdd-aa07-108ed2ea8d27 | -12.19702 | -53.86266 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57548dc0-a570-398b-b5fe-57e05ec98eb6 | -9.06149 | -45.73512 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13f94faf-bdb0-310b-a79c-2194cb8cd3ac | -13.02689 | -48.01849 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22d0b7a6-8a79-3ac7-a57d-cea837815d32 | -11.66741 | -46.90684 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a8c36bf-676d-3bea-b3df-f7c955530196 | -10.55811 | -51.49804 | 2025-09-10 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 392173d9-9218-350a-80b9-79b3301fade7 | -11.45847 | -49.27133 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2733e91-9d70-3d6f-8752-b014ae4970ac | -9.0511 | -50.49279 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4035ad23-520f-367e-a40f-a5d3121e82b6 | -8.04824 | -48.66927 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 03ec0900-42e5-3175-930e-cb0ab10fbaf9 | -12.01792 | -50.99642 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 36693e98-53d9-3973-88cd-795fa7c38a6a | -12.41298 | -44.71795 | 2025-09-10 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72966932-4794-3fb0-a0fa-6e3049ce8251 | -4.94219 | -56.15442 | 2025-09-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80cc8c99-f6ab-3a20-9c04-b92e548f4179 | -10.0062 | -51.70456 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37f5edfd-1e03-339d-869d-21fcbd31b8e7 | -9.01573 | -49.54675 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87cf9905-4c1a-3624-b53a-ae4d8bb9d4bb | -6.85705 | -47.93513 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2fc0b327-0272-34d0-978b-7bfef538f3d4 | -10.96993 | -46.80325 | 2025-09-10 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e02b2fed-0491-3af4-95b9-174990b77dfc | -9.06072 | -45.73017 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 565331c6-3bc5-399e-aad6-a151123d2b3b | -8.42641 | -49.11133 | 2025-09-10 05:04:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed24a4a2-2306-37c5-aa7a-24aeaae6b98d | -10.72644 | -48.29587 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5858948-8782-3573-afd8-2c462fd39009 | -8.0682 | -48.66557 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33b5be56-1ece-3a88-90ff-9710e2a38157 | -8.04963 | -48.69439 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 82eef798-01d4-317a-aaa7-79a3d5abbb75 | -9.04886 | -50.48512 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da0e3472-486a-3616-ba54-01489636ae71 | -6.67773 | -44.54739 | 2025-09-10 05:04:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a79418f-78f8-3e8e-b4f5-556128d50be9 | -8.44998 | -47.28498 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4196e996-3023-3d28-8fa0-aa2513fd30cb | -12.82719 | -52.93972 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01539326-e4c0-3310-b725-177f81021e8a | -11.99625 | -50.97734 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f08e96c3-b3bf-33b2-9ddf-258d41d17d27 | -8.46975 | -47.29776 | 2025-09-10 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1435d2fe-6d45-328c-ad40-f3729ee420dd | -9.51621 | -54.65337 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b845d37-1300-3c33-8dc1-c48d3953e5f6 | -12.99219 | -48.03555 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41c3a42f-4a0d-3024-a1ed-4a2836a2b1e7 | -11.13659 | -48.35241 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17f67321-8c88-3ed8-99b2-7c166d76b349 | -9.804 | -47.79356 | 2025-09-10 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a280207-bd6e-37fb-bd8a-f0d79ba9542a | -5.65825 | -51.26892 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 125bf345-74f6-33ca-87e8-8623465a9736 | -9.69087 | -46.81367 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e26cd3e6-4c19-38f4-b7ae-3a2263965fde | -10.18564 | -46.22105 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c91502f2-64ba-32f0-bc42-46afb74baeb3 | -11.66175 | -46.90615 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8489b926-c0ce-3f75-ad60-2fbfd891fc77 | -11.15994 | -45.28424 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93e0e947-aa9b-340c-8fae-9c7282d82b81 | -13.0265 | -48.0216 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c3c0732-e517-34fe-b9a4-fa23231a4d79 | -12.02641 | -51.03135 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53ecc7a0-c694-35d0-a280-44bbbd53efd5 | -12.84573 | -52.94743 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31c15fd3-eab1-387d-8b0c-ed9bc64cbbe0 | -9.06868 | -45.71461 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 606f05dc-8da4-3313-be79-04dd14d3c58e | -9.52191 | -54.63901 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d588f76b-f513-346d-b316-ea73826c639c | -8.84727 | -47.2755 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f91353f7-cb89-3086-b572-9e94683f4a4d | -12.98853 | -48.02116 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README92.md)

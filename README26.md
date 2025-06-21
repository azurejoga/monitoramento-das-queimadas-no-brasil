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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24b16bed-c9a9-304f-99d5-788f2384c69f | -10.86762 | -53.76312 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 987d6024-6f0c-395b-8c4c-349ab42f9c1c | -9.47549 | -57.84318 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c493b5bd-471a-396a-a361-50f66d3c7fdc | -7.27819 | -49.98742 | 2025-06-21 05:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac485dd7-9bc2-396d-a819-91ef9d07cbb8 | -15.62525 | -57.30711 | 2025-06-21 05:23:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb035b25-e8ff-3b13-9d6a-66c6ee45cbdf | -9.09552 | -50.02659 | 2025-06-21 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 659ff5ff-788b-36c4-825d-79db1db10198 | -10.89041 | -56.45738 | 2025-06-21 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 332ad633-41cf-332f-8979-11c55e244313 | -9.47008 | -57.82922 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e3ee79e-2bd4-34ba-97b8-6eb2d0b4d41a | -10.05269 | -59.35664 | 2025-06-21 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ed6e607-daf3-3479-99a6-0fb056839ce2 | -7.27761 | -49.9918 | 2025-06-21 05:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9678e12-b9e3-3fec-8682-ae4e7ba9391e | -8.73333 | -47.98544 | 2025-06-21 05:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 84f5af62-a019-3a47-9d07-f735fb367a90 | -9.01608 | -61.22207 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 306c5324-09ca-34eb-a145-936cfe128994 | -10.14769 | -48.98961 | 2025-06-21 05:23:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d41dbdd0-a99e-30c1-833e-491fc901bd72 | -8.01717 | -47.65773 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71cecf0a-b9b7-350c-9646-cd620ab3dae7 | -9.47374 | -57.82975 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2d475a3-274d-30d0-b453-ec1a2e8a238b | -11.77775 | -54.37064 | 2025-06-21 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b11f5c4-cc1a-3272-a688-e74fbc148594 | -11.87798 | -54.67429 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 0e0a1f01-b1f3-3292-a3f4-eb536fa28e44 | -12.45343 | -57.18918 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da849908-96b7-3618-a05c-a0c0e778b8a2 | -11.94535 | -58.74492 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2df0b130-e9e8-3ecc-8bc5-ea4298150980 | -10.23501 | -64.35712 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 018f4e9d-bc6b-3065-b113-073bf672994d | -13.04459 | -53.71298 | 2025-06-21 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8c5d9bf7-8473-3d39-bfb3-1cd5706a81cc | -21.08239 | -55.77224 | 2025-06-21 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb39331c-a002-34ab-bc5a-c8d3bfadc0c9 | -11.94054 | -58.75271 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c57ec965-a62c-391c-b777-550a09870abe | -12.50894 | -58.36035 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad573618-8204-30ab-aade-e9e76093727d | -21.44799 | -54.57355 | 2025-06-21 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5db07313-7018-3ab7-bc4b-d6a20dabe0fb | -11.87401 | -54.66883 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| a70586af-361c-3fc8-974f-7bfc51f49383 | -12.58035 | -56.99032 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fe85d25-d965-38e6-9e4b-11bf562fc97d | -11.52709 | -56.98074 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58d6096d-79fd-3f72-babd-0a557d3cc0d5 | -14.02706 | -53.36747 | 2025-06-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a477c63-8996-3c84-b044-faaf3df51491 | -12.02695 | -57.09375 | 2025-06-21 05:25:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f99d1386-a919-3bc7-91dd-95ecdd2c583a | -21.13056 | -56.233 | 2025-06-21 05:25:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 398463e7-c138-31e1-a031-b1dcc7797c66 | -11.78606 | -57.24579 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| e610ce41-e63d-3d8d-818d-523db5b6d76b | -13.24016 | -49.84337 | 2025-06-21 05:25:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fd4dcac8-e50a-30c2-876a-01601d429305 | -11.79454 | -57.24196 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a4692f3-7d4e-3d1f-a94c-d7177ff4adf0 | -12.51082 | -58.34716 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| eb1956c9-1faa-31c0-8bbc-318d13d41489 | -12.96881 | -54.68582 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc777c12-c860-337e-8e17-5ad97acb6df7 | -11.87863 | -54.66944 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 730efe74-93ab-3e40-a396-bed2305a98cd | -10.2379 | -64.356 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38b260ca-3e1e-31d8-a177-60439cebe7c5 | -12.02765 | -57.08867 | 2025-06-21 05:25:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7c5a2bd-bc87-3406-9bb9-71a61e01fc65 | -12.3083 | -63.73586 | 2025-06-21 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0ab9ae1-8de2-3e79-bcb2-9b6fa203e4ae | -11.87928 | -54.66459 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 365c052b-dec6-3a09-9248-b8a2f9113136 | -11.94176 | -58.74439 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e49731e-62a5-346d-b036-1c40ca662968 | -11.77302 | -54.37009 | 2025-06-21 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d7d9277-99f0-3239-9b4d-0aa40d2d0ae0 | -12.57696 | -58.38412 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efb444b4-c0c8-3754-815d-3dd975d46a94 | -12.47142 | -54.42862 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 34a436a9-4d8f-3540-a5a7-77c1cf1face3 | -12.02232 | -57.09821 | 2025-06-21 05:25:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9303affc-8620-3526-a5e0-f81e5c735158 | -13.14801 | -56.80938 | 2025-06-21 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44ca5009-8720-3f12-9675-b51cb174c4ab | -14.02186 | -53.36676 | 2025-06-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43fbc657-a7ec-3fd3-8816-27572548d5a7 | -11.79523 | -57.23701 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 639d2ccf-1b0d-3dec-9e22-542947c4cc4b | -12.28152 | -50.10905 | 2025-06-21 05:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63e998dd-8fb4-3afe-8a07-5306c0723af7 | -11.57496 | -54.56794 | 2025-06-21 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adf4ee16-1a18-3cb7-ab0c-50c84dcc4d9f | -11.95426 | -58.75911 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a85e9aeb-a302-3894-849c-236d39c40262 | -12.52197 | -57.21137 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cba2e6c0-dbea-3652-b6a3-125f00bad06a | -11.62321 | -58.29397 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 486b7fab-d490-307a-bb36-31bb3fa395c3 | -12.4793 | -60.13671 | 2025-06-21 05:25:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05972e16-b95a-3d6f-b759-3f3a7e4e24a5 | -11.86809 | -54.67789 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce2bb9f2-c740-37eb-94c3-1e6ec27c31a3 | -14.03825 | -53.36238 | 2025-06-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b85657b-8b93-320b-bc79-3057d50c09d3 | -11.61972 | -58.29201 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5dd77ece-24af-31e0-9a61-d02ea9510eea | -11.53104 | -56.98132 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3977eaa3-10cf-3ce5-8fc4-84094c55c19b | -21.69662 | -49.5034 | 2025-06-21 05:25:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 65a1340b-fc73-31f2-b843-5016b1ecb39a | -21.44202 | -54.57992 | 2025-06-21 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cc3725e-d476-3cc5-a29a-9f2d83947b12 | -12.88835 | -56.98409 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d5dcec4-8b89-3807-939e-cc81c5e72c75 | -13.36438 | -54.25999 | 2025-06-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4d4c69b4-2a3e-3dd5-99d1-290767e28764 | -13.0392 | -53.71535 | 2025-06-21 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0022f475-ee15-3b77-ac92-875835c9a645 | -11.53248 | -56.97103 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7891c7de-b232-3e7d-aa1b-c4c7a3665ed1 | -12.42529 | -54.87493 | 2025-06-21 05:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3d7b24c-c45e-31ed-afd9-a34c136a1be7 | -12.58083 | -56.9868 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea8bb91-c983-3713-9ac4-67c4a4650f09 | -14.03227 | -53.36817 | 2025-06-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7acdf519-dc6a-3f66-8d76-5b9e22fdd3df | -12.96948 | -54.68078 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ca570f8-da08-3c9a-9458-ebbcfeb7bb84 | -12.51898 | -57.20916 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8aee9113-558f-3caf-9df4-8ef4f2502d92 | -11.52854 | -56.97046 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57a3f89f-5b64-3ac1-8c0d-88de85e77919 | -11.79386 | -57.24689 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f61e7f6-36f6-36aa-b55b-bfbd0bc9989c | -12.47615 | -54.4293 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 59503abc-03ea-3f2d-9541-cdc5e93efc5a | -12.28896 | -50.09965 | 2025-06-21 05:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 237c5021-789a-31f9-926a-16ba38b1a054 | -12.30427 | -63.73902 | 2025-06-21 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b74508c6-8658-3670-bd40-66505c5493cd | -12.3117 | -63.73643 | 2025-06-21 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11c6f368-dd90-36b6-b857-96f90716b650 | -12.97613 | -54.68411 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f3e2871-327b-3760-99b8-148d2b6ae940 | -11.79065 | -57.24142 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 33093689-b329-369d-ac62-90c856576063 | -12.1304 | -54.66604 | 2025-06-21 05:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eae8f707-94d9-3216-a457-8ed86dde807b | -12.05878 | -63.77939 | 2025-06-21 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5963d12b-6194-3190-9bee-d2aa01a67b5f | -12.28838 | -50.10474 | 2025-06-21 05:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 781cd26a-b1ea-3887-ae57-74b444e35f0a | -14.02668 | -53.37069 | 2025-06-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b424d87-54e0-366f-a02c-bb9297cfbb7d | -12.88481 | -56.97995 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 105bbfb9-2ca1-31dd-b479-b325313405a2 | -11.95006 | -58.76271 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22826e1d-84ca-3c61-b3fc-2aabe9521f6a | -11.87733 | -54.67914 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1d15edb5-0ec4-3575-89ed-cc73c0714f90 | -12.89237 | -56.98469 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ba9dbec-afb7-3f71-85c2-111bd1ec3842 | -13.14393 | -56.80883 | 2025-06-21 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8e76cef-6bd3-3a5e-858b-0f46a21fac9d | -11.77368 | -54.36503 | 2025-06-21 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd2590ae-b64b-301e-ae4c-00ace0f98857 | -11.95786 | -58.75956 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 301d83ed-1122-39ca-a271-072b924f9ff6 | -12.02625 | -57.09882 | 2025-06-21 05:25:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f431df7-dfb4-3442-bf82-f198b7cb21fe | -12.57328 | -58.38361 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7edab711-d75b-33bc-a640-6a88684e7768 | -11.62338 | -58.29258 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3253d71-b36a-371e-82b3-e9890524acaa | -11.61956 | -58.29342 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce0e36a6-5b16-3828-ab0a-e8045ea4263b | -12.05475 | -63.78257 | 2025-06-21 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdf1c53d-e0ce-306c-ae40-9ed41da245c1 | -11.70528 | -54.50241 | 2025-06-21 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c0332a5-becd-39bc-8af8-6da71a49b5ff | -12.52292 | -57.20972 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fdec34b-9ad8-3a37-9c6f-9d81b6169cae | -12.57522 | -58.37035 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a8f191b-ca1d-3c55-ba5c-9268e1ba75a7 | -12.97887 | -54.68203 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf8316ea-d185-3d7f-b6c0-3a53b81b565f | -13.29163 | -57.08835 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b88153ea-0384-3dc6-8c58-0ac1b6923dc1 | -12.47278 | -54.42529 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8c82066a-e047-3094-9272-fa030058cd01 | -11.78996 | -57.24636 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |


[Clique aqui para ver as próximas entradas](README27.md)

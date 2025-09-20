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
| db436808-2fed-384b-a474-e635de94ff51 | -5.1181 | -43.1964 | 2025-09-20 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| abe9e167-0b8f-345f-9a10-f99a1cda742b | -5.118 | -43.2198 | 2025-09-20 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b77bc3bb-e28e-3178-9175-801910f2ca5e | -7.3847 | -47.0378 | 2025-09-20 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 05f39507-2770-3be2-a3b8-2bc16cef0f45 | -12.9049 | -46.7713 | 2025-09-20 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 83006c7f-fe12-3d34-8f00-9b27d58aac16 | -5.0992 | -43.2211 | 2025-09-20 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| e3801d64-9ef6-3f20-8d1f-94b8faeb7b09 | -5.0994 | -43.1977 | 2025-09-20 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| bf384780-dd53-3ea9-b5c8-5bff74a4f7fd | -6.5631 | -51.1126 | 2025-09-20 02:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 300e977b-516b-3e90-b36a-a51eba7c0aab | -5.1934 | -45.4835 | 2025-09-20 02:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 0a821f01-95f2-323f-8670-f69876f243c8 | -18.0502 | -50.935 | 2025-09-20 02:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 02682d6d-f375-31e0-ae93-4138f09eff12 | -18.0303 | -50.9385 | 2025-09-20 02:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 4f92fe3d-cde4-3496-844e-8894fa1b85de | -12.9242 | -46.7684 | 2025-09-20 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| c2dbefd0-c262-34eb-9a3f-0cdf6bce90a8 | -12.9045 | -46.794 | 2025-09-20 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 6b1279f9-a1ea-3e5d-8121-bd8216803c6c | -9.55803 | -67.46962 | 2025-09-20 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fb1987ea-ceb1-34b6-83d2-a5e835ce970a | -9.47273 | -67.89123 | 2025-09-20 02:09:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f5179d09-5a58-320d-b1e3-9009d3ca94cf | -10.6663 | -69.10381 | 2025-09-20 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 564fb91b-aeee-3ce4-8994-35138bddded4 | -12.9242 | -46.7684 | 2025-09-20 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 461e4efc-4338-3708-800a-b42c7472bad9 | -19.6073 | -57.7531 | 2025-09-20 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| eef4fd35-5bf3-3b9c-a93b-17799e508732 | -5.0994 | -43.1977 | 2025-09-20 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| b75b82df-9b5a-3b5e-94da-72d11a66fa15 | -5.0992 | -43.2211 | 2025-09-20 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8e1493c2-31db-3765-a468-7ad2b712c1d4 | -5.1181 | -43.1964 | 2025-09-20 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| e54eb6e0-cd1d-374e-84bc-511bb19bc8be | -5.118 | -43.2198 | 2025-09-20 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 34de33c3-d022-3c8e-8ce2-2a264fbe9045 | -12.9049 | -46.7713 | 2025-09-20 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| e2dc2b2e-db75-30b5-8026-a55e2afbec5e | -12.9045 | -46.794 | 2025-09-20 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| ba4c553c-f57e-3d33-a54e-065da09429ab | -19.5432 | -48.0301 | 2025-09-20 02:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 5213c840-d717-32c6-a4c0-069c08582db2 | -9.3614 | -40.4025 | 2025-09-20 02:20:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 6f6e43b6-711d-3f70-b01c-fc52cd5fef86 | -7.3847 | -47.0378 | 2025-09-20 02:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 584d6fc2-02ae-3564-b225-355cc860ca11 | -12.9045 | -46.794 | 2025-09-20 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 49bb9578-f0a0-3570-8a3a-81351e812859 | -5.0994 | -43.1977 | 2025-09-20 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3e931730-ca43-3ec4-8727-a04c72159148 | -5.1181 | -43.1964 | 2025-09-20 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d0b4e032-f588-3235-9620-abd805ebe223 | -5.0992 | -43.2211 | 2025-09-20 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 47e99e93-cb13-3e6e-be61-d549c2afe5db | -12.9049 | -46.7713 | 2025-09-20 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 4b4d3a41-a8d0-3056-b3d5-3c27b29008cd | -9.361 | -40.4273 | 2025-09-20 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.9 |
| e57cfcac-8e90-351f-9776-008d9c155233 | -5.118 | -43.2198 | 2025-09-20 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b1f74591-262d-3913-8094-8c2a6a0e263e | -12.9045 | -46.794 | 2025-09-20 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 813ffe28-bd66-3192-9288-8e99dfb223a2 | -5.118 | -43.2198 | 2025-09-20 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 3b0d4469-19d0-3f5c-8ba4-40949b384d5e | -22.8109 | -45.2767 | 2025-09-20 02:30:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.2 |
| 2f230d45-3e79-3672-81cd-86dc9501e4cb | -12.9049 | -46.7713 | 2025-09-20 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4d31e4d4-d23e-3e3b-ada3-f868c31d10d1 | -7.3847 | -47.0378 | 2025-09-20 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 522d1ff9-4aee-3180-b263-2921efd9a792 | -5.1181 | -43.1964 | 2025-09-20 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| f5b26349-2919-31de-9640-b2eea94b23e9 | -5.0994 | -43.1977 | 2025-09-20 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| de232ed9-7b85-38ad-bc00-3a400c580506 | -5.1181 | -43.1964 | 2025-09-20 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c055cd3b-7f3c-3841-b567-8068de9407c6 | -5.0994 | -43.1977 | 2025-09-20 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a166f356-b5a9-3400-b095-e95799ee0ac2 | -10.2762 | -36.3327 | 2025-09-20 02:40:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| c5499d17-de6d-3026-a21c-f6a73c553867 | -22.8109 | -45.2767 | 2025-09-20 02:40:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.3 |
| 3bdccb02-d89c-3cbd-99b2-e16e8cf22a81 | -12.9045 | -46.794 | 2025-09-20 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 5c4b56f0-7949-3554-8ff3-1a4362601bb1 | -12.9049 | -46.7713 | 2025-09-20 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| cc381e09-daf8-3512-a2de-fae97d34f3b3 | -5.0994 | -43.1977 | 2025-09-20 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| b41f8c20-5a11-302a-bfbb-4a46bb79ae82 | -12.9045 | -46.794 | 2025-09-20 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 04781f5a-abd2-39c3-bca8-7e92b788c97f | -13.0742 | -42.1505 | 2025-09-20 02:50:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 24774a27-0725-3182-8ae7-114f87c16329 | -13.0747 | -42.1261 | 2025-09-20 02:50:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 0157f5a0-e845-3e66-b59d-b44b74847287 | -7.3847 | -47.0378 | 2025-09-20 02:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 23335ce9-73b7-3fb0-a152-e3a0803b0517 | -5.118 | -43.2198 | 2025-09-20 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 60518302-4b91-3bb1-a4cf-0a0021d8bc31 | -5.1181 | -43.1964 | 2025-09-20 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d0cc756b-bbd7-383c-a740-fdc6898e101c | -22.8109 | -45.2767 | 2025-09-20 02:50:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.5 |
| 952f3ab0-2080-37ba-9a5e-34167542f53a | -12.9049 | -46.7713 | 2025-09-20 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 375e0074-46c5-3374-824f-cb4f1b3802e3 | -13.0747 | -42.1261 | 2025-09-20 03:00:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| c870d3e3-2e9c-330c-98fe-3ae5e7a80593 | -12.9045 | -46.794 | 2025-09-20 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 991ab4a5-7f36-3988-bc29-318762b22ce5 | -5.1181 | -43.1964 | 2025-09-20 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ae892530-5b04-3b96-ab8c-d286c201127a | -13.0742 | -42.1505 | 2025-09-20 03:00:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 55.3 |
| bcb91e3f-05d3-35ba-b1eb-95a4228af675 | -5.0994 | -43.1977 | 2025-09-20 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 377f0e53-55df-3cfd-9cd9-76c476c2b87f | -12.9049 | -46.7713 | 2025-09-20 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| b27a5fa4-0f17-3f2e-b70a-f4113312b884 | -22.8109 | -45.2767 | 2025-09-20 03:00:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.8 |
| 20f9b980-730b-3b91-b2f6-9bc965a6a174 | -7.3847 | -47.0378 | 2025-09-20 03:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| ad2921a1-f96e-3e45-9b18-8e3a8d6ba512 | -13.0747 | -42.1261 | 2025-09-20 03:10:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 75.5 |
| d7fcd08d-5ac8-3bf9-ae4f-82e5f76e74be | -13.0742 | -42.1505 | 2025-09-20 03:10:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 360ab0b8-48b7-3efe-b8b1-c0dc4a6d6cfd | -10.7769 | -45.96 | 2025-09-20 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 40bf2a30-6a46-3a2a-906f-856939eef356 | -10.7959 | -45.9575 | 2025-09-20 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| aa7d05c3-04c8-32c8-bd0e-b40c2454c6ad | -5.0994 | -43.1977 | 2025-09-20 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d1d6dd7d-d395-311d-a3a9-ef36699dfe38 | -5.1181 | -43.1964 | 2025-09-20 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 74b7e2f7-3a96-3cdc-8e3a-20d98ccc07ee | -22.8109 | -45.2767 | 2025-09-20 03:10:00 | GOES-19 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.3 |
| 123fce7f-16c7-3647-920d-39c7dda83489 | -11.26322 | -41.50364 | 2025-09-20 03:15:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 60281dc3-ef8a-30ab-b610-f22d9a2bcb76 | -6.19866 | -41.22548 | 2025-09-20 03:15:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 06587488-4a1c-3cab-99ac-9b9958282226 | -10.27669 | -36.34198 | 2025-09-20 03:15:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ab439316-fccb-3d67-8bbf-8b9fe5f104c3 | -10.27563 | -36.34771 | 2025-09-20 03:15:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a53019b0-6757-3d1e-8d5d-290c48a6a8a9 | -9.1389 | -40.1143 | 2025-09-20 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 55800065-8d61-3f43-9fbf-b6a6dc03de5f | -10.27172 | -36.34103 | 2025-09-20 03:15:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fdf712ac-dc3f-301f-a1fd-558471d47e32 | -6.1972 | -41.23308 | 2025-09-20 03:15:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ade909ca-8ac1-3f5c-8503-0f7c35a6a9c2 | -9.13998 | -40.10874 | 2025-09-20 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0750b7e4-7a24-38f3-8b02-d3f879f51fd8 | -6.19693 | -41.22727 | 2025-09-20 03:15:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a4d05fde-13e9-3dfb-a60b-a0b04d760889 | -4.91731 | -38.67854 | 2025-09-20 03:15:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f8c4acd-3f5b-3303-92e3-87f7023c82d8 | -10.27774 | -36.33628 | 2025-09-20 03:15:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5e1605b4-296a-3238-8591-8b94c6c6ba69 | -4.91641 | -38.68365 | 2025-09-20 03:15:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c490e19e-12ce-3103-9aaa-08284e7d685d | -14.72258 | -42.36818 | 2025-09-20 03:17:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5bd97d62-5a1b-3d51-b793-fa54e56bec0a | -22.80242 | -45.28457 | 2025-09-20 03:17:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.3 |
| 265990ca-a585-344a-b1d2-9a12953521df | -14.72773 | -42.37647 | 2025-09-20 03:17:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f9859e71-e798-3b1b-ab5a-ffff5ad92d1c | -22.79898 | -45.26966 | 2025-09-20 03:17:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| e5436caf-b7fb-372d-9103-a29878f87e58 | -15.67666 | -42.47486 | 2025-09-20 03:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a08ca4ea-53e7-3003-b54e-c7f746db9197 | -23.28454 | -45.78335 | 2025-09-20 03:17:00 | NPP-375D | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d0db68da-6830-3e89-a7f5-167733e5fb83 | -22.79893 | -45.27668 | 2025-09-20 03:17:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 11b85830-f101-36d8-af79-b5a6b6333800 | -16.32891 | -43.96469 | 2025-09-20 03:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19a15948-b275-3a76-83bb-241b99fd1544 | -21.94486 | -41.35826 | 2025-09-20 03:17:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 39da5413-f612-3bc9-a949-73c439c57e15 | -14.72747 | -42.36905 | 2025-09-20 03:17:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 59826e92-791f-325a-b6cb-fa35fdd15e58 | -22.79736 | -45.27618 | 2025-09-20 03:17:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 3a3b2784-e730-32da-a90b-54bdd2046826 | -23.29127 | -45.78548 | 2025-09-20 03:17:00 | NPP-375D | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| adcbe43d-2c04-3f21-8b64-1c00f29a1b0e | -15.68196 | -42.48233 | 2025-09-20 03:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8055cc8-6ab2-3d3c-85f0-12dd6d5ba8e4 | -21.94946 | -41.36354 | 2025-09-20 03:17:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 73a8226e-5643-369e-829f-27545075bd84 | -16.32718 | -43.95996 | 2025-09-20 03:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2ba9867-da69-324c-9717-5c43e938e292 | -22.80399 | -45.27826 | 2025-09-20 03:17:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| f466bfb2-e582-3ded-8322-56c7767bf6cc | -22.80396 | -45.285 | 2025-09-20 03:17:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| baa330ae-dc67-3dc1-ab94-9764afa1e29f | -15.67881 | -42.48235 | 2025-09-20 03:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README6.md)

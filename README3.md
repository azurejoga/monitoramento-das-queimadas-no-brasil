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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af467479-37ec-3810-a0f7-50ed4de30382 | -15.9921 | -41.9885 | 2025-06-30 01:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 489d3109-e3f4-30b1-bbe6-a446f0393099 | -12.0705 | -48.4716 | 2025-06-30 01:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 6dc17949-4fc0-3a7e-bc0e-7da5801a008f | -12.0708 | -48.4495 | 2025-06-30 01:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 567dfed0-453b-3432-90b8-eed4dca7ba4e | -11.9469 | -57.4503 | 2025-06-30 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a31d050f-3df8-3fcc-b355-a0ad3e9fea76 | -10.8046 | -44.2553 | 2025-06-30 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 3b0d4214-d63a-30ca-ae32-0f800180ab8b | -12.0705 | -48.4716 | 2025-06-30 01:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 2964f6c2-1809-38c0-8380-e9dfe448efd7 | -12.6319 | -54.2087 | 2025-06-30 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 399c23c2-95fc-3525-86cc-8d31374e067f | -10.7859 | -44.2346 | 2025-06-30 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| e380fdbf-3693-3da6-9f57-9ccf0b543d4b | -12.6316 | -54.2293 | 2025-06-30 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9ae08dbf-58c5-35af-a83e-3cda808bc8ed | -9.2522 | -58.7584 | 2025-06-30 01:30:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| b7dc161b-59e3-3447-bb96-4a4ad748698a | -10.805 | -44.2319 | 2025-06-30 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 201.5 |
| f0a64fe4-3d53-3725-8cd7-ecba56897ddf | -12.6128 | -54.2107 | 2025-06-30 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 91a45fd3-7a75-341e-8779-60f1877068a3 | -12.0708 | -48.4495 | 2025-06-30 01:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 81efb380-b4ff-38b6-a880-f37fe60982a6 | -10.8573 | -53.7425 | 2025-06-30 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 59659828-37ee-3b6f-a4e0-093bf6355cd1 | -15.9921 | -41.9885 | 2025-06-30 01:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 55.5 |
| e4e5156f-2cdc-38ca-b439-c3e504da671a | -10.7859 | -44.2346 | 2025-06-30 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b65421cb-b21b-3d8e-9440-f2d0f75258ad | -12.6316 | -54.2293 | 2025-06-30 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| c7862372-1213-396c-a6bf-dcdc9e120493 | -12.0708 | -48.4495 | 2025-06-30 01:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 57181724-d342-3c45-ad38-155c582bd3c3 | -12.6128 | -54.2107 | 2025-06-30 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b31d83b6-7f84-3334-a773-aabbd9e30b6a | -12.0705 | -48.4716 | 2025-06-30 01:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 81381187-9e1a-3779-b1c8-6c45e580ca3b | -10.805 | -44.2319 | 2025-06-30 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 272.5 |
| ff56844f-e1e9-3fd5-adc4-9c30aaa5e55e | -10.8046 | -44.2553 | 2025-06-30 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 7c23bfdb-bbed-339a-99c4-8203ee36e139 | -11.9469 | -57.4503 | 2025-06-30 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c7aad7fc-9720-3173-aa9a-6659c943478d | -12.6319 | -54.2087 | 2025-06-30 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 80534eae-8dab-3a64-a7c2-1786a168c65d | -9.2522 | -58.7584 | 2025-06-30 01:40:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| fa78d6bd-dd70-3dcf-a204-263a69f897bf | -10.8573 | -53.7425 | 2025-06-30 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 55e9f92a-867c-322e-82f1-be28219d4251 | -10.8241 | -44.2292 | 2025-06-30 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 0fe88942-5c36-3096-a50f-6c6a5685cd8f | -10.8573 | -53.7425 | 2025-06-30 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d2e54ab9-ed34-36e1-a094-28ba53ea6204 | -10.805 | -44.2319 | 2025-06-30 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 315.2 |
| e29f521b-1332-398c-8f69-c827a5197e2e | -12.6316 | -54.2293 | 2025-06-30 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| dc51cf64-9f1e-3ebd-99e0-4923f071dfe1 | -11.928 | -57.4518 | 2025-06-30 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| da501217-8024-379d-bf7a-ee35f39d2464 | -10.8046 | -44.2553 | 2025-06-30 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| ec745410-b3e8-3245-8e0f-bf294b82f487 | -12.0708 | -48.4495 | 2025-06-30 01:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| e21a5ebc-542b-30d9-ba25-314a570391b4 | -12.6128 | -54.2107 | 2025-06-30 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| dfa04489-154f-36e4-8d27-db8361b0a840 | -12.6319 | -54.2087 | 2025-06-30 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c30a2951-ca17-3072-9b5e-4b68363bdc90 | -10.8054 | -44.2086 | 2025-06-30 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 90d56b2d-aed0-33a1-b27d-41dd2b310e59 | -10.7859 | -44.2346 | 2025-06-30 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 90775825-1a8e-328a-9718-74f599b9bece | -11.9469 | -57.4503 | 2025-06-30 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 18aa9084-25d1-3eb4-b03d-32885cc836c9 | -10.805 | -44.2319 | 2025-06-30 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 319.0 |
| ae5d0865-4817-37d3-bb9e-60a7e3549771 | -12.6319 | -54.2087 | 2025-06-30 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f04d9a00-9b24-38b4-9834-c50cfc77026a | -10.8046 | -44.2553 | 2025-06-30 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 206.0 |
| a7abdc2b-d22b-3bbf-b8d8-b1661c705332 | -10.8238 | -44.2526 | 2025-06-30 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f152f01d-9807-38d2-bcd9-0cdab865b768 | -10.8241 | -44.2292 | 2025-06-30 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 08c140a1-8797-3da8-b505-c2be0c805094 | -10.7855 | -44.2579 | 2025-06-30 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 5ec0d649-155c-32e8-888a-a3dd47b2698c | -12.6316 | -54.2293 | 2025-06-30 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 8797b5fa-1566-347e-85e6-edbe5be5348d | -10.7859 | -44.2346 | 2025-06-30 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 5daca545-b4d8-308d-9d59-c4f608639de0 | -10.8573 | -53.7425 | 2025-06-30 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6c1dfadb-6ef8-3512-80da-320a3d70fa43 | -9.2337 | -58.74 | 2025-06-30 02:10:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7f5d41fc-e058-3c38-9782-46a9b1323c30 | -12.6319 | -54.2087 | 2025-06-30 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 75b9e562-e39f-32fe-a16c-f067703d378a | -10.7859 | -44.2346 | 2025-06-30 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 5d9598ac-46da-34db-a5b9-f49c2c2d52e7 | -12.6316 | -54.2293 | 2025-06-30 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| cc0b278f-43f2-3678-86c8-7ff0afdc6bdb | -10.7855 | -44.2579 | 2025-06-30 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 99a30833-878b-37ca-88e9-bcee071f0fa5 | -10.8046 | -44.2553 | 2025-06-30 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 06baeab1-ff33-33ed-a0d0-ab393f2f44ce | -10.805 | -44.2319 | 2025-06-30 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 277.8 |
| 210a5cc3-7a2d-3f7b-b0fe-09ac1c322dc9 | -10.805 | -44.2319 | 2025-06-30 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 246.2 |
| b8d8803e-ac2c-34a7-bb48-bdd0cac6ab2e | -12.6128 | -54.2107 | 2025-06-30 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0104cc50-69db-34d1-93ca-bf34eb5557f8 | -11.9469 | -57.4503 | 2025-06-30 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c1a3adbe-a5c4-305b-9d8e-39f576354a4c | -10.8046 | -44.2553 | 2025-06-30 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| b251fa12-78a1-3b74-bee8-55e76b03da2b | -12.6319 | -54.2087 | 2025-06-30 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fb5bd2b0-c8be-31d9-934a-5001e0d34e86 | -12.6319 | -54.2087 | 2025-06-30 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8d3abf71-d62e-35ae-a1f1-d87f484f2c64 | -10.8046 | -44.2553 | 2025-06-30 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ea90f3d6-36c4-38c5-ad59-f9a148673d1f | -10.805 | -44.2319 | 2025-06-30 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 41403a31-f953-39aa-8d73-86d2b1e997b9 | -12.6316 | -54.2293 | 2025-06-30 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 99102a3b-6aaa-3851-a7fa-90b6f5ceea2c | -10.7859 | -44.2346 | 2025-06-30 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b75539ab-75bf-33f2-a920-bb82eea97663 | -10.8573 | -53.7425 | 2025-06-30 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e0119876-4dfc-35b7-bf84-bb8868a8d7c3 | -10.7855 | -44.2579 | 2025-06-30 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e306fcca-1c8d-31d6-99e6-b929b2208b07 | -10.7859 | -44.2346 | 2025-06-30 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 48338f17-8f60-3898-b6d5-4808fdd24702 | -10.8046 | -44.2553 | 2025-06-30 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| b5ba9c04-7371-3ed9-91d7-c0433f6010b4 | -10.805 | -44.2319 | 2025-06-30 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 201.1 |
| dfebe21a-5b7b-327b-b4be-7e71fbc35da4 | -12.6316 | -54.2293 | 2025-06-30 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4ea4b17d-3fb9-311c-b513-b3a525fc99fa | -10.8573 | -53.7425 | 2025-06-30 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 0b97c053-0ba9-3f7b-bab6-3db1114abbea | -12.6319 | -54.2087 | 2025-06-30 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 31c59928-468d-3300-8b27-7f373cd2fcef | -12.6319 | -54.2087 | 2025-06-30 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 895c6e8a-b669-3a98-a513-a1868ba18bf7 | -10.8046 | -44.2553 | 2025-06-30 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 83abac91-994d-3726-b71a-6430fd4270e3 | -10.7859 | -44.2346 | 2025-06-30 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b0812d43-a411-33e2-a097-aa543740bc0f | -12.6316 | -54.2293 | 2025-06-30 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8e6f64d8-0dfb-3eed-9438-d5989ded2415 | -10.805 | -44.2319 | 2025-06-30 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 0efc66d2-baf8-38d3-b811-5b80f31cc801 | -10.805 | -44.2319 | 2025-06-30 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 7482719c-2833-3579-81b2-466bb17ed085 | -10.8046 | -44.2553 | 2025-06-30 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e33fbf99-4c49-3082-9020-a0c51b7daebe | -12.6128 | -54.2107 | 2025-06-30 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 66e37fce-3b4d-393d-9030-b7d949fee6da | -17.8818 | -53.263 | 2025-06-30 03:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 28acc86b-aa5e-394f-a1d3-44a9678f44b2 | -12.6319 | -54.2087 | 2025-06-30 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9d97bc3e-e1ba-3e65-bd47-c9403d9b000e | -10.8046 | -44.2553 | 2025-06-30 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| abc0132f-6df7-35b7-ba67-a3db86d3b34b | -10.805 | -44.2319 | 2025-06-30 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 2bc4a9ba-cb3a-3807-9096-cfa42ee303dc | -10.8573 | -53.7425 | 2025-06-30 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 91d55503-dfaa-338e-9b92-b45a8537aa26 | -12.6319 | -54.2087 | 2025-06-30 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 644a41b2-4e98-3eb5-afef-8aef7b91341b | -10.805 | -44.2319 | 2025-06-30 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 371fb5e4-023c-3354-a7db-e26ee1cc5689 | -12.6319 | -54.2087 | 2025-06-30 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1180a62d-d16a-32c4-ac38-a3a97677328b | -12.6128 | -54.2107 | 2025-06-30 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| d396b545-49a9-3dc3-b9ad-3d3b2781fe2c | -10.8046 | -44.2553 | 2025-06-30 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 991046a5-e335-3d1c-a146-d9699683af4c | -5.07189 | -37.71763 | 2025-06-30 03:21:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6a43114e-e626-3b4c-96c9-dddb3276cfca | -7.26014 | -43.16313 | 2025-06-30 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c90464ea-ef8d-354d-9b54-ec58d8583f29 | -7.26087 | -43.16198 | 2025-06-30 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b766e3fc-baba-3c4d-a425-08528b36ef1c | -7.25906 | -43.1688 | 2025-06-30 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ec0a0d0b-d597-3bdc-9b07-3ffc2d6f53d5 | -7.19165 | -43.70725 | 2025-06-30 03:23:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f01ddbb-c522-3998-b096-ed1e286f164a | -7.25983 | -43.16766 | 2025-06-30 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b06fd5e0-b846-3f4f-be57-fd8da4693ccb | -7.19277 | -43.70134 | 2025-06-30 03:23:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d618171-fe3d-3fde-b0a4-7a537886457c | -10.79771 | -44.23751 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 83b8718d-445a-36f1-897a-3d1807749950 | -10.79943 | -44.23402 | 2025-06-30 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| a5efe458-b9b2-3085-ba98-71398e73b27c | -15.98771 | -41.98967 | 2025-06-30 03:25:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README4.md)

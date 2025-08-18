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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c60dfe3-073c-368d-a74e-123511252807 | -12.93364 | -46.13576 | 2025-08-18 04:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3286e46a-5572-375b-a58f-f416d32d0193 | -14.98882 | -49.56195 | 2025-08-18 04:49:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fe2a231-d348-35c3-a555-8e2fa233b0fc | -12.6139 | -46.90459 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 835a2565-7f9f-32dd-8071-8a0265054520 | -14.18307 | -45.31232 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fca6ef8-92c9-3776-9fb3-1b20c4ecab36 | -13.58088 | -46.9903 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3174a0a0-8052-3fb2-ac07-61e569abbb66 | -16.16219 | -50.0294 | 2025-08-18 04:49:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7aa7ed02-d875-3989-bb5f-c9ccaabcc928 | -13.24423 | -50.79256 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f980d99-0637-3751-ae9a-475841e39f88 | -13.17265 | -46.88391 | 2025-08-18 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 369e2ecb-78fe-3530-bfa7-165644c01179 | -12.91937 | -46.11415 | 2025-08-18 04:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0302b445-ccdf-39b6-8815-81e898dee768 | -16.21655 | -48.60504 | 2025-08-18 04:49:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05166df9-62fb-3296-a40d-9f9f4712bfe5 | -14.99427 | -54.78468 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17e5dd0c-bc82-3f98-b5c3-da5ec8c2af6a | -13.22697 | -50.74403 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 53f027fe-f83f-3319-91da-ed01635e8449 | -14.19224 | -42.81063 | 2025-08-18 04:49:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a92d942-e402-3ac8-ad01-b1e4affeb2cc | -14.9839 | -50.12892 | 2025-08-18 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0aad6416-a824-3265-923b-14834df9a7a2 | -13.45867 | -55.10448 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17662300-d239-3d01-b022-a938e52d2dc4 | -13.22183 | -50.75492 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 12effb42-7201-3c4b-ac3e-e921cc073257 | -15.72854 | -48.42115 | 2025-08-18 04:49:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc091f9a-dc87-372b-ba08-3931a04dfbe8 | -12.53335 | -48.49821 | 2025-08-18 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| de841f17-ed50-3afa-a731-d1a935363742 | -15.0431 | -56.03158 | 2025-08-18 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa3326be-84be-3fd7-b073-5ed9e04d4b25 | -17.39276 | -42.61769 | 2025-08-18 04:49:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 36df9954-e103-321e-b1f7-c5198455bb48 | -17.10076 | -49.88035 | 2025-08-18 04:49:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 4eaf77d7-1c23-3628-9f69-61763e1b157e | -12.4502 | -46.99312 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b213a31f-9a0c-3a06-abcf-6152d4e1f949 | -13.21783 | -50.75819 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| d495535b-96ff-3ee9-9466-a081e8e80e0f | -13.24766 | -50.79309 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c501f9b-48c0-3e2e-a4ca-a728f923c920 | -13.21327 | -50.76527 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab5868bc-d576-3b56-b5e7-537df28a7aed | -12.92752 | -46.113 | 2025-08-18 04:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 26e9ec52-63cf-3ca7-ba73-137bdb69d4dd | -12.53714 | -48.49875 | 2025-08-18 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13f6ace9-9dee-33e5-8dc0-1557db2a8177 | -13.01007 | -56.84661 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69b31484-e6e0-3e81-b036-ef3e010a5b4a | -13.25269 | -50.75883 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cac92e14-c14d-3220-baec-f7f783233b31 | -17.09643 | -49.88433 | 2025-08-18 04:49:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| b890cb09-ebff-30bd-b83b-af3aedd9dcb4 | -14.98092 | -50.1242 | 2025-08-18 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7af88af6-fa50-3a2c-a237-9704d90adc41 | -13.98441 | -48.10595 | 2025-08-18 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00686de8-7067-3b61-b737-16da6c458bca | -12.9874 | -56.84245 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a55ca263-6546-3739-bbdb-9a235c164b18 | -13.22755 | -50.7636 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| dc5dc653-07fd-3c1b-8dcf-53a06b670daf | -12.99416 | -56.84851 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a4b2bcd1-6c11-3fba-a637-8764b8caf75e | -13.6021 | -47.73903 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de1811c9-de67-38a2-bc4e-c4104d67d2ac | -13.02161 | -56.84643 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e080721d-af8b-318e-ad46-896622b1707a | -14.73101 | -59.6743 | 2025-08-18 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7c4ca2e-5485-3e89-b60c-d511dffb49ea | -13.23098 | -50.76413 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 2f501333-e6a7-3191-b56d-9f3969c9993e | -12.1236 | -47.90272 | 2025-08-18 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae41545e-87fc-3472-a5a7-93d6ca984a5b | -14.18181 | -45.32288 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d384c56c-085f-32f7-83d3-0a14fdbb142a | -14.28847 | -53.19644 | 2025-08-18 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce2fa596-d33f-3cdf-bbba-57b070d39d8c | -13.29566 | -50.82389 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cfb8624-adce-3012-a2b3-90a9169c18f4 | -15.1422 | -48.76609 | 2025-08-18 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7543b620-ff81-378c-9427-ab2a2830fe4a | -15.60941 | -54.3044 | 2025-08-18 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f53afa69-2388-38b8-9028-981c4db148bf | -12.93583 | -46.11874 | 2025-08-18 04:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117b959b-e8ef-3b49-882d-ff4e90c1eed2 | -13.58724 | -47.75804 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e4468926-beb4-3126-8297-7335d3315179 | -12.63263 | -46.89243 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 548070b1-71c3-38e9-8706-d4cdfff21c3f | -15.31851 | -52.97994 | 2025-08-18 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76760221-29b4-3a36-b0b5-b95859c73d6c | -13.21897 | -50.75058 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 32402a07-7ae0-37cc-8501-47642da9bf09 | -14.9921 | -54.77665 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d945034-7198-3db2-be85-e1b5bfcb0ae8 | -13.23784 | -50.74181 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f8089d0-54d7-3ed1-a070-53ffbde6f68c | -15.00513 | -54.78988 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 107d008e-35de-36eb-85b7-f3460274dc14 | -12.99119 | -56.84312 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9489de35-80b7-3c3e-b1db-bf94aff11290 | -12.1197 | -47.90208 | 2025-08-18 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eac7fd5-06d9-37db-8908-0db549a0bf5d | -17.09767 | -49.87521 | 2025-08-18 04:49:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 7f6ad94c-77a3-3819-bfcc-201fefabd906 | -12.12842 | -47.90039 | 2025-08-18 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 614e8f0f-5348-30ab-a18e-81f7b1f97519 | -18.04909 | -43.81381 | 2025-08-18 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 61da1c52-092f-3dc6-b633-a8ffbc2f26ce | -11.31602 | -55.21055 | 2025-08-18 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5055552a-f221-31fc-8f89-ccf0dce5637a | -14.99826 | -54.78143 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3f26271-91aa-3c0f-9b0e-0b167a89f98e | -14.95764 | -54.77486 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbd9e76c-9b67-3d48-8b49-83b732290bf5 | -13.01682 | -56.85267 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eba187a0-c178-36c4-9ca2-edf702d4ce8b | -12.54028 | -48.50393 | 2025-08-18 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddca1c9e-b5be-32f5-a02d-f6b9b74c20d1 | -16.72907 | -47.62297 | 2025-08-18 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8312e643-f5c4-3c71-9945-927ba6877d23 | -13.16914 | -54.9213 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 84df396e-6dd8-3958-b660-98ac3002c97d | -13.17475 | -54.93019 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0391ab99-b0e8-3f00-aa9e-0a1f3b0c5460 | -13.13716 | -57.14654 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 811d81b2-03b3-3c7a-8088-7e0521df3a7f | -11.84909 | -51.58689 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c426eda-802e-3085-8da1-a77abe1ad6a8 | -14.28903 | -53.19289 | 2025-08-18 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e846a4b-f100-388a-ba75-2b68501a054d | -12.8927 | -46.11062 | 2025-08-18 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d46fc21-df60-37d0-8aa4-65c89404b325 | -12.56569 | -46.93818 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd9018f2-bacc-31ef-9b2a-87d0250442ac | -13.16978 | -54.91743 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e5bddb5-fa17-3a4d-911d-9df010245a44 | -14.95611 | -54.76303 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dbb8dae-49c1-3691-a386-bb17085fc724 | -13.97084 | -54.07979 | 2025-08-18 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8a88bd9-731e-3e7e-92aa-32b531d2a48b | -12.99576 | -56.83912 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 727b62cd-503f-3250-ada6-b62481776151 | -11.84406 | -51.57515 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57824837-15e8-3e05-bb0e-0a0657133615 | -16.62566 | -51.36222 | 2025-08-18 04:49:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73530555-84ed-384a-9854-16a90436ce53 | -14.18244 | -45.31762 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c5781bc-f590-3cb0-a3eb-1b8b5e07728f | -12.63679 | -46.89331 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29e312ce-c7dc-3482-a5e0-ed15526eb5cf | -12.98876 | -56.85727 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 85c8995b-8e25-3217-8614-9abaf80c153f | -13.22526 | -50.75546 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bcfc1f33-5f6e-3a39-95ab-5830ca4be521 | -16.7915 | -50.09415 | 2025-08-18 04:49:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d13760f-f866-3f59-ba89-9f4fa0a28d40 | -13.20012 | -50.75933 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42a27a78-be9e-393c-92e4-b68df8727f05 | -13.87249 | -45.53881 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de5c150c-7842-35b0-bd01-ac4c78d3ae09 | -13.22127 | -50.78209 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 95ebddc3-75cd-3d9e-a774-f4a481360530 | -14.59277 | -47.96104 | 2025-08-18 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ea771e-9ed0-351e-adc4-8fb70bd78966 | -13.24127 | -50.74235 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09f665d9-9315-34a6-999e-75ef2a3c4664 | -13.22355 | -50.76687 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 343c5bda-72b8-30e3-b33b-57a7d5c3c276 | -15.14429 | -48.7631 | 2025-08-18 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf90005a-5f27-3241-b774-612ac9d5b018 | -13.43815 | -57.02499 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59a8120c-f3a9-3789-908c-af2c0f9358f9 | -13.25325 | -50.75502 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1e3dec8-277e-3031-b35c-4ba62069d041 | -11.9253 | -50.42929 | 2025-08-18 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 385c1061-56c2-3f7a-8b41-0b2fffe0aa97 | -13.22527 | -50.77882 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8bafdb79-65dd-37ad-9ce1-95c9f9100499 | -12.54474 | -48.49973 | 2025-08-18 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e15ddb4-d739-3d84-b141-af7d11496a5f | -12.63627 | -46.89723 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e17726c-d023-3abb-9ad4-bf118c3349b0 | -13.21497 | -50.75385 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c9cf507d-6d5e-3428-9e66-9e0e4edc50df | -13.13755 | -57.1215 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 492324ec-afc7-3904-a9b6-ad2f73d1646a | -12.57513 | -47.05473 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53d69c54-6833-3577-b6e3-50a239fb5e7e | -16.63488 | -51.3717 | 2025-08-18 04:49:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37f331f1-89f8-387f-8ffc-bc9912a2f161 | -13.43474 | -57.0259 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)

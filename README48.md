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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c60be86-07ef-34d9-a798-d76b244d0390 | -10.52854 | -57.45244 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49a529ca-b84c-3e69-b539-deb431ec45b2 | -13.05492 | -50.62612 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5ba2872-dc2e-33bd-9ec6-327769486fba | -10.82944 | -50.78552 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d944b0f3-28ee-341c-9813-1597f5c1e10b | -11.11859 | -54.01003 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25d83587-8593-3359-a40f-31fb3a4a660b | -11.86486 | -48.97898 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1d94dbe-35cb-32bf-91f9-efef1da914b6 | -12.8024 | -54.06321 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 356aca16-79fe-360e-b584-7968d03af133 | -12.36437 | -43.85842 | 2026-09-21 04:21:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76aaf9e7-3edc-3292-bf89-21d00c858fbd | -10.93183 | -47.87197 | 2026-09-21 04:21:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea55164f-0314-36fa-96c9-9a4e7721970e | -10.38251 | -48.91097 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9d83005f-012b-39a2-bcde-a6f1b29825c1 | -11.94129 | -46.49941 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daafece7-1d02-3abf-bd52-08bc30d2250d | -10.79862 | -50.8295 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57ab6c25-48ce-35bc-a949-2bc9043bd62f | -14.66803 | -54.47472 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ce48130-ed8b-31c3-9efb-fda7c08dcbe5 | -12.63015 | -50.92213 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 466209b2-ae76-3264-ad3d-efe77017959f | -11.72243 | -54.56966 | 2026-09-21 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a51355b-67c0-3aec-8eaa-679f52bc3b77 | -13.72314 | -48.79195 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2d84a99-9549-36df-941f-7b74ac8918db | -11.46746 | -47.76702 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e1f2cf6-845d-3efa-9eb1-3fce2f90340c | -10.21894 | -53.92282 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bb7e444-3061-3b3e-b7cd-546d63491b7c | -9.82104 | -48.4123 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7df88f6c-a0f7-3edb-835c-4d6868749677 | -10.47986 | -50.29076 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0ec4d947-36ad-3424-a623-3d411b3d56d3 | -11.02782 | -54.15537 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 042ec462-60b5-31de-bad6-0a4dfa4e8ed2 | -9.81882 | -48.41477 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1870fff6-cbe3-3dd6-9991-ee6e7c6acaf3 | -10.37949 | -48.90856 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ab187ab2-d2fa-3151-8871-0b6784778280 | -17.01749 | -47.13427 | 2026-09-21 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5344622b-7b10-3d30-9ae4-7c5c7482593b | -12.56816 | -47.07569 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d01fc4f1-c742-3c48-a765-04c363000622 | -10.80824 | -50.7771 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7d77cd0d-61b9-324d-abd6-a2595ae8a94f | -11.11722 | -54.01714 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e89498f-fe6e-3cb0-b864-ea8ff237e035 | -13.43023 | -46.32719 | 2026-09-21 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcae7b28-3fe0-3d5f-9eb3-d5ef0817d3db | -10.47913 | -50.29485 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8a436200-6d47-37b9-b0ed-8cbdfca57044 | -10.45995 | -50.27865 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 08d79d9d-d3b1-3827-85c2-aeb48b2464bf | -9.82669 | -48.44818 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aec68df0-5b8b-39af-8956-6c79b75e2452 | -11.02512 | -54.13969 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54f283e7-71ec-3417-9bc8-1b102b08a790 | -11.32962 | -47.29847 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 848d23b7-9e20-3317-92ea-5706f918ef19 | -11.40579 | -47.34063 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4883133d-37aa-3a8a-bb74-beb94414e07b | -10.87118 | -50.93437 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db3f03e0-b30f-378d-a51f-64fa9fdb9f0e | -10.37046 | -50.2208 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5d363bd3-bdf0-3409-83da-54dcf7f1bc36 | -15.4432 | -48.45889 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5fc7e8b-99e4-3f78-81bc-a039540b99ee | -10.15036 | -47.67801 | 2026-09-21 04:21:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f092395-12d6-3718-82c0-a368baa9cdb5 | -11.04281 | -54.16634 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceb05389-d1bc-3eb1-b8f5-2abf942f7188 | -10.82504 | -50.78471 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b0dd942-f12b-34bc-9e9e-fa00357b3f1f | -11.97849 | -44.9925 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9bb06fb-a48b-39d5-9f91-16fc8c9643ba | -10.87953 | -54.06931 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 801df900-03f5-336c-a796-441f88379853 | -14.06078 | -52.11512 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2facacdd-023d-3dc1-ab08-647edd041171 | -10.4776 | -45.09087 | 2026-09-21 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c68db0c4-f530-323a-b5d2-2e651a3c5a56 | -11.04025 | -54.15107 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67c9a054-5a98-3ffe-8390-b3c696844c8d | -10.58541 | -57.48392 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7afb805b-b9e7-31d9-a2b5-d5922cd3c299 | -10.4775 | -50.32849 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fb28699d-ae6e-3a2d-adee-19d1689f36ea | -11.7918 | -49.8092 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1d068a2-c309-3096-b017-0bccb227a85f | -10.46628 | -50.29249 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9797efe8-d0eb-36f3-be56-f2a6c856cc67 | -10.81478 | -50.14444 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18681ae4-ae01-36a1-8b66-05508111ba71 | -11.71542 | -54.57615 | 2026-09-21 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c63ff735-3569-39e1-a4b6-77a658328180 | -9.0211 | -51.53265 | 2026-09-21 04:21:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a453e0d-4a89-32bc-81ac-e91959e178cf | -10.88527 | -53.98118 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fbf5daa-11d7-383f-9500-2716ccb8ce64 | -10.55731 | -51.29318 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fecbe575-01d2-36a7-ac39-0ced9fe354ce | -8.18764 | -54.70202 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff34bf7d-9c3d-3e26-9210-37901ae66a7d | -13.9298 | -47.84184 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3133c252-92fd-3a09-af00-c3dfeff27db9 | -7.56386 | -57.68662 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c3fe35b-7eb5-3d91-b540-894979fa8502 | -10.16569 | -45.5537 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b212adb5-a260-3074-b7fd-ecc32f4d6384 | -10.09487 | -48.40622 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 88bf48a2-17b1-3362-845b-bae6de8fe6ff | -10.10915 | -48.43814 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a643dfb0-8f50-39fb-ba78-906f16ae36e4 | -9.94809 | -45.73275 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d95e145a-636a-3c53-bef6-0eff886b0de9 | -16.05258 | -52.53675 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0f728f4-1797-387d-a6a1-6862df158a12 | -7.56959 | -57.69528 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a060e273-8c5b-326e-bf63-3ba6ae5a2f62 | -10.37524 | -46.54483 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6213e619-5267-37a8-b5d6-f6be41a696a8 | -10.14645 | -47.68374 | 2026-09-21 04:21:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7875425-01d7-3521-a7f9-602eb10fb357 | -16.18754 | -51.12835 | 2026-09-21 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe5ea90c-8fd3-3301-b7db-33d575392cea | -10.754 | -46.3151 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52f3ba46-53b9-3c62-aeb3-86ad75d8fdb6 | -9.82058 | -48.31001 | 2026-09-21 04:21:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f226c9e5-ffa0-306c-9228-3b4a361f00f9 | -17.02086 | -47.13486 | 2026-09-21 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b11c168f-cf48-3f37-8136-046f37acda12 | -15.4729 | -48.40562 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cb9d1e0-e49e-34eb-8cf8-f3ae4a527d99 | -14.79481 | -48.52364 | 2026-09-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 477768a7-b995-3edc-af57-6b53b7601e43 | -12.81625 | -54.04865 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f155ba8-732f-3a28-935d-dc584d73f11f | -10.31434 | -50.55527 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd350912-4591-387c-9f0f-9cdab4e5109e | -10.85131 | -50.15933 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a725d24b-738c-36df-8077-42499ebfdf1f | -10.92258 | -53.96286 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5b7bbb6-6f3c-361f-809e-98fa18bacf24 | -11.8958 | -48.9917 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84e6f19b-6eb3-3dd0-aa2a-d87fbcb2e423 | -8.60296 | -54.62083 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffd9bdf6-5ff4-3fa1-ab56-0607a1af51d5 | -10.23895 | -45.34787 | 2026-09-21 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0daf0b5-b17f-3e22-b023-ca6d7b7168f6 | -10.74494 | -50.80263 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c76001a-c185-337a-834d-104bd7fa7d65 | -10.53613 | -54.50127 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f493ca44-8d27-3ef1-b003-e3a3d1d1cefd | -16.18342 | -51.12767 | 2026-09-21 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d70bf98-0c2f-36bc-b297-7eed77166d59 | -16.42952 | -42.63578 | 2026-09-21 04:21:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcc5b82d-f83f-3f7a-bca2-f9bda82ab5cb | -7.59534 | -57.67788 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2617e1cb-8513-3e18-83ef-996e8c6e2090 | -10.46422 | -50.27943 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| faa549c9-111c-3b91-a6af-b37a2a24caa6 | -11.43193 | -47.3159 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 656e3207-65c7-3ba9-bcea-9f06d17b716b | -11.32608 | -47.2978 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a32413f-5e53-3e40-96b8-3b99cbfb209c | -9.9707 | -46.55433 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 880e8091-75c0-3e3b-9833-f6725fa3fc79 | -9.93118 | -45.27566 | 2026-09-21 04:21:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a44dafb5-c4ad-3c9b-8180-6844be1280c5 | -14.08991 | -52.13541 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39225c7f-59c7-32f8-8032-051660d796d8 | -11.00184 | -48.23391 | 2026-09-21 04:21:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73fd51b7-aac1-3717-adca-1c80ae01007a | -17.01812 | -47.13051 | 2026-09-21 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25cdbb19-288c-36af-a7b0-c0d0cc38f2d3 | -12.27764 | -50.1586 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffe05f90-01a5-3590-a71b-f2b5cc1c57ba | -11.80462 | -49.8078 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d7799e9b-461e-3671-8766-fc707816f0ff | -14.0396 | -52.07398 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1f0349b-eb20-3486-b2e7-0541a6ba1f6b | -10.697 | -50.76969 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7531ea8d-1a79-336a-9f38-c0d302d946d7 | -11.12945 | -54.01207 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e75c7b9-f994-3a19-8bdd-d018d1182f65 | -11.04639 | -54.90695 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7135dd54-133f-3dc9-b489-23a74c442a75 | -12.80505 | -54.04984 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72fa40f5-a6dc-3e57-9cae-18bfba489e98 | -13.47187 | -46.92119 | 2026-09-21 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0a1530b-692f-3f0f-8ceb-087a75b32cb4 | -14.1052 | -52.12922 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebac9478-c9cb-3e6e-b3f3-adadd67181ec | -17.57254 | -44.97419 | 2026-09-21 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README49.md)

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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b93c5cf-4950-3e8a-a239-2084448eb55c | -8.33098 | -45.37908 | 2026-05-26 04:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09278e41-5bb3-338f-a2c4-ca207d0fcbd4 | -7.59699 | -46.46698 | 2026-05-26 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 652a26e7-a202-3be4-9436-34ab6610f1c8 | -8.55974 | -45.9807 | 2026-05-26 04:29:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e230bc32-13a1-34f6-b1b0-0cdfa93f084a | -9.97099 | -47.87751 | 2026-05-26 04:29:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48570629-adba-3da8-bcc5-26d87c0a4976 | -8.87399 | -51.84013 | 2026-05-26 04:29:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e1b8677d-f6c2-3b73-a58a-dca426a5ba0d | -12.7007 | -44.95924 | 2026-05-26 04:29:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1c60230-097d-3d28-b191-b5c11c985ac3 | -9.30105 | -45.49163 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7109509d-7939-3cf0-931e-d529a3eb223e | -12.2296 | -46.60656 | 2026-05-26 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c1f9ea5-f601-303d-915c-d656a89504c5 | -7.57403 | -50.17532 | 2026-05-26 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65fde6ba-01e7-3ec7-ae8e-3394a47e8e5c | -9.35377 | -45.47383 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c44a9946-8ab2-388e-83a4-89f53ec11520 | -9.2915 | -45.48645 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff919af4-3364-399f-8085-10a84e251fac | -8.98798 | -46.82117 | 2026-05-26 04:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f2efd88-0f30-310d-bf10-23b9ff5c3be7 | -12.23198 | -48.10282 | 2026-05-26 04:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 148afab3-e873-3645-98cf-2d204dfcb339 | -7.13261 | -44.06572 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 608bf748-45fe-3014-91c6-d236050124a7 | -9.67863 | -47.04956 | 2026-05-26 04:29:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71bc7aa4-8637-350c-8414-04903d14f5d9 | -8.55254 | -45.98318 | 2026-05-26 04:29:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 13fe7308-8ee9-361a-9c8b-7f7375a1b1e1 | -10.62903 | -48.33195 | 2026-05-26 04:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85d63719-662d-3428-93d3-ff73aa08d9d6 | -7.21823 | -45.35227 | 2026-05-26 04:29:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1db5011a-e9c1-38e1-b253-392d5b65fa53 | -7.1332 | -44.0619 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a34547d9-d31d-301d-bd3a-e4b7564aaabb | -11.17137 | -55.91806 | 2026-05-26 04:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9b4f417-e0ae-392d-9672-0076477811aa | -11.17193 | -55.9151 | 2026-05-26 04:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e798a814-e065-30cf-baac-48fbb88376a9 | -9.36837 | -45.46866 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec8c7944-89be-369c-aeca-a3b17e6b21cb | -9.3723 | -45.46554 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46db1453-8b05-380d-a90c-1a29ff123bb9 | -9.44971 | -50.84295 | 2026-05-26 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2ee9d6c-7d64-3daf-b1aa-08ee862ff51a | -11.35483 | -52.95378 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6db1834b-df9f-33a5-bbcb-1fd94d5612b6 | -9.2948 | -48.58444 | 2026-05-26 04:29:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76849a14-6557-34f6-bac3-875b73b9d79e | -9.35714 | -45.47436 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0d88b16-9c9f-352f-8652-cb4bac2bb300 | -9.48698 | -40.30551 | 2026-05-26 04:29:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 143af84b-7ce6-368a-a3b6-a97a544fdfb2 | -11.97021 | -46.7916 | 2026-05-26 04:29:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ef446cc-ae35-300d-a2e6-709bcfceb2ff | -11.46068 | -55.12141 | 2026-05-26 04:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89d3c0bd-2679-331e-a4d6-d3df16f0c0be | -9.3022 | -48.58189 | 2026-05-26 04:29:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a606aa2b-d391-3788-a5e3-dee1f57c862b | -8.71219 | -54.99866 | 2026-05-26 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a14b638-0050-3819-9ad2-4d5bfdf77d82 | -9.29202 | -48.58018 | 2026-05-26 04:29:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b941a0bd-96f1-3aaa-91ef-102eaaa528c5 | -10.01098 | -50.73482 | 2026-05-26 04:29:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cde9a84a-9f6b-3aac-9a27-744dc619e57d | -8.61275 | -45.02789 | 2026-05-26 04:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64a9823f-7c14-35a1-852a-b0945a35d856 | -7.00866 | -45.00193 | 2026-05-26 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e9e37f2-4819-363f-855a-e8bf73bff8c5 | -11.78849 | -46.47854 | 2026-05-26 04:29:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf5eedd9-9ad9-3e3c-ab5e-0e4f9eaadfb0 | -10.87756 | -53.73759 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09364e6e-0006-3ee4-963d-a075295c60a4 | -9.05262 | -46.30295 | 2026-05-26 04:29:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 056a8926-1270-315a-98e8-f46eee6532a5 | -8.33434 | -45.37963 | 2026-05-26 04:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7975dac9-258d-32c0-809a-c481d6fc6885 | -10.04019 | -48.68233 | 2026-05-26 04:29:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dc2b008-4b43-373a-affc-7ca156a9b01c | -11.97028 | -47.37748 | 2026-05-26 04:29:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51a264c3-6823-3538-a807-d7f9038eb94d | -10.6363 | -48.32948 | 2026-05-26 04:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df10f69e-aa2b-3986-b51c-f33e3a644e73 | -11.18322 | -55.91094 | 2026-05-26 04:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 65482b05-9dca-359b-9882-5e7809ad6d81 | -9.46625 | -46.11222 | 2026-05-26 04:29:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e4494bc-67e2-39dc-b638-63804b6511f9 | -7.14304 | -44.06731 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53227500-09de-3c90-9757-674be65c6b7a | -12.55544 | -48.35307 | 2026-05-26 04:29:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c846e2c-eca5-35a7-93cd-043a26990b31 | -9.90536 | -44.35117 | 2026-05-26 04:29:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8df21fa3-0c51-3851-9015-f6f26991f72f | -9.44895 | -50.84751 | 2026-05-26 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d8cc07c-d30f-3894-9a79-521c9ef03494 | -12.04806 | -47.33597 | 2026-05-26 04:29:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db1245c6-5b12-3b3c-ba75-d1d34dcdc5ae | -7.63995 | -45.30128 | 2026-05-26 04:29:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c55302cc-3509-39a8-9e15-bd5d28f2167d | -11.21359 | -53.82908 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47773171-1c03-3d64-a141-9e63968ee284 | -11.35349 | -52.96141 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cafb542b-4ba0-3cd5-a3b2-ca00485465b8 | -10.47707 | -48.90524 | 2026-05-26 04:29:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f66c625-8cfa-3951-b6e2-8900ce990b79 | -8.61332 | -45.02422 | 2026-05-26 04:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aceb4d7-adda-35d7-b92c-a293cdb75e8e | -7.5733 | -50.17973 | 2026-05-26 04:29:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44bec8c9-f75a-31a2-a9cd-2281be8e11a6 | -8.5592 | -45.98422 | 2026-05-26 04:29:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a825b7b0-37e1-31d1-8ebc-454ea0bfaf03 | -8.98467 | -46.82064 | 2026-05-26 04:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da1b5f4b-6089-3bf8-b9c2-d01f2ea56a26 | -12.45982 | -46.5212 | 2026-05-26 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e059e4c-74e7-38a2-a817-d60b5a9f5196 | -6.52443 | -55.06427 | 2026-05-26 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94d1b628-0786-3bf2-a71c-a25be5f07f0a | -9.30559 | -48.58245 | 2026-05-26 04:29:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88e4ab41-2f07-38d0-955b-37c1f9e20604 | -9.29541 | -48.58075 | 2026-05-26 04:29:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71de84d0-136b-3f04-97a4-6ec424e4af3a | -11.35764 | -52.96217 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 95d799d1-f5a8-3310-9fd0-fb000739d1ad | -10.59966 | -44.32372 | 2026-05-26 04:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 21001639-94e9-3912-9d94-e10a8202d953 | -6.52387 | -55.06749 | 2026-05-26 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6812aaac-1e57-39d8-863b-b234d26313b2 | -10.60383 | -44.32019 | 2026-05-26 04:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67fb12f4-76da-3333-9772-bcb0651d3ce5 | -9.36555 | -45.4645 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9287c549-1e68-399a-99f9-9ebb461eef20 | -7.1471 | -44.064 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d25c91fb-ece0-305a-9f4e-d17f2bbf7717 | -11.17702 | -55.91594 | 2026-05-26 04:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 250a9f62-1593-3420-9ca2-dd0d12d88d0f | -8.8781 | -46.93508 | 2026-05-26 04:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8665c78b-e11d-3a21-ad4a-23438b84f81e | -12.45927 | -46.5248 | 2026-05-26 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3666a315-ba57-3e90-bf3e-5f2dfb6a02b2 | -10.9142 | -54.11332 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3eefb8a-1683-3f65-941d-4adced2e4225 | -6.51868 | -55.06655 | 2026-05-26 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 686644b2-4853-3008-a47c-b3234f791af6 | -7.14362 | -44.06349 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 471cb7e7-8b66-3508-ac97-c28d11089e62 | -12.44358 | -47.88407 | 2026-05-26 04:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88266576-ff8a-381b-9192-9143e3c4835f | -9.30499 | -48.58614 | 2026-05-26 04:29:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edd13649-a312-3ef9-8b0e-2a98a8f61b52 | -9.53759 | -40.33557 | 2026-05-26 04:29:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9c2f2a7b-21fb-383b-8992-9bb509c0d13b | -11.27507 | -53.96867 | 2026-05-26 04:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf5c8baa-aaee-3f3c-b826-eb5c86ef8560 | -9.36107 | -45.47125 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e694c0c8-d876-363a-8679-bac18602cdf2 | -9.36893 | -45.46502 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8f239633-1458-310b-9435-bdadf443a5f5 | -8.52082 | -54.77238 | 2026-05-26 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55b888d1-2425-39de-98ff-5964ebf59aad | -8.972 | -47.98162 | 2026-05-26 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc0e3938-0129-3151-83aa-807eb75937f9 | -8.55587 | -45.9837 | 2026-05-26 04:29:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 73d594ea-c319-3f92-84b1-0345ea9800c5 | -8.87755 | -46.93856 | 2026-05-26 04:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4208cb0-89f9-3d1e-b2d1-24a46aaac1bb | -10.60028 | -44.31966 | 2026-05-26 04:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b6e0db85-0716-3744-af39-261228821976 | -11.18266 | -55.91392 | 2026-05-26 04:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5e3235ed-b787-3496-80b5-a498463cc8c7 | -10.60639 | -44.32318 | 2026-05-26 04:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6e13108-9e85-3ebc-bf1e-c30d4ac050f3 | -9.48759 | -40.30102 | 2026-05-26 04:29:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 4514d444-1159-392b-8e74-630330d0563d | -9.4452 | -50.84684 | 2026-05-26 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdb78d6a-f447-3be2-ace7-a611d5111150 | -11.96727 | -46.79095 | 2026-05-26 04:29:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6fe04e2-d686-3eeb-9d12-ae56ae9c06c6 | -11.16174 | -46.8186 | 2026-05-26 04:29:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 891a6ec1-644f-3159-8e39-f0afc4cdb23a | -11.35831 | -52.95835 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 3a5c5bb6-6fd2-356c-8cac-549af692e005 | -9.29487 | -45.48697 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4967133-58e8-36c9-bc06-3a8e78e1b54e | -11.3584 | -52.9514 | 2026-05-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| e9c9941b-4e5b-3d1e-8829-ca79988ffaf7 | -11.54564 | -56.92976 | 2026-05-26 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2356178d-3d7c-3202-b598-bf0d0de00373 | -13.65548 | -55.29469 | 2026-05-26 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a42da0e5-f6b8-37b9-9ce8-093059f5f84c | -13.65779 | -55.29465 | 2026-05-26 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 094d39f0-bd5c-3ceb-a8a0-7e48729a4855 | -12.68885 | -54.58152 | 2026-05-26 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09b82e37-6e46-30db-9373-a21d5ef03d1f | -18.77046 | -48.03635 | 2026-05-26 04:32:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 79b173ed-c673-32dc-832a-0210dbf18b7e | -13.71165 | -50.08358 | 2026-05-26 04:32:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README10.md)

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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74e20d6f-3296-3641-be73-887f90647afc | -11.86956 | -48.97477 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba103b66-9c16-3f8c-b3ea-22186c0b6084 | -10.4889 | -50.3391 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdc80651-16b2-35a3-90a7-4709cf84e9fd | -10.9981 | -48.23329 | 2026-09-21 04:21:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dc8e049-fc34-30d1-81c1-02f8dc1c2d4f | -10.37859 | -48.91024 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 24625c76-42dc-35de-9a3d-258a46f2fc44 | -11.01556 | -54.13027 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33bafa56-ce29-3ad8-85d5-51b6573eb0b6 | -13.92911 | -47.84594 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb631e85-0101-3a92-aaf3-7ed753245451 | -11.74875 | -54.5741 | 2026-09-21 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d136e36-3456-3fe0-b989-ed10b3b0864f | -11.94471 | -46.5 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a261db2-142b-336a-9a12-b65de35185f2 | -9.67145 | -48.9753 | 2026-09-21 04:21:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ba629b1-9be6-3228-8386-74643ce36bda | -10.47009 | -50.2813 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| db987d5f-4eaa-37e0-8004-86b07b4ded2f | -9.75746 | -46.06039 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36be0397-228e-3b2d-8bb3-883eca3bc2aa | -11.14517 | -42.79402 | 2026-09-21 04:21:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b251ef83-b1a5-3d9b-a5e5-a5a1d3650c71 | -10.47881 | -51.28363 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a21a6bb-ee1b-30d4-b9f0-66ddbe90e94b | -14.65562 | -54.45681 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6725495-2602-3005-80e0-80fbd322c69d | -16.01141 | -52.52559 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ec3cb6ef-f641-3fe1-b5c5-dbe0b1e2f255 | -12.11283 | -47.04527 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c30c5b84-384f-3350-9c7f-5a62ea3fb6a1 | -11.79684 | -46.84504 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 36d99e24-f23e-3e2b-bd52-d4c2b2de9825 | -10.47337 | -50.30226 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6ccfb24-3d50-375d-ba24-930c25044764 | -16.03472 | -52.52586 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d102d27e-7528-35c0-b537-150eabdf1dfa | -10.79684 | -50.84415 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e0fd5ee-2d86-380e-a5fd-e0e27df3eaa2 | -11.94998 | -46.48935 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b379b46-8b20-3a51-b5ad-ab1918faedad | -10.75809 | -50.60432 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bc44507-b987-3c1b-8852-0e9c6f105a9e | -10.20798 | -53.92071 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89ab682a-d084-3479-9825-bfb1c0299f3e | -14.17892 | -47.86955 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2beb364a-4857-3328-8557-805572854634 | -16.03918 | -52.50953 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0eaa36fa-638e-33b5-bf87-726c8711eca3 | -10.44709 | -51.24993 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ecb7442-ce50-3210-b0b5-b62cf9c3c5ba | -12.11217 | -47.04919 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73ff225a-901d-338b-be34-fd15b6533639 | -14.22817 | -44.6398 | 2026-09-21 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b7ad55f-f9ac-3f76-8c0f-0929d8255a60 | -17.27405 | -44.51348 | 2026-09-21 04:21:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ee7dfa7-62a6-330b-b655-7a0742a37992 | -10.49319 | -50.3399 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| eb302fe5-a8c1-32f1-b8f3-c220c654c7dc | -9.82837 | -48.43851 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 01848aed-0eac-3077-bae6-7950998300d5 | -10.36814 | -50.21854 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57404512-abe5-340e-a183-bc6e386342f4 | -11.0942 | -51.05604 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4d038c9-3a92-3434-b28f-b43fb2ca1e26 | -10.11337 | -45.55659 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2276a19a-cd37-3a8c-bf5b-6bc49a11e525 | -14.62118 | -42.91487 | 2026-09-21 04:21:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da2a2964-a921-3c69-8c61-73f1f5fdd20b | -11.33759 | -51.3599 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e7b02b6-dedb-3da1-bed2-507c1f9f416e | -11.07542 | -54.02308 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c53813ba-d986-3ed0-81c1-506754d8006b | -11.04318 | -54.92329 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4d5267c3-8219-3260-b689-3a6ecf322eaf | -8.16833 | -54.77183 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9de00fa0-25c7-350f-8f68-943eeb291de2 | -11.87912 | -49.01184 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9617ad2-51ae-3e09-951c-f667ef850734 | -10.26432 | -45.48868 | 2026-09-21 04:21:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae6155c3-4574-3fa0-bb9b-8fd9eaa786cb | -11.83852 | -46.8197 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7426a38-664e-334b-bc9e-26ff7e3d8773 | -13.47809 | -46.92612 | 2026-09-21 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b2f88ec-0ad4-34a5-8292-29a0f7ed9e2d | -10.37863 | -48.91362 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b6a33e38-a778-3dee-a0d1-e62a72b635e0 | -7.58104 | -57.67503 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0138819f-739b-3987-ad23-646245db5721 | -8.93717 | -50.91197 | 2026-09-21 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67fb8a74-154c-397c-9fbb-e028997bfaf1 | -13.89007 | -48.56575 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ed366ce-f617-350b-8f43-1f40dffbeb16 | -12.30054 | -50.66036 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 601329d2-8252-32ba-a9e9-2c25a3efd64e | -9.67543 | -48.97603 | 2026-09-21 04:21:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24e24634-01a0-342e-824c-00bc3bf9d5db | -15.45891 | -48.47486 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 664e72e3-2da5-3185-873c-cc30cb08c491 | -7.5896 | -57.66929 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a44998e9-ce06-33c8-b48d-865858ebb6fe | -10.42235 | -50.25136 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 09a33753-b97c-3e62-bdb3-2e743ee999fc | -11.14798 | -42.82079 | 2026-09-21 04:21:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5580601a-2abe-3c70-bbfc-16a644eecec1 | -15.61382 | -47.83939 | 2026-09-21 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0a8dab67-7f11-378f-ac20-145e43dc4366 | -10.70846 | -50.77774 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cbeba47-c3cd-3bbe-9cba-515da5173470 | -10.3768 | -48.92035 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b3224b22-970a-30a6-a7b3-fed24cd3d10a | -16.03898 | -52.97754 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 990e87e6-130b-3320-a273-e2cce88b8919 | -10.3918 | -50.22471 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e59d28fc-06c7-331b-9665-76f14b66c669 | -9.90647 | -45.09592 | 2026-09-21 04:21:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ea3dc81-98dc-342c-b38f-e6fd1d210801 | -10.5597 | -46.56194 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1dc90077-11da-3627-aed6-3852485b2481 | -12.81125 | -54.05185 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c243cf31-13c8-3f57-b053-0a98b69df52b | -15.46108 | -48.44031 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9a56dba-c5c6-391a-bf1c-bdf4844038ce | -10.68279 | -50.23027 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a782749d-ab25-3059-9782-1713fcdcea54 | -12.1135 | -47.04133 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bc66266-be4c-389c-9722-13e249a4ffd4 | -13.24983 | -51.80278 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6920ecdb-ea07-30ad-b7d5-9de65a82324a | -11.85651 | -46.88263 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99485c58-c9a3-309e-9a39-4ac3a32da31d | -10.4753 | -45.10508 | 2026-09-21 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4f3fc49-18e6-33e5-beb8-f943b0f7bbae | -10.41097 | -50.24084 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 6ceaefd5-6d3d-3d33-b4bb-3665062fbec3 | -10.71362 | -54.01377 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c15a3675-6545-311a-9bc6-5496ec492756 | -16.03755 | -46.08007 | 2026-09-21 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 16a17f52-347b-3800-a9e5-15832cb9583f | -10.91851 | -53.95472 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 440b2296-6083-3954-8003-d4a0abdb1c58 | -11.11791 | -54.01357 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ffe043c-94fc-3878-932e-e198d9ca205d | -11.05126 | -54.91254 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29bd35d4-00cb-3fd3-8643-67c415a589bf | -14.03341 | -52.08208 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 90505233-16ef-35e9-9040-d318070309b3 | -12.80534 | -54.05411 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbe19fc0-6b34-3d72-9a2f-737e5f6ec87e | -10.86674 | -50.93353 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b4ddc63-0554-3ce8-9c35-2b1982602cc2 | -10.92057 | -53.94395 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61a92233-0b59-3b93-81ed-7c562812fd5e | -9.74999 | -46.06298 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64f9675a-420e-3428-90d7-466ee7473d45 | -16.03646 | -52.5235 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad2b63f3-2309-3496-b616-f17d0c6a397d | -10.4708 | -50.27719 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f74e0832-6104-3656-9afb-5d9247d0a203 | -10.20865 | -53.91714 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f78bb19-a210-3c68-8560-bc5249f7b3ca | -10.55811 | -46.56085 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e089c28-2386-36b8-9677-c6cc7ed562f0 | -8.17346 | -54.7775 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad953af6-306a-3912-92a1-3ec08d98e996 | -7.57962 | -57.68219 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e36e70d0-e36f-3b34-ad98-eba0de751390 | -16.01864 | -52.53683 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f993ca52-6a13-3e51-9bc2-bb8795af3b2d | -10.79828 | -50.75851 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df8b78e5-2b74-338e-b0e3-3b79f4c3f7ea | -10.69765 | -50.76221 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6ee75e3-8332-36f8-aa22-06e83cc5b490 | -10.26095 | -45.48819 | 2026-09-21 04:21:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a31fa880-7c95-3df0-b890-2061e7dd6ced | -12.53431 | -50.08102 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 770324f6-1793-3cc9-a5d6-d81e3a04e3a2 | -10.80722 | -50.83702 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8509886c-62c2-32d3-be11-55a073999deb | -16.01416 | -52.53578 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8811ef1-6012-3a25-aad0-10be04974513 | -11.62768 | -47.77221 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dedaa2c-4497-3ed3-90c9-cea385219867 | -16.04008 | -52.52217 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 3aa491d3-8867-3cbf-bda7-a21b6b2ce06b | -11.04556 | -54.91117 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f81c30a-f3cf-3516-bc53-fd83ccd21725 | -10.87562 | -50.93523 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38cb3d3a-24cc-3dde-bbc6-405ff175b54a | -11.38413 | -44.0495 | 2026-09-21 04:21:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4697ac7d-eb58-349f-b39f-d2c9939f9c88 | -14.05626 | -52.11415 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b5e0400-fbf4-3528-909d-1bfaf0bc3b98 | -13.94107 | -47.83805 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9be47fc9-d995-3aac-af88-429070ef08a8 | -10.75895 | -50.80073 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a7448060-8b94-388e-ae0b-c3c87972bd79 | -13.94036 | -47.84216 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README52.md)

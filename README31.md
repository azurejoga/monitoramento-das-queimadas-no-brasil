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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0e4b87a-789b-317b-9565-4d46654ea33e | -15.65954 | -56.03619 | 2026-08-23 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2bf40295-2616-3f5f-afb2-9a223cd76b05 | -9.43921 | -51.59904 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc005acf-05cf-3180-819b-6bc3a169b475 | -12.75745 | -48.38686 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5617e36-32b4-30b5-8ac9-2476f8d36bfe | -14.33513 | -52.9252 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5539003-bc98-3c6c-a956-dbc27064e323 | -9.23275 | -60.38347 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b9cd2f6-c219-375f-97b6-373222c7f250 | -11.68283 | -54.58323 | 2026-08-23 04:46:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ab48b09b-567e-3977-9e2c-90356eb83dd7 | -12.40474 | -42.90469 | 2026-08-23 04:46:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50e4d3d8-4281-3bbe-9851-3298d28a5a35 | -8.62919 | -54.74366 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 967647f1-697a-3493-85f2-c7136245ac9f | -8.53791 | -54.83052 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8b81b91-6563-3fa0-ae30-97136b99e68c | -9.51834 | -51.67627 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 103bc128-9fa6-3a7b-bb21-afcec833c965 | -10.79694 | -50.97202 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d662288-8380-3c02-8d5f-092326c5e9d1 | -14.30489 | -53.22993 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 614c3c40-fe86-3b61-a2b0-e1efdc751e30 | -9.58874 | -60.50686 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d90e498-65aa-39ef-be53-3dfe5dc98f4b | -15.21023 | -52.79822 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdd5d665-71c9-3b12-a969-9aa405c970a4 | -9.79274 | -46.61241 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db5ebb76-df50-39aa-9a6a-427dacf7479f | -9.45707 | -56.90953 | 2026-08-23 04:46:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3140f57b-c07a-308a-b3b6-28203ebeb49d | -10.70653 | -47.73632 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae1cbed3-0f74-38a1-8c4a-6eb890ed5c4e | -9.01316 | -50.76957 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc0be3b0-e457-33dd-9dc8-a2ae09fa87e2 | -10.27107 | -50.38168 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6de0ab5c-b3a6-393c-a897-8143c59b2411 | -13.15585 | -51.42098 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| bc841e87-0a24-3baf-8023-45bb59043b7d | -9.0097 | -50.76897 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f492bcfb-088d-3e94-bbea-db7c5ffae5e5 | -16.01656 | -51.39985 | 2026-08-23 04:46:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0128dba5-75d5-3e8c-b407-554676992b47 | -11.85123 | -51.67604 | 2026-08-23 04:46:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1388726-06d9-37bb-a228-a61e9a2ab4f2 | -12.28279 | -43.15049 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b50fe4e9-4cdf-3332-8ac1-f6f0a5670c3f | -9.19242 | -59.45262 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43e72988-6592-3221-951f-815edc6bc654 | -8.90365 | -60.54694 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5807e343-affc-3fa4-8cd9-f98f8d567a74 | -12.48866 | -44.76932 | 2026-08-23 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2dd93f6e-0253-31fc-88e6-b15ff49d2033 | -8.96249 | -50.75287 | 2026-08-23 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0387762a-0f40-3f54-a8f2-72544439aaac | -10.46465 | -49.97045 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dead71dd-0776-327e-a1bd-6ec71063ee4b | -9.01725 | -50.76632 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5cf71aa-da2b-3f6a-8319-4f181fd783a4 | -9.06103 | -60.43224 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22806da9-f83f-312f-a1f9-c8f8ee5a7f93 | -12.72387 | -48.40389 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8993cad9-109a-38b5-92ec-707af6cb22f4 | -16.0525 | -50.44418 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c069f390-7914-316a-a1b5-cd4748ed7e63 | -8.89888 | -60.54733 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c8e59316-03ee-3fde-bd87-334caebd0ed2 | -11.15865 | -54.0092 | 2026-08-23 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9281b90c-15d4-39f9-a192-efa1633f55e7 | -16.34663 | -49.48048 | 2026-08-23 04:46:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 579a0536-c56a-31ef-b086-729eae7b7d44 | -10.70371 | -47.73219 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c27fbcb-80fa-3946-bcf0-7686912da105 | -15.5298 | -53.97969 | 2026-08-23 04:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 072e4b68-646d-3222-ab02-97a25a85a487 | -11.27613 | -50.73548 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a97ca042-ed87-39de-84aa-9bbe977f607c | -8.22394 | -55.02397 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dfd904d-7e45-3b07-afda-1df87f31070e | -9.85731 | -60.10125 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c43a9b3d-85e1-3168-b71c-c4e26763845d | -13.15521 | -51.42477 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 9d6b7775-eaaf-309e-a5a0-4ea2ebb8bb31 | -12.74627 | -48.41462 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2239883-71e9-3b6a-9ef0-6dd90e92caa9 | -14.9654 | -52.66968 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 710f8b9c-13ab-34ab-a34d-ffb90da3c8d6 | -9.1916 | -59.45696 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4f367996-479e-35ef-a23b-980987a19881 | -15.25276 | -52.8485 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cc885ed-0b49-3fc2-8e5d-30ada7a6f0d9 | -14.95829 | -52.64727 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0da9b93-731a-35a1-a75d-5145de9b85d6 | -9.01373 | -50.72237 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aadf758d-05f7-3d4a-ab25-892a9e7f5327 | -16.39384 | -51.33258 | 2026-08-23 04:46:00 | NPP-375D | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a05a008-5a3e-3332-be84-79507ffb8dbb | -13.16676 | -51.41898 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1e1494d-7b71-3704-a74d-52307effb7f0 | -10.83584 | -49.39465 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c6236c6-a1d7-385b-a730-506de6b608a0 | -16.05869 | -50.42679 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 492426c4-264c-304d-89e8-035dd43d10be | -13.68927 | -51.85344 | 2026-08-23 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc115b1c-bb0b-3415-b570-a4157bfb167d | -9.43095 | -51.66963 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91e8caba-4209-3db1-9185-1404bf209956 | -13.44164 | -57.08136 | 2026-08-23 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7abee050-53c2-3afd-8f77-f1f0eef7d378 | -9.21071 | -59.78934 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fee93394-dcb9-3e9c-acf4-405fdd358ae6 | -13.20724 | -51.42988 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f97e6a1e-70a6-35e7-94d1-6ab785000a50 | -8.9861 | -50.76083 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 28d2108e-4bc7-305d-81f2-6d4f6883b262 | -10.69383 | -47.71981 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b574bb73-e4e7-32b0-ad65-daa327755edd | -10.38122 | -50.41484 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12f5f1ec-62c2-351d-9ea1-135feb61ed4b | -10.30789 | -48.21486 | 2026-08-23 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c543cf16-067b-33ce-8c10-305a621fbb8c | -9.85493 | -60.1125 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d81ab36-04ae-3f36-b151-0ba98c1cb967 | -10.45794 | -49.96934 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9c596ee6-dd00-35dd-b585-c411ddea6a90 | -10.05102 | -46.42566 | 2026-08-23 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| df4bb336-958e-3a76-a706-3590f021000c | -12.7683 | -47.10102 | 2026-08-23 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7784b0e9-16b0-3e37-8356-a61329a2f092 | -10.45593 | -49.97318 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94c45162-9591-3d6b-ab63-17d503bdf035 | -15.53004 | -53.98228 | 2026-08-23 04:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b296ea7d-186a-3bf4-a000-3f6390272709 | -15.51359 | -49.83209 | 2026-08-23 04:46:00 | NPP-375D | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3a434c0e-8318-3aca-a099-b8b623337bfa | -16.40563 | -51.8381 | 2026-08-23 04:46:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 154e10c6-7f64-3c61-a5d7-c6c42f0f9dc5 | -9.58775 | -60.51193 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7adf09e-3f35-3445-a5f7-671408ed128b | -14.42922 | -52.9456 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8053e34b-1406-3e70-900a-ac4d8b862b88 | -13.15242 | -51.42039 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 053babbb-d9ef-36a7-a9e5-370adcc16201 | -11.2066 | -55.04876 | 2026-08-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 455b714d-ed44-3836-8bdd-80bdcb823516 | -12.84641 | -48.46756 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96827cc6-3cef-3f88-84ab-4f0c2f91531f | -14.57975 | -53.02352 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eed619fb-23aa-3a44-b952-01acf412446f | -11.43758 | -44.53852 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94c4029e-6aa6-34eb-83cc-4b9ce97f0451 | -12.82078 | -48.47786 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75468734-23ac-3f99-ab44-bc2bbfb917b0 | -10.93839 | -49.60309 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9ffeefe-571f-3c74-a402-de3735ec82fc | -10.68867 | -44.18137 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8ddcc97-6c69-36c4-bff4-b1f0588cafb2 | -11.05517 | -49.50606 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91743b4d-c10b-3269-a217-1a4e8bd67106 | -15.76117 | -55.55202 | 2026-08-23 04:46:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcd9a215-d46e-31b7-8425-9f05ec5c2b11 | -16.05479 | -50.42981 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bdae4e67-976d-3e1b-97b1-524f042ee134 | -8.92985 | -60.72816 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ee87d1e-c24d-3832-a06c-6a5cebf76b68 | -9.01378 | -50.76574 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89c21836-b743-3da6-9b46-4f01d5fa73c5 | -13.1801 | -51.44467 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04d20b4c-df1e-3f28-a199-d9f553b93f5f | -14.36105 | -51.83185 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f8ddc17-3131-3a58-96c6-aea8bec31d02 | -9.63663 | -48.31717 | 2026-08-23 04:46:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd666ab8-3216-35a0-91df-b8ff544a7d99 | -9.79331 | -46.60854 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8b5d1ca-a725-35ba-a8ef-e4e8d328daf0 | -14.49022 | -51.81441 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f4048a1-0cef-3ac0-be7c-df72f75a312a | -13.99541 | -53.71756 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fa49b54-ed6e-34e6-8daa-fa16be8f9bf4 | -10.49325 | -42.54737 | 2026-08-23 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 815c215e-2485-36a6-96c3-7167a65932df | -9.43494 | -51.60255 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 545499c4-dfde-3037-95ee-6ca500216f72 | -10.0632 | -60.50426 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c1d9556-7140-37f8-a828-1b733b048589 | -16.06144 | -50.43095 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84c183ab-a7c5-3059-ba8a-b0c9ca033356 | -12.21711 | -43.16843 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7c7b3d05-5cbf-3118-903d-b81074730a95 | -12.75072 | -48.40807 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03c353ac-e6b5-3afd-affa-a62c6c8affcc | -9.43071 | -51.6161 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0da03bee-d98f-3ae6-8a1f-63bc3fa17504 | -12.84478 | -48.47813 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7faf540d-8e15-3030-8ca7-7a1c765ea324 | -11.44293 | -44.52903 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 856315bb-d691-39cf-ae9a-69902f4f9ad8 | -9.11194 | -61.59064 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)

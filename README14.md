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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ed61f22-7f76-32e5-9c47-4067a7c6a6b0 | -1.8413 | -54.4841 | 2026-08-20 01:02:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00bbff6e-1094-3c41-83df-7230166b6ac6 | -7.5689 | -55.552101 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a753d0f1-fdcb-3691-b088-cd11a385859b | -3.5342 | -48.1805 | 2026-08-20 01:02:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62932c26-ffa0-30a4-8bf3-315ecf940781 | -6.0907 | -57.918301 | 2026-08-20 01:02:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2c083f8-3485-345d-9f27-d957b860a86e | -14.1815 | -53.070999 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8fdd7a3c-17dc-3285-84f0-a392141216e9 | -3.0992 | -61.214901 | 2026-08-20 01:02:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37c027f7-3078-3431-bcdb-8b4d13c19c30 | -16.072399 | -54.9632 | 2026-08-20 01:02:00 | METOP-C | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3896afce-466d-3dda-b028-406607cdbe34 | -9.5087 | -51.632198 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d501fa8-a72c-301d-9f71-f2675b517e89 | -9.1286 | -51.1119 | 2026-08-20 01:02:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f145357-8262-326e-bcd4-dae789e57410 | -6.3914 | -54.945599 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2338d54-4a58-3a35-9781-1632ab7a5838 | -16.0741 | -54.971199 | 2026-08-20 01:02:00 | METOP-C | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4babe86b-5ef6-313e-a161-fdc170f0e24e | -11.1804 | -54.0219 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7115667-e802-346b-a2c3-099e6fac2db3 | -4.2827 | -46.5117 | 2026-08-20 01:02:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5c8af04c-5339-38c9-be1b-9fdc7c0de7f3 | -9.4166 | -60.428799 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 537715ac-fc33-35ea-a85d-1cbbdfd6621b | -6.4365 | -52.758301 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d86d4a29-2735-3683-9aab-c00df681058a | -11.2164 | -53.999001 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3995847b-989c-3f5e-a332-cb38ad0a24d2 | -13.4481 | -43.837601 | 2026-08-20 01:02:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80a737ce-c656-309a-92d7-430b3b48f312 | -21.7118 | -47.130501 | 2026-08-20 01:02:00 | METOP-C | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4638916e-7d1f-36ba-99df-0ed220c5cdb7 | -6.6385 | -56.4077 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3085add6-2620-3f18-9e7a-8819edb8153e | -1.8347 | -54.500301 | 2026-08-20 01:02:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36c8a8bd-c0d6-3bce-a743-7c7ede5af9ba | -10.4474 | -54.658401 | 2026-08-20 01:02:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23cbca0b-4691-3950-a169-5473faf6e648 | -11.8142 | -44.820099 | 2026-08-20 01:02:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71627bd0-4b94-39a5-83fd-7a9c4096e2e7 | -8.5355 | -54.858101 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed92714e-0f06-36c1-b3dd-f4e4d133e03a | -9.3929 | -60.559299 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d2e0de6-d402-333e-8d33-3df40ca170de | -5.7949 | -55.7243 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a991164-586a-3e13-aa3e-0e1ae6e386dd | -6.8968 | -55.7234 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa1f604-7325-3840-8931-fba805720467 | -5.8015 | -55.708099 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8647be2e-08f6-32c8-b3c9-bdace228065d | -14.1556 | -53.047401 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 001fc10b-ecff-3227-b29a-fa566d16ae9e | -9.2035 | -59.754299 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62f47e46-4af4-3ee8-b7e5-daa817509482 | -14.3525 | -51.909801 | 2026-08-20 01:02:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd019db-ac42-3eea-a298-5bc7bd525de8 | -8.7188 | -49.6045 | 2026-08-20 01:02:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb2ff9b3-ce72-3b88-b132-d1a46a115305 | -15.0119 | -52.730202 | 2026-08-20 01:02:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d104598-c2b4-3c79-85fa-3e1bca5006b2 | -6.2496 | -55.411499 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a83061a7-ed04-3d16-9392-9a65c4ffd1e5 | -8.5174 | -54.869499 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef7e1963-aaa8-3029-ba10-5023bd35e4dd | -11.2153 | -55.058399 | 2026-08-20 01:02:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a22afc3-4aeb-3014-80f2-c497be371ae2 | -12.8048 | -48.422699 | 2026-08-20 01:02:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08def3e4-6f25-3cec-a272-ba8a7e7a97ea | -8.4865 | -54.869099 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8d838e-1c4e-3a04-a5e5-2cbb8eae3535 | -14.4463 | -45.596001 | 2026-08-20 01:02:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd8e63cf-b454-3810-b315-0727b5fb40f3 | -14.1768 | -53.0499 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 188d9b9e-abd8-33e0-91df-7858a6a4890a | -9.2183 | -59.776001 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86ffe692-5717-37e0-b3e8-c3e2c2062739 | -8.5257 | -54.860298 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 631892b0-d53f-3b91-bb89-4e100ae97728 | -18.035999 | -44.598202 | 2026-08-20 01:02:00 | METOP-C | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| acc26bcd-7776-3836-b644-efa5038dd2e9 | -9.1244 | -51.138302 | 2026-08-20 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e011786-7847-37a8-a452-137f0a3d8bda | -6.8921 | -56.437 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76035424-5620-3ae5-b7cf-2dad42de0389 | -3.0939 | -61.191002 | 2026-08-20 01:02:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf4899b8-9584-361d-8fcc-9ee9e0683d6f | -10.3318 | -57.558498 | 2026-08-20 01:02:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9db538a2-9b6e-33b5-a1c3-f46d5cb604dd | -14.7355 | -47.144299 | 2026-08-20 01:02:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 19d3af5b-2e22-3cc5-86a0-cbaaa892dcc8 | -8.5449 | -55.313 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5e8972-a725-3b24-994a-ea7081ddd720 | -9.1263 | -51.146301 | 2026-08-20 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 531d32ec-7c4c-3833-b921-b03cc1a1d528 | -8.5395 | -54.784199 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab0d5895-92a6-39b7-812e-fe5e3944fa00 | -6.4348 | -52.750999 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0a3cd0-01cc-374b-acf8-b84b654caa89 | -18.030199 | -44.615398 | 2026-08-20 01:02:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 43aed8cd-71b7-3858-8949-a6256835d593 | -10.3201 | -57.551498 | 2026-08-20 01:02:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b698397d-a069-3aac-88b3-db53da383fbe | -14.0234 | -53.657001 | 2026-08-20 01:02:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 486adb16-3d0f-35df-bac6-7d2c7362ffaf | -10.4588 | -54.6633 | 2026-08-20 01:02:00 | METOP-C | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10bd8a26-894d-3cd0-8cde-6388347e9d80 | -6.8773 | -56.416901 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8103d540-c301-3865-81d5-36ba78a332f0 | -2.57 | -47.233501 | 2026-08-20 01:02:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62cdcbca-4770-3dfa-ad94-585ed5ce6b99 | -13.5672 | -51.680099 | 2026-08-20 01:02:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a3bc695-0169-3066-ab12-ae9ca001063c | -6.8904 | -56.4296 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4042f81-0942-37e4-871c-01093bba760f | -10.324 | -57.569599 | 2026-08-20 01:02:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1f5f421-a0a1-3809-adba-94b52d9b6873 | -8.562 | -54.655399 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe09b28f-c540-3d4b-842f-f95afaea9249 | -7.3574 | -45.817402 | 2026-08-20 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c029779-6ae6-3021-821d-ea63b959757d | -8.5635 | -54.6623 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9bef822-1efd-3bf7-81c4-a0f4841aa219 | -8.5674 | -54.770699 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84d80e6a-535e-3d3c-bf45-4e533ddaa5de | -5.4296 | -49.223999 | 2026-08-20 01:02:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76e635f1-adb3-3574-b47b-6c7efee0b259 | -9.9862 | -53.934799 | 2026-08-20 01:02:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f3a8453-9c10-36ea-81d4-920e9b86d18b | -11.9976 | -53.440498 | 2026-08-20 01:02:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a11a4e0-8f73-3fb1-af82-c699557f6778 | -14.167 | -53.0522 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 818df513-281c-33d3-bfdc-3fdbaf677b21 | -17.776199 | -49.122898 | 2026-08-20 01:02:00 | METOP-C | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 29ddcffe-91a2-3f3b-874e-c2e2646ee694 | -13.5737 | -51.6633 | 2026-08-20 01:02:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 147a1a05-c716-395e-b90d-3f4b4d00becf | -6.6189 | -56.319801 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25a3d932-e794-3662-a4f6-275e4be5ebd7 | -9.2133 | -59.752201 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65cb6c1a-cda5-312f-932f-63724b5efdf3 | -8.5889 | -54.729401 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53e8ac7a-b719-3185-8c8f-125f8e801170 | -6.6195 | -53.372299 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5486323-0238-3b15-a036-e59dd237c114 | -11.9961 | -53.433498 | 2026-08-20 01:02:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36aa7151-5dab-3cc0-bdf3-3ba774675119 | -8.6632 | -54.647202 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f491000-4e76-37ae-89fa-3c9b9ba2df65 | -14.1532 | -52.944401 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88b10be6-57c5-3db5-a7df-eaea281a1fca | -23.0816 | -49.164501 | 2026-08-20 01:02:00 | METOP-C | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 350b81c3-fdea-3d22-9810-14e92f7063d7 | -9.1032 | -60.343601 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 331ada58-24a5-3c60-8f1b-3ee2e3f5fc8f | -8.8921 | -60.5513 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54085615-9a7b-3c54-84bc-dd042b109278 | -14.0218 | -53.649899 | 2026-08-20 01:02:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 767468ae-f931-37ef-935a-7904567e2678 | -7.4743 | -55.314602 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6825a48c-44fe-3dec-afcf-ba5289f415dd | -8.4947 | -54.860001 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bba36aae-993b-3b7b-ae99-5dbe003605ee | -14.2041 | -52.895699 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0da202a-17ef-35d1-a4b7-6d5d430eb3c4 | -15.5426 | -50.2658 | 2026-08-20 01:02:00 | METOP-C | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 717bb1d4-9604-3401-981c-81388f75a562 | -14.2139 | -52.893398 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ced0079-b78d-3e4d-b5ab-4c5d328ce93f | -13.4102 | -54.376801 | 2026-08-20 01:02:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49036da5-0920-37cd-990d-f772b93325ef | -5.7917 | -55.7103 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f857a2a-9439-3c2a-aabf-b26a75913454 | -12.8268 | -48.427898 | 2026-08-20 01:02:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cedf4250-aff4-3599-8d12-986af06ff420 | -23.5958 | -52.853401 | 2026-08-20 01:02:00 | METOP-C | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03d62b36-528b-3a89-9fe8-432ae324f833 | -6.717 | -59.084099 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dac00204-451c-372f-87b2-258c173f90c6 | -15.365 | -52.7892 | 2026-08-20 01:02:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ae88493-21bd-3e29-8409-cdc7f9c898f3 | -6.448 | -52.763401 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d540538-4b5e-354d-8307-680db076c85e | -8.6589 | -54.582699 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4aa627d-ccfe-393d-a66c-e1bb2728f0bb | -8.5885 | -54.7733 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa3eb613-5fad-3350-a183-344747bcac18 | -13.4004 | -54.379002 | 2026-08-20 01:02:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a54f7b9-de76-371d-831a-b7cbc598f510 | -10.7996 | -50.3148 | 2026-08-20 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c52797ab-dd44-3581-b1ef-4494682b05de | -7.6117 | -45.192402 | 2026-08-20 01:02:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4495fd-f3c3-3336-9d58-58fad19d2e18 | -11.2169 | -55.065701 | 2026-08-20 01:02:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e84781c7-c7a0-383e-97a5-50f4f8098ff8 | -14.4366 | -45.598598 | 2026-08-20 01:02:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README15.md)

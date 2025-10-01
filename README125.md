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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc2b0aa2-3954-3485-bd9e-3db65cc59b35 | -10.28779 | -50.46953 | 2025-10-01 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ed1d202-812c-38ea-a0a0-b55967ebe574 | -11.85096 | -45.00037 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c65ce635-fe41-3d5e-b4d2-d5ff333b2658 | -12.76267 | -46.88345 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f537adb9-af7a-38e6-bb0b-92cb85dc3036 | -13.22848 | -47.32794 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3465a02a-8ca1-3f5f-99bd-d73319f39f90 | -10.82623 | -45.38309 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90b81796-d94f-3a41-a41d-0e3a87e46810 | -10.81478 | -45.36394 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d21a8072-3096-33d9-b894-408aab3c5f49 | -12.9532 | -46.41838 | 2025-10-01 05:10:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22b23161-c862-37db-aa90-aa7fdb2df632 | -11.38702 | -44.89874 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2cb35c5-3c7c-37ee-89e5-b730711ce136 | -11.81757 | -44.98302 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba18b598-fe96-3d2e-a9b4-013312cfef4a | -10.06826 | -50.26012 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 67624d17-c06f-3c24-b351-ac3ee3208da6 | -8.53471 | -44.70647 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 531128ee-13d3-3a2a-a0f7-4282e9742faa | -12.83191 | -47.03872 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8ac353a-0770-390b-9128-3dda23cf61e0 | -6.51398 | -54.89096 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8de2dad0-9c53-3ea2-b595-df3ce6462dd3 | -10.77082 | -45.36798 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d17e630-c4d0-3a8e-bb9a-de5817334d60 | -9.4278 | -54.71908 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e037370-e502-3a88-af06-3b395f0cae3e | -10.63349 | -48.53121 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8b94f74c-4270-305b-9921-79ddcc4e6294 | -11.48306 | -54.60604 | 2025-10-01 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b89931e-785b-3f22-9f93-769d3dccfbb0 | -11.56987 | -50.17746 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7e99a53-474e-3ffb-9262-26f85910fd84 | -13.30287 | -47.21121 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 078b481a-3898-3529-89f9-333e1dff72b7 | -12.17269 | -51.41479 | 2025-10-01 05:10:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3959f9bc-eba9-3e76-8083-cbed75084bfb | -7.80482 | -50.04221 | 2025-10-01 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6feb0247-7fd3-346c-a6f3-f4b9b09af54a | -13.35765 | -48.11119 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e30657b6-02b5-3d9c-aca7-95cf6336e365 | -7.41149 | -45.41901 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4850c465-b713-3707-9cb3-2afdc2b1645a | -10.07039 | -50.26805 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9866a53e-1827-369b-af84-fca9e9ad4cd0 | -8.88613 | -46.60987 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feaaf23e-10f4-3f8a-9422-c44cbd414baf | -7.88231 | -47.28253 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4947fa0d-8ae2-3242-8700-ef3d83dde7b1 | -13.12992 | -47.42823 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 131383a6-c3fa-30cd-ad66-f021969f902c | -11.75719 | -46.878 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30489781-f32f-31f1-a6ab-1390db5581b1 | -11.84277 | -48.05812 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92d74253-850f-3121-8d30-770ccec79ec3 | -11.2065 | -47.20328 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f60c4960-a041-327f-8d56-f83af788bc20 | -6.79334 | -44.74263 | 2025-10-01 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 16a72775-278f-366d-84ba-ac7791e81169 | -11.20046 | -47.20238 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da678690-47f7-3f63-b26f-85b60bb6e039 | -13.33324 | -47.8724 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5aee0ad8-1c3d-3208-8207-3d7dfc0dbe8f | -11.27678 | -47.81578 | 2025-10-01 05:10:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f4b2ccc-e3ef-3ff9-95c4-e7ef43851cc4 | -11.79689 | -47.59959 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 87e00d28-7de3-3ad0-a555-7b3562e82eb0 | -11.86522 | -48.02285 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bc46d8f-c2fe-3766-9747-0326e692739c | -7.8236 | -47.06392 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa82b817-adf5-3f1a-a9af-f012cfcfeffa | -12.2433 | -47.81863 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08b51d02-7350-365e-af92-0c143e6d0acb | -12.43016 | -50.17565 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af03e859-7f90-35f2-9d62-ac0071c4659e | -8.91116 | -54.93076 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9faed2e6-e6bd-3b50-9c8d-de144aaa4ac7 | -13.34093 | -47.80678 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3f5ee33-f2b0-33ee-b81c-7a86fd1bc0ba | -13.32077 | -47.3407 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7dd562dc-ea19-38da-b514-cba45802cab4 | -8.554 | -44.72766 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c55987ad-e40d-3845-9f97-f29313a90d1e | -11.75952 | -46.85862 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b2adbee-ea70-30f4-924c-4aed607f52b6 | -13.35814 | -48.10696 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a25dc1a5-dcb9-3bc7-9a92-961f7e8be119 | -11.46322 | -45.08415 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 647da9d3-b65b-3f5b-ae67-d455f78e085d | -12.24392 | -47.81343 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4048c5ae-0fd9-35f5-81b3-f0803bbab02c | -13.13711 | -47.41959 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a354d124-0c99-3b5e-8011-f11ab8f30c9b | -9.58599 | -54.58632 | 2025-10-01 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7fae30d-2560-3329-b605-d4dc54d80a59 | -12.97325 | -48.42974 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc1746ad-77cd-319c-95a2-b6bd5b07228e | -11.84338 | -45.00502 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 063ae38f-63d2-3fff-abf8-3c716fc439d8 | -7.02952 | -46.98238 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6849405f-1a4f-303f-9845-b822a35044b9 | -9.51467 | -54.73952 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6da2610-049a-3018-b283-917ce041b9bf | -10.24163 | -52.69847 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a348aa2-aac8-3a35-8293-5f96f3f8ebd3 | -7.14614 | -47.26376 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab9a8386-8d2b-3741-b815-d00153b41816 | -12.98613 | -48.41893 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 029b4d88-213e-3600-95fd-5ea7f138fe95 | -11.85445 | -45.02181 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 29e45c07-eb0d-372b-ad52-b71d3ddb439a | -10.10612 | -50.22292 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e58be744-5da0-3340-920f-cfc1724a1cae | -8.61345 | -50.40451 | 2025-10-01 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8054529c-b424-3c99-ba2e-1afe1887eb2b | -12.16134 | -47.76896 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 468e78cf-227e-3282-88d4-41e1b6c79d22 | -7.14047 | -47.26262 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d56fd35-449e-3034-a1d1-ef42f3af73dc | -11.20038 | -47.76483 | 2025-10-01 05:10:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e856a9e-27db-33bc-8258-d8c0048e7ae5 | -12.87736 | -46.91743 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b8cf370-22f3-372d-a9e3-23ce863d24f5 | -12.46546 | -50.22283 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1695b94b-645a-36a8-ba1b-ec690e1113d1 | -12.24505 | -47.80392 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4687f31-d8c7-347b-a822-c8bb9df30340 | -10.48429 | -49.37127 | 2025-10-01 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ddf78eb-0109-3c13-882c-b35f20bc567e | -12.83505 | -47.01062 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2df5611-4e4e-39a6-a4ee-94396ea8f500 | -11.96339 | -46.59842 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 646477f5-9d33-376d-bcdb-2b68707108ae | -13.32965 | -47.85139 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aba1b9fb-e626-37cd-b782-75b137784085 | -11.31316 | -53.9596 | 2025-10-01 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8b40b6f-c420-3fd2-a348-b57ee9e260ea | -10.92864 | -54.32896 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55b30881-0343-382c-9f9b-391bf5d20d11 | -11.1832 | -47.20269 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bb766f1-a837-3ab5-8e39-d034edc55422 | -9.42481 | -54.71432 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 333da404-23d5-3b75-836a-ed0e16f458bf | -12.23843 | -47.80918 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b15750e1-4214-3b95-998e-f4822ff6dcc1 | -10.06897 | -50.27892 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e261436c-0a07-366d-b4a7-8be11685c18f | -10.18858 | -52.56306 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84928caa-ba64-3eaf-a793-60adbcb600c7 | -12.27797 | -47.82929 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3c91109-70f0-33c0-8402-94ae38cfca4f | -13.29904 | -47.58542 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b9c47e8-244e-3c09-b68d-c5ee2fd9b70a | -10.10051 | -50.22773 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a9d03f2-f19e-3a71-a5c2-62d5637fb6ee | -13.33116 | -47.83848 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e396dabf-af05-38e9-b11a-e7f4723404d0 | -10.01882 | -50.25892 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83ac5563-f860-34be-b44f-c92ce11019ab | -11.77997 | -47.58917 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cd1d4f2-1c89-3903-b78d-18656a8b4119 | -7.82235 | -47.06651 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c308b46-20ef-3185-8347-21c36af8609a | -11.15145 | -54.1171 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eaeaccd6-7f7c-3d53-90f4-77ce47d6f610 | -9.58171 | -54.59005 | 2025-10-01 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de0e3c3c-1626-3c7f-950f-8cb5167e4d00 | -5.6259 | -51.93819 | 2025-10-01 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63b806ba-dd70-3ab6-af64-4366e2605f5c | -13.3315 | -47.86291 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0bc8ad11-b3ff-3d43-8da4-f5915a7c039a | -12.43187 | -50.17144 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca73e6bf-8de1-3ef2-83ab-8f30d417cacb | -9.76477 | -57.01021 | 2025-10-01 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6922013c-cb65-3709-8d40-71c0764c8ed6 | -7.1456 | -47.26789 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9fccd0a-2152-35b2-8d8e-1e63f5f7b8e9 | -10.63398 | -48.52735 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b01566e8-80d3-3a86-bc7e-88abe3d2ce70 | -12.87421 | -46.94514 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8dba77bc-00bd-3426-ad6c-5444554fb125 | -12.86798 | -46.77271 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e946745c-718f-3e57-a787-548fdd747643 | -12.84048 | -46.87387 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbf9fdbe-790b-309a-a9c9-3a9f69c39ebc | -11.45427 | -44.97408 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0476548-f618-3271-9bbf-c3f85a03e7ea | -9.9421 | -55.16118 | 2025-10-01 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a4fa6a8-a496-307c-8fbd-9aed8813a656 | -12.82216 | -47.01246 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0271d08-ab41-3565-a095-032e44f7cdf5 | -10.66163 | -48.53062 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7e7ed58-576f-3017-8ab9-d5ecb720eb2b | -11.83168 | -44.98325 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15005aa4-1ac7-30ec-bf59-4fb080d9bea3 | -12.83874 | -47.03426 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README126.md)

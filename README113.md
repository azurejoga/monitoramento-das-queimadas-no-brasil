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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efabcb3d-14aa-3d0a-9232-cdfe7122e147 | -12.57712 | -48.4813 | 2026-08-28 17:26:00 | NPP-375 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 10315be4-9f1e-315b-863c-65fe773b163b | -10.63449 | -45.22461 | 2026-08-28 17:26:00 | NPP-375 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c2d5d0a4-02bb-39cf-94e1-de50fb2c36c9 | -11.96176 | -45.4993 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c5703ad0-5c6b-315e-8666-62b1a1b193df | -10.83319 | -50.52814 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9b07d8f6-4f4e-3d1b-ab64-78f39fc16c06 | -11.77491 | -54.51458 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eaa0a399-d466-31d4-915b-ff16a66e64d0 | -17.59664 | -51.64355 | 2026-08-28 17:26:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c07c7fa7-958d-3fab-b7ca-b2f8195636f4 | -9.49642 | -45.661 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 22f014b8-a179-380b-bdf3-099da1627d5e | -13.88725 | -53.24376 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 2bc03b74-001f-3c0d-b55a-345c3f6fd305 | -14.88313 | -52.63443 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 0f8e865b-4623-3585-aac9-274a22a3f318 | -14.82962 | -45.53103 | 2026-08-28 17:26:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 32aed382-9bc2-37dd-9dc4-6e18e0648f58 | -14.89941 | -56.32411 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 01d94f33-4a35-3c61-b03b-08537248b67f | -9.89027 | -46.35464 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fae65575-de98-3574-9e51-4056d10bbc59 | -15.35185 | -52.82857 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e93d7cbe-3309-3315-b164-6163194c05f9 | -13.31082 | -46.91933 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f7caa2e-99fe-3de5-b7c9-9b68a400c89e | -12.25971 | -59.35115 | 2026-08-28 17:26:00 | NPP-375 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 05e54f8d-3052-3ae4-8e0f-ae627e1f7051 | -15.39894 | -52.85631 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5732b891-8e26-3d2e-bd46-7816425c54ea | -12.11631 | -57.21343 | 2026-08-28 17:26:00 | NPP-375 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81d6dae2-dce3-372a-83d7-f8f967253a88 | -10.30668 | -49.97009 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1c30574b-edc8-38f4-a879-8500c4492f52 | -13.65666 | -47.75217 | 2026-08-28 17:26:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 53ec7dba-0458-3a43-8cfa-d6404cde906e | -15.3553 | -52.82795 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fa149f81-f5db-3f7d-a2d8-08b7dbf37dc4 | -11.21585 | -55.06821 | 2026-08-28 17:26:00 | NPP-375 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| b01712cc-f7cb-33f1-be55-520106448eca | -9.79621 | -46.33676 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a2429bdc-3038-3dc8-af0a-41a6edc0ad8d | -14.60041 | -40.59191 | 2026-08-28 17:26:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 3fe9a45d-ceed-35d3-a29a-fc0fee4293a0 | -14.45503 | -53.37056 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 78a0e387-e821-31f7-b2b1-9cc33425cb17 | -11.67445 | -46.73078 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4a18d1a-3abd-330b-9440-e0ec457dbb45 | -14.64025 | -57.00258 | 2026-08-28 17:26:00 | NPP-375 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 8085091e-6eb6-3b31-a6e1-e35b3b31d638 | -15.1285 | -52.83103 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1bd8015a-d11d-39ec-aeb1-febf36917b12 | -11.26609 | -50.70489 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2f8f63f2-4df7-3f64-9f67-9b6527981565 | -9.49601 | -45.62648 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ea7ed06-07e7-31d7-a250-cf43c3db2959 | -11.14848 | -45.56362 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5d475554-2ae0-312b-8dbd-e9470da2cf4f | -9.80238 | -46.33906 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e5d495aa-31a9-3b99-bfaf-522875d31a34 | -14.87923 | -52.61086 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| b424230a-c9b3-3a47-b3fe-8645bf46eb22 | -10.92605 | -46.62068 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04306962-9933-35c9-8c74-ab4448d08437 | -14.60391 | -47.97219 | 2026-08-28 17:26:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c05f1570-f5b4-33ba-9cf7-888bfd6bcb31 | -16.18013 | -45.63363 | 2026-08-28 17:26:00 | NPP-375 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a630ebd8-55af-3098-8932-4e8bfa023ce7 | -14.89657 | -56.32835 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 252493f9-cd94-3e21-b2a2-694d02fd597c | -9.48943 | -45.6236 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5fcefbbd-4439-32aa-9445-3f0730d5a6c6 | -14.46291 | -58.51959 | 2026-08-28 17:26:00 | NPP-375 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c483a987-fd83-3fe5-8c78-ce5dfb85ad13 | -11.65692 | -55.69278 | 2026-08-28 17:26:00 | NPP-375 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 409e2138-8436-3235-8d3c-6d0266a115d0 | -11.70868 | -51.54167 | 2026-08-28 17:26:00 | NPP-375 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f42052b2-378b-358b-a758-8b971eabe8a2 | -13.87525 | -54.11277 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 130b9c0b-c045-34e7-acd3-e4625de233e6 | -10.53776 | -50.77261 | 2026-08-28 17:26:00 | NPP-375 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 57cb5924-7fcd-36d3-8781-f7363e5520b8 | -10.57616 | -46.29656 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| acdedb5a-f56e-3913-a0a9-0865fa69db7e | -13.64529 | -47.7436 | 2026-08-28 17:26:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| da9a9ab0-ceaa-3b34-980a-4fc5d30a1eb1 | -12.7815 | -46.45421 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 98b50416-876a-3bdf-9163-1a5a009c126c | -9.68655 | -46.56567 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b7c4b983-0a09-30c2-9129-24a0a93799a3 | -14.87988 | -52.61478 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c7d5580b-9cbc-3658-8d41-62b246be7f76 | -17.25866 | -53.30025 | 2026-08-28 17:26:00 | NPP-375 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4a4d20b-d1f7-38fb-8e07-71284e892778 | -14.33578 | -51.70971 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f5ef46a9-258b-3cc6-87ad-aa0615eeef33 | -13.81923 | -53.93383 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1772fbd7-645b-3380-9712-825d4cd05ba0 | -12.08364 | -47.17838 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5683140a-66d8-3550-98d9-77c31538c1c2 | -13.5884 | -45.77514 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| ffab032a-307b-3380-96a4-cd785fcbb498 | -10.32897 | -49.96321 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 792442e6-9a30-32b9-b576-9386aa4e1092 | -14.18449 | -52.82267 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3f0ccf8c-8275-31dd-99c6-190a68d83ef5 | -12.28376 | -54.09166 | 2026-08-28 17:26:00 | NPP-375 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 05dd0031-4bb4-3d6e-9fe6-4ed218b16294 | -14.15852 | -52.83918 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7fa4969c-2404-3f68-9652-a0b697e0fc1e | -11.88817 | -57.10869 | 2026-08-28 17:26:00 | NPP-375 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6ed191c3-5c42-37e4-81c1-6b07b476ae04 | -10.63697 | -45.2249 | 2026-08-28 17:26:00 | NPP-375 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 22f5a407-a55e-3df9-989f-288b7ebf69f5 | -10.31171 | -49.97349 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 000a2a2a-8401-3fdd-a1db-0ff7983a195b | -14.03181 | -42.15977 | 2026-08-28 17:26:00 | NPP-375 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 49.4 |
| df638efa-777c-3d13-8500-64742912f267 | -14.21742 | -45.3077 | 2026-08-28 17:26:00 | NPP-375 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f101ce77-2f1b-3043-82cc-f952b0339f57 | -9.79638 | -43.55795 | 2026-08-28 17:26:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4ab17535-60ec-3bc8-bea0-420ba387eb97 | -11.81454 | -47.21851 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25a08c0d-c87f-3190-ba15-01c1792c6d60 | -11.60327 | -50.19944 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0cf9aba3-2ffd-35f5-8a58-58734467f12d | -14.6157 | -53.14824 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 155c4ac4-942a-3f6e-a75a-c43dbe5f4858 | -14.4277 | -52.58857 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 046de63d-e775-3ec4-a103-767cab39d058 | -13.55228 | -52.6194 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 893f6112-895b-37d1-ae23-fdb65f8212c2 | -15.64067 | -45.91033 | 2026-08-28 17:26:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38ecd6ff-9acc-3647-930c-82ac7035e32a | -11.83695 | -47.22653 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d320ead-bfdb-3e68-8d36-3f3906cef9f5 | -13.32849 | -46.93718 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ae95836-7548-3fbb-b768-2b048e1eef6e | -14.92344 | -56.31997 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c6052599-a9ad-34e3-9ead-c3521ae035c6 | -11.23436 | -53.98935 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 6790d8c2-25c2-3587-a2b5-ecb5646834d6 | -12.3531 | -44.39497 | 2026-08-28 17:26:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7cf7ddb5-f964-35bc-9d61-910df716c24d | -11.37733 | -45.14317 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1a60310d-99df-39f8-91a5-d74e3cfc0fb3 | -17.5454 | -51.1166 | 2026-08-28 17:26:00 | NPP-375 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 77be9d2a-d95d-3fea-baa2-2cd68e232e03 | -10.83662 | -50.51257 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 17ca1e75-4309-3a58-858c-ca4a93389db3 | -14.41296 | -52.96038 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 91b162ef-e855-395a-9cc3-5a515f010e6b | -11.27975 | -54.009 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e7d2c06d-e8c8-3d13-bdd6-480a5af9e7c8 | -10.23946 | -48.45087 | 2026-08-28 17:26:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 58b2bc73-0263-30e8-9305-86667e8c815e | -13.42827 | -51.86415 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 81a620b9-eed3-36be-8c76-46e1871d758d | -16.78966 | -50.02345 | 2026-08-28 17:26:00 | NPP-375 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| d824ab14-7c7c-3661-89bf-3b2124589827 | -10.85039 | -50.22159 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 19e8ddad-937b-37f8-9aea-8cb00bb1d65a | -9.66123 | -45.71711 | 2026-08-28 17:26:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6235817-e4bf-34ad-a0d2-7a5301c7b560 | -11.19185 | -55.09031 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 21349568-b33b-3e2d-9970-548024482656 | -13.32106 | -48.20096 | 2026-08-28 17:26:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8c220199-eb08-3ee7-b6ca-a7edeba5cd42 | -12.05017 | -47.18418 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e78f72ec-72f1-328e-bff8-495c0ae5a792 | -11.8454 | -47.21561 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd422667-03ff-31c8-9a20-76e277224f97 | -14.64137 | -57.01027 | 2026-08-28 17:26:00 | NPP-375 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| fdbfb9fe-ce16-3fc4-ba6c-3e2c0b159027 | -16.12728 | -55.86934 | 2026-08-28 17:26:00 | NPP-375 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 71043ceb-b9fa-3c59-b8c0-77bec6608783 | -14.43768 | -53.38934 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 75f3687d-7332-3a57-8473-be442fbc2eb9 | -15.35311 | -52.83628 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b63e103-e85d-3a9f-b466-929a6f2591bf | -13.55516 | -52.61474 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c675ef06-04ea-32e6-b280-ea616ad1a3c8 | -14.50276 | -53.53612 | 2026-08-28 17:26:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d7796654-9896-385d-871a-1f6a9ada568f | -9.69635 | -46.55654 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 267c35f9-8305-33ac-bf88-c505109db3ac | -9.79524 | -43.55222 | 2026-08-28 17:26:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e01fb855-f8ba-3dc5-8d84-521f59befe47 | -11.24927 | -45.05938 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4d65eb00-4f08-315d-a35a-a78138ebc7e9 | -11.58112 | -45.51453 | 2026-08-28 17:26:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 692e2d8f-2b6e-3670-a896-eaa73a0d3a0f | -14.4956 | -40.33279 | 2026-08-28 17:26:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 4277df65-4360-35e4-ba67-71fc3a89b67c | -18.10619 | -51.61113 | 2026-08-28 17:26:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 9876fece-5ac0-3dad-9615-09e4fe8dbf2c | -9.86584 | -45.84859 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |


[Clique aqui para ver as próximas entradas](README114.md)

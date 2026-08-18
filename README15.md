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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64a34c5c-dfca-31b1-9fe8-d5dcad7fbb57 | -11.61944 | -46.77859 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1571c1ee-f800-38f8-a033-c17b33995572 | -11.36555 | -46.39412 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9420a08-f2e7-39cf-9c66-5035b31f7490 | -14.16381 | -52.8983 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d9056d7-e641-3462-9edc-27fbdec0ddc8 | -14.30135 | -47.17641 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c5156bd-a9f9-3d0a-bc8a-00fc4d2b4d1d | -14.25482 | -51.92595 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9f92aa31-c13d-339f-ae03-532fd0636453 | -12.0092 | -46.42705 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e8dfde65-48f0-3eab-b3a8-2e0d6ebbf884 | -14.35784 | -51.92084 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2be82d4-4318-30eb-b1da-67d29514cf4a | -14.25354 | -51.9275 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 75eed301-b37f-3bb4-b51d-77c81542e18a | -11.33938 | -45.9293 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51442249-054c-3f32-a10a-c7201acfd8bd | -17.1059 | -46.59004 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 227c24a6-d22b-30c3-b817-d6d4d9138d8f | -13.56529 | -51.77521 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fa50c72-c0d7-3ca1-9c21-30710e13b689 | -14.42804 | -51.88547 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce81f903-dd9f-33c5-b642-868eed47ea98 | -17.0884 | -46.60145 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bba513f1-96cd-3ded-a0b4-e1f8f873fa65 | -12.18483 | -45.15721 | 2026-08-18 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 477deacd-68fc-32b0-af49-57adc34c5688 | -13.50334 | -46.28786 | 2026-08-18 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7818cf9c-dfcd-3c3c-bb5d-e923d4dea6a8 | -14.45016 | -51.83182 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4f35296e-a1a1-3d6b-8dbd-6cb8b449f410 | -11.52391 | -46.63993 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a7323866-38ec-3914-96c9-5a3123d2eb70 | -14.17338 | -52.93165 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bc1daaec-4d54-3439-a21e-ee2e55fd411d | -12.46766 | -54.1816 | 2026-08-18 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89254bb3-65e7-30e3-a939-4b8bd83b904a | -14.39696 | -48.93624 | 2026-08-18 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93b7330d-9540-3f30-a768-bcad3d48c8cb | -12.47015 | -54.19566 | 2026-08-18 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba835049-9b61-3f81-a8bd-45ce521a50f8 | -14.44539 | -51.82718 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf92be97-8049-357a-a746-56b124504185 | -13.44772 | -43.84297 | 2026-08-18 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86d078c4-61a3-3f57-9340-86a6aed70cba | -11.36769 | -55.42079 | 2026-08-18 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6ff4afba-91e1-36c3-81f6-eb173e74b264 | -12.25015 | -43.15622 | 2026-08-18 04:04:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b095ce1-661d-30bb-8d0f-221678fe7cec | -12.45689 | -46.52332 | 2026-08-18 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd8f680f-92a1-396f-93ea-c3f6c3941f96 | -17.94894 | -44.42699 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28e91b9f-409d-3e4b-b907-887a83ea653d | -14.1851 | -52.93436 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7962e557-f1cf-32c6-9183-ec3258583546 | -14.26383 | -51.93355 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d19dbfd-a02b-3d90-9668-8c5d12ce6705 | -12.77438 | -48.42771 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a54de6c-c026-38c4-80d1-9465b203c3c7 | -11.36149 | -46.39347 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40ae0bd9-e75c-3873-88f5-f121b8df3f99 | -17.98009 | -44.4285 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bda50db9-5b43-3065-9ae8-2c1fe59af9fb | -17.09216 | -46.60215 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 625f01c2-ff45-3736-9e6a-2527c05f1196 | -13.27543 | -51.65525 | 2026-08-18 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 178cd944-b46b-3eaa-a8e0-dbeade532a5f | -13.58083 | -51.75497 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ce833a8-e480-348c-967d-dbe1bec5218b | -13.28018 | -51.66033 | 2026-08-18 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90c653c8-6b8a-3f59-9f2c-ba04fd072878 | -17.9659 | -44.42993 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e56cb6a-2ad9-3bf6-8569-ab768b558380 | -14.36058 | -51.87938 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76f32bc5-59ec-3854-8138-8682fce1c52f | -13.56604 | -51.77147 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09760dd3-34aa-315e-84b0-ae38be6e130a | -12.01714 | -46.49917 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 326f1c41-445a-3963-bd59-e07976b1c0fc | -14.8703 | -46.63835 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eee1ed0-73bf-308f-88ec-d38cfee81659 | -16.57275 | -51.62024 | 2026-08-18 04:04:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f53acf89-8559-3853-b4f9-a532a607214f | -14.25507 | -51.92001 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9404d124-ebdd-3130-9499-295cbf64ac6a | -14.35737 | -51.86711 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59ebc674-2948-35a7-aee1-f0b0e1c4b03c | -17.98286 | -44.4329 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a88c343-2b4a-3801-81b6-bc7462141ec6 | -11.36187 | -46.3898 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5e61b316-9982-3baf-926f-e9d3cff788de | -11.12792 | -47.28508 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8ab45a6-f2e1-3a1d-862d-6c939f0a69ae | -15.27022 | -56.50227 | 2026-08-18 04:04:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7865be62-b587-32a4-98ce-0764785924ab | -12.54054 | -47.8493 | 2026-08-18 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28d55f84-f8a2-3124-91e3-fff0a546c397 | -14.2583 | -51.93242 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 64095d00-5f3c-34b3-9575-1fc0817f93e1 | -17.10754 | -46.58057 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cef88962-80dc-3e4b-8f10-bf1370aedc04 | -14.172 | -52.90873 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 79f74626-93cd-3ba1-a631-677fb0bedea1 | -12.47252 | -54.18447 | 2026-08-18 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 552a3de8-6eb5-34ca-bff4-e139c9682109 | -11.13154 | -46.4893 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edd3b8e1-78b0-3300-ac8b-3d8d0ad26ddd | -17.94705 | -44.4384 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a89b85c8-c3bd-370f-8393-5c01b253dcd2 | -13.56837 | -51.70205 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05cf211e-a26c-3838-85b7-8ad2568d01b6 | -14.83059 | -46.63557 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a345f63-925e-3ee2-bc3a-4f363834233f | -11.14252 | -47.27807 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be05ce38-b204-34bb-ad10-08d630409c00 | -11.52462 | -46.63576 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 006e3dbf-5602-3825-b466-2bc78ffc3a98 | -14.35741 | -51.86739 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38681abe-56f6-3eed-987b-daa3fefc501d | -13.4156 | -54.38097 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3a38fc2a-b00a-35cd-9e42-e47ff96b9bcf | -17.10625 | -46.56569 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abb7caeb-4050-3e13-904f-31d536a0cb45 | -14.17395 | -52.89934 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd9b4a97-27c9-31f0-b062-a190d8ac4298 | -14.26229 | -51.94112 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2eb3974-240b-3bef-ae0c-e999bd241a2e | -11.51562 | -46.61446 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96a57cf8-0a67-3a32-9f14-b923565e3a87 | -11.19033 | -49.68499 | 2026-08-18 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddd17911-d206-3fcf-9fd0-505fccbee4fe | -14.28115 | -51.93325 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ab5fa45-abdd-369e-99ed-f1f0b8fc546d | -12.05316 | -46.45995 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38059c5b-048a-3f80-8ed5-c238cb8341c7 | -14.1624 | -52.89597 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 316b1e03-460f-3cea-995a-d0bf808016b3 | -11.12204 | -46.49556 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07373ef8-f305-34db-8bd8-88c68f243df8 | -14.81873 | -46.63442 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b3892802-27d2-33f0-abfe-f294559dd00a | -17.98412 | -44.42525 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e220df60-6548-3fb8-9b8c-e003d0b0df5c | -14.35997 | -51.88338 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b7af456-caee-3764-a60a-878a29e82596 | -13.41106 | -54.33892 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47e8cd88-8c62-384e-93a5-3d0c07894dd1 | -17.10683 | -46.58772 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b130be06-5ff0-310e-9aa1-ccad2f86b2cf | -11.51419 | -46.59837 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38ef36fb-fa2a-3473-95b2-ee7775199ab9 | -15.26317 | -56.50063 | 2026-08-18 04:04:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a1abea03-9b65-380a-8983-2c9b5224b460 | -14.30474 | -47.18087 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97329ec6-8d40-3000-85fa-686c991532cf | -11.45522 | -46.57359 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e77984ae-0487-375d-b9d1-ae403b9bcfe0 | -14.36255 | -51.92589 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dc45d52-925e-3a18-acf9-68e56e528c63 | -14.17107 | -52.91322 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 07ccaf6d-d3e9-3745-af24-0b2b51fa1df4 | -14.8074 | -46.65149 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| e03301a0-25ca-314e-8b8f-8662ec1112ff | -14.16339 | -52.9206 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 2abb3092-1ff5-3fc8-9932-3d1ec9de6432 | -11.35656 | -46.39645 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7df6fb95-ae4c-3ee2-8555-b5db0c1f97a7 | -13.41232 | -54.33473 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34b5c930-27b9-3bcf-b327-13b68188a82b | -15.30157 | -56.44815 | 2026-08-18 04:04:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8024d7c-e635-34dd-a76c-df68180df623 | -14.81784 | -46.63939 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9e85f8f0-7f84-349f-aa48-16b0696c03e4 | -19.2945 | -41.92989 | 2026-08-18 04:04:00 | NOAA-21 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 048e985e-1052-3e86-8126-55703d3017d9 | -11.38976 | -46.39893 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ceaf41f-9d29-357c-a2d5-b16a1e883cd5 | -17.08381 | -46.60549 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1b83845-c294-3bf1-8cf4-0d992bace78a | -11.36619 | -46.3905 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2bb17430-ba26-38b9-aefd-1154b6e818e5 | -14.04021 | -53.69128 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eb478d95-e93a-3ec4-b710-f62345334824 | -14.16141 | -52.90069 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea29172a-04e0-3823-9049-6661860322d1 | -14.36211 | -51.87192 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 668313c6-284f-3bae-9859-916b6836b9bd | -11.52316 | -46.64425 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d9c79b2d-5d1f-3c9c-837e-cdc7441ac5ce | -14.16749 | -52.93042 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 908506f0-8495-3eea-babc-7131a09884b4 | -14.35983 | -51.88305 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed43ec48-8f33-33b5-adbf-677b1e834b38 | -14.18603 | -52.92987 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ed1b1f0a-5d1e-3340-9873-0b64e3e76989 | -14.15951 | -52.9098 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e87c730c-99a5-3ab4-91c6-40a9bcf9d5e5 | -14.8322 | -46.62654 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)

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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44ec2961-c944-3f3a-b549-e9721e68336d | -9.1591 | -50.140701 | 2025-11-18 00:55:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cef297f-17ed-3e80-a21e-66ed968d1d5c | -3.2696 | -50.017899 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f06f7fda-aaab-3173-9f7c-fb5f71b3c74f | -9.3824 | -48.444199 | 2025-11-18 00:55:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca10b0b5-4fa2-314f-b7d3-e49219c521e4 | -2.8624 | -49.463402 | 2025-11-18 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c107830-f22c-3835-a051-c9aba70ad829 | -3.4775 | -46.0802 | 2025-11-18 00:55:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8673ad18-4093-39d9-baf3-eca63f13cf15 | -2.5085 | -47.815498 | 2025-11-18 00:55:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d80e736a-ef8e-3424-8d7f-2508aea431d2 | -2.9959 | -45.4384 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85b7f426-4b8f-3aa4-b405-e705a6dfe49a | -3.8 | -50.125599 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2d030c9-c3f7-3c28-b649-e6cdd558bed3 | -8.2072 | -45.0289 | 2025-11-18 00:55:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e3ad2131-48ae-312c-9ac8-0c123db690ad | -10.2985 | -57.138302 | 2025-11-18 00:55:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f66b2b08-84ae-3976-bfb7-187f754c7dc8 | -2.2949 | -51.7812 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 523375af-754f-357d-980f-6117d48b8628 | -2.4771 | -50.2467 | 2025-11-18 00:55:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e4f6014-3f29-3884-a4d0-ebc458f5eabe | -8.2821 | -44.000198 | 2025-11-18 00:55:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8f9f8e45-e578-33cf-930a-aba7be50ff28 | -2.9783 | -51.076199 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d69e2628-4295-3ff4-b518-5036ee0c4015 | -2.5309 | -58.016102 | 2025-11-18 00:55:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 944cd45c-5c62-343a-bf23-1a667a45a8d4 | -2.9881 | -51.073898 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f09be53-a8e3-3a5b-8b79-aedba7f1fb5d | -8.4637 | -47.966599 | 2025-11-18 00:55:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 063756a9-caad-39fd-aca5-860a2c0ffba2 | -9.4039 | -48.447498 | 2025-11-18 00:55:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba31e672-bea8-3ee3-bf0c-fbe4bde7946b | -3.1471 | -52.257401 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6e8c96c-7a54-3b93-913a-dd77b2865424 | -10.3422 | -48.9245 | 2025-11-18 00:55:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8373210-f947-313a-af1a-9c394c6285bf | -9.7194 | -48.910702 | 2025-11-18 00:55:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f1351bf-30af-3b09-a11a-afaeba46ebcc | -2.8505 | -45.215801 | 2025-11-18 00:55:00 | METOP-C | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 479ceb5f-ac03-39c7-b781-ded7185355ba | -3.0264 | -47.8283 | 2025-11-18 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a685a353-13fb-32b5-849b-35e1fd2448ee | -4.1339 | -52.108002 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd4b929d-5ca9-368d-abf6-a83eb5e288d9 | 1.528 | -55.973 | 2025-11-18 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e737568-4913-3966-b748-e04cb2e52d38 | -3.2715 | -50.025799 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b0692a5-3113-3964-8699-6f1bbd4bc826 | -7.8598 | -46.866402 | 2025-11-18 00:55:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35abaef2-1c7e-315d-9a30-a7d1bf330b21 | -7.5424 | -47.048901 | 2025-11-18 00:55:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e7cfb59-caa1-354a-9cc9-e83b093bf957 | -3.5201 | -50.341301 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d84f306-56d0-309a-8279-11caaa394bcc | -10.9142 | -48.676701 | 2025-11-18 00:55:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ae71439-48e3-335d-a006-bc2a73d3581f | -10.342 | -49.6325 | 2025-11-18 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d175e97b-167d-3c3d-ab1d-499e1501f9c3 | -8.2134 | -48.3046 | 2025-11-18 00:55:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6bd2f795-0dc7-3476-96f6-bf122678908e | -4.5506 | -48.4818 | 2025-11-18 00:55:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8c785e3-09eb-3e15-9a94-dd737e3a61c7 | -3.0723 | -50.2341 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ec8405-d489-3def-852b-e468a51402c2 | -3.3541 | -44.405602 | 2025-11-18 00:55:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 720338da-c6ea-33f0-9d4d-81159c1bfe28 | -3.1742 | -48.019199 | 2025-11-18 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5f28a7e-f1a9-3705-bdfc-1311ef82ebae | -3.4203 | -50.3559 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0088c556-043d-39bb-95d4-82663580e226 | -4.019 | -45.549702 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcfc4a78-3cae-31a3-a17d-64907aad910b | -4.1731 | -44.229099 | 2025-11-18 00:55:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d80a9c1-3281-31ca-b093-677601eecf35 | -3.4779 | -55.428001 | 2025-11-18 00:55:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 668e0e29-4789-3d2d-ba1c-9997c8a1b647 | -9.9699 | -44.769299 | 2025-11-18 00:55:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1f64622-ec35-35bc-bc21-41a273ec257d | -3.1472 | -51.316101 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb6bdcd1-56d2-3f39-8f64-c97bde7f7cc4 | -7.8244 | -47.148701 | 2025-11-18 00:55:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23295687-86f7-3281-a130-0d694d4d906f | -10.535 | -47.989201 | 2025-11-18 00:55:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ee0ba3a-cfdc-357c-a443-da835c4acfba | -9.9731 | -44.782101 | 2025-11-18 00:55:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 44fe7297-8f47-3e53-add3-c79abd29c5e8 | -10.6638 | -49.3736 | 2025-11-18 00:55:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ee6361e-4df3-37fc-8d94-094031b21a27 | -9.7282 | -49.124699 | 2025-11-18 00:55:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2884412e-b458-3b3c-b399-b215af279493 | -3.0288 | -47.8386 | 2025-11-18 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf9f2f5-5253-3b13-bc2a-a366761c7a42 | -3.8294 | -49.807899 | 2025-11-18 00:55:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9a85a4a-ac57-3965-bb7d-beb1da797397 | -3.1596 | -50.165699 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89a1e8a1-f349-3b73-aed8-aee96f565bbf | -3.1335 | -45.7575 | 2025-11-18 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d308f8b4-9608-3768-8f9b-e70043179977 | -2.4735 | -50.231098 | 2025-11-18 00:55:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a54fe457-118b-3e79-ba95-bdfe7ec6aeb2 | -7.689 | -46.842701 | 2025-11-18 00:55:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bf30d12-40d1-3210-86d3-016018fb26c2 | -3.2689 | -52.473999 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d694f23b-a503-3af4-8f2a-18e4ef57c117 | -8.9342 | -49.838001 | 2025-11-18 00:55:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04a055d0-8b38-3239-986e-e3ff512de4c3 | -6.668 | -42.0392 | 2025-11-18 00:55:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4334fe11-27fb-3613-ab8c-b70c0a9f2fb4 | -5.9627 | -52.937901 | 2025-11-18 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b069973-5802-33bc-a242-6de3493be888 | -9.7184 | -49.126999 | 2025-11-18 00:55:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12da031e-56d6-357b-981b-3e6e12758339 | -3.3499 | -44.388302 | 2025-11-18 00:55:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebb9fe16-fb1b-365c-a8d5-f48557f00f02 | -4.5231 | -46.409199 | 2025-11-18 00:55:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5ed3100-81d7-3183-8476-dfe2bc1c4247 | -4.1355 | -52.114899 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f73ed2e9-2773-3682-9442-c3dddc1e2352 | -3.1649 | -51.4827 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88d74f6-4d7f-3d37-829f-ccd0638d462c | -6.1485 | -46.1003 | 2025-11-18 00:55:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f258660e-20d0-3eeb-a5e4-28aa0f949993 | -4.14 | -46.356998 | 2025-11-18 00:55:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 583c4c3b-933b-32c1-af5d-9ecb1ce44573 | -3.3444 | -44.407902 | 2025-11-18 00:55:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 720b2ac1-66c5-3b6b-8c97-cc0eda2658ba | -3.019 | -47.8409 | 2025-11-18 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53aed65b-fb2f-32e9-b040-e1d4b4274e8f | -4.1764 | -44.2257 | 2025-11-18 01:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e3b6a4f9-586b-3ce5-80fb-01bf13faacce | -3.4769 | -46.0879 | 2025-11-18 01:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 74fafd71-b686-3c11-9974-96b2be6656a4 | -2.8298 | -45.4195 | 2025-11-18 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 126.0 |
| ce830d00-c2b1-312d-afca-844506f02ebb | -3.3555 | -44.3798 | 2025-11-18 01:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5ee65846-c978-3fc4-b356-0e8acf5ed8e6 | -4.1949 | -44.2476 | 2025-11-18 01:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f11c1e6e-aae9-3a16-887f-1c72fc6a7445 | -2.8677 | -45.2382 | 2025-11-18 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e9f79952-5673-3e63-9c49-554e59d3c629 | -9.1124 | -44.3334 | 2025-11-18 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bd3b8969-b4e3-335b-b87e-f9bc35d285df | -4.1762 | -44.2486 | 2025-11-18 01:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| fafe8b57-a5c1-30c6-b59f-54c31efe6f16 | -8.304 | -44.0075 | 2025-11-18 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 885e41f1-312d-3ca8-b20d-7b6cf9aef32d | -8.3043 | -43.9842 | 2025-11-18 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 4a518ebb-deae-3865-9a10-bfab78857178 | -12.856 | -41.4813 | 2025-11-18 01:00:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 1517ef82-8a9b-3b3b-a726-c187590d4e6f | -3.2506 | -43.0449 | 2025-11-18 01:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| cdcb4e68-0e0e-353f-abd9-71f910bef3bc | -6.6687 | -42.0314 | 2025-11-18 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 39.6 |
| cdf7b476-e9b0-3748-9a5e-597e9fc3cf7a | -4.195 | -44.2247 | 2025-11-18 01:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 507587e9-77c3-3f18-a59a-df7034f5eaa4 | -10.3535 | -48.9174 | 2025-11-18 01:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 3afa1d38-6fdf-34b4-a50b-dc3d128d765e | -3.1256 | -45.7449 | 2025-11-18 01:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 9ac3f5b6-8d83-3922-8237-15bd10f0e46e | -8.2854 | -43.9863 | 2025-11-18 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 0ce89343-4a49-371e-8a65-af30e2109b17 | -8.2851 | -44.0095 | 2025-11-18 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 193.8 |
| ba89fed4-99cd-342c-a3f8-ced38bd16e34 | -2.5238 | -47.8115 | 2025-11-18 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8dba67e0-c227-3c60-94b5-b5c02783926d | -3.0714 | -45.4107 | 2025-11-18 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| efdd7cb1-1966-3391-bf9e-f628f0f6c5d3 | -6.1138 | -42.9569 | 2025-11-18 01:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 9dfeef55-48dc-3706-8890-20f8b19ccaad | -3.477 | -46.0656 | 2025-11-18 01:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 256.9 |
| d333c333-2468-3073-9ec2-dc1fb20be6d2 | -3.0236 | -47.8396 | 2025-11-18 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 82fec6db-7975-3f34-80a4-bbbb32046636 | -3.3554 | -44.4026 | 2025-11-18 01:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 1ff9a193-64bb-3920-b4d2-57579f99623f | -9.0934 | -44.3356 | 2025-11-18 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 16bf203e-7a75-356c-9eab-82c964ff531b | -9.3969 | -48.4523 | 2025-11-18 01:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 3388250c-c390-3ff9-9347-7c1f6cc1f128 | -3.3367 | -44.4034 | 2025-11-18 01:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3c3b7fe5-c8e0-392f-9cf1-76fff6611c6b | -6.7202 | -40.7943 | 2025-11-18 01:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 2bbb7702-00be-36d5-ab1d-ebf908d22c89 | -3.0714 | -45.4107 | 2025-11-18 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 1d1d2c71-699a-3139-8bb2-027c062e5a02 | -9.4765 | -40.3613 | 2025-11-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 550.2 |
| 7c3d7cb7-a627-340f-8927-f08cb4c98667 | -12.856 | -41.4813 | 2025-11-18 01:10:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 1d3920c4-05ac-3cdf-916b-a770b57c2452 | -3.3367 | -44.4034 | 2025-11-18 01:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 8c71578d-99d4-3874-9730-8310b9a341f7 | -8.2854 | -43.9863 | 2025-11-18 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 170.3 |
| a2b94cb6-5ff8-3041-8b09-14b1c391bc8a | -2.8298 | -45.4195 | 2025-11-18 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 132.5 |


[Clique aqui para ver as próximas entradas](README14.md)

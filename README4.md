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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8efe2bf8-7fd8-3376-8f02-32053e921674 | -20.336 | -57.770802 | 2025-11-17 00:31:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7edabb30-2846-30aa-a7f5-ae1a3330a7b7 | -2.5088 | -47.814602 | 2025-11-17 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eba21f59-a88e-3be7-9ff3-60d1a1d31717 | -3.2215 | -50.964001 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac47e545-1935-37f4-8c9c-d072b6fa474e | -9.7012 | -43.959 | 2025-11-17 00:31:00 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cebec105-7211-3c30-8b0e-458f2e01a668 | -11.7268 | -49.8442 | 2025-11-17 00:31:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2d3a310-09b5-3938-875c-f385b12d4361 | -10.126 | -49.144901 | 2025-11-17 00:31:00 | METOP-B | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46ed8663-c949-33cb-a05c-70b9d2461907 | -11.1223 | -44.922901 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4ca481-f177-3d34-b7c7-676182dd3093 | -6.6488 | -42.014 | 2025-11-17 00:31:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b51ec2c-52bb-387c-97e8-60b74a8d56b3 | -3.5075 | -51.5779 | 2025-11-17 00:31:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9ccaccd-88b6-3dd3-ae71-a333dd5af12b | -3.4277 | -52.1717 | 2025-11-17 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1408aa68-9416-3388-96b1-5c44b86e5bf6 | -11.8454 | -49.2094 | 2025-11-17 00:31:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec2780e3-7de6-3de0-adbe-0e954a400017 | -2.9128 | -54.1576 | 2025-11-17 00:31:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3a9c8a-abc5-3635-9892-ac6d25daf5de | -4.684 | -46.305099 | 2025-11-17 00:31:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cb43837-d7a9-3dab-9350-13f368cf7844 | -2.4747 | -50.227299 | 2025-11-17 00:31:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc910c00-8af8-31f5-b567-bc71f7afb9c8 | -3.7571 | -51.053001 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5642b883-2264-3316-999c-f4bf6da5d747 | -3.6455 | -50.216801 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10a1cc2d-395a-37d9-a7ad-fbbb57ba57c3 | -20.3139 | -57.7603 | 2025-11-17 00:31:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b3d083af-be14-3f65-9444-2c23d23887a8 | -8.5201 | -46.057999 | 2025-11-17 00:31:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c861735c-8995-331c-914b-fed16026d49f | -3.7591 | -51.061699 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b701148f-a026-34a3-b84a-147bfe8de112 | -3.2356 | -50.4911 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2325f26c-36b2-3268-8c79-801f00341398 | -10.6564 | -49.377899 | 2025-11-17 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c03879c-5edc-3aea-a4f3-bb073c1af6f6 | -3.4685 | -49.677502 | 2025-11-17 00:31:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b772aa9-f976-3057-8f30-62fc36e230f7 | -3.7573 | -51.098301 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0ca9e02-2696-395d-954e-74eddf57400b | -2.4991 | -47.816898 | 2025-11-17 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5147e7-cb3c-33d5-b16a-8d97dd8def1a | -4.0524 | -47.484001 | 2025-11-17 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b62c2bba-e602-3acb-89a9-566b3f2b1df2 | -1.5262 | -54.812698 | 2025-11-17 00:31:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f75726c1-f9a3-3373-a266-ae88a509de6d | -2.4957 | -47.802502 | 2025-11-17 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60446331-dd27-31b1-937b-1b48555101c4 | -2.477 | -50.237301 | 2025-11-17 00:31:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6641fac4-18e0-3660-bee2-514ee073f021 | -3.1897 | -50.648399 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d55e8943-628f-38ef-8079-5075e24d2bc9 | -3.7062 | -45.904301 | 2025-11-17 00:31:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff32eee-4118-3d9a-9210-3a64a53957fb | -3.2875 | -51.428001 | 2025-11-17 00:31:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8d264c1-608d-3099-89e8-f824a9e1c9ba | -1.9754 | -51.993401 | 2025-11-17 00:31:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67a776fc-a8b4-3268-b6e8-a06f483c4e9f | -9.6374 | -43.910801 | 2025-11-17 00:31:00 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 383e4ac6-d3cc-3b9e-a9ed-020a54c65886 | -3.0658 | -45.195702 | 2025-11-17 00:31:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1ce9083-3e38-3ff2-9123-48a4e1a6b64b | -9.0551 | -44.778099 | 2025-11-17 00:31:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db5863ce-bcdb-33ab-90d6-6a2323ab34da | -8.5693 | -46.466099 | 2025-11-17 00:31:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d65ab74f-ece4-3c5a-b756-00426082d639 | -3.228 | -50.502602 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2f03fe-d82f-3922-ab79-9891ad70a497 | -9.7338 | -47.219799 | 2025-11-17 00:31:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b53e225-f4e6-351d-8792-1275eca58404 | -12.2195 | -49.6119 | 2025-11-17 00:31:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11a28b28-abaa-3fdd-89d0-cfc825d7f653 | -3.7611 | -51.070301 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7aa58ab-065c-3cbf-a72e-be352b805548 | -11.7019 | -48.867298 | 2025-11-17 00:31:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87714a43-fe32-37ed-b137-00c630b04382 | -3.4569 | -49.9813 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4410a58a-509a-3371-b3c2-a09b4c4b3730 | -2.4672 | -50.239498 | 2025-11-17 00:31:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70376333-7211-34a5-bfac-01ff2e2b0cf3 | -2.6928 | -52.067101 | 2025-11-17 00:31:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90276236-cf63-3b78-bfb2-37474c6597f7 | -3.6491 | -44.732601 | 2025-11-17 00:31:00 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1cc3466-ea0c-3084-a27d-3cba57079340 | -3.8412 | -55.8008 | 2025-11-17 00:31:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb5a72aa-36fd-30b1-85b8-c7dd3b10a331 | -3.2927 | -50.071499 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 460c471b-95c3-3759-acb4-21fac6d27bba | -11.7074 | -48.8466 | 2025-11-17 00:31:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7de1fc1-f108-31ef-afe2-4401a2775113 | -3.4566 | -52.342098 | 2025-11-17 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6661b8-7093-3d51-902d-198514737dd5 | -6.6662 | -42.042198 | 2025-11-17 00:31:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 67959ae5-732b-3c79-85d7-37fac93639ce | -9.3141 | -46.5606 | 2025-11-17 00:31:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1d2b692-b603-3bff-bd4a-63df76d4a16b | -3.4087 | -50.127998 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7efa7a79-e555-37b0-98f7-dfb8edd8a996 | -3.2302 | -50.512001 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49b1bf41-2667-3479-9ef6-461b43ce9481 | -4.9836 | -44.3367 | 2025-11-17 00:31:00 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e268f618-ad5d-33cb-bf72-4940a81dac39 | -8.8654 | -50.187599 | 2025-11-17 00:31:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8647a030-daf4-3c4c-bc7e-3095aed0eaab | -9.7301 | -43.951401 | 2025-11-17 00:31:00 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 401596ba-e165-38f7-b0ee-6f6b034c0fb0 | -6.8418 | -42.850101 | 2025-11-17 00:31:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 74ba1ca2-ff4c-3089-8c0d-21657ee2f13f | -10.3136 | -50.157501 | 2025-11-17 00:31:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b80821c1-cabe-3ec3-bb26-f3af1a7aa15c | -4.0558 | -47.498299 | 2025-11-17 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad12d30c-ecef-3d2e-9a7c-bac55680cacf | -3.527 | -49.091202 | 2025-11-17 00:31:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c01cfb9-d891-309f-853f-1084898dd345 | -3.7747 | -47.742001 | 2025-11-17 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cccc4ee-e226-3973-ad70-2bbfc7b62673 | -5.2151 | -49.574001 | 2025-11-17 00:31:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67639b73-fbf3-3538-87db-0533aa0f19c8 | -11.3473 | -48.896198 | 2025-11-17 00:31:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41921a72-523a-3483-9f69-e8ead134f6e6 | -3.426 | -52.164001 | 2025-11-17 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f892c2e-5598-3a74-b331-1afd3911bea8 | -9.1437 | -48.061501 | 2025-11-17 00:31:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc054492-9175-3899-8d5b-92451bb8d752 | -10.8093 | -44.3027 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2b59c55f-f33d-3679-90da-60c76ad65984 | -4.9795 | -44.361801 | 2025-11-17 00:31:00 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a563fc6-6586-39ef-847f-2163ad1469f8 | -8.3186 | -45.412201 | 2025-11-17 00:31:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2c6d994-ec9c-3830-9f61-46a5158ccaf3 | -9.7108 | -43.956402 | 2025-11-17 00:31:00 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4428552e-5b16-3ccd-b691-3f9581ebea57 | -9.3239 | -46.558201 | 2025-11-17 00:31:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89d0d21e-f886-372c-8e3c-1e7a93644a28 | -1.4652 | -53.412102 | 2025-11-17 00:31:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34d5589f-c5ed-3524-a30f-1c91d1163b41 | -11.8159 | -47.583401 | 2025-11-17 00:31:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3afc9b00-d353-32d6-af88-631f557b7fb9 | -10.3155 | -50.165699 | 2025-11-17 00:31:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 810d3133-6480-3ddf-b61c-8188ab122b47 | -4.7235 | -46.3839 | 2025-11-17 00:31:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9274c86d-9102-340f-b45d-2688bee1e1d3 | -10.8763 | -44.645802 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87613d1a-2982-3aa3-bdf3-719fb98abad5 | -3.5156 | -54.361301 | 2025-11-17 00:31:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d5751de-bef6-3ab2-9610-45e3fd979f13 | -10.9463 | -44.515598 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f7a1fc5-ea85-3a8c-9e14-5668eb391892 | -8.2853 | -44.173801 | 2025-11-17 00:31:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de10bb6b-87d7-3a72-a838-fbb06eb56c2b | -3.24 | -50.5098 | 2025-11-17 00:31:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9ca1639-f7ca-3314-bca3-3dda59b6b183 | -4.8741 | -44.849899 | 2025-11-17 00:31:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e12e949-71a1-341f-9012-1baa63d15810 | -11.8335 | -49.202999 | 2025-11-17 00:31:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc97914a-ba01-3588-8272-67783e587c1b | -10.5302 | -47.904099 | 2025-11-17 00:31:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 438f60f9-0b81-3ff6-bda1-956f7eaf6bf0 | -4.0474 | -49.0299 | 2025-11-17 00:31:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe477b38-0eb8-339a-9a28-f836077a815d | -2.5122 | -47.828899 | 2025-11-17 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c10e6780-4f6a-308e-85f8-a7bfaf7bf983 | -11.7117 | -48.864899 | 2025-11-17 00:31:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1002abec-044f-366b-b4b0-0af9885c5c5b | -4.8889 | -44.8685 | 2025-11-17 00:31:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c03efa0-f472-338c-8545-69a1a8162b75 | -4.68 | -46.2883 | 2025-11-17 00:31:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac3cac2-5632-3897-8b82-e7635f5a596a | -3.4238 | -52.918701 | 2025-11-17 00:31:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a58c67e-98f4-3da2-b9da-fc143487e3a4 | -3.4593 | -49.991299 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 044228da-a76d-3b3d-aca7-a254671fdd68 | -9.0454 | -44.780602 | 2025-11-17 00:31:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 87d9b68c-3bc8-3f56-a109-e71f6c48b981 | -2.6812 | -52.061401 | 2025-11-17 00:31:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e551b3a3-7e43-36ff-be20-ea5333d1d1e3 | -10.9115 | -49.408901 | 2025-11-17 00:31:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dde23b68-2775-3396-8785-8bda285eb5fa | -11.3375 | -48.898602 | 2025-11-17 00:31:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc5064c-ac50-397e-b4aa-6462000fb4a9 | -3.4334 | -50.101601 | 2025-11-17 00:31:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68d41786-e4f3-30e9-b6c5-9439975a571e | -9.5711 | -49.1124 | 2025-11-17 00:31:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 982b0287-87b7-3ffe-823b-46cd9c610960 | -3.7107 | -45.922901 | 2025-11-17 00:31:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8eecf11b-b972-3de0-b4bf-98151c01feeb | -6.6873 | -42.0535 | 2025-11-17 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 183.8 |
| 777c363e-3e8d-3e8d-81b8-85ac9bf416ef | -11.7017 | -48.8692 | 2025-11-17 00:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e86b8618-efb9-30cb-af4a-dde10e32d47c | -10.6687 | -49.3813 | 2025-11-17 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 3bb90e12-9629-320f-bb44-2513d1a1cc97 | -9.5343 | -40.3282 | 2025-11-17 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 527.0 |


[Clique aqui para ver as próximas entradas](README5.md)

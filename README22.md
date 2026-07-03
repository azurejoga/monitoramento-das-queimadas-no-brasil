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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2b4dd0c-b96d-3611-ba91-17b0aa586a3a | -7.7958 | -47.1569 | 2026-07-03 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f5160501-72ee-3193-9f8c-af80f812d600 | -11.4345 | -46.5291 | 2026-07-03 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6b60af36-9154-3286-b22d-bd03f31f1d38 | -19.5078 | -52.7365 | 2026-07-03 14:30:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 0bef8575-72c7-3c9e-840c-a93184b63fdd | -6.9135 | -43.7281 | 2026-07-03 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 108dd439-b13f-3bc9-8d44-3129a91596f3 | -5.7945 | -45.0586 | 2026-07-03 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 9b0249a3-3986-3fc1-875d-ac491936f749 | -8.6919 | -54.5873 | 2026-07-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 84fc44f9-eb63-342d-b669-b895d23da794 | -3.8857 | -42.9675 | 2026-07-03 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2a0f0491-db12-3b17-a090-3467e55bfccf | -19.5078 | -52.7365 | 2026-07-03 14:40:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f23818ef-917c-33a8-9f04-484770ba647d | -3.4261 | -41.6901 | 2026-07-03 14:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 437cc4f5-5a23-3b40-b2b3-aa7de9681fc5 | -12.4947 | -48.2607 | 2026-07-03 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 7c0d98a0-f562-30fb-8911-7e32e9714ffc | -6.9135 | -43.7281 | 2026-07-03 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 2b4b1f01-4db9-3758-b40f-c0bd2d264a27 | -11.4345 | -46.5291 | 2026-07-03 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 75a390a7-4869-39bb-bc7a-a4ddfaefa596 | -8.6921 | -54.567 | 2026-07-03 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2eaad93c-73c3-3c1d-b308-5f707bedf2b6 | -6.9326 | -43.7032 | 2026-07-03 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2d9506a1-a953-3108-8659-a15e16b57941 | -6.9323 | -43.7264 | 2026-07-03 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 150.2 |
| e174f920-d523-36d4-bdfa-82f91a651707 | -12.7548 | -44.5428 | 2026-07-03 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 62a82a97-0405-30b9-9f02-d4c15f72e417 | -5.7945 | -45.0586 | 2026-07-03 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| b277b550-55f7-3572-9c4b-40e139ce9156 | -3.4259 | -41.714 | 2026-07-03 14:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 202.6 |
| 907ce344-34a4-3bf1-ba6a-b42166f63c2d | -12.5138 | -48.2581 | 2026-07-03 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 3ec9671d-470b-3286-880a-3ac27f145623 | -12.7553 | -44.5194 | 2026-07-03 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 293.3 |
| 60365399-e884-362a-911b-3a9e112cf132 | -5.5907 | -42.7164 | 2026-07-03 14:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 3789e010-8353-3c0d-bb6d-d75e5ed0ebd2 | -6.9138 | -43.7049 | 2026-07-03 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 851a0916-ab9d-3f74-bc96-f6958996d2f3 | -11.0201 | -49.989 | 2026-07-03 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 1d8bf7a8-d5d5-358b-b719-fd419db2f060 | -5.7945 | -45.0586 | 2026-07-03 14:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 3aa37adf-2907-3097-bb36-71afe105cc30 | -11.4345 | -46.5291 | 2026-07-03 14:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 905b32ba-a3a2-3f2f-a7c0-379446770dfc | -8.6921 | -54.567 | 2026-07-03 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 29d35ea4-6fce-39e2-b54a-e12e02440b9c | -5.9255 | -45.049 | 2026-07-03 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 9e61f28b-dd89-3288-8a45-a7d3744ef47b | -12.7553 | -44.5194 | 2026-07-03 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 266.5 |
| b490854d-7f4b-368e-bd78-a38e47ed9f35 | -3.4259 | -41.714 | 2026-07-03 14:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 148.1 |
| b0ba4bf1-39a8-39e9-a82b-c1b25efbded9 | -12.5138 | -48.2581 | 2026-07-03 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 3b24d63c-6cbe-39dd-8430-3db3e78fdfa8 | -3.4072 | -41.7149 | 2026-07-03 14:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| d39d9e88-68b5-3642-844c-91f94f896814 | -12.7548 | -44.5428 | 2026-07-03 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 976f407f-8e36-3c25-88d8-851355eb5fa1 | -10.3953 | -50.0132 | 2026-07-03 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 65b14df3-2c6d-39c3-a4cb-35806b83e13d | -8.6919 | -54.5873 | 2026-07-03 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3a65c196-8ebb-3186-a9ab-41a0868dd15f | -6.9326 | -43.7032 | 2026-07-03 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 1f66bb8a-540e-3375-b83c-64cbe9ab0bf7 | -6.9135 | -43.7281 | 2026-07-03 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 99f1d83a-e121-37d7-bed8-869840764b10 | -19.5078 | -52.7365 | 2026-07-03 14:50:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 10b26494-8b7b-35e4-9079-786be8bed45f | -6.9323 | -43.7264 | 2026-07-03 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 2ae71aa4-8340-3919-98b4-7a04715454dd | -11.6984 | -51.6391 | 2026-07-03 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 82ab5328-1f20-3dcf-84fa-b25cfa234e5f | -11.0201 | -49.989 | 2026-07-03 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 41eb0b58-b540-330f-abc8-3af65d26e43a | -5.9068 | -45.0504 | 2026-07-03 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| d28d2b79-d675-3224-9ad8-811fe31ea01d | -8.6919 | -54.5873 | 2026-07-03 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 56d5c2f5-8490-34b9-bd8b-d27abe6f9ab2 | -6.9323 | -43.7264 | 2026-07-03 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 288.1 |
| 423d8f73-fff4-3fde-a015-ea25f3602322 | -6.9135 | -43.7281 | 2026-07-03 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| cb6d9dd4-7b93-34e8-a91f-6681697f869d | -10.3953 | -50.0132 | 2026-07-03 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 57a512f2-24e7-3897-be13-2db475ec9574 | -11.6984 | -51.6391 | 2026-07-03 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 3e200648-7b13-322b-9d13-3aed6c4b4ead | -10.395 | -50.0347 | 2026-07-03 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 0efb0706-a5cc-30b5-bc0b-c02b265492ce | -11.0201 | -49.989 | 2026-07-03 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| caf4d985-ee06-3c45-8eab-947b94147b99 | -6.9138 | -43.7049 | 2026-07-03 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 4aefa2f7-558c-32dd-a026-a555b8a11490 | -3.4259 | -41.714 | 2026-07-03 15:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 799a7b80-e668-39d6-9c5f-d426ddccc451 | -5.7945 | -45.0586 | 2026-07-03 15:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| d68df726-68de-3491-b6e6-4e9b8f8066e8 | -8.6921 | -54.567 | 2026-07-03 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 9e6c2710-4a73-3ff7-aec4-9b1ab24fdc70 | -12.5138 | -48.2581 | 2026-07-03 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 1f37f15b-a99d-3934-a96b-c9a4ea323eb0 | -19.5078 | -52.7365 | 2026-07-03 15:00:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2cf9807c-9567-3d09-89f6-69d622a18d21 | -6.9326 | -43.7032 | 2026-07-03 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 621f717e-df08-31f7-8f51-177302827f78 | -12.7548 | -44.5428 | 2026-07-03 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 5c607e7d-c822-3945-9297-cecec304153a | -6.9323 | -43.7264 | 2026-07-03 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 247.9 |
| 98480ccf-b087-3246-ab21-87c2f69976cb | -19.5078 | -52.7365 | 2026-07-03 15:10:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 96975ce6-274b-3bb7-8674-62aa98e3d42a | -5.7945 | -45.0586 | 2026-07-03 15:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| e66641a1-e0ed-3cc7-9f0c-af10fee8405e | -6.9326 | -43.7032 | 2026-07-03 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| dc0ae6b3-b7fc-327d-b4a1-5f30c6d986f3 | -6.9135 | -43.7281 | 2026-07-03 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 786bf1ec-c7cc-392f-b839-f9c709963b4c | -6.9138 | -43.7049 | 2026-07-03 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 91953f64-5356-3210-b46a-4ff9fe67881e | -8.6919 | -54.5873 | 2026-07-03 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| bcdcc065-3305-336e-b3df-82778f5ebc23 | -12.5138 | -48.2581 | 2026-07-03 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| ea61168e-8d4e-334b-9852-9d2c0a245675 | -11.0201 | -49.989 | 2026-07-03 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 45842491-0b8f-399c-b6ca-5a5abb86888b | -10.3953 | -50.0132 | 2026-07-03 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 4215c22a-7eeb-3fa5-bc2c-c84e5824cef1 | -8.6921 | -54.567 | 2026-07-03 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 29c4c0f7-efd1-3503-b31a-799d81ef924e | -10.395 | -50.0347 | 2026-07-03 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 9a083268-8385-3b11-9aa5-6bf2238548c6 | -6.9326 | -43.7032 | 2026-07-03 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| d7b1b2aa-15e8-3450-bbc6-e9f5c573f094 | -6.4877 | -44.9828 | 2026-07-03 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 05a4391c-3e7f-3ef1-a340-c8df8e5f949f | -6.9135 | -43.7281 | 2026-07-03 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 155.0 |
| f9b68dd7-d8ff-366f-ae2b-7287c9d9e37c | -8.6921 | -54.567 | 2026-07-03 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| dac8b549-ed69-3b2a-b018-431d1f5cf319 | -19.5078 | -52.7365 | 2026-07-03 15:20:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 986255ce-9f18-3aab-afa9-0fe83a5e9d05 | -10.395 | -50.0347 | 2026-07-03 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 590b369a-480c-3d68-866f-dd0f581d1f19 | -6.9138 | -43.7049 | 2026-07-03 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e11672e2-93c7-315a-9394-716932b837b2 | -6.4879 | -44.9601 | 2026-07-03 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| cd7771f4-f260-324c-8838-d2dac6585d27 | -6.9323 | -43.7264 | 2026-07-03 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 739ce841-e308-3375-83d4-2ad27420ed09 | -10.3953 | -50.0132 | 2026-07-03 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c45ec373-0a3b-3161-935e-5d9968afd97a | -11.0201 | -49.989 | 2026-07-03 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7c73b7f0-7c6e-315f-a530-4f4697cb5c61 | -12.5138 | -48.2581 | 2026-07-03 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 45d959df-6fbb-3833-ac95-b09bfb6611ff | -8.6919 | -54.5873 | 2026-07-03 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 062db4f1-2248-3857-bad4-2d72cb930153 | -8.6919 | -54.5873 | 2026-07-03 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 37cfb871-080c-3804-bb8f-889bea2291c3 | -6.9323 | -43.7264 | 2026-07-03 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 192.1 |
| af159e13-4830-34ee-bec9-e15a5ee83f05 | -6.9135 | -43.7281 | 2026-07-03 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 0e013e10-b99b-3fc8-afdf-71edd85ecc82 | -8.6315 | -55.0754 | 2026-07-03 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 0c789648-3fd0-3ce7-ab1e-88fb76d2cd12 | -11.0201 | -49.989 | 2026-07-03 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 3583783e-0d77-3cab-9d2b-ca20bed7d529 | -8.6921 | -54.567 | 2026-07-03 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| d015e0ce-73ea-3da9-86af-757d399b832e | -6.9326 | -43.7032 | 2026-07-03 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 7bfb28e7-34d9-317f-a15c-a8b9d1bf14d1 | -19.5078 | -52.7365 | 2026-07-03 15:30:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7f8b1e90-d2a3-39ae-a989-ddb0b9126961 | -12.5138 | -48.2581 | 2026-07-03 15:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 7fedf958-354e-30b0-ab48-5096c3f03678 | -6.9138 | -43.7049 | 2026-07-03 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 1e1ea530-3352-3f6d-b837-2299448a37d8 | -3.8671 | -42.9685 | 2026-07-03 15:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 0fe348d7-e567-353e-8cc6-746940ffeac8 | -19.5078 | -52.7365 | 2026-07-03 15:40:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| fb67a2ad-990c-3865-aa98-1ec137896087 | -12.5138 | -48.2581 | 2026-07-03 15:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| c57b7149-a73a-30d1-bcf3-47e42de686ff | -8.6315 | -55.0754 | 2026-07-03 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| ad4725cc-68b3-3f5a-93be-2e50331e6c0c | -3.9722 | -47.2143 | 2026-07-03 15:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 666c4ae0-5008-39a7-8fc0-e9ac13c71199 | -6.9135 | -43.7281 | 2026-07-03 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 3f3b6316-b2ed-35c0-8232-78ff86a33463 | -8.6919 | -54.5873 | 2026-07-03 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 9196c30f-0c2a-3af0-ac5d-b09ede06fb01 | -6.9326 | -43.7032 | 2026-07-03 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 57eaeb2e-33db-3184-9ab3-1c1999893eef | -8.0448 | -46.7131 | 2026-07-03 15:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |


[Clique aqui para ver as próximas entradas](README23.md)

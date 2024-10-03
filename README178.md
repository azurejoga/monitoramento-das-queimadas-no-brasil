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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 317971c1-5bdf-30b2-b2fb-f0e374c16ad4 | -16.08743 | -50.43067 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25eda290-409c-391b-a606-b573a5f18f97 | -16.08704 | -50.43126 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19f16348-4b3f-391f-a43c-e79df9b73430 | -16.08183 | -50.42801 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 061636e8-3912-3583-a7af-10b843f214ff | -16.08145 | -50.42868 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ddcb8c7-b5c7-3607-8bf2-5cdda5f413f7 | -16.08127 | -50.3239 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a00f93f0-1d4e-315b-bf3d-141bc65cf578 | -16.08096 | -50.32279 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7340034-d95c-3c2a-9e8e-5e41e5a01a8f | -16.08085 | -50.32775 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbfc3fc8-b8c7-3db1-b134-8137c0ead12b | -16.08056 | -50.32665 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0e68141-8051-3c0e-8c56-8135ad8df0f8 | -16.08015 | -50.33058 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86070ff7-c78c-34ad-9738-42e93665bf54 | -16.07602 | -50.31791 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f6fa86d3-b98b-3aa5-ba15-d72cf66d05ad | -16.07557 | -50.32195 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e3e1c547-fc2b-36ec-b301-04c7ba59e84f | -16.07524 | -50.32087 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0997f59b-3783-3b38-927a-10f7596bd35c | -15.35018 | -51.55436 | 2024-10-03 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5ad76d9-53c9-3e80-9dd7-5ebfe21bd2ed | -17.83512 | -50.81189 | 2024-10-03 05:18:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 562994aa-f81f-3805-9833-320d5342d092 | -15.67653 | -52.50774 | 2024-10-03 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b99cdb68-b549-3997-a669-e5ad0e7512ca | -15.67619 | -52.51066 | 2024-10-03 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 493e52ee-76cc-3b6b-8f8d-d9bff0b0a636 | -15.67152 | -52.50694 | 2024-10-03 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae538ae3-c348-3940-a10e-f45f157071a7 | -15.67117 | -52.50988 | 2024-10-03 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a6c2cd8-7435-3b30-9584-b60b3dc7e161 | -17.61444 | -53.14927 | 2024-10-03 05:18:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33f679bc-f521-3b9e-80f8-c63148fc370e | -20.00726 | -55.45867 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 436eaeb4-0e75-3ce0-a180-6c2bf78058a7 | -20.00342 | -55.45335 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d3890b3-3413-3367-a035-ac6eae2936be | -19.99902 | -55.45284 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89943ca4-2dbb-389b-b7e9-407336e047ab | -19.99849 | -55.45743 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de770e90-0d15-334f-96f2-23a58fd137fe | -19.99463 | -55.45232 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4ef976c-7770-33c9-9018-ebd3b7fb4db8 | -19.96397 | -55.48174 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66db49bd-3c65-3031-8287-f8e0786304f4 | -19.95961 | -55.48104 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76375fd6-0fc9-3df9-961b-15384832ff20 | -19.95909 | -55.4853 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83a516d3-ea4a-3010-9e03-8b001b217693 | -17.83006 | -57.68983 | 2024-10-03 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1b2ca40d-aa36-32e2-bd2c-f0c47cd10b25 | -17.05424 | -56.6994 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0acf11ee-28e5-3d53-bc53-6f3450ef4904 | -17.05035 | -56.69883 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b3e8730b-a23e-34d6-85fa-a5ddbe9f7453 | -17.04578 | -56.70336 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3233901c-7dec-3af2-9f27-ece193cd7eeb | -16.97259 | -56.59136 | 2024-10-03 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8b66cf6e-defb-380c-be06-fa82705807ce | -16.96867 | -56.5908 | 2024-10-03 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f7b15e78-4821-3ff8-ba6b-6be0cf683f97 | -20.0551 | -55.95736 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 23a2ae27-0051-361b-bb95-3eab8ba3c7c6 | -20.05085 | -55.95677 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 37334c55-5c9c-3a5f-a53d-3c5e2328c8ce | -20.05035 | -55.96095 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d4bb9baa-a948-3cc6-8f2b-491bbb5a9e13 | -20.0461 | -55.96037 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7ef09c46-a722-3750-8d61-f08383bdc263 | -20.04185 | -55.95978 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 03c85930-f8a3-3254-b103-cfb7df6da6df | -20.0381 | -55.95502 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1d2bc8aa-ce2a-3823-9cc9-ed61c0321e37 | -20.03486 | -55.9529 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6a463f62-9987-30e8-8a0b-dbddcff1bd28 | -20.02957 | -55.96066 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| d623e62d-3b99-329c-ad7b-0967e4fed0bd | -20.02911 | -55.95802 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| da80c944-06bd-3a5b-9845-63c8e7bcba7c | -20.02861 | -55.9622 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 833171bc-c08a-311e-9388-0e1cf7c3ffaf | -19.65783 | -56.47141 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fa270b53-a043-3ee8-8cee-8d69cdda5035 | -19.65374 | -56.47083 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2eb748a2-c574-3837-be59-af233d817fa2 | -19.63792 | -56.56541 | 2024-10-03 05:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a372c939-2958-3f44-9407-cf7ecfe654ec | -16.60248 | -57.22341 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2f77f646-7504-3849-baf7-0535e623f33f | -16.59742 | -57.23224 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2399caca-f732-3310-a019-1592a1e5488e | -16.55369 | -57.41039 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 33dff384-e28f-3e17-9cd8-c623f9d36514 | -16.54997 | -57.40984 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d7c38c16-71b7-3ab7-9ee8-5df18a23f9db | -16.47142 | -57.44216 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cf5710fd-85d9-364c-83d2-051248dff603 | -16.469 | -57.43246 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 53242611-d787-3148-9d12-42989b1bba32 | -16.46529 | -57.43192 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3db7539c-7211-3fb2-8c68-8e114f50f038 | -16.4603 | -57.44053 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 7d3f4028-1b8c-3fb4-900f-55f3e3c262ee | -16.45902 | -57.44968 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 96bfc256-621e-39f4-8165-f057eda505aa | -16.45659 | -57.43997 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6da39c83-b47e-3754-a0af-21909a5886a7 | -16.45531 | -57.44914 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 55532908-3f19-38e9-956a-f305c496c124 | -16.45225 | -57.44399 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1c5a5436-1c92-3c90-9e57-d1d4d7dfa863 | -16.45161 | -57.44857 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3461307d-eaab-3289-8588-b484136306ac | -16.44854 | -57.44344 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2cb493ea-09b7-3b3a-a8a9-6e2132887a3f | -16.44484 | -57.44288 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a1f3fd43-4bf3-3452-b29c-a74e1d0292af | -16.4442 | -57.44745 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e70bf8ec-bd79-3bbe-b062-439bf129635b | -16.44004 | -57.39547 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| de8b9311-7869-3548-9888-1237f97de31e | -16.43941 | -57.40004 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 22304d9b-6018-334a-be55-7a85a791d010 | -16.43633 | -57.39491 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 677d6b73-5f89-3ba3-ab0c-905a1971585f | -15.57326 | -57.46639 | 2024-10-03 05:18:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa19a00d-cf03-3f2e-a2d0-07cd97f7e4c2 | -16.60183 | -57.2281 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ee0c3f2f-4d3f-3b91-92cc-2f0ccb6e2e97 | -16.55305 | -57.41497 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6f4672d1-f2e5-3e43-9415-c6d6bab8600e | -16.54934 | -57.41442 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d8cc06fa-0bb1-3f8c-8e41-2a018466ea44 | -16.46771 | -57.44161 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3eaeef17-a851-3fff-99aa-09b94dd79393 | -16.46465 | -57.4365 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 665b3457-4e00-3469-82d8-36538ceaa2c8 | -16.464 | -57.44107 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 651d2cd9-90c6-323f-9fb0-af5647db0fd7 | -16.4615 | -57.29514 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8c3e3681-f00b-38a8-abd1-440389d4a4b7 | -16.46094 | -57.43596 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 497df8eb-3ed8-3ab6-ba4f-1c0fdf19b103 | -16.45966 | -57.4451 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| edb29b94-0325-33ce-9d59-a37535ee5ae9 | -16.45595 | -57.44455 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3f1e1aef-d2f2-39b8-972c-47b471722ca9 | -16.45288 | -57.43943 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d1469162-2297-3e79-a5e0-d6aa83632a29 | -16.44918 | -57.43888 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cae21d5c-2ac9-3309-adde-7c47411c01bc | -16.4479 | -57.44801 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 05b8e565-62dd-3e46-833e-40503fc62f38 | -16.44547 | -57.43832 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 49edec5d-1a20-312a-a0bb-6399a5959984 | -16.43696 | -57.39032 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 680f6534-079a-3674-b262-bb352a72e9b4 | -16.4357 | -57.39949 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4144b039-173c-3284-9b51-9bb80c7f1433 | -15.69856 | -57.4249 | 2024-10-03 05:18:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3217accf-9c73-3987-9826-dd4410247d8c | -15.57693 | -57.46695 | 2024-10-03 05:18:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f52955a-11a6-30c8-b93d-60fbb24dc305 | -15.5763 | -57.47138 | 2024-10-03 05:18:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5cf0316-afc8-35b0-8e7d-437b9f4ec1e4 | -17.04231 | -56.75975 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| acd15d2f-feb2-3c54-bfa0-4d1d30cb5119 | -17.03909 | -56.75413 | 2024-10-03 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1b9ddf36-b420-3e39-a331-b40a1c0941c4 | -16.91242 | -57.69601 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3ec4ab18-a28c-359e-b71e-fb5a3f13ec00 | -16.91181 | -57.7005 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0e62313f-022b-3987-9bdb-eaf38deda111 | -16.90875 | -57.69546 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| be121c86-762a-3a0b-a307-aa45db04d378 | -16.90507 | -57.69491 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 55b4505a-65f5-3cde-ad48-686490a457d4 | -16.89587 | -57.67976 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 218b08ee-6889-3c12-a349-13315067e5d6 | -16.79719 | -57.64591 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b09364a8-72ca-31f7-a120-18233f8ea2c8 | -16.79375 | -57.48323 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 88fe0ab8-ae70-3fbe-b47f-4a26f9000bef | -16.7824 | -57.82802 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 71bb9f85-3f87-35de-9e3c-80cbc9361ea0 | -16.78179 | -57.83243 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0d6c18e7-b3bc-3677-809b-f9f1b8761a93 | -16.77875 | -57.82747 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 5cc8df18-51d8-32a9-ab44-ac4b34033913 | -16.76781 | -57.82582 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ed870305-be46-3ac0-b28c-39ff8133b735 | -16.69867 | -57.47095 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bb1bbfec-e147-3834-acf5-39fadccaf5f8 | -16.6956 | -57.46582 | 2024-10-03 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |


[Clique aqui para ver as próximas entradas](README179.md)

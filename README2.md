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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a800c69c-fbcc-3f5e-9ec0-93438ed048cf | -15.3596 | -47.0724 | 2025-10-01 00:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 482442a1-cfb8-394c-92f3-789b113f8da4 | -5.655 | -43.9013 | 2025-10-01 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 52ad74d9-061f-399c-b3d9-13ff6cd30fa6 | -9.4206 | -54.5753 | 2025-10-01 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 56140f9c-120d-34ce-aa80-af5e57157818 | -10.0337 | -50.2424 | 2025-10-01 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 567d3fab-d858-35f0-b96c-3292e7ec19ff | -11.3858 | -44.8923 | 2025-10-01 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7a9e7afd-6de5-3105-aa2d-65574e853d5b | -21.0572 | -45.6638 | 2025-10-01 00:10:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 75312c84-7565-3bdf-bc56-4d616b4b33a7 | -9.9193 | -43.6508 | 2025-10-01 00:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 29b17987-b579-3327-b067-ad63b9582299 | -6.2707 | -44.1766 | 2025-10-01 00:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 6a157c35-ee49-334c-9575-fc1ce489da5a | -6.1001 | -42.4391 | 2025-10-01 00:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 12c3f5d4-6c8c-3a14-bae6-ac62bcc6d3bd | -16.0225 | -50.8771 | 2025-10-01 00:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 91409ca5-6704-37b8-8869-565ffa34030b | -3.1013 | -47.0082 | 2025-10-01 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 5e00a354-0b6a-3ec3-8805-1eb82c5836b2 | -21.0365 | -45.6693 | 2025-10-01 00:10:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 129.3 |
| ee1e83a7-eaeb-3d12-b68e-5b66270d369b | -11.4784 | -45.0637 | 2025-10-01 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| fd35cf29-83bf-31af-8d93-7feedccd2c91 | -6.4607 | -43.9301 | 2025-10-01 00:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| a02c3fdf-68e0-368b-b311-e2bbd8ffd56a | -3.5161 | -49.4528 | 2025-10-01 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| a6fff95f-9493-3ea4-bc9a-a12063a62766 | -6.949 | -63.1048 | 2025-10-01 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2679a465-1b21-3137-a909-0d4ba231c4f4 | -3.1012 | -47.0301 | 2025-10-01 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 6764ebbb-de32-31d5-8248-c3a7a897ed6c | -9.2902 | -54.5242 | 2025-10-01 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| eaaf84a3-5fc4-3826-9256-20282e0309c4 | -8.5587 | -44.7414 | 2025-10-01 00:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d9bc5cda-20d5-36de-a51c-887b06b99201 | -11.1523 | -54.3104 | 2025-10-01 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| daae9ba8-1d51-3a28-a100-7585631e3cdb | -11.8246 | -44.9669 | 2025-10-01 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| d0347ab7-1fa8-3b65-b75c-47fa2e148b03 | -13.3274 | -47.8536 | 2025-10-01 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| dbfa64ec-4e51-3b8a-9ab2-46ce685c75a1 | -8.559 | -44.7184 | 2025-10-01 00:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 67c4d014-1a18-3497-ae0d-6d95c6cd0836 | -5.6548 | -43.9244 | 2025-10-01 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 99836929-d4a9-304d-b212-0ae73fca9a33 | -5.8657 | -43.3981 | 2025-10-01 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| bd6800fa-56cb-3a83-9fe3-ee9ad3843d89 | -22.2844 | -46.709 | 2025-10-01 00:10:00 | GOES-19 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.7 |
| 47dc3eda-8c35-37c1-b093-7f0746e809f6 | -9.3089 | -54.5229 | 2025-10-01 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| cf226999-bad0-3a23-a2ac-2d05f9fc4238 | -3.4762 | -50.0883 | 2025-10-01 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 15843c27-a6ed-340d-8be5-4224e550e7c6 | -21.0365 | -45.6693 | 2025-10-01 00:20:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 73b278c1-5ca3-3a39-8f9b-4db337f16565 | -11.1523 | -54.3104 | 2025-10-01 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 2edcc1fd-52e1-3c2c-83e3-5e2661301db0 | -17.9778 | -45.0057 | 2025-10-01 00:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 97de7f33-2b8d-314a-813c-fb708b749f52 | -10.1084 | -50.299 | 2025-10-01 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| de2c0e2f-bd92-38ed-8b51-e75c9befcacb | -22.1217 | -44.6886 | 2025-10-01 00:20:00 | GOES-19 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.6 |
| fa62139a-1687-3af6-aefe-ecedafde0023 | -3.5161 | -49.4528 | 2025-10-01 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 242493b8-cd03-3c20-94ef-9a5c709a2469 | -13.7687 | -47.9659 | 2025-10-01 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 839c5c2e-7630-3f00-a1c8-c53fc57152c3 | -9.0821 | -48.0252 | 2025-10-01 00:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 0a955d73-a482-3580-a9be-8802c6fd2754 | -12.8949 | -45.264 | 2025-10-01 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 90d200bc-37b5-3010-ad41-8547cf7494f5 | -9.938 | -43.6718 | 2025-10-01 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 560.8 |
| c31b036d-dba2-3350-86a4-b55473354f21 | -16.2562 | -50.9275 | 2025-10-01 00:20:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 0bf60302-f675-30f2-bf9b-0934338013ab | -11.3858 | -44.8923 | 2025-10-01 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| dcb0f18a-8c09-38c3-ad02-ab65d426beca | -13.3467 | -47.8508 | 2025-10-01 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 093ece1d-65ed-325d-8f19-d8830642c84f | -6.2707 | -44.1766 | 2025-10-01 00:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 97be6dfe-4e63-30ae-9f2e-0e8f78165d3d | -11.8054 | -44.9697 | 2025-10-01 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| bef11528-cb22-34b3-9ea0-6e2b1426e3df | -13.2973 | -50.6605 | 2025-10-01 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 248.0 |
| 25131139-723a-3de8-94d1-175f0e277146 | -20.6103 | -46.2098 | 2025-10-01 00:20:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 1dfbbeb4-529d-3113-bf8b-73580d9328c9 | -13.3278 | -47.8313 | 2025-10-01 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| bb9b21cd-8794-3d91-8265-b21896c0c310 | -13.327 | -47.876 | 2025-10-01 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 5135e23d-df35-34d7-8449-5f37b1240a20 | -8.5587 | -44.7414 | 2025-10-01 00:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0b49ff3a-0d12-38f5-a312-863a54b79c2d | -13.3274 | -47.8536 | 2025-10-01 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 1ecab463-c931-3bf2-9283-784da2d4390f | -6.4607 | -43.9301 | 2025-10-01 00:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 99c6d844-a6c3-3a24-a920-7ead1b61c9f2 | -3.4577 | -50.089 | 2025-10-01 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| a7ecfa7e-3df6-35a9-beca-d9afab3d3292 | -9.9376 | -43.6953 | 2025-10-01 00:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| fc6a9a27-dd93-31af-a34b-82baead48f02 | -10.0895 | -50.3009 | 2025-10-01 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 71c71ab1-0223-3106-ad87-839e2cd59ba8 | -13.2976 | -50.639 | 2025-10-01 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| aa73cc7c-7f28-35b8-964f-5682dc088f34 | -9.9189 | -43.6743 | 2025-10-01 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 275.4 |
| 802685a1-8463-314e-af91-2f13e2d0dd5c | -20.6309 | -46.2046 | 2025-10-01 00:20:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b2be89eb-630a-3922-ba3f-7fa56f818a50 | -11.8246 | -44.9669 | 2025-10-01 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 82a099f8-ba09-36c7-8612-9091d91c7a35 | -10.0892 | -50.3222 | 2025-10-01 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 0d563db0-de89-3545-9d6e-0cf9bcb0e903 | -11.4049 | -44.8895 | 2025-10-01 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 152235f0-0980-31d9-9bf6-6cf5a8b08e58 | -13.7881 | -47.9629 | 2025-10-01 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a54d88ba-6184-329d-989f-1300e64c435b | -3.0827 | -47.0088 | 2025-10-01 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 45dd3e1f-e340-3bfa-ac0f-2e2f008dc8f6 | -9.9193 | -43.6508 | 2025-10-01 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 8c43dfa7-6a5b-3a65-a46e-797c4d9c552c | -11.8242 | -44.9901 | 2025-10-01 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 5f33c52b-5795-3a93-99fd-183a58bf2899 | -8.559 | -44.7184 | 2025-10-01 00:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9efd01d1-a82d-3a65-b221-3d95160185dd | -9.9383 | -43.6483 | 2025-10-01 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| 16cb0c47-4bd3-3f35-935c-2f0daf806036 | -9.4396 | -54.5537 | 2025-10-01 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f0258657-0442-37ae-aa28-ff1a908a516a | -3.1012 | -47.0301 | 2025-10-01 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 450faa5d-bb7a-3d1a-8985-d34b49d29243 | -20.611 | -46.1858 | 2025-10-01 00:20:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 103.2 |
| e0643e1e-73ad-3db1-86dd-613ad309c623 | -3.1013 | -47.0082 | 2025-10-01 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 5b65852f-d1bd-3780-90d2-cd3517f06ecd | -11.478 | -45.0868 | 2025-10-01 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 152a8a53-a40a-32e4-a069-a9de1c3fd8cf | -20.6316 | -46.1806 | 2025-10-01 00:20:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5504ff58-c6b9-31b6-925c-d6d977256529 | -6.949 | -63.1048 | 2025-10-01 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 697ce667-35b5-3fb5-9073-cd9a9ed5a607 | -22.2844 | -46.709 | 2025-10-01 00:20:00 | GOES-19 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.2 |
| 3323bd6a-e1d5-347e-bac5-4be7d2ead7d4 | -21.0572 | -45.6638 | 2025-10-01 00:20:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 5544e33e-4d48-328a-8c74-411f1ff67c31 | -5.1591 | -42.7717 | 2025-10-01 00:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 060596cd-bde1-394b-8f44-3d2c0c7fc249 | -9.4394 | -54.5739 | 2025-10-01 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b9d70363-2f5e-3ba9-aaf1-26a52afc8539 | -9.9186 | -43.6978 | 2025-10-01 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a43102af-258f-39f8-8569-d1001d1d2b61 | -10.1081 | -50.3203 | 2025-10-01 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a6fe59c1-5ff5-31fa-a181-4f510b877ca5 | -13.7691 | -47.9435 | 2025-10-01 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 154.8 |
| e261c795-df00-33c6-aa44-f17f8991c403 | -9.0821 | -48.0252 | 2025-10-01 00:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| f1636d8b-8d72-36c7-92da-6e29c570ac50 | -3.0827 | -47.0088 | 2025-10-01 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 9980f45e-d88e-3e26-b8e7-eb0aa0b6e644 | -9.2902 | -54.5242 | 2025-10-01 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 55a272da-1631-3f73-b105-036507e322f7 | -8.5587 | -44.7414 | 2025-10-01 00:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9a2d06e2-c1a4-3242-b9d3-3fd9ef45ca7b | -11.8434 | -44.9872 | 2025-10-01 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 189.2 |
| dc291aae-39e4-36c3-a062-547e5f166228 | -21.0572 | -45.6638 | 2025-10-01 00:30:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 7a335214-de01-3f12-9ff8-fd9a7b98a235 | -12.8756 | -45.2671 | 2025-10-01 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 72654362-9b49-3ba7-ad37-43f07eb7c298 | -10.1084 | -50.299 | 2025-10-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 16f71a56-b669-33c8-a035-ffb853570397 | -20.6103 | -46.2098 | 2025-10-01 00:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e04e1413-6660-3fbc-b7e5-21093d811e47 | -13.3274 | -47.8536 | 2025-10-01 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 61143dd1-1ff4-352a-836a-8938622624c3 | -10.0337 | -50.2424 | 2025-10-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 76b9bc79-3a06-3af0-a670-01b667583686 | -3.1012 | -47.0301 | 2025-10-01 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 7ae30fce-f5fb-3de4-a4e4-cbfc55df4bf1 | -21.0564 | -45.6881 | 2025-10-01 00:30:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e8ef9b2f-a75f-36f6-b667-c5b885539933 | -11.3858 | -44.8923 | 2025-10-01 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e809dc54-0040-3b9f-8a15-f0c73b91efc7 | -11.1523 | -54.3104 | 2025-10-01 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 6f7386f5-c8da-3344-9c2a-0ae80b78a8d4 | -8.559 | -44.7184 | 2025-10-01 00:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 970c2912-cf64-3f39-87b7-a61183d99d7c | -14.7137 | -48.1525 | 2025-10-01 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 74db881f-0543-31c0-867f-61d535e8b082 | -3.4762 | -50.0883 | 2025-10-01 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 7cd2da42-4af5-395f-880f-b8207c0b90c6 | -15.9431 | -48.1245 | 2025-10-01 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 7c0f6fd4-f837-3063-9844-4f4e74f5b033 | -9.3089 | -54.5229 | 2025-10-01 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| b5551d2a-fa4c-3317-9dac-aa59bf070c51 | -9.9376 | -43.6953 | 2025-10-01 00:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |


[Clique aqui para ver as próximas entradas](README3.md)

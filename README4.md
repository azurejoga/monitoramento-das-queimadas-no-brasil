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
| 154d617a-10b0-350b-b17f-2600f2c6b6bf | -6.13112 | -43.95277 | 2024-12-19 01:02:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 4eba381e-1e01-33d7-95e6-0a6b2d4bce8d | -4.89303 | -41.41948 | 2024-12-19 01:02:00 | TERRA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 9cbf8783-3457-344f-b8bf-de429693ea16 | -3.23032 | -46.807 | 2024-12-19 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 2f40dd56-f5f8-3d36-a0f5-5a5f001a3a8b | -2.84439 | -49.50164 | 2024-12-19 01:04:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 784a37ad-fe54-3dab-b8ea-3f7efa27e7e5 | -1.87349 | -46.34128 | 2024-12-19 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9079a577-e4ee-38a8-92c2-c3cf2f807a60 | -1.75611 | -45.82647 | 2024-12-19 01:04:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 0a05a2ae-4866-331d-8966-22f9843d649f | -2.06975 | -52.05919 | 2024-12-19 01:04:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c94b4bf6-4942-335d-bd7f-e8006b98c23b | -1.86563 | -46.33095 | 2024-12-19 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8f4fa162-e911-36eb-afb5-4fca181f64d1 | -1.88832 | -52.07905 | 2024-12-19 01:04:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f86a76c-ef6f-3e05-88c2-d00df16b876e | -1.72448 | -52.56316 | 2024-12-19 01:04:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 916870b8-8871-3626-b4ba-18377ae99546 | -1.72324 | -52.55423 | 2024-12-19 01:04:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 405fecad-08fe-33d8-af3e-6182f21d0335 | -1.26418 | -54.15802 | 2024-12-19 01:04:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a20ee2bc-0344-3db4-b30a-d070ebc964f8 | -2.05966 | -52.05162 | 2024-12-19 01:04:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 974692d6-ce6d-340f-ab18-4f42d64af812 | -2.84579 | -49.5116 | 2024-12-19 01:04:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 206a40a5-0d1e-3df5-a6ca-286f1aea561b | -1.27086 | -54.137 | 2024-12-19 01:04:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0e9a7608-8567-33ff-8f34-02e5c4a77b55 | -19.065901 | -52.887501 | 2024-12-19 01:05:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 56de783a-3752-3387-816b-cf05a682c7eb | -4.3543 | -48.476501 | 2024-12-19 01:05:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0af31be2-ebf9-3217-8a90-158dc803f9ad | -13.4886 | -52.9459 | 2024-12-19 01:05:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24e0d5e6-04f9-33bf-8ac9-5d8ef521e891 | -13.9002 | -54.614101 | 2024-12-19 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2660e01b-7ef6-38e2-9678-4811dbcc13f5 | -3.2256 | -46.8144 | 2024-12-19 01:05:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9951e2-3d87-3878-9fdb-8ff34ca5cf7d | -13.9296 | -54.607498 | 2024-12-19 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| efbc8fb7-fd9b-3634-8d52-bf7af2c87752 | -20.7826 | -49.8484 | 2024-12-19 01:05:00 | METOP-C | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cef32420-e1ed-372b-bf8d-67b0bcef85b9 | -13.8986 | -54.606602 | 2024-12-19 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59464525-d5c8-3a1b-9d31-b64453e8a186 | -13.9312 | -54.614899 | 2024-12-19 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1494e1be-27d8-344d-b5bd-d5bcf00c0ec8 | -12.2391 | -54.311298 | 2024-12-19 01:05:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 498c332b-930f-3d78-ba57-b08107c3772f | -13.3103 | -52.4333 | 2024-12-19 01:05:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca0af465-5504-39a7-a935-35b671f8840c | -3.2406 | -46.791599 | 2024-12-19 01:05:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6979b69-fb84-3c35-a81b-563a054b1a0f | -12.2375 | -54.3041 | 2024-12-19 01:05:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87a97740-9e11-34b9-95dc-774cbd8fe66a | -20.478399 | -55.8339 | 2024-12-19 01:05:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b2c56e98-a431-373c-87f3-af1907868c57 | -3.2169 | -46.778 | 2024-12-19 01:05:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6dbf56ff-e4d0-33c0-ba4e-e5471c9ca5ea | -13.928 | -54.599998 | 2024-12-19 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c0cec79-b673-3e18-ac01-5bb491dc6e15 | -22.548599 | -48.363201 | 2024-12-19 01:05:00 | METOP-C | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 44f220cc-034d-3cef-81ea-d8efd5ed9e42 | -3.6871 | -49.5625 | 2024-12-19 01:05:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8670c8c9-362f-3eb4-a78e-11baa61cd5e7 | -3.2309 | -46.7939 | 2024-12-19 01:05:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 445cf516-211d-3bf1-af53-6744d8196e1e | -20.784401 | -49.8559 | 2024-12-19 01:05:00 | METOP-C | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e9736e7-e62f-3698-8227-37460d7a4ef1 | -17.9792 | -54.002602 | 2024-12-19 01:05:00 | METOP-C | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3421e916-b7e6-3199-a8e3-402a9913a869 | -3.2353 | -46.812099 | 2024-12-19 01:05:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2a20006-6a5c-3228-b735-b37c866bd113 | -19.064301 | -52.8801 | 2024-12-19 01:05:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fc252490-e557-3b9f-b832-6a5604acff07 | -4.4804 | -45.404701 | 2024-12-19 01:05:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8e5f30b-efc5-3c70-9694-ae6a336ff08f | -12.2277 | -54.306301 | 2024-12-19 01:05:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2bffec1-513d-3867-ba72-a745b53d898a | -3.2266 | -46.7757 | 2024-12-19 01:05:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 773612c9-df11-363a-a0de-7f00d6cc5155 | -13.4902 | -52.9529 | 2024-12-19 01:05:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f2a45969-d3c6-39f5-9caa-3d57ad6330e6 | -13.3119 | -52.4403 | 2024-12-19 01:05:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7af4ee6b-d7f2-3446-89d4-bf0c76d66cc3 | -17.977501 | -53.994801 | 2024-12-19 01:05:00 | METOP-C | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c3d2e30d-e322-376d-9dff-36475420c457 | -22.2094 | -53.147202 | 2024-12-19 01:05:00 | METOP-C | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88c2dffd-f25d-35bc-a8cc-7dc5bc3246b9 | -12.2293 | -54.313499 | 2024-12-19 01:05:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0af1b1d-546e-3cff-b6a5-91fa8c48f96f | -4.3316 | -48.295898 | 2024-12-19 01:05:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5de0f38a-3fac-3952-aa1a-3f2d65a538c6 | -3.6898 | -49.5741 | 2024-12-19 01:05:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa08ac88-92c5-31f5-a64d-bed9f648705f | -19.124399 | -53.450199 | 2024-12-19 01:05:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e24dfc67-fad3-360c-812b-839ad4f2d963 | -18.7453 | -56.5536 | 2024-12-19 01:05:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e9d5a394-dcc3-3b51-9835-0490450c743d | -3.245 | -46.809799 | 2024-12-19 01:05:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acced351-0727-3243-84d9-83acf8cbb131 | -19.067499 | -52.894901 | 2024-12-19 01:05:00 | METOP-C | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 00a69745-709c-3f25-bce3-3164ce732a2c | -20.480301 | -55.843899 | 2024-12-19 01:05:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| da388a46-cded-3bb5-b3a4-8275327af877 | -3.2213 | -46.7962 | 2024-12-19 01:05:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2be76a09-a17d-3684-87e9-b22d8c490a60 | -4.4761 | -45.4286 | 2024-12-19 01:05:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ffb1288-05f5-39d6-bfee-9fb44ae7af4f | -4.0442 | -49.765999 | 2024-12-19 01:05:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 376c6db9-4416-33ab-8729-7e8017d3fe1e | -19.125999 | -53.457802 | 2024-12-19 01:05:00 | METOP-C | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 11d5f4d4-66a6-3400-9f71-daee9f70f2e6 | -4.4858 | -45.426201 | 2024-12-19 01:05:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5452b8-2d34-384e-8362-4682a8b5317e | -3.2363 | -46.773399 | 2024-12-19 01:05:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d44593cd-b385-3e76-b28e-928cf8179d1b | -4.4853 | -45.4353 | 2024-12-19 01:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b72c4a83-ae1c-393e-93c1-c889ee1ebcb1 | -3.2136 | -46.7843 | 2024-12-19 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ed28e672-d044-3d96-905c-843254115fee | -3.2135 | -46.8063 | 2024-12-19 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 303749be-5ac6-39c2-be84-d71d85bda01c | -4.8893 | -41.3867 | 2024-12-19 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| c7135003-3b32-358b-a5eb-748aa3aa9728 | -4.4854 | -45.4128 | 2024-12-19 01:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 76150e71-522e-349f-acda-0fb1ab24c3da | -3.232 | -46.8056 | 2024-12-19 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| fd5de02f-a075-3042-a427-684d049542e9 | -3.2321 | -46.7836 | 2024-12-19 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| c5e28ea9-6f8e-3178-bb98-818fb9fe9933 | -4.8891 | -41.4108 | 2024-12-19 01:10:00 | GOES-16 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 108.8 |
| c816281b-ffb2-3a58-9358-820362e7eb81 | -4.4854 | -45.4128 | 2024-12-19 01:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4f58687d-9ac9-3809-be76-f172647caec6 | -6.1229 | -43.9578 | 2024-12-19 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ed0ea3da-4f3e-3096-97cc-7d485fb8aa69 | -4.8893 | -41.3867 | 2024-12-19 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| f507b466-5392-365a-8294-5733face2a29 | -4.8891 | -41.4108 | 2024-12-19 01:20:00 | GOES-16 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 93c7736d-4019-3d16-87f7-44e5b306703d | -7.9926 | -35.1333 | 2024-12-19 01:20:00 | GOES-16 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 46.6 |
| dbbfcdf1-70d3-30f9-a6aa-21810c16cdb6 | -3.2321 | -46.7836 | 2024-12-19 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 215.6 |
| 27c7a3aa-c0bf-34c8-9a43-20f84585c8c6 | -7.7062 | -35.0926 | 2024-12-19 01:20:00 | GOES-16 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| c5c0e3b1-1a6c-3679-8d4d-cc7c10c8bdef | -3.232 | -46.8056 | 2024-12-19 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 38656287-59d4-36ee-9320-d0276cf09330 | -3.2136 | -46.7843 | 2024-12-19 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| 265c85a6-d4af-310b-97bf-fd436550df89 | -3.2135 | -46.8063 | 2024-12-19 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 31455d1f-9d0b-3458-a22a-753f32a86f7d | -8.0122 | -35.1029 | 2024-12-19 01:20:00 | GOES-16 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| 67612ffa-34fa-3d32-9a50-b247c89d6ab4 | -8.0118 | -35.1305 | 2024-12-19 01:20:00 | GOES-16 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| 2fb60efd-6908-3928-806e-edf1b9ce20fb | -4.8891 | -41.4108 | 2024-12-19 01:30:00 | GOES-16 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 133.8 |
| eae77227-a3c6-3740-9a09-9e45259fdf29 | -3.2507 | -46.7829 | 2024-12-19 01:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 8d68ce73-f0d5-342a-a858-44b58d29c70c | -3.2321 | -46.7836 | 2024-12-19 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 189.1 |
| f27f8084-ef8e-36ea-b7be-3a3ebb99d03b | -3.232 | -46.8056 | 2024-12-19 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 181.0 |
| 6a6352b1-a0bb-3cf3-bdb9-7f3ac7903051 | -3.2136 | -46.7843 | 2024-12-19 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 000016a6-b609-36f7-9f4e-747db298d298 | -4.8893 | -41.3867 | 2024-12-19 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 120.4 |
| a68710b9-04a6-3a65-b08f-872bdcff8176 | -3.2135 | -46.8063 | 2024-12-19 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 0dd31cf8-da4f-3e86-87c0-e04c18d101b5 | -3.2321 | -46.7836 | 2024-12-19 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| a7c7c23f-757a-3573-9a8c-c361e8d38db5 | -3.2136 | -46.7843 | 2024-12-19 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| fc942f86-8eeb-322a-b974-0eb4dc7cc44f | -3.2135 | -46.8063 | 2024-12-19 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 8fb0fe48-4db6-32fc-b258-190f76618111 | -3.232 | -46.8056 | 2024-12-19 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| b4bd6917-b988-35d0-a70c-2aab1d6e82fc | -4.8891 | -41.4108 | 2024-12-19 01:40:00 | GOES-16 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| a0f243ed-311c-3700-88b8-47f608a57323 | -4.8893 | -41.3867 | 2024-12-19 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 012f9549-399a-38f2-9c63-0125f4f05a1b | -4.8893 | -41.3867 | 2024-12-19 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| c56e6d8b-2724-3acd-8a87-cb7c330f2f71 | -4.7766 | -46.4022 | 2024-12-19 02:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.0 |
| aaa000b8-701f-39dc-9dac-2df80be25d11 | -9.66025 | -36.10662 | 2024-12-19 02:49:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4288c564-bd27-35ab-9ddf-bfb4115f605c | -6.475 | -35.26353 | 2024-12-19 02:49:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 912885e8-651e-316a-9ffc-88b5b840ffc3 | -9.65903 | -36.1126 | 2024-12-19 02:49:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 47c7e77e-b9e9-3df4-99ab-e74319d22309 | -6.9832 | -35.07489 | 2024-12-19 02:49:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b4355d7a-7697-3e41-a59a-bcca5f9ebea4 | -9.66573 | -36.11386 | 2024-12-19 02:49:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 437d62c9-c28f-3a0d-8a28-7faeb4d35b42 | -7.68739 | -35.25097 | 2024-12-19 02:49:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README5.md)

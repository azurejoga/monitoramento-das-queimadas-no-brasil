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
| c0efa1df-9bac-38bf-af3a-4b929f7f7d99 | -17.9275 | -57.2034 | 2024-10-25 01:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 4b39e8ef-43dd-3364-8867-f38575a88bf0 | -17.9473 | -57.2009 | 2024-10-25 01:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 337e4e4d-1adc-32dd-ad45-7408f081887e | -18.0254 | -57.253 | 2024-10-25 01:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 6e056c70-7526-345b-bfbc-941b932018b1 | -18.0434 | -57.3539 | 2024-10-25 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.2 |
| 4fdcbd69-eb3a-34bd-98e5-ead1f19721ae | -18.0438 | -57.3332 | 2024-10-25 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| c4792d15-1f99-3f3c-a5e3-f1e13e03cefd | -18.0441 | -57.3126 | 2024-10-25 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| a2e6ea26-9e07-3063-b79b-25325d91959b | -18.0639 | -57.3101 | 2024-10-25 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 944eccf7-a5d3-3afd-986b-0568d31555b5 | -18.0844 | -57.2663 | 2024-10-25 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.2 |
| a5891310-6fe1-36f8-af00-f88e66296f9b | -18.0847 | -57.2456 | 2024-10-25 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 78aecf50-f7b8-325b-a59b-a2138a14c7cb | -18.1042 | -57.2638 | 2024-10-25 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.0 |
| e8132118-c238-3e30-8e05-8822e0804ba0 | -18.3199 | -56.2404 | 2024-10-25 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.3 |
| b52beb6a-6383-364d-ab75-faf78219d4e1 | -18.3203 | -56.2195 | 2024-10-25 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 53a72a38-4b9d-3a50-81f9-c646fb96870c | -18.3398 | -56.2377 | 2024-10-25 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 2b252732-9781-3374-89b0-7629f6aa8269 | -19.5681 | -56.6114 | 2024-10-25 01:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| e90555c7-7e80-3083-9ee9-71ffe09c63c0 | -19.5685 | -56.5904 | 2024-10-25 01:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 3dacff98-376a-37e0-945a-9502d3ba6bee | -19.5882 | -56.6086 | 2024-10-25 01:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.4 |
| cc0d639f-c01a-36b4-a50c-aeaabce70615 | -19.5886 | -56.5876 | 2024-10-25 01:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 17156334-e00e-322f-838d-66f18ffd3fb0 | -18.34629 | -56.20131 | 2024-10-25 02:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| baccbb7a-fabf-34b7-b990-21f2c9c68a8b | -16.55669 | -56.24238 | 2024-10-25 02:04:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| a55bfda8-d2b1-3f92-9324-51ff8d6fae12 | -17.0201 | -56.01746 | 2024-10-25 02:04:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 2c9bae31-96cc-3e15-8ba1-636cee5630eb | -17.01559 | -55.99276 | 2024-10-25 02:04:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 1279ab99-3c2b-32f1-88b3-31815922a35f | -17.01065 | -56.0003 | 2024-10-25 02:04:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 471de973-44e2-3971-a9c3-4db31b6a61df | -16.5647 | -56.24625 | 2024-10-25 02:04:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 0628a9b2-1d7b-38f9-addc-d3a758995341 | -18.33779 | -56.20959 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.4 |
| 5fd26765-ade2-3cee-886c-4d8aea47dd64 | -18.3285 | -56.23489 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| a15effe8-68d4-3bc4-aa7f-c0031d13b2d4 | -18.08468 | -57.25016 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| d4da1574-824c-3ff4-93ec-184e384ff4c2 | -18.05536 | -57.32025 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.4 |
| b2ed081f-d931-3e1e-b400-573b9b23c90d | -18.05213 | -57.30134 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.4 |
| a7529141-e4cb-3d0f-ae3a-ce9b808231c1 | -18.04554 | -57.31665 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 39ab9931-558c-3719-b96d-fea80544f447 | -18.04309 | -57.32266 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 01648004-2ff3-3cad-b954-bbeadacd8204 | -18.04051 | -57.38138 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 6dd3da84-60e5-36c4-8bd1-92c5194a7227 | -18.03985 | -57.30376 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 1753ac6a-e663-386b-bdd0-db2c087ac7e6 | -18.03729 | -57.36269 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.5 |
| af1c90e7-0c67-3cf4-8637-ae572714966b | -18.03407 | -57.34393 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| b99b30cc-7f20-374c-8c27-d525b63ec355 | -18.03082 | -57.32508 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| ba27077f-e5e9-354e-9e83-d9661d767a29 | -17.94574 | -57.20361 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 872d402a-2542-339d-b256-f2ff1cc6998a | -17.94426 | -57.21033 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| f6050812-38e9-3443-8470-fb24753df239 | -17.94095 | -57.19095 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.4 |
| c712fd4a-596c-3f5f-89e1-7d4f644ebe6c | -17.93334 | -57.20603 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 989cacdd-0902-30e4-ac9c-7baad2494414 | -17.93186 | -57.21276 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.4 |
| cfcb966d-dbbb-3a54-9c40-2a5f036c9dde | -17.92853 | -57.1934 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 7eaa3e66-d905-3783-a7d8-a62208ed3427 | -17.9149 | -57.5517 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| f9e10b6f-322a-3e65-b519-5ff15743aa52 | -17.91041 | -57.23693 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 93457ac5-ca56-3877-8caa-e374c7b907f1 | -17.90236 | -57.55147 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 54035c38-61ad-3784-b9e1-181217fdad56 | -17.84667 | -57.54637 | 2024-10-25 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 912d47fb-d40a-36be-b11b-6ecb99449366 | -17.81592 | -57.51395 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 43ff6dd7-46d7-3de8-bd69-aee9ab85e648 | -17.81249 | -57.52119 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| df055d87-d13d-33b8-b81e-1c560c7956c2 | -17.80035 | -57.52356 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| efd17368-57f7-30fb-b265-ac01de1a13a4 | -17.75498 | -57.55135 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 87c9ca04-dd33-3967-8493-f3934a0e515b | -17.74925 | -57.59025 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| efb9f313-f035-33bd-bd68-b27e88c26e23 | -17.73716 | -57.59257 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 819caec8-354e-3dcb-ba2d-907df5b45677 | -17.70157 | -57.33525 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| cf825b86-bca8-3e16-b1e4-b9664f153ef6 | -17.69446 | -57.35072 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.7 |
| 130bd9b5-c059-3526-9356-68b8661ff94b | -17.69247 | -57.35675 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 953e4348-67d6-3d1d-b2c3-035edf497e03 | -17.69108 | -57.33167 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 5ffd2d27-cb38-33c8-b654-b6c12c1ddbc2 | -17.68923 | -57.33767 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 740798c0-18ac-35c4-a616-bef4c2dfc57c | -17.67501 | -57.47696 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| b6d640ee-5e45-3c83-8b3d-833d73d98425 | -17.24741 | -57.50642 | 2024-10-25 02:04:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.4 |
| c436e96d-f718-397a-ae53-301c320aaa5d | -17.237 | -57.22904 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 10e6705b-ff2a-3e06-87c1-f7f807d0aef1 | -17.23269 | -57.51583 | 2024-10-25 02:04:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 19f6a0ae-7bd9-3494-88aa-c4fa8e25f34b | -17.22793 | -57.25123 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 94c57cb6-e088-3712-97e5-5ca95826aa02 | -17.22395 | -57.2381 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| a1dd2c4e-a464-3f55-b383-3881794ecafc | -17.22444 | -57.23148 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| b8eb74b8-8d02-3f41-9b50-c8e0b21b1e31 | -17.21716 | -57.49932 | 2024-10-25 02:04:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| 316edb0e-3b3c-3fca-b4f4-30a7d6ff8a71 | -17.08764 | -57.43145 | 2024-10-25 02:04:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| c1ea3bc9-b4d1-3a84-92be-3d2548070d02 | -17.06959 | -57.47448 | 2024-10-25 02:04:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| d32f9105-f950-3b79-b6e0-a4e64f4cf460 | -17.01831 | -57.49081 | 2024-10-25 02:04:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 6a5a23bc-6c48-3bef-9acf-c46ac59cab4f | -16.99485 | -57.35558 | 2024-10-25 02:04:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.3 |
| b710f53c-e5e7-3d44-b2b5-f71e0b625988 | -16.97359 | -57.54446 | 2024-10-25 02:04:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 4d578532-ab64-3d4a-89ae-5d8615ddfcdc | -15.03587 | -59.70721 | 2024-10-25 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 421a144f-c2c2-3897-90ef-ec159385b9e1 | -15.03374 | -59.71399 | 2024-10-25 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4c3ccb2e-634f-300c-9d83-a4f30c81c34f | -15.03151 | -59.69983 | 2024-10-25 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8d3ee451-a3fe-3c22-a96d-14ef354fa7d6 | -15.93297 | -59.56749 | 2024-10-25 02:04:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 212dd8fd-8be2-3cde-86e8-f089ec59d67f | -15.68957 | -59.75097 | 2024-10-25 02:04:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 95b4dba3-8fff-3474-b2e7-0f99ce09238b | -15.68732 | -59.73725 | 2024-10-25 02:04:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d8757cde-76bc-313b-9ad4-3ef6d9e4d885 | -15.68415 | -59.74356 | 2024-10-25 02:04:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 47c5e013-a36b-312f-a1cb-12ee8d4f3d57 | -15.67345 | -59.74544 | 2024-10-25 02:04:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 29a4a085-4da0-3ac4-a130-e49d8d6d9887 | -15.66494 | -59.76105 | 2024-10-25 02:04:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ee88372f-4319-37bb-bcb3-41048daf73de | -12.97382 | -62.74535 | 2024-10-25 02:04:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 357f8fbf-7c40-3839-9e06-f7463e352e32 | -12.72828 | -63.02335 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7e9b00e6-fbfd-3991-9d0e-f8551c3720da | -9.43521 | -67.14837 | 2024-10-25 02:04:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eb45c855-c9c8-3082-9f95-032c07c9bebe | -12.5392 | -63.05492 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 511db59f-6371-306a-b04f-ae14447c9c9b | -12.53147 | -63.06605 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 78c4a590-be7f-39e8-97a0-a56cc8ab3331 | -12.53004 | -63.05634 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 29.2 |
| cdee0889-9c46-33b7-8e87-a369fb5bfdad | -12.52088 | -63.05776 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 6760d97d-b4e0-37a7-9073-f319843b25a2 | -12.47323 | -63.17003 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 51ae4a65-b52a-38e4-8f5e-0575d22485ac | -12.47183 | -63.16039 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.7 |
| dc8443ff-517c-3cb5-8604-4eccd8ae0141 | -12.46551 | -63.18107 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a8b1f06b-ae2f-3fd9-8fc5-6b2aa49af5f0 | -12.46482 | -63.24011 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ccf61624-85ad-313a-8c76-353973f03ae4 | -12.46411 | -63.17144 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 23d3b3e8-e651-378c-8ff2-784aa8015326 | -12.4627 | -63.1618 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 24.1 |
| aa539e2a-1d1e-3fab-86b9-dcb5692fbd9f | -12.45921 | -63.20172 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a0dc9470-f139-35b0-beca-745dffa48420 | -12.4578 | -63.1921 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cec397b3-b3cf-30a3-878b-43cc871242e2 | -12.45639 | -63.18248 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 927938b1-2c25-3b5f-9432-a7df321236c6 | -12.45498 | -63.17286 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 67cc0fab-05d0-3ebd-93a0-187ac685d2c4 | -12.39217 | -63.88621 | 2024-10-25 02:04:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 65f8c843-ce70-3898-bd78-bd545d222f57 | -12.39085 | -63.87701 | 2024-10-25 02:04:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 670daa83-099d-3e00-bc06-b0ba17882472 | -12.38521 | -62.94105 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fcf6e3e5-dd00-382d-ab86-6f9144c6e0d4 | -12.38324 | -63.88758 | 2024-10-25 02:04:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 29.4 |
| f2692677-1b0d-3053-94ed-d1e89bba738d | -12.38192 | -63.87837 | 2024-10-25 02:04:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |


[Clique aqui para ver as próximas entradas](README16.md)

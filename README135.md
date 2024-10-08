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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f47ec052-2dd7-3624-bbc8-a2de3bc60b06 | -16.673 | -57.1077 | 2024-10-08 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 8e30f081-cc89-3632-8921-3ddd451abc5d | -16.8048 | -57.4197 | 2024-10-08 10:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |
| ce7cdfb8-dca8-31a6-ad5b-c6838fae2cfe | -16.571 | -46.4553 | 2024-10-08 10:26:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 251d3cf5-394f-3610-bb07-3c655e70c039 | -16.673 | -57.1077 | 2024-10-08 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.0 |
| 6e1a7232-3a9d-3dad-85d0-5868d71182ea | -16.6726 | -57.1283 | 2024-10-08 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.7 |
| 7c5e7fb0-0e50-36d9-a43e-ccc669f5de26 | -16.8048 | -57.4197 | 2024-10-08 10:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 37aa9a11-2c6a-3d73-b151-c91fbfd859b1 | -17.0992 | -57.3651 | 2024-10-08 10:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 5aa86a04-06d1-39d8-9032-1ef3cc56b344 | -16.5715 | -46.4321 | 2024-10-08 10:36:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 3d703e49-9ad0-3e1f-9177-4739de11640a | -16.571 | -46.4553 | 2024-10-08 10:36:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 05d1cd47-cdca-31c9-86d8-c2963a61493f | -16.6726 | -57.1283 | 2024-10-08 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.6 |
| 29bd3bce-10e7-3a04-984f-6f6b7affc0f2 | -16.6531 | -57.1305 | 2024-10-08 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| c6359193-1f34-34de-b270-3b6f2dc0eea7 | -16.673 | -57.1077 | 2024-10-08 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| e091bfb4-b2a9-3aa8-940f-4f8a0a88478a | -16.8048 | -57.4197 | 2024-10-08 10:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| fda00aae-f647-3dc8-a509-1247ba0afe91 | -17.0992 | -57.3651 | 2024-10-08 10:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| cf3bfaf4-1901-3f98-b0f9-42c81dde0da8 | -16.4184 | -55.9455 | 2024-10-08 10:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.9 |
| a6895f79-0ae9-3ab7-802a-c50ef25c060d | -16.571 | -46.4553 | 2024-10-08 10:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 134.7 |
| e4fde225-6702-388b-a791-516c840e9e03 | -16.5715 | -46.4321 | 2024-10-08 10:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 1ff5b65a-020d-33ae-82bb-328f9c66d7e4 | -16.5902 | -46.4746 | 2024-10-08 10:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e9d33437-0629-3020-b5ae-e35d538863b5 | -16.6531 | -57.1305 | 2024-10-08 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 1048acb9-1d13-3966-a7eb-d39964b674fa | -16.6726 | -57.1283 | 2024-10-08 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.4 |
| bef13f8c-2e92-31aa-86bf-0cf6b7dd1efc | -16.673 | -57.1077 | 2024-10-08 10:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.7 |
| deeb0809-f700-3f4e-b3f8-b497d2a447e5 | -16.8048 | -57.4197 | 2024-10-08 10:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 3cc3066e-fbd4-3175-9a20-1fd012d3877f | -17.0992 | -57.3651 | 2024-10-08 10:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| b1d0dfd0-8f05-3965-b162-1d77b04c9c18 | -20.6609 | -45.8864 | 2024-10-08 10:47:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 49746c1f-3acb-304c-887c-e3ec09bdf593 | -20.6602 | -45.9105 | 2024-10-08 10:47:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 220.6 |
| efecfa60-2fff-3965-ab2b-ee4379f92566 | -16.5704 | -46.4785 | 2024-10-08 10:56:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 79972722-fd96-364f-8155-1cc01105d069 | -16.571 | -46.4553 | 2024-10-08 10:56:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 9d80b869-2f61-351a-a705-8e98a8160f8d | -16.5715 | -46.4321 | 2024-10-08 10:56:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 7c12851c-87ed-38be-8525-60b564588ad4 | -16.5902 | -46.4746 | 2024-10-08 10:56:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 8c679d69-0eab-37f7-90ec-e7503fb1e00e | -16.4184 | -55.9455 | 2024-10-08 10:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 126.0 |
| ecb41d97-9ee8-32df-bae5-6f75b32cf128 | -16.4379 | -55.9431 | 2024-10-08 10:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 181.2 |
| 65a8c508-3508-3aa3-85e4-b3db84a96f97 | -16.6726 | -57.1283 | 2024-10-08 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 2d38ab91-2587-3166-b24f-a8fe035cd18e | -16.673 | -57.1077 | 2024-10-08 10:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| c2321102-1057-3009-b447-f4b6c754448b | -16.8048 | -57.4197 | 2024-10-08 10:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 537c964e-6916-3843-b57e-555c48a253a5 | -17.0992 | -57.3651 | 2024-10-08 10:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.3 |
| 57998d1d-75cf-3e89-95db-f33603309036 | -13.8744 | -44.6329 | 2024-10-08 11:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 44e9f725-7fad-3990-bff4-d347bff807b6 | -16.4184 | -55.9455 | 2024-10-08 11:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 130.4 |
| 043a3b33-4c82-3a51-b36c-1e18fca5a285 | -16.571 | -46.4553 | 2024-10-08 11:06:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 8ee45507-5c56-38ad-873e-e642b842d274 | -16.673 | -57.1077 | 2024-10-08 11:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.1 |
| d8129abd-91a5-3a4c-8cb6-8b0835c5d634 | -16.6726 | -57.1283 | 2024-10-08 11:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 970d1f7f-6f14-3862-b546-282c4c0119bd | -16.8048 | -57.4197 | 2024-10-08 11:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| f1bb7fbf-dab7-3a43-94d8-dcbfbcb8fdcf | -17.0992 | -57.3651 | 2024-10-08 11:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 77899e7c-c197-3798-aa07-702d5a8d31e2 | -20.3519 | -48.8417 | 2024-10-08 11:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 78212d6f-087d-3adc-b827-6a43dfa314cc | -20.3513 | -48.8648 | 2024-10-08 11:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 5a4379dc-b214-36dc-84f4-50539ee2c5d3 | -16.4184 | -55.9455 | 2024-10-08 11:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 187.9 |
| 1a91635c-60b9-3d07-92ff-1ebcbd908361 | -16.5512 | -46.4592 | 2024-10-08 11:16:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1db707b6-3778-3934-978f-f2c3e77e73ed | -16.571 | -46.4553 | 2024-10-08 11:16:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 5c22ac15-1657-3391-8cf1-7b6dfb0bd14b | -16.6726 | -57.1283 | 2024-10-08 11:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.9 |
| d5b66057-c279-32b1-862a-1250d6c159ac | -16.673 | -57.1077 | 2024-10-08 11:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.4 |
| 3a9ee814-030a-3602-98a2-1ac69bd32b57 | -16.6922 | -57.126 | 2024-10-08 11:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| eabcbe9b-8e65-3a88-973a-58630efc7499 | -16.8048 | -57.4197 | 2024-10-08 11:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| f52bd724-e01c-3a11-ad7e-ac23cb399eea | -17.0992 | -57.3651 | 2024-10-08 11:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.9 |
| c2a34045-27d3-3e5b-8977-723a467647c6 | -17.6692 | -53.0174 | 2024-10-08 11:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 63b47087-1117-330d-88af-98993602304a | -20.3724 | -48.8372 | 2024-10-08 11:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 0335caf0-7339-3576-81ec-600c245004a8 | -14.7186 | -45.1588 | 2024-10-08 11:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 35e246bf-9503-3308-9ea3-8e10b5ad29c1 | -16.5902 | -46.4746 | 2024-10-08 11:26:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 177.0 |
| fab0558d-8046-3644-8d8f-3c59c4e895e2 | -16.571 | -46.4553 | 2024-10-08 11:26:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 395.6 |
| b33e016b-cf79-3da7-bab4-5c9c85884bea | -16.4184 | -55.9455 | 2024-10-08 11:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.8 |
| 522b9793-9c72-3834-ab55-6e12c7cbca81 | -16.6922 | -57.126 | 2024-10-08 11:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 1b0307ac-6151-3649-a511-a7f37df7f60a | -16.6531 | -57.1305 | 2024-10-08 11:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| e5a2b206-49a8-30a0-8bb1-5b5769ae33e0 | -16.6726 | -57.1283 | 2024-10-08 11:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.7 |
| b0caa82e-60a8-3b2a-9ea1-c9fbbe038b00 | -16.6534 | -57.11 | 2024-10-08 11:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| c4e9e059-fcb7-34c1-a119-747e30b419a9 | -16.673 | -57.1077 | 2024-10-08 11:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.5 |
| 643e782d-744d-3646-a1ac-96bf9ed9fb59 | -16.8048 | -57.4197 | 2024-10-08 11:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.9 |
| a96423d1-eaa9-3221-8303-c7cefc8e6ee9 | -17.0992 | -57.3651 | 2024-10-08 11:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 575f3730-283b-3802-bb1b-3bbddc74e4a9 | -18.6195 | -57.2396 | 2024-10-08 11:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.5 |
| 40945ac7-bd58-3f77-8f51-0308dc5125c2 | -18.6192 | -57.2603 | 2024-10-08 11:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 5ef80463-33c4-3e34-9a2c-f908c17c9776 | -20.3724 | -48.8372 | 2024-10-08 11:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 82401aeb-3a24-3c07-acc8-501141f11cd8 | -14.7186 | -45.1588 | 2024-10-08 11:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5ff91a29-b211-3daf-bb93-39c530b4d032 | -16.4184 | -55.9455 | 2024-10-08 11:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 143.3 |
| 18fb7b6e-e068-39b1-965e-ea15c2e9958f | -16.418 | -55.9662 | 2024-10-08 11:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| ebd865f9-454e-3dde-9a5b-4f25c375ddfd | -16.8048 | -57.4197 | 2024-10-08 11:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.9 |
| 6ffcc079-38ff-3cf7-a95e-a805084f76b8 | -17.0992 | -57.3651 | 2024-10-08 11:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.6 |
| 98920e1b-1a3d-33bf-8760-f17c43561c74 | -17.6692 | -53.0174 | 2024-10-08 11:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b6143771-e5ba-3116-a5c8-caf5c12ffe6c | -20.4258 | -47.6453 | 2024-10-08 11:36:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 123.7 |
| fb09e1d6-be4f-374e-93ef-f8b9605270db | -20.3513 | -48.8648 | 2024-10-08 11:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 3dedb216-6a9d-3c00-9ba9-4c587d1f4805 | -14.7186 | -45.1588 | 2024-10-08 11:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| a730dc41-a7d8-3af7-9ed3-989ac1018129 | -16.5902 | -46.4746 | 2024-10-08 11:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 6e51d0e5-47f2-305b-93ff-ac0654eeab18 | -16.4184 | -55.9455 | 2024-10-08 11:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 133.1 |
| c42282e3-0b14-3a3d-93c3-d01f390d4b10 | -16.571 | -46.4553 | 2024-10-08 11:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 348.5 |
| df06f183-498f-3164-85f0-8fe42d51e3d2 | -16.5512 | -46.4592 | 2024-10-08 11:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| dd1249c9-6a08-381f-bd3e-076cb33af477 | -16.8048 | -57.4197 | 2024-10-08 11:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 178.3 |
| f8d2f33d-1de0-3269-94b9-a0a37f544bb7 | -16.8244 | -57.4175 | 2024-10-08 11:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 8729d616-e2e1-38e6-b947-724b4f0940ae | -17.1471 | -56.8256 | 2024-10-08 11:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 0e57d4c8-5482-3c53-8412-82f5c7191447 | -17.0992 | -57.3651 | 2024-10-08 11:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 183.6 |
| f9289041-2a5e-3e14-b737-22a7c0850146 | -17.6692 | -53.0174 | 2024-10-08 11:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e50cfd65-5ec6-3734-97fe-15a2195754c5 | -18.7183 | -57.2682 | 2024-10-08 11:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 3d4fcd23-9b93-3482-8745-f2812c6fab11 | -20.3513 | -48.8648 | 2024-10-08 11:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 334.5 |
| 20ae2950-1473-3406-80f9-9dcb2dd927f3 | -20.3935 | -48.8096 | 2024-10-08 11:46:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 113.2 |
| f3ff6ad6-123a-321b-8ab8-86d3d05b1c47 | -20.3315 | -48.8462 | 2024-10-08 11:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 15182edb-6f80-32fc-8ab5-6f21b8ce4f58 | -21.9782 | -46.5507 | 2024-10-08 11:47:07 | GOES-16 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.3 |
| 5170e3a6-b303-333f-b0f6-a22d92eac7cb | -13.8754 | -44.5858 | 2024-10-08 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| a0ac1b71-c6a9-3811-933b-455994978011 | -13.8559 | -44.5892 | 2024-10-08 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| feda5a45-007d-37e7-833f-a741d3bc09cb | -13.9333 | -44.5989 | 2024-10-08 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 1b498980-b98a-3549-9cd6-5440f93a4074 | -14.6991 | -45.1624 | 2024-10-08 11:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 15691fb9-7c20-35f5-b370-22c2c280a55e | -14.7186 | -45.1588 | 2024-10-08 11:56:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| c59289b6-03ff-383e-ab4a-3898a8d2fa7b | -15.7068 | -59.4326 | 2024-10-08 11:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 9967a52a-3d53-3c26-af4c-e1b5903d3cb4 | -16.418 | -55.9662 | 2024-10-08 11:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 57c9ebf1-5748-3d0b-b163-91318220cbd1 | -16.3956 | -57.3845 | 2024-10-08 11:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 360ac004-50c5-31df-a9c8-79fba9f1d626 | -16.4184 | -55.9455 | 2024-10-08 11:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 165.1 |


[Clique aqui para ver as próximas entradas](README136.md)

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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd0dbce-a530-3755-bb57-e89f355ec2ce | -2.6482 | -49.2465 | 2024-10-29 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 74201cf1-148a-3e33-a279-ee407e5282d3 | -2.6666 | -49.2673 | 2024-10-29 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0d6f7b0c-6e28-3190-beb9-5e2d3a8b69cd | -3.0501 | -50.4171 | 2024-10-29 04:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 5e708337-9978-39ac-94b7-201d7291ae02 | -3.1097 | -54.2865 | 2024-10-29 04:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| bb110d1e-4792-34f4-928c-5d97b0c53cca | -3.1098 | -54.2665 | 2024-10-29 04:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 24e6dcb1-cda9-343c-a8b8-cfd3dc2e3850 | -3.1794 | -50.3922 | 2024-10-29 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ad5487c6-bb4f-31be-8688-0b33c4a759de | -3.2503 | -46.8709 | 2024-10-29 04:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 4a7948b8-f1e4-3cfb-a3cc-f62da30cb941 | -3.2504 | -46.8489 | 2024-10-29 04:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d7b80dc0-ddb8-3fa2-b30a-7a1c40165d39 | -4.3473 | -43.779 | 2024-10-29 04:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| d6987efb-3a8b-376f-be29-ac8127856512 | -4.3475 | -43.7559 | 2024-10-29 04:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| f2231630-b0a3-3c39-af89-57f518d678d3 | -4.2762 | -46.0956 | 2024-10-29 04:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b7118141-125e-3f46-9669-eeb0cd7665b1 | -6.137 | -42.507 | 2024-10-29 04:15:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 8537e234-b7ec-3f69-872f-c453e00f718e | -12.3334 | -49.9208 | 2024-10-29 04:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4b33400f-113c-325f-8945-20a6dda32609 | -12.3522 | -49.94 | 2024-10-29 04:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f303b172-e858-3aee-b646-a8b82c20644b | -12.3526 | -49.9184 | 2024-10-29 04:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b412f6fb-4f56-3222-b755-f073538df7e8 | -13.6028 | -45.587 | 2024-10-29 04:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 569db1ac-6fa9-38b8-8758-ed13365fbdd8 | -2.6667 | -49.246 | 2024-10-29 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 6bf51919-5ab0-31e8-ab6f-d7c92db369a0 | -2.6666 | -49.2673 | 2024-10-29 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 784bb577-560a-33dd-acf1-39e36e77910f | -2.6482 | -49.2465 | 2024-10-29 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e1d71944-1ee7-3089-b3ab-77312b303295 | -3.1097 | -54.2865 | 2024-10-29 04:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 6033e596-c2f2-3e45-a56e-4675a640905d | -3.0913 | -54.287 | 2024-10-29 04:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e83afbdb-c167-358e-a228-9b78d6feb422 | -3.2503 | -46.8709 | 2024-10-29 04:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 8f16e15a-b631-38b5-bb7b-8be6e5c4c65e | -3.1794 | -50.3922 | 2024-10-29 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 464cbb38-3956-3891-9ea2-a845bec7c42a | -4.3473 | -43.779 | 2024-10-29 04:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 8e97fdc8-cf49-39c2-905d-d9e9347850a2 | -12.3526 | -49.9184 | 2024-10-29 04:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 4a3f7d79-09d4-3391-959f-64f10a70f98c | -12.3522 | -49.94 | 2024-10-29 04:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f25625fb-ea9c-3221-9e64-668893ce80b0 | -12.3334 | -49.9208 | 2024-10-29 04:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 8f20758f-c685-34ef-8516-9902a5186ca2 | -2.6666 | -49.2673 | 2024-10-29 04:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 4a31a13b-d835-3f9b-9f31-450ad5c270de | -2.6667 | -49.246 | 2024-10-29 04:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| d31a5e56-8e2d-354f-888e-b406bbce00e3 | -3.1097 | -54.2865 | 2024-10-29 04:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 2543fd42-8cb8-3e0a-a9db-b431a376c1e9 | -3.1098 | -54.2665 | 2024-10-29 04:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c27ed3d7-60cc-3dae-9d85-9d21350cb4b5 | -3.1794 | -50.3922 | 2024-10-29 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e9b8ac04-89de-3606-b1aa-e351cd02fb14 | -3.2503 | -46.8709 | 2024-10-29 04:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 3ed9b2a6-efa1-38a9-84e8-ad53b708a54e | -4.2762 | -46.0956 | 2024-10-29 04:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| d32d12a6-9919-30a1-bc61-a047b3587db4 | -12.3526 | -49.9184 | 2024-10-29 04:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 9a23c331-6671-313d-a014-053a11970237 | -12.3522 | -49.94 | 2024-10-29 04:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| fc76e196-9561-3863-881c-a2b86d7181fe | -13.6887 | -46.1247 | 2024-10-29 04:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a3c05891-0635-37d8-b877-b8e4883e4c59 | -2.13376 | -48.3797 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e3a74c5-b830-31f0-932a-868614c2ebd7 | -3.58993 | -40.33238 | 2024-10-29 04:38:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 56fa688e-fe81-34ac-9708-49e6f4830065 | -4.40685 | -40.6945 | 2024-10-29 04:38:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 010a3cc3-6883-32aa-8e22-8165ec0f5e1e | -3.85794 | -40.70111 | 2024-10-29 04:38:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 86c3da07-e0e0-3bb8-a7e0-c2b46e038645 | -3.85728 | -40.70058 | 2024-10-29 04:38:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e209e0d4-91bd-3be6-b2fe-57adf08e69ba | -3.85684 | -40.70346 | 2024-10-29 04:38:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a973799c-1a8f-333f-b4c7-8deb97a3073c | -3.85296 | -40.70041 | 2024-10-29 04:38:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c7558faf-36ee-3191-ace3-5e26d2940ba4 | -3.80003 | -40.96589 | 2024-10-29 04:38:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e225fd4-b160-3eab-bca4-23dc74b435f6 | -3.79731 | -40.96488 | 2024-10-29 04:38:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf27af37-db7a-36b1-9af7-e5c20ab22a9b | -3.39423 | -41.60923 | 2024-10-29 04:38:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8370c5ea-9678-3653-a8e7-07f3a3c5224a | -4.85777 | -42.47176 | 2024-10-29 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e0d3deb2-beb9-338e-af8f-d5ed2a14514c | -4.85711 | -42.47623 | 2024-10-29 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 32360d87-6dd4-3a3b-82d3-da75e18e3bb8 | -4.09862 | -42.51884 | 2024-10-29 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8c4b55aa-40b3-3a6d-83b3-614dc700196a | -3.94864 | -41.50106 | 2024-10-29 04:38:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa947a21-9fad-3923-a01e-782919b7dd70 | -3.94739 | -41.49835 | 2024-10-29 04:38:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c5c190ff-6fa1-344e-bb05-a1ad4f3c280c | -3.86919 | -41.79641 | 2024-10-29 04:38:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0a991eac-357d-3f02-9ab3-b08a0223aaeb | -4.86528 | -42.63398 | 2024-10-29 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b93de8f8-a3cd-3d4b-8b7a-cbf11e8b4d27 | -4.86508 | -42.63166 | 2024-10-29 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 09011934-8601-3065-babb-9ef285e85210 | -4.94276 | -43.20687 | 2024-10-29 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9733058-2c95-313c-8081-c72007f1481f | -4.50356 | -43.13371 | 2024-10-29 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a1c6455a-50f7-3591-b835-86d34601fb53 | -4.38366 | -43.0353 | 2024-10-29 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c781632-8036-300c-9ebf-0b2363cc2a63 | -4.38308 | -43.03929 | 2024-10-29 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4656731d-ed10-3da6-a30a-0f55ef5430e8 | -3.41525 | -44.31864 | 2024-10-29 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bda423ef-d003-30d2-8a2b-c5c544576045 | -3.07413 | -44.11039 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a61ad2f2-9469-3d4c-a269-994562aaf5f9 | -3.48178 | -43.91547 | 2024-10-29 04:38:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 701c0c16-e240-3219-aac8-852302a29651 | -3.40918 | -42.98398 | 2024-10-29 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e60389e-bf79-3aa5-99e0-9d1b16504a6a | -3.40905 | -42.9873 | 2024-10-29 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 099f3912-8c57-3670-a618-1667e2d7f616 | -3.40857 | -42.9879 | 2024-10-29 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a15a834-fa52-370f-827e-d2ef531247d0 | -3.40483 | -42.98666 | 2024-10-29 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffd69ab6-2fc8-3e41-8a62-a9ac35fa83b0 | -3.35669 | -42.95994 | 2024-10-29 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3deecc2b-9f96-3997-bfc7-d093e0c277c5 | -3.42202 | -44.31128 | 2024-10-29 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52b9a364-5821-3752-9e6c-16df08488575 | -3.42062 | -44.30956 | 2024-10-29 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c1144c3-86da-3ee9-8aa4-80a6b7b72956 | -3.65726 | -44.18597 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4c7c2930-7919-3cc1-9123-f7e3bb0f0c23 | -3.65335 | -44.18537 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 878d75a9-21f3-3f8d-959f-f9f4fbfe8d6b | -4.8029 | -43.78559 | 2024-10-29 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da97af5f-d636-3240-8624-be51dd4c3dd9 | -4.80229 | -43.78837 | 2024-10-29 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31874b07-bfc0-322e-8179-555d72bf7853 | -4.80176 | -43.79198 | 2024-10-29 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a959cf90-e54a-3e55-ab3d-ef5f7b245b9e | -4.82011 | -44.35629 | 2024-10-29 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5761c5fc-9000-3662-a3f4-b0ece303ee2b | -4.70033 | -44.16362 | 2024-10-29 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a44f26f-595a-3b74-b3ac-02e641b25e2d | -4.69635 | -44.16301 | 2024-10-29 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5699634d-4823-30a0-b5af-306e5a05e299 | -4.26755 | -44.4018 | 2024-10-29 04:38:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 206fc248-6a2a-3912-ac0f-78ae72324c1a | -3.65652 | -44.19095 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d985cb81-0c67-39fb-9520-dafcedf4fb32 | -3.65636 | -44.18936 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 688adf7f-725b-31a5-af7c-5a7b795c482d | -3.65558 | -44.19436 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 23117ad1-e87e-3b6f-98af-af754d05db29 | -3.65261 | -44.19033 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6fe02813-4ec7-317b-a5c1-2b54d590d664 | -3.65244 | -44.18875 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4e31b842-cdc9-3a77-bcda-24e090583f01 | -3.65167 | -44.19373 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f655350a-2c6a-3062-a4dd-8f206204b75b | -3.6487 | -44.18972 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8e67bcf7-93e1-33c9-b2ef-7d3534147036 | -3.64853 | -44.18816 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dc9acdb8-4f61-30e8-9ff6-965bf938cf5d | -3.64777 | -44.19312 | 2024-10-29 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 994cb4ba-d285-3514-8edf-502e22e7bae5 | -3.47299 | -45.4226 | 2024-10-29 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ae74d42-e9d8-36a8-b537-1b3f0d26f833 | -3.47249 | -45.42003 | 2024-10-29 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b43f34c-4ef7-3d2f-b3e5-35c5ea30f882 | -3.47183 | -45.42426 | 2024-10-29 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 891a6a3b-2b5d-3eac-9dd1-71e4fad23ca1 | -3.46936 | -45.42204 | 2024-10-29 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2a6ebb8-e727-301e-8874-1a484cb9b4e9 | -3.08068 | -45.91014 | 2024-10-29 04:38:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79642307-b4b3-3360-9088-387a137b6e35 | -3.07654 | -45.91356 | 2024-10-29 04:38:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5322f419-82c9-3a59-a34e-0f0fd49d9c44 | -3.01986 | -45.1255 | 2024-10-29 04:38:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fe17ce0-055a-3869-a2ee-f4c0351a52b3 | -2.24566 | -45.61512 | 2024-10-29 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 729a113e-ea40-37e3-8262-886492ea786d | -2.2455 | -45.61446 | 2024-10-29 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a28d859-0b88-3bb3-8708-6b2b4018377f | -2.24503 | -45.61913 | 2024-10-29 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6854db5-8260-3559-8b30-1087193eeaa5 | -2.24489 | -45.61847 | 2024-10-29 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a212a3f4-265d-31cd-bc0e-e82d8d089c1c | -2.24211 | -45.61458 | 2024-10-29 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2eca2be-4335-39d7-8ca5-21c7b2aa7e5a | -2.24195 | -45.61391 | 2024-10-29 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README35.md)

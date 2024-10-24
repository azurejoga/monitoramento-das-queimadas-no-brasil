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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| badb3c11-a75e-3e86-8532-57e1b7cfdbd0 | -17.23042 | -57.24867 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9c6401b3-1711-3c17-a52b-1fe1ab8720dc | -17.22952 | -57.25329 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 083b53d7-0e5d-3871-bbab-f1fbb1e54028 | -17.22931 | -57.32559 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 47195e20-10ef-376d-8d8d-b8b66c166910 | -17.22768 | -57.24894 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 21b51c0b-f488-3896-865a-7a9d54b871ba | -17.22681 | -57.25357 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4018a874-e76b-3e07-9da5-6b291f91668f | -17.22598 | -57.24775 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5d342122-a406-368f-9bed-bc6988afc286 | -17.22507 | -57.25237 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3492d0c5-3d49-3cce-94fe-b937f867d0a2 | -17.22417 | -57.25699 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e2b4152b-3083-3aec-a8f6-d614521c0cf1 | -17.22149 | -57.25728 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d441b245-5b40-3c1d-87fa-6b54a84e18f7 | -17.22046 | -57.29958 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0047bb9c-455c-3709-88ea-e40034e80f7b | -17.21972 | -57.25608 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cf0110d3-73ac-34d3-a3d3-7c64e83f7742 | -17.21616 | -57.26099 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9d1941f7-9c5b-3adf-be99-13f74ca7e0ea | -17.21529 | -57.26562 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 468b1c0f-145c-3cac-8e37-fe68775d06ea | -17.21345 | -57.2644 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 11d26bf5-aa8b-30e1-9c22-ecc4575eb36a | -17.20996 | -57.26933 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ec1a0869-a1e2-3a3a-8acc-7ca41e8eaf68 | -17.19218 | -57.28976 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1defc979-af45-3959-925b-079592bd8da6 | -17.1913 | -57.29443 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f4cf49b3-b80c-3aad-ab17-725e59b489a8 | -17.18683 | -57.29351 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9f053a0f-be91-3e13-94c0-f0099152cc5d | -17.18595 | -57.29816 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e56daf02-3d87-30ac-b291-65ff61c6fc76 | -17.08886 | -57.39036 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 84d5211d-779e-34f9-bc02-38316adb0a68 | -17.08698 | -57.39222 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cce38634-dfc7-3977-ba60-63c31c698672 | -17.08079 | -57.38379 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 262be68d-4a07-31d9-af22-371175c079a9 | -17.07887 | -57.38562 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| b94d8e64-467e-3da4-9f2b-ec583357c525 | -17.07629 | -57.38287 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| d819052b-0181-345f-ad77-7495e3041325 | -17.07536 | -57.38758 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 74028ccc-c466-3b8d-9f67-17e4d1309e3b | -17.07438 | -57.38468 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 84d485b3-3d46-3cde-863b-7528b6dff148 | -17.06447 | -57.38756 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0a88b730-74ff-3bdb-89ec-7c596b711be6 | -17.05907 | -57.39136 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 377b42ab-bdf2-33e1-af49-d166ce2c0a33 | -17.03564 | -57.39144 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 94f9b192-0bb3-3ef3-83e4-d2136b6ee7a5 | -17.03029 | -57.37066 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2c5681e7-0495-37f8-b159-9ff02865eb5a | -17.0267 | -57.365 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8f623e9a-5410-3bd3-a163-d6d246f6bb1e | -17.02579 | -57.36974 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 36a879ad-d48d-3a6c-963f-dd020cbe6630 | -17.02221 | -57.36408 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 01159ca6-8e6f-3ddc-b11a-8762544daff4 | -17.02037 | -57.37354 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| af96aaf2-5da5-3489-a85c-530d991aaf11 | -17.01854 | -57.383 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2e637378-3017-32d9-aa6d-87b8381e67e5 | -17.01588 | -57.3726 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8cc94769-3010-3e2e-ae5e-4d5303607760 | -17.01496 | -57.37733 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 15a97120-7b9d-3f5e-bf26-28aa6c38d383 | -17.01321 | -57.36223 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4e757327-1044-3a4f-9f8f-7628c179ae89 | -17.01229 | -57.36695 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b18b42ed-388a-34bf-a494-f89cfc3a3c05 | -17.01045 | -57.37641 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| b3164e77-cdf8-3314-9d4f-0bbd976fa5e5 | -17.00871 | -57.36132 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dec94f08-ad8d-35a4-b4e7-ace447db7e09 | -17.00615 | -57.32651 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5e7109c8-7a67-3faf-a160-af303f0284b4 | -17.00595 | -57.37548 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 4ef26f02-885d-3af0-8254-e6b56be6763d | -17.00503 | -57.38021 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 42e26480-7346-389e-95cd-fe2068dd7920 | -17.00145 | -57.37455 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 26e3c9c0-c822-3e22-b1e2-0eb3bdec6648 | -17.00075 | -57.33028 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 6f9cd9d7-faec-3be2-8399-d1ecb07aed53 | -16.86841 | -57.27213 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 27ec7ad6-733c-3755-bc11-5e9d3d4af63a | -16.8223 | -57.41553 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f5c552ff-2988-380f-a7b5-e9a35e0be599 | -17.78778 | -57.57341 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 6b3b8262-208b-3a68-9453-4a0f5c4efa88 | -17.78687 | -57.57815 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| e0d6fb68-c591-3501-93b6-deefff9af951 | -17.78595 | -57.58289 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e9628033-8bff-3da5-bfbb-210da6755f6e | -17.78146 | -57.58194 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d775eaa7-c444-3732-8b85-86a7f9debabd | -17.78054 | -57.58669 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 129d77c8-a664-39c7-9c9d-1192ee2ab20d | -17.77696 | -57.581 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2a6731e3-d665-3cff-a540-db0385e36a5b | -17.77604 | -57.58575 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2cb39e62-f414-3837-8403-6f4e22beb4ae | -17.77246 | -57.58005 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 45daf3ae-6c8a-334c-a71d-efef70d048ad | -17.77154 | -57.58481 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5e21930b-5497-3813-8ad1-8ff622f02ac9 | -17.76705 | -57.58386 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9741d3bc-1656-30ff-93b5-f4faf5c046e8 | -17.76255 | -57.58291 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 14e86127-d924-3e8e-b271-ce50d932bdde | -17.75262 | -57.58578 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 13b09ef5-2c4f-341f-ba94-5ee51571064d | -17.7517 | -57.59054 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| e1846688-e1e8-33d2-abd0-302fed4f0e15 | -17.74812 | -57.58484 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b15a27c4-62fe-38a5-9673-34b69da94d14 | -17.7472 | -57.58959 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| cb5d1082-2f91-37e2-a64e-ed946743b797 | -17.7464 | -57.56967 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 00fb8199-edea-302a-8312-08b12b6fdea1 | -17.74455 | -57.57916 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| dc55bd64-54e2-343b-b123-9ec272ceae11 | -17.74362 | -57.5839 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b7ff33be-9093-30c3-ba1e-b481eb677021 | -17.74098 | -57.57347 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8b2e6a70-bd9a-3cd7-b4e2-98aea38a5377 | -17.77659 | -57.39097 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bec88e37-7306-3f47-85b3-a5c7912b0c99 | -17.77304 | -57.38544 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 828bec31-9a4b-3a8d-ba6a-e385177466d0 | -17.7686 | -57.38452 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4660e505-0c93-311f-b574-9c844eaad68f | -17.7571 | -57.13898 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8c1d4f32-9198-336d-9ee5-6578f1176395 | -17.75264 | -57.37162 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 65143715-e7d3-3f80-8522-e87bda934431 | -17.7502 | -57.36852 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 331fcd14-25d2-3784-a2ba-2613ff6f9c02 | -17.74933 | -57.37312 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ef47adf4-ecdc-3cc1-8bd6-91d07fb7fd1a | -17.7482 | -57.3707 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c5e5be0e-4221-34e8-ab94-239144878db5 | -17.71113 | -57.35556 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 616762c2-3aef-37ff-ba6e-6abd44dda36e | -17.71025 | -57.36015 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b9a4916e-e19d-3054-99aa-a2d09ad61f98 | -17.70581 | -57.35923 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 55422dcf-aa68-32e3-a3b4-0fde22a5b6ed | -17.70048 | -57.36292 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c6b29df1-2fe8-3aa9-8cf3-bacf79054270 | -17.69515 | -57.3666 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 66f38cfc-3ad3-391e-bef6-940258b674da | -17.69426 | -57.37122 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 842d89f3-5990-3471-bf37-5f7ad25c6a99 | -17.3145 | -57.28301 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0fbdff7a-2dc7-3b00-89ad-54a4d281db01 | -17.31227 | -57.27999 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| fe7a84f7-2329-3fb1-ad79-0bd3c47efbe3 | -17.30161 | -57.28739 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 126740a2-338b-3b9a-9ce4-ee7920eaa15b | -17.29716 | -57.28647 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 782298b5-16f8-315a-aa54-6b910a868106 | -17.29359 | -57.28092 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 58146e8b-92d7-317d-a893-355e3378eaf4 | -17.2927 | -57.28555 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4b2c16eb-0aae-35c2-b1a6-494fe49c242c | -17.28289 | -57.2643 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4485b44a-bc9e-3f92-b541-72da6ea68517 | -17.28201 | -57.26891 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1aa3ce6a-98f8-34fa-a135-feb7e7c1379d | -17.28113 | -57.29762 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| c0494b65-985d-397b-babd-9aa5e1fb6baa | -17.28112 | -57.27353 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 44e63fd7-2311-3af5-9db3-a95b40d216e8 | -17.28024 | -57.30225 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a6a6eeaa-4ff2-3928-8204-ccbc860f91eb | -17.27756 | -57.26799 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| e5b2f741-278c-3c25-a5c0-45dbd8f1b35a | -17.27668 | -57.2967 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 01aba6b7-907b-3188-9fea-754b35511597 | -17.27579 | -57.30133 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 430a7b69-04e6-3047-8708-495701043636 | -17.27133 | -57.30041 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 48d69c96-4bf7-380d-8d20-8801d251a2ae | -17.27133 | -57.27632 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| adf0f4e8-4243-3f80-adb3-b027b83bc7f0 | -17.27044 | -57.28094 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b2fa17ab-977b-311b-9a11-fd8771f13209 | -17.26955 | -57.28558 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 99091ae2-06b5-3932-914b-14694684a440 | -17.26955 | -57.23759 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README54.md)

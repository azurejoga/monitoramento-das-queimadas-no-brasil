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
| 09638ba6-55b7-3adb-a92b-6aae348bcdb1 | -7.05803 | -71.7605 | 2024-10-04 05:50:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1323bde-016b-373d-94c4-b18c2b07b31f | -7.05409 | -71.75984 | 2024-10-04 05:50:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a48ed71-4d14-3a56-be1f-6c902a968d81 | -7.05323 | -71.7649 | 2024-10-04 05:50:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f6ed03d-ad3a-3176-8dfe-e7eda1df36c8 | -7.05015 | -71.7592 | 2024-10-04 05:50:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 047fe9d5-87c8-3de7-998a-1ef63098cbd5 | -7.04929 | -71.76428 | 2024-10-04 05:50:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96ea6dbe-5edf-3d37-b558-458d9eac73f9 | -16.13594 | -55.91915 | 2024-10-04 05:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 137445fc-0370-394a-8a13-0d8f12739c5d | -16.67317 | -55.5034 | 2024-10-04 05:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 387d085f-c9f8-3422-8ab2-ec8ddea652c7 | -16.67225 | -55.50459 | 2024-10-04 05:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 63c6a987-07d6-39f3-9584-e16e72b68f5d | -17.05881 | -56.68727 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| be8508c6-43b1-36d8-8914-6fb15e460bfc | -17.05826 | -56.69299 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 46e8a56b-49d3-392c-965d-6d20fcc6b649 | -17.04468 | -56.69721 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c78a4e69-0fb5-3383-9ad6-2535c331fc3a | -17.03816 | -56.69649 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ddc1821e-8eab-349b-b4e4-9df26f2ef517 | -17.03762 | -56.70222 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cacf0bec-0b03-3066-94d6-7fd030382025 | -16.93003 | -55.83442 | 2024-10-04 05:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b6ae6e7d-db8c-33d2-b7bf-b1c476fa761f | -16.92948 | -55.84084 | 2024-10-04 05:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 205ee85b-b9fa-33d5-abb5-067ac015565c | -16.92877 | -55.83403 | 2024-10-04 05:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a7a849a7-3614-3627-a31f-8c3e295ac128 | -16.92818 | -55.84043 | 2024-10-04 05:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 952e8694-be1d-3a8c-b7be-5fe978af8ae4 | -16.92193 | -55.83323 | 2024-10-04 05:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 305ca7a5-120f-3e80-bf90-04857fd0d95b | -16.92135 | -55.83958 | 2024-10-04 05:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1b4c6dcc-232f-3cd9-8c18-4bfb852e54b1 | -16.91628 | -55.81945 | 2024-10-04 05:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4f38441d-05e8-3045-aba7-1888598209a9 | -16.91569 | -55.82594 | 2024-10-04 05:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| a772a74a-ea5e-359e-94fe-13545471c0e0 | -16.61668 | -57.19593 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 834066f1-a320-32f0-839f-fdd9633105cc | -16.61355 | -57.19104 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b6c40227-ec1e-3396-8b53-562df5898fe1 | -16.61302 | -57.19622 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 73b9b54e-d594-3d6f-a671-554787bf5eb7 | -16.61136 | -57.18478 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3fdbc11a-5dde-36a3-a81a-b00040ea10e6 | -16.61087 | -57.18998 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1fad1616-43da-3d11-b489-72d60b7668ce | -16.61038 | -57.19518 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 453de13c-91d6-39f2-958a-6e656f5dbea8 | -16.60989 | -57.20037 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 56cb6aef-4d94-3cc8-adaa-0aaf337e4511 | -16.6083 | -57.17994 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8e26e8ed-da94-3d72-bde6-15f672aa366f | -16.60777 | -57.18513 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c31643be-c756-3fd3-932a-9c5e8df89cdd | -16.60725 | -57.1903 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c9a09dd4-5be5-3c07-aee9-9e2cb187c4ef | -16.60673 | -57.19548 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| aa5b3eaf-83bf-39e8-988c-0f22b73692c2 | -16.6062 | -57.20066 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| f8514e68-6a4c-36e1-9cb2-db2af909ba48 | -16.60555 | -57.17884 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 89294a05-4676-32ff-b774-422d0aab9ab7 | -16.60506 | -57.18404 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c16a9701-dce2-3a51-bcc5-23f9c989a5d2 | -16.60457 | -57.18924 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 17798a5d-2bb6-3e0f-833f-9e7841a422cc | -16.60408 | -57.19442 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| e0715459-e0aa-3cfc-80d1-6c2fc33d515d | -16.60359 | -57.19962 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| b6bedb9c-fd55-3a3c-9fb9-f13857ab7e09 | -16.60252 | -57.17399 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| be7fd46c-d0ff-3979-833b-3ac2468d2f73 | -16.602 | -57.1792 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 56d145c5-a094-33d4-8e41-2100b05793cf | -16.60147 | -57.18439 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| f94d9e1d-557f-3885-91f9-2264fd623fbf | -16.60095 | -57.18956 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| eeccdb05-d605-3092-a97d-58935de4c551 | -16.60043 | -57.19475 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9e148237-9be8-3482-af32-5e3f5e9e006d | -16.60023 | -57.16764 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e06f09a1-780a-373f-a8bb-e684239815cd | -16.59974 | -57.17286 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ba09f4eb-5b18-3ba8-8c47-331df94caacb | -16.59925 | -57.17809 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 74ef059a-56f3-3b13-9771-1df91228cfdb | -16.59876 | -57.18328 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 468c6155-84c4-32ef-b5aa-a73825d552e1 | -16.59827 | -57.18847 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 14b890f8-ee8e-399d-b141-2295c722a18f | -16.59779 | -57.19366 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 95884f66-436f-3ed2-bd00-8d8f4dd78e91 | -16.59674 | -57.16805 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 46d6487d-39a6-3416-b56a-f7128139755b | -16.5957 | -57.17848 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8cd6a9d0-d1aa-3bdc-bd59-0bc5f77cd365 | -16.59518 | -57.18365 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| fadbb196-6537-305c-8193-fd4686a140ea | -16.59466 | -57.18882 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 0a39ce56-74aa-3cee-8d11-6979dc4ad54e | -16.57178 | -57.29031 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d61219b6-300d-3d8b-a146-f377b6d0847c | -16.57127 | -57.29543 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 625ddb78-4a48-3970-b05a-6e77811845a4 | -16.56604 | -57.28445 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| da21d581-3a75-3b2d-972d-ba531109f613 | -16.56553 | -57.28956 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8f4dc806-6ae0-386b-8758-32141c759bed | -16.56502 | -57.29467 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 6764b083-53e5-3ca4-a1c7-21c3cd3d06c2 | -16.55978 | -57.28373 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 063e0943-ebbc-3e44-b794-c8481116a4df | -16.55927 | -57.28882 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7675b115-0993-348a-aae2-31e83da4c000 | -16.41887 | -57.38734 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 2994396e-c206-3496-9563-dd894064d755 | -16.41837 | -57.39235 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| da917c41-fab6-3c5b-9871-b8b2fbd8820b | -16.41788 | -57.39734 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 903f1e3e-c0ea-3cad-b545-5df767c617be | -16.41265 | -57.38662 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a50664f7-ae42-3958-becc-931aeeca7d91 | -16.41216 | -57.39162 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 23ada1da-193c-327c-a176-15b306e1b323 | -16.41167 | -57.39665 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4b76828d-ecb1-3c37-96d3-255176802183 | -16.40741 | -57.38638 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 22608e83-fa9e-3252-b7cb-aa955c28259e | -16.40688 | -57.39138 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dc9f1446-d500-36ab-b02d-5f6ccdd1ad30 | -16.40636 | -57.39637 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b49f8285-d107-32d7-9882-fb9386415939 | -16.40595 | -57.39094 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e6e76dbf-8b75-3828-aee8-605110f53533 | -16.40583 | -57.40141 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| da81b566-5941-33b6-877c-fabe77c8e59e | -16.40546 | -57.39593 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c06e0937-5e57-3104-b38e-089c932f15fe | -16.40067 | -57.39069 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 596a32cb-292c-36bc-b52e-a3767702ba1d | -16.08148 | -57.52905 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58a4177b-7fcc-3cc4-a7f6-8346b17ca9c5 | -16.0811 | -57.53281 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 825fcc7a-7ca4-35ed-aae4-ad376bb8348b | -15.9388 | -57.46522 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5348e13b-03ce-373e-8f1a-b4b8d173f61d | -15.78827 | -57.35646 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eef65cb0-ea7b-34be-adc6-bbb5a3e14f48 | -15.78786 | -57.36045 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7522c632-3b2b-30ec-8f2f-a6d20c8d70e6 | -15.78745 | -57.36445 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b5f6841-439c-3612-aeb4-aeeec2da7596 | -15.78178 | -57.35875 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aeb3de63-81f6-3d86-81a6-8cec748e8650 | -15.77647 | -57.35363 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05e5fa69-603a-38d5-8a1c-beb9f8aff938 | -15.77609 | -57.35318 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e16f7b58-16b3-36d4-9f40-71aa6460da32 | -15.77603 | -57.35771 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78428c37-4ec3-3777-bf3b-d8b8aa0554ff | -15.77081 | -57.3481 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1887c5f2-3876-3eeb-a93c-4f644092a604 | -15.77039 | -57.34763 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1be6201e-55d0-3307-9f1e-65cd023a6517 | -15.6948 | -57.41831 | 2024-10-04 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c966d0d-6113-3c14-974f-9a212efe5658 | -15.69439 | -57.42229 | 2024-10-04 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 219e938a-ef9f-3d50-b19f-4d8d6b08f131 | -15.65391 | -57.39488 | 2024-10-04 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8334eb51-39b4-3e97-baa0-8aac6ea88641 | -15.65358 | -57.39518 | 2024-10-04 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01f9ec16-edad-3759-9c32-b2eb253adb4b | -15.64745 | -57.39702 | 2024-10-04 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0ab4305-8b46-3309-a62f-a086388192c4 | -15.64713 | -57.3973 | 2024-10-04 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dce1bf9b-53db-3ca8-a4f3-a1520711aaff | -15.64699 | -57.40131 | 2024-10-04 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 770cd12b-409c-3235-8315-e6c51841c7a8 | -15.6467 | -57.40168 | 2024-10-04 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74efc621-a6fb-3f15-ae86-26e1ad510012 | -16.92201 | -57.70152 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| dcfd7baf-1b27-3c66-bb5b-fb61ef100ddf | -16.92153 | -57.70638 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4ef191b8-b198-3612-bd0a-13cce1c74522 | -16.91636 | -57.69592 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b90f7740-2c3f-363e-a448-c5c85c7100dd | -16.91589 | -57.70077 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f5e2d885-aa90-312d-9e9e-e42616c886ed | -16.89279 | -57.68324 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fadcfefc-0f11-3fe6-89b8-f2e20e000edd | -16.88713 | -57.67764 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e6cdcf8f-4ede-3c53-a0b6-9be8fdd15175 | -16.8871 | -57.67744 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |


[Clique aqui para ver as próximas entradas](README179.md)

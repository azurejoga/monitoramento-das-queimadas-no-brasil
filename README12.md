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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d40676d2-48f6-312f-a52d-bc73792c4bdd | -7.78113 | -34.94414 | 2024-11-22 02:55:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 1f592028-e751-3814-aafa-80696b13e3ad | -6.91743 | -37.10791 | 2024-11-22 02:55:00 | NOAA-20 | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e17381d7-8ffc-3010-bfb3-17e4fae03218 | -1.2041 | -51.9478 | 2024-11-22 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 2292d703-c16d-3ee9-b880-bade9d9d4071 | -3.4975 | -53.8137 | 2024-11-22 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 16af0f6d-f251-3132-b7bb-961a1fbd1ec1 | -3.5159 | -53.8132 | 2024-11-22 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 4fe2f449-97a1-3a55-8697-9954950e82ca | -2.5013 | -48.9949 | 2024-11-22 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 7edd522c-5790-3dce-919b-ca79bce6d91e | -3.516 | -53.793 | 2024-11-22 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 76b5183d-f61c-3eca-a63c-ab4b03e42f6e | -2.9984 | -45.1207 | 2024-11-22 03:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 95c3cd99-4f2f-355a-a1ac-0c5371769649 | -3.774 | -46.1196 | 2024-11-22 03:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 2136f794-eeee-3958-9d24-26ebf2c4bf08 | -3.2768 | -53.8199 | 2024-11-22 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2b27f035-0f7b-3bff-8141-e9fb7d1d465d | -1.2041 | -51.9683 | 2024-11-22 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 119c710f-8cad-3ec7-ac6c-fa6bc742343f | -3.7554 | -46.1204 | 2024-11-22 03:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| e0e980e2-0739-3e5f-a920-5418f82de1da | -1.1857 | -51.948 | 2024-11-22 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 163dc1de-af39-32f1-a716-aae40e8c7bfd | -1.1287 | -53.4153 | 2024-11-22 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0b173fd1-c8d7-3d1c-8a97-f33d13b6e1d3 | -3.3451 | -50.5126 | 2024-11-22 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ac00279c-1dc0-3210-b005-15b463fae551 | -2.9798 | -45.1214 | 2024-11-22 03:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 1138a403-1f50-314e-9433-44f266c5258a | -3.4592 | -45.9104 | 2024-11-22 03:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 170b701f-7580-313f-8cf5-ebc45222cc85 | -2.3549 | -48.5493 | 2024-11-22 03:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| e99e245f-c24d-321d-915b-3f2864ee0f44 | -1.1287 | -53.3951 | 2024-11-22 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 980239e3-ad30-33ac-9178-5c435507c754 | -3.23 | -54.25 | 2024-11-22 03:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23134cbb-24ce-3a34-8f49-66be52655755 | -3.2569 | -54.2426 | 2024-11-22 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 33d85d1d-5aa7-3ae1-8ead-a967741928a7 | -1.1857 | -51.948 | 2024-11-22 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 426859c4-2660-30d0-a109-717d35d3762f | -1.1287 | -53.3951 | 2024-11-22 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 94bf0874-723c-3d2a-8d79-01ad53bf822c | -3.2384 | -54.2632 | 2024-11-22 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 1f2d6ee4-a94e-3542-a149-56c3a14d9c82 | -3.8355 | -52.2576 | 2024-11-22 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ad5ac776-5d6b-3105-83c8-77427aee285b | -3.3451 | -50.5126 | 2024-11-22 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| bb63c13a-e891-31bd-9fa3-6d82a99d3374 | -3.2385 | -54.2431 | 2024-11-22 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 252.2 |
| dcba5705-7e5b-354e-b20c-3d36c2b0903b | -3.4976 | -53.7935 | 2024-11-22 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| e819d2cb-8580-3ac9-a5a6-a6d7f648c31b | -1.2041 | -51.9683 | 2024-11-22 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8447c03e-286e-3c51-b25a-c537b005f769 | -3.516 | -53.793 | 2024-11-22 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| a4971222-ba8c-3ebd-bc9d-c6004a706843 | -3.2201 | -54.2436 | 2024-11-22 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 35141d3b-d112-3cad-b61c-e21ee571cdd8 | -3.4592 | -45.9104 | 2024-11-22 03:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 8a3a3205-3e90-38fa-9582-91aea07d049f | -3.2386 | -54.223 | 2024-11-22 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| a2a4bcdc-a359-3468-b096-b37828a9e274 | -2.3548 | -48.5708 | 2024-11-22 03:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 1633ff99-24bc-3dcb-b42b-504df2d99bdd | -3.4593 | -45.8881 | 2024-11-22 03:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8040bd27-6dba-3261-8efb-a8d4b33772f6 | -3.4975 | -53.8137 | 2024-11-22 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| dd97b02a-4e42-3ee9-b0dd-c11c50d97257 | -2.3549 | -48.5493 | 2024-11-22 03:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| a0a30e5a-b9d9-357a-97fe-79d5acfde27e | -3.2768 | -53.8199 | 2024-11-22 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d839b636-e876-39b7-916f-0a87d7346eb6 | -2.9984 | -45.1207 | 2024-11-22 03:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c06b53e4-f198-363d-9e3e-1bf4f0bbed3a | -1.2041 | -51.9478 | 2024-11-22 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 9a6e3f68-becb-39ee-a7bc-454974e0f4f3 | -3.5159 | -53.8132 | 2024-11-22 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| ed9806fd-8919-34eb-8c8f-c997e23779c9 | -1.1103 | -53.3953 | 2024-11-22 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ae41b411-d303-3632-8cc3-57cb3068c5a8 | -2.5013 | -48.9949 | 2024-11-22 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| cb4f5323-935e-3bcf-9436-cec1fc934536 | -2.9798 | -45.1214 | 2024-11-22 03:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0f1f82d3-8adb-385b-9386-e31939e22634 | -3.2767 | -53.84 | 2024-11-22 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 81381846-8fad-3a0c-a73a-3607cb65f6f1 | -3.7554 | -46.1204 | 2024-11-22 03:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| f3551669-2e8d-3741-ad0a-5e45c4045d72 | -3.774 | -46.1196 | 2024-11-22 03:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 15bb23a7-5870-3a0b-bb52-cfac7ce1e8e3 | -3.22 | -54.2636 | 2024-11-22 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 064ad7b3-3e6e-3ab2-b62f-6df5798ab50b | -3.2384 | -54.2632 | 2024-11-22 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| cb7cae39-3116-341f-aad3-7c60b86bb94a | -3.2768 | -53.8199 | 2024-11-22 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| fcc5e762-13ae-3ea6-aeea-7a0393081a5b | -1.5869 | -53.8134 | 2024-11-22 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f6bd7de8-01ab-3a68-aea9-3f78b3163770 | -3.5159 | -53.8132 | 2024-11-22 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 2b1ac143-b7dd-3cf5-9b0e-eab83a6c5691 | -3.2386 | -54.223 | 2024-11-22 03:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| a16df62f-ba9a-3779-a8e9-e48d6242ad74 | -3.295 | -53.8597 | 2024-11-22 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| d17ce2a1-d91f-3087-83a1-e9d512e80eae | -1.2041 | -51.9683 | 2024-11-22 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 72d8e67c-e675-3cc1-833f-183185f58a26 | -2.3549 | -48.5493 | 2024-11-22 03:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 6af62033-cadc-3264-aa29-9d3f0a4a2263 | -3.516 | -53.793 | 2024-11-22 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6a393963-22ec-34b0-9600-f5a3033a6381 | -3.7554 | -46.1204 | 2024-11-22 03:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b3d4f311-d68b-376e-b4be-08f1f6f2f1fa | -3.4592 | -45.9104 | 2024-11-22 03:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 5131dfb5-58ac-3e6c-a70e-b290deb0984a | -3.2767 | -53.84 | 2024-11-22 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| c3257f41-4966-3e13-be7b-d29d1d69085d | -2.5013 | -48.9949 | 2024-11-22 03:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 75bd2a0b-8d8a-308b-9a3c-72c6d8ef7edd | -1.1857 | -51.948 | 2024-11-22 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| eaaa59af-b81f-3a2d-bec0-b29d7b2fbfb4 | -1.1287 | -53.3951 | 2024-11-22 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 0ac0b4d1-6586-3224-88fd-77aaa1a8009e | -3.22 | -54.2636 | 2024-11-22 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| ec87efa7-2689-3e24-bb13-f54ad74b9404 | -3.2569 | -54.2426 | 2024-11-22 03:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 83d968b1-f068-3705-bc34-33575660ba18 | -3.2201 | -54.2436 | 2024-11-22 03:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 2fbbfcaf-9660-3693-bac2-881806f08b59 | -3.2385 | -54.2431 | 2024-11-22 03:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 251.8 |
| 78ad4520-1cc1-3010-b5a8-d33aa02cc3eb | -3.8355 | -52.2576 | 2024-11-22 03:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 61df42e9-60e3-3d2d-bcd5-60c1970ad764 | -3.2951 | -53.8395 | 2024-11-22 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| b6556e08-f6c3-36e9-87df-9b85c75181e0 | -1.2041 | -51.9478 | 2024-11-22 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c59980b0-83e8-3322-bb34-9fdc1e1e7353 | -2.9798 | -45.1214 | 2024-11-22 03:20:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 678f2485-3e3c-31e3-9914-3a6a627c1b76 | -1.1287 | -53.4153 | 2024-11-22 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 08bbb488-f7c3-315e-a25c-41d9939bc539 | -3.2569 | -54.2426 | 2024-11-22 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| e14a20af-1a20-34e0-a220-ccf717eeaccc | -3.2768 | -53.8199 | 2024-11-22 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c79dd884-f4a0-30ef-a652-a85c9927b51d | -3.4592 | -45.9104 | 2024-11-22 03:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ddf061d1-b29c-3fc0-b013-7381008e9d8e | -2.3549 | -48.5493 | 2024-11-22 03:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b0b8e52d-732f-3c5b-8bf9-d1344594843f | -2.9798 | -45.1214 | 2024-11-22 03:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 41313fd7-c62b-3e5d-a837-14849b4486c1 | -1.2041 | -51.9478 | 2024-11-22 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d746abdf-36b5-3331-980f-af2df18eda81 | -3.22 | -54.2636 | 2024-11-22 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f9883776-c240-3735-ae87-b36767bdc249 | -3.2767 | -53.84 | 2024-11-22 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| dc3b37c7-3df8-3aff-9b42-4e5983316124 | -2.9984 | -45.1207 | 2024-11-22 03:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 431a4fc7-1a8e-30a9-98bf-225d38b5be55 | -1.1287 | -53.3951 | 2024-11-22 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 6ade5600-b8a7-3c78-a4b8-76b4bb47c6a5 | -3.2201 | -54.2436 | 2024-11-22 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| fa515a69-cb53-3a17-b688-1bdf5bd2f934 | -1.1857 | -51.948 | 2024-11-22 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f161725b-82d6-3b42-864b-178cf1d5edb5 | -3.2385 | -54.2431 | 2024-11-22 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 232.2 |
| 972f6026-c1d9-303b-b19f-e6235d24b0c7 | -3.295 | -53.8597 | 2024-11-22 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 62964c06-c151-3a98-b1fa-87b29caa4bbc | -3.516 | -53.793 | 2024-11-22 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| a2f28730-3927-3f2d-a2e4-c6855973e2bf | -1.7366 | -52.3916 | 2024-11-22 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 923a70ac-c45a-3256-9412-3067c1bee502 | -3.2386 | -54.223 | 2024-11-22 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 976c3b4f-2848-3e24-9645-52cd3903fb43 | -3.2384 | -54.2632 | 2024-11-22 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| e3880466-b24e-393d-a469-9c4d8b0a4ee5 | -6.1182 | -42.5086 | 2024-11-22 03:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 30185760-0a26-3567-898d-368f74202ff8 | -3.2951 | -53.8395 | 2024-11-22 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| a6883ca0-a1dc-3542-a6a1-7c00fa0e6da4 | -3.4593 | -45.8881 | 2024-11-22 03:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f75bce9b-9d3f-329f-9f61-fde871c21ebd | -1.1103 | -53.3953 | 2024-11-22 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 02871c14-b1a5-3ebd-9e0e-82410ec615b7 | -3.2767 | -53.84 | 2024-11-22 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 06b77cae-89bf-32cb-862e-90b33923e5f5 | -3.2569 | -54.2426 | 2024-11-22 03:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| bd2e85a7-b8f5-3c33-b947-b3c6cf8064e7 | -3.4592 | -45.9104 | 2024-11-22 03:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| b11e6da1-58e6-383a-8c7e-ebbc7fabfc29 | -2.9798 | -45.1214 | 2024-11-22 03:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| adbbb9d7-83d7-33be-8979-30f684841a00 | -2.9984 | -45.1207 | 2024-11-22 03:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 60923a2f-38df-3f29-8139-888eab61b248 | -6.1182 | -42.5086 | 2024-11-22 03:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |


[Clique aqui para ver as próximas entradas](README13.md)

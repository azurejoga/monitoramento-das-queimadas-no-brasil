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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4f273c-da51-3104-bf8f-4a8699874b06 | -2.8043 | -51.80866 | 2025-12-17 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e85f861a-69d6-3a9d-87bf-c5406b8fc755 | -2.22605 | -51.94525 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04e92853-bad0-3414-bc4f-851fd25318ac | -2.83562 | -54.8385 | 2025-12-17 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 922631dd-84b7-3f47-9a65-0fea193d155d | -0.70995 | -51.9881 | 2025-12-17 05:16:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73d5bdf7-ffd7-32dc-b5f6-fd1cba3b4ca5 | -2.22667 | -51.9411 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f620a98-1602-30ad-97e5-5f96c22d8b6b | -3.68875 | -52.0073 | 2025-12-17 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e980d830-30d3-3dca-ba97-4cf68f4fdf51 | -2.70018 | -51.63968 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04ef54b6-e5e0-3529-aa6f-2698f6fd34cb | -0.70598 | -51.98523 | 2025-12-17 05:16:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91dd9a94-9671-3727-af31-db26603019d2 | -2.69773 | -51.64547 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e0951ce-edb5-32c6-852a-7dc08cb8290b | -1.16531 | -53.65709 | 2025-12-17 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c48b2b-9443-3fb6-9035-bc2421f80ce4 | 2.70522 | -60.74643 | 2025-12-17 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6b1fa0ab-03ff-3cc5-9865-76fb6893bd8b | -2.165 | -53.68796 | 2025-12-17 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c510092-b2f8-3f59-b0cb-55cf09a7d93d | -2.36618 | -47.67705 | 2025-12-17 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34774def-ce88-367e-a2f6-c756aa338646 | -2.92775 | -48.22309 | 2025-12-17 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a60d321c-4a2a-3f21-a235-3f94923a8afe | -3.20805 | -50.6643 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d5805aa-864b-34a4-bcee-1b32b153fab1 | -2.23536 | -51.94244 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ac47199-b36a-3a88-a90d-dde491e89c1e | -1.66526 | -52.05931 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c80089a-09b0-3f09-9b77-b28b1242d69c | -2.22851 | -51.9478 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ea87696-05dd-384f-b87e-73eb80f4fbc2 | -2.9334 | -48.22409 | 2025-12-17 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af5879ee-fa1f-3256-8b6a-fb7e9808e6ac | -2.79255 | -51.41048 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7beb8c8-d84a-3b94-b7d1-67add37826c3 | -2.05039 | -45.44867 | 2025-12-17 05:16:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a98d0e02-23b8-3234-8e2f-dc7a87d539d8 | -1.41963 | -46.06956 | 2025-12-17 05:16:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fef9f9e-68cc-384b-aa26-cd47ffd3197e | 2.70591 | -60.75087 | 2025-12-17 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9d75c769-2d5d-32ab-8e39-abd212a85d93 | -2.23101 | -51.94177 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14b8dab0-5da2-30dd-a467-fdcfe47d19b0 | -2.68744 | -52.07781 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f6c14f1-0e10-3bb8-85f2-38a19fd0f102 | -2.22544 | -51.94939 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32999574-b55c-3522-9cc4-3e3556fdb083 | -2.68221 | -53.0732 | 2025-12-17 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db8c2320-a979-302b-903f-6516930c09a9 | -1.70454 | -52.62562 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58ac7df3-15e3-3601-be71-6bdbd2502959 | -2.92719 | -48.22696 | 2025-12-17 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f00012-2a74-38ef-9360-61d8131382c8 | -2.68809 | -52.07349 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e37c2029-e0d3-3d12-8902-756fad83e6c3 | -2.36986 | -51.91417 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fb4b890-d371-3a28-80a7-21dbafd188fd | -2.37421 | -51.91491 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3cc947d0-663c-3dd5-969b-9795df27ac08 | -3.31103 | -53.21271 | 2025-12-17 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 322b741f-23ad-3839-ba99-157112bb1df1 | -3.03297 | -45.35371 | 2025-12-17 05:16:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dff077f3-246d-356f-b3b4-2b087ad4f91d | -1.66798 | -52.06215 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47a0a5db-59a3-340a-ac0a-44cd32c92b6f | -3.81949 | -48.87401 | 2025-12-17 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d25fb5b5-6975-3963-9db3-6541fb16033a | 2.70895 | -60.74586 | 2025-12-17 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 001fc638-f09e-37be-bfbb-13715548b9a2 | -3.1242 | -54.17375 | 2025-12-17 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5d06237f-467e-3711-8bdf-04cc9a597619 | -1.66036 | -52.06263 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30a0f494-1f1a-3cd3-b13b-dba8757c2455 | -2.77858 | -54.53011 | 2025-12-17 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6784dcb3-0dc3-3722-968d-6b2305590029 | -1.66463 | -52.0633 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f6c5f1c-f296-32c3-a097-097176d03d2a | -3.0262 | -45.35257 | 2025-12-17 05:16:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 704eafdb-ca4c-3e94-bd4a-89a9f9c75ee3 | -3.12801 | -54.1743 | 2025-12-17 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76c43da5-b4ea-3ecb-964f-c3ad16d6a82c | -3.0286 | -51.93534 | 2025-12-17 05:16:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 555f0a06-8b46-3602-b817-6eb157f65f0d | -3.87172 | -40.45162 | 2025-12-17 05:31:00 | AQUA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5dafdb07-21de-3253-8c2d-4ad8406cd499 | -5.55329 | -37.756 | 2025-12-17 05:31:00 | AQUA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bd273a86-04bf-37fe-8cd4-4f7f49faf548 | -9.15403 | -40.97427 | 2025-12-17 05:33:00 | AQUA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 26389c8b-3b29-3097-84d4-a2ddb7f90843 | 2.70666 | -60.74834 | 2025-12-17 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94f9eb09-3b84-35e9-94d9-87f636327d4a | 3.06554 | -60.46848 | 2025-12-17 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77efcbeb-b1a4-3f80-9356-0cb18ce7dc9a | 2.69736 | -60.75787 | 2025-12-17 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c148571b-920b-39ad-b30e-1e9a1e28251a | 2.71019 | -60.74778 | 2025-12-17 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7211deb8-51d8-312a-9381-00d5f2010388 | 2.70314 | -60.7489 | 2025-12-17 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef8da6b1-e136-35d3-be2a-b0d1a8159b9f | 2.69673 | -60.75394 | 2025-12-17 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52484099-7da4-3ed2-8aac-445f5207b1c2 | 2.7073 | -60.75227 | 2025-12-17 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8d0fa60-e608-3542-ac72-8ea24776bc7c | 3.4462 | -60.1465 | 2025-12-17 05:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d590cc0-6854-3f3f-bbd5-11afba509ada | -2.37164 | -51.91859 | 2025-12-17 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e36dbd23-9627-369e-857d-436ee64b995d | -2.3783 | -51.91979 | 2025-12-17 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e2702988-ff0a-3c0b-ac74-34a3c64c9e73 | -2.37659 | -51.91354 | 2025-12-17 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3b5970aa-7914-3991-be28-baf712360736 | -2.69189 | -59.42519 | 2025-12-17 05:46:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90bc423c-f1db-32c0-9a9b-36f7a72fd65b | -2.37569 | -51.91937 | 2025-12-17 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3e710ff-2c1a-3c76-bf6c-64ebc3de6c92 | -2.36902 | -51.91824 | 2025-12-17 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 709df947-1ee6-31c3-af4e-233dbc85905f | -2.70028 | -51.64079 | 2025-12-17 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef29327c-030a-394e-8b84-d0ac94378b83 | -2.37916 | -51.91397 | 2025-12-17 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3899c7fe-740d-3ff4-bb28-3aa9e49a1aef | -2.37251 | -51.9127 | 2025-12-17 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be3b3a50-7444-3711-9151-81fd4914f61a | 2.70562 | -60.75268 | 2025-12-17 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 787d63c9-14fc-32df-91d7-5f5cd9b361a2 | 2.71089 | -60.75183 | 2025-12-17 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2ced652-9618-3fac-ae3d-dca0855060d7 | 2.69561 | -60.75765 | 2025-12-17 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3f43249-4ced-3580-bfd4-dd281b85e6d3 | 2.71035 | -60.74856 | 2025-12-17 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5254a022-8838-33c8-a29a-5d097e399ffb | 2.70508 | -60.7494 | 2025-12-17 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c5a3fbd-0919-3c2a-8585-31b9361f9d0b | 2.70713 | -60.75042 | 2025-12-17 07:09:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 79b4c486-4b53-3caa-97ad-83ed94304073 | -3.34529 | -41.49947 | 2025-12-17 11:34:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| fabc1299-f9f5-35fe-a7e7-8a5657b0c0d5 | -6.77291 | -38.10476 | 2025-12-17 11:36:00 | TERRA_M-M | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 9ca51238-0d7a-3feb-87d4-24194bea9156 | -5.22862 | -38.58036 | 2025-12-17 11:36:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 58cf7e88-562d-31eb-b507-f0b2cecc76c8 | -6.87506 | -38.41347 | 2025-12-17 11:36:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 59b14f67-8942-321a-8175-e5e8973c54c7 | -7.63506 | -35.57686 | 2025-12-17 11:36:00 | TERRA_M-M | NATUBA | PARAÍBA | Brasil | 2509909 | 25 | 33 | nan | nan | nan | Caatinga | 9.5 |
| af116981-6795-3d7e-80d7-eaa2cbb57084 | -6.96974 | -38.01781 | 2025-12-17 11:36:00 | TERRA_M-M | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 1f9994b1-3e12-38e0-893f-f37fbfffa216 | -6.37556 | -38.30361 | 2025-12-17 11:36:00 | TERRA_M-M | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 53b783b3-77ab-3c4d-8b89-0eb413335362 | -8.72848 | -37.17227 | 2025-12-17 11:36:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 25bbeb37-14c7-39ab-9a18-426b0234c4de | -8.62643 | -35.34579 | 2025-12-17 11:36:00 | TERRA_M-M | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| b61e7e73-4887-398c-b612-a61a59809b94 | -5.07126 | -38.20475 | 2025-12-17 11:36:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 18fd8fa2-c170-3af0-8aaa-bcfe79e74e33 | -5.38918 | -38.04337 | 2025-12-17 11:36:00 | TERRA_M-M | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| cf335435-acfc-399f-bd23-c707e36dc98c | -7.12861 | -38.13402 | 2025-12-17 11:36:00 | TERRA_M-M | IGARACY | PARAÍBA | Brasil | 2502607 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 29fd1976-3a72-3b9a-8657-5280e691a221 | -5.69938 | -37.745 | 2025-12-17 11:36:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7b2fe746-6b00-35e4-84e5-535a6bc6f619 | -5.50159 | -39.49493 | 2025-12-17 11:36:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e00b3413-60be-3c69-bebc-011947512dba | -7.09498 | -37.39124 | 2025-12-17 11:36:00 | TERRA_M-M | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 7.3 |
| acf632b0-94f6-39f2-818f-b68a57ad1f65 | -8.86512 | -37.97517 | 2025-12-17 11:36:00 | TERRA_M-M | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8abc6afa-bfea-3f94-ac6d-94b9abb3fa6b | -6.57605 | -38.64691 | 2025-12-17 11:36:00 | TERRA_M-M | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 036b2a54-c0a2-3418-bf33-5fca8da4607e | -8.31255 | -40.0882 | 2025-12-17 11:36:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 8211cb96-d6e4-3d2a-9352-cdd45034e13d | -9.11526 | -40.08582 | 2025-12-17 11:36:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0535359e-bdb1-33d5-8250-42ec4d71a519 | -5.87343 | -38.25895 | 2025-12-17 11:36:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 6a70e8b3-d75d-33af-9a75-f9cb77d0953c | -5.87217 | -38.26775 | 2025-12-17 11:36:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 8cbf48af-0b66-3005-a43c-f1cae8b9898f | -8.32155 | -40.08949 | 2025-12-17 11:36:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 169e7c01-e9df-3cc1-9d0a-ed5086c6e9e3 | -5.69676 | -38.59604 | 2025-12-17 11:36:00 | TERRA_M-M | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| fd0b6d90-2ecb-3ae5-a00e-2718abe3f636 | -9.76198 | -41.88999 | 2025-12-17 11:36:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 30ac44da-4445-3e71-8005-6a40c31cd4a9 | -4.70485 | -39.39095 | 2025-12-17 11:36:00 | TERRA_M-M | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2bfd3370-9049-3c31-8c3b-dacdf9848763 | -11.88092 | -37.60866 | 2025-12-17 11:36:00 | TERRA_M-M | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 95cbd9ab-0f4f-3725-8244-aab0a66482ae | -15.46265 | -39.15424 | 2025-12-17 11:38:00 | TERRA_M-M | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 143.0 |
| f12ca146-0f88-31b1-a818-717e29f7b924 | -13.72437 | -39.91774 | 2025-12-17 11:38:00 | TERRA_M-M | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 909ffa00-5d55-3a3a-9505-3fcbc2ef0381 | -13.72308 | -39.92676 | 2025-12-17 11:38:00 | TERRA_M-M | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 113.9 |
| e0067ff4-ea3a-3a7c-844f-700493f8b617 | -15.46135 | -39.16373 | 2025-12-17 11:38:00 | TERRA_M-M | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |


[Clique aqui para ver as próximas entradas](README12.md)

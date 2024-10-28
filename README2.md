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
| 3bbeb6fa-f935-36a2-9733-69027485586a | -3.0501 | -50.4171 | 2024-10-28 00:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| b9eb3e73-9020-3832-986f-fea71386ef29 | -3.0538 | -49.4895 | 2024-10-28 00:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 21bb6cb2-df36-361d-b4b5-073a0c97d755 | -3.1661 | -53.9235 | 2024-10-28 00:15:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a56879c2-8688-372a-89b6-a231a96ad854 | -3.272 | -46.2072 | 2024-10-28 00:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5d6b540d-413f-3d83-9a16-0dd043d23086 | -3.4014 | -46.3131 | 2024-10-28 00:15:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 14a4f2c8-2404-36a4-9501-8ef0cdcc347b | -3.6727 | -51.5629 | 2024-10-28 00:15:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4933c0ea-9532-3acd-969f-6c523f85ab56 | -3.6911 | -51.5622 | 2024-10-28 00:15:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| e6288a2f-0084-3a42-8f9f-41efab355b4e | -3.7346 | -59.4577 | 2024-10-28 00:15:27 | GOES-16 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| de6a9c3a-cf1e-3efc-ae0d-d434b120dfa9 | -3.9949 | -46.4867 | 2024-10-28 00:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 97c54d6c-088c-315b-918c-bcf1af39cdd1 | -4.0681 | -50.024 | 2024-10-28 00:15:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d95d96b8-9790-3e13-bcd3-e2c91d3186ac | -4.2797 | -45.5362 | 2024-10-28 00:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 86d4c143-1bc0-3019-a4fa-af869a841ea6 | -4.4093 | -45.6641 | 2024-10-28 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 133.9 |
| f24175e0-0322-3610-9fe1-85160a5828f2 | -4.4094 | -45.6416 | 2024-10-28 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 211.2 |
| a524cf76-767c-317c-b1b4-42db3b9f4454 | -4.4279 | -45.6631 | 2024-10-28 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 618e7854-7c0b-3f82-8806-f64b8ce65a14 | -4.428 | -45.6406 | 2024-10-28 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 176.3 |
| aa0a05b6-b844-3fd2-9af5-d41f3d64d4a8 | -4.4844 | -42.8866 | 2024-10-28 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f7aa5601-e042-395d-818a-5511f0dbf42d | -4.758 | -46.4033 | 2024-10-28 00:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 1b5b87ef-4f5f-3629-8d8f-9e3fe087bf2d | -4.7581 | -46.3811 | 2024-10-28 00:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 122.6 |
| fd88ad79-7c71-3495-a3cc-fa3fca7ba9b2 | -4.7766 | -46.4022 | 2024-10-28 00:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 211.3 |
| 62f62378-cdc5-30e8-bada-8711dcdb7ed4 | -4.7768 | -46.3801 | 2024-10-28 00:15:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 184.0 |
| bdb059ab-8de1-3dd9-aa17-3bc0d605d89f | -4.9496 | -43.2078 | 2024-10-28 00:15:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6ab674bd-b8b1-3f42-89e1-ebdb2cb1daf6 | -4.9683 | -43.2066 | 2024-10-28 00:15:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 10729fd1-3921-3dd4-9dd3-36303f2219fc | -4.9685 | -43.1832 | 2024-10-28 00:15:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b828a85c-3347-35ac-9a41-1d1f9422a2c4 | -4.9498 | -43.1845 | 2024-10-28 00:15:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b90c44a8-7442-31a1-8e2c-0343275d69c6 | -4.9262 | -49.0077 | 2024-10-28 00:15:33 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7dd44bef-42dc-36da-b11d-6ba4d79236d7 | -0.9815 | -53.699 | 2024-10-28 00:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e44ed55b-dfe5-3993-978c-75907817b271 | -1.0733 | -53.658 | 2024-10-28 00:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f789275e-fcc1-3180-943a-10941966c423 | -1.1653 | -53.4957 | 2024-10-28 00:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e1b60c9f-d677-35fe-a932-24d13ec1219e | -1.1836 | -53.5158 | 2024-10-28 00:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 05b56ab5-f35d-3c65-b80c-488a51a7634a | -1.1836 | -53.4956 | 2024-10-28 00:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 5acfd9b0-f684-3796-b5d8-4913b68874b2 | -1.5349 | -52.1079 | 2024-10-28 00:25:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 05e6efce-7e3e-3ae1-8b20-df128c5c02dc | -1.5349 | -52.0874 | 2024-10-28 00:25:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| f0c0e58f-b737-3176-9432-20465c3de291 | -1.5349 | -52.0668 | 2024-10-28 00:25:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| f4c2ef5b-cd9e-374e-ae88-e0582831a635 | -1.5532 | -52.1076 | 2024-10-28 00:25:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| ad55b52b-495d-3345-b897-726ea0b73827 | -1.5533 | -52.0871 | 2024-10-28 00:25:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 4ab080c3-06c6-349b-8737-46e1ffabe9f5 | -1.9763 | -52.0804 | 2024-10-28 00:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a2999af3-8be3-3219-b87e-038798b44657 | -2.0497 | -52.1611 | 2024-10-28 00:25:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 73963eda-9290-3da4-8707-b3f6140233cc | -2.0499 | -52.0791 | 2024-10-28 00:25:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6711532e-08df-33b4-aaa0-bbda1b20674d | -2.1826 | -50.6065 | 2024-10-28 00:25:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 984eee19-8d2d-37ee-b208-26410014330c | -2.2662 | -53.8027 | 2024-10-28 00:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 13703be2-3cbf-3f67-bab5-8c9d77101a14 | -2.2662 | -53.7825 | 2024-10-28 00:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 447.4 |
| ad1f4bb9-48f2-334f-bc75-c2425a7699af | -2.2663 | -53.7624 | 2024-10-28 00:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 1cf632b7-fdb2-3baf-9058-98d274757df5 | -2.2845 | -53.8023 | 2024-10-28 00:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 1dd2d1a9-6fcb-37cd-9e35-73ea67ec49d7 | -2.2846 | -53.7822 | 2024-10-28 00:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 237.4 |
| dfa2d6f1-0e50-3f81-a1c5-d28ea46ca14d | -2.2846 | -53.762 | 2024-10-28 00:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4bd29b00-5699-3d4b-abe4-efd062ad3c74 | -2.3919 | -48.5484 | 2024-10-28 00:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9e2dc27f-d8c6-3996-a9e8-249be426cb6e | -2.4104 | -48.5479 | 2024-10-28 00:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 50cad70d-3ce2-39b1-a740-13015fda46ca | -2.5126 | -51.2028 | 2024-10-28 00:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 60773d43-8a35-300f-b392-9f9a0d9a3f67 | -2.5127 | -51.1821 | 2024-10-28 00:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 92c86cad-460c-36ce-964a-62dbcb2e384b | -2.5127 | -51.1613 | 2024-10-28 00:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 98f4a3ed-dc89-3db9-bdff-d5a8de9ffc2b | -2.5251 | -47.442 | 2024-10-28 00:25:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 4e5b73fc-3f1d-35d3-9f82-074cc98a89a9 | -2.531 | -51.2024 | 2024-10-28 00:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1e150ac7-c9cc-3e42-a7be-c3cc885b8750 | -2.5311 | -51.1816 | 2024-10-28 00:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 3af93508-1544-34e0-8256-cb7fe02b517f | -2.5312 | -51.1609 | 2024-10-28 00:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 3e30ea28-302a-3aa2-928c-da776f544f95 | -2.6505 | -54.2971 | 2024-10-28 00:25:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 4ee4de85-8d77-360b-8c8d-ad63336d6274 | -2.7034 | -49.3088 | 2024-10-28 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 20c4e7d1-6538-366d-8887-903151c69314 | -2.8054 | -51.8157 | 2024-10-28 00:25:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| d76c1b75-1cb9-346b-a31b-b4e519c09e0a | -2.8054 | -51.7951 | 2024-10-28 00:25:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 0c09817f-8c75-3d4b-8bc4-5311d7dff312 | -2.8555 | -53.3459 | 2024-10-28 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6ba0d995-ab94-39b3-bc81-31a600880d8c | -2.8556 | -53.3256 | 2024-10-28 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ab321476-1323-3776-bb22-f1f393ab81e0 | -2.8739 | -53.3454 | 2024-10-28 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 2bcd196c-1657-3af4-b087-b7a16ef96de4 | -2.8739 | -53.3252 | 2024-10-28 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 9ea6229c-e6d5-3206-81fe-290d71fb9c76 | -3.0317 | -50.4176 | 2024-10-28 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 01521198-4d92-3fbf-a698-372436241c14 | -3.0353 | -49.4901 | 2024-10-28 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| d994f79b-0558-3f72-899e-c739ffaeb4ba | -3.0538 | -49.4895 | 2024-10-28 00:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c196ee9a-4c0f-3a04-b652-452006217ee7 | -3.2534 | -46.2079 | 2024-10-28 00:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4c9a9f42-2ec2-3067-accf-8aafab4bfa0e | -3.2719 | -46.2294 | 2024-10-28 00:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ca17cae6-8ee3-3f0e-a218-9f27867ad3ed | -3.272 | -46.2072 | 2024-10-28 00:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 129.0 |
| ac6bbd52-45cd-349b-89e0-9d336f4d0b1c | -3.4013 | -46.3353 | 2024-10-28 00:25:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c2013049-f28e-3eba-8b0c-0f6913e7405a | -3.4014 | -46.3131 | 2024-10-28 00:25:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2487a1b2-7aff-38f5-ab4c-e2cc69319df8 | -3.42 | -46.3123 | 2024-10-28 00:25:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 1bfd9b8b-f8f0-36cd-986e-638f2409b6a1 | -3.6727 | -51.5629 | 2024-10-28 00:25:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b65ac0f5-d64f-3ee1-98db-24a55e84396b | -3.6911 | -51.5622 | 2024-10-28 00:25:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| afb002b8-d654-338e-a01a-6d3416cd8c05 | -3.7346 | -59.4577 | 2024-10-28 00:25:27 | GOES-16 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e61828c4-d089-37a6-8da7-122a33450135 | -4.2797 | -45.5362 | 2024-10-28 00:25:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 232.9 |
| a204ce8b-0b61-3a11-8c1d-5bb99cb14f7e | -4.2799 | -45.5138 | 2024-10-28 00:25:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 87.9 |
| bab7da9d-7f48-3ca2-86dd-94b3bcae607b | -4.4093 | -45.6641 | 2024-10-28 00:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 19f32e58-65c3-3bc4-b4d4-5dc977474bf8 | -4.4094 | -45.6416 | 2024-10-28 00:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 3067806b-e2f1-3621-a59a-ab3c6466d3cb | -4.4279 | -45.6631 | 2024-10-28 00:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 886c088e-aa6c-3f57-8abb-837460cfb4e1 | -4.428 | -45.6406 | 2024-10-28 00:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 209.4 |
| 2bbd5b22-420c-378b-93d6-659e11a05720 | -4.7768 | -46.3801 | 2024-10-28 00:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 33476482-6f43-3f38-808b-bd62f4396156 | -4.758 | -46.4033 | 2024-10-28 00:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 4edf531a-3e69-3fd8-b496-caaa1b0e3edb | -4.7581 | -46.3811 | 2024-10-28 00:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b93de9ea-7377-3c18-90a6-b1c9fd0bbcad | -4.7766 | -46.4022 | 2024-10-28 00:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 205.3 |
| 72b7941c-e5cd-33e7-a009-34c7407d1155 | -4.9496 | -43.2078 | 2024-10-28 00:25:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| f2b4bc12-1eed-315a-ad1b-dd4df31c19e8 | -4.9683 | -43.2066 | 2024-10-28 00:25:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 997761c7-f7d0-3c29-83a2-f81f11476a41 | -4.9498 | -43.1845 | 2024-10-28 00:25:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d227d1f9-1877-36c8-80c9-3b3859f92a0b | -15.3686 | -40.1745 | 2024-10-28 00:26:30 | GOES-16 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 150.7 |
| 9a6c1bed-09cd-3a66-bd42-a3716bc6cf6c | -1.1836 | -53.5158 | 2024-10-28 00:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e340215c-77e0-37d8-a5ec-a492542059dd | -1.1836 | -53.4956 | 2024-10-28 00:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| d4b5f8f3-f8b8-38f1-9ff3-e3a66e307ac4 | -1.5349 | -52.1079 | 2024-10-28 00:35:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 9543bdd0-35bb-3caa-b9dd-c7525bf59d13 | -1.5349 | -52.0874 | 2024-10-28 00:35:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| e387f3c5-6ec1-3b2b-bff9-ed0d210d342b | -1.5532 | -52.1076 | 2024-10-28 00:35:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6b9cc46c-d069-39ac-b0a8-ebe376f6ee2d | -1.5533 | -52.0871 | 2024-10-28 00:35:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| c3e63b10-dc8f-335d-a951-a910438903da | -1.9763 | -52.0804 | 2024-10-28 00:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d402eb76-cc71-3c5f-8674-2153c20bd4c6 | -2.0497 | -52.1611 | 2024-10-28 00:35:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5c19717a-70bd-364f-857a-b7f65067c664 | -2.0499 | -52.0791 | 2024-10-28 00:35:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 1568dc1c-f3c7-3588-9fe0-03d2f885efe9 | -2.2662 | -53.8027 | 2024-10-28 00:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| c77c3afb-766e-3c05-9b57-3acb42dee9a6 | -2.2662 | -53.7825 | 2024-10-28 00:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 306.4 |
| 6a905abb-5bb3-3df2-b97a-d6f8180aa94f | -2.2663 | -53.7624 | 2024-10-28 00:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |


[Clique aqui para ver as próximas entradas](README3.md)

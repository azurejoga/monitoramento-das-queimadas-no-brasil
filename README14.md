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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c415ebe0-f69a-363f-9f3f-a83e4669a66c | -3.0192 | -53.8668 | 2024-12-03 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9c5e22cf-9b42-33c0-a58e-363ee63077d9 | -3.1831 | -54.3247 | 2024-12-03 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6212a460-aed3-314d-897e-36936979aecc | -3.2775 | -53.6181 | 2024-12-03 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d5c99c5d-2d96-3937-b3a6-24153b050db3 | -3.3422 | -51.2007 | 2024-12-03 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| aa7f94e0-3f66-36cc-8c43-a88fb00a8eb3 | -3.5497 | -50.1699 | 2024-12-03 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 6e5800b2-07f8-3374-845d-89ca3f4714ab | -3.0376 | -53.8664 | 2024-12-03 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ec7a699e-9ef1-3bbc-8690-484477870549 | -2.8396 | -52.5941 | 2024-12-03 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d4d3c53d-d3b3-3950-945d-995f3056fa11 | -3.0761 | -53.3606 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 2c00d650-2ca4-3532-bdbb-82222df63671 | -3.5496 | -50.191 | 2024-12-03 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 83ff0407-3d71-3a57-8941-655a0dc4fc68 | -2.8212 | -52.5945 | 2024-12-03 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b9aafc41-f980-33ed-ac82-3f2ead38be82 | -2.8212 | -52.5741 | 2024-12-03 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c4a92bc1-cb1d-33ae-abba-e6ee2f848c01 | -3.5682 | -50.1693 | 2024-12-03 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 8bfbc602-9547-3904-a12c-0f6c2d73e175 | -2.8396 | -52.5736 | 2024-12-03 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 52cac4b5-4a5c-3618-a049-0cfee15ffbe7 | -3.076 | -53.3808 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 183.2 |
| 9a620b32-7746-342c-8ea0-446960331bf6 | -2.8013 | -53.043 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0e7b3bbb-7bfc-37d2-af0e-db1e37a0b2dc | -5.8009 | -46.4941 | 2024-12-03 01:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 73d93cb3-dc7d-3172-a866-c0420fcc1c31 | -1.7361 | -52.6366 | 2024-12-03 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| f22b03ca-8a86-3307-8b88-19666e1f3dc5 | -2.3459 | -45.7036 | 2024-12-03 01:10:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 5e5c6693-89e5-350f-bf98-d2c25b54c178 | -3.2591 | -53.6186 | 2024-12-03 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| d55c3333-5550-33c5-842e-d1b92ece20be | -2.8196 | -53.0629 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 78e7b095-2245-3565-b565-c1acb8d010d4 | -3.259 | -53.659 | 2024-12-03 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1a7ad199-c7b4-3b70-8421-a9abe021aad3 | -3.272 | -50.3263 | 2024-12-03 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8df1ecf3-ccb0-3f73-8eb0-53a0b2b520b0 | -2.3645 | -45.7031 | 2024-12-03 01:10:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| fd33ffdd-77f5-333c-b13e-d07d74c642bc | -4.5402 | -42.93 | 2024-12-03 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 43b5f3e5-dff8-3d99-b2a3-68e139937176 | -1.7541 | -52.7993 | 2024-12-03 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 0f629093-b459-306c-a122-1b5c86e31b22 | -1.736 | -52.657 | 2024-12-03 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 51daff05-4323-3f6c-a162-773613cee522 | -3.2774 | -53.6383 | 2024-12-03 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 054922e8-1685-382f-90b2-0acf6f9b2fcc | -3.0944 | -53.3804 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 6c9e0524-c6b7-352e-9d5e-757b1918313b | -2.8012 | -53.0633 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| dd85c951-237c-3f59-8ad7-ce8c806e23f0 | -4.5589 | -42.9289 | 2024-12-03 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2ad39a01-392a-3c86-bec9-b428b78348bc | -3.0761 | -53.3606 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| d1c06328-ca8b-388b-a429-ce6a54c272ad | -2.8212 | -52.5741 | 2024-12-03 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| e0fd7d1b-ce73-32c8-98b8-2e354f2def8d | -2.2111 | -53.7835 | 2024-12-03 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e722c35f-8804-388c-be58-8006ebbc57f2 | -1.7361 | -52.6162 | 2024-12-03 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6a573064-0701-32a8-9ff5-c0c9e170ecb5 | -3.0376 | -53.8664 | 2024-12-03 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| a3a964e0-2143-32ce-9ca4-84d7e17b556b | -3.5497 | -50.1699 | 2024-12-03 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| e5d4058f-c53f-3b0d-8a77-de93c71517af | -3.259 | -53.6388 | 2024-12-03 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| edf3062e-6f37-3d10-b9ef-4a1732a3c9f8 | -2.8197 | -53.0425 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b4874c92-3f46-391b-8b5a-b475aa5c96e5 | -3.2774 | -53.6383 | 2024-12-03 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 0786dc34-d764-32f8-8522-3f98455cac4c | -1.7361 | -52.6366 | 2024-12-03 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e032b023-f516-37ea-911f-c4c938f6b4d9 | -2.3459 | -45.7036 | 2024-12-03 01:20:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 8265fe80-e224-3877-9734-cd4f7014a931 | -2.8196 | -53.0629 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ab5dcbf9-42ae-3650-a3f9-507d9e3aa738 | -6.1229 | -43.9578 | 2024-12-03 01:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e243cc2e-a456-3db6-9e5c-527cc656932f | -2.3396 | -53.8013 | 2024-12-03 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 1d6d4673-4b41-3f73-ac0f-271bbd1ea163 | -2.8212 | -52.5945 | 2024-12-03 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 50eea94e-afcc-39ab-a76c-473068c3b774 | 2.7267 | -60.3916 | 2024-12-03 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f66b8222-ae12-390f-a9e2-d2886103fd9f | -3.5682 | -50.1693 | 2024-12-03 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e157e157-065f-3ce4-b0d4-34c804df5403 | -3.076 | -53.3808 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 180.3 |
| 648d2212-bc1b-3203-a940-f5f45a373fe4 | -3.076 | -53.4011 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 343d25f9-7a80-3851-86af-9f0a8940be1e | -2.8013 | -53.043 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9d8db677-59f6-35f2-ad50-12731f2ade1a | -3.259 | -53.659 | 2024-12-03 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 2b84b80c-5164-327d-a853-85ba2d0c2053 | -3.2905 | -50.3257 | 2024-12-03 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c3b4f379-457a-36f5-80a2-688445e2b5a7 | -3.2591 | -53.6186 | 2024-12-03 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 457903a6-4b2a-36d0-95db-2992f6768692 | -3.0949 | -53.2385 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| bc8f1f45-7b73-3575-a5e3-512ffad00c17 | -5.1552 | -43.2406 | 2024-12-03 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 55487ec1-5a86-3205-bf62-d783ad484cea | -3.2775 | -53.6181 | 2024-12-03 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| d50a6d73-2bc4-321f-8e56-103f1f3fc5c2 | -5.801 | -46.4719 | 2024-12-03 01:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 49e65c40-8660-3d8f-9a84-c30d13b8298a | -3.3421 | -51.2215 | 2024-12-03 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4e3f25aa-0b00-3ff6-960a-0ed61793a92b | -3.183 | -54.3448 | 2024-12-03 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 91550056-7a2d-39be-abc8-ca1c231ca6bd | -5.8009 | -46.4941 | 2024-12-03 01:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d6779066-4932-3546-be88-900830af4a63 | -2.8396 | -52.5941 | 2024-12-03 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b460f2d5-2d0f-3183-9f84-45558975d3a7 | -4.5402 | -42.93 | 2024-12-03 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 59e95f47-81bd-326e-9dca-3e4714cf01b3 | -2.8396 | -52.5736 | 2024-12-03 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 0bcc398e-6844-38cf-b57e-5c9226d77286 | -3.0944 | -53.3804 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 2fef74e4-7d2e-36ec-9dfd-edc810e7606e | -5.1365 | -43.2419 | 2024-12-03 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e8e53e36-6230-372a-9395-f1749a3399bf | -3.2406 | -53.6595 | 2024-12-03 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 34ee2e72-95c4-3bab-83dd-9002b040fc47 | -5.8197 | -46.4706 | 2024-12-03 01:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 83deb4ad-82c5-358b-8efb-8860be6966a7 | -3.5496 | -50.191 | 2024-12-03 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 60cb40cb-0ff8-31c7-bbb4-37ef8e3ab4be | -1.7541 | -52.7789 | 2024-12-03 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 7e4ff99b-ddf1-36c2-9ee1-75a12de35a41 | -5.8195 | -46.4929 | 2024-12-03 01:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 04f3af17-c527-3a07-98aa-c8275f436060 | -1.7541 | -52.7993 | 2024-12-03 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3e90ebba-2b67-38b0-bbec-1e3f7a05518d | -3.5681 | -50.1903 | 2024-12-03 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ccf1bb65-1800-3c2a-94ec-fa0931444498 | -3.3422 | -51.2007 | 2024-12-03 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e889aacb-ad6d-3d79-bb09-0df8250f6306 | -3.0945 | -53.3601 | 2024-12-03 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 497fa0ad-b43b-3ce0-88b4-979a1a1dcb17 | -3.7715 | -43.3233 | 2024-12-03 01:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| abe573ca-0b46-3422-947e-401e9c2b984b | -2.8396 | -52.5736 | 2024-12-03 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 0f26f1bb-4493-39be-8e1c-4a78920e66e4 | -5.8197 | -46.4706 | 2024-12-03 01:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 884a7c5d-ce0b-3c03-802e-bf6aef5f6a60 | -4.5402 | -42.93 | 2024-12-03 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 57db7c23-52cd-3107-b681-48c4e931b628 | -2.7377 | -45.2201 | 2024-12-03 01:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5ae1eb54-c722-31ac-a64c-23a5cfcc7200 | -6.1229 | -43.9578 | 2024-12-03 01:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 03a2c6d8-469a-3069-8fb7-5391d0d77aec | -3.076 | -53.3808 | 2024-12-03 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 390ad300-3a0c-3def-9fb1-f81bd1756834 | -3.259 | -53.659 | 2024-12-03 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| bfb7fcb5-2cb7-3185-b0af-f7d12732d730 | -3.5496 | -50.191 | 2024-12-03 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 901d60b5-6405-335d-9522-97c5fa4e4600 | -3.0761 | -53.3606 | 2024-12-03 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 9032aeea-3bac-3812-9541-b33fc1b94dfd | -1.7541 | -52.7789 | 2024-12-03 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8df86f87-c63c-3927-b543-48d8b9b5c65f | -2.8212 | -52.5945 | 2024-12-03 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cbe95420-6bd0-3f85-b26d-1e4f8e19fd80 | -3.0376 | -53.8664 | 2024-12-03 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| efe9f5d5-94d7-309e-a26d-05b8bfbe3f35 | -3.183 | -54.3448 | 2024-12-03 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 41033b9a-1a34-38f5-8928-880a605efe91 | -1.7361 | -52.6366 | 2024-12-03 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| dee1f909-5b5b-3c56-94a1-3b9fa87ba139 | -2.8012 | -53.0633 | 2024-12-03 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0ff43d25-fbcd-31f6-b70b-ba6f4ea2839d | -3.5497 | -50.1699 | 2024-12-03 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| bb7b1129-dd5a-3d60-8846-8bed3c61b969 | -3.0944 | -53.3804 | 2024-12-03 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 3d372618-88c0-33bc-b54c-3a9bb79e603a | -2.2111 | -53.7835 | 2024-12-03 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 97793576-42f0-330f-ac41-d2c52b2083df | 2.7267 | -60.3916 | 2024-12-03 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 285ea587-e067-3b2a-86d6-96ff770c2996 | -1.8239 | -46.6045 | 2024-12-03 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| cc3e2deb-b266-3820-bf93-b0e975b3c23e | -5.8195 | -46.4929 | 2024-12-03 01:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0538cf7e-3056-362e-a3e9-094a5cdd7044 | -1.8053 | -46.649 | 2024-12-03 01:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 24258c7a-bfbf-3b2c-a5de-2132eee30414 | -2.8212 | -52.5741 | 2024-12-03 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6460a5c1-ba67-361c-9942-a32ae6e99af4 | -5.801 | -46.4719 | 2024-12-03 01:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| ac9a474d-cc3c-3c7b-b749-400d57ee6a60 | -3.0945 | -53.3601 | 2024-12-03 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |


[Clique aqui para ver as próximas entradas](README15.md)

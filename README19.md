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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feb413e1-e94a-3e7c-bc52-4573ea8ed994 | -2.2111 | -53.7835 | 2024-12-03 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 1250c625-b244-3841-98ee-d0f7c1d7682e | -2.7191 | -45.2208 | 2024-12-03 02:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 50251d68-7d2d-3f84-9e41-50b13b9311ab | -3.0761 | -53.3606 | 2024-12-03 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1fd8d4d6-e9eb-38a3-a19b-639ec1059103 | 1.1072 | -55.9874 | 2024-12-03 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7dcaa078-4c24-3edf-ac95-2781f385de0c | -2.7192 | -45.1982 | 2024-12-03 03:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a2abae12-5aab-3bb1-ba57-4464fa92f8c1 | -2.7377 | -45.2201 | 2024-12-03 03:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f050f500-af68-3585-8e4f-7532fcfef6a8 | -2.8485 | -45.3963 | 2024-12-03 03:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.1 |
| a3e1b414-b1c6-36d3-a341-904c575c421c | -5.7824 | -46.4732 | 2024-12-03 03:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c837113d-9b7b-34c5-84d9-f7ab89ba795b | -5.8009 | -46.4941 | 2024-12-03 03:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 953f27b6-ef6b-329a-b62b-8f80214d6ac3 | -2.8012 | -53.0633 | 2024-12-03 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8c8e071f-599d-3511-8f1e-7dd61f6701d4 | -1.0919 | -53.4359 | 2024-12-03 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0a72793b-5770-37d9-a07b-1973fd98f7d9 | -2.2111 | -53.7835 | 2024-12-03 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 493617a1-6b09-30bc-b4d1-05a41c4b703e | -1.8053 | -46.649 | 2024-12-03 03:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| d13fe691-9320-3e70-9b94-943e3947724f | -1.0919 | -53.4561 | 2024-12-03 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 185.3 |
| ac2061b6-cdd6-3b10-a319-7912427e5789 | -5.1365 | -43.2419 | 2024-12-03 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| d39b6521-f2ba-37de-8595-29147d54499d | -5.118 | -43.2198 | 2024-12-03 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8037dc37-b92a-335a-adf9-3d9f1a08e101 | -5.1552 | -43.2406 | 2024-12-03 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ff0397b9-0760-3c8e-ada5-bf112392878a | -2.8196 | -53.0629 | 2024-12-03 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 3ecfa9b2-bb2a-3b93-8647-c745e370cd79 | -5.8197 | -46.4706 | 2024-12-03 03:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a7dc26a3-6ebc-38a0-a92a-4050edb0582f | -5.801 | -46.4719 | 2024-12-03 03:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 8e85806f-0157-3d67-a3c0-dc1b48ab3995 | -5.8195 | -46.4929 | 2024-12-03 03:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 3a14b987-e5d9-36b6-8e11-c5cac78efd31 | -5.1367 | -43.2185 | 2024-12-03 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a210058e-f889-3df7-8871-592929da3eee | -2.8013 | -53.043 | 2024-12-03 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 65c2f376-e220-399c-a1b3-59bc14f0d728 | -2.8197 | -53.0425 | 2024-12-03 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 44627451-45c7-3bb2-b87f-198ed4ab6954 | -3.076 | -53.3808 | 2024-12-03 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 180.6 |
| 9c075f8f-1103-38dc-bb42-7e89991746d1 | -5.1181 | -43.1964 | 2024-12-03 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 130d2f46-526b-3a52-903d-9a29dc45a11d | -1.0735 | -53.4562 | 2024-12-03 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 82b9cb25-cfa3-3a7b-827c-dbbe296b84ae | -3.0944 | -53.3804 | 2024-12-03 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 609941e2-4af2-34d2-bddc-d875d7d78040 | -2.7378 | -45.1976 | 2024-12-03 03:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 51c60015-4bcd-3e1f-9512-73933496e65d | -1.0736 | -53.436 | 2024-12-03 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| fc693ebe-9651-3772-ab86-cfd6bbe84b0d | -5.81 | -46.48 | 2024-12-03 03:00:00 | MSG-03 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00670122-9ad3-3d7f-bfe2-6bda7ab026db | -5.1181 | -43.1964 | 2024-12-03 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c4ce9f08-20c6-35e3-ad36-d11828d3beb2 | 1.1072 | -55.9874 | 2024-12-03 03:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 8380fb3c-2591-3747-949f-31682f43a124 | -1.0919 | -53.4561 | 2024-12-03 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 16132017-e616-3e11-9daa-8f0911d2542c | -3.2591 | -53.6186 | 2024-12-03 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 95f9e306-9776-33bd-993a-3cf2f5ab3926 | -1.8053 | -46.649 | 2024-12-03 03:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| a7738b22-8155-3d04-806d-fc49f4a4de80 | -2.2111 | -53.7835 | 2024-12-03 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e11aee5b-ad9e-3cfc-9fe2-e3cc98907308 | -3.2775 | -53.6181 | 2024-12-03 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d4b53264-05ae-3193-96b7-251158e269d1 | -2.8013 | -53.043 | 2024-12-03 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9d940451-7529-3a8c-8804-aee59e056d6e | -5.8195 | -46.4929 | 2024-12-03 03:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 9c890806-af37-3c9e-9382-e5e1092f2d11 | -5.118 | -43.2198 | 2024-12-03 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| a818ba0c-f5f6-3735-9f7d-63c89241de70 | -3.259 | -53.659 | 2024-12-03 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| fbadd946-f675-3a51-9077-b37103f59259 | -3.2589 | -53.6792 | 2024-12-03 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| fa158dec-1b57-3269-ac37-b46c857e91be | -3.347 | -46.0486 | 2024-12-03 03:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 6bd2467f-01e5-3e26-b643-76026df858ae | -2.8012 | -53.0633 | 2024-12-03 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9c8866d1-a977-30d1-9bdb-e9c7fdc3aed8 | -2.8197 | -53.0425 | 2024-12-03 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 7ef83963-5820-3153-8e36-d25e7174dec5 | -3.076 | -53.3808 | 2024-12-03 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 56f552bd-f54c-395a-ad0b-5fd3c2b2012c | -1.0735 | -53.4562 | 2024-12-03 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 743428da-0717-3329-ba8c-f263b4689bf1 | -5.8197 | -46.4706 | 2024-12-03 03:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 839c2f92-858d-3023-8671-90379faf067b | -3.0944 | -53.3804 | 2024-12-03 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| a1e3b067-2bdf-3bee-a2be-886a786f6241 | -2.8196 | -53.0629 | 2024-12-03 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ca451787-6972-308f-b110-fe2ea09ce926 | -5.801 | -46.4719 | 2024-12-03 03:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 222.1 |
| cbcef830-cbd9-3d29-9d6b-a1dd0d4f5d4f | -5.1365 | -43.2419 | 2024-12-03 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 06a6c44a-3a94-3fc0-82ec-9b2497d03e64 | -5.1367 | -43.2185 | 2024-12-03 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ea69b9cb-4db5-3495-a758-5b7317468949 | -2.8485 | -45.3963 | 2024-12-03 03:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e002fbda-0245-331b-a580-77b6e1665b5f | -1.0736 | -53.436 | 2024-12-03 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e8989e12-1fbb-347a-82fa-71fdb041a58c | -3.2774 | -53.6383 | 2024-12-03 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c5ed65a5-8ac3-3043-92f5-f823cfd2c1b9 | -3.259 | -53.6388 | 2024-12-03 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| fce04291-066c-3e63-a650-0bac2abd7a66 | -5.8009 | -46.4941 | 2024-12-03 03:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 52e51340-bd4c-3302-8967-c7b474508d1f | -1.0735 | -53.4562 | 2024-12-03 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 359c407c-8607-3cd5-8b55-1c51079f81b3 | -3.0945 | -53.3601 | 2024-12-03 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5e08c478-024f-369a-afc6-c860ad3f585e | -1.0736 | -53.436 | 2024-12-03 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 441773dc-9101-3bf3-ae84-3b215cd69c4f | -5.1181 | -43.1964 | 2024-12-03 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b277e926-0581-37bd-88d6-d25811b86bcc | -3.2774 | -53.6383 | 2024-12-03 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9f421bc2-d4d3-31ef-8b7c-49034fc1bb67 | -5.118 | -43.2198 | 2024-12-03 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 29a7cb6e-d7c9-39f8-8603-0986734e5927 | -5.1367 | -43.2185 | 2024-12-03 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 0e6ba69b-3564-359e-8484-6ac9636985ab | -2.8012 | -53.0633 | 2024-12-03 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0194c03e-f4a9-33e5-9b02-508f05a59502 | -3.2775 | -53.6181 | 2024-12-03 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 7967e2cd-ff76-3f7f-a849-7d7fc6c7004c | -3.259 | -53.6388 | 2024-12-03 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2ee7240e-40e3-3414-96de-070b63e449ba | -2.8485 | -45.3963 | 2024-12-03 03:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 8c82e5b7-ebcd-30ed-b6be-9a8f7bcbe036 | -2.8013 | -53.043 | 2024-12-03 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2a47edf4-11de-38ee-9146-9e6684d13663 | -3.0944 | -53.4006 | 2024-12-03 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8a8126b0-b90e-3ea3-abea-ad257789cb66 | -2.2111 | -53.7835 | 2024-12-03 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ce320e16-f6be-3dd8-8e98-276753cc36d7 | -2.8196 | -53.0629 | 2024-12-03 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| d2e5471f-59a3-39df-8a59-b13dd06f3a79 | -5.8195 | -46.4929 | 2024-12-03 03:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2c744c26-468c-36ed-a721-5230b93104a8 | -4.1914 | -51.1914 | 2024-12-03 03:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| b8bcc7be-edf1-32c2-9496-5c99c5df2543 | -3.2591 | -53.6186 | 2024-12-03 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 7e302738-6b98-3038-8e55-cfef4306479d | -5.801 | -46.4719 | 2024-12-03 03:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 4a65e0a0-ffd9-3da8-bf81-473232bd191a | -1.0919 | -53.4561 | 2024-12-03 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| d88e384e-2e22-3f02-836c-bb4ad6236ec1 | -5.8009 | -46.4941 | 2024-12-03 03:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 506ffe7f-4868-3b17-a79e-f655e6a1b6dd | -3.0944 | -53.3804 | 2024-12-03 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 855d11ab-05b7-3ba0-ba2c-91d681b9e24d | -5.1365 | -43.2419 | 2024-12-03 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 208a8f24-a700-3f2e-8fe4-db3b6d7a706f | -3.076 | -53.3808 | 2024-12-03 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| eb2c242f-58a6-3760-86bc-3079e88cdcea | -2.8197 | -53.0425 | 2024-12-03 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| fac31cde-d952-30b0-9735-69b9e9817c74 | -3.347 | -46.0486 | 2024-12-03 03:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 92217501-7c9b-3874-a770-74fb1fd59c94 | -5.8197 | -46.4706 | 2024-12-03 03:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 5461e860-c20b-3ed2-9213-7d2484229b67 | -3.259 | -53.659 | 2024-12-03 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 7cc0ca91-6df0-3aee-8d07-3f48e549a9b0 | -3.2774 | -53.6383 | 2024-12-03 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0449455f-b7b0-382d-b911-14a7d2ee3eff | -2.8013 | -53.043 | 2024-12-03 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 149b214c-0b1f-3a3d-842a-95b08e3fea09 | -3.347 | -46.0486 | 2024-12-03 03:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| adc8ad0c-07a0-32d6-a4f2-617e97342a84 | -4.1914 | -51.1914 | 2024-12-03 03:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e9c7350e-71e9-3211-8677-0f35f643baf6 | -5.8197 | -46.4706 | 2024-12-03 03:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 7ae13094-26da-38dc-8416-241d159576b5 | -5.8195 | -46.4929 | 2024-12-03 03:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4d516f23-484f-364b-b559-ed4d704c1c9e | -5.1181 | -43.1964 | 2024-12-03 03:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 02b474dc-9afb-3fe5-a4e0-6245bcd2b75c | -3.076 | -53.3808 | 2024-12-03 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 89826c25-aba6-3401-bbae-05ddf075ff43 | -3.259 | -53.6388 | 2024-12-03 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 23a7e278-2f4d-34f3-937b-87059caac3aa | -2.8485 | -45.3963 | 2024-12-03 03:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c8bc9a39-61c5-3d55-ba15-5f11d8be01ae | -1.0919 | -53.4561 | 2024-12-03 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| fd272dcc-2ddf-3483-95a1-38dabf58691b | -5.118 | -43.2198 | 2024-12-03 03:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| fef1d1d1-9a89-3858-8f59-6e343914bb96 | -5.8009 | -46.4941 | 2024-12-03 03:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |


[Clique aqui para ver as próximas entradas](README20.md)

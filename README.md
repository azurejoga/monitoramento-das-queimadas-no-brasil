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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2306008f-9472-3b17-b94c-167885aae139 | -1.4762 | -54.1964 | 2025-01-15 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f54dca27-306d-3041-a2a7-fc32b2b7c7ea | 2.0856 | -61.8168 | 2025-01-15 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 3e4a7985-9865-36d0-8997-59258a09428c | 2.1039 | -61.8166 | 2025-01-15 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 211.0 |
| ce87c566-68a9-3404-9d21-2b234d24ecd3 | 1.3217 | -60.4452 | 2025-01-15 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 9ac07ac9-2479-3bfb-9a4f-f385f7a0151e | 2.1038 | -61.8354 | 2025-01-15 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 107.9 |
| dbb2c172-af1f-3493-b5cd-61c285c3fe0f | 1.3217 | -60.4262 | 2025-01-15 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.9 |
| fabd22c7-57bd-3c83-aee2-32b3da25b475 | 2.0857 | -61.798 | 2025-01-15 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 83e85fa5-8610-3d30-934f-c12511863e18 | 2.0856 | -61.8356 | 2025-01-15 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| a41b2d56-4b71-36ea-9fcb-836160bed6eb | 2.1039 | -61.7978 | 2025-01-15 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 75367d4f-a849-3ae4-b6d4-c116d855633e | -2.5104 | -51.9258 | 2025-01-15 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| b5d6d0d7-1960-3f0e-b5a5-41c47a5de836 | 2.0856 | -61.8356 | 2025-01-15 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1be12e3d-e398-30e0-8e90-a3350df9fccc | 2.0856 | -61.8168 | 2025-01-15 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 6f05c50c-3474-3404-8a2a-f53e5cd14cf9 | 2.1038 | -61.8354 | 2025-01-15 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 181bd796-368d-387a-873c-8dc686d38d6f | 2.1039 | -61.8166 | 2025-01-15 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 236.8 |
| 4f47b6e7-aff7-3fb2-99fd-2af60b858575 | -2.5104 | -51.9258 | 2025-01-15 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2515ed00-30f7-3ca0-8dad-e50f35e68a4b | 2.1039 | -61.7978 | 2025-01-15 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ec5ff048-b27e-3e66-885d-0179c43184d2 | 2.1039 | -61.8166 | 2025-01-15 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 232.7 |
| 3803f0e7-8d65-3970-bc7a-34d957691ac4 | 2.1039 | -61.7978 | 2025-01-15 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b77a8e73-7483-34af-ad55-9dda1a7da448 | 2.0856 | -61.8356 | 2025-01-15 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| cea06f33-a1bf-3547-b57a-1ee8cb46a11d | -2.5104 | -51.9258 | 2025-01-15 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f2c0f8b1-b9c5-3d84-9b08-c65fa39f3b62 | 2.1038 | -61.8354 | 2025-01-15 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 254bba48-c90b-3ad9-ae44-70513fd75bb6 | 2.0856 | -61.8168 | 2025-01-15 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 3d2a41da-ebe2-3d96-b475-cf2df3e4a16c | 1.3217 | -60.4262 | 2025-01-15 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 79a741dc-ce6c-3250-b2a2-1f6945e297ae | 1.3217 | -60.4452 | 2025-01-15 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 15dc5b16-4d47-3ec5-96c5-6ff2933c597c | 2.1039 | -61.8166 | 2025-01-15 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 20692ce2-8fdf-35a8-88c7-48137a5be769 | 2.0856 | -61.8168 | 2025-01-15 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 79886723-dba8-34b2-a1e4-3d1223c409f6 | 2.1038 | -61.8354 | 2025-01-15 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 8ee60742-dfe6-3448-ae59-5e951c1e9e1e | 2.1039 | -61.7978 | 2025-01-15 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ff68b62f-ef79-3d0d-9b02-d970ec0e70aa | -2.5104 | -51.9258 | 2025-01-15 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 967f620f-55b8-3ec7-9c58-271dc2066fd9 | 2.1039 | -61.8166 | 2025-01-15 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 176.7 |
| dea0eba0-47cc-308f-a43d-24118f0388e9 | 1.3217 | -60.4262 | 2025-01-15 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1ca4b1e4-4ea3-3dcc-a55f-1a30b1ad4a81 | 1.3217 | -60.4452 | 2025-01-15 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 66831b1d-d9cd-3669-a598-854765d2931b | 2.1038 | -61.8354 | 2025-01-15 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 85096c73-c7d7-3eb2-bffd-a9fd4d058da7 | 2.0856 | -61.8168 | 2025-01-15 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8fdd15e2-4da6-3ccd-9b69-fcf103cc84e6 | -21.4554 | -48.623199 | 2025-01-15 00:47:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 618947cf-8908-3e85-a816-8e4276f2cb08 | -3.314 | -53.874599 | 2025-01-15 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76be1caa-4367-3d6a-b066-39e7a5af069d | -21.4534 | -48.614601 | 2025-01-15 00:47:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| abcbf002-6306-311e-8def-216be03c2f88 | 2.0945 | -61.832199 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e6d4dc1f-33aa-3b2e-84ad-a385fbbadf9c | 1.3153 | -60.4212 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fa2b6a42-25dd-3f1a-9ade-d61e92bb3dbb | 1.3193 | -60.4491 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dd9bc845-7295-3335-8193-ec327e7a348b | 0.6574 | -59.599602 | 2025-01-15 00:49:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 75cb24c6-59b4-329e-8ad1-a3c4d2636072 | 2.087 | -61.82 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 746f7123-23b0-37a3-bc59-f6711c62f6c7 | 2.2789 | -60.214199 | 2025-01-15 00:49:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b277580c-f728-3626-b9a6-af9928748937 | 1.3114 | -60.438301 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a353af02-c03b-3bd5-8c86-cad85535b61d | 2.277 | -60.222301 | 2025-01-15 00:49:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 741967bc-3cbe-33fd-a47e-05e7d5017f76 | 1.3095 | -60.446899 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d48a2186-adf1-3e78-b319-c7ba1e427ddb | -2.5085 | -51.927399 | 2025-01-15 00:49:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54176e75-81a6-3c3a-8615-111d982dcf1a | -2.5106 | -51.9366 | 2025-01-15 00:49:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c70cca9-4f09-31f2-ae10-d05d7d64b575 | -2.5127 | -51.9459 | 2025-01-15 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eae6cd3-034a-39f4-9af7-a0c9600f8de4 | 2.0847 | -61.830002 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 630d4c32-5780-3348-bf02-403f12d35467 | 2.0922 | -61.8423 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 66751656-7eee-3569-b816-ea1f0f2f9399 | 1.3188 | -60.043201 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4a260c-5aef-3b43-8bbc-750aec058644 | 2.0968 | -61.822201 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef5a90a-5fd7-30d7-bc7c-19bf3041c4de | 2.0801 | -61.850201 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fd612acb-d375-375f-aa3f-aa11d8c2537d | 1.3207 | -60.035 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 73f4cd1b-369a-31a9-9fbe-4f01f71e72a9 | 3.2224 | -60.188099 | 2025-01-15 00:49:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 167567aa-729c-3aa7-9c48-caac6cc2040b | 2.0991 | -61.812099 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 81f065db-07f7-3107-b06c-6f8952fdee96 | 2.0899 | -61.852402 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 333e2dcd-a873-35db-af8b-75775f90ad1d | 1.3212 | -60.440498 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aff53eb7-5a91-349f-bcee-5d1283609c18 | 1.3403 | -60.039398 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3644470d-18a4-3927-9d20-35aea7d309ab | 1.3421 | -60.0312 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 46f3e8e3-e36f-318a-a613-6d1da3694088 | 2.0893 | -61.809898 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c577c8d1-e900-35b6-ba9d-622a3c4c3947 | 2.0824 | -61.840099 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e6f8a962-d908-3d04-a8c6-2439d54785e6 | 2.2752 | -60.230499 | 2025-01-15 00:49:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f74ee492-1fa6-31f3-82d3-a4a096bb3369 | 1.3134 | -60.429699 | 2025-01-15 00:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 61f0f515-c293-3c91-ba46-aa620763c72a | 4.245 | -60.673302 | 2025-01-15 00:49:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 876a5e93-d1f1-36af-9361-90084f1bfde7 | 2.1043 | -61.8344 | 2025-01-15 00:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 521eae8d-0af1-3d65-942e-899fbc8995fb | 2.1038 | -61.8354 | 2025-01-15 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 75bb6981-adc6-3bbc-8c4a-5e24df44a25e | 2.1039 | -61.8166 | 2025-01-15 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 64258082-d750-34bb-9614-30528007213d | 2.0856 | -61.8356 | 2025-01-15 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ec16f4ef-3385-3dca-92ff-25b5a3152df6 | 2.1039 | -61.7978 | 2025-01-15 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 17ffcbfd-608c-3ac0-97c5-591c2a5b15f6 | -2.5104 | -51.9258 | 2025-01-15 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f56d9e24-cbe5-3691-bdf3-1e4d99431cef | 2.0856 | -61.8168 | 2025-01-15 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d2f353ef-3ab5-3c1b-bca4-09b797a07d26 | -21.45196 | -48.60518 | 2025-01-15 00:52:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| 67a2303b-6b6c-3ae8-a18f-ba4bf61c96d3 | -22.10526 | -49.63263 | 2025-01-15 00:52:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 90793d70-24e8-3252-a948-e41fc296d751 | -21.45328 | -48.61575 | 2025-01-15 00:52:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 206ddd40-04ce-34da-81f6-de997ea8dff3 | -21.44519 | -48.60139 | 2025-01-15 00:52:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| eb4051eb-c592-3fd9-b88e-1428c5b78117 | -21.74551 | -50.82182 | 2025-01-15 00:52:00 | TERRA_M-M | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 77973044-b0b2-3070-b2e3-897a11f81908 | -21.44655 | -48.61192 | 2025-01-15 00:52:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b87f602e-10d9-3686-8d73-3f15bea73036 | -2.51643 | -51.91631 | 2025-01-15 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 09a39fd9-a6b3-306f-be83-676ca1669202 | -2.50868 | -51.92686 | 2025-01-15 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| a77adf19-9445-3504-8fa9-79d994e70144 | -2.5177 | -51.92556 | 2025-01-15 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2eb08bf7-d470-3d2e-b4e6-5ed49d429fc3 | -2.50741 | -51.91762 | 2025-01-15 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3b1bf2d9-2627-33b0-a11d-8ae673e18353 | 2.28359 | -60.23409 | 2025-01-15 00:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.3 |
| d511be79-dbf6-3e2e-bd2c-e5f3ebf8dd55 | 2.0903 | -61.81996 | 2025-01-15 00:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 99.6 |
| bf85a58e-8e7a-3796-b23f-5e903da1a871 | 2.28812 | -60.2048 | 2025-01-15 00:58:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 451e4d9f-a402-3ca6-8751-63d8441a88a1 | 1.32422 | -60.03043 | 2025-01-15 00:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.7 |
| b24d3886-e1e6-30ca-acca-1dcb25a65775 | 2.10765 | -61.822 | 2025-01-15 00:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b070678c-f3de-3546-9ee4-a2aa2d6efc05 | 2.28657 | -60.22953 | 2025-01-15 00:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 99fb0625-7fb8-3926-a4c7-88d23a53d867 | 2.10564 | -61.81686 | 2025-01-15 00:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 910df8d0-2acd-3f76-ae27-6634c6b633a8 | 2.08828 | -61.8149 | 2025-01-15 00:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 061cae1a-231a-3d03-972e-09aacdf36854 | 1.32689 | -60.44092 | 2025-01-15 00:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8ed30b5e-b2fa-395b-b680-1d43541a9b8a | 2.29089 | -60.20004 | 2025-01-15 00:58:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 32.5 |
| c0c36c8c-4e4a-356a-9a3b-71657f7d19d3 | 2.0856 | -61.8356 | 2025-01-15 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9c5cb97f-062f-3ac3-a9ba-29c00f836721 | 2.1039 | -61.8166 | 2025-01-15 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 1e6cadf3-9247-3cdd-96be-cade53131074 | 1.3217 | -60.4262 | 2025-01-15 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1f335805-a0b1-3b44-9a61-8deb3c87cd9c | -2.5104 | -51.9258 | 2025-01-15 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 921f7707-043e-3066-bb89-4501b0cc8981 | 1.3217 | -60.4452 | 2025-01-15 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6bd9c9f5-e6ea-305a-9dd0-624792f3157c | 2.1038 | -61.8354 | 2025-01-15 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 78.7 |
| c9f8f7b6-a10d-3a32-83a1-84cd1ff9ac7c | 2.1038 | -61.8354 | 2025-01-15 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |


[Clique aqui para ver as próximas entradas](README2.md)

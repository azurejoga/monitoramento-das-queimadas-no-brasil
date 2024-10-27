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
| 5e3e2787-ba99-3121-97d5-d77b5213f823 | -2.6359 | -54.292999 | 2024-10-27 01:10:14 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b746db2b-8bbb-3489-ad3d-a91f895c1324 | -2.6441 | -54.283901 | 2024-10-27 01:10:14 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 113b56e5-2e7f-3721-8850-28998dad8ab3 | -2.6457 | -54.290798 | 2024-10-27 01:10:14 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc3d3dc-5e9d-3f13-8fef-07932e66f61c | -2.6472 | -54.2976 | 2024-10-27 01:10:14 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2feae3aa-3bbb-39ad-a767-eb25da9883a5 | -2.5715 | -54.012798 | 2024-10-27 01:10:14 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 670336eb-68ef-3717-b32f-9943f85ca462 | -2.5417 | -54.242401 | 2024-10-27 01:10:15 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dfb68ca-fc73-3477-9ce0-c983e5040343 | -2.5358 | -53.992001 | 2024-10-27 01:10:15 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77ed0f72-5e47-3dc5-8ff7-eb33e850ffd3 | -2.7842 | -54.309898 | 2024-10-27 01:10:25 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a013434-1ecb-36d1-892d-27c82203ace2 | -2.817 | -54.4529 | 2024-10-27 01:10:25 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82110b16-d18b-3d76-b99e-4695ee1c93e6 | -2.8291 | -54.5504 | 2024-10-27 01:10:25 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2471b24-0716-30e6-8d25-e103a323d68e | -2.8306 | -54.557201 | 2024-10-27 01:10:25 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0c5b6e5-caa9-3d21-a7d9-bb2731af60ac | -2.8322 | -54.563999 | 2024-10-27 01:10:25 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df040709-7c4a-3351-9f4b-8a2ae97a9688 | -2.8875 | -54.895199 | 2024-10-27 01:10:26 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7108a8e-7d58-3141-b5fb-b03d3ce2cc8b | -2.8859 | -54.888401 | 2024-10-27 01:10:26 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8c2189e-2808-36d0-81cd-984fb0a9b195 | -2.0024 | -52.082802 | 2024-10-27 01:10:29 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d1955e4-dfed-3fe8-8f32-ceedb25e1db7 | -2.5425 | -54.6502 | 2024-10-27 01:10:30 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f1d2d9c-9eda-3ed7-aab6-dd4b4e25a102 | -2.544 | -54.657001 | 2024-10-27 01:10:30 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a9a02b4-90fc-3151-b196-c86c627e2cd2 | -1.9283 | -52.074799 | 2024-10-27 01:10:31 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b943ee0-5565-3e36-80c2-258992eddc4a | -1.9301 | -52.0826 | 2024-10-27 01:10:31 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23060ee4-9c45-39cf-8c1f-35058b230d03 | -1.9319 | -52.090401 | 2024-10-27 01:10:31 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8c843e-ccd9-37de-a8de-eaa9faab7ae9 | -2.3257 | -53.930801 | 2024-10-27 01:10:31 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04bd1c52-185b-35bd-96bb-06909e7ad75e | -2.2064 | -53.681301 | 2024-10-27 01:10:32 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35985843-e9ad-3e0d-9edb-b54032ce0d2c | -2.208 | -53.688301 | 2024-10-27 01:10:32 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a78fd5-a9fe-3624-aec5-81d3c94b1822 | -2.1947 | -53.720402 | 2024-10-27 01:10:32 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4062a80d-dd54-35b3-bc88-13fe3d926f7b | -1.6713 | -52.033401 | 2024-10-27 01:10:35 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62a32643-ffeb-3fee-bfe9-686a3d513cc7 | -1.6731 | -52.041302 | 2024-10-27 01:10:35 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d09e35-cae8-3c5a-b7e3-ff62af2254eb | -1.6749 | -52.049198 | 2024-10-27 01:10:35 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f5b1ae-9b55-3aef-9013-328e8cad6f55 | -1.7397 | -52.3293 | 2024-10-27 01:10:35 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f234b378-dc78-38d4-bd4e-a001d74e4493 | -2.2245 | -54.4781 | 2024-10-27 01:10:35 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cda02285-015f-30e8-87f4-45b4aa81e9dc | -2.226 | -54.484901 | 2024-10-27 01:10:35 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f637377a-2339-3711-8fc2-565a6dcd8a57 | -2.2276 | -54.491699 | 2024-10-27 01:10:35 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50e6b5e5-ef5b-376f-80bd-d31578450764 | -3.1771 | -58.935299 | 2024-10-27 01:10:36 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27c5c689-30f8-3742-b8e5-dedb9d797ce2 | -3.1793 | -58.945 | 2024-10-27 01:10:36 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d0ab94d-486e-30f0-a84d-77e07b110a87 | -1.5611 | -51.957901 | 2024-10-27 01:10:36 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e981a2-057e-32c4-9182-7a51487c3f9f | -1.8867 | -53.5919 | 2024-10-27 01:10:37 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fae4f071-4b95-341d-ad06-1ca08992e965 | -2.1197 | -54.830299 | 2024-10-27 01:10:38 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2bfaa1a-c3d4-322f-a93a-2460b9d044c8 | -2.1446 | -54.939201 | 2024-10-27 01:10:38 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 851b879c-b44f-363a-b2b9-b7680f704742 | -2.1462 | -54.945999 | 2024-10-27 01:10:38 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 885f4617-ff31-396b-8f51-411a35386f93 | -2.1478 | -54.952801 | 2024-10-27 01:10:38 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4393a52-aedf-35b0-832d-dab2c90ac15b | -2.0615 | -54.621799 | 2024-10-27 01:10:38 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3b87d4d-654d-36d1-a78c-5215c3f7d1dc | -2.0517 | -54.624001 | 2024-10-27 01:10:38 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aafc7619-5149-3dc2-a307-cf51ee9d1628 | -1.6421 | -52.933498 | 2024-10-27 01:10:38 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d98957-0e9a-3b26-9d87-43a0434acedc | -1.9578 | -54.394501 | 2024-10-27 01:10:39 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be36fef1-e6aa-3750-9c1e-d42623e0bd80 | -1.9594 | -54.401402 | 2024-10-27 01:10:39 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc04de3-3771-3b87-a3e6-e05690990a27 | -1.4278 | -52.228699 | 2024-10-27 01:10:39 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 863ec350-e850-38b1-b344-4d4a3302ae64 | -2.1106 | -55.240799 | 2024-10-27 01:10:39 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb613dd-67df-33f9-947f-f700acea807e | -2.1122 | -55.247601 | 2024-10-27 01:10:39 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c08872ba-22a3-37d8-bad9-3e7bcf316a41 | -1.9317 | -54.550701 | 2024-10-27 01:10:40 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd77f015-8b79-336f-848e-7978b52b0453 | -1.9333 | -54.557499 | 2024-10-27 01:10:40 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c13a5378-5c76-3d44-a589-d75b31f88ff5 | -2.5909 | -57.526402 | 2024-10-27 01:10:40 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 783465b5-5637-370c-bce0-da1af853692f | -2.5927 | -57.5345 | 2024-10-27 01:10:40 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7002db4c-0a3c-3091-b73b-d41e55d20db1 | -1.6043 | -53.306198 | 2024-10-27 01:10:40 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c64df06-0aad-328f-84d4-b99542b8d26b | -1.6059 | -53.3134 | 2024-10-27 01:10:40 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 661a63a4-8f08-3fed-a4e0-b95989f02df5 | -1.6075 | -53.320499 | 2024-10-27 01:10:40 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47bc5ce4-d816-3555-b614-54c46901878f | -1.6092 | -53.327599 | 2024-10-27 01:10:40 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34bd9029-cade-32b0-9e55-d6fd290c00c6 | -1.7926 | -54.259201 | 2024-10-27 01:10:41 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab60d48f-de95-3dd2-81c0-a02e0944241d | -2.0353 | -55.452 | 2024-10-27 01:10:41 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29d872e4-caa5-3547-ad52-d51c74218a05 | -1.578 | -53.505901 | 2024-10-27 01:10:42 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36ae1d10-1d72-3e11-818a-0d7f83bff899 | -1.5796 | -53.513 | 2024-10-27 01:10:42 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48614bdb-7691-3c57-9f3f-b0caf202d61a | -2.0255 | -55.454201 | 2024-10-27 01:10:42 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82eeac24-a469-3473-8778-8acd9e9000b2 | -1.2267 | -52.116901 | 2024-10-27 01:10:42 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b0ea7fe-3dce-3d5d-acb2-b7d4dc89c622 | -1.2286 | -52.124901 | 2024-10-27 01:10:42 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d86b1f2-8334-3660-b841-14f5163e4138 | -1.9991 | -55.699402 | 2024-10-27 01:10:43 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92b1760f-5964-31aa-b881-1c98820ce315 | -1.4326 | -53.412102 | 2024-10-27 01:10:44 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5df3f6d2-aabc-3d80-ae6c-c72e4088d013 | -1.4343 | -53.419201 | 2024-10-27 01:10:44 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b66755b2-2ea2-326a-9b7d-51a82a1fdcc4 | -1.4359 | -53.426201 | 2024-10-27 01:10:44 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd0d76bc-b1cb-37f4-aef4-df7501c1f2c8 | -1.4375 | -53.4333 | 2024-10-27 01:10:44 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1875f6f7-dcf9-3637-a68c-d7e3658ab981 | -1.7232 | -54.990398 | 2024-10-27 01:10:45 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d07ba596-bbcd-3f0a-be35-a0b9f0a77451 | -1.7247 | -54.9972 | 2024-10-27 01:10:45 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d1d096-4266-3472-9470-72c63f1317b7 | -1.955 | -56.002201 | 2024-10-27 01:10:45 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecd6b8bc-c161-3b50-87e8-6320bcc63f8c | -1.9566 | -56.009201 | 2024-10-27 01:10:45 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1ef3a6e-627a-3902-a3c2-7c262f031fec | -1.9582 | -56.0163 | 2024-10-27 01:10:45 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a13948e7-a1ff-30a7-bb27-65064481fa25 | -1.9598 | -56.0233 | 2024-10-27 01:10:45 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 995f24c8-fbab-3ca0-8959-a48233582144 | -1.2631 | -53.034 | 2024-10-27 01:10:45 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ed1abe8-5cbe-3e57-9074-08ecfdff2179 | -1.2647 | -53.041302 | 2024-10-27 01:10:45 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15092a3a-b6a9-3cf0-9dcf-eacc05ad698d | -1.4383 | -54.064301 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9da7bb0b-fb9a-3630-8c67-9036037b333e | -1.4399 | -54.071201 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 249bf44c-4657-3a70-b6c6-6c1b8d9a12f3 | -1.4415 | -54.078098 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c717689f-7f89-3e81-b749-fdd02b35db9a | -1.4269 | -54.059601 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 955d39ea-0919-3035-932c-3d47d4979734 | -1.4285 | -54.066502 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42b71d61-ed5a-3935-a993-daeb13311508 | -1.4301 | -54.073399 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 997c6d5f-feaa-326a-94e3-23691dbc56ef | -1.4317 | -54.080299 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dbf3247-07a4-3249-b4c0-d46c27cadd35 | -1.4171 | -54.061798 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31cce3bb-9618-34df-bce0-19649dc44b28 | -1.4187 | -54.068699 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c24bf6e-533f-3a68-b5ed-a4c80fe2bcf9 | -2.0578 | -56.858398 | 2024-10-27 01:10:46 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8fe4972-bbf2-3e1f-bdbc-264d2bce551f | -2.0595 | -56.865799 | 2024-10-27 01:10:46 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d448c7c-c030-3eba-9364-837aa332a439 | -1.4026 | -54.0434 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed43e4ab-9088-360b-8697-7aa257829d2b | -1.4578 | -54.283699 | 2024-10-27 01:10:46 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa2f1724-79db-3ee0-8083-1077c0af8228 | -1.448 | -54.2859 | 2024-10-27 01:10:47 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52678c81-a9cb-3c1b-a16d-3e151ab87923 | -1.6445 | -55.186798 | 2024-10-27 01:10:47 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93efb394-110e-3359-8766-0435c549b4c9 | -1.6461 | -55.1936 | 2024-10-27 01:10:47 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebd0ae0d-918a-3394-9177-a929890d99fc | -1.1302 | -53.442501 | 2024-10-27 01:10:49 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65eda976-a011-3cb7-a17e-58e59d50e3d8 | -1.1807 | -53.661598 | 2024-10-27 01:10:49 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 023bd011-7923-3148-8fd6-c47cefc54e5e | -1.3083 | -54.216301 | 2024-10-27 01:10:49 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baf4fcc3-4327-38cd-b7cb-0c825a8d1a5a | -1.3098 | -54.223202 | 2024-10-27 01:10:49 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a4a00f8-1a5c-3141-810c-437f866a0f33 | -1.6073 | -55.699299 | 2024-10-27 01:10:49 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc555948-b391-3703-aa24-4adcf35ab1ab | -1.1798 | -53.882099 | 2024-10-27 01:10:49 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b69fa745-8294-3816-b5f8-83175ec48fa5 | -1.1814 | -53.889099 | 2024-10-27 01:10:49 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 551a68db-855a-329a-9632-e6c70ce8f421 | -1.183 | -53.896 | 2024-10-27 01:10:49 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61f969d6-ab7a-3304-93a7-94eae5d18890 | -1.3454 | -54.603001 | 2024-10-27 01:10:49 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)

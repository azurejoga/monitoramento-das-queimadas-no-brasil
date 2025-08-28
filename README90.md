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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4163c35b-69fd-31cc-b242-243ec0ec7c7f | -14.3503 | -52.0838 | 2025-08-28 08:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| ee5fa4df-9121-33c8-a295-fd0555644b35 | -6.4355 | -44.5764 | 2025-08-28 08:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a0235792-a429-3fea-a0cd-b099b738a988 | -13.2269 | -46.0391 | 2025-08-28 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 808c9db5-970f-39fb-af47-a93ff908f139 | -6.8772 | -43.6152 | 2025-08-28 08:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 2d832605-ab81-34fd-b6be-4a9f32133c2b | -9.1339 | -65.788 | 2025-08-28 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 1bc79495-9965-3ce7-b851-dca4af9d096e | -9.1154 | -65.7886 | 2025-08-28 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 31128d0c-f3fa-3f07-bdc6-6779b1a7a70a | -9.1155 | -65.7699 | 2025-08-28 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| b11a5276-395e-3685-92cd-92dcf6288748 | -9.1155 | -65.7699 | 2025-08-28 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c02610d7-58cc-32fd-b78a-557111da633a | -9.1154 | -65.7886 | 2025-08-28 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 1f817e8b-f6cd-3ccb-9863-773280e50072 | -9.134 | -65.7694 | 2025-08-28 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 57c7551b-19a2-3563-a30b-6550e0427bfc | -9.1339 | -65.788 | 2025-08-28 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 053db3be-1ee7-346c-aa46-61b410d07309 | -13.2075 | -46.0421 | 2025-08-28 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 1a050c2f-6667-36ff-b14c-797ea492480a | -9.1155 | -65.7699 | 2025-08-28 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 88b19627-5f82-36bd-8e06-0db7573fbc92 | -9.1339 | -65.788 | 2025-08-28 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0846fd6a-19a4-347b-ace5-83061d0716a5 | -9.1154 | -65.7886 | 2025-08-28 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 167.7 |
| 83140369-d907-398e-9531-7e27b3a33925 | -9.134 | -65.7694 | 2025-08-28 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 54c0b24c-cc34-3619-9d6d-4514a7cf9a8e | -9.1155 | -65.7699 | 2025-08-28 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| f6d37946-ce33-30eb-89e4-e679e274be3e | -9.1339 | -65.788 | 2025-08-28 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 0bcbba65-6257-30a4-b82a-8ecd787d1369 | -9.1154 | -65.7886 | 2025-08-28 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 7401be59-f97a-3ab6-8078-2c4a672641f1 | -9.134 | -65.7694 | 2025-08-28 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 77c1eaef-8ae7-3b25-8cbf-9e930e9cd706 | -9.1339 | -65.788 | 2025-08-28 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4e45562b-032e-3df0-b5d8-053f938ce611 | -9.134 | -65.7694 | 2025-08-28 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| aa5c4564-4d07-3a9e-bbf3-def1635d5566 | -9.1155 | -65.7699 | 2025-08-28 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c49fc2c6-cd18-34bc-92ac-4708d76c9db3 | -9.1154 | -65.7886 | 2025-08-28 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 336b2ff7-9e24-33b6-983d-c74e5b54d64d | -9.1154 | -65.7886 | 2025-08-28 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 158.0 |
| ef8a25bc-8456-3525-8dfb-49ed79822a1b | -9.1155 | -65.7699 | 2025-08-28 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| f4d1ee39-0660-3655-af54-2c5d22aab3cf | -9.1339 | -65.788 | 2025-08-28 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ffe02d11-1caf-399c-b2ef-357d90f37f39 | -9.134 | -65.7694 | 2025-08-28 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 976568d4-1b4f-3078-85b2-96011adb5050 | -9.1154 | -65.7886 | 2025-08-28 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 46a7787a-033c-3a74-b224-49b506bcddd8 | -9.1155 | -65.7699 | 2025-08-28 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 821dfb94-ec61-30e7-995b-eaac2cabf369 | -9.1339 | -65.788 | 2025-08-28 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| cff776a6-89f7-3c99-a8ed-fc1a25273736 | -9.134 | -65.7694 | 2025-08-28 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| cb98d911-8810-3fe9-8cf9-08f9a9b5d855 | -9.134 | -65.7694 | 2025-08-28 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| bcf0a80f-e5f3-3c45-a63a-df23acbea985 | -9.1339 | -65.788 | 2025-08-28 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 3b790ac9-366a-3b43-9b43-79dc727d361b | -9.1155 | -65.7699 | 2025-08-28 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e0b5e574-69a8-34a7-94d6-50eae8f86e30 | -9.1154 | -65.7886 | 2025-08-28 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 0798d7da-c7dc-3db5-9b16-37ff8dcd93dd | -9.1339 | -65.788 | 2025-08-28 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 14f82fae-3023-37bd-9240-0d0b01fb483f | -9.1154 | -65.7886 | 2025-08-28 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 263b531f-0867-3f8e-91f1-27890f0e6af7 | -9.134 | -65.7694 | 2025-08-28 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 4f8f0757-b523-348c-9e31-0263d10e6c1c | -9.1155 | -65.7699 | 2025-08-28 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| aab02c0d-f2e4-3bc0-9099-2247e2b4213f | -9.1154 | -65.7886 | 2025-08-28 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 36966802-25e4-356d-bc75-c33d63bfcf84 | -9.134 | -65.7694 | 2025-08-28 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0bfd599c-4f20-3477-8fe6-1d3b5c45b71a | -9.1339 | -65.788 | 2025-08-28 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 09e3b634-aa84-3e0c-a9ca-8ded704d434d | -9.1155 | -65.7699 | 2025-08-28 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 312bd120-6c38-3c9a-843f-a20db0631d19 | -10.327 | -46.8045 | 2025-08-28 10:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| be6bbbcd-bacc-3b61-a72e-26fa124bda07 | -9.1154 | -65.7886 | 2025-08-28 10:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 162.8 |
| b810e9e3-9e1d-3c53-8218-d75f44469bfa | -9.1155 | -65.7699 | 2025-08-28 10:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2412c3a4-2e57-341a-b55b-2c3268bc059b | -9.1154 | -65.7886 | 2025-08-28 10:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 5ed57a6d-1b5e-32a5-8e4f-c8ebf0b3de2b | -11.3521 | -43.5423 | 2025-08-28 10:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 28e94917-2f07-3ab8-bfe8-6cc68d1a8542 | -6.8772 | -43.6152 | 2025-08-28 10:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 3ffecfbf-ac2f-38a2-bcac-8cf89ddaf5ba | -9.1154 | -65.7886 | 2025-08-28 10:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 184.6 |
| 995219cc-88ae-3dbb-a988-16744cd3bc67 | -9.1155 | -65.7699 | 2025-08-28 10:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 27075113-9363-3a1f-836b-a17feaa5bab1 | -6.8772 | -43.6152 | 2025-08-28 11:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| b6be5f23-e6bb-387a-b3eb-a2c2d4137bd2 | -9.1155 | -65.7699 | 2025-08-28 11:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ca48cef2-f487-35ce-a4df-ca47962f1037 | -9.1154 | -65.7886 | 2025-08-28 11:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 205.9 |
| 3022aaa8-635d-3324-b047-869a3cae9250 | -9.1154 | -65.7886 | 2025-08-28 11:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 178.6 |
| 22653dcf-6b91-3b3f-9d8f-d614145ddc20 | -9.1155 | -65.7699 | 2025-08-28 11:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 1b2d83cb-f261-372e-887c-97e77946c2a7 | -6.8772 | -43.6152 | 2025-08-28 11:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| fa9219f6-b4c5-352a-a4e2-98aa574d498a | -6.8772 | -43.6152 | 2025-08-28 11:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 7b862928-0869-30d8-ab75-3ee558f73c57 | -9.1154 | -65.7886 | 2025-08-28 11:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 09a78dbd-4e7c-3082-86bc-889a5b00f74f | -9.1155 | -65.7699 | 2025-08-28 11:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 1bbb77a2-a48e-37a5-9214-570ddf1f5c33 | -11.3521 | -43.5423 | 2025-08-28 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 9f523657-db67-321e-8c74-ba5d124c7a0c | -11.5703 | -46.3978 | 2025-08-28 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 83cbafcf-579b-37dd-8ce7-15cc35631c49 | -12.8805 | -48.1186 | 2025-08-28 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 44a54e72-81bf-3f2e-8968-4c3e104efe41 | -11.5703 | -46.3978 | 2025-08-28 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 292.7 |
| 85a20a3c-e5b0-3496-9314-e0fb496905d3 | -11.5894 | -46.3952 | 2025-08-28 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1d65f24f-4a2f-3b02-90b1-691af9c8beb9 | -6.1595 | -44.0472 | 2025-08-28 11:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2b5b60f1-59cf-37fe-8623-5b9b2c422633 | -6.8772 | -43.6152 | 2025-08-28 11:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| cf6fb714-bebb-3cd5-9473-0fe7207b6916 | -11.5707 | -46.3751 | 2025-08-28 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 6705058c-1877-3a07-a737-9a3283007e7f | -9.1155 | -65.7699 | 2025-08-28 11:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 634e439e-bb46-349f-bce7-ac1a3335a3ad | -11.5699 | -46.4205 | 2025-08-28 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c651360a-09ab-384f-9585-0bba7c999fff | -9.1154 | -65.7886 | 2025-08-28 11:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 207.0 |
| 2fd6ca08-c34f-399d-b2e2-2da1a141f425 | -11.3521 | -43.5423 | 2025-08-28 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 31ff7b33-c7b0-32f2-b21c-c43be4211baf | -6.1593 | -44.0703 | 2025-08-28 11:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e54a9606-95ba-3c86-a923-08f7203e3ddf | -9.1155 | -65.7699 | 2025-08-28 11:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| f267af98-f98b-3c07-9bbf-7397b0cca9e2 | -11.5894 | -46.3952 | 2025-08-28 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| eb46ac2b-fbc5-37a6-9eba-edeb1ff64eed | -11.5703 | -46.3978 | 2025-08-28 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 414.7 |
| bfebd617-294b-397e-bc8f-5ae0fa6d1b3b | -6.1595 | -44.0472 | 2025-08-28 11:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| d0812cd6-89a2-3024-889c-abbddae1de86 | -9.1154 | -65.7886 | 2025-08-28 11:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 244.6 |
| 56a00c83-142a-3d49-bfe1-20e6964afa28 | -6.8772 | -43.6152 | 2025-08-28 11:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| a9c56c74-c9c4-30ad-ba05-9b29555dbb37 | -11.5699 | -46.4205 | 2025-08-28 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e99b8986-34e2-3470-a3ee-9178e7243604 | -11.5707 | -46.3751 | 2025-08-28 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8e86a668-5b6f-3e66-b0b0-004e1bb4d80f | -11.5703 | -46.3978 | 2025-08-28 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 345.8 |
| c77c460f-fd9a-31e5-8991-24407982a72b | -11.5699 | -46.4205 | 2025-08-28 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| c0792d98-3161-3ab3-bafc-ce3ee6bddb94 | -9.1339 | -65.788 | 2025-08-28 11:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 40c06f02-4669-371a-afa7-f4b2033d3e6e | -6.8772 | -43.6152 | 2025-08-28 11:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| a9438dc8-2cfd-37d8-a3b0-3cc3518e6154 | -11.5707 | -46.3751 | 2025-08-28 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 13ac5f7a-876a-3490-810e-7df88c230ec2 | -9.6794 | -47.0798 | 2025-08-28 11:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a8e0ae14-1192-3d1b-b2a2-026a6091cb4e | -11.3521 | -43.5423 | 2025-08-28 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ca56d881-02e3-31fc-9acb-bb219d1d7ae5 | -9.1154 | -65.7886 | 2025-08-28 11:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 268.3 |
| 9d72f9ee-643b-340d-80a3-b08a690a3fc3 | -11.5894 | -46.3952 | 2025-08-28 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| ea70304b-ca08-32bc-9996-0b1f3e9b3308 | -6.1595 | -44.0472 | 2025-08-28 11:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| dc0c1b48-f13d-3fd5-99fa-a7d9fbd7ddc7 | -6.1593 | -44.0703 | 2025-08-28 11:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 1d94ac98-0f2f-3063-ad86-1bdda43fd19c | -9.1155 | -65.7699 | 2025-08-28 11:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 044435c2-4754-3b3e-aca2-f33c4c8f6e8c | -11.5703 | -46.3978 | 2025-08-28 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 52b4ad8e-f18b-3148-a38f-f9703f9e1c7e | -6.8772 | -43.6152 | 2025-08-28 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 386554c7-6aac-348b-8d93-b086f769a8b3 | -13.7373 | -51.9077 | 2025-08-28 12:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| faa1e96b-733c-3051-9140-4722aabb62ca | -9.6794 | -47.0798 | 2025-08-28 12:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a4cf2778-10d2-3353-9a2d-618b45f19211 | -9.2632 | -65.8959 | 2025-08-28 12:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 79121fab-7d05-38cc-927e-f2143e5d30fa | -11.3521 | -43.5423 | 2025-08-28 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |


[Clique aqui para ver as próximas entradas](README91.md)

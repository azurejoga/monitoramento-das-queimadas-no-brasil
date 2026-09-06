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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3004009-592d-3a4d-80c4-64acea70e7e2 | -5.2715 | -60.1255 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 82ddbfeb-5585-3d9e-8a24-74f813db781f | -3.7645 | -61.7548 | 2026-09-06 15:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| c78850e1-9153-3e5f-a715-ab7d8b073686 | -6.7648 | -59.4408 | 2026-09-06 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 748db9fb-d4dd-3ac1-a3d7-777f0122a130 | -5.6566 | -60.2284 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 43fa237d-5ddc-30eb-9fc6-fd833a45c25f | 1.8029 | -56.0587 | 2026-09-06 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 359e0c31-9685-39ee-bede-d2e085fccab2 | -8.9791 | -44.3951 | 2026-09-06 15:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| c6d0225d-c386-3453-a892-a8a8bf5162fd | -5.9998 | -57.7859 | 2026-09-06 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 687a0757-f98c-339f-b96b-2ad3a9684424 | -3.6215 | -60.566 | 2026-09-06 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 24e04268-2e4b-3df1-8214-956798633d90 | -5.4731 | -60.1959 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b028dc54-db29-36d8-9927-a2e96da7d955 | -5.2537 | -59.9923 | 2026-09-06 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1b7d5ea2-871e-3531-8157-c053eabfe16e | -3.3871 | -59.4075 | 2026-09-06 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 6c31af07-7056-3566-b21a-9df6e1323d76 | -3.8575 | -61.1867 | 2026-09-06 15:10:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 92101b46-0ca9-36b6-9f8c-787cd1132e78 | -5.2898 | -60.125 | 2026-09-06 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| ed28e458-3087-322c-84e9-931c9c19eb9b | -10.6452 | -45.8635 | 2026-09-06 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 72c741ad-6ee7-37b4-94c1-68b7f684a639 | -5.2529 | -60.1643 | 2026-09-06 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| d49b0bcf-d1f9-37be-b6fc-8d7ccc57d180 | -5.6566 | -60.2284 | 2026-09-06 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 141.0 |
| be8a6529-40f5-394d-83dc-2ba7a6093131 | -3.4269 | -58.3104 | 2026-09-06 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 3c3b3b24-68e7-3247-bc61-f74fcb684557 | -10.6639 | -45.8838 | 2026-09-06 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 70b44e28-cb81-39ec-851b-81e864bdea8d | -5.6382 | -60.2289 | 2026-09-06 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 7681db81-b615-3a5f-a05e-0e1594140735 | -3.1462 | -60.6317 | 2026-09-06 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| dad85392-6edb-3296-8368-a4c9b247c5c4 | -3.128 | -60.632 | 2026-09-06 15:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 459668cc-0d38-3cf9-9c8c-3ea395f974cf | -7.6079 | -57.616 | 2026-09-06 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ad27baf7-fd23-377b-a304-3efdd50094b8 | -3.3871 | -59.4075 | 2026-09-06 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 9227abe9-1aab-3b8e-8ba5-51d36f9cc8e0 | -2.9521 | -57.8946 | 2026-09-06 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4002fe98-3cd3-3754-8d6c-fec769bc614d | -3.387 | -59.4266 | 2026-09-06 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 575624d7-1e4b-3b40-83f0-2cf4a46bd13d | -3.7828 | -61.7545 | 2026-09-06 15:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1e8fc27e-461d-324c-a4cb-ed6f87e69184 | -3.3688 | -59.4079 | 2026-09-06 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 89060c76-784a-3e0a-b519-69ae9827e93b | -3.3871 | -59.3883 | 2026-09-06 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2028ec2b-c7f1-38a4-ba37-e5fe4cf62c6c | -3.7645 | -61.7548 | 2026-09-06 15:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 147.1 |
| aa45e01d-e8de-30cf-af43-be41755fbe7d | -6.6514 | -59.945 | 2026-09-06 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f43f1fdc-4b31-308c-911e-566982f23982 | -3.6215 | -60.566 | 2026-09-06 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e33c87ca-8434-3915-b930-589c6a6fed3e | 1.8029 | -56.0587 | 2026-09-06 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e487fbef-3db9-3c22-9210-3d1d3895a998 | -2.9338 | -57.8949 | 2026-09-06 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 925f70aa-ae95-3ff5-abfd-981d2a563da7 | -5.5098 | -60.1947 | 2026-09-06 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1d592e36-8c8b-3c3e-aa59-6d615af4f95e | -5.4914 | -60.1953 | 2026-09-06 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 254.3 |
| 4084be18-0bea-3975-a5c7-704489eae7d0 | -2.85 | -50.45 | 2026-09-06 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e283fa0-8e75-3d20-a855-6695b523bc0c | -2.88 | -50.45 | 2026-09-06 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3357f82b-add6-314b-b636-7f0bda6d38b7 | -5.2537 | -59.9923 | 2026-09-06 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| f6b105c3-dd11-3645-a84f-19f4d017b60b | -10.3205 | -49.9567 | 2026-09-06 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 35d8a1cb-6c7e-3dd0-9791-d1aa7d0dcb2b | -3.7645 | -61.7548 | 2026-09-06 15:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 0e5f9aa6-d0f6-3f2c-b015-9e9491c93f29 | -3.6215 | -60.585 | 2026-09-06 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 295f993e-b971-3ac2-9628-e9d03147c437 | -3.1462 | -60.6317 | 2026-09-06 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 00b0ee8a-3339-367f-8023-37957c839681 | -3.3688 | -59.4079 | 2026-09-06 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a7a7bf31-388a-3eaa-a2cb-6e8a7b5d8589 | -3.3687 | -59.427 | 2026-09-06 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 6a6e32fb-7128-3f0b-a253-6749bcccf698 | -5.4914 | -60.1953 | 2026-09-06 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 204.3 |
| e1cdfff4-53f2-3569-8f7a-26a71cc175cb | -5.6566 | -60.2284 | 2026-09-06 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.9 |
| ce4d919a-d5f8-3211-a95d-094d9bac9765 | -3.1462 | -60.6506 | 2026-09-06 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 4470e75c-e8f2-33d9-be41-074c5f822046 | -3.7645 | -61.7737 | 2026-09-06 15:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| d00e7937-0a3e-3fad-9c3d-b5360623236d | -4.2821 | -59.9803 | 2026-09-06 15:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 33bfaa4a-50fb-38c2-b774-a96ee6c01356 | -5.4731 | -60.1959 | 2026-09-06 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| af0cdec2-9db7-3905-867f-f3e26f508baf | -10.3397 | -49.9333 | 2026-09-06 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| b033d516-fc94-384b-9e4a-a7085984a446 | -3.4269 | -58.3104 | 2026-09-06 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 7226e936-7e59-315e-b48a-31781a24566d | -5.9635 | -57.6899 | 2026-09-06 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6bbe3059-fc9a-3989-8848-dbfc2a9a8c85 | -5.2898 | -60.125 | 2026-09-06 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 04916286-b838-3f02-b0a5-61febce5c6eb | -7.6779 | -44.3266 | 2026-09-06 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| bb61a082-f69b-3fbb-b3a4-5b1420d41f4e | -3.6215 | -60.566 | 2026-09-06 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7750a71e-1aab-38d7-a5a6-f45fa5627499 | -5.1239 | -56.271 | 2026-09-06 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5fa73714-8963-3e76-b778-32fa84a96de6 | -7.6079 | -57.616 | 2026-09-06 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ef8102fd-4b5b-3f86-9125-711794752df1 | -5.5098 | -60.1947 | 2026-09-06 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 5a229c93-2a81-3dec-a4d3-c919e0783130 | -3.387 | -59.4266 | 2026-09-06 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2ff01d79-73b0-3df3-98a4-e7863426080d | -3.8575 | -61.1867 | 2026-09-06 15:20:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f0444538-0cfb-3f43-aa54-302112de242c | -2.9338 | -57.8949 | 2026-09-06 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2677735e-146f-3326-a8d7-544d807525d8 | 1.8029 | -56.0587 | 2026-09-06 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 7f76e49d-71aa-3fe3-a910-4b33aa2c0c9e | -3.3871 | -59.4075 | 2026-09-06 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 71bbd000-0241-3df4-a7a0-5c779b4263ca | -3.128 | -60.632 | 2026-09-06 15:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9d3219ce-7484-31a9-901c-04315755180f | -5.6382 | -60.2289 | 2026-09-06 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 9505b204-6b86-3cad-9e5c-0c6c6a013596 | -8.9601 | -44.3973 | 2026-09-06 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 8b596e58-7c8e-3317-9e32-ec5fc4da5ce9 | -5.2715 | -60.1255 | 2026-09-06 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4b464194-d400-3ec2-ac77-64d42b92e958 | -5.4731 | -60.1959 | 2026-09-06 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5b0908e4-6b62-31bf-9ffa-06014603e663 | -5.6566 | -60.2284 | 2026-09-06 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 1b8c9512-82a4-31a2-a4db-c7f779127ecb | -6.1361 | -59.9063 | 2026-09-06 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 6f092412-6413-3a4e-ba27-b49d5a167b43 | -5.4914 | -60.1953 | 2026-09-06 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 145.7 |
| a6ac8e6a-65e9-3f20-9f98-69d66ab784e9 | -3.7645 | -61.7548 | 2026-09-06 15:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 77256b02-d706-3d43-ba18-937fdb7291cd | -3.4003 | -61.3087 | 2026-09-06 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| fdc76524-6c18-3034-b7d9-ca66d19f43d7 | -6.0992 | -59.9267 | 2026-09-06 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| db140dd0-84e5-3fef-8ecf-555d04fbe0e3 | -2.9338 | -57.8949 | 2026-09-06 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 2a143915-428d-3dc3-81f0-53f61125515b | -3.387 | -59.4266 | 2026-09-06 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| c2234d39-9486-3b0d-8d15-aa3c4dddb2b4 | -3.3871 | -59.4075 | 2026-09-06 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 66ef837a-7050-3484-a488-97914ca86466 | -6.7833 | -59.4208 | 2026-09-06 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1cd47e22-ae75-3456-8b7b-0f96de3b5273 | -5.2715 | -60.1255 | 2026-09-06 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 0f7ad793-e0d5-36f5-af8e-57a81bc08769 | -3.1462 | -60.6317 | 2026-09-06 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 58615836-7487-3a41-b4da-0d58f21a2604 | -3.6215 | -60.566 | 2026-09-06 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 75618ca0-7825-308f-88c2-ada4091bdba4 | -6.641 | -58.4987 | 2026-09-06 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f4f49da3-63a4-3d0e-968c-be573ee9818c | -3.8575 | -61.1867 | 2026-09-06 15:30:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 87c90ac9-a3b1-3507-8c61-798185a9f505 | -10.2031 | -50.2681 | 2026-09-06 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b54aa592-443b-3eb7-ad79-d4e6d77658cf | -5.6382 | -60.2289 | 2026-09-06 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 83f7ff4a-b890-37df-ab30-64e9aa044f98 | -10.0542 | -50.1123 | 2026-09-06 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| affe9bb5-2a8a-356a-ba2c-a774ee51fddc | -10.3016 | -49.9587 | 2026-09-06 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| bffe3109-2163-31d1-8264-36fedc2016f5 | -3.1462 | -60.6506 | 2026-09-06 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0337b66e-b4a7-3b0f-923b-8ba74a043ee0 | -3.3688 | -59.4079 | 2026-09-06 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| cc9500d9-e1e8-3a4e-9039-02a8bf39844e | -1.4944 | -54.2563 | 2026-09-06 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1aa33b44-b31c-3bc9-97aa-99a2ed0bc645 | -5.5098 | -60.1947 | 2026-09-06 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 06fa075a-8043-3857-96cb-47800b5c0c56 | -7.6079 | -57.616 | 2026-09-06 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 64de1bad-0b31-34b1-8584-307157526e0c | -3.4269 | -58.3104 | 2026-09-06 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 09bbd1af-1457-3233-96b5-cad0f4bc54fd | -10.2406 | -50.2857 | 2026-09-06 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ff176a28-3711-3d2b-b2d7-7217c514383d | -3.3687 | -59.427 | 2026-09-06 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| a005c50f-e507-3e01-be8c-ba39b8a59149 | -5.2898 | -60.125 | 2026-09-06 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 77988105-4f56-3a39-a13f-d9b6aad965f0 | -5.9635 | -57.6899 | 2026-09-06 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ce452a0e-b806-3228-8b56-1988aa35154f | -5.4914 | -60.1953 | 2026-09-06 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 69255522-d20c-3f21-8e90-9da39b8b37ae | -5.9819 | -57.6892 | 2026-09-06 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |


[Clique aqui para ver as próximas entradas](README39.md)

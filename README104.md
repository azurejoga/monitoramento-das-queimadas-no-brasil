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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa443e20-0c93-3cdf-8012-3123db237b7d | -6.34524 | -58.17667 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a27c3d3-5449-3ab8-b8b5-121a7ddb94e9 | -6.34469 | -58.18016 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 397adf96-ca3c-343f-ba9e-e47286217555 | -6.34358 | -58.16564 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa6b236f-e64c-387b-be9e-4b885b589497 | -6.34302 | -58.16914 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a6a50e7-7fd1-3a62-894f-bb93b57e0f17 | -6.34247 | -58.17264 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c01a33f-16da-3319-889d-ad036da75b1c | -6.34192 | -58.17614 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ea144e2-a6dd-3f38-a816-80b2bf956231 | -6.33915 | -58.17211 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ee4b1d4-7652-3d4d-b9b7-b992c5668bde | -6.33859 | -58.17561 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 326a66f7-497f-3a19-a10a-abc0141e2dcd | -5.95653 | -57.69073 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ddb2876-b4a8-32b1-af1e-533a750b4328 | -6.51284 | -58.40532 | 2024-10-14 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 268dc081-cc66-3b35-8275-823bb12e06e6 | -3.17728 | -58.58522 | 2024-10-14 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6334b68-596d-3436-907e-862e055fce6f | -3.17386 | -58.58468 | 2024-10-14 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc053df5-390f-3a5c-a5a4-c18ed6bec933 | 1.13205 | -59.52677 | 2024-10-14 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3eabce7-524f-3cd0-9974-6b3eab3126a0 | 1.1308 | -59.5252 | 2024-10-14 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9c747a6-19dd-3cc7-aa92-ed377e12a3ab | 1.1283 | -59.52736 | 2024-10-14 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad3f2af2-81d5-3fc1-938b-b72b68c9628c | 1.12259 | -59.52186 | 2024-10-14 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fc9693a-689b-3036-b071-9d3686ee4582 | 1.09093 | -59.46698 | 2024-10-14 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36673b70-a39c-3b0b-826c-b8014ee0cc8e | 1.03521 | -59.45281 | 2024-10-14 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b12fe81f-e39b-3f8f-be81-131a44178be4 | 1.03451 | -59.44831 | 2024-10-14 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 208ae247-d4a4-3f81-a0a0-e0355916367a | -1.78699 | -60.3347 | 2024-10-14 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53a372e9-ce38-33ad-a203-476d8db5a6c3 | -1.78649 | -60.33746 | 2024-10-14 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5269cf76-b49f-3c0b-9b8c-d28da05f5bc1 | -0.7823 | -48.68267 | 2024-10-14 05:08:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3d787ef-ddab-3041-ae37-b6df24480e95 | -0.39813 | -52.01921 | 2024-10-14 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2e83191-b7d8-3bc9-97f4-d9314edca4b0 | -0.39435 | -52.01863 | 2024-10-14 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef29eec9-7d7e-3fcf-8986-1934864aafbd | -0.37873 | -52.01855 | 2024-10-14 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6996699a-0be5-3284-95ba-4eb92948bda7 | -0.13028 | -51.57218 | 2024-10-14 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 067dd6d6-971f-3c9c-9927-9f3246bd2f7b | -1.1436 | -54.10026 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66b93388-942e-3292-8379-22ab0fe81a5f | -1.14302 | -54.104 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a691a42c-d6ac-3e5e-861a-76ef9033126e | -1.0939 | -54.17311 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4e89c0ff-cfe7-3cdd-be28-93c5eceed2b4 | -1.02208 | -53.73471 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f32281e4-a28a-3c13-a94d-bf43f116d53a | -1.0192 | -53.73032 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e97b0b51-02d1-3402-abe6-5cb469d06e02 | -3.31146 | -42.84782 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86747250-9a55-3c33-af92-a95e92ad0111 | -3.30635 | -42.83263 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3b3ba6aa-c068-3555-8954-09f0fbe28f98 | -3.30533 | -42.83969 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 542a0eeb-556c-3dae-a0d2-a0ff87a36f3e | -3.3043 | -42.84681 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a9249450-63c5-3232-8d5e-baede40e3b7c | -3.30344 | -42.83242 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1099a515-f731-3544-82a3-e73a54220263 | -3.30328 | -42.85389 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 2c794c42-11bf-347f-9919-13de85a1f59d | -3.30238 | -42.83947 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 2b4bd0a2-95f2-33c9-a0b3-80cb182e7220 | -3.30131 | -42.84657 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ebb71919-979e-385e-8580-94d782192141 | -3.30024 | -42.85363 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 38784f69-f8d2-3036-88d1-a9a170d69950 | -3.29918 | -42.83165 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9643eee6-2b50-35d6-b4a5-33c6cc230f26 | -3.29816 | -42.83873 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 56537ec2-4635-3c8f-8320-ad4c8f4b40af | -3.29714 | -42.84583 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 7f3aa2d6-a3c6-3441-a97b-44f11b99537c | -3.29612 | -42.85291 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b298a3c7-ac51-3ba2-946a-9251e5f5bad0 | -3.2952 | -42.83857 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| c45e3bc4-2617-323d-845e-7cea5fe2ca92 | -3.29414 | -42.84563 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 374217a9-5768-3026-98c3-6e8fecef4500 | -3.29308 | -42.85266 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c0af688b-0642-3980-8349-436a6eb125dc | -3.29099 | -42.83779 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7eb050d4-e931-335e-b2e4-d1842e37795b | -3.28998 | -42.84486 | 2024-10-14 05:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 98226f2c-5f19-3436-a973-382f03f1848b | -4.04309 | -43.04685 | 2024-10-14 05:08:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 492b1fb7-d0be-3669-9e94-53d4bd8e5807 | -4.03595 | -43.04583 | 2024-10-14 05:08:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba5cc39d-de8f-3c57-8f9d-4d61b9ecb56a | -4.02981 | -43.03778 | 2024-10-14 05:08:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 025c1f42-d3f9-3535-99c8-c73fedc472e4 | -3.41434 | -43.35009 | 2024-10-14 05:08:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21951745-0fdb-398a-9820-6c9f825abdd9 | -4.03495 | -43.05285 | 2024-10-14 05:08:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66979cbd-b283-3003-848b-181e73123b96 | -5.19482 | -44.75962 | 2024-10-14 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbb35a51-62ba-3fe4-8520-5a1f4672a25b | -5.19404 | -44.76514 | 2024-10-14 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfb10b13-47e9-38a0-a047-0905aee37e13 | -5.19379 | -44.76152 | 2024-10-14 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6c08d7b-aaf5-3494-b635-d52b27c4a3f1 | -5.19304 | -44.76704 | 2024-10-14 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ece60d31-6266-31d5-9073-35fdc2a4a540 | -6.26492 | -43.9036 | 2024-10-14 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 949f92b1-49f9-38bd-b987-aa635e7a3526 | -6.2641 | -43.90966 | 2024-10-14 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b06d1d4-8820-3d27-9e0f-60a997f0a227 | -6.26349 | -43.90252 | 2024-10-14 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4aee8059-e97b-3710-8fde-b6c697939524 | -6.26268 | -43.90882 | 2024-10-14 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 246734f9-c63e-3144-9f8d-11bef0406622 | -6.45063 | -44.2962 | 2024-10-14 05:08:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22942aad-013e-3fe5-95e1-ee0aa10fcd3d | -6.44449 | -44.29594 | 2024-10-14 05:08:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b15d60a4-d689-30c2-a519-0d77f1e4db63 | -6.44379 | -44.29527 | 2024-10-14 05:08:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cb16595-f5ca-3274-86de-503397457470 | -6.43826 | -44.29026 | 2024-10-14 05:08:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5040e669-31d7-3d93-b257-ef62d3e23760 | -6.43759 | -44.29546 | 2024-10-14 05:08:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b391a645-8d1f-3703-89e4-0dc896d23658 | -6.43687 | -44.29489 | 2024-10-14 05:08:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff921fa8-f75c-316f-997b-74d4cd718e99 | -6.39674 | -44.83501 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af032e03-9f0f-3f24-938b-cb60896cd2b1 | -6.39426 | -44.83596 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d63c9a9e-531f-3cd3-8f9d-51826cd97ea8 | -6.39003 | -44.83467 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abe70c34-6613-3276-84c6-425fdc316e09 | -6.38929 | -44.84004 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f24b191-b933-387f-a841-7284a9aa23d7 | -6.38858 | -44.84515 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1f98b50-8c85-3d71-b2fd-d4fac3cb484d | -6.38754 | -44.83577 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9db1f956-a094-3e43-8106-16b1f1c1d358 | -6.38685 | -44.84101 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2a88c63e-8c6d-3c78-a920-47f8b484a427 | -6.38617 | -44.84615 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 23ea2289-46f6-3850-a803-7f729fea5ce3 | -6.38186 | -44.84498 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13cd31f5-c7fa-33b9-bcc8-46e8a82b43ff | -6.38107 | -44.85064 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a103a700-2efd-3b53-aa58-4c839b2da007 | -6.3787 | -44.85173 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e068ce9-4c18-3865-af1d-b6a3fb5b5948 | -6.17336 | -44.59863 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8efd2f64-dee0-34f4-9ef2-0b4015ac4ec5 | -6.1726 | -44.6045 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a9e8d4d-e9c6-3e04-a8b7-d35a0f4ebae4 | -6.17033 | -44.59798 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf5c81a5-ff3e-3c80-ac4a-9a720f52453c | -6.16954 | -44.60378 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac3fee6f-dbfb-3ce1-a56a-7008f9f94a33 | -6.16589 | -44.60362 | 2024-10-14 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61934c78-15ca-34c3-a41d-dba94f55c708 | -6.05357 | -44.8112 | 2024-10-14 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c53d94ae-a3da-308d-b7a4-0cb1541bc748 | -6.04852 | -44.81115 | 2024-10-14 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 149cc62f-4184-3645-aedc-46353c4ebac3 | -5.87251 | -44.04671 | 2024-10-14 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ecec014-63d4-3e10-8202-b4effa931852 | -5.87244 | -44.04707 | 2024-10-14 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a43e263e-4a7a-39d1-8ed7-14c3eb496ce9 | -5.87162 | -44.05307 | 2024-10-14 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4616e1da-e177-3c58-9322-d9beff9001d3 | -5.87159 | -44.05344 | 2024-10-14 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 632db3ab-2f5c-32f8-a5a3-c33f93ce9dfc | -7.93354 | -44.51842 | 2024-10-14 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd47eaea-ef91-3024-9f9d-f39b1e979258 | -7.92662 | -44.51781 | 2024-10-14 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 39abf834-878f-3156-8db8-0e7b9b12a818 | -7.60197 | -44.64053 | 2024-10-14 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69a5c913-1a07-38a4-8d02-491fba9db35c | -7.60116 | -44.6469 | 2024-10-14 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bbf76cc-f48c-32b8-80c2-6af02c5449d4 | -7.27016 | -44.96526 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 873d309c-d7cd-3879-bc1a-d0eb461b55e4 | -7.26945 | -44.97061 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 316626d4-29e6-3de6-8d81-b4c86c768ec9 | -7.26351 | -44.96437 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edabe0ba-2a58-3cdc-b37c-721557a59cd9 | -7.26284 | -44.96949 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17c4e29c-a1b2-38fe-956c-c5a582a72a59 | -7.25687 | -44.96345 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40787232-3e59-31d3-bfd3-f3fbd3a3c509 | -7.25622 | -44.96843 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README105.md)

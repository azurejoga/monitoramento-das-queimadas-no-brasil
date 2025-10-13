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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bc01414-d03a-3022-a2dc-8d6de232a80b | -2.5239 | -47.7899 | 2025-10-13 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 56879d1e-e274-3727-bb6d-80043c51c3d4 | -7.5449 | -46.089 | 2025-10-13 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| f145ff23-e405-379e-89a2-2f61bcd6398a | -2.5424 | -47.7893 | 2025-10-13 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| b27d9a8b-ac74-3b45-aa32-4588fb437c80 | -13.8957 | -45.4681 | 2025-10-13 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 330aad0b-38f1-38e9-b94b-27dca002b6b4 | -11.7497 | -64.9571 | 2025-10-13 01:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| aa9b5114-a0d9-37fd-8d83-d10cb789a50f | -6.5274 | -39.4786 | 2025-10-13 01:00:00 | GOES-19 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 108.7 |
| d45def17-0b01-32cd-8391-6ca6a0ba89f2 | -14.2825 | -51.5384 | 2025-10-13 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 145720e8-3a8f-35dc-8fcd-b7c046c7a8d6 | -16.1207 | -53.9625 | 2025-10-13 01:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| ce1d7d2f-2a68-3ef2-b422-901635cc4f74 | -17.3384 | -53.7922 | 2025-10-13 01:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 013dd18c-973c-361d-ae51-cb73e2efabf9 | -3.1433 | -50.2044 | 2025-10-13 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 41cf3405-3af9-31ea-a80e-f72e4d2e87ff | -4.6696 | -43.1326 | 2025-10-13 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 66766a4d-e96e-3bc3-b332-969e7e6a75ab | -14.2829 | -51.517 | 2025-10-13 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| e210562f-2bcd-31b4-b418-fbbd6f94dfae | -2.5238 | -47.8115 | 2025-10-13 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 3d0809f7-d91e-3091-8010-3b2446770b11 | -11.7309 | -64.9579 | 2025-10-13 01:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 9aaa5485-fc90-3fde-af44-1ff76dfd3bc4 | -17.338 | -53.8135 | 2025-10-13 01:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 5bbc7402-9700-31cc-b725-0ee03b2eeb0a | -14.3019 | -51.5359 | 2025-10-13 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 06030f30-3657-3213-9ecd-01d2953ba457 | -3.0726 | -49.404 | 2025-10-13 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| ff11169e-a9e6-31e0-a9de-a8050ac644e6 | -11.7495 | -64.976 | 2025-10-13 01:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c5c56099-e4ff-33e0-875c-3af34f205558 | -6.5464 | -39.4766 | 2025-10-13 01:00:00 | GOES-19 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 253.1 |
| fc753c64-e0af-3de2-8932-72857cc007bb | -6.5461 | -39.5017 | 2025-10-13 01:00:00 | GOES-19 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 3029efed-3c9d-3d46-b9ec-59b489a251fa | -3.0541 | -49.4046 | 2025-10-13 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ba94956e-4098-373f-9cd1-4e0b2b6de597 | -4.6885 | -43.108 | 2025-10-13 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f16b57a3-8271-3031-90b1-342f6784dbea | -6.5271 | -39.5036 | 2025-10-13 01:00:00 | GOES-19 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 54.5 |
| b833a4dd-2a21-3335-bc61-dccc06bd45b0 | -14.2822 | -51.5599 | 2025-10-13 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| de32a286-966a-3dcf-a21f-e8b5c4a66b9e | -4.6883 | -43.1314 | 2025-10-13 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 85344a4c-b36f-3648-b82d-1108b66b6a96 | -13.4977 | -51.2992 | 2025-10-13 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f773472b-8f65-33dd-9a23-10932e428fd3 | -2.5423 | -47.811 | 2025-10-13 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 4be62022-c972-3dd8-b42a-d42e13ab382f | -11.7308 | -64.9769 | 2025-10-13 01:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 42ff15ba-a49e-35d8-ad41-0e926872c061 | -4.6698 | -43.1092 | 2025-10-13 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 89c50263-29c8-3745-8b26-095e11b90fc1 | -13.517 | -51.2967 | 2025-10-13 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e5b8a350-2a17-383d-a64b-5d293686bbb7 | -13.8762 | -45.4714 | 2025-10-13 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| a78753c1-ccef-3c02-be07-be0e1025c474 | -14.3019 | -51.5359 | 2025-10-13 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 64bb3ea6-151b-3286-a4dd-0ce49591e7cc | -11.7497 | -64.9571 | 2025-10-13 01:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a1479a9b-b57b-35b6-bfff-b66550c4053f | -2.5424 | -47.7893 | 2025-10-13 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 56784709-e735-38d2-9473-ef962997f5e2 | -2.5238 | -47.8115 | 2025-10-13 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| c7e863e4-8d7e-34b3-983a-dfce25147c71 | -8.8905 | -45.3452 | 2025-10-13 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5b8eeece-20f2-30cd-8667-6717735ea723 | -8.8909 | -45.3224 | 2025-10-13 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 3d617dc3-194b-3b10-a7d5-10a6abd3ff37 | -4.6698 | -43.1092 | 2025-10-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| faf8b363-5479-3cc5-878a-1e16f5f8c2e4 | -8.8722 | -45.3016 | 2025-10-13 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 585ece30-16b0-3671-a3e8-f1ee7578bbd8 | -14.2825 | -51.5384 | 2025-10-13 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| b4eafb59-42aa-3b2d-966a-23dfdf393560 | -16.1207 | -53.9625 | 2025-10-13 01:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| ce6e7d78-41c6-31d6-8969-641adf486424 | -2.5423 | -47.811 | 2025-10-13 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| e30deaac-2225-3def-9eaf-5d82b90e4225 | -4.6696 | -43.1326 | 2025-10-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| d8346d54-3e0a-31d8-8317-380b94a92f12 | -8.8719 | -45.3244 | 2025-10-13 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 334.3 |
| b5a2af36-5524-3885-a9a6-89097ccfd52b | -17.3384 | -53.7922 | 2025-10-13 01:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 49066c23-0ce6-3f19-8474-c9d093e98046 | -2.5239 | -47.7899 | 2025-10-13 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 15f3b5d0-65f7-3257-bf09-d96a150f6119 | -8.8716 | -45.3472 | 2025-10-13 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 186.0 |
| ebcd752a-a9e3-353c-b9f0-6ef1f7771ef1 | -16.1203 | -53.9836 | 2025-10-13 01:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 379160d5-2622-37fc-81b6-87fca234dcb0 | -3.0726 | -49.404 | 2025-10-13 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| d821df8a-807d-3068-8dcc-6817cc9f3e78 | -7.5449 | -46.089 | 2025-10-13 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| d15b5236-0a71-3951-af67-54729578fcbb | -8.8729 | -45.256 | 2025-10-13 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 982e4382-8c15-3605-83a5-c2281d4f4242 | -3.0541 | -49.4046 | 2025-10-13 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 094cc86e-e8ad-30f8-838b-3674c07460f5 | -11.7309 | -64.9579 | 2025-10-13 01:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 0b99216f-6a15-328e-8b5f-868ab13c5736 | -4.6883 | -43.1314 | 2025-10-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1bbebd01-c7b8-3ae3-9750-375ba1986a1b | -8.8921 | -45.2311 | 2025-10-13 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 7f90f65c-b8fa-3320-b1b5-c73aec9f50c1 | -3.1433 | -50.2044 | 2025-10-13 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c923b298-45e9-361f-a667-c30309fb4ce3 | -14.2822 | -51.5599 | 2025-10-13 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 31d58eb8-6bbb-30f7-b943-40cc37154386 | -4.6885 | -43.108 | 2025-10-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 31a25951-4ef5-37a2-b6ad-e681d9ec6cdd | -8.8918 | -45.2539 | 2025-10-13 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c1b74a23-8542-32b9-ac9b-c7b6bab607db | -8.8732 | -45.2332 | 2025-10-13 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 64b45a16-64b9-3d74-aec6-0a66961cd883 | -17.338 | -53.8135 | 2025-10-13 01:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 138.7 |
| e0122f8b-488c-3883-b7f8-94816156ddc7 | -14.3015 | -51.5573 | 2025-10-13 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| c168b87f-463c-3a00-a439-2450124a3c20 | -7.5449 | -46.089 | 2025-10-13 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 0b578df5-4716-38c0-bb4a-4e5b33545d50 | -17.3384 | -53.7922 | 2025-10-13 01:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 38fafa3c-0b25-3eb5-8e0b-81b433e5fad2 | -4.6696 | -43.1326 | 2025-10-13 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 79286b7f-3669-34d7-818d-62b3f9f65cb8 | -3.0726 | -49.404 | 2025-10-13 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 8ab4aea8-cf90-3ccb-b119-e616722c60e2 | -2.5423 | -47.811 | 2025-10-13 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 09b30282-61a8-3793-a920-5ba8024e9dcd | -4.6883 | -43.1314 | 2025-10-13 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 3a56696d-42ac-3c88-9efa-7bcb26b0e763 | -2.5238 | -47.8115 | 2025-10-13 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| e56366a2-777f-3155-909c-adf3c40b6312 | -2.5424 | -47.7893 | 2025-10-13 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| c5a32de5-f7d5-3c0e-a246-c73c52a21d12 | -3.1248 | -50.205 | 2025-10-13 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0a37efa0-f970-343c-94e3-881f8c28b59d | -14.3015 | -51.5573 | 2025-10-13 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c3b3081c-935c-390b-a1a7-ff3084f98df0 | -2.5239 | -47.7899 | 2025-10-13 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 113f9158-fd39-38bb-b899-09e57424df1f | -17.338 | -53.8135 | 2025-10-13 01:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 141.2 |
| edc4481c-a6c8-3551-b092-41091c19538d | -16.1207 | -53.9625 | 2025-10-13 01:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| b439a593-45a4-30d8-9d9e-9fa201cd4bd6 | -16.1207 | -53.9625 | 2025-10-13 01:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 88c6e03e-f175-3c43-9b3a-4c733079cf18 | -16.1203 | -53.9836 | 2025-10-13 01:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 659c3d2e-b564-39d3-9fca-4d945135f7bc | -4.6883 | -43.1314 | 2025-10-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9911c7c1-aa91-30f2-aa27-c84ef11d97c4 | -2.5238 | -47.8115 | 2025-10-13 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 78032e4a-1847-39b2-8ccc-fd52048427ff | -2.5423 | -47.811 | 2025-10-13 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| a5a41886-7cee-3bba-8c18-180630829afc | -4.6696 | -43.1326 | 2025-10-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a5d7be8b-eac2-3998-af5e-a1255023e4bb | -14.3019 | -51.5359 | 2025-10-13 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4c8d6cd5-7450-3247-b59f-0861f777945b | -2.5239 | -47.7899 | 2025-10-13 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| a54f0f6e-2b9a-3d6c-ba90-668af66acac4 | -7.5449 | -46.089 | 2025-10-13 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 224a2cac-e1fe-3220-8553-6844c6efe272 | -4.6698 | -43.1092 | 2025-10-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 546a54ca-60a5-32a7-9857-423a971281f0 | -8.8729 | -45.256 | 2025-10-13 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2c51a3ef-1fde-39c4-8429-13041f22131e | -14.2825 | -51.5384 | 2025-10-13 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4247e0a2-6f0d-3e75-84f9-bf20d86b75d4 | -17.3384 | -53.7922 | 2025-10-13 01:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 118.4 |
| a410343e-5948-35c0-9f84-db670397ace8 | -4.6885 | -43.108 | 2025-10-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| ead9bcf4-0684-3470-b57c-fdc368cc2459 | -17.338 | -53.8135 | 2025-10-13 01:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 56cb4415-7a93-3f20-a644-665146c3a717 | -3.0726 | -49.404 | 2025-10-13 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 830b02e2-78ce-3837-8f05-e180bb698f62 | -2.5424 | -47.7893 | 2025-10-13 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| c5c9ab92-284e-3743-80c5-cdf780c94ae8 | -14.3015 | -51.5573 | 2025-10-13 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| c7a8b9ce-2a91-3114-80e3-eadd4ed11471 | -3.1248 | -50.205 | 2025-10-13 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f67cecc1-569a-38f0-9cf8-8dca9d703281 | -19.0316 | -57.5589 | 2025-10-13 01:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 34.7 |
| 80633be1-d0c5-3516-a675-67bcafdf8f26 | -2.5238 | -47.8115 | 2025-10-13 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| ea67c4a0-447d-3d8b-b8e4-b312dcf6ef80 | -7.5449 | -46.089 | 2025-10-13 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d2927e6f-aef5-3300-b7fe-e6b1a4db3c4c | -17.338 | -53.8135 | 2025-10-13 01:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 110.6 |
| e867b01b-c6c5-363a-b08b-30ea99c798ad | -10.8093 | -43.9744 | 2025-10-13 01:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9a567c27-2c94-33a5-bd27-2aa114efb68e | -14.3015 | -51.5573 | 2025-10-13 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |


[Clique aqui para ver as próximas entradas](README5.md)

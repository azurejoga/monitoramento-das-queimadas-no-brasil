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
| 68a1ee23-a2c1-31f1-ae5b-1091fac703a8 | -11.9406 | -51.75626 | 2025-06-22 00:22:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 07d9325e-dd76-3ecb-be57-08589f7b977f | -7.87791 | -47.8894 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 50faad28-d71a-354d-ae3d-68f600a9d407 | -8.60421 | -51.5761 | 2025-06-22 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| fd3e9de8-cf64-34eb-b2f9-327ed75ec993 | -10.98799 | -45.08302 | 2025-06-22 00:22:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| baf00fac-08bd-35fb-8cc7-a266c7e65817 | -9.20765 | -40.28437 | 2025-06-22 00:22:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 90edeb30-bb01-34d4-9989-8e248aabee29 | -10.65077 | -44.49306 | 2025-06-22 00:22:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2255a454-042e-39da-9106-ef4c750978ca | -10.01703 | -44.50492 | 2025-06-22 00:22:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de25b053-5d5e-34ea-af51-59fd3972b308 | -8.01374 | -47.6641 | 2025-06-22 00:22:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 34768737-9b2d-369d-94a1-7d47d8b7650b | -8.60022 | -51.58175 | 2025-06-22 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| fdd5a195-17bf-3e77-b05f-41f366c525ba | -8.0703 | -43.0981 | 2025-06-22 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| de9b9999-f344-338f-aabf-14e9dbfce21c | -10.9324 | -57.1312 | 2025-06-22 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e3cbd014-30e9-3366-b398-93392455379e | -11.0006 | -45.0847 | 2025-06-22 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 3105bc88-5a12-36ac-b9f1-c313cf88fb6e | -11.617 | -58.289 | 2025-06-22 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 20b9c84c-5e6b-3926-98c9-664322379920 | -10.9815 | -45.0874 | 2025-06-22 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 386910ff-28d2-32f0-bb4e-021fa2a18573 | -11.0006 | -45.0847 | 2025-06-22 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 527a2874-ff95-3d01-ba12-4f0b5e8245b0 | -10.9324 | -57.1312 | 2025-06-22 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 49da3c58-6302-31a1-895e-f48d912c8fb4 | -8.0703 | -43.0981 | 2025-06-22 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 2ed3b355-d528-3383-ba73-2b2a4da6eb76 | -11.617 | -58.289 | 2025-06-22 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 7277ff05-68b9-3611-904f-d1e94d21f42b | -9.4622 | -56.0614 | 2025-06-22 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 456ec0be-cf75-3b2e-acc0-2984d4b69df1 | -8.0342 | -47.642 | 2025-06-22 00:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c00de38d-e6cf-3627-8049-305621b54244 | -10.9815 | -45.0874 | 2025-06-22 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| c0fd1498-455d-37df-be13-a2ab63d68ddd | -10.9815 | -45.0874 | 2025-06-22 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4931d625-b753-395c-a22b-ee71ed233ab5 | -10.9324 | -57.1312 | 2025-06-22 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 90e56c32-03f1-39ff-84e7-a74402b0811b | -9.4622 | -56.0614 | 2025-06-22 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f44e78af-a67b-378a-b3d4-61c6dfbc71d4 | -8.0342 | -47.642 | 2025-06-22 00:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 73cb91b7-f5e1-35eb-81a4-ea2b2c730f77 | -8.0703 | -43.0981 | 2025-06-22 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| e22eb23d-1226-3800-a6ae-bfdd441adaf4 | -8.6094 | -51.594 | 2025-06-22 00:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 31dba8c4-0f50-3ef9-b0aa-4c4269a1bc2c | -11.0006 | -45.0847 | 2025-06-22 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 08b21329-2a3f-31ae-9465-a93cd1879873 | -12.4767 | -54.4302 | 2025-06-22 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 8cc840e2-ad40-3f9a-a1a1-3549594940ca | -12.477 | -54.4096 | 2025-06-22 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 6999a660-8607-34ee-8ac9-8d12a89b8b2b | -12.4767 | -54.4302 | 2025-06-22 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 114.4 |
| fc94f78c-3bf2-34d2-90a1-cfda432fac8f | -11.0006 | -45.0847 | 2025-06-22 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| ce4aaafe-f7b6-3301-9359-b7e0a382e8a1 | -10.9815 | -45.0874 | 2025-06-22 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| b23019a5-8b76-31d1-b444-40df41df6d7e | -8.0703 | -43.0981 | 2025-06-22 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 8cfb7ca5-9bac-3474-b77a-885f87e4261d | -10.9324 | -57.1312 | 2025-06-22 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 10740722-b48b-331c-b942-ac19dbca4975 | -10.9326 | -57.1113 | 2025-06-22 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| e9adb0fc-b76b-3ba9-820c-5540e36e11f0 | -9.4622 | -56.0614 | 2025-06-22 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8a1291e6-5cc9-3a10-8656-8bb3202c42e0 | -12.477 | -54.4096 | 2025-06-22 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| eda0f600-1279-30a0-869b-59531b11dcf9 | -11.617 | -58.289 | 2025-06-22 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 32bfd069-df61-3d42-97dd-84d6f14ad21a | -12.4958 | -54.4283 | 2025-06-22 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c0cd3ae0-cb81-34fd-adee-65fa415b5e11 | -12.477 | -54.4096 | 2025-06-22 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| be6b167e-a30f-3859-a00a-3fa5e3495580 | -12.4767 | -54.4302 | 2025-06-22 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 172.1 |
| fbbed24e-6ca4-32bf-8418-48898687f0e2 | -10.9324 | -57.1312 | 2025-06-22 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1068a7fe-2022-3f87-baeb-9e8f18f4c78c | -12.4958 | -54.4283 | 2025-06-22 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| e39c85b0-d2b6-3ff4-a0e0-7dc389f56b70 | -11.617 | -58.289 | 2025-06-22 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5bbfac89-57bf-3999-813b-b8aa37d178d3 | -8.5909 | -51.5746 | 2025-06-22 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e616811e-22a2-3f8c-91c0-d0b58c6eae2a | -9.4622 | -56.0614 | 2025-06-22 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f6809389-b85e-309a-a924-3cd0a539d719 | -8.5907 | -51.5955 | 2025-06-22 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 00bd0af9-eedd-3309-8251-a776ba4b3fef | -10.9815 | -45.0874 | 2025-06-22 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| d909756b-60eb-3fdd-a013-1836d3d8cc19 | -11.617 | -58.289 | 2025-06-22 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 1dce5ce4-9f44-323d-9472-16f926de3851 | -9.4622 | -56.0614 | 2025-06-22 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d73f0990-b8d3-35cb-b885-9fe241cf9c90 | -8.6094 | -51.594 | 2025-06-22 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6db65b22-16b6-3e8b-a072-5122c3d5da55 | -8.0703 | -43.0981 | 2025-06-22 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| c9cc586d-e5a6-377f-aaad-98ce526bd61f | -10.9324 | -57.1312 | 2025-06-22 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f0959158-1ce9-3b4c-8869-e8e9c5c8c3fa | -8.6097 | -51.5731 | 2025-06-22 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| a0c3b1ab-b13a-30ca-b720-e1034a1d9d6f | -12.4767 | -54.4302 | 2025-06-22 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| a8b9f6ed-63f5-3263-b315-d795aafc7794 | -11.0006 | -45.0847 | 2025-06-22 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 1c976a0e-7647-37ed-a9f2-7290ee6bf0b8 | -8.5907 | -51.5955 | 2025-06-22 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 127591da-5bfd-3be8-8f4b-16bc2c46122e | -8.5909 | -51.5746 | 2025-06-22 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 3f218fb1-8d55-3fa0-b3de-a7f9aed19ed7 | -12.477 | -54.4096 | 2025-06-22 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 79480d29-fefa-3839-818b-6a5cb1ec2644 | -9.4622 | -56.0614 | 2025-06-22 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d94e7be2-59a4-3f62-83cc-8ddfe5b60298 | -12.477 | -54.4096 | 2025-06-22 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 08db3fc1-8fea-317a-840f-8bb3cc7defb0 | -8.5907 | -51.5955 | 2025-06-22 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 9bc9bfd7-d982-342c-9aca-ad9230de703c | -10.9324 | -57.1312 | 2025-06-22 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 690f6b56-c708-34ac-8eab-acf12d77809a | -8.6097 | -51.5731 | 2025-06-22 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 07e20532-ebd7-3193-bdad-f32734d507b4 | -10.9815 | -45.0874 | 2025-06-22 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 311fe4e0-199e-3871-b7b3-6ffd63e21b96 | -12.4767 | -54.4302 | 2025-06-22 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 3cbd659a-d511-3079-b355-284fd8cda071 | -12.4577 | -54.4321 | 2025-06-22 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3516f165-c820-3c32-9940-6a2cf40ea730 | -12.4958 | -54.4283 | 2025-06-22 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 73e53e88-b9f7-37d7-a864-3f14e4204e49 | -9.553 | -40.3503 | 2025-06-22 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 6a491178-bb23-331c-8996-afa2433d455f | -11.0006 | -45.0847 | 2025-06-22 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 62a38304-8501-368c-bd33-236cd1510568 | -8.5909 | -51.5746 | 2025-06-22 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| b15fe851-a776-3695-865c-ef587462bb07 | -8.6094 | -51.594 | 2025-06-22 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| aacee0f3-7129-3423-a4ea-ff3ea72b5dd1 | -10.9324 | -57.1312 | 2025-06-22 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 424025ac-074b-3f26-af50-6cba6df22029 | -12.477 | -54.4096 | 2025-06-22 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| d4547b7f-7a28-30db-9e19-4806588fbecc | -12.4577 | -54.4321 | 2025-06-22 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 18018428-d963-301e-a0f1-15388e925e7d | -12.4767 | -54.4302 | 2025-06-22 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 175.2 |
| e477b99a-eabb-3128-8f64-3ae3fcb627d5 | -9.4622 | -56.0614 | 2025-06-22 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4bbfd8d1-8e64-36cb-b268-cf98841b0a61 | -10.9815 | -45.0874 | 2025-06-22 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 61990483-7875-350d-a94c-d35847790c29 | -8.5909 | -51.5746 | 2025-06-22 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0ec18e0f-4507-3f62-8535-4c1eb2e49975 | -12.477 | -54.4096 | 2025-06-22 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 38c5fff6-b199-3418-bda2-cc04eaf1a8f7 | -12.4767 | -54.4302 | 2025-06-22 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 92669fdb-3e26-3158-92fe-9ca1252fe73c | -11.0006 | -45.0847 | 2025-06-22 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2fd9632f-9d95-36d7-b677-e1ff6f11e023 | -9.4622 | -56.0614 | 2025-06-22 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| bbd9f003-90aa-36df-aa01-d911c88432e2 | -8.6094 | -51.594 | 2025-06-22 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 62481961-9f16-3e2a-8f8c-171633f24e99 | -8.6097 | -51.5731 | 2025-06-22 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a040605d-8c04-32e2-b2ea-6533fb0cc9a7 | -9.553 | -40.3503 | 2025-06-22 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 75e49a53-f386-3497-b3df-4ef5fe374133 | -12.4958 | -54.4283 | 2025-06-22 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 15fc3f46-3145-3f2e-af6d-23fd3c6d80fe | -10.9324 | -57.1312 | 2025-06-22 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d50cc73c-fd6a-3673-b832-ace1671947ec | -8.5907 | -51.5955 | 2025-06-22 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| dbd09e6e-3c22-3388-aec9-02606ce2ba7e | -11.617 | -58.289 | 2025-06-22 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 4678c659-a93a-3c8a-a6ff-9b3d4e2cbc4c | -9.5534 | -40.3254 | 2025-06-22 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 3ca3d769-5618-3d72-ba70-250f3ac43c84 | -11.61369 | -58.2827 | 2025-06-22 01:58:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 4502b26f-7896-3d59-8177-15509ed1efa4 | -9.92334 | -59.91406 | 2025-06-22 01:58:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 4658bdae-f6dc-3d9d-919d-230e330d16dc | -11.62347 | -58.28614 | 2025-06-22 01:58:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 3ab3acd8-d86f-349b-ac93-9088cec2edf7 | -12.477 | -54.4096 | 2025-06-22 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a61126a1-5782-3907-aef4-92cf2d3ccaf0 | -10.9324 | -57.1312 | 2025-06-22 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 96b091e8-a6a2-3ed2-9c8d-1ae54795b464 | -8.6094 | -51.594 | 2025-06-22 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7ca86f06-e398-3956-b3be-9b34b7e2e957 | -8.5907 | -51.5955 | 2025-06-22 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| dbf68b5c-80bc-3fa3-9f06-26b5cc0eae01 | -8.5909 | -51.5746 | 2025-06-22 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |


[Clique aqui para ver as próximas entradas](README3.md)

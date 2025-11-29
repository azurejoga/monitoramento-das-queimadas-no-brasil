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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb768277-df88-3163-86d7-42e4a5da2f12 | -20.4503 | -47.4995 | 2025-11-29 01:40:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 00034a7c-d61e-3c46-8c31-7e535111cd30 | -2.7845 | -47.4125 | 2025-11-29 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5e33ea8c-af13-37a0-bca0-7f0db79d6595 | -20.1807 | -52.3975 | 2025-11-29 01:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 69c1572c-320c-32ba-811a-cbc530f2ba73 | -3.2134 | -46.8283 | 2025-11-29 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| df547fd2-69b6-34d3-b784-316c645b2d27 | -1.4737 | -45.7907 | 2025-11-29 01:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2f1545ba-0e03-354e-9e8a-282838d83e9e | -20.2256 | -47.5285 | 2025-11-29 01:50:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 272cc8ce-3987-3fda-b795-57d3013f7b1d | -2.6322 | -48.542 | 2025-11-29 01:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5674bf59-77b9-3b77-a8e9-8c92068caaaa | -8.0507 | -43.1472 | 2025-11-29 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 6e6bc5c0-f15a-3af1-ac7b-ad1fd35bacb0 | -8.0318 | -43.1493 | 2025-11-29 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.1 |
| 5924859c-8844-39e6-8bad-b8de59f483a7 | -8.1633 | -43.2055 | 2025-11-29 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| def2536c-830e-34e8-88be-e6dc79ca0819 | -2.7845 | -47.4343 | 2025-11-29 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| aeceecc2-2014-3973-a630-acfdc849ff79 | -8.051 | -43.1237 | 2025-11-29 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 647ebcb3-d6a8-34ad-89b4-78c2f2ec7b0e | -20.4503 | -47.4995 | 2025-11-29 01:50:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 60fbfde9-5402-3c4c-b4ca-010aa7ca10a3 | -1.4923 | -45.7903 | 2025-11-29 01:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 65e8c6a0-8578-3453-b5ac-24d29df3c4f3 | -2.7845 | -47.4125 | 2025-11-29 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b9b56af4-03cc-3b21-9ad2-7a6c0ea68c2a | -8.0321 | -43.1257 | 2025-11-29 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 191.0 |
| 8cca6dfd-c059-365f-8f69-d2f25072d30c | -2.6341 | -48.0249 | 2025-11-29 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 36fe0ee0-9937-3443-b618-ff50b0ecdd4b | -3.2134 | -46.8283 | 2025-11-29 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d1969e52-807e-3e7d-93c5-d205df921749 | -20.1807 | -52.3975 | 2025-11-29 01:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b027544d-e4a3-3b2a-af84-1164e5ee1022 | -8.6789 | -44.2211 | 2025-11-29 01:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| db4bb5af-dac3-3aff-958f-49ef72f28b1b | -20.1813 | -52.3754 | 2025-11-29 01:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 112.1 |
| de42d0dd-1af9-30d1-9d5e-40aefada3a68 | -8.6789 | -44.2211 | 2025-11-29 02:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ab2091e5-ca06-3684-b0ba-4d73e0e11a8b | -8.1633 | -43.2055 | 2025-11-29 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| a2736051-3059-379f-b713-01d1485dc675 | -2.7845 | -47.4125 | 2025-11-29 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 1c5f4e18-ea21-356d-91ed-5a1cfde900b9 | -8.0318 | -43.1493 | 2025-11-29 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 745afa49-d6dc-3766-9304-77530cebad7b | -2.803 | -47.4337 | 2025-11-29 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| e3aa6244-1c5b-332c-8d09-12e6b96e128c | -1.4737 | -45.7907 | 2025-11-29 02:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 72955129-3825-3823-96b9-8d9cbfaa6e0b | -20.4503 | -47.4995 | 2025-11-29 02:00:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 4e38fb5f-693b-34c1-881a-d0f26839cdf5 | -8.051 | -43.1237 | 2025-11-29 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.0 |
| de552105-b5c2-37fc-a092-2523886c824d | -20.1813 | -52.3754 | 2025-11-29 02:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 236.9 |
| 1a831564-2245-377a-8aa5-95872f8b3597 | -1.4923 | -45.7903 | 2025-11-29 02:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| bf342c7d-416c-31a4-814c-2fa7520bf0ee | -8.0321 | -43.1257 | 2025-11-29 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 180.3 |
| f0e22349-a748-3ede-be86-71fd621e57ec | -8.1822 | -43.2034 | 2025-11-29 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 978e5d90-241a-3148-ae13-7767a80d53bd | -2.6526 | -48.0244 | 2025-11-29 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c4d6a3a7-13d7-3958-87d9-c5c91825944d | -20.2256 | -47.5285 | 2025-11-29 02:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 2f6c347e-c48d-3c53-be98-643c42bb158a | -8.0507 | -43.1472 | 2025-11-29 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 69bb731f-ca33-3cb6-8e9c-dbdc6962ea0d | -3.2134 | -46.8283 | 2025-11-29 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 8bceb23c-7a8a-31c7-8e08-583802eb9f9e | -20.1807 | -52.3975 | 2025-11-29 02:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 288cd45b-6b47-3aa0-bf81-0bc1d873db83 | -2.7845 | -47.4343 | 2025-11-29 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 95dafbce-5f79-3fb5-a4bb-965e748f6170 | -20.2016 | -52.3717 | 2025-11-29 02:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 95.8 |
| de071acd-9121-3e3d-9e0b-011b976efaa7 | -2.6322 | -48.542 | 2025-11-29 02:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| d0024233-16a0-3960-a87b-7c5a1b23370f | -20.4503 | -47.4995 | 2025-11-29 02:10:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 0255d5cf-9d34-3ec0-bbf9-818826ada72a | -8.051 | -43.1237 | 2025-11-29 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.1 |
| 090f0585-3073-329f-ac33-487e78d70143 | -1.4923 | -45.7903 | 2025-11-29 02:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9c6add40-03a1-30f3-9559-6855d38977af | -2.6322 | -48.542 | 2025-11-29 02:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 88cb07c9-dbd1-3e95-995a-1324dd7baf19 | -20.1807 | -52.3975 | 2025-11-29 02:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 128.7 |
| c1371d92-577c-3005-9d17-f5d4315cfbf5 | -20.1818 | -52.3533 | 2025-11-29 02:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 2abf7f4e-5a49-3239-bc60-bfa179947f12 | -8.1633 | -43.2055 | 2025-11-29 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 0f70d11a-9865-37fb-8d9b-fc8eb713280d | -2.6526 | -48.0244 | 2025-11-29 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 18ef1428-0d86-3bf1-a4ea-58d2f5a8ea96 | -8.0507 | -43.1472 | 2025-11-29 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 880fe135-a68e-3041-89a6-09a1a68c2330 | -2.7845 | -47.4125 | 2025-11-29 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2fc8a7e1-4a11-3569-ad9b-f46e1f88f875 | -1.4737 | -45.7907 | 2025-11-29 02:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 8f95a4d2-0965-3dd4-b0e1-49de40cf1c55 | -20.1813 | -52.3754 | 2025-11-29 02:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 57fe978b-ec91-3d50-beae-bc96495a9ef6 | -8.1822 | -43.2034 | 2025-11-29 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 85c4bdc2-7798-3aa2-8284-befd9ec990b1 | -20.2016 | -52.3717 | 2025-11-29 02:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 120.4 |
| f097130b-c270-307e-948d-27d7393d503f | -2.7845 | -47.4343 | 2025-11-29 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 4adf1e7a-3169-3231-9a89-5f66f526741c | -20.201 | -52.3937 | 2025-11-29 02:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d9494d44-7d93-3a11-b0a0-698876e51f72 | -8.0318 | -43.1493 | 2025-11-29 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 074036d8-bf46-32f7-baa4-2932215989e0 | -20.1609 | -52.3791 | 2025-11-29 02:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 95172aa2-e1e9-3e84-a680-7a47f1753c7a | -8.0321 | -43.1257 | 2025-11-29 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.9 |
| b226d018-a735-3fa7-b099-f31c65be643e | -20.1813 | -52.3754 | 2025-11-29 02:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 260.5 |
| ccfbe498-8c1f-3fad-86b4-137a2412c8e5 | -20.1807 | -52.3975 | 2025-11-29 02:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 3f2aefc5-886b-3cc3-9ed2-be9151356b86 | -8.0318 | -43.1493 | 2025-11-29 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 15854078-b8f6-382f-88c4-1742793f4020 | -1.4923 | -45.7903 | 2025-11-29 02:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4f169dfb-6513-3da1-bf07-996ed60ebc71 | -1.4737 | -45.7907 | 2025-11-29 02:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 388810ae-ed70-3a02-8182-f204c2fd4b93 | -20.201 | -52.3937 | 2025-11-29 02:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 152bf079-f906-3063-b992-578db660b836 | -20.1818 | -52.3533 | 2025-11-29 02:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a99dcfae-4e93-3ed7-b6ae-731da4d0dfe6 | -20.2016 | -52.3717 | 2025-11-29 02:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 25a6cb9a-95b8-3468-aa54-ab43527c3888 | -8.0321 | -43.1257 | 2025-11-29 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.1 |
| 896dff1c-7301-30f7-98e1-1364d3d23215 | -20.4503 | -47.4995 | 2025-11-29 02:20:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a50a1e9d-c578-3d65-b847-a92c45de794e | -8.0507 | -43.1472 | 2025-11-29 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 7e42c9b3-1fe3-3b48-9b83-31ad52adb05a | -2.7845 | -47.4125 | 2025-11-29 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ecc3ce3e-c285-3400-bf4a-56d243ca290a | -2.7845 | -47.4343 | 2025-11-29 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 3ac37b29-59a5-30f2-8167-816392301b8d | -8.1633 | -43.2055 | 2025-11-29 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| f8b32c93-7bbd-3fe0-8954-04cd361cd6ad | -8.051 | -43.1237 | 2025-11-29 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 77074977-f05b-3cdc-9c16-ab602976402e | -8.0318 | -43.1493 | 2025-11-29 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| c0dd5b8e-ae17-381c-8eab-560e3cbbb5c0 | -20.1807 | -52.3975 | 2025-11-29 02:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 3c798c37-673f-3ab7-95ee-9109dd737dec | -8.051 | -43.1237 | 2025-11-29 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 4f41ff11-d4e4-34e5-9b7e-8cb8c7a9d845 | -18.1415 | -47.1299 | 2025-11-29 02:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 11afa96f-bc56-30d9-a410-6a17b8faa9d7 | -8.0321 | -43.1257 | 2025-11-29 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 8a4a48bf-4c44-37ed-86bb-54283334bf84 | -2.7845 | -47.4125 | 2025-11-29 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 17f81a00-71fd-37cd-a0e2-4234265668ff | -20.4503 | -47.4995 | 2025-11-29 02:30:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 0440378a-7ed0-34a9-a264-550729d82929 | -20.1609 | -52.3791 | 2025-11-29 02:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 25e5c652-543e-3ce6-b631-20147aecefff | -1.4923 | -45.7903 | 2025-11-29 02:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 14ef06b4-5f61-3c40-b431-66bd010edee7 | -2.7845 | -47.4343 | 2025-11-29 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e81047ee-e5b6-3eb5-8183-002bf56e8e9c | -20.201 | -52.3937 | 2025-11-29 02:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 0d5acf32-3f8a-3e4f-b915-ff15b9d35f5a | -8.0507 | -43.1472 | 2025-11-29 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 7e2d21c4-a61a-3523-9379-fbecadc5f538 | -20.1813 | -52.3754 | 2025-11-29 02:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 218.6 |
| 3bd0e88c-47b0-39ed-bfc3-e36e43536541 | -20.2016 | -52.3717 | 2025-11-29 02:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 9dc75855-6c8e-3cc1-a398-249d6f747380 | -8.1633 | -43.2055 | 2025-11-29 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 673eb148-9aad-3802-ac8f-d54dc402f024 | -2.7845 | -47.4125 | 2025-11-29 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5ea55d22-ea96-3626-b3b5-127a0e3043f1 | -8.0321 | -43.1257 | 2025-11-29 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.6 |
| d8ce207c-b431-3a64-9780-737381581f39 | -20.201 | -52.3937 | 2025-11-29 02:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2557eabe-baff-3273-a549-763c067c290c | -8.0318 | -43.1493 | 2025-11-29 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| af07bcb3-a88e-3914-8533-78a820a6a005 | -2.5327 | -45.3843 | 2025-11-29 02:40:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| aa069576-3043-3708-9b42-b614302befc2 | -1.4923 | -45.7903 | 2025-11-29 02:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b846889b-6ccd-36c4-9346-f70672a480ed | -20.1807 | -52.3975 | 2025-11-29 02:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 137.1 |
| bb4d11f1-5c8d-338c-8ef8-ea255494b7ba | -8.051 | -43.1237 | 2025-11-29 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 44bc86c3-264f-383d-b99b-8fd8ac51a73a | -8.1633 | -43.2055 | 2025-11-29 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 0d79d7ac-dbaa-3d1d-8f5e-d63061b6ba43 | -20.1609 | -52.3791 | 2025-11-29 02:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 62.9 |


[Clique aqui para ver as próximas entradas](README10.md)

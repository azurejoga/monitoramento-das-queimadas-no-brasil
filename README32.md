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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ad16fdf-f9ec-3eaf-8b26-9c2500ff1972 | -6.51506 | -47.03414 | 2024-10-26 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0961128f-ee9f-3cfc-8a04-f0d8d0471d3e | -6.46737 | -46.72057 | 2024-10-26 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 290912eb-384f-349d-a5df-b3fe8e408588 | -6.46691 | -46.72322 | 2024-10-26 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d08fdaa-c1c8-3543-8875-fd8885682ae3 | -7.49349 | -48.0859 | 2024-10-26 03:55:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ae846f5-4cf0-347c-af01-ff91a5a5d7f0 | -7.4493 | -46.91405 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1d9ba66-1378-39cb-b8de-51a8a5866ed3 | -7.36299 | -46.9903 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4548cae0-2df7-3953-9107-a0aff7ed4a2c | -7.35895 | -46.99004 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c95f1e16-40a1-358b-8f68-033531fb158f | -7.35793 | -46.98945 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc26fab8-94d2-3363-ab0a-2bf3e9586066 | -7.07363 | -46.87852 | 2024-10-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a9e733b-5592-3f89-ad7b-e4f4df711bf4 | -7.06909 | -46.87481 | 2024-10-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a95a801-6120-3d56-9d3d-da88f79eae7c | -7.67237 | -47.31005 | 2024-10-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e2520f8-d18f-3790-bbd0-f8c2c17ca0c9 | -7.67182 | -47.31316 | 2024-10-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed82d782-3157-3524-9b9e-a3a3440d540c | -7.67126 | -47.31624 | 2024-10-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69a367c9-ea59-3163-9955-d5072673b3e7 | -7.66667 | -47.31229 | 2024-10-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b3693d3-c3e4-32ea-b580-ef2cd5308242 | -7.66611 | -47.31539 | 2024-10-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dd12656-95b5-3576-9fc3-14675433ecdc | -7.59428 | -47.08299 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7076335-09e5-3fab-a973-c6e225b5e94b | -7.59376 | -47.08589 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c5e75de-f46d-39f1-aa52-314e16fb9d91 | -7.58328 | -47.11518 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c8c2f84-d11d-3284-b6c9-e7726274f2d5 | -9.26904 | -47.91143 | 2024-10-26 03:55:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ed29eba-b31f-3dff-9d44-30867b18f742 | -9.26386 | -47.91041 | 2024-10-26 03:55:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4316ab2-ad6a-3762-89d0-5a3a2106f326 | -9.07859 | -48.00385 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24ffbc6e-0221-3407-b337-fb3fe99bfa78 | -9.07799 | -48.00712 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7321eb9d-95c7-35f0-9e3d-79407e92e4bb | -9.07335 | -48.00282 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc40c587-1c7c-3661-aec8-270e2328b861 | -9.07276 | -48.00608 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd921db7-2039-33d9-95e0-799e0dd2ed14 | -9.06812 | -48.00176 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c54c4a8c-785f-344b-aa33-3521524d6e41 | -9.06752 | -48.00503 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62331abd-606e-3ed5-b72c-5a633759290f | -9.05417 | -48.72511 | 2024-10-26 03:55:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b79f31b8-c177-3a13-a79c-8b667cfaea04 | -9.04933 | -48.72052 | 2024-10-26 03:55:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27d398a8-926c-3bc5-80ec-0105ca930638 | -9.04864 | -48.72424 | 2024-10-26 03:55:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6259a629-32fc-3770-977d-e4a4909091e1 | -8.97938 | -47.74935 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cac72f0-9dfc-36f0-882f-0afdfbb1b9fb | -8.90697 | -48.53954 | 2024-10-26 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6109d4f9-2a09-3a89-a3cf-3d788d033b70 | -8.90629 | -48.5431 | 2024-10-26 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c148009a-eebe-3ca4-9f10-28c02c21b378 | -8.90609 | -48.53909 | 2024-10-26 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b0dee4f-14a1-3c04-b906-2f3ac6347655 | -8.90544 | -48.54264 | 2024-10-26 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ff22b90-dcf2-3a76-ae92-e6faca44c593 | -8.89637 | -48.53053 | 2024-10-26 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a127f73-0b70-3f4d-b1af-7145cc5ecb15 | -8.89576 | -48.53391 | 2024-10-26 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63fd1a38-bad7-3ac6-bf6d-757023a5716e | -8.89514 | -48.5373 | 2024-10-26 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c26ed9be-99c1-345e-9c53-b9dba3cef195 | -8.80198 | -47.85861 | 2024-10-26 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7bde311-e770-3bb2-8b44-ff3509ca74a1 | -8.80141 | -47.86179 | 2024-10-26 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46a76182-0bb0-3fdd-b563-0fa36db63dee | -8.47413 | -47.81557 | 2024-10-26 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da72d51b-dc5e-3b82-9e99-6e5b7e481283 | -8.46945 | -47.81153 | 2024-10-26 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2db8021-7669-30fe-8a6d-57837d92aa80 | -8.46887 | -47.81472 | 2024-10-26 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbc2b747-511a-38e0-b908-a54d894c01ba | -8.46829 | -47.81792 | 2024-10-26 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a0bc85d1-0d76-311a-9c03-19a58611d3ea | -9.99302 | -48.84966 | 2024-10-26 03:55:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c7b1b98-a1c3-36d1-9d0c-3d34873deb37 | -9.99236 | -48.85319 | 2024-10-26 03:55:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b751ce3a-a92a-36a5-bb20-19a5c32e9a7a | -9.73992 | -48.26234 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 159f60a1-1eec-37fd-b65d-6fe56788bf97 | -9.7393 | -48.26567 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22a1ca06-e318-373f-be9f-64f32f3050e7 | -9.73592 | -48.25932 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a49a3649-6a11-3b9a-ba66-a2467625522f | -9.73534 | -48.26257 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3c093a7d-528e-313a-af28-9b1bd790dff9 | -9.73475 | -48.26582 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b0634b5-f15c-3b49-95c9-0bb49e4af445 | -9.73468 | -48.26119 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9bc7985c-3b93-3627-8248-e9be87def897 | -9.73408 | -48.26439 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 950ee974-711d-31bd-b6dd-d3acf65d31a6 | -9.73004 | -48.26167 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8b77067a-736e-3cf9-9696-1af2ffdfb7e8 | -9.72949 | -48.26472 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67f0856b-0386-3ae5-8b53-99a2ffc91d02 | -9.72937 | -48.26038 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f62a2034-08f5-302d-8a69-3008edff2309 | -9.72893 | -48.26779 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4450538-455f-3eba-9aff-5dcc1a657fe7 | -9.72822 | -48.26646 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1fcef5a-1222-3160-a80c-cbcac5b45fd4 | -9.72228 | -48.26896 | 2024-10-26 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c82c3ef6-15ec-34d4-ad97-17e5aaffdbf2 | -9.50512 | -47.80806 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 80b9afad-e47d-3f90-83b7-e860a49c2603 | -9.50455 | -47.81114 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7ba5ee57-faa4-386c-a869-2739d23bf8e6 | -9.50396 | -47.81431 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 33447904-e43f-3426-b8a2-d1cd4fdb1046 | -9.49941 | -47.81013 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 99f4bed4-949a-392d-a7e5-e10662ff6d4e | -9.49884 | -47.81323 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 205ddce3-d17c-335b-a7a8-687ed2afbde5 | -9.49825 | -47.81635 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f9b6b744-30b7-3c04-bbe4-cd6c381a11f0 | -9.49312 | -47.81533 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1605c42c-db97-33e8-90de-9c5a6e6d08b7 | -9.49254 | -47.81842 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5675933-5a1d-3d59-9d2f-c1d9a710d3fa | -9.49127 | -47.81545 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 545a1da6-f109-39e9-bd08-aab0927191b9 | -9.49072 | -47.81857 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71e59319-55d3-3de5-bd87-56be8a9aaee7 | -9.48797 | -47.81439 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4854eaf-3f7b-3368-97c6-73c4da141bec | -10.19526 | -47.62536 | 2024-10-26 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9203c0c-1613-336a-94e6-fbad25b5a198 | -10.19416 | -47.63127 | 2024-10-26 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cffc8d61-a295-33a1-b74f-8e82d1900aff | -10.18968 | -47.62741 | 2024-10-26 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1760b1a4-ac94-34c3-85a0-51ded9241859 | -3.48784 | -48.2427 | 2024-10-26 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4a57ac0-7fa4-3ff6-8383-3259179182d3 | -3.48702 | -48.24301 | 2024-10-26 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db398935-fe34-3d2d-bafc-64f4fa433ae8 | -4.8844 | -48.6633 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29c877dd-9430-37c6-8b3c-6d1539f46194 | -4.87204 | -48.56065 | 2024-10-26 03:55:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 385fd335-55df-3bc9-8459-fb9163df844f | -4.8442 | -48.6163 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01844770-988a-3894-9ec3-5f486a82771c | -4.84342 | -48.62073 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95018eb5-168a-3512-a420-d68f1828d800 | -4.8391 | -48.61098 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4f460739-4e62-3f98-9605-c1bfad277751 | -4.83831 | -48.61544 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b87c91d1-5aa8-3ecd-9d51-16171dd89c87 | -4.83754 | -48.61979 | 2024-10-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4bfc2ba1-2cc1-370f-b0d3-ea326f80872e | -4.7028 | -47.96138 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dd37464-a22f-3f3c-a0e0-308ba6111ee5 | -4.69958 | -47.96133 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45434b33-0616-34a7-8d8b-a1c3bc2d41e5 | -4.58267 | -48.01595 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a041755a-6210-320f-b61d-b9292fb385aa | -4.58133 | -48.02387 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| d5776759-ee34-3331-a612-7b46d18a6927 | -4.58066 | -48.02786 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| b9b932dc-7dca-3aa1-9dd7-da00d32216a4 | -4.57998 | -48.03184 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a89d98a8-1337-3504-b447-1b4bd5ea961c | -4.57876 | -48.0204 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 916b423a-94e0-3d3a-9e2c-d232816634a0 | -4.57806 | -48.02436 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e1011d62-1fbd-3cb1-bd32-16f42feca231 | -4.57736 | -48.02834 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1465657b-3041-3da6-b3d5-9fdaad439dee | -4.57663 | -48.03241 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2c11e3b7-2468-3e63-849a-870483290467 | -4.57634 | -48.0189 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 18e89402-9f59-3cc2-8d3a-b98204ed3ab6 | -4.5759 | -48.03655 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2fcbf610-a188-3cdb-803e-ffaaefc77f7e | -4.57567 | -48.02286 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 4a9ed897-5172-375a-b84c-3c6c4b9fdae6 | -4.57499 | -48.02686 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5fdcd7c2-5df0-37ee-b92f-f6445328da74 | -4.5743 | -48.03094 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5440e30d-6420-31d0-8a2b-f400e0714646 | -4.57358 | -48.03516 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a064d204-fe3c-32b6-b59c-b632bf07f208 | -4.57309 | -48.01948 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 85915c26-d872-375c-a35b-31b1360a8ab2 | -4.57238 | -48.02345 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d8ed6432-d069-3e22-9fe4-f60c64f20551 | -4.57167 | -48.02746 | 2024-10-26 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |


[Clique aqui para ver as próximas entradas](README33.md)

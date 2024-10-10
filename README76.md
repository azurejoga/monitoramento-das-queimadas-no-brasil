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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbd790fd-de30-3d6d-8c77-99d9b4243252 | -6.85452 | -47.34388 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa3ed843-2dc8-303d-b1de-52147b29e980 | -6.84687 | -46.92434 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad67258d-904a-3f6f-b621-1681db700f57 | -6.84624 | -46.92818 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 954725fb-e1c3-382e-b6ab-51d0fe605df0 | -6.84339 | -46.92377 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0802ca4-f10a-3c70-9f44-8a2abe90c51f | -6.84276 | -46.92762 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d27ef196-0222-37e7-b0b4-a4399ddf76bf | -7.94873 | -47.71536 | 2024-10-10 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 960a4aa3-6155-3f0b-922a-510cc6827235 | -7.94807 | -47.7194 | 2024-10-10 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dca2f17b-a2fc-3b4c-ba7f-aa361e6d5efc | -7.94517 | -47.71477 | 2024-10-10 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7b3a577-9e63-3c8e-bd58-88d556626451 | -7.94451 | -47.71879 | 2024-10-10 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38511930-922d-3272-8742-eb88d9e4d4f0 | -7.76673 | -47.03379 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 188687ff-1eeb-329b-9ff7-db4075757b7b | -7.76612 | -47.03761 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7d1678c-33c7-3cb5-9493-23de9999b5af | -7.7655 | -47.04142 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1653818-94f0-3597-a9e1-2f0d129f5f7b | -7.76264 | -47.03705 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85b242d8-74c8-389b-92c0-72a5f3ecea71 | -7.49383 | -47.20469 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dc2d29d-655b-35e6-984d-5974726f62af | -7.49033 | -47.20412 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc1b5217-a96f-3d4d-ab44-f85a66a7a34e | -7.43878 | -46.9664 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 493d8454-a92c-3cf7-9a74-be36a665b5b1 | -7.43262 | -48.35854 | 2024-10-10 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 218feeb0-c8ba-3f8d-adbb-fc4d6b306a67 | -6.67151 | -47.11304 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75cbe189-1769-376a-bb59-c6bdb93c26bb | -6.66863 | -47.10857 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 472ab0ae-fc7d-3f3c-ac5f-571f9a624772 | -6.66799 | -47.1125 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 097c31ca-dfa5-3e98-9228-bcf49fc8ea91 | -6.65302 | -46.74098 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e742472a-f00c-36e0-848b-5e2ef7e1c055 | -6.62196 | -47.08484 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e46b7837-9814-396f-99de-f579fb15050d | -6.5817 | -47.71684 | 2024-10-10 04:19:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c217e733-35ee-35ce-bb0f-e33875aedd2d | -8.55125 | -47.82508 | 2024-10-10 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 370c98c7-b050-35d8-9739-660abe531b13 | -8.26937 | -47.85223 | 2024-10-10 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db0aff7d-36b5-3b35-ae96-2c9edb59ae58 | -8.2687 | -47.85631 | 2024-10-10 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 710c6630-bf78-36fd-be07-ee2f00cc7048 | -9.10671 | -47.65397 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50bfcda8-cc47-341a-9931-a93f4227b581 | -9.09386 | -48.17457 | 2024-10-10 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b4a252f-a2e3-33d6-b361-762c115ecb68 | -9.07498 | -47.69456 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11d62923-f859-337a-98c3-da61b5bb7343 | -9.04433 | -47.81612 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0952749-ac04-389b-9cf5-4a3ca4527c66 | -8.99186 | -47.73777 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e80d60f5-28b5-34e1-ac02-5dfd99af415d | -8.98899 | -47.73324 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19ef9c78-039b-3006-b2a0-38e56cd7dda2 | -8.98833 | -47.73719 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cafa4b6e-5ac0-3732-ad54-1b6dbafd9d0c | -8.0437 | -47.19938 | 2024-10-10 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f31876a-c9bf-3d1b-b2ed-711f8b5f71a6 | -8.50065 | -48.63875 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dce5f64e-f51e-37bc-b874-7cadd92f2699 | -8.49984 | -48.63637 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ffd5ecd-6e08-36f3-9b39-a7c961a36cf0 | -8.49912 | -48.64075 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c2a91c1-62d0-363c-b935-f1a1cfd6bc0f | -8.49768 | -48.63375 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b982da79-db5a-35f5-beab-f9c0faddc792 | -8.49694 | -48.63815 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 519b04b0-aadd-3f51-8899-0f8c1e8308d1 | -8.49612 | -48.63576 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 928f36b9-0cb8-3402-b3fe-62b504eee235 | -8.49541 | -48.64013 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5419615-680b-3ab9-8781-e399f3f8962e | -8.49397 | -48.63316 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3199c2a-a2c6-3f0c-9b76-41ab4cebb30d | -8.49323 | -48.63753 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cd95e3d-61cb-3ab3-8e2e-bb9f70ae1302 | -8.49241 | -48.63514 | 2024-10-10 04:19:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99c25101-262d-3737-889e-59646c3c80ad | -9.92782 | -48.27897 | 2024-10-10 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8609509-5273-373d-accd-6139cefd6569 | -9.86839 | -48.26023 | 2024-10-10 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8e12696-4978-3af6-887e-bb9212ad39a2 | -9.86769 | -48.26437 | 2024-10-10 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfafdc9d-b4cc-3495-942d-290669994c60 | -9.8648 | -48.25972 | 2024-10-10 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddfb43a0-2a36-3c31-bffe-bc9277158106 | -9.8641 | -48.26387 | 2024-10-10 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ad1b559-fc56-33d8-8eb3-aa84bbfcefad | -9.85982 | -48.26743 | 2024-10-10 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 917f560a-e19a-30e0-8e7e-d388917d00d6 | -9.85888 | -48.26466 | 2024-10-10 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7aade516-660b-3944-b4c9-db9b0ddf8a81 | -9.61007 | -47.55462 | 2024-10-10 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a486b6e1-56a0-3060-9e9b-a25dee835375 | -9.36619 | -48.80279 | 2024-10-10 04:19:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d87faecf-35b0-392e-b4a7-61fd20dad5ca | -9.36544 | -48.80721 | 2024-10-10 04:19:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8b427d5e-7e3a-3a39-a1d4-bd5c075e40bb | -10.05542 | -48.74833 | 2024-10-10 04:19:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff343238-c6f6-3f6c-ae9c-c000efa19769 | -10.05104 | -48.75206 | 2024-10-10 04:19:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a70405fd-f4a3-3a48-b014-732c933d7854 | -10.04737 | -48.75152 | 2024-10-10 04:19:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56025448-8b37-3131-aaf9-0c4ef2ab6a32 | -10.03559 | -48.73201 | 2024-10-10 04:19:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ade9730-c07b-3ef8-8d8d-3b2c469fab2e | -10.01229 | -48.84786 | 2024-10-10 04:19:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d05defa4-1862-34b3-ae42-2a5b04a49570 | -10.00861 | -48.84726 | 2024-10-10 04:19:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a15b650a-c1e0-32fd-acd6-8818384c4201 | -10.00788 | -48.85159 | 2024-10-10 04:19:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b1e525cc-87e7-3c66-8762-2f344851d55b | -10.00493 | -48.84665 | 2024-10-10 04:19:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e95167df-2a14-3142-9b20-51e82bc158ee | -10.00419 | -48.85101 | 2024-10-10 04:19:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cddc6be2-6e85-31e8-94d1-b0a6226011d7 | -10.72826 | -48.72254 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 54e9c00d-05c9-3b9f-9739-6328904e151f | -10.68183 | -48.73258 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cefc133e-a4e5-3da1-91c7-9c8208defe0c | -10.67893 | -48.72762 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d745ceec-82d0-3f85-a07b-b851cf783de5 | -10.6782 | -48.73195 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cad4c5a-c971-32d2-9b3a-2be3b6c64c69 | -10.6775 | -48.71399 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05364cbf-2eaa-310a-99c8-c79082e54a4c | -10.67677 | -48.71834 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a0c8ad8-50c5-3b5a-be5b-1f9a28cf73bd | -10.67603 | -48.7227 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae088ab3-0eec-3f11-82fb-01c9901255e2 | -10.6753 | -48.72704 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae880082-0930-30b0-a515-16d8028e7ca9 | -10.67311 | -48.71791 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4289280-4fd3-3ec3-9243-4abb2af7a840 | -10.67166 | -48.72649 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e774ab94-67d3-383b-a592-21314ddf1335 | -10.66874 | -48.72168 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c39d2ef-7f1b-358f-bfee-8687f8d5f5bf | -10.61404 | -48.29629 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9872e138-05e6-3089-9c9c-4ffa48299b1e | -10.61156 | -48.29636 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6977cc63-942d-350c-8bf8-76eb8c20fbd4 | -10.61048 | -48.29571 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7afee88d-f981-361e-bda0-a650076465b8 | -10.608 | -48.29578 | 2024-10-10 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8758534d-e641-3296-a23f-75c37cf2e44c | -10.60726 | -47.70983 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd8ebd2b-25fe-3434-b4d1-0b9c33755a09 | -10.60443 | -47.70539 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bcf5a90c-ad20-3d40-950a-86a7338ecbba | -10.60379 | -47.70924 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92cef99a-876d-3a9f-8541-0ae221fda3b2 | -10.60096 | -47.70481 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2784417-7c1c-34fe-8e75-79bf707fdbaf | -10.57925 | -48.0295 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b433b2ca-29ca-38bf-85d2-94147762289e | -10.57638 | -48.02497 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9a0e071a-8152-3b10-84b1-04d5b9162bc0 | -10.57574 | -48.02888 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 48002f56-8a63-3973-a8ba-96a78f42d8b7 | -10.57507 | -48.03287 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c710b7d9-b4ef-3591-9a26-749452e57242 | -10.57288 | -48.02435 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0e5f2804-7efe-3e64-84f2-54434871f3e5 | -10.57222 | -48.02827 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d62e69db-b1b8-3014-99cf-4124acdbabb7 | -10.57156 | -48.03226 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4aa45387-0f3e-31fc-ad84-f3a6b8589aa9 | -10.57088 | -48.0363 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 133c10fc-2ec8-3372-9869-2e39d360b5e5 | -10.56936 | -48.02376 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 626bc4d2-c110-3177-a576-7076a05f8e79 | -10.56871 | -48.02769 | 2024-10-10 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2388b6cc-c795-3559-b039-739a6b15573a | -10.55552 | -47.75774 | 2024-10-10 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0107164-7c13-38ce-bef9-6ab9b5b5254f | -10.3123 | -48.88617 | 2024-10-10 04:19:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 847767f6-9e5f-36a9-8cbc-da09fb9c006f | -12.09358 | -48.65154 | 2024-10-10 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d246955-7513-3411-9ab5-89cf74a11f99 | -12.09289 | -48.65562 | 2024-10-10 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5d5b51f-6962-37f4-92c7-cbc2bdf39b02 | -11.71213 | -48.42737 | 2024-10-10 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7538824-e4ed-3638-933c-8ae72babde74 | -10.97903 | -47.88149 | 2024-10-10 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd0761a1-706f-3edf-9de4-b054db18dca4 | -12.72742 | -48.42472 | 2024-10-10 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cce1318a-9647-3d7a-a85a-4f465b861e2f | -12.71626 | -48.42695 | 2024-10-10 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README77.md)

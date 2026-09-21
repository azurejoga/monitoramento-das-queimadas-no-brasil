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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d78f142-f13e-3a1b-bdc4-0afc99ad3d86 | -5.12717 | -42.85215 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 63ed4a2d-503c-3266-a3ee-f48c9552c6a1 | -7.04659 | -43.69719 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dad08bc-1b6d-3d30-bd81-9af3224e67f9 | -5.88268 | -39.10947 | 2026-09-21 16:03:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9eeddd9b-bcf4-33ca-b2fa-49ea34b78f31 | -5.75265 | -43.72215 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b65420a8-a987-3042-8535-6f9f813c0f4f | -4.23018 | -51.22808 | 2026-09-21 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| d54932f6-06c0-3ec4-ac13-57aa22bddd03 | -8.37993 | -47.27954 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 66cf672e-2a9e-356c-a5a2-e17f92c76015 | -7.74144 | -46.79005 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 52989407-099c-347d-b08e-d010ad112812 | -8.36411 | -45.64335 | 2026-09-21 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| c74a32ee-36d2-3df4-ba3f-e422fc4713a4 | -6.38935 | -45.19501 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 89806079-b976-3741-91ce-79735b057c4f | -6.18407 | -47.49314 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6b34d0a2-0575-3a6a-b1a5-980599bbeba0 | -7.57381 | -46.73729 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 311ec544-1fb2-3a22-9275-399a6ae9fb69 | -6.08662 | -38.29911 | 2026-09-21 16:03:00 | NOAA-21 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 65ef5366-17f0-31d4-9436-0ec71f6ef631 | -7.73923 | -46.77341 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 25e31330-7c08-3ab0-a7e2-179514732a5b | -5.67934 | -43.42189 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1d991c7b-557b-3e76-bd4b-0a1a04a47962 | -2.94048 | -50.48981 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 45233802-8539-32cc-aa56-c9dddac6553d | -6.39801 | -45.18922 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2efa13f0-b34e-344b-9411-bec26f688fdb | -4.56026 | -38.07772 | 2026-09-21 16:03:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 59b9c60f-16f6-332a-823f-17a2685e3818 | -6.47358 | -42.76101 | 2026-09-21 16:03:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 637bd43a-5034-337f-b748-1f4dbd5ce645 | -5.39415 | -42.95078 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 21c05866-7af4-36a2-89c7-6494b5fb30a9 | -7.8761 | -48.92439 | 2026-09-21 16:03:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c262790c-d3fa-3f5d-9c61-cbcc5e8833eb | -5.76292 | -43.70532 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 52d249f2-7910-390e-af27-101e75f3f709 | -4.81418 | -43.62581 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e2feed2-5a3a-3be1-8f1e-26d0b687e8bf | -3.9224 | -38.46343 | 2026-09-21 16:03:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f8262b1c-9bb7-369c-a091-d903a9eee83c | -8.43921 | -45.81882 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 38f1f25c-f424-3d37-bce6-701266a071dd | -7.73512 | -43.88611 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 346ea6d0-29e0-39f8-ba69-2fee3c797368 | -7.67031 | -48.18381 | 2026-09-21 16:03:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 72564ad5-6735-3242-85fd-7a5fc38fc8be | -2.39163 | -48.08966 | 2026-09-21 16:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8ffdae32-cbc6-355d-8915-81d836f8fc0e | -5.61652 | -43.39103 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f47ea700-3374-345b-b518-af150f92a374 | -5.75875 | -42.64395 | 2026-09-21 16:03:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 8e1d814c-843d-3328-b452-5b2af7e5bf17 | -7.74805 | -46.71881 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 283.4 |
| d8e8315a-f312-3249-9c89-b80bc099a937 | -5.55876 | -45.515 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bf10b873-8a91-3068-8f34-2812ad7451f0 | -7.07599 | -44.30933 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 90e2f772-6899-35c3-98c2-89538f8a63a1 | -5.65027 | -43.4223 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 715d410b-e437-3d9f-83db-06599dc925dc | -7.06456 | -41.8263 | 2026-09-21 16:03:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 76617a82-daff-340b-89ed-d7bfe5c71f19 | -4.40035 | -40.73287 | 2026-09-21 16:03:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 68c05246-83a2-3cbd-acf5-1ecc2931535d | -3.34193 | -42.76485 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3b43269b-b224-36fb-bd7a-5569e78659b3 | -7.57863 | -46.73333 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 106a6c52-4d70-31b7-bbc0-31d2d9b89f33 | -4.35559 | -41.96869 | 2026-09-21 16:03:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 593634f7-99ec-3261-b078-38345ef366ac | -6.45218 | -44.91301 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7787396f-0fc7-3f8b-b196-39a262c56a5c | -8.61868 | -47.29974 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5567bf9f-14b4-3bb6-b15a-3fd09802a03c | -7.06506 | -43.67404 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0b7b2de4-c71f-322b-8e12-59a96999b86f | -4.05956 | -45.68377 | 2026-09-21 16:03:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| f85c5595-58f9-3b81-94bb-8842937371f4 | -7.16492 | -43.02018 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 72aa6cbf-cc01-3c5f-bf7a-2e7f55bc3dc9 | -7.08204 | -46.28721 | 2026-09-21 16:03:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df105ac7-3a8d-3ded-a296-3b809caebc28 | -5.17128 | -42.88127 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 711118f7-43d6-34cd-a6e5-5ccbc0d37f79 | -7.54165 | -47.32534 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 98b6d868-c851-3535-83cd-61dbed6e86b9 | -7.8849 | -47.65885 | 2026-09-21 16:03:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ccc6e63e-4bc6-3cf1-8269-20872a3133f0 | -7.3733 | -44.63209 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3395c461-fd55-3bb4-970f-5c9cc663dda0 | -4.89891 | -43.46304 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a3614186-7d15-3783-85d0-579b834319c1 | -6.53825 | -44.92481 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d05fa599-106a-372d-b436-fe22a8288166 | -3.72167 | -45.27481 | 2026-09-21 16:03:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1b1abe1f-f3dc-363c-aaf4-45cabcc3324b | -6.92177 | -42.94939 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 06cc9ff5-c3f0-3ec2-8660-fb0d501c5c60 | -6.98801 | -47.47458 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9e27717-5e01-3947-ac00-9fabc7128848 | -6.31045 | -47.62415 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f4f7f0dc-b4c3-3b2e-8b99-579ab561825d | -7.31818 | -46.74927 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 796594d2-88f8-3705-9f7f-0bb6efbaa698 | -6.27289 | -41.65289 | 2026-09-21 16:03:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8e6929f9-4146-3da3-970e-ca5c6e96e202 | -6.0073 | -45.24758 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 41c917ec-cf54-37ae-bfdd-110aa2936e06 | -7.40946 | -44.78955 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a2e0051f-f67a-3f67-9768-5b357c0b1a44 | -3.2489 | -42.99654 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b2d05806-cd60-3f24-a2da-aa01ee268de3 | -5.81267 | -43.862 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ccf5350b-5536-33d9-8b9a-dbed5cb1beb5 | -7.17148 | -37.72083 | 2026-09-21 16:03:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 22d2ec6a-392d-3b21-9f72-36045e262fbc | -5.53654 | -47.42518 | 2026-09-21 16:03:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1814e996-4036-3b66-8952-74c34b4060d0 | -6.90317 | -42.93422 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| f119130c-278f-34a0-aedb-33568f679458 | -7.00425 | -43.29604 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| a0c510c3-f887-39f3-bffd-49fe6451dc6f | -4.11638 | -46.40075 | 2026-09-21 16:03:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| ed31f8d9-e38d-31e1-958f-c8b1e454ad73 | -6.48888 | -44.77132 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6ab56742-8954-3dd4-896f-a00330d4de45 | -7.03471 | -43.67464 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ef35f09f-bed9-3b87-a89a-725d6c5f0816 | -5.75689 | -47.28622 | 2026-09-21 16:03:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 296d2627-8774-3e9c-8cc4-c072fc829acd | -6.56676 | -45.54372 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 41b8492b-06b2-3105-8dab-d27a71d4fa2c | -7.03192 | -42.08121 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 9bfa47fa-8f58-336c-b956-25601208f0bd | -4.2377 | -51.23287 | 2026-09-21 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5f8270d5-f997-3cd6-ba91-cc14a9fe1c45 | -5.98829 | -44.71955 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| ac8f23a1-ca5f-3f19-a832-8608662e43a3 | -6.39077 | -45.20491 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ced9733f-d91d-35c1-95bd-30c0718abae1 | -5.137 | -42.75592 | 2026-09-21 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e10ea7a3-63d2-3d94-b614-41112aa37cfd | -4.31856 | -43.9087 | 2026-09-21 16:03:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| af4a3571-a6c1-3ece-b371-8156703779e2 | -8.36699 | -47.18227 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 58c4fa43-177c-3d9a-a104-dea0709d4f89 | -6.15965 | -44.182 | 2026-09-21 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32039c5a-4b8b-3032-8b27-824f70b5759d | -6.45285 | -44.91768 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f241c8fd-e783-3e92-9046-bbcdd859b37a | -6.08609 | -38.29566 | 2026-09-21 16:03:00 | NOAA-21 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 395be2b4-54da-3569-8c8a-9d5a5264e7be | -6.92528 | -42.94529 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 350f72ee-2b65-3a7b-b0a0-d47963ef2b30 | -4.22297 | -48.61443 | 2026-09-21 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| aaba13f1-9621-31fb-9303-f0970f3f52fe | -6.92566 | -42.89136 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 1bfeacdd-221a-39da-93bf-dd0e0eb6e7e2 | -8.41366 | -47.53383 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0eaef28-7fed-35a3-b7e2-b8427bd97d24 | -4.85293 | -40.52347 | 2026-09-21 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 782d6ba2-3783-3dec-8220-58fea0256ee9 | -5.83167 | -47.79118 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 989e1b63-726a-3e6d-828d-ba756b581bb0 | -3.66549 | -40.55536 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 64e056b5-b1e7-3238-9640-5910bfad91a3 | -7.74541 | -46.77935 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 28d3e08b-6f94-3b1f-a473-b9fde18f9675 | -5.76485 | -43.70458 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4aa72aad-68dd-316e-95ee-659c3d7820e6 | -2.16747 | -48.32052 | 2026-09-21 16:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 93db7659-99fd-3811-8e00-e9b7f2b3317b | -5.61329 | -44.8411 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 05420cdb-e55d-3f5f-ab5b-b79e62038143 | -5.61554 | -35.40459 | 2026-09-21 16:03:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 95228e3e-178a-35be-b81a-0829db03456b | -7.00132 | -43.29697 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 077fb38a-f527-3de5-809f-c3fd3e279109 | -7.16518 | -44.52285 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d9735c8f-3967-3f8d-8d19-0f223bf9a396 | -6.99306 | -43.29807 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| d61c9840-1f15-32a3-aa4f-63394d708f75 | -6.54581 | -42.56861 | 2026-09-21 16:03:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 6ec3cbf0-a74e-30f9-95b8-60e369a1d1a6 | -5.56029 | -41.56058 | 2026-09-21 16:03:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c2aa4370-b547-3088-8ed6-0e70edc53f3c | -6.90164 | -42.92359 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| c6581055-ff69-3122-9a17-1d32bd52c6b0 | -3.3488 | -42.75915 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d36adecd-5555-3842-b79d-a66f230fb6df | -7.63576 | -45.42323 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2385eda4-c49b-329e-8f29-07d04f2c035e | -8.31198 | -46.01308 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |


[Clique aqui para ver as próximas entradas](README173.md)

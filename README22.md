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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b06d6ac-6bc7-3749-9fc5-c5003874cc56 | -0.8784 | -52.7444 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee0c2c4-0e3e-34ee-ba57-55addb327113 | -2.3148 | -53.877701 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47402c48-59a6-3eff-b70c-c1580cdb0cd4 | -3.1139 | -53.994099 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26780871-cab6-3efc-98cf-4f1c5c8cce93 | -3.5238 | -53.812599 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40cec19a-1ae8-399c-bd05-4791b1ef8000 | -1.2451 | -54.006302 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c79799b6-4b9d-3732-a72d-202a3ee33279 | -2.0352 | -54.4832 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd0a9fd5-a54d-3814-9e7b-67c36b639189 | 0.3993 | -50.856602 | 2024-11-24 01:22:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c2ab23a6-0d9d-36d2-82ee-c551df8d2261 | -1.3053 | -51.726601 | 2024-11-24 01:22:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04dbabdd-b017-3531-95f8-82e0a72c4320 | -2.5777 | -51.864799 | 2024-11-24 01:22:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6079e571-239c-3ff0-b712-25a5f4a95c19 | -3.192 | -54.762402 | 2024-11-24 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0febcd04-86ab-32d5-9221-436995122404 | -3.2199 | -53.920399 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e5a4106-8cfc-3569-a381-5c01a4e00e1a | 0.409 | -50.858799 | 2024-11-24 01:22:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc84061-edb9-327c-89ca-718b258db21b | -3.2659 | -53.810001 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a836a957-0b3c-3ee3-ac2f-b44ad5b62615 | -2.8633 | -51.8153 | 2024-11-24 01:22:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5702f9b3-405a-3104-8186-fd703523f28f | -3.4806 | -51.993099 | 2024-11-24 01:22:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95b7b27d-243a-3bb1-a689-7a6b3ec17293 | -0.8856 | -52.775002 | 2024-11-24 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 513c51a9-de2d-39de-94a6-2a5ad489c748 | -5.9586 | -48.034401 | 2024-11-24 01:22:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c351082-9630-34c2-9e76-9eee8224fc5d | -3.1166 | -54.005798 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d921207b-f607-3771-b489-26e9c2c125f6 | -21.3223 | -55.940399 | 2024-11-24 01:22:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 036ddeee-2c0a-30d7-a3c4-1bbaebac47db | -3.2527 | -53.277 | 2024-11-24 01:22:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79c50e92-c0fb-3f44-90f1-995a137bcbc8 | -1.4051 | -54.471802 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aa8451b-e692-38d7-8928-9436f69e449c | -20.3274 | -48.821201 | 2024-11-24 01:22:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7e2e22ee-f09f-373b-b29a-5c0eca9de946 | -3.2784 | -53.819698 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75fd8384-d7bf-3dba-890b-2370b3c29061 | -2.5918 | -54.224098 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 315f553e-51b0-3368-b7c2-5ac52934bc0b | -1.2325 | -53.688301 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fff6d05-7903-3b0c-8143-fc91370d7f70 | -1.5109 | -54.1763 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90b57508-5609-3410-ac8e-cd5d6e87e371 | -3.521 | -53.8008 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5212a67-23c8-39f5-a359-33fcb953eae3 | -1.7737 | -52.713902 | 2024-11-24 01:22:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba512630-632f-3f7b-8fe7-7a32709d9d84 | -1.7565 | -54.523201 | 2024-11-24 01:22:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b796f767-fa90-347d-87b6-aa1c941bfe0b | -1.2196 | -53.677399 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 270bf12a-5e83-33b4-bc36-9e3bccd4785e | -2.5816 | -51.881302 | 2024-11-24 01:22:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 826d6d2d-6df8-3465-8e8f-cfec397512fb | -3.2297 | -53.918098 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 371b3711-0765-3a19-b5fa-ad29fca77737 | -1.5137 | -54.188202 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a532f7db-99e6-393d-9092-34b04eb664cc | -5.9654 | -48.061199 | 2024-11-24 01:22:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3c155f1-4039-3241-849e-466918d7fca5 | -3.2486 | -54.215801 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccb081ac-9f29-346a-b73e-61d961b6f62f | -3.514 | -53.814899 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a445999-a5f3-3ecc-a35d-fc94eb575b95 | -3.2583 | -54.213501 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d68469c8-496f-3e87-910c-266497ebc2a6 | -1.5256 | -51.619202 | 2024-11-24 01:22:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4532c3f0-6e8e-3d31-8692-de91d0444b23 | -5.949 | -48.0369 | 2024-11-24 01:22:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 855b5f01-eae3-3d68-b561-5d63883a50a0 | -3.2756 | -53.8078 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7c103f8-4244-3beb-aff2-c8d5c60020a0 | -1.2227 | -53.690498 | 2024-11-24 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 439f6038-4e9d-3f2c-8024-00feaf5fac0d | -1.7538 | -54.512001 | 2024-11-24 01:22:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbf154fa-968c-367a-92a1-d2592d0b3873 | -1.5206 | -54.174099 | 2024-11-24 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89727151-e4ea-36f2-a73c-c354d4789a8b | -1.2955 | -51.728802 | 2024-11-24 01:22:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea45371-2fba-313b-852b-21edcae407a4 | -3.2609 | -54.224701 | 2024-11-24 01:22:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347aa8e4-3662-324b-aecb-e3084a125ec5 | -1.5129 | -54.1959 | 2024-11-24 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5c997b15-4b20-3cdb-a9cc-25833c0e1352 | -3.0582 | -53.2192 | 2024-11-24 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c80cca61-bfcf-3d93-83ea-8fa4c190ef02 | -5.9557 | -48.0425 | 2024-11-24 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| af43939f-1c38-3dc4-b99b-c9a1ea33922f | -1.3666 | -53.8362 | 2024-11-24 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 9cb88594-4dd9-3e62-a429-a6bde06444fc | -3.2928 | -45.7384 | 2024-11-24 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 169.3 |
| fc911578-e821-35ef-81fb-57967070ce86 | -1.6195 | -46.8726 | 2024-11-24 01:30:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 02323765-3699-3272-a4e4-47dcced95722 | -2.4456 | -49.0816 | 2024-11-24 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e8666875-a015-37d5-9217-c1d26ee98f40 | -3.5159 | -53.8132 | 2024-11-24 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| d7e7b3ce-d9af-3dd0-b40c-51e4581d1fcd | -4.242 | -48.6978 | 2024-11-24 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| f5fba2e0-cb25-373f-b364-178eb9c8632c | -2.7411 | -49.1162 | 2024-11-24 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 00de2fcc-43e9-3cc2-b547-e7f4e89603a6 | -2.741 | -49.1375 | 2024-11-24 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 35c1281b-52d9-3ae9-9fd8-0a6aba55b0cd | -4.0848 | -50.36 | 2024-11-24 01:30:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0eb163e4-3ce6-3e54-b24f-ca0933d04ff6 | -5.1185 | -43.1497 | 2024-11-24 01:30:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 71e1ecf7-98eb-3065-812a-04c98c249756 | -1.5129 | -54.1759 | 2024-11-24 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| bc867bc4-5682-32be-8b21-147a168a6c46 | -2.2137 | -46.3965 | 2024-11-24 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| f40d459d-e4c9-3f6b-bc16-806c90cb4da0 | -3.1068 | -45.7903 | 2024-11-24 01:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 14e21473-ae44-3ceb-ac7e-c6cfffb4e196 | -4.2419 | -48.7193 | 2024-11-24 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 07a73ced-7a3a-3d20-a0a3-f1113efaf958 | -1.601 | -46.8729 | 2024-11-24 01:30:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b1735198-fb12-34ec-9d57-da1b1c834341 | -3.2929 | -45.7161 | 2024-11-24 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 8e611b65-71f6-36f6-b7e7-66576f2db0b9 | -2.464 | -49.0811 | 2024-11-24 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| aaef5eaa-c16e-3d5f-847a-02b2987f2616 | -3.3115 | -45.7153 | 2024-11-24 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 89e842f8-2d87-39ff-816e-2c90ea063b80 | -1.6195 | -46.8946 | 2024-11-24 01:30:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7c6627bd-fda5-30f1-a7a7-f587da00b016 | -3.3114 | -45.7377 | 2024-11-24 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f1f32f16-a4d0-3248-b765-5f049e36eb28 | -1.8239 | -46.6265 | 2024-11-24 01:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| ff89116b-0ade-3766-815e-70d5f62df74d | -5.0998 | -43.151 | 2024-11-24 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 5855f57b-a070-3220-a55d-ba244ef5196f | -3.2386 | -54.223 | 2024-11-24 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9257e3ac-d2f8-31e7-a988-d9a9789fafe7 | -1.8238 | -46.6486 | 2024-11-24 01:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1bf979ec-ed19-38b2-80b0-dacd67613ae0 | -5.9556 | -48.0642 | 2024-11-24 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 6a19df75-651e-3911-9218-cbfb07bf8df7 | -0.8723 | -52.7686 | 2024-11-24 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 973045be-2907-3ae8-ba9a-d47aab84d4bc | -1.601 | -46.8949 | 2024-11-24 01:30:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f39cd455-cb7f-3742-8095-f4d3fc2bb8f1 | -3.0355 | -49.4476 | 2024-11-24 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3bc5f27d-ecb2-34b3-8736-e79dd447249c | -2.7411 | -49.1162 | 2024-11-24 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| fb421e2f-91cd-3d5c-a836-7d51527c42cb | -2.7149 | -46.2713 | 2024-11-24 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a39fcdb1-12b8-3fd1-9f6b-86ee84156f6a | -3.2386 | -54.223 | 2024-11-24 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a36770b7-18d0-3b3c-830f-6b88a6f91bb6 | -3.2929 | -45.7161 | 2024-11-24 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 134.3 |
| cff33118-5827-3e48-88b6-9785df6502a3 | -3.0582 | -53.2192 | 2024-11-24 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 656ea79c-cb14-3be1-bb07-20dd9b93880d | -3.0355 | -49.4476 | 2024-11-24 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b2a6bb5e-df0a-3e38-8cd7-e1b36dcd3821 | -1.8238 | -46.6486 | 2024-11-24 01:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| f74e99c7-b02f-3773-b381-81e2446b5ab1 | -1.6195 | -46.8946 | 2024-11-24 01:40:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f58fc9fb-3960-3be8-a515-5d727efe08b5 | -5.0998 | -43.151 | 2024-11-24 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 49e82d52-89b1-3e97-8b4e-6d7168cd7265 | -1.5129 | -54.1759 | 2024-11-24 01:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e626d3d9-3819-3a49-882e-caca51938b86 | -3.0354 | -49.4688 | 2024-11-24 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| aca0d046-9217-30f5-b966-dad436778f1b | -1.3666 | -53.8362 | 2024-11-24 01:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 7803e0e4-bc7a-33a1-881e-3a1123d25430 | -3.054 | -49.4471 | 2024-11-24 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| e6a1f746-e23e-3136-b23f-9d1aa018d38a | -3.3115 | -45.7153 | 2024-11-24 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ed3802d5-376c-3b82-9e4a-f684918fe57d | -2.2137 | -46.3965 | 2024-11-24 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1452de6a-096a-3ddc-971e-9048e846e4fb | -2.4456 | -49.0816 | 2024-11-24 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7b87e220-d13b-3d34-b064-b08a67c6f53b | -1.6195 | -46.8726 | 2024-11-24 01:40:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| b2f52965-e6c8-39ec-9e95-689230f0715c | -3.8417 | -44.0594 | 2024-11-24 01:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 12e60b82-a0ac-397f-81cf-b24792e523f0 | -1.5129 | -54.1959 | 2024-11-24 01:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 052ebe23-6cf7-3732-b200-ca048fffd0f7 | -2.7596 | -49.1157 | 2024-11-24 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| d8854842-111b-348a-8da6-349739ff29cb | -3.3114 | -45.7377 | 2024-11-24 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 92c55c1f-616d-3a8b-9738-86d5bd6bec93 | -5.9557 | -48.0425 | 2024-11-24 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 58f0d256-03d3-3eec-9ba1-f46c41bbfd5c | -3.2928 | -45.7384 | 2024-11-24 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 184.9 |
| 9a4e3566-07c2-3a1f-86ac-d80e22c60f12 | -4.242 | -48.6978 | 2024-11-24 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |


[Clique aqui para ver as próximas entradas](README23.md)

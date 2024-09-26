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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9155ac7-1f87-3b7e-871d-d90a749db221 | -11.39202 | -46.3852 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| c7995492-7aac-33d4-bd7b-06c51177c768 | -11.28734 | -46.29102 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 004fcc00-12ff-393a-b08b-c4ce105d867b | -11.286 | -46.28101 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 027219b1-a42d-39ad-8745-980fc7833aec | -11.27523 | -46.27204 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 75938aea-b467-38d3-be77-778070f3265f | -11.22417 | -45.48719 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4627dff9-2b70-39f6-9cfa-e31b7bc46551 | -11.22016 | -45.52615 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ac631cee-8c5d-3211-bbb6-c82a3777b207 | -11.21889 | -45.51669 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 29c301c5-8c5c-3d8a-ae95-07b3c432dbf4 | -11.20201 | -45.52873 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f6b57bc4-44a1-3cbf-be93-c6a03e9d4a5f | -11.17614 | -45.53909 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e96a935f-8c51-37e5-a77a-55ef0bc36990 | -11.14286 | -46.18323 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8e62e3d1-f9c4-3b19-bd39-0febb7d62518 | -11.1322 | -46.17451 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| e85a7c90-2713-37fb-8c82-2d21b40c1196 | -11.13088 | -46.16457 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| f43436ed-5600-3b0e-8bac-84486af785ca | -11.12824 | -46.14472 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a56939eb-cf0a-3623-b54c-2f756ba21082 | -10.99588 | -44.42487 | 2024-09-26 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 323083f6-0f6e-379f-8d79-d090117ab051 | -10.98827 | -44.43513 | 2024-09-26 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ce02294e-1978-3626-95fa-805886a3e1cb | -10.98703 | -44.42615 | 2024-09-26 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 6bab927e-6f23-302f-8cf0-c19141572e4f | -10.83883 | -45.90321 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 3357f2bc-8805-3f0a-92b0-fa800c69d10c | -10.83623 | -45.88395 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0f90f4f0-7f9f-3fd4-b9b4-7334ffa16640 | -10.82836 | -45.89494 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5d32eba8-5b6e-3e3b-b129-33c685ef63bf | -10.82708 | -45.8854 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9c4aa8ab-2843-35a1-b897-a9cb0fc8f058 | -10.76395 | -44.61395 | 2024-09-26 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 29a0d921-2fcb-36f4-8a0b-e607e9a0bdd1 | -10.72633 | -45.20901 | 2024-09-26 00:43:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5fc5f1c8-b20f-3362-8fbe-0c375d212e6c | -10.67473 | -44.5049 | 2024-09-26 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b3826b2-424a-373c-8246-29d1d37aaee0 | -10.66588 | -44.50618 | 2024-09-26 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eeb94899-7b86-318d-a20f-a02a57d5e487 | -10.62985 | -45.85614 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bd48e593-0c0a-324c-a75b-a808eb08f8dc | -10.62858 | -45.84665 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a6236801-d394-3591-9a40-a9af68adfd61 | -10.60773 | -45.83009 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dc9c029b-58fd-3a5f-a900-a8dcde7aa9fc | -10.46792 | -45.81301 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d3f4c842-5ada-3185-972d-cce14a59d1cc | -10.4588 | -45.81429 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 19618e04-13f3-335c-ba5f-a413d1105f13 | -10.45751 | -45.80476 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8d40cbec-4b6b-3596-8667-a58b6ef77222 | -10.29914 | -43.52767 | 2024-09-26 00:43:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b498fa53-369d-3a68-aaf0-3236a4605cf9 | -10.00783 | -36.04702 | 2024-09-26 00:43:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 44.9 |
| 492a04d0-6d67-3ee0-8b4a-d6c8edf4f233 | -10.00736 | -36.04155 | 2024-09-26 00:43:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 59.0 |
| c23411e1-c33a-3c41-b8c2-fbb9b685b33f | -9.80951 | -53.57097 | 2024-09-26 00:43:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 3d9b81dc-3e0f-3d8d-b5c6-28f3ce3274d9 | -9.80273 | -53.56508 | 2024-09-26 00:43:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 397c9d51-28cf-30c8-8d39-8a98a01b43c1 | -9.60131 | -50.16153 | 2024-09-26 00:43:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 0e242698-8d54-316f-be4e-ac9d6735116b | -9.59669 | -50.16848 | 2024-09-26 00:43:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| e9ffb9a3-1951-3ec7-bb1b-7fd1dc0407cb | -9.59443 | -50.15104 | 2024-09-26 00:43:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 23f615e4-9f44-3504-8dd9-10e8e829a89c | -9.58921 | -50.16308 | 2024-09-26 00:43:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 04232b5a-da16-30bb-a22e-e8b18519e419 | -9.5871 | -50.14563 | 2024-09-26 00:43:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| cb0cf5e8-2304-3bba-b414-2a88e9da43c9 | -9.58234 | -50.15257 | 2024-09-26 00:43:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 46790c67-18e5-3985-80e0-76ee6e2ac3e3 | -9.55267 | -50.20967 | 2024-09-26 00:43:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3efc7cc0-3631-3def-83f4-2ab28565cfef | -9.55047 | -50.19211 | 2024-09-26 00:43:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| efadde78-39bf-39e6-ab60-55bef3b20264 | -9.50934 | -47.25761 | 2024-09-26 00:43:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0dbb461d-4617-3f0b-842b-57516856e48f | -9.43855 | -51.49844 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| e9f7d5f1-2c68-3ed6-8cb2-cbfa2e695752 | -9.43581 | -51.4761 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 708cc4c3-2709-3739-996b-b5c974077d02 | -9.21789 | -46.91592 | 2024-09-26 00:43:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 880001ae-c98e-3a78-8c1a-642cd57aad37 | -9.14181 | -51.532 | 2024-09-26 00:43:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 24eb4ce9-de4d-39a1-aab5-9771bdc84932 | -9.13317 | -51.53846 | 2024-09-26 00:43:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 86aca87a-2a33-3de9-a105-75d6407a083a | -9.1284 | -51.53382 | 2024-09-26 00:43:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 60ba7a72-dd18-3dda-a50e-d308e4a21f31 | -8.70854 | -54.79168 | 2024-09-26 00:43:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 2fd1d5fe-c4b1-307d-aae4-283b3714abb2 | -8.7059 | -54.79909 | 2024-09-26 00:43:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e12b6a85-b945-33d9-91f2-f86a209d9fef | -8.60867 | -50.26693 | 2024-09-26 00:43:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d7d3fb6d-ea94-3e24-993a-ea03ccb5add7 | -8.52083 | -55.20678 | 2024-09-26 00:43:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 82b147ff-05c3-3d04-be09-7dd42e163412 | -8.44942 | -47.14009 | 2024-09-26 00:43:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 63400c10-ba70-31f9-a77a-aa2747f20bb7 | -8.32132 | -55.02639 | 2024-09-26 00:43:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| ecbf763a-2859-329a-88ab-3e73a862d7cb | -8.32 | -55.03323 | 2024-09-26 00:43:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| fe4a405c-dba1-3e83-a6be-123e90658d00 | -8.31676 | -54.98552 | 2024-09-26 00:43:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 597ff394-66b2-3ca1-bf3a-46b340f3c97a | -8.3152 | -54.99262 | 2024-09-26 00:43:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| bea05c5e-d3bc-3726-ad4b-f047b0767955 | -7.49415 | -47.09258 | 2024-09-26 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c8eb586f-fff4-322e-a3ab-5baa3731bb7d | -7.49279 | -47.08254 | 2024-09-26 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d5297a6a-eb73-301a-9077-01bc16415cd1 | -7.3078 | -46.67287 | 2024-09-26 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d2023469-8347-32a2-823b-51325d1b24fb | -7.27085 | -46.87212 | 2024-09-26 00:43:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 39f4eb1a-5c71-31d0-8124-9d0c7e1b7bd8 | -7.2695 | -46.86214 | 2024-09-26 00:43:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b520e5d7-ff1f-3168-8d3a-3ae96e131f1f | -7.22513 | -44.79255 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| ff69ac30-878f-3f2f-8503-1fc1065c2cbc | -7.22461 | -45.52921 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ddf15c2f-2745-3713-9efe-4a3796451402 | -7.21395 | -44.79136 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 219798b2-f468-384a-b36a-67a91af66ef6 | -7.1282 | -44.8367 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| aba59a41-1345-396f-ace2-206d8f56165b | -7.12696 | -44.82784 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2ccbdc42-160e-3c9a-8f68-52e254e8148b | -7.1032 | -46.45162 | 2024-09-26 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 97c9b996-02ef-3668-8554-3921f1d33bf1 | -7.10192 | -46.4422 | 2024-09-26 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| b2ad5c27-16f8-3e91-a67b-4c399f6c8c8c | -7.0941 | -46.45289 | 2024-09-26 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4aa57b89-fc22-32ba-a3e4-3bc2bd198de8 | -7.09282 | -46.44342 | 2024-09-26 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| ec46184f-74bb-3143-95f5-3da4ffeabecd | -6.80103 | -46.59548 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5284cf7-528d-364e-a925-98ab665a1f6a | -6.78307 | -44.73301 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| ab3d09cb-c043-38cc-83a0-99d6a0488851 | -6.78182 | -44.72416 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b2f01f69-b5a1-3e4d-a86a-93ecad101e44 | -6.73787 | -47.22519 | 2024-09-26 00:43:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f2cc96c4-3982-3842-aa1f-8a0be7ce8604 | -6.73652 | -47.21511 | 2024-09-26 00:43:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| d7a7e9df-6de1-3585-9c71-e781cf9c9910 | -6.72849 | -47.2265 | 2024-09-26 00:43:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f67bdb33-c273-3f75-b3e2-ab4777d48e0c | -6.72715 | -47.21645 | 2024-09-26 00:43:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 927ef51d-5cbd-3a28-a697-1607b2c813bd | -6.68113 | -44.66288 | 2024-09-26 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e39e6703-2ddf-3ede-9f05-94030cdd16f0 | -5.55375 | -45.10281 | 2024-09-26 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7aa50685-6d1c-3c9c-a0bc-deaa8d985d0f | -5.5449 | -45.10407 | 2024-09-26 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 01f515a4-3c6a-3bb5-9193-36e5e9cc4e0a | -5.53238 | -45.8059 | 2024-09-26 00:45:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 68b6f8ab-133e-36ca-a4ac-c46a2fa3cf21 | -5.47683 | -45.87448 | 2024-09-26 00:45:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b832b48e-4a2d-3883-96ae-3caf0dba0207 | -5.46691 | -46.46962 | 2024-09-26 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b915047d-b6d9-3d3c-aef4-9f34bfb6be0a | -5.28814 | -48.83453 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0860960f-9d5b-3d3a-ae8f-d4d880a257ee | -5.28595 | -48.82903 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 5b33dc53-18e6-3287-844e-31cc87af3c86 | -5.27796 | -48.83588 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f286cbcb-add8-3f0c-8d31-dd4831b1c60b | -5.25225 | -48.8758 | 2024-09-26 00:45:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0f6048f1-da84-3dd8-a2b1-bb711e70a7bb | -5.22168 | -47.97314 | 2024-09-26 00:45:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 40d20cb3-f738-374f-bd34-b5cc469934b2 | -5.22023 | -47.96253 | 2024-09-26 00:45:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| daad3732-1179-332b-9703-cbb608b3ef63 | -5.21095 | -49.25147 | 2024-09-26 00:45:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 327a20d7-cd0e-357e-b418-bcfbc45c77ce | -5.18295 | -45.21614 | 2024-09-26 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e4ce6b25-bb2e-3332-879a-33523b74c7a4 | -5.18171 | -45.20731 | 2024-09-26 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a803baaf-d965-3afb-87f8-61df582ae25f | -5.1392 | -45.49811 | 2024-09-26 00:45:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4c60af60-b585-3fa6-8760-0d1725aa3bd0 | -5.09983 | -45.21587 | 2024-09-26 00:45:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fd426ded-baf8-32f8-816a-c500714b3589 | -5.0986 | -45.20704 | 2024-09-26 00:45:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8a920ff9-c0b1-3644-a436-d74b69b3c649 | -5.09099 | -45.21712 | 2024-09-26 00:45:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 27c03f47-ea62-3e9d-95cc-415957ef6578 | -5.08976 | -45.20829 | 2024-09-26 00:45:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |


[Clique aqui para ver as próximas entradas](README14.md)

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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb68102e-79e2-3ebc-b687-327fadae5b58 | -6.6021 | -58.849 | 2026-09-13 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 7f5f8d89-f953-3d72-8036-e8dc4bda17d3 | -2.6602 | -57.5313 | 2026-09-13 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| df1ee07c-153c-3687-9106-426f328e988b | -10.312 | -45.2907 | 2026-09-13 02:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 02310e48-d204-390a-9e3e-b5d5288b6cb7 | -2.6785 | -57.531 | 2026-09-13 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4ccfcb20-b61b-35b3-bf7c-8a73743367ee | -10.6827 | -54.1679 | 2026-09-13 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.1 |
| dc53cdfb-7fbb-33f8-a788-32263761ae65 | -2.9579 | -50.3988 | 2026-09-13 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 2185321b-4453-3a30-9aec-3f869d362971 | -10.6829 | -54.1475 | 2026-09-13 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b608ebd3-1ddd-37e9-b27f-248508cf75c8 | -6.1111 | -57.6645 | 2026-09-13 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 762b975c-0ee5-3c45-bed6-15e53cf6639d | -6.863 | -55.5801 | 2026-09-13 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 38dd0264-ee21-3def-9367-549dfa9b2156 | -2.6785 | -57.531 | 2026-09-13 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| bbbf64bf-6288-303d-9f3e-8ff0695aa4bb | -10.6413 | -46.1133 | 2026-09-13 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 99bacc7a-9b08-391f-b4d5-0ef223c89fec | -12.8543 | -44.386 | 2026-09-13 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6a518d1c-d220-3c41-85f4-a9036b6d4616 | -5.1254 | -55.9748 | 2026-09-13 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 8dda252b-dfd5-3525-a554-5a8739f0cae1 | -10.6417 | -46.0906 | 2026-09-13 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 4952f1f2-51d1-3180-8fd2-2ee57978bcd1 | -10.6827 | -54.1679 | 2026-09-13 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 9ef3a6d9-037f-36f7-b5a5-9ff9995f4a22 | -12.8736 | -44.3828 | 2026-09-13 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| f326957d-d9ce-360f-b22c-6fee228ee781 | -4.9298 | -45.814 | 2026-09-13 02:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9cb6682d-f6ae-337e-bba9-0397c6708791 | -10.6829 | -54.1475 | 2026-09-13 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d90bfaa5-e782-390e-a303-04e0fb32b393 | -10.7018 | -54.1458 | 2026-09-13 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fc247aa3-5485-3558-ac07-dfbdc97cac02 | -4.9296 | -45.8363 | 2026-09-13 02:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 22b62bda-fb17-3ca2-a790-b5c395dd5c41 | -13.616 | -47.8774 | 2026-09-13 02:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9553ceee-a717-36fe-966a-24108bbcc570 | -8.5417 | -54.6985 | 2026-09-13 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7979abb2-119f-303a-99bd-bc4874891d78 | -2.6784 | -57.5504 | 2026-09-13 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ce8312e9-ee95-3f81-9209-315f8a605551 | -10.312 | -45.2907 | 2026-09-13 02:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| f43eb8dd-3431-3f6f-bbd1-2830a48af9be | -5.1255 | -55.955 | 2026-09-13 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 4c7052f6-290d-3841-a7c8-a73183836e75 | -10.7015 | -54.1663 | 2026-09-13 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| d339c53c-3090-358b-93e1-5d0c1fb10622 | -2.6602 | -57.5313 | 2026-09-13 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 4fa85ebf-55a5-3cec-9efc-ae4de6d5c896 | -5.1255 | -55.955 | 2026-09-13 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 68a30826-8ddf-3719-9928-f81219274fec | -2.6785 | -57.531 | 2026-09-13 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f750b854-cb63-3f1e-bc22-e0fa1df5c31f | -6.1111 | -57.6645 | 2026-09-13 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 65215730-b079-3a96-843a-ba446f393727 | -10.6829 | -54.1475 | 2026-09-13 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 04541e48-f999-3f93-959a-594fc5c971f6 | -13.616 | -47.8774 | 2026-09-13 02:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 317806e4-9195-355a-91e0-b3ac882ce24f | -2.6784 | -57.5504 | 2026-09-13 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| b87762df-7f1c-3bd9-b1a8-829ae88189a3 | -2.6785 | -57.5115 | 2026-09-13 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| a165c630-615b-3fd2-b9d2-0b303ca4e200 | -8.5415 | -54.7187 | 2026-09-13 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c92e1e95-ec44-396a-8a01-649378751a93 | -10.7015 | -54.1663 | 2026-09-13 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9012c372-3836-3567-9239-a590857e3418 | -8.5417 | -54.6985 | 2026-09-13 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ccc8ffa7-453f-3a41-bc0b-1fb6d4f5090a | -10.6417 | -46.0906 | 2026-09-13 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 9229fbd2-6588-3784-8313-0bf7ea85e216 | -10.6827 | -54.1679 | 2026-09-13 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| e386dbcd-5315-3bd8-9862-e1044c9a8449 | -2.6784 | -57.5504 | 2026-09-13 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 58e853c8-705e-3d2e-814d-5cbc5b225116 | -10.6829 | -54.1475 | 2026-09-13 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4d91546f-527c-3df0-8d5a-7acdab950616 | -10.6827 | -54.1679 | 2026-09-13 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 149.4 |
| d214956c-795f-38cf-9d84-f5a4ed71259c | -2.6785 | -57.531 | 2026-09-13 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7ecc76c4-3d8a-3283-9838-b58b42073fbc | -8.5417 | -54.6985 | 2026-09-13 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a3297a31-7a54-30aa-a446-dbafbab0e914 | -13.616 | -47.8774 | 2026-09-13 03:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 48f68f55-dcb1-3fe9-914e-898ebb005f08 | -10.7015 | -54.1663 | 2026-09-13 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 282a857a-4040-37c8-8a80-6319c8275b71 | -6.1111 | -57.6645 | 2026-09-13 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 5d4a47cd-1472-33b9-81ef-e7e40be1c327 | -6.0731 | -57.861 | 2026-09-13 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 2465958a-4a44-361c-942c-bb7286bda0cd | -10.7015 | -54.1663 | 2026-09-13 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 68e7830d-e50d-34cd-b27b-2591116ce662 | -2.6785 | -57.531 | 2026-09-13 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| aae49205-2dc1-39f5-8fc6-7130e40f79eb | -10.6827 | -54.1679 | 2026-09-13 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 1af179f8-f36b-36c3-87d4-50ede189e6b7 | -2.6602 | -57.5313 | 2026-09-13 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 5f993def-1979-3991-9ec4-e139bcde68bf | -2.9579 | -50.3988 | 2026-09-13 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 97a68b52-e191-3d0b-a2b0-b252f2bb7d6b | -6.1111 | -57.6645 | 2026-09-13 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 25e34759-452c-39d4-99e4-1a1be033ae29 | -2.9578 | -50.4198 | 2026-09-13 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a4fed2a1-6faf-3373-ad01-deccf430b63d | -10.6829 | -54.1475 | 2026-09-13 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6183db3c-6c1c-387f-9b46-9aa7f4719000 | -2.6784 | -57.5504 | 2026-09-13 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b86d684b-2943-39f7-aea7-897031225680 | -18.64726 | -41.99192 | 2026-09-13 03:15:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fd27ceb2-921b-348d-aacf-f91ffacf4495 | -6.1111 | -57.6645 | 2026-09-13 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 1a7dddca-a8c5-34a0-b9f1-fdde98b70105 | -10.6829 | -54.1475 | 2026-09-13 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 74040d12-b29d-30bd-8884-343e3dfe6a3a | -10.6417 | -46.0906 | 2026-09-13 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f751e2b2-3356-3885-96bc-060bf2dab22e | -12.8543 | -44.386 | 2026-09-13 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f7f92a86-05bb-3e7f-9129-0597d1b87a31 | -10.6413 | -46.1133 | 2026-09-13 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 585d69ce-7899-3022-81df-43b573a20d25 | -3.728 | -61.7555 | 2026-09-13 03:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 5ff86304-476c-3ede-b2df-5ac433a5ec6e | -10.6827 | -54.1679 | 2026-09-13 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 0c9349f7-eac1-3b6b-8a02-59763361936a | -2.6784 | -57.5504 | 2026-09-13 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6a1c985b-5108-320e-befa-c5fc5a4689ab | -10.6431 | -45.9999 | 2026-09-13 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 1c2d285c-5dcc-3d65-a6bf-3d2ecadaf699 | -2.6785 | -57.531 | 2026-09-13 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 2d297164-6c3a-39e3-8b46-1f82ed20c502 | -10.7015 | -54.1663 | 2026-09-13 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| cb4af303-077a-33cb-9e15-7199f4c95c35 | -4.39009 | -42.34408 | 2026-09-13 03:28:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7d839548-06f9-3cc7-9b52-ded752321d22 | -3.33078 | -42.2981 | 2026-09-13 03:28:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b558f568-5c34-354d-b3e8-04b92598828c | -4.39751 | -42.33974 | 2026-09-13 03:28:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9425c928-a9c2-3c0c-828c-465c6e3579fe | -3.32979 | -42.30387 | 2026-09-13 03:28:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| cd721f2e-9103-357c-bf36-4c2d2092021a | -2.6785 | -57.531 | 2026-09-13 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| b9a80f03-d801-3915-a0f3-2d4312e1776f | -2.6784 | -57.5504 | 2026-09-13 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 2d7541a3-2642-3e6f-9b65-33d2bccd28a4 | -10.6413 | -46.1133 | 2026-09-13 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| eb243a09-b6a3-35bd-b782-68b4724f0d9f | -10.6829 | -54.1475 | 2026-09-13 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b486fe04-cd6d-3bfc-b90a-0e6e3c15c492 | -10.6827 | -54.1679 | 2026-09-13 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| ab83d4d8-fa94-3e6b-ac6d-d25ef65469a8 | -10.6417 | -46.0906 | 2026-09-13 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| dd17147f-6616-3dc4-84b3-29ad738723d2 | -12.8543 | -44.386 | 2026-09-13 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 1b21867d-aa2b-3dc9-9a07-54aaf5cc0a5e | -2.9578 | -50.4198 | 2026-09-13 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| cbea8226-def4-3cd0-8dc8-ce3c5c9537f2 | -10.6223 | -46.1157 | 2026-09-13 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9d0dbb5d-b9ff-3ac9-82d9-8db84737f027 | -2.9579 | -50.3988 | 2026-09-13 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 76af3504-88b1-304d-a0cc-38cd3c7350a2 | -10.7015 | -54.1663 | 2026-09-13 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 74c32e7f-0064-3768-a743-d651a47a2cc9 | -10.6226 | -46.0931 | 2026-09-13 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 74e67656-c5a3-3543-9714-46f74aa5ab80 | -10.6431 | -45.9999 | 2026-09-13 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 076b8874-4dba-3204-ae0e-4a837516a7dc | -6.1111 | -57.6645 | 2026-09-13 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 307c75db-73fc-3468-aa59-f74a14c77aad | -10.3018 | -45.298 | 2026-09-13 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1f619a5-b9b8-3a2c-8de7-cea9f196623a | -7.01028 | -44.62997 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e43901d7-7306-3147-9475-130569301c22 | -7.96899 | -43.99559 | 2026-09-13 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b218d233-8bd9-34e8-88a9-dbb6eb04f9a0 | -7.01741 | -44.63107 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7e981e22-3530-30b0-a2c0-633621f31aef | -10.25564 | -36.30029 | 2026-09-13 03:30:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 42bf2262-acde-31b0-bc19-2c5de5c9b344 | -7.01872 | -44.62407 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 27f38aa0-e2ab-375f-a921-cadc7b0daa6e | -7.95684 | -43.99723 | 2026-09-13 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6caa2af1-6048-34e7-9182-b5c4c5710e35 | -10.30682 | -45.29869 | 2026-09-13 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a1d45874-38df-30ff-b2bd-f16c0122c3ad | -7.01605 | -44.63836 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a72686e8-24cc-34ce-a52b-f3b5207fc82b | -10.25959 | -36.30098 | 2026-09-13 03:30:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 45.2 |
| 85a7d9a5-3ae3-3b84-b729-1c782bc732ab | -6.82911 | -43.51017 | 2026-09-13 03:30:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c4241c9-113d-3cc5-9b7d-fb7d016fd682 | -8.28563 | -39.97225 | 2026-09-13 03:30:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 50fd2330-197c-3d6e-9dea-3fd8e6944331 | -10.31049 | -45.29086 | 2026-09-13 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README18.md)

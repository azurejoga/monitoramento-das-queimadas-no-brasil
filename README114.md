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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01edd2ea-0460-3040-a478-4dde9da9284b | -5.79676 | -46.4524 | 2024-10-03 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a540420-8220-3717-a35c-d516a0986356 | -5.77974 | -46.10635 | 2024-10-03 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e859401f-1c93-3230-b13b-6c92fb88dc15 | -5.59809 | -46.3721 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ffc8406-9276-3615-98ff-137ea5a42d5f | -5.09243 | -46.06233 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a311c52f-da29-3418-81c2-80258403743e | -5.08886 | -46.11761 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a8fb308a-fefd-3ef7-9047-51a20207fdc7 | -5.08827 | -46.12169 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eff76451-c13a-37d3-acd5-12e41e07801d | -5.08391 | -46.12103 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb0b1027-4afe-3516-9e92-3d7eeeb4a18c | -5.04436 | -45.81227 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5777d2c4-34a1-3527-a875-f18ae4e803e4 | -5.03989 | -45.81173 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c215c067-4686-300d-b5cc-f891be34d44a | -7.85383 | -46.25537 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1a6b5ec9-9282-3dda-a45a-e5631cc8fc5a | -7.74138 | -46.15324 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be9da567-6f55-3306-86bb-07cacefdfcac | -7.73917 | -46.14524 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c75960a-51a2-36c9-ba1a-7df895981963 | -7.73825 | -46.143 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffb9303f-64f4-39e7-939e-c689de83b9cb | -7.73755 | -46.14781 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6edcf724-7dea-3f2c-80d9-2bf56e86a793 | -7.7353 | -46.13976 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed1d6ab7-a009-3d98-a328-04893bce1b05 | -7.73373 | -46.14228 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac3672f3-8ea4-3aae-9544-aa9d6ed8a394 | -7.72989 | -46.13679 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d084f8f2-d5a9-3e8f-9cb4-e5245b5f95f1 | -7.7247 | -46.14073 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab5ef957-0b7d-3f11-a356-ffee16ca8a77 | -7.62468 | -45.51215 | 2024-10-03 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 466c4d29-5466-3115-9059-cb90d628c40a | -7.37407 | -45.88948 | 2024-10-03 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14125bc8-9ab4-3386-9c69-d5e9e6e67569 | -7.21218 | -46.68451 | 2024-10-03 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5524bc18-d4c5-3252-8cd2-e4a04cdf713c | -7.20905 | -46.67567 | 2024-10-03 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e393dd24-2398-3961-8ef9-8f5ebc7fefbb | -7.20845 | -46.67976 | 2024-10-03 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04465b95-9442-3281-9b57-19fd5a1e9051 | -7.20786 | -46.68383 | 2024-10-03 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e5ef12d1-1a08-3c49-bd54-d1b55e3d0564 | -7.06451 | -45.35128 | 2024-10-03 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 303e3769-2a0a-34b6-9d6d-ae43d179807a | -7.04218 | -45.33818 | 2024-10-03 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9a2f5883-ed11-325c-be84-ac6839734905 | -7.00105 | -45.49443 | 2024-10-03 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ab2ff1b-f755-3fd8-ad41-981790e5d76d | -6.99635 | -45.49379 | 2024-10-03 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 796038b4-4b8c-361c-ab92-fd858b2f5a0b | -6.66801 | -45.33016 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fdc8a44-cdf1-3141-86e9-2a9fabd5bacf | -6.66327 | -45.32966 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64a7b7d2-c361-30dd-8e6b-3dd7c45a0b9b | -6.66257 | -45.33447 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7258d3c0-1be2-3c91-b5c9-97994b46d8b7 | -6.65854 | -45.32909 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df45d36a-e471-3d69-8122-018601bcdcf4 | -6.65783 | -45.33397 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d9a658b-4c2d-3877-bd5c-997de7f2b95e | -6.64506 | -45.32235 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6921e441-66b8-345f-a21e-f2dd6a4c78b7 | -6.64435 | -45.32731 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10dda293-f4ee-3195-a986-47c8f988999a | -6.63963 | -45.32666 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de19d6b5-f3c1-3646-ab60-378943efcad2 | -6.48201 | -46.4772 | 2024-10-03 04:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30c44c7e-f3ff-3f41-9643-c28a0042478e | -6.48139 | -46.4814 | 2024-10-03 04:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bbc29f4-ca02-3f6b-982c-bd97ea9dce61 | -3.41401 | -47.06548 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a245d3b-92bd-3778-b687-054090904e21 | -3.41222 | -47.0689 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b713def7-ad3c-32d5-9c98-ae86fe6341c1 | -3.31969 | -47.02144 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32e4fd3a-9999-38d3-95ce-b1a3778dbd74 | -2.98909 | -47.45041 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7875463-dc39-3b79-8122-8f5a6225f175 | -2.7296 | -46.79352 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c067c64-c298-3f6d-8917-9874fa1dc24c | -2.72505 | -46.79639 | 2024-10-03 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 607f40c5-f6e4-3069-9ca1-a20a280764db | -2.5394 | -47.2299 | 2024-10-03 04:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10e8d52f-bc7e-3f5b-bb46-f110cbeb5279 | -2.53623 | -47.22441 | 2024-10-03 04:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43600a4f-8d0a-3eea-a758-cfa1f68b5658 | -2.53603 | -47.22752 | 2024-10-03 04:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 436afe19-8bdf-3d1a-b01a-477d1f281627 | -2.53549 | -47.22933 | 2024-10-03 04:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10d4a916-8b7a-3361-9fa6-d465c36853c2 | -2.5286 | -47.06995 | 2024-10-03 04:49:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 117859d8-e103-3700-abe2-d5bda99c13cf | -4.9434 | -47.13849 | 2024-10-03 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30f3c9f9-615f-36d5-b99c-950223778281 | -4.9231 | -47.13539 | 2024-10-03 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d31c154-26b2-3421-8b9d-a611c82370df | -4.81637 | -47.64885 | 2024-10-03 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c114caf-13d5-3f57-9397-66b5b6929c67 | -4.65126 | -47.43677 | 2024-10-03 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29814908-bbe3-3e65-8a84-3c5ba73cfa0e | -4.64955 | -47.4349 | 2024-10-03 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 91488829-6e37-3430-99eb-406751d52f88 | -4.6473 | -47.43613 | 2024-10-03 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 92ca779f-1c73-307d-8a21-1b5005faea56 | -4.64559 | -47.43427 | 2024-10-03 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4816f62-b3d0-399b-a354-1eec38bc4cd3 | -4.47509 | -47.73649 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 409719db-9f2e-3788-93b5-4c491085e20a | -4.39593 | -47.28353 | 2024-10-03 04:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c1776b0-1d85-3d04-82b3-b4af33d5de73 | -4.2879 | -47.49764 | 2024-10-03 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7869d39-5bfd-3987-86fd-89a5a3ab137c | -4.15588 | -47.20182 | 2024-10-03 04:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d087b4ef-a4f0-33d3-afff-0ee4e3900355 | -4.15451 | -47.19997 | 2024-10-03 04:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fff8203b-7e50-3457-b159-e567a547fadb | -3.76479 | -47.49922 | 2024-10-03 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f39d0e41-5c8f-3218-a3d3-90beaa722007 | -3.70412 | -47.60958 | 2024-10-03 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5665f309-cd9a-30b4-8a35-290b2a5c451c | -3.70097 | -47.60417 | 2024-10-03 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccda9a43-70dc-302f-a615-765a996f833f | -3.69782 | -47.59878 | 2024-10-03 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4dd26e1-9ee1-3187-9459-c49e4a93544a | -4.49498 | -46.38714 | 2024-10-03 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20a13591-a172-3168-895d-e8dbc93db401 | -4.49113 | -46.38768 | 2024-10-03 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ce21149-f304-3929-a9a2-e99400399d2a | -4.40419 | -46.33022 | 2024-10-03 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e659cfe-0980-3911-b71f-4760560c275c | -4.4036 | -46.33429 | 2024-10-03 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87c77d04-d000-3dd7-bdd3-1a93dc2e7fab | -6.43186 | -47.40298 | 2024-10-03 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f227d787-b6b0-3f03-aa63-80bf3b93c38f | -6.28191 | -46.98804 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 561bb667-707a-37cd-8490-908261a8a1bb | -6.27773 | -46.98738 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e04f2525-7d9d-3fdf-8fa3-75b3fde97f91 | -6.27717 | -46.99118 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b29a7a98-ba26-3c4f-b258-371fc330836a | -6.12728 | -48.0609 | 2024-10-03 04:49:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 399722a4-bc96-3caf-b0a9-5075e2ae517b | -6.12531 | -47.26614 | 2024-10-03 04:49:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 968a1895-34e2-3c5c-90a6-3c5ea1484b24 | -6.12478 | -47.26974 | 2024-10-03 04:49:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ff9775a-0918-3416-aafc-b90fcdfd2d8a | -5.46366 | -47.09032 | 2024-10-03 04:49:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a1857c5-233c-3216-b5a2-b08a403aab62 | -5.46079 | -47.0895 | 2024-10-03 04:49:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b4c0e89-7534-3703-a498-e3f94dd9cbdd | -5.43045 | -47.09586 | 2024-10-03 04:49:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4c4d97d-6446-31c1-ae88-f4cbef13ee4b | -5.42991 | -47.09946 | 2024-10-03 04:49:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b2e1eb0-9ad7-3fd3-a821-fff81b525a4d | -5.36303 | -47.80748 | 2024-10-03 04:49:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1694a72e-8411-3bcd-b791-88e8a9756a3e | -5.35401 | -46.71829 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12638b07-851b-3385-b30e-7b88adf17e0e | -5.35345 | -46.72207 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 471ef3f8-c790-3900-8781-3ad549f1b5ce | -5.3529 | -46.72584 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 420aad2d-ce6d-3ad2-b053-59a5e9898a32 | -5.2382 | -46.77216 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9629c83d-a178-3159-83f4-cbc923814ce9 | -5.06366 | -47.67192 | 2024-10-03 04:49:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e293288f-8d47-3e2d-bc1e-9806b545d28b | -7.80751 | -47.47126 | 2024-10-03 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93469dd7-73f1-3f6b-89ff-e1943f248865 | -7.80284 | -47.47437 | 2024-10-03 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1f30172-bc21-32e3-8c5c-1e8cdbdc9944 | -7.76279 | -47.5025 | 2024-10-03 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17a179ec-ac6a-3a98-8198-c62747ec88e9 | -7.76084 | -47.50241 | 2024-10-03 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1711a80-3710-331b-aa49-a3d120fd825e | -7.41963 | -47.86502 | 2024-10-03 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 67065fba-e30c-3920-b567-434979cd5203 | -7.41561 | -47.86441 | 2024-10-03 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3566d996-40d5-3fef-9fb4-e46066e476da | -7.18056 | -47.82712 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eef6c1fe-ade4-3706-8adb-8983781b8492 | -7.17742 | -47.82533 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5dbc6d1c-814a-307d-ae5e-38b3075923e0 | -7.17656 | -47.82649 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d26158b6-3109-3716-be5c-20cdadb9c8f6 | -7.17629 | -47.83329 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43dc5730-5de3-3dbb-be85-cfddfcb9ea83 | -7.17577 | -47.83178 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5b5a838-e3c5-3075-8bd9-18824203646f | -7.17496 | -47.83714 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 360cc595-e225-3529-8321-5a8927294597 | -7.11516 | -47.88195 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ea2fee4-2ca5-3857-85c1-7d55dbcf0206 | -7.11442 | -47.88702 | 2024-10-03 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README115.md)

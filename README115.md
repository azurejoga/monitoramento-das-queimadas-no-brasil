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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f10fea5-e538-3557-a5e9-32662899edbe | -18.26878 | -43.42943 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44b47418-03c8-390a-abcc-9f7996bd7945 | -18.2683 | -43.43353 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3771703e-916d-3723-9547-937213c1b319 | -18.22139 | -43.28631 | 2024-10-04 04:34:00 | NPP-375D | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7afe67db-3f43-3e89-8e9c-259e21920245 | -18.21554 | -43.29615 | 2024-10-04 04:34:00 | NPP-375D | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fc7081a-dd36-3691-8e11-549c650f038b | -19.42824 | -43.89825 | 2024-10-04 04:34:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60b5b0df-8654-3fee-9f77-8d168f857eb3 | -19.42373 | -43.89766 | 2024-10-04 04:34:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96efcd2f-8eb7-3262-bae3-f7210beda23e | -19.28497 | -43.77595 | 2024-10-04 04:34:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c44274e-a28c-367b-8c16-874c20f76ec4 | -19.28488 | -43.77437 | 2024-10-04 04:34:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a583737c-6262-3ed4-81e8-c50161ccd720 | -19.28442 | -43.78072 | 2024-10-04 04:34:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20204c82-42bb-3add-9307-48bc9547aaee | -19.28431 | -43.77908 | 2024-10-04 04:34:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89132e2e-6c67-3e1f-8810-e492f6c49eef | -19.28312 | -43.7888 | 2024-10-04 04:34:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1919b475-12e1-39a0-af3e-03bcfd958559 | -19.28093 | -43.7689 | 2024-10-04 04:34:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec194b59-5db2-3635-9648-305d5fb4b1ad | -19.27979 | -43.77835 | 2024-10-04 04:34:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b1d5d05-8a3d-31e0-b0fc-ef94b741e8d2 | -19.25266 | -43.37411 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1976420-8ce7-3aeb-ac15-d617051a57a2 | -19.25035 | -43.75472 | 2024-10-04 04:34:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f64fb22a-f56b-3881-9b1f-db00b5252f4d | -19.24978 | -43.75957 | 2024-10-04 04:34:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9ff02b7-64e8-3a1d-bfac-8f78570b07e1 | -19.24678 | -43.38428 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a31ee4e-f42b-36d4-8128-957e2bfffb87 | -19.23801 | -43.37834 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 598e9b3b-78a8-3c9d-acc3-cadc9611b5c4 | -19.23671 | -43.36533 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6282b43-d4c4-3170-93da-94f1253d4e18 | -19.2354 | -43.37614 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 326af41f-f3ea-3de1-b3b5-b607340974de | -19.19924 | -43.71819 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6ca22c5-0160-375f-b48e-03d034f65832 | -19.19818 | -43.72129 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbcd2685-23c5-3d73-83a5-c2d74f87a266 | -19.06495 | -44.43799 | 2024-10-04 04:34:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ed88432-cc43-3e41-8476-f9901e9aa0c3 | -19.06442 | -44.44225 | 2024-10-04 04:34:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee1678af-b439-37aa-bc5d-9313429ef5e2 | -19.0639 | -44.44649 | 2024-10-04 04:34:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f5bc236-2b6e-3ce0-9772-d313cdd43443 | -19.05362 | -44.42265 | 2024-10-04 04:34:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc194d8e-63ec-3d51-a42e-0a0b08c48b2e | -19.05306 | -44.42723 | 2024-10-04 04:34:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06b85826-c32b-3c81-b141-c54dcea0da19 | -18.59054 | -43.95587 | 2024-10-04 04:34:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83d12d8f-2403-30d0-b4ca-a5357db7a6b5 | -18.59002 | -43.96004 | 2024-10-04 04:34:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7eeb90f-5349-3009-b4ec-6922a396de09 | -18.58608 | -43.95544 | 2024-10-04 04:34:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d209f58-da87-3848-b2e8-982bc7ca77a9 | -18.58507 | -43.96367 | 2024-10-04 04:34:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 254d59de-275d-3bef-ab8b-66472cc37304 | -18.56876 | -43.83621 | 2024-10-04 04:34:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec6e440d-471a-326e-9876-6ccc5645adc0 | -18.5682 | -43.84085 | 2024-10-04 04:34:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcd27472-d522-3b76-936d-1277df4d0ca9 | -18.40298 | -44.46414 | 2024-10-04 04:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c77fff6d-7534-3d85-9c54-15f448132edf | -18.37602 | -44.03621 | 2024-10-04 04:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae45ac43-c954-3a06-9eed-57049ef0a9e7 | -18.37165 | -44.03534 | 2024-10-04 04:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dfe8790-a598-3b2e-ad75-5c8f942fb17b | -18.36673 | -44.03885 | 2024-10-04 04:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82b99cf4-a2f9-3df0-a7de-df772447ae49 | -18.34727 | -44.0149 | 2024-10-04 04:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82f81e9b-b32d-3c32-816d-bf62c772edf7 | -18.33393 | -44.01412 | 2024-10-04 04:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8af89678-ab0c-3a9c-9491-dbe7a68e95da | -18.33149 | -44.03422 | 2024-10-04 04:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f91fa4a1-2b0a-3602-842c-47418f5c4113 | -18.32953 | -44.01344 | 2024-10-04 04:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c54f0c4c-ca3c-39f6-9795-c21e7c73f31e | -18.32906 | -44.01733 | 2024-10-04 04:34:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac18b097-a54d-3918-8148-8b56cd6292eb | -18.26453 | -43.43177 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 75b00bce-113c-3f56-9fcf-059328606d89 | -18.21093 | -43.29545 | 2024-10-04 04:34:00 | NPP-375D | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd73067c-6559-3c4a-8374-f2256f0347ee | -19.24131 | -43.36637 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ab06829-3cfc-330e-85a9-a799971433e8 | -19.23924 | -43.36737 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bbbc0d27-1898-350f-bc34-3ea87bed6273 | -19.23747 | -43.38305 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9e64d13-d102-3e8c-8182-7e1d4cb53180 | -19.23479 | -43.38123 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93054b7e-288e-36ce-bf1f-0968ba20057c | -19.23344 | -43.37693 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62c6b799-235d-3a1f-b166-0d3af464664a | -19.23022 | -43.37995 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 206aa43d-f9b4-3d70-8b3b-8d6be6e87fa9 | -18.8664 | -43.59237 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0c7b01ad-9ddd-3d6c-806c-95a3b01d7c6a | -18.86174 | -43.59259 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 81c25188-e113-35e9-9f00-881b99e1a86d | -18.86117 | -43.59733 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 62e1a68c-ff69-3aa6-bf5e-33b1d5106244 | -18.85986 | -43.56969 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 975533ae-5355-3428-a919-6f9b48102029 | -18.85718 | -43.59195 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 94d70302-1600-37e1-962f-f6fac6e34389 | -18.85658 | -43.59693 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| e938629f-c403-3f11-a038-319f3a40e5e1 | -18.85602 | -43.6016 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 23b5afa1-6698-39be-9bda-b7b07adb3ad2 | -18.85549 | -43.606 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 58d1dd93-e317-3710-9025-1f285ecaea3e | -18.85469 | -43.57402 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fede6f0f-c701-335d-8254-2bf941beef1f | -18.85399 | -43.57986 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1fdcc566-1def-37e8-8db8-ca76d684c069 | -18.8533 | -43.58563 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 53f9f20a-b449-3fd3-b960-381dd1fc0f67 | -18.85264 | -43.5911 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a6e9652c-c27c-38d6-b075-b58a7239cffe | -18.85202 | -43.59628 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e3e91875-0db9-34e7-81a7-6676b5f58e3e | -18.85145 | -43.60104 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| bf283143-1477-341c-9962-e35ada8d918d | -18.85023 | -43.5725 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bddac315-1a0a-3a63-a294-729003e88c7c | -18.84954 | -43.57829 | 2024-10-04 04:34:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f65b5389-f40d-3ccb-96b2-f1583219fa58 | -18.84478 | -43.618 | 2024-10-04 04:34:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ebb0942f-8b1f-3bd6-89cf-ec9a04f4471b | -18.83954 | -43.62317 | 2024-10-04 04:34:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9c48223f-10d6-398d-8be3-01921f58d301 | -18.26862 | -43.43629 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 582732a1-a250-3d34-b83b-b34cfafb22e0 | -18.26371 | -43.43299 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dc2185fd-5a90-3e71-bc3a-e19d66105ca1 | -18.26404 | -43.43575 | 2024-10-04 04:34:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75735bf7-7442-3a51-b754-43d8292a81d4 | -18.98623 | -43.28171 | 2024-10-04 04:34:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b1af2838-11c6-3164-b189-7b124618cfe9 | -19.24159 | -43.38839 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cf596f6-8e56-3701-bcc7-bfd84da7bf64 | -19.25208 | -43.37926 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bd798b8-63ec-353d-b05c-026bd5a0886d | -19.2435 | -43.38741 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44a8dd0f-08fc-3921-b1fc-2c92247b34d4 | -19.23941 | -43.3821 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 399a5c63-5d7a-3837-bb09-0b65c9d217be | -19.23421 | -43.38606 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c584535d-9347-3729-93f1-e73b791a6339 | -19.23285 | -43.38212 | 2024-10-04 04:34:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e8d3dbe-8084-316e-b976-104fa52a80da | -13.66328 | -43.7299 | 2024-10-04 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b680b253-cb8f-34be-b60c-799919af0402 | -13.66276 | -43.73384 | 2024-10-04 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7d9e782-07a8-3731-8006-757e7a850040 | -13.53971 | -43.63044 | 2024-10-04 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22f71a33-9876-3d08-a261-79b0687d823f | -13.53903 | -43.62888 | 2024-10-04 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cd2a52f-4d8a-3eea-bcd7-cfd2ae9f8f00 | -13.51854 | -44.40535 | 2024-10-04 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17bcdc49-f5b7-32dc-9f15-d5fd9598f11a | -13.48137 | -43.77502 | 2024-10-04 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 07657d62-0176-3027-a751-113f2520c2a4 | -13.47719 | -43.77438 | 2024-10-04 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29988b0b-f4a5-337e-89f0-fc7919a8608e | -13.43497 | -44.77404 | 2024-10-04 04:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfda32b2-e49a-3334-a21b-91e18edf0b4a | -13.02146 | -43.75223 | 2024-10-04 04:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c124844-0491-3e29-9f30-40b26b3f74d1 | -13.02095 | -43.75606 | 2024-10-04 04:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd23d06b-ba25-3eb1-b0a4-e26f869ec5b5 | -12.73138 | -43.4833 | 2024-10-04 04:34:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ebe1187-c878-3305-a83a-b4673243fe60 | -12.36635 | -44.61573 | 2024-10-04 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b632bb8-4df8-3dbd-8861-7d339b3d2f4c | -12.35761 | -44.64994 | 2024-10-04 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daa3e660-aafd-37aa-815c-e2394753d163 | -14.91055 | -45.12808 | 2024-10-04 04:34:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 672a0930-168b-33ae-8989-eb6cfe85a5f7 | -14.90663 | -45.12751 | 2024-10-04 04:34:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28884469-8366-3930-84dc-ae1305f1b8f9 | -14.50738 | -45.2196 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3f16af2-52bf-309b-9381-76ffa8440b04 | -14.50352 | -45.21895 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43792b7e-3539-399a-8c95-99f786a047a2 | -14.18927 | -44.24534 | 2024-10-04 04:34:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f78ccfe8-a3c1-344b-9e3a-c8dd35532a07 | -14.18875 | -44.24908 | 2024-10-04 04:34:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4164009d-7605-3e81-94d5-578c1a714853 | -14.18466 | -44.2485 | 2024-10-04 04:34:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b798d7e-5114-3db4-970f-4c2504da057f | -14.16775 | -44.64902 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eda6a3fb-0def-3d86-a824-58f161325ce5 | -14.16704 | -44.65432 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README116.md)

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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73bff78f-eae9-3d10-b59e-a4ed880b8817 | 0.03349 | -60.98432 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b31a208-da0c-33ca-80ac-677a9da9b1db | 0.03629 | -60.98025 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97fa3be9-ed16-3a3f-96ab-f0efdff6c079 | 0.47206 | -60.32913 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8404dd2-f95b-36d4-b0fe-95448295f678 | 0.03909 | -60.97617 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7881e7a3-ad43-3273-bb1b-708682078539 | 0.03684 | -60.9838 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbd3d056-bac6-30ff-b3df-d861e1e6e804 | 0.13559 | -60.39943 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c272994b-603a-3520-b7f9-9364b02441da | 0.07354 | -60.45367 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ec1c9ca-309c-3476-87b8-bdf0f024d3f7 | 0.38 | -60.36934 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac66898a-865c-390d-bd3b-7ecf22858821 | 0.04075 | -60.98682 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 152bf664-923c-3dfa-b993-eac7eef9c48c | 0.14015 | -60.40625 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e54e1a78-543a-3fab-9060-902f717e4da1 | 0.05136 | -60.98883 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a97cf252-fb33-36e4-9ba6-ca52a2b4d9a4 | 0.0346 | -60.9914 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eae3f340-3c39-3fdb-b075-1a5e8361eba9 | 0.04244 | -60.97565 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40f6c884-5c0b-3a85-b2d3-fc0c08fab85c | -0.15309 | -60.75261 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88960ef7-21fd-39ee-b871-2d4e4ca99cf0 | 0.13276 | -60.40364 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87c90097-9bf0-3c6e-8c64-d380d2039c76 | 0.0736 | -60.54365 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e85bff8c-e1dd-35ed-a30b-b8f880dc96c3 | 0.49381 | -60.51295 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 015b9858-1a21-38bc-9a7a-cebc62ba1c66 | 0.46197 | -60.3984 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48684881-6830-39b1-844b-f452df95101a | 0.31493 | -60.44332 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d495a83-f06f-3250-83d6-86dc364a2c02 | 0.03515 | -60.99494 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 394e8176-3548-3536-b872-5e5487fc0f56 | 0.13219 | -60.39996 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 093e8430-bc81-3c9b-b38e-8a3ad8e65171 | 0.30308 | -60.45639 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f91b41ad-489e-3bd9-a60c-409efc3f4565 | 0.03964 | -60.97973 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b3ebbb8-1e4f-3294-9e9a-03a7544f42a9 | 0.30366 | -60.46005 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e22706e-7b3b-39b2-8b4a-7182e1555f4b | 0.13732 | -60.41045 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98619074-6c4b-341c-b8f6-4016634de30a | 0.048 | -60.98933 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11470fc8-0ffc-3ee6-8333-f737554c5545 | 0.0441 | -60.98629 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73cd87c1-7a45-3aa4-85e9-beafbddd481f | 0.46139 | -60.39474 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08aa4ac5-bf2a-369a-9a61-9ce702b3548f | 0.82141 | -60.6069 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83490035-904b-3b5e-a39d-7ef72462184c | 0.0318 | -60.99548 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73a24a65-b6f9-3ecc-9408-210d91cfbac9 | -0.16041 | -60.75006 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ee83189-a4fe-3b65-a672-e61a1a91d458 | 0.04745 | -60.98579 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 078cf756-2207-3df6-97f7-0b583b053623 | 0.05416 | -60.98479 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d86758e0-0ecb-31ca-a0b6-02c6f17c5ff0 | 0.3025 | -60.45274 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9c31d86-c203-31e9-8100-fac5da3bfd17 | 0.37943 | -60.36564 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a0f79a4-b409-34c9-a9c9-2ec14709f48f | 0.75635 | -60.23693 | 2026-03-06 05:35:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4ac814c-f0e5-3b23-8478-d8219ad0ebef | 0.03405 | -60.98787 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a68bfc3-636a-339c-9352-3e0934b5f3fe | 0.82198 | -60.61049 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 856b4e2c-5d86-3ac4-bdb7-f9841cec01ec | 0.31211 | -60.44751 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf079dd1-1315-38e4-85d2-b985e131d64c | 0.03294 | -60.98078 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c6c2231-a9cb-3c92-bcd8-0c06fe1a63e2 | 0.05081 | -60.98528 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23f50333-9ace-3b34-b9f6-f819b6716914 | 0.13617 | -60.4031 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47848826-0406-3c7f-84fb-b10315bd8242 | 0.31154 | -60.44386 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a9244c4-975d-36b2-8eac-7853717a10b8 | 0.03795 | -60.99087 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08153ec4-9eea-375a-b981-e6dc6d50e764 | 0.0413 | -60.99035 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 871bbddb-eb54-38cc-937e-82032f8f4d4f | 0.05471 | -60.98832 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e51934b-6b25-3cc2-a9d8-03545f2ee88e | 0.49042 | -60.51347 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 370a9d01-4814-359f-9edd-3f0cb10ea450 | 0.66823 | -60.30284 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89df76be-589d-3451-a653-1d53b1e528f2 | 0.13391 | -60.41098 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2277525-f28f-3abc-8ca7-8df9bf676a75 | 0.13675 | -60.40677 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0d09d7e-ceed-3344-ad18-27d07efc8d31 | 0.66482 | -60.30338 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d61e4abc-09e3-306a-a6d4-a3e40f9ff397 | 0.662 | -60.30759 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ad0f507-5d3b-396d-8551-886e5169605d | 0.45742 | -60.39162 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0ef7797-aadf-3e22-b4e0-4600aa8e5b73 | 0.03125 | -60.99194 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8b83bae4-4221-3d73-80f6-cf5ec1b04dfc | 4.83074 | -60.66534 | 2026-03-06 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2fbaa0b-346f-3fab-8709-ef8cc9a47081 | 4.83153 | -60.67007 | 2026-03-06 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 995edc45-346e-341b-b84e-d70c05969fd4 | 3.25188 | -60.74949 | 2026-03-06 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 546a58fc-7731-32a4-bc4a-c5ba3f2b6343 | 4.96907 | -60.26505 | 2026-03-06 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d41b3653-f1bb-3cd1-a8ba-7c4f3250a8b1 | 4.19948 | -60.51762 | 2026-03-06 06:03:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f9a2d08-9d52-378a-8059-41cb3a3cedef | 3.04698 | -60.84278 | 2026-03-06 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ad3904b-5741-3d3a-adba-0b77592763a2 | 4.20255 | -60.51865 | 2026-03-06 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f00ed07f-6349-38cb-93a7-886cce56000e | 3.25574 | -60.74382 | 2026-03-06 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 722142c3-e7dc-35fa-a924-04408c1d8d29 | 4.9635 | -60.26064 | 2026-03-06 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99c8179a-e2c0-3d75-be36-705c2b064a5b | 2.93099 | -61.04961 | 2026-03-06 06:03:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8925d7f8-f2c0-343a-b578-2113dc227b75 | 4.50643 | -60.54886 | 2026-03-06 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aadfd48e-ea40-3fa8-a132-6132f3e38346 | 2.47309 | -60.02538 | 2026-03-06 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a4f1a04-fbba-3172-9b7e-24ddd56bed0e | 4.96436 | -60.2657 | 2026-03-06 06:03:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8726b878-836b-329f-9fb5-618b9914a0de | 0.75907 | -60.24051 | 2026-03-06 06:05:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48abd208-5e90-331d-9976-794397c11f89 | 0.66328 | -60.30983 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b9f237c-eaae-32f8-a3be-61d16b808db2 | 0.03403 | -60.98183 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fc65b5c-0a12-3b90-83dc-37df5a72d149 | 0.0502 | -60.99004 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e5bd40d-c54d-30e6-9cd3-8cb4a8a3d83b | 0.03485 | -60.98705 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6b33d13-1bcb-3ad1-b32a-6cf1a17c23b4 | 0.05424 | -60.98424 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec9e962b-3d67-3c4f-829c-05fbddcb38a7 | 0.03167 | -60.99821 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0faaf103-a84c-361b-baa1-22d4ead60f44 | 0.05505 | -60.98938 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcfd90fb-ef13-37a8-8b9a-e147c8dfc693 | 0.03085 | -60.99306 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e69ca163-7787-3c3f-81fc-ccdb4536704b | 0.03886 | -60.98103 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75f07e06-bea2-33d7-80fb-7564b8b06b0f | 0.7586 | -60.23764 | 2026-03-06 06:05:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38684685-4c40-31fd-aa64-b7c649574312 | 0.03567 | -60.99219 | 2026-03-06 06:05:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ada83d9-8858-3e2c-87c7-5d21f81bf08b | -2.29143 | -44.6967 | 2026-03-06 12:27:00 | TERRA_M-T | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 8d901d44-1223-325d-b25e-918c1705e4c7 | -13.61914 | -53.53645 | 2026-03-06 12:29:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b1ac25ab-03a0-3577-b258-b1de58d5bfdc | -17.57275 | -53.07209 | 2026-03-06 12:31:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1be3c8ba-02cc-3be6-908e-0e6728178d59 | -23.85354 | -53.97499 | 2026-03-06 12:33:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 8adc26ca-bede-3de1-bd6c-833feec37f18 | -23.85122 | -53.98024 | 2026-03-06 12:33:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 4d63f2dd-04c2-3389-94f2-8576b7c88d74 | -23.5627 | -54.50373 | 2026-03-06 12:33:00 | TERRA_M-T | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| c64b989e-a69e-31d5-803d-b20b4cf55fc0 | -22.07139 | -56.69418 | 2026-03-06 12:33:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ef7220f-117b-330c-9efa-7bd900449d67 | -23.90606 | -53.87148 | 2026-03-06 12:33:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| e03f43d4-53f5-351f-a898-3393c618fdb4 | -22.82811 | -48.15628 | 2026-03-06 12:33:00 | TERRA_M-T | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2ae9aaf9-f1f3-39e4-a55b-f77d968add57 | -21.62104 | -56.61956 | 2026-03-06 12:33:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0bd2da1a-2864-39f7-971e-0c5f21bea145 | -21.61969 | -56.62899 | 2026-03-06 12:33:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 40a38c53-4c0b-3bb4-9e7a-b7bf4a0b72b6 | -29.22435 | -51.33875 | 2026-03-06 12:36:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 4a4d6da1-b729-3bd9-9dc4-e15e554143da | -30.59618 | -52.33096 | 2026-03-06 12:36:00 | TERRA_M-T | DOM FELICIANO | RIO GRANDE DO SUL | Brasil | 4306502 | 43 | 33 | nan | nan | nan | Pampa | 8.8 |



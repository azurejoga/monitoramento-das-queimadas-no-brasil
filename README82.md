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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| effd16cb-14bc-342e-aa26-975b4bdaba7e | -21.7965 | -48.78403 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9b45e15-7978-3237-9474-8c61522079c2 | -21.58416 | -48.60268 | 2024-10-04 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d289f4ec-8bed-3071-bbc3-556c28bb2968 | -21.35337 | -48.90228 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 172384a3-a4bb-3aec-8873-830b1fed1030 | -21.34488 | -48.88581 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2e11c6be-5209-336b-82dd-09a1d0d3826f | -21.33868 | -48.8991 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cce52fb2-9711-37a6-a53a-ad36f856177e | -21.33698 | -48.9085 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84fae611-29de-3229-89cf-790561650f49 | -21.33352 | -48.86426 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87f8a9d1-b408-3721-8ae2-0f5123181822 | -21.32677 | -48.9016 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cc90aa4-a435-36e9-8407-e226ab0e750d | -21.32616 | -48.86281 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 119b2679-b79d-3e94-a43c-c589c4eff469 | -21.32249 | -48.86206 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95e0b637-51c7-3044-8218-5d5f2c46ca77 | -21.31915 | -48.88046 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c03f9ac0-3ad5-35aa-8cae-4db9ef77df3a | -21.31798 | -48.86592 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 538d1c48-f859-35a6-aa46-29ea69211c59 | -21.31119 | -48.90328 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| be3b9bff-8f87-3d3e-aa14-d2f709f0d3b7 | -21.31035 | -48.90793 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bf7cfaf6-a84c-3f57-b79f-e20b6ca9508d | -21.3095 | -48.9126 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6aed5ff2-05d7-349f-9ede-ed74a0391da2 | -21.29845 | -48.91031 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 01ab4718-f850-34af-b876-a31ba6609abe | -21.29734 | -48.89545 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f039f00-4460-388e-80ed-32c1f9555843 | -21.28283 | -48.91208 | 2024-10-04 04:12:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b3d02c2e-5a4e-31cd-ab31-49def1fb923e | -21.33621 | -48.80727 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| d0636c94-da22-3861-97fa-ceb88dbf02ee | -21.34803 | -48.80491 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eed0d49b-3185-3ef2-a6d3-8c859a8d9802 | -21.57541 | -48.48523 | 2024-10-04 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7946fb6d-fd94-354a-bd86-c7be1bd890a6 | -21.57461 | -48.48966 | 2024-10-04 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06a51b2f-fe55-3bba-9d54-2bc04f992a33 | -21.5746 | -48.48243 | 2024-10-04 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f11c9f44-0653-3eba-b3ba-99233f0a00d3 | -21.57382 | -48.48687 | 2024-10-04 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 889c3d6f-7f89-3354-b219-f999d7adfc2a | -21.57305 | -48.49129 | 2024-10-04 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 152a7b8c-9181-37a3-a719-3b2f74963f88 | -21.57021 | -48.49339 | 2024-10-04 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 462b94fa-cf92-3f9e-bb04-171a0bff4fef | -21.40613 | -48.8772 | 2024-10-04 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59788fb9-72ff-3ae2-bf41-fa5581d7880f | -21.40246 | -48.87646 | 2024-10-04 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c27856be-8cb8-3236-86e5-777cb3580052 | -21.35789 | -48.89836 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8a6ae8c-4ac4-3cd9-acf7-c36a19d2ef1c | -21.35422 | -48.89756 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 60e30606-a4f0-3f17-9040-e5db52a8fb57 | -21.3494 | -48.8819 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2654ac02-28d7-302d-9223-0f713b64b178 | -21.3487 | -48.84344 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a30d3146-ab22-3162-a1b7-e62028ebf97e | -21.34855 | -48.8866 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c9b887fd-8dc4-3824-8cd5-c28aec9983cf | -21.34539 | -48.86182 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3305e391-2235-340a-93df-cba05a736ec2 | -21.34121 | -48.88504 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db1077c9-5c45-33de-9123-019575e70d79 | -21.33216 | -48.89294 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13658976-2c2d-321d-97cd-0984439a3486 | -21.32961 | -48.90704 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5676191-85e7-33fb-8ee8-6194fc95d146 | -21.32592 | -48.90631 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50ed5874-d794-3a87-b887-d5b4c909b1a1 | -21.31882 | -48.86129 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 273ce97c-88c9-3c3f-9300-3f2d95e09e65 | -21.31855 | -48.90485 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 03fa3084-4f73-39ae-8b81-f64f647e4081 | -21.31007 | -48.88846 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 23.8 |
| fab7af04-1192-3f61-96b2-164216ed43db | -21.30836 | -48.89784 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5ea7a10-e5d8-37d7-a4a5-36edfbb3a7b4 | -21.29931 | -48.90557 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84cdd71b-27f8-39f8-ba13-c93216b5c333 | -21.29904 | -48.88617 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f3c219c8-03ab-39a4-9699-f6b32ec1d2c0 | -21.29671 | -48.91982 | 2024-10-04 04:12:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fb8d5244-4bb9-390e-8df3-6764864a58cd | -21.29451 | -48.89004 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 552a298a-4a6c-35c9-a8fa-811e68d08daf | -21.29194 | -48.90407 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e1bc8c3e-58af-31e4-abea-b9bb1e322946 | -21.2837 | -48.90735 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 309d2e0b-b9ff-3dc3-90fb-2f94db8177f8 | -21.28117 | -48.9084 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fe2da877-a9d4-3e42-bfcd-72891ac80030 | -21.39432 | -48.8865 | 2024-10-04 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 630d7a0d-2af5-3efe-b68f-5dcab570b3e8 | -21.39342 | -48.88419 | 2024-10-04 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92bb750a-6659-319a-a733-cb3963f513f9 | -21.35873 | -48.89365 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bbd8eb9-ee79-3048-9d9c-6fb416e83206 | -21.34602 | -48.9007 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 5ea423ed-9450-33a6-811e-8abab01ec8f0 | -21.34235 | -48.8999 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 21.6 |
| f5fec8ae-e0a5-3baf-a883-8669e08836aa | -21.33783 | -48.90377 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9798c25b-887a-3a31-bbd3-20a30929e761 | -21.3333 | -48.90776 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d212a0d6-56d4-387a-b9a1-b255db68198e | -21.33186 | -48.87345 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a92e57e-de90-3759-9649-e81e32fa1d1d | -21.32847 | -48.8922 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1aa6e200-c33d-3059-967e-f8e5dad79fa2 | -21.32651 | -48.88198 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b5ad85e6-8fcc-3c93-ba52-f6955d7601f7 | -21.32309 | -48.90087 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b63bdee-9b4b-3366-aadc-862e6223bbca | -21.3194 | -48.90012 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40693cd5-6f5b-3137-b008-c88795c0e5fa | -21.31572 | -48.89937 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1bf53895-38a8-3844-b4b4-a6db530f6588 | -21.31547 | -48.87974 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7c2911f8-8877-3d94-b78e-b8398ad4477e | -21.31487 | -48.90407 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0e357e7c-9fb2-3de0-a3ad-59c1f3d85650 | -21.31375 | -48.88919 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ff940133-e01b-3bc9-8151-65fd0db9dd04 | -21.31204 | -48.89862 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bf4ec66-66d7-3fe9-abe8-b636e900eb42 | -21.30921 | -48.89317 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 276df2b3-7f72-33c1-a38b-6219d299183e | -21.30811 | -48.87827 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e79b98d2-fda5-323a-bd74-3495b3c8d8fc | -21.30667 | -48.90713 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 02ad6dfa-1734-3e4e-be50-886f9d1c467a | -21.303 | -48.90634 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f26bb7b8-1f6e-3b91-9cec-67558c6282d3 | -21.30271 | -48.88696 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ef9f964c-8687-3491-8209-20679a5440a4 | -21.30214 | -48.91105 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 7e551485-86ca-33f2-843d-38b4abb7bef9 | -21.29563 | -48.90481 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5a45782-291b-3d4d-97bf-f4e40a5f232a | -21.29476 | -48.90956 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 117.1 |
| df2eb8e1-9da8-3417-8521-b954c1870640 | -21.29367 | -48.89466 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ce11bbb-2515-3297-a27b-35b451a9de21 | -21.29303 | -48.91904 | 2024-10-04 04:12:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 25d4062a-4070-3bd2-bd4f-78b6334e4942 | -21.29281 | -48.89935 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2aa60046-ae56-3ecc-86b6-0af456746a67 | -21.29021 | -48.91358 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 926d970a-eb88-3c5b-82fa-b2830b09edd5 | -21.28999 | -48.8939 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf3cd784-8784-32ba-90e6-882f195a00a1 | -21.28935 | -48.91827 | 2024-10-04 04:12:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e0716454-9459-3714-a06f-b09b41acaeae | -21.28913 | -48.89859 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 50779e28-e48b-3d12-9d4c-0c6b9cba0dda | -21.28826 | -48.90333 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7f2f3b5e-83d7-31f1-9516-6c58f58baeb2 | -21.28739 | -48.9081 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| fb9d3ef8-1652-343e-a5b6-c34510c39049 | -21.28457 | -48.90261 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7dabc01d-5479-3d40-9013-407662b80a77 | -21.28201 | -48.90367 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5235fe21-00b2-32ce-8793-57ef32058552 | -21.33255 | -48.8065 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 07282103-b9c3-321c-b8bf-8f336997ec9a | -22.37535 | -49.04365 | 2024-10-04 04:12:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5ba0f8b7-e5e4-35b2-a37e-c9c22518ffac | -22.37169 | -49.04292 | 2024-10-04 04:12:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 29c74d1b-cea6-3f54-9dca-f370707c504d | -22.34937 | -49.22774 | 2024-10-04 04:12:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a285da7a-af88-30ab-8792-d8805d4b3744 | -22.38653 | -49.25515 | 2024-10-04 04:12:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 792ba081-6d5c-3c9d-ba2a-ba02a670f95e | -21.81266 | -48.77803 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50ed82b0-96a3-391c-8804-b2c6def32d56 | -22.54101 | -48.81532 | 2024-10-04 04:12:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f4a3425-432f-3694-817e-c459e1e4dc28 | -22.4659 | -50.12446 | 2024-10-04 04:12:00 | NOAA-21 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d21dee4-b71b-32fc-8edf-ef5f5af8a1ef | -22.46204 | -50.12363 | 2024-10-04 04:12:00 | NOAA-21 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 939c4c1b-598d-3b09-bf34-b1cf34cbfcbc | -18.11641 | -49.28427 | 2024-10-04 04:12:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8a69825-0037-3b77-8213-04a45a352c21 | -18.11248 | -49.28337 | 2024-10-04 04:12:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eee3095-6277-3aa4-9c2b-7b660e7dda24 | -18.11151 | -49.28868 | 2024-10-04 04:12:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 309e0dd0-19c7-3beb-9665-f0c2f781c38e | -22.26993 | -51.48487 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 7c879396-cb2b-34c6-851e-22cb8f39c0c3 | -22.2691 | -51.48905 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 856f8d89-b7cd-34c2-97e6-c496a1c998bd | -22.26655 | -51.47977 | 2024-10-04 04:12:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README83.md)

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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f32fc9f1-6521-321a-ac74-07408c7f2317 | -6.39191 | -45.51183 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d69d752-d82c-32da-bbc0-a3b7841c65ec | -6.37672 | -45.55202 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 3930bd7b-9742-35e1-aceb-b9af6f146aee | -7.03167 | -44.65128 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 59691517-18b0-3800-98d7-49b1714a69ab | -5.4886 | -42.15591 | 2025-08-23 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f68d7308-72c3-308a-a3c2-b7c43df664e9 | -3.55184 | -41.62284 | 2025-08-23 04:00:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 61a768a8-4420-3095-a817-c957c0f5c87e | -7.03779 | -44.66258 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5209c0f0-876c-3931-a531-fb0d0a5ace3f | -5.36029 | -45.19344 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61aa39d2-ae45-3182-b484-5d5d1d2040f7 | -7.60758 | -45.24908 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3072f5c9-2af7-3f4f-ad0b-9c532ccbcc46 | -6.60353 | -44.5658 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 8b6a8ebf-1083-381c-b307-5b199a5ae587 | -3.43466 | -49.04424 | 2025-08-23 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 915e8405-e200-3fdf-a857-8ae25cb5fdbd | -2.25318 | -47.85152 | 2025-08-23 04:00:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc8818c7-05da-3ab7-90f3-4aa4a40f0a40 | -2.91487 | -48.30442 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffe054ae-4176-39ac-aa20-34ab8d9f67e1 | -2.7006 | -48.20955 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11341776-b618-3ec9-8a0e-d6f9d413944e | -7.87003 | -46.29366 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ee2e61d-8ce4-344b-8d3d-2bb318957a89 | -2.38153 | -47.66278 | 2025-08-23 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17258d8e-921a-3eae-8e60-7431b1c72245 | -7.62938 | -45.24177 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6e6685b8-9fd1-3c75-acd5-ae374e1f4898 | -3.51592 | -47.21177 | 2025-08-23 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4dc8d2a-99b1-3018-936a-7442c7e7f148 | -4.07454 | -48.04078 | 2025-08-23 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd0de4e6-3805-3aaf-a3b8-a463c5361565 | -6.36716 | -45.55806 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 896c0e1f-3fe7-3975-b7be-72572f4f6301 | -6.3761 | -45.55579 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 050fe4af-6131-38b7-9264-234fe437e48b | -6.60743 | -44.56643 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| d200d867-3ea9-3261-b4a3-74837bcd2d62 | -7.6506 | -46.28286 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b987958a-76d7-39fc-8265-25b4af41cfd7 | -6.11574 | -44.37865 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3d3bf40-9333-39b4-8bd5-c6ce371a57fa | -7.20898 | -45.31329 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39fa4a65-3cb6-3cf7-a036-f688795b17a2 | -7.64705 | -46.27781 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2baa7a5-dbf1-34e5-9155-642b3ecd8e99 | -6.77305 | -44.31901 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f88ede47-116e-364e-aae8-0dbf8ee04b01 | -2.91431 | -48.30773 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fbb4b70c-eb5e-3a43-a5fe-8daf055e7bad | -6.18403 | -45.43182 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c7b979de-773e-3c4f-bd8d-94e0d924c072 | -3.54838 | -41.62229 | 2025-08-23 04:00:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b6ef50b6-23d2-382f-84ee-e39f3e967e3c | -6.992 | -44.14417 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88399331-e8bc-33a9-87ca-fdb4d897fa20 | -4.30627 | -48.1016 | 2025-08-23 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c1736c2-2dbc-3927-8d03-3f2441d10826 | -7.62054 | -46.25249 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96731523-2029-3f60-a40e-7d8c728acaa9 | -6.28211 | -52.82412 | 2025-08-23 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef959b52-22aa-3252-9f26-a01a5db7e6b4 | -2.7059 | -48.21043 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed7218b2-93a6-33f4-8975-63c88af2a849 | -5.87571 | -53.62597 | 2025-08-23 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e154b331-b82d-3989-99be-06599e1d9061 | -4.53016 | -38.23009 | 2025-08-23 04:00:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d257ba42-e8b8-38a0-9a38-e89237690133 | -6.42101 | -41.21768 | 2025-08-23 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3394c38a-58af-3ea9-b988-347408525e38 | -4.84866 | -42.84604 | 2025-08-23 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fed6775-79b2-3cac-897a-fe39772bf312 | -6.39007 | -45.52296 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d4384c9-7918-32f3-a62e-da4893a9db7b | -3.64892 | -48.33009 | 2025-08-23 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1b642b6-f1cf-32fd-a722-bbf0ec8fa704 | -6.5678 | -42.98762 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9aeb0564-d656-3d2e-bca8-0a3824d45b00 | -6.79046 | -44.99146 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fecf2407-b18f-338a-bb0c-df30a232cfe4 | -7.42884 | -45.41985 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7f7ef36-4199-3692-b389-0d78a4665f4b | -3.04831 | -47.02007 | 2025-08-23 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6111e60d-9791-3c50-a745-7f2f1e1fc518 | -6.38404 | -45.53362 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b4200097-c9e3-3104-8bda-c46e4fcfa088 | -5.83075 | -45.16689 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 441a2693-6c13-3241-8376-abc427ef4a14 | -6.49864 | -42.98457 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64b0fb68-744f-3617-84bb-109138a0e432 | -6.52494 | -43.8701 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 87bfb134-893e-3b1f-8a9b-6a51b16ce005 | -7.63055 | -45.23468 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9e5cc975-cf1b-3a34-904d-f0616ac4565c | -5.22826 | -37.85708 | 2025-08-23 04:00:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e274a97-0c25-3d25-8f89-c4864712d829 | -5.83014 | -45.17055 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1d617e7-fa34-36c0-80a6-4e0963226109 | -6.76926 | -44.31811 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d355ec1-12f3-3c84-956b-9b7ffefbf9ef | -7.62538 | -45.24107 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2a9aa8a6-4481-378d-8fc0-04da2a0407dc | -5.8883 | -43.4537 | 2025-08-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 483c2769-1d1d-31aa-8cea-d0ba4c4b6ab0 | -7.21302 | -45.31403 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a30a17e-6fcd-3826-ab94-a18ccc1fd8e9 | -7.42945 | -45.41624 | 2025-08-23 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 786aac72-98b5-3be0-bb97-83252b5a076d | -6.93411 | -39.56132 | 2025-08-23 04:00:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e186ab77-1a33-3459-a32d-8440e576be05 | -6.11178 | -44.40268 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2c75c07-cd93-3558-a8c6-dfb96bffe3df | -6.42157 | -41.21412 | 2025-08-23 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 768fa267-3733-30f7-a6e6-9a79bfae5241 | -6.5187 | -44.42375 | 2025-08-23 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4b59f68-8cbc-3d05-8e97-bc332a5eca09 | -3.75757 | -41.02938 | 2025-08-23 04:00:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2b24eb8-38b9-3feb-b1ac-fbb1c14eae61 | -7.07945 | -44.0594 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 334190fd-e152-3526-84d7-fba96ee0ef01 | -3.24109 | -39.52472 | 2025-08-23 04:00:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 755d64a1-d06c-3eb5-ab9f-26183bec924e | -6.50206 | -43.11982 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b66131e-1f08-3478-a8bc-3fbb7609846d | -4.31563 | -48.24488 | 2025-08-23 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea79b934-b5b3-3e2f-aa2d-b4fd3ac9b289 | -7.64754 | -45.2416 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7367aa37-0825-384c-993e-35575525b417 | -7.73928 | -45.7326 | 2025-08-23 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f8dc5c4-8cc0-3059-a57d-d8d78ac74efb | -6.18342 | -45.43554 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| e9169176-2626-3bbd-b88f-5ba192cae660 | -7.6046 | -43.02729 | 2025-08-23 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 01efd4ca-5bad-3bcd-bc71-cd4ff91be710 | -6.93743 | -39.56184 | 2025-08-23 04:00:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2d4cfadc-da70-344b-b4da-67f559acfd11 | -6.50221 | -42.98516 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 828b0b7f-19bd-3e09-b320-0ad8cb6ee1e1 | -8.08049 | -43.68369 | 2025-08-23 04:00:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f5d132a-94d2-3981-90dd-da784ceb3dd8 | -6.39236 | -45.51875 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f20ddcf7-0dfb-39c6-a2b1-7d0653506836 | -7.02778 | -44.65062 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5ce923a5-ea89-32d1-b883-403c23a13f63 | -4.12211 | -48.11601 | 2025-08-23 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 753791d0-4992-3531-b271-3e9a71cbd340 | -3.97849 | -43.2435 | 2025-08-23 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fac0b68f-6ace-3435-9205-1dfe1fc18801 | -4.34363 | -46.46562 | 2025-08-23 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| f50d8960-e3f0-3d6e-9ede-b9ead7c1dae7 | -6.37548 | -45.55956 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 5a390890-8434-32b2-be06-30460de532c2 | -6.78448 | -44.32124 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a8f4ef6-6632-3935-8d2c-a3bfca090a6d | -6.40449 | -45.49789 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c77cd6ef-e6b0-3e82-963c-d1bc6a3b4c91 | -4.14309 | -46.45596 | 2025-08-23 04:00:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07773566-ca32-30f8-8d7c-d40c851afe62 | -7.64206 | -46.28123 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5df341a7-1195-3189-9d2d-fe121ed08e3e | -2.2584 | -47.85231 | 2025-08-23 04:00:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe98fdb7-00e4-37f4-98cc-28fb7981ec5c | -6.04998 | -44.36016 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8bd2385-659e-3478-be99-d00d81e9552f | -6.37194 | -45.55506 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 11741319-95d6-3c12-aeb9-7f153a3a67c6 | -3.55591 | -41.6196 | 2025-08-23 04:00:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3fe011df-5626-3644-a774-5b67128d96ef | -4.59267 | -48.95883 | 2025-08-23 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82ea73a4-1e54-3a04-8f4b-6570cee55723 | -2.55457 | -47.71551 | 2025-08-23 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fca0a6fd-6ab4-3269-a0c5-d96f5a7edbf3 | -6.59883 | -44.57 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8e0e74ba-c101-30a0-8796-c7db9803ab92 | -5.46679 | -42.91716 | 2025-08-23 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1f3f7d90-8056-326c-9ce3-40e06063cebd | -6.31637 | -43.74716 | 2025-08-23 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 581abc97-465d-327d-acca-470b86a46553 | -7.08092 | -44.59494 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 769cad67-ade3-37e5-a613-bfc568adaf56 | -2.90843 | -48.24588 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69427087-076f-3e5a-a049-45ad31caf051 | -7.61626 | -46.2518 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcff29d0-44e5-307d-84a7-42be33ece7e6 | -7.06997 | -44.61299 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b320226-c93f-355e-9a6d-aa47cd47c7fd | -6.40095 | -44.28844 | 2025-08-23 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0c4cb4c-1b1c-371f-a57a-d0d21a0a972e | -7.08413 | -44.05784 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79bae66d-5755-3675-87d3-f5edc23f715c | -7.60981 | -44.37191 | 2025-08-23 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02e3ffef-4cc9-381a-8d64-08c4bdaeb4c0 | -4.12159 | -48.11903 | 2025-08-23 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7306795b-cda7-3f63-a6eb-92ad278398e5 | -3.816 | -41.56557 | 2025-08-23 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README25.md)

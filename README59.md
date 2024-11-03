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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c40b448-cb6e-34a0-b292-770ad223344c | -3.08285 | -54.15097 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2efda666-6940-3da7-965a-ee992f79077f | -3.08214 | -54.15548 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| eaf99dc1-1744-31fa-b612-dd22c9ae1be5 | -3.08142 | -54.15998 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f0a9bd6-c263-3f4f-9ae8-4edcf27ceea8 | -3.08071 | -54.16447 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f942aabc-52b5-35d1-b058-6774efb0eaa0 | -3.07912 | -54.15034 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8e9ba9f8-dfd8-3315-b5fa-36bd0fe5532b | -3.0784 | -54.15485 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 687e954c-ce19-3735-9895-37c49ce5d70c | -3.07768 | -54.15937 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 56f91490-f0c4-3a30-8ba4-5e1517a47e1b | -3.07697 | -54.16387 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e8c0367a-e9b8-3c5a-9ac3-d3000fb21c7e | -3.0761 | -54.14521 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec59e2f9-63ec-3e78-b4f8-57512284fdfe | -3.07538 | -54.14973 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09efb543-a5ad-31e2-bd85-0dd2a39fae5d | -3.07466 | -54.15424 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2ce90dde-b4e9-340d-bfcd-31925f96c0c5 | -3.07394 | -54.15875 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2fb9fe18-6a72-3d84-9785-deed4ae933c6 | -3.07322 | -54.16326 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2daa348b-dc8e-34f7-ac46-564a5d0d369b | -3.07251 | -54.16772 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c73aff55-58dd-333d-86e1-86361a9bdaeb | -3.07236 | -54.1446 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59988a26-2edf-39da-be5a-7ec0c52300f3 | -3.07164 | -54.14911 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ba1c1186-dee8-31a2-a88e-cda370683571 | -3.07092 | -54.15363 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f0072e9a-0eed-35bc-a814-0da5690f7fc9 | -3.0702 | -54.15814 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f44b44f0-ff2f-366d-afbc-babf454d4e50 | -3.06948 | -54.16264 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1654229f-9a58-35bd-aecb-be89458dc1c0 | -3.06877 | -54.16711 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 947006e8-09ff-3237-96cd-48822c932ace | -3.06862 | -54.14401 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5775417-89c5-3a05-9b46-049aff45dfaa | -3.0679 | -54.14852 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 36d68d22-e092-3cce-8a8d-d3b21917cc91 | -3.06718 | -54.15303 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8e1e1e30-f0fb-33e9-806f-7f962db2820b | -3.06646 | -54.15753 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 882fe799-e16f-3c68-b0b1-1b2d64d8eef0 | -3.06574 | -54.16203 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 06e8e61b-243f-342c-9f8c-c914aca03051 | -3.06503 | -54.16651 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef0699ab-a88d-3f53-b405-f580343e2b03 | -3.06487 | -54.14343 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f19881b4-946b-36e8-903e-e8c80304f343 | -3.06415 | -54.14793 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f30f78b0-0c20-3a8e-9ae6-3e57fcf239a6 | -3.06344 | -54.15242 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8c697b8b-6786-3f01-9830-5eef5a80f82b | -3.06272 | -54.15692 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 345c9cec-69dd-3ccf-8f60-06704fd28ca8 | -3.06041 | -54.14733 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4a050f62-0d3f-34d3-bfef-18f2b3c48cee | -3.05969 | -54.15182 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 726bc21e-0d33-3e80-b316-19d98573383d | -3.05897 | -54.15632 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9b37c752-ae6b-341d-be65-fae352c8261a | -3.05739 | -54.14225 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68673516-80a5-353e-b2f5-7ffa9780c793 | -3.05667 | -54.14674 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b2292c3-c817-301c-8dc4-0c890c886ac0 | -3.05595 | -54.15123 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b699e123-6f29-3877-b6e6-38efdd22ddf6 | -3.05523 | -54.15573 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 662e877b-4fb3-3320-a6b4-68bd9041ece7 | -3.05365 | -54.14166 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b19aa1bd-73f4-38da-8a1f-36d3160480bb | -3.05293 | -54.14615 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac7aab2e-a53c-3fd0-ad95-493109c6360b | -3.05221 | -54.15063 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9beb5259-ae74-373c-9276-9d81ce398998 | -3.04991 | -54.14106 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cc35135-3993-3beb-8fb2-ba60fef58522 | -3.04919 | -54.14555 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40e641ec-a094-3703-9bbf-c08605124ebf | -3.04846 | -54.15005 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49c41d41-82cc-3fe0-940f-196a1c70aeb9 | -3.04545 | -54.14495 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e3473e9-6d81-364b-b419-0c0cd206d704 | -3.01386 | -54.10326 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7ec25a8-fe3b-3e44-929f-0ff2d00e54c7 | -3.00523 | -54.09923 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9704c1be-aa1f-3770-afec-31887c063f31 | -2.99655 | -54.13008 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09ddcd69-4aae-38bb-a10c-b61107fe0615 | -2.95018 | -54.13216 | 2024-11-03 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 592f30a5-1f30-329d-8a2f-e43f33b1e527 | -4.42599 | -55.39213 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ca25f70-29f9-3095-994b-c9939dc8e12b | -4.42124 | -55.3964 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5df060c3-2261-39db-9f25-e68a74475be9 | -4.41808 | -55.39075 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d70fc6ed-49a3-35bc-8274-e0261bc78f95 | -4.41728 | -55.39575 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f47882a-e56a-3cdd-aefd-e6ed6a62cd07 | -4.41509 | -55.43476 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ba15058-39e1-3475-b570-d815774724f3 | -4.41332 | -55.39511 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe376a7c-7a58-3518-8845-853da48bfb28 | -4.4125 | -55.40019 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c51cb353-2b6b-340d-b1a1-84254cf7aa6f | -4.33733 | -55.318 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5b7dfcd-701d-37bf-82cb-c392663e7804 | -4.337 | -55.31585 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d9fd7d8-2c7b-3fc6-8ab8-dde9d323c952 | -4.33616 | -55.32086 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed483b07-9904-3490-a944-60575f103b96 | -4.33338 | -55.31741 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7af3b9aa-4a0b-32a8-962f-ed7d517ffb2f | -4.29898 | -55.13142 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e765dab7-f3a3-39c1-b8f5-31186592daf4 | -4.27307 | -55.14274 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31f7d9da-59e3-303c-888b-98cf7ca12249 | -4.27231 | -55.14532 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c01df9b0-d43a-3d80-8f4a-faac70ae6859 | -4.27226 | -55.14763 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a39425f-da8a-30e4-9416-047c73eb0d18 | -4.27144 | -55.15263 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fbb3ccc-444a-390a-99dc-48142002c129 | -4.27073 | -55.15531 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3b9e3f4-9474-32b3-9c36-e4c842dabf6e | -4.26361 | -55.15144 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c11750b2-9106-3b54-bd31-13a21234434f | -4.2629 | -55.17944 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9918e907-3ed7-3f72-a98f-f7ba12b1e232 | -4.26211 | -55.15911 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b163ee67-8a64-3910-ae04-26b09a637a02 | -4.21083 | -55.40543 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a563d61c-06dd-396c-81f7-d444433aa87c | -3.95932 | -55.33964 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c31fe9b-934f-3bd7-bd84-9eb20f4e61f7 | -3.92361 | -55.38321 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36f47ba8-7947-3d92-bc9c-521527048ab2 | -3.89351 | -55.37812 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc3424d6-2c0a-39e4-880c-34d086091071 | -3.6446 | -55.27011 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0757a19-b153-3428-a21d-8b794d17e72b | -4.50728 | -55.46055 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8304b37f-9568-3d1f-963d-18bb6cdf0c9f | -4.50673 | -55.46397 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeb2025f-0252-3a0c-b45f-09260b9080c4 | -4.50504 | -55.47442 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b68d2eb3-273b-3ae0-a62f-b84b78e723f4 | -4.50162 | -55.47033 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cd4c665-2c2a-3067-9d38-a467dfbd811c | -4.49764 | -55.4697 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb2c6b94-8385-3cc6-bb5f-b3a76dacaabb | -4.08523 | -54.34678 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd2d4fd4-5ccc-3cf5-981d-21f746788e18 | -4.08452 | -54.35111 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93e2250d-5564-3a61-bbb5-a9c258b80f18 | -4.02213 | -54.34835 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1360e8a8-90bd-315e-9ea5-02c9d1e6efde | -4.01885 | -54.80126 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fec9f5f-4d2d-3814-98d3-d33ed7788f34 | -4.01501 | -54.80063 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfa75141-40cb-3ed6-a60d-4474f1094746 | -4.01113 | -54.82437 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dc56614b-eda9-3928-a09b-b195f8136a11 | -3.90508 | -54.16308 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94e39090-2d04-3383-9fe1-7f9855b10913 | -3.8783 | -54.14089 | 2024-11-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93e13e09-5d9c-3f77-b200-ff52d0d79965 | -3.73719 | -54.06699 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b8ae6b6-3a7b-33c9-b57f-6ff23eded5f7 | -3.73349 | -54.06646 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64d7b9a3-c54d-38a7-a2ff-151fdc61d77f | -6.22599 | -55.65666 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75362975-d0b7-3681-992f-72f0fd9fbb02 | -6.22368 | -55.64611 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c94e227-c77b-3a23-9b7b-b45a0965ad81 | -2.04972 | -56.35877 | 2024-11-03 04:46:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55d34b71-e20c-3d0f-80c6-01f853b976d1 | -2.04575 | -56.06544 | 2024-11-03 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 93ffc940-66d7-3ca3-81bf-8c61f91bba64 | -2.04533 | -56.3581 | 2024-11-03 04:46:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a607187-e46d-3b8a-be62-cc0c9dfa4952 | -2.04511 | -56.06951 | 2024-11-03 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9d8cbf70-c2ec-386a-bde0-aef95ebbb1ae | -2.04448 | -56.07358 | 2024-11-03 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1444ac00-2ac7-3f1d-8b03-83b9f9c82c14 | -2.01585 | -55.86779 | 2024-11-03 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| beb6e7e9-a028-39ee-adc4-4ada0bcd62ae | -1.92307 | -55.46404 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c127296-ca2f-3407-b505-08fccc883d42 | -1.91953 | -55.45962 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a90e5a1-6b8a-3ddb-a5d0-5f1159f0738f | -1.84171 | -56.2768 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ffa9673-4e4a-3d2a-bb29-fcbfcef32f1b | -1.82275 | -55.2781 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README60.md)

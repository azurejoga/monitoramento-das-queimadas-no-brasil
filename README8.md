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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77ac13e9-ff87-3035-bcd7-6ee1b8d1f5a4 | -8.1822 | -43.2034 | 2025-11-29 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| f78e54c7-931b-3663-96d1-c56674924ca7 | -20.2262 | -47.5051 | 2025-11-29 01:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 10c0e0a2-26d5-3f77-8bf1-8bd4be798d4c | -2.8031 | -47.4119 | 2025-11-29 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 95ac3e3c-eb2e-307b-92d3-ca2bb1e9d15d | -2.803 | -47.4337 | 2025-11-29 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 05410386-818a-3165-a668-64113ccdb3c0 | -8.0507 | -43.1472 | 2025-11-29 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 153.7 |
| 909b84d3-7938-3081-b6c3-1dd498ffa995 | -3.1068 | -45.7903 | 2025-11-29 01:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 02a175f9-6d04-379f-b56c-31be19d7eb3e | -8.0321 | -43.1257 | 2025-11-29 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 365.0 |
| 49e8cf13-36de-329a-8492-36630c8c8a84 | -8.0318 | -43.1493 | 2025-11-29 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 172.5 |
| 8fdad4d2-484a-3b96-b432-0746fab895e6 | -3.3572 | -44.0591 | 2025-11-29 01:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 58499356-28c8-3603-a3fa-b5585d2543e3 | -20.4503 | -47.4995 | 2025-11-29 01:00:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 74817702-a18a-3f86-81a8-bcba07de50ec | -1.4737 | -45.7907 | 2025-11-29 01:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| dc621e49-62af-3056-ace4-42adbdee7293 | -20.2262 | -47.5051 | 2025-11-29 01:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 59.8 |
| b8f777cd-1903-3470-9276-468ad2e51343 | -8.1822 | -43.2034 | 2025-11-29 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 9f912c1d-58f5-3232-b90d-d05de968a6a3 | -8.051 | -43.1237 | 2025-11-29 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 301.2 |
| 1a9a4134-76a2-3be7-9e97-7da3336834db | -20.4503 | -47.4995 | 2025-11-29 01:10:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e7026bbf-568b-3e90-9fb0-0b52c69a1333 | -20.2256 | -47.5285 | 2025-11-29 01:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 6576c6d3-05b7-379c-9fb4-744d1fc40480 | -2.3459 | -45.7036 | 2025-11-29 01:10:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 87e9a5dc-cb2b-3e5f-8bdc-162bb3e3acb1 | -8.0507 | -43.1472 | 2025-11-29 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| 426b5bf8-85e6-3849-9b55-2580e3eb925f | -8.1633 | -43.2055 | 2025-11-29 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| d0eac732-0a89-3f58-9d9f-9407a48a3f31 | -4.3727 | -45.5538 | 2025-11-29 01:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d736521a-212b-3d38-b1e9-99bd25624851 | -2.803 | -47.4337 | 2025-11-29 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| d704a527-6ffa-317f-ae4d-00862d5ddc52 | -2.6322 | -48.542 | 2025-11-29 01:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| a4f091d0-b32b-3b36-b43b-0a23d72ba75f | -3.1068 | -45.7903 | 2025-11-29 01:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 342d87d5-49ac-3833-9d1a-bf1fc1ca4825 | -8.0318 | -43.1493 | 2025-11-29 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| 0085478e-ee57-3b0a-a06f-be4f1c7609c5 | -4.3914 | -45.5528 | 2025-11-29 01:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 41c7d0d9-66f9-3982-82b8-f876b8597b7d | -20.1813 | -52.3754 | 2025-11-29 01:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 104.6 |
| f6033556-9a94-354a-8a7c-f78330e8fce5 | -2.7845 | -47.4343 | 2025-11-29 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| e3f667de-674a-34d7-8156-e54c0e8b55af | -8.0321 | -43.1257 | 2025-11-29 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 319.9 |
| 4983c427-158b-3b14-8fb8-265e62500ec6 | -3.2134 | -46.8283 | 2025-11-29 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4c5b32a2-c880-3b27-9aae-4d6115718077 | -2.8031 | -47.4119 | 2025-11-29 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| adfb1ffd-8865-38dc-87c2-6a7c78030120 | -19.1273 | -52.7152 | 2025-11-29 01:10:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2d7acfd1-2d0f-3eb6-8867-0d2b3d7a33de | -1.4923 | -45.7903 | 2025-11-29 01:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 941d8330-2734-3682-bb76-a20ca9cdfa46 | -2.7845 | -47.4125 | 2025-11-29 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1cf5f199-ff95-384a-9a04-787907145de8 | -2.3459 | -45.7036 | 2025-11-29 01:20:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 74e32195-6a63-3e95-895d-c37f01c3ccab | -1.4923 | -45.7903 | 2025-11-29 01:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 50ca7ef8-322e-368e-a5ef-45af7e99ef93 | -2.803 | -47.4337 | 2025-11-29 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a497b30f-0050-3aa5-a297-e3bd8a1155ea | -20.2262 | -47.5051 | 2025-11-29 01:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e571e3c3-5023-3230-9390-12b5d0d68eeb | -8.1633 | -43.2055 | 2025-11-29 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| c7e0f30a-6028-3938-a843-00496b288c60 | -1.4737 | -45.7907 | 2025-11-29 01:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| afa95d5d-86a0-3fe7-8a59-fc0f6f113d1d | -20.1813 | -52.3754 | 2025-11-29 01:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 208d4351-9944-32ee-8500-ca601f6806b0 | -2.7845 | -47.4125 | 2025-11-29 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 701bb3a4-1403-3006-a5b3-b96754d03e3d | -8.0507 | -43.1472 | 2025-11-29 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 8b84272b-72aa-3e9b-a28e-76364e7a83c6 | -4.3914 | -45.5528 | 2025-11-29 01:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 81e936ba-0bab-36ce-8cef-157bb360691d | -20.2256 | -47.5285 | 2025-11-29 01:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 66512c85-2f68-33e6-8a6a-4993ab98dbb4 | -20.2016 | -52.3717 | 2025-11-29 01:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 109.7 |
| bab66d07-7403-3066-a56e-a4b1887f94cf | -20.1807 | -52.3975 | 2025-11-29 01:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 83.0 |
| fcc6f5cf-5d07-3e3a-8aee-7d7eb02791e3 | -3.1068 | -45.7903 | 2025-11-29 01:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a7472c47-47a2-3bc7-bbff-ffa3ecfee9f7 | -8.0321 | -43.1257 | 2025-11-29 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 327.6 |
| 43149b6e-9a2c-3b07-9c50-269c773ff980 | -8.66 | -44.2232 | 2025-11-29 01:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 5263fd8c-e241-3f18-852a-8b96e036cbde | -20.4503 | -47.4995 | 2025-11-29 01:20:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 38a41d82-abf2-32d7-9b78-e46b1e9352e8 | -20.4496 | -47.523 | 2025-11-29 01:20:00 | GOES-19 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 59ef022e-dde6-32d9-a8ee-4f8fc22a2b5e | -4.3727 | -45.5538 | 2025-11-29 01:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 26c9dd92-8c71-3c4a-9a5f-34e9276cff25 | -2.7845 | -47.4343 | 2025-11-29 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 8ca5de14-d4d4-3ae7-9a52-a4bdf902f8bd | -8.051 | -43.1237 | 2025-11-29 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 210.0 |
| 4592708f-c08a-3a57-872c-10b7a701f46c | -8.6789 | -44.2211 | 2025-11-29 01:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f5133ffc-91e2-3948-bbd1-7d127faed456 | -3.2134 | -46.8283 | 2025-11-29 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d18a4a5a-c0a8-304e-a385-b61170bdae91 | -8.0318 | -43.1493 | 2025-11-29 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.8 |
| be8fd27e-3045-30cd-895d-a3f284f217c8 | -2.6322 | -48.542 | 2025-11-29 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| d7ce84cc-8d40-329b-8605-4df71da8b050 | -2.7845 | -47.4343 | 2025-11-29 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| f0876fbd-0cab-388b-819f-f2e871261688 | -2.9792 | -45.2567 | 2025-11-29 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 5571f679-4434-3dce-a3d0-c669a62732bb | -8.6789 | -44.2211 | 2025-11-29 01:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| b4b73657-991a-3f6c-849a-a9c0aa1444a0 | -1.4737 | -45.7907 | 2025-11-29 01:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e111f1c8-c40e-323d-9e34-44cb251f385a | -8.1822 | -43.2034 | 2025-11-29 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 13beea08-8688-318c-9249-8f2ed62f0684 | -8.0507 | -43.1472 | 2025-11-29 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 18104333-4d80-3259-831a-d02ed880646b | -20.4503 | -47.4995 | 2025-11-29 01:30:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b695125f-78d8-3352-baa9-73f71ed46359 | -8.0321 | -43.1257 | 2025-11-29 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 243.4 |
| 97ed4f7c-9088-3817-aa98-44b349b84ebd | -20.1807 | -52.3975 | 2025-11-29 01:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 441932d8-90b1-3994-9d9e-44c359d5509e | -8.1633 | -43.2055 | 2025-11-29 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 7ea49ee7-078e-3f94-b80b-7e47e37c7e76 | -2.9793 | -45.2341 | 2025-11-29 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7bcef6a8-45bd-3610-9ce8-27ec7c75d17e | -8.0318 | -43.1493 | 2025-11-29 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 610b5df0-e6d1-3475-953b-27ea32acfd1d | -20.4496 | -47.523 | 2025-11-29 01:30:00 | GOES-19 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 885e5245-d5c4-331c-b42a-bbecc06e86c5 | -1.4923 | -45.7903 | 2025-11-29 01:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 49ec3775-c495-30be-b42f-4189e7f14580 | -2.6322 | -48.542 | 2025-11-29 01:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 75617a18-1b54-34c0-af76-a8145b3600fa | -3.2134 | -46.8283 | 2025-11-29 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6cae1bc0-f6c2-3b67-a205-1a412fa9b22e | -20.2256 | -47.5285 | 2025-11-29 01:30:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9b02afb0-39ce-3252-b012-a0c3c1a49e48 | -2.7845 | -47.4125 | 2025-11-29 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 8f6aef60-e36c-321d-aeb7-a347d1b24b73 | -2.803 | -47.4337 | 2025-11-29 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| abe7c834-ea3b-3f55-abd2-e07395a2dff0 | -20.1813 | -52.3754 | 2025-11-29 01:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 8cefe020-957b-34d3-945d-630981a16dc9 | -8.051 | -43.1237 | 2025-11-29 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 225.5 |
| 3a03929e-ba50-3b33-82fa-aade98bb854f | -19.1273 | -52.7152 | 2025-11-29 01:30:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 5045460f-9c5f-3bae-a179-64929ba135be | -20.2016 | -52.3717 | 2025-11-29 01:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 69ce9e09-cac2-37a6-be61-96cb77c5668c | -8.0318 | -43.1493 | 2025-11-29 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 147.1 |
| 0bd0eefc-db70-3b8d-8a52-3603c2319c78 | -8.0507 | -43.1472 | 2025-11-29 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 6219b1ec-9821-344d-be89-e34cbff9caf6 | -2.7845 | -47.4343 | 2025-11-29 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| a13fa434-4700-36e6-b3a8-c41d67089a07 | -2.6322 | -48.542 | 2025-11-29 01:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 6622b827-4aba-3be9-9e2f-7e4e74c29918 | -8.1633 | -43.2055 | 2025-11-29 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 145ebd50-de24-3b62-9bab-9e309700a6fa | -1.4737 | -45.7907 | 2025-11-29 01:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 67f292ba-2efe-3cef-a665-add5f6e475ce | -8.6789 | -44.2211 | 2025-11-29 01:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 0643653d-c2d3-3a3a-936e-b92519e5ffae | -2.803 | -47.4337 | 2025-11-29 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3ac78a2b-ec43-31e0-83f6-b942571c8318 | -20.4283 | -57.9341 | 2025-11-29 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 2f54b420-739b-3561-9ae1-3214b6b1f7d1 | -8.051 | -43.1237 | 2025-11-29 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 158.5 |
| 8a689f9c-0239-332f-b90e-cd7db6a38d6d | -1.4923 | -45.7903 | 2025-11-29 01:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d0fd6704-16d6-3c4c-8d0e-36b544d7f3d5 | -20.1813 | -52.3754 | 2025-11-29 01:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 107164bf-ab85-3f72-834a-ac3c6e062ef3 | -2.6341 | -48.0249 | 2025-11-29 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 744cd5f0-6839-3a35-a8b4-2ad0493b0a09 | -20.2016 | -52.3717 | 2025-11-29 01:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e68a1966-7f47-3bf1-8935-b049c665a60e | -8.1822 | -43.2034 | 2025-11-29 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 78f61a53-5cdd-3b1f-b90e-4f85210eb52b | -3.8998 | -40.7727 | 2025-11-29 01:40:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 23bb8bf4-e238-30e8-ac6a-8b08b2e98faa | -20.2256 | -47.5285 | 2025-11-29 01:40:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 296b0efe-a366-39b2-b8e8-81d0b475e27a | -8.0321 | -43.1257 | 2025-11-29 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 230.1 |
| 29914621-76a9-3f76-9177-a83a6d9f9591 | -20.4496 | -47.523 | 2025-11-29 01:40:00 | GOES-19 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 51.6 |


[Clique aqui para ver as próximas entradas](README9.md)

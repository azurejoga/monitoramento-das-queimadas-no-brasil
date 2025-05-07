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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba128ea5-4ccb-3c2a-a937-d995dea770d0 | -16.0443 | -43.8059 | 2025-05-07 00:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0329a6b8-eee4-32e1-a491-72c27ff96928 | -11.3963 | -52.9477 | 2025-05-07 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a9f01f48-fce0-3ccb-bfea-8ad26b80a42c | -11.3963 | -52.9477 | 2025-05-07 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 97fe0948-5d88-3e68-bffb-44a0b7783948 | -11.3963 | -52.9477 | 2025-05-07 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 713e0da2-4c27-3f75-9097-c8334a30dbc6 | -11.779 | -48.695 | 2025-05-07 00:34:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cb2a9c9-8fee-3709-99da-19ff9468b235 | -10.7163 | -42.326099 | 2025-05-07 00:34:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bf4ac195-b3f9-3731-b758-92886e0c2dd5 | -11.4038 | -52.933998 | 2025-05-07 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b27a56cd-168d-3158-ad1c-3bbbec5f25dd | -12.1798 | -54.234901 | 2025-05-07 00:34:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31d83150-63ea-3c95-9c41-b2330351cb88 | -6.5577 | -44.491299 | 2025-05-07 00:34:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98200c60-d8d9-32d1-8379-9f11c80d38cc | -13.5056 | -52.952599 | 2025-05-07 00:34:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ef5db1a-87bb-3e4f-b6eb-9427c46b61d4 | -13.0515 | -53.704399 | 2025-05-07 00:34:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e29171c-0ac1-3d9f-966f-4bbfd44e57b1 | -11.3924 | -52.929199 | 2025-05-07 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df125d74-e4a5-3932-9392-35f2adcfdbc7 | -18.2943 | -52.9865 | 2025-05-07 00:34:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 87e2bc78-2576-3e17-a7f7-2573e70dfa2d | -13.5072 | -52.959801 | 2025-05-07 00:34:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f83da714-8472-305f-b827-6a9fd28b806c | -16.048901 | -43.805099 | 2025-05-07 00:34:00 | METOP-B | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 628a5fd7-4857-303f-9692-851351279fc4 | -10.5122 | -46.979099 | 2025-05-07 00:34:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 784c1bf1-72c5-389e-addc-e1bca13ab70b | -13.0547 | -53.719299 | 2025-05-07 00:34:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 531f44e8-d92e-388c-8b4e-408f47522504 | -11.4054 | -52.941002 | 2025-05-07 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e477ef66-8a99-3c07-b386-ff11a908f8a3 | -9.2782 | -47.900101 | 2025-05-07 00:34:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4876702b-d186-32de-9382-24de738a0a9d | -12.8351 | -47.402 | 2025-05-07 00:34:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8358ee1f-b9ab-315c-b71f-561edc353355 | -11.2808 | -52.471001 | 2025-05-07 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca75b0b-165b-3295-b31e-947467ec2568 | -11.3955 | -52.943199 | 2025-05-07 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb19376c-238b-37d2-92f7-39e2798c5832 | -18.2911 | -52.970699 | 2025-05-07 00:34:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1381f6f7-0c79-3a45-90e9-aa57266835f8 | -17.152 | -54.0042 | 2025-05-07 00:34:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b244136-254b-3163-b25f-d05c78b209bc | -16.045 | -43.7901 | 2025-05-07 00:34:00 | METOP-B | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a0dbd7f9-b2d2-3fca-bf51-da2547af8049 | -18.425501 | -54.7024 | 2025-05-07 00:34:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| edd40d23-e464-37d1-b671-d185e7af41de | -14.6975 | -53.386101 | 2025-05-07 00:34:00 | METOP-B | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20dc6534-a3ff-33dd-9ebb-92da6ffad993 | -13.0563 | -53.7267 | 2025-05-07 00:34:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63b58f20-9480-33e0-aee6-b319000bb208 | -12.3738 | -52.479698 | 2025-05-07 00:34:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18d9110e-747a-387f-936e-bd57b58774cd | -11.3939 | -52.936199 | 2025-05-07 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55b2c0d6-f3a8-3247-82c4-54c24c707696 | -18.4237 | -54.693001 | 2025-05-07 00:34:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fbe5e863-8a40-35a8-804e-cc1b467e1a73 | -12.1782 | -54.227299 | 2025-05-07 00:34:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9055d703-c219-3390-9415-f0bf94db38e3 | -12.8375 | -47.411999 | 2025-05-07 00:34:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a0c4745-78a8-39d9-bb4e-2f3c9480fd05 | -18.2927 | -52.9786 | 2025-05-07 00:34:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9475c735-72bd-3335-b233-70a28400475d | -18.2959 | -52.9944 | 2025-05-07 00:34:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5ecb15af-c9e0-3b82-b768-29af57773fb3 | -11.2793 | -52.464001 | 2025-05-07 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff18e369-8d13-3f14-8fc8-b8dc5fd70fe8 | -6.709 | -42.137501 | 2025-05-07 00:34:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 34a8e5dd-96ea-3099-858c-eb953c545c43 | -8.2452 | -49.735199 | 2025-05-07 00:34:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84202bac-019c-3a33-a4b4-cdab23f057b3 | -10.7259 | -42.323502 | 2025-05-07 00:34:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e09e755d-485c-3a3a-a35d-20840529ec9f | -13.0531 | -53.711899 | 2025-05-07 00:34:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85eba412-1178-35ce-a278-a3e4addb1313 | -11.397 | -52.950199 | 2025-05-07 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13f5b654-1dd9-3641-bb10-0ed79da301a0 | -6.6994 | -42.139999 | 2025-05-07 00:34:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 65fcf9af-96a6-3c9f-b3db-3ca45b911654 | -11.4023 | -52.926998 | 2025-05-07 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4d6a8b2-87be-376d-8ef7-73f795ccb3f7 | -17.150299 | -53.9958 | 2025-05-07 00:34:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4013793c-0d72-3a9d-a3a8-042bba95dd8a | -14.6991 | -53.3936 | 2025-05-07 00:34:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3932420-4439-3461-bd65-a739185b480b | -16.652599 | -55.7384 | 2025-05-07 00:34:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dfec6459-6d36-3480-a4f6-3721f865b75a | -11.7811 | -48.703701 | 2025-05-07 00:34:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7001fddf-80fc-377b-b8e7-8ebad694be2c | -23.6129 | -48.990799 | 2025-05-07 00:37:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1f6fa203-407e-32df-a4e2-875335e92222 | -23.617701 | -49.013302 | 2025-05-07 00:37:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1586eea2-2707-358f-9294-8f476dc007f3 | -23.6161 | -49.005798 | 2025-05-07 00:37:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0f017cc8-9b08-35da-b4de-64dbda19e67c | -21.3906 | -48.6362 | 2025-05-07 00:37:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4f28274b-3006-37d1-8b39-03658bf4dd6b | -22.8132 | -47.124199 | 2025-05-07 00:37:00 | METOP-B | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5bc65430-e139-3a5a-ac2c-e64bce30e1f3 | -21.062401 | -49.9538 | 2025-05-07 00:37:00 | METOP-B | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7afaf67b-5cb5-3335-96e9-b988f2c03638 | -21.2246 | -48.678501 | 2025-05-07 00:37:00 | METOP-B | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4115ad73-1dcb-3f47-aadf-7c1925812189 | -20.572201 | -54.056099 | 2025-05-07 00:37:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0f62f380-709a-3633-a4fe-0fa5047802dc | -21.388901 | -48.6287 | 2025-05-07 00:37:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a8b33a3c-652c-33aa-bc53-1f8a69e1ee2d | -20.0676 | -49.363201 | 2025-05-07 00:37:00 | METOP-B | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e632eaea-e735-3202-88a8-e81e1d17d3b1 | -22.8151 | -47.132401 | 2025-05-07 00:37:00 | METOP-B | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ce97129-a599-3a1a-a25b-8be447e9dee1 | -20.0693 | -49.370602 | 2025-05-07 00:37:00 | METOP-B | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a24b7e64-044d-3c80-89fa-2d36044e808b | -21.0609 | -49.946499 | 2025-05-07 00:37:00 | METOP-B | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16552338-53ab-3a3e-861d-190317c42d63 | -23.6145 | -48.998299 | 2025-05-07 00:37:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 52d5070a-c9a1-3e43-ae95-3daae522e27f | -11.3963 | -52.9477 | 2025-05-07 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1a58dc4d-5811-3f07-96a0-a3e2b67e1514 | -11.3963 | -52.9477 | 2025-05-07 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 76c1dd96-3871-3dbd-97d1-d3fc358662b3 | -11.3963 | -52.9477 | 2025-05-07 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 669fe2f7-b33e-3639-9ccd-289e064c9c65 | -18.41413 | -54.71236 | 2025-05-07 01:09:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8720c299-aa99-350b-97e4-1c24d11dcf47 | -20.05442 | -49.37151 | 2025-05-07 01:09:00 | TERRA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 5a9a5adc-ba7a-3baa-a6b0-3de1b79404e4 | -20.56189 | -54.0643 | 2025-05-07 01:09:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5ddbe35-b65c-303b-bfa6-622cff5e933c | -20.56317 | -54.07386 | 2025-05-07 01:09:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d6669596-5d60-3387-90be-fe381534fda9 | -23.60996 | -49.01606 | 2025-05-07 01:09:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 24c6dd57-9f3a-3b0e-81a4-deb19ffc530a | -18.28671 | -52.99061 | 2025-05-07 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 511a9705-653a-314b-ba10-d4a5b3e5170f | -22.80896 | -47.12819 | 2025-05-07 01:09:00 | TERRA_M-M | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 4cafa00f-c860-3858-806e-5b15f894f074 | -20.71823 | -54.40987 | 2025-05-07 01:09:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8d96e78f-bc05-3f8a-82ee-4abb4789fce3 | -23.60799 | -49.0038 | 2025-05-07 01:09:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ed60eeb4-da45-3d59-a3c5-6249a7625089 | -16.65771 | -55.74973 | 2025-05-07 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 539e8b7c-94ac-33ae-966c-d6b4c3a49520 | -18.28537 | -52.98124 | 2025-05-07 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1e10376f-3ff4-37f6-a29b-9a53c9298345 | -17.14844 | -54.00272 | 2025-05-07 01:09:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bf707221-3a2d-33e2-a5fa-70387fafffbe | -17.14971 | -54.01192 | 2025-05-07 01:09:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9df18e48-3654-308d-a028-c66f9cf68a7b | -21.06153 | -49.96096 | 2025-05-07 01:09:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| ccbf9c93-2b1e-34b4-af53-59650a515027 | -18.4231 | -54.71098 | 2025-05-07 01:09:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 31bff5f2-07dd-38bd-981e-2dfc1fc0c6b4 | -21.04666 | -55.9987 | 2025-05-07 01:09:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c44604ba-5345-3880-a5b0-ac4a12cd04f1 | -19.7662 | -48.0041 | 2025-05-07 01:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ec58fce9-13b6-3a51-a95e-02eff137499d | -11.3963 | -52.9477 | 2025-05-07 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b081fca6-257e-3410-9512-493f7288ceab | -19.7459 | -48.0086 | 2025-05-07 01:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 117.9 |
| adce9e1c-c0b2-3c8a-985c-8b591ce56a76 | -18.284 | -52.9848 | 2025-05-07 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| edcc4d26-abe0-310b-945a-04e39c94253d | -12.17932 | -54.23787 | 2025-05-07 01:11:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3620207-f850-3963-9b43-f6573b45cdc9 | -13.50792 | -52.96215 | 2025-05-07 01:11:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f70523d1-3606-3ab8-9a31-865e4a0d5760 | -14.68503 | -53.39106 | 2025-05-07 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 45855039-d94f-3328-9ba6-de46b5d0d04b | -11.27657 | -52.4736 | 2025-05-07 01:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6007097c-2d92-3536-b3ed-85f2f11033fd | -13.05515 | -53.72344 | 2025-05-07 01:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f9699108-bd27-38f5-8d57-80c49b5d2aaf | -11.77833 | -48.7114 | 2025-05-07 01:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 99faec3a-431f-35db-b3c7-7443bb379e0c | -11.77519 | -48.69807 | 2025-05-07 01:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ffdd17ef-2549-3122-9ddb-cb03416ffda2 | -13.05381 | -53.71412 | 2025-05-07 01:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| de3d82ba-d5ec-30cd-aee8-242244253c68 | -13.04751 | -53.73418 | 2025-05-07 01:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a5338966-7349-323f-88d5-45ed429217b1 | -12.17041 | -54.23922 | 2025-05-07 01:11:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b432171a-bf13-39f9-ae5e-c1a7f28dadd9 | -11.39546 | -52.95026 | 2025-05-07 01:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 27bbf01a-2aeb-3dd5-a008-e293983a1c0a | -14.69533 | -53.39902 | 2025-05-07 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 725a9e51-ae66-3520-8573-f3e975e439f3 | -11.80558 | -57.36688 | 2025-05-07 01:11:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3515a5ce-02d9-35f4-be26-78b86724c145 | -11.25724 | -52.47659 | 2025-05-07 01:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 24f282c8-318a-336b-b4a5-d3fcca91d295 | -11.38457 | -52.94149 | 2025-05-07 01:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b22f4e2e-48fb-37ee-a51a-88223e6183e3 | -13.49873 | -52.96357 | 2025-05-07 01:11:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README2.md)

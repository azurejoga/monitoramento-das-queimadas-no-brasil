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
| fe27c235-2a19-3ca5-9a26-f2d3b4f95246 | -4.2931 | -48.23973 | 2025-11-14 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b6f7ed87-eeca-3ac9-a91d-ea857c0a15e2 | -7.92935 | -44.34459 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 01da73e3-cea5-33fe-8066-8d0854ec19b7 | -2.9557 | -45.7588 | 2025-11-14 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8a854036-c723-36cb-9ddc-fc48f53eb194 | -5.74288 | -49.32109 | 2025-11-14 00:34:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 61aded85-3ace-32e8-8058-da2e8fcb760e | -4.22131 | -49.11419 | 2025-11-14 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 895f1573-a5ee-354a-9f86-6e9f4a84e837 | -2.87256 | -51.47783 | 2025-11-14 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c9c946e5-253b-3045-b1ba-b4d78db57650 | -4.1107 | -48.01598 | 2025-11-14 00:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4d3b598f-06fc-3087-ac26-2abe28e876ff | -8.90357 | -47.89375 | 2025-11-14 00:34:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0311e8ea-a3d7-35b2-b6c7-8bec5f0a87ed | -4.71307 | -46.45261 | 2025-11-14 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 113.4 |
| f8453d68-d028-33a6-80a4-f48a7989639a | -2.88789 | -45.29557 | 2025-11-14 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 2001a957-b956-3136-9bba-7edae5c656e6 | -7.06357 | -48.36232 | 2025-11-14 00:34:00 | TERRA_M-M | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 12a7738f-e81d-3301-977e-660c1bc6b2fd | -4.32964 | -49.03826 | 2025-11-14 00:34:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0578e44a-74e8-355b-b201-090485c1eb9b | -1.93187 | -54.5178 | 2025-11-14 00:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ccb8819b-3178-3e7f-ac71-9496626d2dea | -5.59458 | -45.17249 | 2025-11-14 00:34:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 627c447f-cc8c-3c61-a267-53c0baf4cb64 | -4.11331 | -50.05449 | 2025-11-14 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fcca8b7f-3ac4-3201-b485-9144eed28655 | -3.65865 | -45.92807 | 2025-11-14 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 99e47bb1-3385-3159-a477-4da9d6f4c750 | -3.72071 | -54.45483 | 2025-11-14 00:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 89d54598-796e-3d0e-832e-d11ceef7d68f | -2.63671 | -45.76511 | 2025-11-14 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f69c8517-7d53-3769-ba7d-6ceedf3df810 | -2.88535 | -45.27824 | 2025-11-14 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 96e1ca92-07d4-3d75-a337-0634c1386403 | -2.79427 | -45.49532 | 2025-11-14 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| fdc0eacc-b152-3228-aa50-1a0884e5769c | -5.46365 | -47.10793 | 2025-11-14 00:34:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 464a11fc-b45c-37c4-9e3f-8f061790ccee | -7.84224 | -44.29528 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 5d61fc40-43ae-3834-9ce6-e2c04a851e75 | -3.98384 | -48.00242 | 2025-11-14 00:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| e9f9d075-66a3-3a08-b4b0-9b7ecd755696 | -3.48109 | -45.66126 | 2025-11-14 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e40b86f6-81d4-3936-881e-7135cead7ca2 | -2.11992 | -45.35669 | 2025-11-14 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 792988cd-39a8-3b63-a3df-60bfc79d59ba | -6.68827 | -47.79905 | 2025-11-14 00:34:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5d4d45ab-baae-3bd5-8ce7-f49bdc68cb87 | -7.93872 | -44.32586 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| de18d2eb-0aae-3eb9-8ac6-713848ce997b | -7.84982 | -44.30498 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 226.3 |
| 5de86813-163d-31a7-82e9-49589ef9822f | -0.86951 | -47.31209 | 2025-11-14 00:34:00 | TERRA_M-M | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 7501a13d-02f9-3f1c-948f-030f097f15f8 | -2.63444 | -45.74906 | 2025-11-14 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 62aa5f24-fa87-3dae-b4be-2811f32432db | -2.51548 | -47.80822 | 2025-11-14 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 032820ac-3b33-3e6b-a591-3611d832d7d2 | -8.65531 | -47.38219 | 2025-11-14 00:34:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c4616ab6-f8da-36b3-8250-d07a848b0a5f | -7.66764 | -45.88642 | 2025-11-14 00:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6bdfbfa7-d82a-320c-9e4b-9c219d8d3110 | -2.47327 | -48.22942 | 2025-11-14 00:34:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2cae1944-9898-3fa2-b8d0-52d90c75625a | -7.92679 | -44.32774 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 56247ab2-0236-31d4-9578-25f8907f08d8 | -3.82244 | -44.25062 | 2025-11-14 00:34:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3d38d4b0-306c-347c-b4db-f6381ffdd11b | -3.85093 | -52.29807 | 2025-11-14 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4160eb36-5af6-3487-963d-bec66328f7b3 | -3.32495 | -52.08629 | 2025-11-14 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c57c0886-5e6a-3d0c-a825-0f198cd65235 | -3.76454 | -47.73921 | 2025-11-14 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b4839192-1486-3634-8a4f-0a20361304a5 | -3.46012 | -50.59259 | 2025-11-14 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4333192-f3df-3e88-ae6d-37d02742abc3 | -4.75882 | -44.45909 | 2025-11-14 00:34:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8b3ce126-1622-35cb-af51-1d2695ca050b | -3.72236 | -54.46707 | 2025-11-14 00:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c6ea8822-b4ae-3658-93a2-e2ce2eea56aa | -4.64056 | -48.7514 | 2025-11-14 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c45ec120-e58b-357d-b84d-0af53966a258 | -3.36598 | -48.40223 | 2025-11-14 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| db8e28cc-12a1-3fae-b29a-b66837db53b4 | -2.33783 | -55.68979 | 2025-11-14 00:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 40788b79-1348-34f2-bddc-ed239fae1903 | -5.86122 | -47.5835 | 2025-11-14 00:34:00 | TERRA_M-M | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1e88ef4c-8a54-3bae-9ae9-efdd2f9e5ece | -3.63064 | -49.10968 | 2025-11-14 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e5e8bb59-515e-393a-a242-7594e81a8651 | -2.38276 | -48.68359 | 2025-11-14 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| da5af2cb-3a06-3915-92c9-4609dfde56fa | -6.88755 | -42.8479 | 2025-11-14 00:34:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| bd9eed51-982b-3642-a0c4-868083a05808 | -7.84712 | -44.28792 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 274.0 |
| 09f14460-1912-3f56-888c-167b4a61af3b | -3.30916 | -50.10501 | 2025-11-14 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 403f5fc7-a825-3ab8-8884-187ab12bd3d6 | -3.99205 | -47.19164 | 2025-11-14 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a1ad840f-460b-3ab0-82b7-c34f87c542b9 | -5.3532 | -46.76366 | 2025-11-14 00:34:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ee696048-8c88-33ae-af60-0619632eeb23 | -1.11065 | -52.59388 | 2025-11-14 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 85264ab5-dc78-3f78-91fa-5e0e70e15c46 | -2.94765 | -49.36203 | 2025-11-14 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 714338e8-dae5-303a-b46a-753e93f6531d | -4.53171 | -46.39634 | 2025-11-14 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3201bcf4-11ac-3fe5-9de6-53fe6d4691b2 | -3.12618 | -52.24801 | 2025-11-14 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d7ffdac-c03e-34bb-b733-809644978f11 | -3.16128 | -50.62619 | 2025-11-14 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3b652d3a-d0c8-3b95-aff1-59d3db314a5d | -6.44867 | -45.66506 | 2025-11-14 00:34:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| de71497a-4ac0-3326-9cd3-2479c38aaf18 | -3.52503 | -52.80294 | 2025-11-14 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c3dea65-5b4b-308f-8820-0fe44cd58c9e | -4.10104 | -48.01735 | 2025-11-14 00:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 071ac2ec-acc0-32fd-906b-043b004c672b | -1.83142 | -53.79928 | 2025-11-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| fe2bbc8f-e371-3cd7-aa07-aa1551f87dc2 | -4.5356 | -46.42305 | 2025-11-14 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 71deadd4-87fa-393a-a804-6f8503692b70 | -2.79303 | -52.97342 | 2025-11-14 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 549086f7-9eb8-3b9f-869f-61112ac7ec6f | -6.15347 | -48.05923 | 2025-11-14 00:34:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef6ce48b-7662-3b18-83dc-90ed4bd5aa39 | -4.53364 | -46.4096 | 2025-11-14 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e328d16e-93b0-33bb-af53-25513424ae4f | -6.16145 | -48.04791 | 2025-11-14 00:34:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 8e3d7c5a-11bb-34f9-b336-0af8bae4fcb5 | -3.32369 | -52.07715 | 2025-11-14 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff5a2e91-0dbd-3bd7-86ee-59208e2ddaa4 | -4.71113 | -46.43942 | 2025-11-14 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 3c0a1940-b171-34e5-bcc6-945630fd30a3 | -3.90902 | -50.04107 | 2025-11-14 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b2ba8b40-4277-38d0-8a85-4e4c45f8a643 | -3.63896 | -44.34518 | 2025-11-14 00:34:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 63dcc599-f7ee-3dc0-a103-fb959502fea8 | -7.8591 | -44.28605 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| bc435dc2-561b-34b4-a40b-f21d9432f5f1 | -6.47529 | -48.37682 | 2025-11-14 00:34:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ef4a0e90-e7d9-3bd3-8dd0-91666d9dabe0 | -4.45376 | -43.91672 | 2025-11-14 00:34:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6f2cec64-d291-38d2-a786-d76707140e78 | -3.95359 | -47.4912 | 2025-11-14 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f4f54154-fe61-39da-b47c-a84229d13d46 | -3.344 | -48.38428 | 2025-11-14 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 064dadb1-e460-30cf-96b5-bfa3ea630437 | -3.7629 | -46.01253 | 2025-11-14 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 43336e95-8c2c-310c-aff7-a4cfc8f29cd1 | -5.36759 | -46.2994 | 2025-11-14 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 8f3ad70d-dc14-38ff-832d-9d75159c0eb0 | -6.40706 | -39.76448 | 2025-11-14 00:34:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 33.0 |
| 2a4c3a0d-0fdc-3eba-9b86-4aaf2f8e2289 | -6.0952 | -47.92261 | 2025-11-14 00:34:00 | TERRA_M-M | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fd9c6ace-9853-39d5-b7bb-c98fd91a64e7 | -5.75309 | -49.26382 | 2025-11-14 00:34:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a9693864-2690-3aeb-9fa6-586c667d69c7 | -8.9453 | -49.82149 | 2025-11-14 00:34:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fad57695-149a-3385-9017-1d313292dc8f | -3.77279 | -47.72657 | 2025-11-14 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a66a2e85-d623-3c09-b9cf-3790094df54a | -3.76398 | -47.74559 | 2025-11-14 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 47a66bd3-5ccf-3bd7-9c04-cf8ef4fc875c | -2.80618 | -45.49359 | 2025-11-14 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ccdc8b2d-754c-3f35-b822-71f0b0ee74d2 | -7.02326 | -46.43636 | 2025-11-14 00:34:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 282d50a3-f23e-399a-a3de-bbee24469523 | -4.21219 | -49.11549 | 2025-11-14 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 826e947c-4910-3d0e-823a-2e0903c25adf | -2.52548 | -47.80674 | 2025-11-14 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 6bc11480-7984-3e27-870f-20b1f2c829f9 | -4.77711 | -48.68013 | 2025-11-14 00:34:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2a54b47c-159f-373b-b98d-d898f4c6e4db | -2.28296 | -53.63612 | 2025-11-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 64ce9067-22a1-3a2d-9a00-79fa57d69454 | -3.53336 | -51.31862 | 2025-11-14 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 03cb7784-fede-32df-a228-15181313bd96 | -2.62793 | -47.30705 | 2025-11-14 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d4c04deb-a92e-31f4-a021-9dc6242edeea | -7.66568 | -45.87339 | 2025-11-14 00:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f20dd74b-2d95-3215-aea9-f032b59e638f | -3.35507 | -46.86888 | 2025-11-14 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 88654ea4-7f9a-3fbd-8e6f-38c063607771 | -6.15204 | -48.04924 | 2025-11-14 00:34:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 107ff111-2f47-381b-8e68-cc840e675bab | -6.42377 | -47.30809 | 2025-11-14 00:34:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 15fbf830-ca0c-3557-94f8-3a9be6ee7f3f | -5.06422 | -49.87667 | 2025-11-14 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7114f020-52f4-3f9b-a51f-ab30db1a9335 | -3.44416 | -44.53426 | 2025-11-14 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 50c27ccf-9e33-3901-ba52-dfc95262ab37 | -5.48688 | -47.70141 | 2025-11-14 00:34:00 | TERRA_M-M | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cd0e295a-3c46-3358-a9b7-fa0c047fdf9e | -3.0125 | -49.43322 | 2025-11-14 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |


[Clique aqui para ver as próximas entradas](README5.md)

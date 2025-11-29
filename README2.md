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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22191786-2e2f-35a4-b1a6-f1cafa879483 | -2.7845 | -47.4125 | 2025-11-29 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a10e2b71-6aee-374e-a04e-a9a9092888e3 | -20.180401 | -52.353199 | 2025-11-29 00:24:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0ff40d2c-e2e5-37b0-9588-34df54897e79 | -8.673 | -44.219501 | 2025-11-29 00:24:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0af5972-b7e2-3e5a-ab01-5a6636c5ae2c | -7.4532 | -44.748501 | 2025-11-29 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f6d688bb-51b0-3feb-ae5e-d5c29ad98f5d | -2.7047 | -48.3419 | 2025-11-29 00:24:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df1c3be-3247-3f11-bd0b-37bd40432c48 | -2.7739 | -45.482899 | 2025-11-29 00:24:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 174a0f35-1706-3298-b2aa-3e1a8c2bf0d8 | -6.2079 | -43.2822 | 2025-11-29 00:24:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a29b555f-365f-3ab0-aa0b-99eeb36baf14 | -6.5326 | -38.861301 | 2025-11-29 00:24:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6e7b3f10-45f1-35ac-aefb-5d908b24fbaf | -4.3751 | -43.744999 | 2025-11-29 00:24:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58135bff-9bd5-34a4-b82d-a9bf6dc7f091 | -8.6714 | -44.212601 | 2025-11-29 00:24:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a1c497d0-462a-3123-a63c-846b6732007f | -9.321 | -43.087799 | 2025-11-29 00:24:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a6fa7f4e-a297-3929-b411-46b66602ec89 | -20.442301 | -47.5131 | 2025-11-29 00:24:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 613c8476-6bda-3a03-ae3e-a612b629577d | -20.9685 | -48.618801 | 2025-11-29 00:24:00 | METOP-C | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff045ef2-271e-3560-b7ae-3c8dc8ce0244 | -8.1613 | -43.2052 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 12cdc752-5224-39ed-a4e9-bfaacdc3070b | -4.1156 | -44.902 | 2025-11-29 00:24:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89731d12-2ecf-3538-b13d-a5593bcc9132 | -9.8768 | -47.448399 | 2025-11-29 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d680f28-389f-3283-9884-e5281d91af93 | -4.3308 | -48.752602 | 2025-11-29 00:24:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cfe5b14-7c25-365c-9a39-40ab9c31c322 | -2.918 | -45.256901 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab1cdf0-4e80-38b6-bd02-28b1391e07f6 | -8.0482 | -43.118198 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0cf4acd4-500a-344d-b3ca-dc4182e7113e | -7.4516 | -44.741699 | 2025-11-29 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 259a6fb3-d5ca-381a-a0ad-80b07b3030f8 | -3.2395 | -47.250198 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a606534-e1c1-3c00-bbd6-ca247f42113c | -20.2155 | -47.5471 | 2025-11-29 00:24:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 78714321-a069-38cf-98ab-38932d48fbc7 | -20.165001 | -52.381302 | 2025-11-29 00:24:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6df30415-a82c-3bad-80e0-7eb3fd3a3438 | -3.3421 | -39.990799 | 2025-11-29 00:24:00 | METOP-C | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ee28462e-7785-3fe8-81f6-6df63fe04a1d | -3.5943 | -47.269699 | 2025-11-29 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbb204f9-11c3-33c8-ba60-e7581037c776 | -6.3349 | -39.237701 | 2025-11-29 00:24:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 06e8164b-8326-36e8-ba90-34a750c2bf23 | -3.7631 | -46.969601 | 2025-11-29 00:24:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0b8030-f24d-3c94-9225-64a2bf0a835e | -17.611601 | -46.6605 | 2025-11-29 00:24:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9613bc80-58de-3dc6-bb00-e5f77af91d56 | -2.2274 | -47.512199 | 2025-11-29 00:24:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df492f1e-08e8-30b3-93bb-be5bb178da67 | -2.9719 | -45.581799 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3c147f0-1df7-35de-b44f-f324da077fa0 | -17.601801 | -46.662601 | 2025-11-29 00:24:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5115d06a-78fa-3f24-89f1-81c65969ae90 | -9.959 | -42.322201 | 2025-11-29 00:24:00 | METOP-C | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4f53c2cd-a4da-3f11-8027-d06dcc3bc634 | -22.0758 | -46.809101 | 2025-11-29 00:24:00 | METOP-C | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d787928d-b823-3451-aa15-1f14f048db4e | -2.929 | -45.304798 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9e74c3-ccb8-322e-9936-4ac7e8703df2 | -2.9817 | -45.579601 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c34faf13-46dc-3e8e-b0b6-4b5a7d83cb46 | -3.4578 | -47.621201 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5d16135-0d01-3b00-aa8e-c128d3ef73fd | -2.9259 | -45.2911 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba4d64d3-fc35-373c-b0ec-e5b72d956f6e | -4.0403 | -48.878101 | 2025-11-29 00:24:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f4bbfa2-f1e9-382b-ad5c-87ff41298654 | -3.4611 | -47.636002 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93b9b205-c840-31c9-8ae5-3fb7f325496d | -8.1727 | -43.210098 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6cf575a1-9bf8-3b3b-985c-3054bbd29fa5 | -2.9165 | -45.250099 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce65c9cb-3877-3f8b-85fa-40d9ae7bf70c | -20.739799 | -47.2062 | 2025-11-29 00:24:00 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aeda6b9f-354e-3eb2-9d34-312082b641fb | -4.5457 | -44.126099 | 2025-11-29 00:24:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 846b6bee-2a46-3868-8c53-6d699c3d4c48 | -3.7615 | -46.962502 | 2025-11-29 00:24:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 627b7029-a491-39ff-bb29-1df0af164ff8 | -8.1629 | -43.212399 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ac9d5655-413b-3d4f-b7b2-f463d75ad6a2 | -20.980801 | -48.631302 | 2025-11-29 00:24:00 | METOP-C | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6374951-d134-3398-b3f9-bcef56be5ae4 | -3.9427 | -47.034401 | 2025-11-29 00:24:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2b8af6-9021-3660-a11b-67f265c83e84 | -8.765 | -40.979198 | 2025-11-29 00:24:00 | METOP-C | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| fc430afc-c447-3d9c-a938-affff1463b2b | -8.1596 | -43.198101 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ce437bc-1516-3d85-b4c4-43ddbc13594c | -2.4302 | -46.368401 | 2025-11-29 00:24:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6adcbdb2-b710-34a2-805d-3cf1480d4ba9 | -2.9786 | -45.566002 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1cadd88-3ffb-36d7-a198-c44a7cec2501 | -2.9704 | -45.575001 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb3957be-393d-376e-84dd-82611d5eb1c7 | -2.721 | -45.2075 | 2025-11-29 00:24:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1594bca-1788-359e-805f-cee3146b739e | -3.5759 | -50.287601 | 2025-11-29 00:24:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e34fe3d-922c-3053-8796-f8c95df81dbd | -8.0286 | -43.1227 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3cfd6d6-da66-31c6-bcef-fa93129a2171 | -3.9808 | -49.025299 | 2025-11-29 00:24:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a28a7852-2d3c-3437-b67e-8bfe8e2af4b8 | -3.5829 | -47.264599 | 2025-11-29 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe26776f-6fd6-31bd-9959-e35b479308bc | -5.3655 | -43.032299 | 2025-11-29 00:24:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| dc1c6983-e89a-3850-aac6-ad9678175e0c | -2.9686 | -45.2528 | 2025-11-29 00:24:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a09d29a-1901-3cba-8c72-551bfadc1cab | -2.7065 | -48.349701 | 2025-11-29 00:24:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a90b34e-f410-3895-b504-97c546bdba97 | -3.7599 | -46.955399 | 2025-11-29 00:24:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a0f6fcf0-0e97-3f6b-8997-f3f31242b8ee | -3.5792 | -44.542999 | 2025-11-29 00:24:00 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aceed4c3-9f2f-3238-9c76-b03ee5d3dda7 | -5.362 | -43.0173 | 2025-11-29 00:24:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 7fb2b054-f788-30c7-9757-14ed36eb7f1d | -3.5159 | -47.196499 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 171d28e8-0f81-304c-940e-3a363384045b | -1.4999 | -47.801998 | 2025-11-29 00:24:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7901e595-d499-3f74-aad3-f2f5871797bf | -3.5616 | -47.171299 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 763c6f19-ab5b-351d-8ec7-a33927e48b94 | -4.169 | -43.745998 | 2025-11-29 00:24:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1002483-4f09-3868-8d8a-0b8abb470148 | -2.7418 | -45.253201 | 2025-11-29 00:24:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bbffdfce-1e8c-3f14-bba7-014efd92c4a3 | -4.3734 | -43.737801 | 2025-11-29 00:24:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b90665c6-136b-3a86-b104-95369c0aca59 | -8.0368 | -43.1134 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 095b62df-0a9b-39df-9eee-2f17cd5d75f1 | -20.2034 | -47.537201 | 2025-11-29 00:24:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c1f86cfd-d4a9-3d95-8f66-b1671ec80c0d | -4.1172 | -44.908798 | 2025-11-29 00:24:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba4ced5e-b06d-32e2-b11a-63f8bc5b8b7a | -6.7131 | -40.817001 | 2025-11-29 00:24:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e431f1cd-b231-36be-a9c6-7adb3d028ee0 | -3.6528 | -50.218498 | 2025-11-29 00:24:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3be8bb7-6a69-3a4f-81e1-ab37e9cb4052 | -8.0401 | -43.127701 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 258bae94-fba6-35ff-88ab-f8e1429d5fe6 | -5.9256 | -43.400002 | 2025-11-29 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bd1442b-8699-3020-b5dc-55cdb0aa7e67 | -2.7434 | -45.260101 | 2025-11-29 00:24:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12c166d9-49e0-3d00-b1d1-c8464a0628aa | -4.01 | -49.1096 | 2025-11-29 00:24:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 253e4b15-0b02-3fac-996c-445c276de220 | -3.8447 | -44.128399 | 2025-11-29 00:24:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b4ed2ac-f657-31e9-89f5-d42598654a30 | -20.2057 | -47.549198 | 2025-11-29 00:24:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3bd76285-d446-3088-9daa-a995c0c712c8 | -2.8441 | -45.7892 | 2025-11-29 00:24:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 727e79cd-bbda-346c-8467-c8cbedf206c8 | -6.3252 | -39.240002 | 2025-11-29 00:24:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5decb7a4-7546-3169-bd9e-bf375dacd9fd | -3.4595 | -47.628601 | 2025-11-29 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab2c9f33-96d6-3af5-a962-734c0cb3490c | -3.5175 | -47.203602 | 2025-11-29 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffb7ab8e-616e-3355-be51-6217a7dd2f69 | -20.7474 | -47.192501 | 2025-11-29 00:24:00 | METOP-C | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9a551317-7d6e-3795-aa8c-76e7ff838667 | -5.0739 | -40.8218 | 2025-11-29 00:24:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e3c9fd92-cf6a-38ab-92b0-e876c6ab7579 | -3.1756 | -45.615002 | 2025-11-29 00:24:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35d13248-9849-3b3d-a298-b21818c9bcb4 | -3.8851 | -40.763901 | 2025-11-29 00:24:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| dbc1296e-2597-3bf6-a8f6-f4988001342e | -3.5967 | -40.851799 | 2025-11-29 00:24:00 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bb5f433a-2898-3cda-af02-da7243acf0dd | -20.2012 | -47.525299 | 2025-11-29 00:24:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f8bff003-89e8-3ecf-8e2e-39d5294aadd5 | -3.6687 | -50.655998 | 2025-11-29 00:24:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da11db66-64f8-3493-868f-cd23616cae30 | -20.211 | -47.523201 | 2025-11-29 00:24:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a2e32fcc-5f59-3220-9b59-8dbf845d3b40 | -1.4885 | -47.797001 | 2025-11-29 00:24:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 286ca77b-9e22-3c68-8643-a39b176fd8c9 | -8.0303 | -43.129902 | 2025-11-29 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d23db92-1eec-3586-8155-32a5933f5cd6 | -6.2062 | -43.274899 | 2025-11-29 00:24:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abd897a1-aae5-3206-96ab-6cf8e770c9ec | -3.8827 | -40.753799 | 2025-11-29 00:24:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 313e9f80-b6ac-3641-957a-a00e4f5fd39e | -20.160999 | -52.356499 | 2025-11-29 00:24:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f4d23a41-b8e1-3f9c-acee-eec5c0094b24 | -17.6096 | -46.650799 | 2025-11-29 00:24:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ffdcab35-5dfb-31bb-b2ab-56e16e7bfe0b | -3.5845 | -47.271801 | 2025-11-29 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 471d4f6a-895d-34fb-b905-66317cf5469b | -4.5441 | -44.119099 | 2025-11-29 00:24:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)

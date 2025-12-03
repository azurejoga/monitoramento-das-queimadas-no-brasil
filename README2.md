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
| 63084d8c-11ea-3dca-8164-8ebf103f54e4 | -2.6266 | -45.1336 | 2025-12-03 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 339.3 |
| 8bb1d6a7-bd0c-3c2a-9ff9-597f693d7492 | -11.2702 | -52.4605 | 2025-12-03 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a44ed6d9-8825-3d04-9cc9-d7b912d77321 | -11.1379 | -53.9429 | 2025-12-03 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 786633db-4c3a-3971-b24e-b2d2662c0bf8 | -8.0513 | -43.1001 | 2025-12-03 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| faedf38d-d8b2-39b3-ad55-d0bb7607ef5a | -1.4923 | -45.768 | 2025-12-03 00:30:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 010b46c7-a2f8-349b-a2d1-bf2f8d33c6fb | -3.9053 | -45.913 | 2025-12-03 00:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| cfbd9f15-770f-3c37-9de6-988007631fa9 | -2.6079 | -45.1568 | 2025-12-03 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| aa9d2d54-7551-39f0-9957-c49d8142326c | -1.4737 | -45.7907 | 2025-12-03 00:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 81a2f97b-ebc7-3eeb-be10-f347a2073d0a | -11.119 | -53.9446 | 2025-12-03 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 195a565a-fd59-39d1-9a5d-75eb6f520b91 | -11.1377 | -53.9634 | 2025-12-03 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 8443f199-929a-3772-b95a-5a5af02c47d4 | -4.346 | -49.949 | 2025-12-03 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8c1929b1-b2b6-3294-9970-9629d2079873 | -11.2702 | -52.4605 | 2025-12-03 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 54d17d05-d6ab-3a0e-a223-91a1365cfee6 | -2.9225 | -45.4611 | 2025-12-03 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 73d601e5-ca57-399f-b817-52308e1401c7 | -9.9731 | -36.0634 | 2025-12-03 00:40:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| a6ea0b7b-c007-3cfe-8120-215b5a9d9e4b | -11.1379 | -53.9429 | 2025-12-03 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2400a5a6-6d47-3607-9c0d-9197a91c8686 | -1.4737 | -45.7907 | 2025-12-03 00:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 80d0713a-f117-3f6c-8928-651713ec97a5 | -8.0321 | -43.1257 | 2025-12-03 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 17136653-c2fe-358d-9577-adc0322efdcf | -1.9167 | -54.0901 | 2025-12-03 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 9282a829-0ee4-30f8-8305-75ef9239b5e5 | -1.4738 | -45.7684 | 2025-12-03 00:40:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c6715cbe-d4ea-36d7-9fae-bbf2da25a40d | -3.2195 | -45.5398 | 2025-12-03 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 516e9c7c-86c8-379a-8a7c-aff2907c665a | -2.6266 | -45.1336 | 2025-12-03 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 288.0 |
| 6483380c-9b64-3b21-bc45-ab4deabf858d | -2.2086 | -48.0145 | 2025-12-03 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| d33b2440-eeac-3cc4-bd0e-b209b604b297 | -8.0324 | -43.1022 | 2025-12-03 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 432229e0-1af1-30cc-9330-7a58933c53e4 | -3.9053 | -45.913 | 2025-12-03 00:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f8144a1b-4811-3806-924f-f9db3b083282 | -11.119 | -53.9446 | 2025-12-03 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 50705084-fe37-36b1-840d-c2a96d02532a | -2.6265 | -45.1562 | 2025-12-03 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 205.7 |
| a04481d6-8350-329f-81de-7aa1d87a9d1f | -8.051 | -43.1237 | 2025-12-03 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 63ec9226-ed46-37ec-b08f-6662f141e365 | -2.608 | -45.1342 | 2025-12-03 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 27fc7178-c279-3324-ab1e-b0ff00b0825c | -4.4154 | -47.6085 | 2025-12-03 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| be0660f3-a6d6-3931-bfbb-407f1a2351cf | -8.0513 | -43.1001 | 2025-12-03 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 572ea79a-5bc6-3881-8cbe-0f7cbbc000c2 | -9.9538 | -36.0668 | 2025-12-03 00:40:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| f5c27115-aa95-3f4a-83b2-82b510c08461 | -1.4923 | -45.7903 | 2025-12-03 00:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| cca7e0e6-c8b9-3a92-8e9a-333c48661667 | -2.2087 | -47.9929 | 2025-12-03 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| b9f977fb-11d8-3c42-b932-b2741741ec50 | 2.8731 | -60.2563 | 2025-12-03 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 8d61ba13-d192-3536-818d-a5f7a8ff2905 | -1.4737 | -45.7907 | 2025-12-03 00:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 24249002-bb58-3b82-8579-92287bb2bcff | -2.608 | -45.1342 | 2025-12-03 00:50:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ea1bd166-4074-398d-82f6-0680ed7910f3 | -11.1379 | -53.9429 | 2025-12-03 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0fe79673-67b0-3f56-9622-7c027b603516 | -2.6266 | -45.1336 | 2025-12-03 00:50:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 6998daa4-24a8-3477-b989-bb9c44e66a43 | -11.119 | -53.9446 | 2025-12-03 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 39c35242-8f73-3d03-aeef-95566157788a | -3.4703 | -43.8009 | 2025-12-03 00:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8511cb77-9bba-3bbf-a6bb-b4f641e650d2 | -4.346 | -49.949 | 2025-12-03 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0293d92f-05b8-3c9e-b1aa-12a63fd2ce79 | -4.4154 | -47.6085 | 2025-12-03 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e6fdb589-53e7-3cd2-8473-aea6409e5367 | -4.2914 | -43.7591 | 2025-12-03 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a8f25b8c-27ba-367e-9644-4dc2dd6cd25f | -8.1075 | -43.1411 | 2025-12-03 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| ee330e6c-4c94-30f7-913e-f54c5f944455 | -3.2195 | -45.5398 | 2025-12-03 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 113.3 |
| a0be7198-2fdc-3514-bb85-2647763235f0 | -4.3892 | -43.1263 | 2025-12-03 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 29bc07cf-c14d-3944-93b8-d73e4a12b032 | -4.389 | -43.1497 | 2025-12-03 00:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f3913faf-75b7-307e-9936-31ab73f19e45 | -4.2913 | -43.7822 | 2025-12-03 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f9a23d56-cedf-3b83-a1a0-d31f3664ec13 | -3.9053 | -45.913 | 2025-12-03 00:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 2e2eafaf-be17-3f71-b450-bded9b5985cc | -2.2087 | -47.9929 | 2025-12-03 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 1f10ff3e-aa82-3cda-b127-b00d0768c0f6 | -2.9225 | -45.4611 | 2025-12-03 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 581a6778-2e76-3602-a07d-fc986e4ae361 | -2.9798 | -49.513 | 2025-12-03 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| a0b44c5e-64e8-32ac-8b6a-a51dc3bfda80 | -2.6265 | -45.1562 | 2025-12-03 00:50:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 8b37ca2f-9ba1-3e28-88e8-9317f8e03340 | -2.2086 | -48.0145 | 2025-12-03 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| db01acfc-3225-3b62-9d77-7460ba72fa5f | -1.4738 | -45.7684 | 2025-12-03 00:50:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| eec26363-ac02-3413-832d-305490412a4d | -11.1188 | -53.9652 | 2025-12-03 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7945d88a-5b5b-3cde-8f66-1f2828cd67a0 | -3.9239 | -45.9121 | 2025-12-03 01:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 112f9eeb-71e6-3d61-83cd-00e0566f9249 | -2.6265 | -45.1562 | 2025-12-03 01:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 97140770-d0ed-3ab0-845e-59d5aaa59231 | -2.2086 | -48.0145 | 2025-12-03 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| d8f20e51-7a88-3d0e-a738-1bc59f3ed63a | -2.9798 | -49.513 | 2025-12-03 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| def95387-f44c-376c-ac01-49d0dd2dd48f | -3.9053 | -45.913 | 2025-12-03 01:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| f90d524c-34d1-35c2-8ae2-d1e8a89d8b9a | -11.1379 | -53.9429 | 2025-12-03 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3a61e18d-996c-3822-9616-8f82d3eee268 | -8.1075 | -43.1411 | 2025-12-03 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 92853aa7-0a8c-3639-9da2-73654359bc73 | -1.4737 | -45.7907 | 2025-12-03 01:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| ea009205-eba6-3d65-beeb-e449db9b6c87 | -8.1072 | -43.1646 | 2025-12-03 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| bede43eb-9322-3352-9642-3e5c1097fba2 | -11.119 | -53.9446 | 2025-12-03 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| d77ad45c-1acc-31b8-a174-13a8436906e8 | -2.6266 | -45.1336 | 2025-12-03 01:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 95747cc9-5187-3902-b314-bb1c31733ea1 | -4.4154 | -47.6085 | 2025-12-03 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9f621105-6959-3310-b602-747333bf92c4 | -11.1188 | -53.9652 | 2025-12-03 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| c3063716-cbaa-3c87-914d-b53c88e8da2a | -2.2087 | -47.9929 | 2025-12-03 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 859d19d0-0e42-30e1-a047-a424d65a8757 | -8.0886 | -43.1431 | 2025-12-03 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 45152f6e-8ab6-37ed-9f66-e8b8797368c4 | -3.2195 | -45.5398 | 2025-12-03 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 90f37753-7388-3692-9630-8ba75952388e | -4.2914 | -43.7591 | 2025-12-03 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 1e9afd98-0e84-3193-bbef-68754f8d0cc2 | 1.9867 | -55.7211 | 2025-12-03 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 81a35308-e300-3465-b26d-c1d6c89157cc | -2.608 | -45.1342 | 2025-12-03 01:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 77d24215-6eae-3c5b-843b-6a77fe5223e3 | -2.9225 | -45.4611 | 2025-12-03 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 5fecc7dd-7d92-3593-8fd1-4000578e882e | -4.2913 | -43.7822 | 2025-12-03 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 41a3072d-d7d1-3b4b-a16b-3ceeaf0cc4fb | -10.1012 | -36.4182 | 2025-12-03 01:10:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 75.3 |
| e9f9b5e2-8998-3a93-9cc5-5f1237ca8b60 | -2.6265 | -45.1562 | 2025-12-03 01:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 103.4 |
| ececb574-760a-3ed4-a055-11da33fc5961 | -2.608 | -45.1342 | 2025-12-03 01:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 3a0de076-4bee-33a4-8007-a221ace7ef22 | -3.4703 | -43.8009 | 2025-12-03 01:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| aae37fbc-66d8-3612-83cd-6c3afe3bc02c | -11.119 | -53.9446 | 2025-12-03 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 9b5d62d2-f760-322e-a2d8-3418104b80e2 | -11.1188 | -53.9652 | 2025-12-03 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| abd6283f-4379-374d-a28d-f497173b4e6c | -3.9053 | -45.913 | 2025-12-03 01:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 81964ca9-21ae-3267-a16e-f58ce6a728d4 | -19.645 | -56.7891 | 2025-12-03 01:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.2 |
| efbb464c-808e-3084-9cae-894fae3db98b | -2.6266 | -45.1336 | 2025-12-03 01:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 132.6 |
| aa0bbf60-d7a8-3a46-b07e-8ad9b6e26cf7 | 1.9867 | -55.7211 | 2025-12-03 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d9349ffc-f5fa-3625-b741-f77f5f36db1d | -1.4737 | -45.7907 | 2025-12-03 01:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 89b5a6f4-3530-3d09-b37d-559495e2bb1d | -2.2086 | -48.0145 | 2025-12-03 01:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| eacc8f05-7a9d-3ae0-93c0-9a60a48cb82a | -2.2087 | -47.9929 | 2025-12-03 01:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 609f9cf9-c8fb-3f99-8855-11080db9e532 | -11.1379 | -53.9429 | 2025-12-03 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a208604e-70a7-3286-9e42-5a648824819d | -2.9225 | -45.4611 | 2025-12-03 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| f1983f28-e356-3cef-b2f2-cb2092522077 | -3.2195 | -45.5398 | 2025-12-03 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 04b04e02-7e96-3d69-a3e0-239f45c1bb1a | -19.6249 | -56.7919 | 2025-12-03 01:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| c2cd39b5-832c-3f3c-9ddf-6332e092c118 | -8.1075 | -43.1411 | 2025-12-03 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 7250ca16-d261-31f7-85bc-e8eb03f380af | -1.4737 | -45.7907 | 2025-12-03 01:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 52976c1a-597e-3d4e-8beb-09dd0a7dad20 | -3.2195 | -45.5398 | 2025-12-03 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 2201f729-0f53-38ef-a543-877c19ec576a | -8.0703 | -43.0981 | 2025-12-03 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 9bb1fc94-77bf-34c4-a753-8b1cc5081b42 | -8.0321 | -43.1257 | 2025-12-03 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 6f16892a-b221-33f3-93ba-9ddaceb72993 | 1.9867 | -55.7211 | 2025-12-03 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |


[Clique aqui para ver as próximas entradas](README3.md)

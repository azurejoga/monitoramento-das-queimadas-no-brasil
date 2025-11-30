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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe957e14-95bf-358e-96dc-e54ddd86fcd7 | -19.92829 | -57.43993 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 66f6eefc-a40f-38fa-97f6-9ac09498429a | -18.12292 | -47.15842 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 461850e3-14a8-3b7f-8102-da82e8724f66 | -17.50155 | -57.12267 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9acdde5b-00d4-3ccc-97d7-880649bff333 | -21.53389 | -49.52692 | 2025-11-30 04:27:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14ab2985-1041-30f2-a20b-5b586faffdf1 | -16.21858 | -52.18468 | 2025-11-30 04:27:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4b59f52a-f972-3bbd-8842-31f1fc7734f4 | -19.63518 | -47.66988 | 2025-11-30 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 336abb1a-af77-392d-b127-75e994e4d1b6 | -17.49152 | -57.15022 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| da004f59-ce46-3dc5-b61b-bc1f4b609999 | -17.72281 | -48.2028 | 2025-11-30 04:27:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ac700b4-45b1-32d1-a69f-768830143fe2 | -20.18687 | -52.38073 | 2025-11-30 04:27:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6360e1be-16c1-3c1e-9626-83511b57f0fe | -18.41039 | -46.84711 | 2025-11-30 04:27:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e34b6fe-3024-39d0-bbcc-5c424916b487 | -19.97957 | -47.8418 | 2025-11-30 04:27:00 | NPP-375D | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f6fcee9-5635-37e1-b7fe-b0e635a3347d | -17.51457 | -57.14805 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0015f2a3-f59e-3121-b956-b46f99ae94c8 | -19.86049 | -57.78728 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f8dbea2a-f711-3ec5-b785-cfb28cc498da | -16.79682 | -53.77127 | 2025-11-30 04:27:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df5c52d2-bfe6-3f13-92d6-7cfbd0e17c7f | -17.48691 | -57.14538 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ab85146a-80e9-3524-9282-b13c26e96391 | -23.2379 | -46.64744 | 2025-11-30 04:27:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2a4b6fca-442e-3a4e-b9f0-409dd287f4d5 | -19.92758 | -57.44332 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7ac4c441-be25-3a24-94a7-9d38660a4fc3 | -19.86584 | -57.7886 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7720f0b8-4058-3058-84ab-4a8ef0b6880b | -16.21924 | -52.18108 | 2025-11-30 04:27:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c70bc3fe-e9c9-33c4-9525-f5d7747bbd5d | -19.86277 | -57.77652 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bb4b5fef-b0d8-3057-9acf-e6390cac9fdf | -16.76656 | -51.35527 | 2025-11-30 04:27:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a79433ba-adbe-313b-8cc7-7c9085e23977 | -19.9829 | -47.84239 | 2025-11-30 04:27:00 | NPP-375D | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11bc1de0-3397-3ef7-8af3-48312fe082ea | -17.50843 | -57.15039 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 190aaf1a-5829-3e49-952a-e7d24c8efcbd | -18.41095 | -46.84345 | 2025-11-30 04:27:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5493978-b2da-339d-86c1-8afa742207d9 | -17.49229 | -57.14664 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fcee97f2-3781-3f07-8b7f-f1e35fb2e650 | -21.00416 | -49.30544 | 2025-11-30 04:27:00 | NPP-375D | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| dfdb36c2-1631-3cfb-a3bc-8dd60ed2818f | -17.08654 | -46.86608 | 2025-11-30 04:27:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d3fa960-25b4-3837-807f-9bb7a3953a72 | -17.50081 | -57.12626 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 28827583-4711-32b9-b024-2d1a7bf821d5 | -17.48006 | -57.11766 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e5874860-25a7-398c-b1b8-ae536cdd546d | -17.64584 | -50.79564 | 2025-11-30 04:27:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae449ec5-068c-303d-b240-f8d720cc4bf8 | -22.73869 | -46.59013 | 2025-11-30 04:27:00 | NPP-375D | PINHALZINHO | SÃO PAULO | Brasil | 3538204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3c1a7ce3-befb-33ea-bc0a-196ef5d23beb | -19.33476 | -54.17525 | 2025-11-30 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a35c6bc-3a3a-3280-b268-6adb7c6b9024 | -17.4969 | -57.15148 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5c1ff0fc-468c-3fc9-ad27-aed4426890a5 | -20.17923 | -52.37918 | 2025-11-30 04:27:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f94483d0-d415-3d43-be3a-fdea904e2c32 | -17.50713 | -57.15035 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0f046806-6518-3da7-903a-3fe8a5a0901d | -22.8454 | -47.21084 | 2025-11-30 04:27:00 | NPP-375D | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 50146815-f38f-391f-9154-da03a18db02a | -21.00081 | -49.30481 | 2025-11-30 04:27:00 | NPP-375D | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 41b1a264-d089-38cf-95f8-c40ae84cc9a3 | -17.48561 | -57.14528 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2b40e460-3348-3c05-ba53-2ae5f6abb9df | -17.49025 | -57.15015 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e03a0df5-1861-3843-9fe3-0cea2c27a676 | -19.92091 | -57.44886 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f4151243-3c86-3219-a070-6cd4226bdc54 | -19.83761 | -57.76276 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 59bef655-1a11-367f-8165-a93a9327bef0 | -23.88162 | -50.28616 | 2025-11-30 04:27:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5e8f1ee1-da9c-37b9-a33b-3f3fbeff458b | -18.62198 | -45.22874 | 2025-11-30 04:27:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 448b56a4-82fb-3f82-9d51-db33989909ca | -19.93352 | -57.4412 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 69d4dc58-7832-332a-afff-4dc67fe212ec | -20.18975 | -52.38655 | 2025-11-30 04:27:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37ee822f-5f91-33da-843e-22b58967c413 | -17.49563 | -57.15142 | 2025-11-30 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1bb53f30-5cc0-3750-818b-b147e6466140 | -17.85962 | -44.31028 | 2025-11-30 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e3179b4-e0bb-3213-a1d9-99543f5ad3e4 | -18.41152 | -46.83979 | 2025-11-30 04:27:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a39f0ab-0314-35a4-a994-235b1910d92b | -19.84973 | -57.79133 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e9e563ee-dea7-3f39-aace-9c85f1b93faa | -23.18086 | -45.65839 | 2025-11-30 04:27:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 894a2407-3046-3c9f-b916-c9af2b752f24 | -19.84142 | -57.77124 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 373bab0c-bfce-312b-8fec-4f963f80fbca | -23.18027 | -45.66261 | 2025-11-30 04:27:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cb21ee9f-a372-31da-ad4e-321e0bd99169 | -19.92464 | -57.44936 | 2025-11-30 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 923452e6-3408-3c99-8a1b-5c9c13e109ce | -25.23633 | -50.76515 | 2025-11-30 04:29:00 | NPP-375D | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6dbb6c48-ab31-33a3-a97f-81545f46f99c | -29.3254 | -50.72448 | 2025-11-30 04:29:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7abbbb38-0acb-34b9-8f60-de0118510d14 | -25.04195 | -51.17033 | 2025-11-30 04:29:00 | NPP-375D | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 20d055e0-1f12-3dca-95f2-82a30e06d1c1 | -25.04265 | -51.16622 | 2025-11-30 04:29:00 | NPP-375D | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dbd1fe4b-1e77-3dd9-8c83-2b3004f7c4b9 | -23.79032 | -53.06357 | 2025-11-30 04:29:00 | NPP-375D | CRUZEIRO DO OESTE | PARANÁ | Brasil | 4106605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 01e2fc91-2279-31e0-b69a-90be80436886 | -24.07333 | -51.0567 | 2025-11-30 04:29:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 79485263-ba56-3f5c-b31d-047c2cd9fbeb | -12.0195 | -49.2659 | 2025-11-30 04:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| ad9c052f-cec4-305a-83e0-e889054f4403 | -8.1633 | -43.2055 | 2025-11-30 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| a310fd1c-a825-36d1-af9d-c440e069f872 | -19.8675 | -57.7808 | 2025-11-30 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.0 |
| 972b9e35-6a83-37d3-abb4-735150c2047c | -8.1633 | -43.2055 | 2025-11-30 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 20c63f23-e5b5-3e32-add9-2a57f3b58b09 | -12.0195 | -49.2659 | 2025-11-30 04:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8223ecd1-f346-3b78-be7a-0eeae5d7ca42 | 3.34755 | -51.31454 | 2025-11-30 04:42:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2cdd3dd-55e4-3fa7-84a5-6f6335287771 | 3.34696 | -51.3107 | 2025-11-30 04:42:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b18ce85-4f1d-3a09-bb32-a93a2fd8a65c | 3.34883 | -51.3459 | 2025-11-30 04:42:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f3128de-e78f-34af-829f-e3fa213473a3 | 3.35044 | -51.31017 | 2025-11-30 04:42:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6357f964-1cc8-30cf-a714-936f8f90847b | 3.34824 | -51.34204 | 2025-11-30 04:42:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e08c5e39-e3bb-3e0a-903f-54775128e3f8 | 3.35282 | -51.32554 | 2025-11-30 04:42:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 424caca1-fbef-3bf4-991b-64e5d2a1ee87 | -3.59134 | -41.6657 | 2025-11-30 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 49973192-4213-3df5-84f6-0616a7f0d654 | -1.12131 | -47.73907 | 2025-11-30 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65f1dfed-3a6e-3f5b-b824-25a202329c6f | -2.63558 | -48.5433 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4925be89-b3f7-33a8-a177-fd6362e27447 | -2.38722 | -47.61225 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ac92ab2-5b16-391a-97ac-07416f4cd8eb | -1.89725 | -46.44648 | 2025-11-30 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d7ce82c-8a59-3f21-8ad0-bf7744a38bbf | -2.93172 | -51.84837 | 2025-11-30 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33690e1e-23f1-3a65-a39a-873649bf47a4 | -5.72767 | -39.83687 | 2025-11-30 04:44:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d2e9780c-e462-33e2-a83f-0d7f195123e2 | -2.44323 | -49.03132 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e77c838c-96e6-3eb5-ab49-61883c1e53c7 | -2.50665 | -49.10216 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9d63ded-d7e4-3863-ac28-72cc85bb07b1 | -2.51278 | -49.10672 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b04ff6a-b0a7-3528-abac-a52115806cef | -2.34979 | -47.85577 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e610e2f-2dc0-3150-8a2e-46d2cb53f6d1 | -1.47401 | -47.74992 | 2025-11-30 04:44:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b25ff02-4df2-365b-a39d-8da693acd6a0 | -2.90042 | -45.26508 | 2025-11-30 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3028d19e-cb49-319e-a627-a81b0c2fb8ba | -2.76735 | -49.15359 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eabe3930-4f72-349f-82c6-53b4625faf3f | -2.6107 | -49.26214 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9463a992-c3b8-3498-9045-25423380ac98 | 0.61082 | -51.56134 | 2025-11-30 04:44:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8dec8e31-bd7f-3624-a33c-02ec5f189649 | -2.64405 | -48.5558 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be6911ca-6043-3141-a916-5ac6b7b85ebe | -4.52229 | -44.74834 | 2025-11-30 04:44:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e63211c-74f1-3d0d-bf83-909c76cd108c | -3.44326 | -45.41513 | 2025-11-30 04:44:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8c0c582-dcfd-3192-8688-1e75b27503eb | -2.63104 | -48.55008 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58430ab2-43b2-3ef2-bc38-fd061e91407e | -2.30213 | -47.73918 | 2025-11-30 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23858b92-bb6e-3b8b-b557-167759ca8c7f | 0.76542 | -50.80535 | 2025-11-30 04:44:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1fd2337a-b974-3b42-9764-fa2d5925a2f6 | -1.47341 | -47.75372 | 2025-11-30 04:44:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e38db982-54f4-3be0-8271-ef1dce90743b | -4.41062 | -44.4462 | 2025-11-30 04:44:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c155f43b-5b4c-3a4f-b163-6ef5bd136fcb | -2.70112 | -47.40746 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d847fe1-bbb9-3ad9-8d72-0bc8a5dcfc69 | -2.35037 | -48.62252 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68f162fc-5421-3863-b699-cc03ad9fb80d | -3.24888 | -50.68886 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf4a97c7-abe5-3668-991f-b3d0f149d51c | -1.88141 | -47.92262 | 2025-11-30 04:44:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64603de5-53c0-396d-95aa-36fc64552f26 | -5.74465 | -40.81908 | 2025-11-30 04:44:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f15ad329-3e95-3d27-847a-8b43e43eb597 | -2.59682 | -49.26357 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README17.md)

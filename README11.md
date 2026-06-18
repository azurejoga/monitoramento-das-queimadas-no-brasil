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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fdefc7e-8946-351d-bcdb-c2dd121cf427 | -18.25086 | -54.51737 | 2026-06-18 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b3a5ca6-3069-3e6f-94c3-0be3ebdc23bd | -18.82232 | -51.46912 | 2026-06-18 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7007ecad-470a-3a2d-95db-052f31f82979 | -18.83212 | -51.47472 | 2026-06-18 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1d30594a-c082-3941-915c-6d759a8b748a | -18.41658 | -54.5462 | 2026-06-18 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d31a37a6-02c6-35ff-9191-7e56facd6a18 | -19.78486 | -45.39444 | 2026-06-18 04:51:00 | NOAA-21 | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46584e09-ad2a-3a32-87a8-1b29218e4e75 | -27.45044 | -48.4479 | 2026-06-18 04:53:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e221997f-f56d-3ed5-ae44-647f6828e0d3 | -27.33608 | -50.11844 | 2026-06-18 04:53:00 | NOAA-21 | PONTE ALTA | SANTA CATARINA | Brasil | 4213302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 268b67e7-cf51-3f01-b7bb-1fc746869347 | -27.44698 | -48.44791 | 2026-06-18 04:53:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46c19082-9177-3bb7-98b1-ea94d16ad5c9 | -30.65032 | -52.76447 | 2026-06-18 04:53:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 18e59998-2b9f-3b44-8481-17478598dec6 | -12.8354 | -44.3657 | 2026-06-18 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 49317b42-1527-3240-a2c4-c9389a44feaf | -12.8354 | -44.3657 | 2026-06-18 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| cbe74a01-a7bc-3cae-b1be-88ca37e0da2d | -12.8354 | -44.3657 | 2026-06-18 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f29428f7-6487-3bec-b0ef-c93c613bec15 | -8.11205 | -46.47015 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8f24544-b96e-3d68-ac87-0b8f742f5b5a | -7.3646 | -49.85993 | 2026-06-18 05:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8488cb46-22ef-3087-bfa6-cb3a0af091af | -6.15968 | -48.50496 | 2026-06-18 05:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7f5e7c6-de18-3d68-9f42-cad30b3cbd6c | -7.59521 | -46.47641 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3efd0c1-de99-3478-b327-765179ffa81b | -7.83883 | -48.39257 | 2026-06-18 05:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4d221f8-21ac-3058-b04b-55ab2604a507 | -8.93221 | -46.98662 | 2026-06-18 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8ef1f1c-e528-3bf1-8c69-9d57de6db1de | -5.29452 | -43.95038 | 2026-06-18 05:21:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64b0079c-a877-35a6-875c-6a035d9ff28b | -3.8507 | -54.22208 | 2026-06-18 05:21:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faea7ef6-dd3b-36f0-99af-c3cd5de2cd26 | -7.59387 | -46.4753 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0259a45-e290-315a-8788-aa60812e8482 | -6.55992 | -47.88916 | 2026-06-18 05:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c31b2307-7cbb-3ed0-86c0-6681c3d2a6c1 | -7.60142 | -46.47725 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c790e88-0210-3b0a-88a9-31fe57f013a3 | -6.56547 | -47.89023 | 2026-06-18 05:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ace0e04d-b95d-3825-ae23-64719c8c41bb | -8.93276 | -46.98234 | 2026-06-18 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 178a3459-4123-3e91-acde-e411bc6f7fd7 | -6.39757 | -44.17593 | 2026-06-18 05:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56c0a05e-1927-3375-a716-9d523f42643b | -8.50534 | -49.73803 | 2026-06-18 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fbb9492-657d-33fb-be26-215551610910 | -7.91882 | -48.25114 | 2026-06-18 05:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5337cd66-905c-3220-b8b1-7868411c417d | -7.35889 | -49.86478 | 2026-06-18 05:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3bbc45d-902f-3b3d-854a-15c30382aaf2 | -8.91041 | -46.9667 | 2026-06-18 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f00b873-ad12-371d-8f86-363d5cf51da6 | -6.39927 | -44.17724 | 2026-06-18 05:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7eaba4f-4fac-3ac0-9bb5-bfd03ce62502 | -8.90998 | -46.96544 | 2026-06-18 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d921a2db-ece3-3e39-995f-6c564ae43681 | -7.60008 | -46.47616 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a7464b64-e309-3efe-b585-f66b42a3ffa0 | -8.9369 | -48.00211 | 2026-06-18 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b0a7e62-c54e-3782-94e2-9704d8ff67a5 | -7.60071 | -46.47132 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c68f1d71-a81a-32ab-9dda-cfe4cdf6ae85 | -7.79658 | -46.45655 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46b8514f-0e41-39c5-a3f4-ae3e993d13b0 | -6.15688 | -48.5048 | 2026-06-18 05:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 910ca85e-dbb9-3c6e-b206-2fa93f549c7c | -7.79722 | -46.45185 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b3b8e68-4063-3a37-b9d4-5e3e62f44406 | -3.51329 | -48.0354 | 2026-06-18 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad68c500-f4b5-36f1-984f-bcd83305b9f6 | -5.13237 | -47.99257 | 2026-06-18 05:21:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bee789b3-972e-3775-8ee2-1c842deb607d | -7.36383 | -49.86552 | 2026-06-18 05:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a01773dc-b9e7-32a5-9be4-4b4f4d96b5cd | -6.83593 | -47.91598 | 2026-06-18 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9ed4e62-4b7b-34a5-b676-77b43e89d32a | -7.83854 | -55.40851 | 2026-06-18 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937a9ca8-6cd5-3914-9146-adf6dd9709b8 | -6.15639 | -48.50813 | 2026-06-18 05:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a77ae697-d63d-3b28-9ec2-b12e63143204 | -7.60209 | -46.47242 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af379fe0-9ed5-3d1b-8b66-65841a949980 | -7.91932 | -48.24741 | 2026-06-18 05:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cc66047-2e5e-354f-9a19-23ce5cb2a4e8 | -7.72062 | -44.16522 | 2026-06-18 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 604d352e-fdb0-3529-873a-fc99c331a0a2 | -8.9098 | -46.97129 | 2026-06-18 05:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61009489-279b-315f-9d4d-3e59ea3bd4cc | -4.35205 | -47.76354 | 2026-06-18 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99ea760b-2895-3c9f-acab-81891c9755ab | -8.9094 | -46.97005 | 2026-06-18 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0550d8ef-29a0-3a87-b9e3-7c67ceccb6b6 | -5.2936 | -43.95718 | 2026-06-18 05:21:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 308d2b94-1edd-387d-a096-fa09bd417628 | -7.72152 | -44.15813 | 2026-06-18 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dec5ea5-f7b4-3d09-b84b-3f8890587614 | -4.35155 | -47.76707 | 2026-06-18 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 977e7d8c-70ed-3382-9aae-1cc2edebea91 | -7.71711 | -44.16566 | 2026-06-18 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbd7b6d5-0157-37bc-8231-7851fa39b699 | -5.28986 | -43.95124 | 2026-06-18 05:21:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7df8c17b-c4e1-36d5-8b35-df7df3ac3fcd | -3.50802 | -48.03447 | 2026-06-18 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fe6e29a-7016-35e0-b4c0-c18c2de25851 | -2.73631 | -58.19075 | 2026-06-18 05:21:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19bf0229-1be4-37dd-a5fb-62580a87b379 | -6.56413 | -47.88898 | 2026-06-18 05:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19391d8d-7e04-3405-9a81-794e1e73c19d | -3.55045 | -49.10674 | 2026-06-18 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d643fdb9-ec72-3af4-9875-2e512e209819 | -6.39224 | -44.17626 | 2026-06-18 05:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34761388-8be0-303c-b0e8-6f5dfa9d0bc8 | -6.28491 | -43.6362 | 2026-06-18 05:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52f2d531-15d5-36c8-b9e0-6fd52b59c188 | -5.2889 | -43.95803 | 2026-06-18 05:21:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 736784a0-4ba6-3f4d-a509-c1797e2e1bc6 | -7.83914 | -55.40459 | 2026-06-18 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34ba543b-2669-31e1-ad0e-67d9fe95eb7c | -7.71804 | -44.1587 | 2026-06-18 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc089740-3b99-37f3-9eaa-e64e848c7341 | -3.85427 | -54.22264 | 2026-06-18 05:21:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1564f21f-1aa1-3241-a701-505d199cf753 | -7.71618 | -44.17261 | 2026-06-18 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca4b3790-168a-34cc-8ff4-228b31b3fe76 | -4.35699 | -47.76793 | 2026-06-18 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9013dbaf-ace8-30b9-9b88-0a49e37b686d | -7.71349 | -44.16413 | 2026-06-18 05:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57d531c2-80d6-32a9-a443-edd0eb3d723d | -7.83932 | -48.38904 | 2026-06-18 05:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3f02e96-7600-3070-b9d7-742762e40810 | -3.50753 | -48.03773 | 2026-06-18 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e881353f-3775-3c92-b570-4f794cde09a7 | -7.83562 | -55.40404 | 2026-06-18 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b6f369d-4f4d-3266-8b52-a7a9cdca0622 | -7.83502 | -55.40797 | 2026-06-18 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e6a871e-731d-300b-a8ad-602e4f0c09fd | -6.1539 | -48.50741 | 2026-06-18 05:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30aeb1c5-15ab-37fa-98b7-7030008d5b1b | -7.80215 | -46.46232 | 2026-06-18 05:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ae4c692-c002-32e1-b28e-292a0794c98a | -6.84104 | -47.92026 | 2026-06-18 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c50bc4e-b9bd-325b-8f2f-d1abb9aec780 | -5.29688 | -43.95218 | 2026-06-18 05:21:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1407ba97-1554-3928-9ef9-9126839215f3 | -10.15673 | -56.61988 | 2026-06-18 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e26e4e02-c2f2-3598-8dce-e7c1f13ca460 | -8.9808 | -47.98213 | 2026-06-18 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1d0479b-325b-3ffc-9777-9fb89551577b | -18.99002 | -52.45979 | 2026-06-18 05:23:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2218cd10-cd22-391e-809f-877e7df3c3f7 | -10.14873 | -56.62628 | 2026-06-18 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a579e07-d22a-37bd-8770-ebeb9f9905d3 | -14.29335 | -57.5419 | 2026-06-18 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fca6785e-5348-3491-874b-a959d3438515 | -15.07239 | -55.81446 | 2026-06-18 05:23:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b10520a5-df3e-3921-821f-5c906cf7214f | -10.99211 | -47.752 | 2026-06-18 05:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff81cae0-ed0b-32c2-ae8e-d226396e714a | -11.66801 | -56.76497 | 2026-06-18 05:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 083928c3-ba7c-302d-a1b4-74be8dfc59e2 | -12.20899 | -52.78186 | 2026-06-18 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d35da7a4-fe57-3205-86c4-d3b40a2c3c6d | -14.09294 | -59.45921 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da82a0f3-b56f-34df-9bdb-03d4307efd80 | -10.27366 | -60.54249 | 2026-06-18 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbf84e9a-3773-3821-8ef0-2142d6ee06d8 | -14.09514 | -59.46689 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13ee5d39-cffa-381b-96a2-b59533900afd | -10.54497 | -53.72383 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0943c122-506a-3636-9c07-1b4fbe054637 | -13.19806 | -50.34194 | 2026-06-18 05:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97acfc04-3f37-3c86-bef6-6a5bfe865602 | -9.94266 | -65.01038 | 2026-06-18 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dda5c8c0-6243-34a2-8b79-a078bab5cecf | -14.09458 | -59.47045 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40233cf5-dfbb-3d1a-b8c8-8d1d10709119 | -13.65211 | -60.61733 | 2026-06-18 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e57ea3b-ab53-3688-bd57-20a15232ddf0 | -15.07611 | -55.81514 | 2026-06-18 05:23:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5efdd159-d5bb-39c5-817e-baac63faee3a | -18.98513 | -52.45915 | 2026-06-18 05:23:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f63c307-3eb3-3b9c-a711-62083bf1ffbc | -11.24938 | -46.62233 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31b19453-69d1-3610-8a90-501d8aba5a95 | -11.24838 | -46.62973 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0906bcff-f37d-3611-ba82-fe7a354bb98e | -13.19767 | -50.34509 | 2026-06-18 05:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b6b6026c-56c7-3995-b252-44b23892e870 | -10.98669 | -47.74667 | 2026-06-18 05:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 497671eb-3999-3b65-ad40-c286d5bc7f55 | -11.91557 | -57.03856 | 2026-06-18 05:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)

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
| 13feb0d1-e449-3955-bc0b-2e1f27d917e4 | -11.1761 | -53.996601 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d32eb6fe-94d5-3fff-8197-b225eb97886d | -9.0621 | -50.866001 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44dd6e9f-a388-3f29-b9a9-a1cd0b3a68dc | -3.5309 | -48.180099 | 2026-08-21 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae4f541-b1d7-3fe3-964d-fc96e38548e2 | -8.5474 | -54.780399 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c28437c2-bc9d-342d-b9bc-8273ecd7d9b5 | -10.76 | -50.311001 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62670041-6da4-318b-99b7-f8babe0f0f41 | -14.7163 | -47.1441 | 2026-08-21 00:14:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0c8d1b6b-3b25-3697-9fa7-45354d9563f6 | -6.0251 | -50.197102 | 2026-08-21 00:14:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a981815-f017-373b-9886-8d39012cced7 | -8.6565 | -54.620899 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5153e700-7e7b-3c61-9120-6e7c2b484f11 | -9.0718 | -50.863701 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c8e1f3d-a6d8-3e54-8f78-ba4c93ed7c13 | -9.0554 | -50.882 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84ef428b-bc56-3645-bfcf-06e75b436610 | -13.6684 | -51.794498 | 2026-08-21 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc79baa6-2665-37a9-b1c8-0eeb7fc71c77 | -9.3976 | -60.387798 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3fbc1c5-9056-36de-9884-92d4a103784e | -2.7081 | -54.751099 | 2026-08-21 00:14:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8d03314-128a-3ff8-956c-ba7dd76a163d | -9.417 | -60.383999 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62d761b2-7d58-3f59-b543-ef4aabe7e953 | -4.0735 | -42.487499 | 2026-08-21 00:14:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 801eea49-5e5b-3f85-ba68-6b51c3775549 | -12.5169 | -54.733898 | 2026-08-21 00:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e12a7aea-411c-3835-baad-3382e653602c | -12.5092 | -54.7458 | 2026-08-21 00:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9d75307-8b58-3041-ac20-ee9e6250189a | -3.53 | -48.2 | 2026-08-21 00:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9796c479-f8a4-3f49-9b5f-40f5cdaaf8ae | -7.34 | -45.8 | 2026-08-21 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d36074a-b8dd-3aa9-90b4-ce20c7f404f7 | -9.4 | -60.46 | 2026-08-21 00:15:00 | MSG-03 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35eca97b-8fd2-399c-9b2b-2ac2d6ac2d4b | -7.37 | -45.8 | 2026-08-21 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9adf8a01-a1f8-34de-a92c-b9ab7a30ac31 | -7.34 | -45.85 | 2026-08-21 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f5556d4-1bc5-3dc9-be50-7c9b25a8e3fc | -9.4 | -60.38 | 2026-08-21 00:15:00 | MSG-03 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a0be89c-c433-3080-bbcb-0c35369239c3 | -7.37 | -45.85 | 2026-08-21 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0c620c-edc9-3cf9-a704-48b2b7fab057 | -10.2781 | -50.3032 | 2026-08-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| e584ccf2-4d6d-3202-ad95-e09bf0a21d68 | -6.9332 | -59.0287 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e804ab7e-fb29-394c-91df-e47e2cc48bf1 | -6.9333 | -59.0094 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 99b633d7-f08b-31dd-9893-65e7f47edbad | -6.6938 | -58.942 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 202.9 |
| 40821c34-385c-387d-a997-369d73d72970 | -6.2341 | -55.6109 | 2026-08-21 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 182.8 |
| ca8d0a53-b569-3e0e-96fd-57decc69a71d | 2.5983 | -60.697 | 2026-08-21 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 11d9958e-789c-3664-86fa-2d631bb047ec | -7.7702 | -61.1634 | 2026-08-21 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0aa4ccd6-50da-3842-a602-ea9517eaaee0 | -11.1745 | -54.0421 | 2026-08-21 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1fdb536e-d02f-3142-8ba6-672ed6ac6765 | -3.5221 | -48.1896 | 2026-08-21 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 72eedca4-abb5-32ac-a455-3be676deb379 | -6.9516 | -59.028 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 891d757e-de60-3efd-9f53-46bae86dd05a | -11.175 | -54.001 | 2026-08-21 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 61899a47-6ddb-3466-bb9a-543c7d85786c | -18.0285 | -44.6113 | 2026-08-21 00:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 00fdf0fa-897c-307d-8c4e-786ac5fba446 | -3.9596 | -43.1038 | 2026-08-21 00:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 8712f3a7-aa10-355c-b2d2-565bd56146be | -18.2134 | -50.7518 | 2026-08-21 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 73793a39-ce1d-365c-89a6-98fbfa47e9f2 | -6.9517 | -59.0086 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| da63d2f4-14a4-363f-9615-ca79bf5e9e6a | -6.6939 | -58.9226 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 1ca244f5-3a74-3285-a05f-e6e7b0c677c9 | -12.5101 | -54.7755 | 2026-08-21 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5839b3a5-77ce-36ae-938b-14b95b8a228e | -7.3415 | -45.8152 | 2026-08-21 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 6692a842-2580-3ab9-af58-63c01512cb2f | -4.0943 | -42.5097 | 2026-08-21 00:20:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 860c604e-1e4b-3a4a-8dcc-a62c663516b1 | -6.5829 | -58.9851 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 198e8acb-8486-34bd-acb2-5c644e87a9a5 | -7.3791 | -45.8119 | 2026-08-21 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 240.7 |
| 8ed278ef-4d99-3e1d-8b8d-8f461b341e54 | -3.5406 | -48.1889 | 2026-08-21 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 216.7 |
| 5dda61ab-0d36-3208-8a8e-7198753344b2 | -10.7501 | -50.3396 | 2026-08-21 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 81281085-fb3a-3b40-88e2-eb144ada5501 | -8.3903 | -62.6963 | 2026-08-21 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 5f25fc82-6838-33cb-a200-d956a869d789 | -3.5591 | -48.1882 | 2026-08-21 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2a374955-7f64-306f-95e5-cce7231ef3eb | -10.3159 | -50.2994 | 2026-08-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 114c6a06-2122-30e5-bed3-740790634691 | -12.5104 | -54.755 | 2026-08-21 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 60dc4c42-0ef3-31a6-b333-e8da0fa73860 | -18.1939 | -50.7332 | 2026-08-21 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 56531fae-0937-3fcb-ba52-84212ae6cc19 | -4.9423 | -55.7837 | 2026-08-21 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 541b267a-0894-332a-bd8b-6cb450e505e8 | -11.1936 | -54.0199 | 2026-08-21 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 266a04af-2463-31fb-a61d-f2567ce5ad3a | -7.3788 | -45.8344 | 2026-08-21 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 4a1b15da-4047-3085-bf04-f31ff1f72879 | -14.715 | -47.1387 | 2026-08-21 00:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 0bf797a1-1b29-362b-93b6-930085393b99 | -10.3162 | -50.278 | 2026-08-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 430aea56-664f-32ab-9afb-8e81bc69ba41 | -7.3603 | -45.8136 | 2026-08-21 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 476.2 |
| d10bb93d-cae8-3d2f-ac04-485f8ac0978e | -11.1558 | -54.0233 | 2026-08-21 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| a45ec98c-f3be-397e-ad3a-902be9f358db | -10.769 | -50.3376 | 2026-08-21 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| b088702a-2a6b-3974-ad86-8652015fe84f | -14.3343 | -51.8944 | 2026-08-21 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 8229725a-e93b-3546-a1eb-241a25b78965 | -3.5407 | -48.1673 | 2026-08-21 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 7400e68c-d1f0-3837-8294-9b0686d277a8 | -6.2155 | -55.6316 | 2026-08-21 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 4e7b93b8-d4cf-3b94-a942-a59326be5d38 | -9.2071 | -59.771 | 2026-08-21 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 72dd5800-6305-306c-bd29-d5c6678467f3 | -10.7693 | -50.3162 | 2026-08-21 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 86b7d421-8a6a-3dc5-9125-41557c9f7811 | -10.3148 | -50.3848 | 2026-08-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 714bcf33-a43f-36da-aa7c-d5fabda218d0 | -18.1934 | -50.7554 | 2026-08-21 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 51e9b77b-79ec-3524-9f3c-4ddfaa301ad4 | -7.36 | -45.8361 | 2026-08-21 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 229.1 |
| dab646d6-5fe4-31cb-a3b6-c7a02f31dcee | -7.7703 | -61.1443 | 2026-08-21 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b9eae6e1-d3a5-3c7b-af33-ca3dedef311c | -6.8593 | -59.0318 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 20d7707d-4764-3d7b-88e3-27eb4cea528e | -6.8756 | -59.4171 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 2fab8bfc-095e-360a-ae26-863ced7454d1 | -11.1561 | -54.0028 | 2026-08-21 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f030629a-fcd2-330e-9ac6-05f0156f5f93 | -15.7156 | -47.781 | 2026-08-21 00:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 7e5f385a-403c-334c-b78e-20541cf304ac | -6.5828 | -59.0044 | 2026-08-21 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 40c16221-5311-3f4e-9b68-b94691fa2166 | -6.2156 | -55.6118 | 2026-08-21 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 073fdb87-1070-3f1e-9ca5-f3398e85b50c | -11.1747 | -54.0216 | 2026-08-21 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 229.4 |
| f4cc7ccb-04e9-3201-8ed5-ac8502677e97 | -10.7504 | -50.3182 | 2026-08-21 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 727332be-6acf-351c-b9d3-953c9cc8fa37 | -14.3339 | -51.9157 | 2026-08-21 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a7c3e48c-9302-32cc-9e8a-3effcbee69af | -10.2595 | -50.2838 | 2026-08-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7801698e-44ee-335c-9596-1da44b595dbc | -18.2139 | -50.7296 | 2026-08-21 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d4e84083-21cc-3a5a-97b4-721162af780c | -10.2592 | -50.3051 | 2026-08-21 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0e512390-a99a-314c-a2c8-7ab7caef264b | -7.3788 | -45.8344 | 2026-08-21 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 63f79571-c88d-30a7-bdd9-09c1fbe996f0 | -4.9423 | -55.7837 | 2026-08-21 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d3001e35-4e64-375f-bbd1-950e81329850 | -7.3603 | -45.8136 | 2026-08-21 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 537.9 |
| a3ce44e6-3fa7-3009-a8aa-1c5be97f17e2 | -14.3343 | -51.8944 | 2026-08-21 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 8efeed85-15b9-38b0-ac10-72aea2b57115 | -7.7702 | -61.1634 | 2026-08-21 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 295ee100-a952-3563-b829-7dd5b076ca6f | -7.3415 | -45.8152 | 2026-08-21 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 69d1e723-80d1-393a-95c6-84b4d832b3ef | 2.5983 | -60.697 | 2026-08-21 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 25e0a88c-8505-3e54-af82-7b2365261a29 | -11.1561 | -54.0028 | 2026-08-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 1867bf86-efa2-3e3b-9a38-fea7fe7676f3 | -4.0943 | -42.5097 | 2026-08-21 00:30:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 2d43d071-f734-38ad-b67e-4080f1673601 | -7.3605 | -45.791 | 2026-08-21 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 55361dea-40d3-3dff-9cd6-8020acc403be | -3.5406 | -48.1889 | 2026-08-21 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 5f6f30bc-78e4-37be-a07b-62eccf221413 | -6.894 | -59.4164 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 0ae3e38a-3c87-3eb6-b951-2b1d1b0a2779 | -12.5104 | -54.755 | 2026-08-21 00:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 61978ef1-f977-351a-8c86-12444bac5d68 | -10.7693 | -50.3162 | 2026-08-21 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5e4c7acd-1dd2-329a-9d37-000c916dbf68 | -10.2595 | -50.2838 | 2026-08-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 576f4800-be1c-3166-9237-0671f875179f | -11.1745 | -54.0421 | 2026-08-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d7dbf76f-3952-35b0-b93d-ba4937c14850 | -11.1936 | -54.0199 | 2026-08-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 746c864e-be13-302d-af6f-9ae62e7e57e6 | -10.769 | -50.3376 | 2026-08-21 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| c703c363-59a5-3395-90d8-9d92b73033e8 | -6.9517 | -59.0086 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |


[Clique aqui para ver as próximas entradas](README9.md)

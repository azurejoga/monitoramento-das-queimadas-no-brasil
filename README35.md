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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f414a1a-e1a7-3b97-b423-08513f61ad4e | -9.39621 | -60.54401 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56265e87-6264-3e25-81ec-0ff876779d7d | -9.22341 | -59.64249 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4177387-1c1f-307d-bdec-929a6d24a9b4 | -8.98252 | -60.56062 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8c9c4bc-e4c5-319f-8923-ab29439009f7 | -9.54449 | -63.57604 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85e50fc8-9e5a-330c-b8d1-bd57de8680d3 | -9.19589 | -59.62997 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ab397b50-1dd6-3f99-bdce-c5c3d8d43c06 | -9.50222 | -60.51259 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f25fb3c9-88ca-32d3-b15c-e15d33aca282 | -9.9268 | -60.46819 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75ee2cd3-8f00-396e-9a00-db22cd96fe71 | -10.12536 | -57.7752 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24b50373-0c92-322c-a99e-d71422969128 | -9.55032 | -63.66813 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f62c54a9-309e-35a6-aefc-a52d29e52ac7 | -11.36391 | -55.39167 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 906d6da7-e29f-3aba-b7f1-36d3975da0f2 | -5.45061 | -60.14227 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4eda8a04-ae17-3733-b950-3efd857f5bdb | -6.07735 | -59.94474 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98440162-ddc7-3df6-920b-235ae9ffc81b | -8.99124 | -60.50385 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88b7267f-0486-3333-a00a-3bef09d2ad41 | -6.07451 | -59.9634 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e54ef81b-0ef0-365e-aed3-0f109ec45c84 | -7.21642 | -60.38545 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bdade9d-894c-38a9-80b0-eb987a8d09e0 | -5.91897 | -61.30214 | 2025-08-17 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6810ae01-670f-3cb7-83eb-654225fa2e2c | -9.39217 | -60.54731 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7927c503-c348-33bf-8dc6-72f0053b02c8 | -8.06153 | -70.58279 | 2025-08-17 05:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd586911-423f-31f5-a0ca-4bd2f90c5bc1 | -9.16417 | -59.62078 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f82055a8-46da-3dab-85a9-a99af4f162cf | -9.50681 | -60.55239 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 463fd3b9-3665-3816-aa05-6cb5e3061e1b | -5.45742 | -60.14332 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b79e70f4-bd23-3c45-9f70-4e57c30f44da | -8.86932 | -68.50715 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de022c64-8d2d-329c-8194-96867bb492ee | -11.7341 | -62.32972 | 2025-08-17 05:31:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a6773dd-5729-367c-84ee-dac1b19b4fba | -11.36945 | -55.42516 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf74a393-b623-3b4f-9695-9b5255c2222f | -9.16356 | -59.62492 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cf05cc7-0306-3e56-a640-4ba9fc01615b | -9.51202 | -60.54147 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 989383ca-0ea5-3f7d-a9c5-fa4279aeeee3 | -9.18266 | -59.64479 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5495a050-011c-33ba-8f53-839685fd1771 | -10.34212 | -64.47931 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6a929bd-5f0f-307d-aaad-8c0bbb23e417 | -11.43025 | -52.22094 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1057053e-2f10-3bc2-9595-911e10e6d505 | -10.68529 | -69.55149 | 2025-08-17 05:31:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2ed40ab-98d5-359b-8fd2-ee6cba75da34 | -10.34612 | -64.4762 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b045542e-a58a-36b7-9c06-14fbc06436ec | -9.18982 | -59.64602 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ca799b2-832b-3136-80df-f68b0935a0c1 | -9.55538 | -63.658 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b19846e2-af09-32c4-8868-d482fc338e02 | -8.98255 | -60.53743 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4be39335-5ea3-325f-8f4c-6128ae0c343e | -9.5103 | -60.52948 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e3860dc-ad47-3a38-b733-1b097bd0c03b | -7.53399 | -50.53191 | 2025-08-17 05:31:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a75f91d1-1f74-319d-b2ff-12cacda6cf39 | -6.08137 | -59.94151 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f292e2e1-87ed-360e-b163-0ae2f24f0495 | -9.22279 | -59.64661 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89f9ca27-c367-3e68-a410-1668da9751ad | -8.98146 | -60.49847 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0262b912-45a8-358d-a823-b3ca22bcc94c | -10.11018 | -57.76563 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33052933-39b2-3177-a48a-f297b348c098 | -9.8866 | -64.26939 | 2025-08-17 05:31:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62920950-e2a6-38a4-b0aa-66bdfa2e8021 | -8.89491 | -60.74269 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ea56fcb-4f74-3de4-81cb-a02701f1012f | -6.66372 | -58.81789 | 2025-08-17 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff7d40b0-9451-3f3e-8b7c-bb76bd197afe | -5.80963 | -59.21825 | 2025-08-17 05:31:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73dbc9cf-cac2-3efa-9da4-df16aa6e4b63 | -8.98891 | -60.51905 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78cad1bc-19c7-3141-a76c-e92c37527817 | -9.1582 | -59.61142 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7107856a-4a0a-340d-ba1e-320eca50991e | -9.21982 | -59.64196 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deb72ad4-0c11-339f-ad64-fd4100764005 | -5.8061 | -59.21773 | 2025-08-17 05:31:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5beea15e-24cb-3a26-b618-100571214ce7 | -8.99348 | -60.53526 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7874fadf-0d20-340a-b2ba-10ac50c76be0 | -8.59809 | -69.71213 | 2025-08-17 05:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31164e6d-1f9b-3d2b-9ec9-a257ddeddd15 | -8.98197 | -60.54121 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30cea956-7575-32af-9325-b8649aba5fbe | -7.50155 | -60.30255 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0266189-0dee-3439-bd35-2b7ff7d5d1cd | -6.67165 | -58.81472 | 2025-08-17 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c3521f8-3a89-3ce5-98f9-f6b04d267572 | -6.1404 | -57.93079 | 2025-08-17 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 567fc051-3ec7-39a8-b67d-04a3d93543ef | -9.90588 | -67.01649 | 2025-08-17 05:31:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bc9d846-5a54-38d8-b91f-5ac8a9e0cc10 | -11.41321 | -55.35452 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d510319d-e9a3-32a2-8a75-1400b6fb8a87 | -8.33512 | -70.57214 | 2025-08-17 05:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8a29132-616c-3eff-8d7e-f49f38e85b8f | -8.97742 | -60.50173 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9f677c08-477b-3f34-bc82-aa2d32a7f0aa | -8.99407 | -60.53146 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad680510-bef9-3702-9b24-552676c467a7 | -5.4489 | -60.13079 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd338a9b-76c4-3f03-b279-366416937c9c | -9.55481 | -63.66156 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac30e5d-f6ff-3db6-a55d-45791d8be218 | -7.09829 | -59.22055 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4361d2d-ae80-31a9-9eae-4d5d3b55b9d3 | -11.36322 | -55.39706 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0f2726c-19dc-3f48-843f-2e870fe25f7f | -9.42121 | -58.91344 | 2025-08-17 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20dbeecb-62bb-3fb3-800f-358feb2267f4 | -8.99294 | -60.51579 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad16cc8e-8701-306c-a673-ce6e538ad69e | -9.97611 | -63.29417 | 2025-08-17 05:31:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e627142-a390-3f2f-b941-ed4b55482bad | -8.9929 | -60.53904 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4bb6063-c556-3326-8229-86de7965d26e | -9.20249 | -60.83087 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ff576a6-683e-3efc-b36d-a872fd8ea2c1 | -9.15997 | -59.62439 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b8f2fcd-f602-3e77-9aa9-98cc0aceaf16 | -6.66008 | -58.81732 | 2025-08-17 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03a7ad63-2a4f-34ab-9146-b905c002a01d | -6.65943 | -58.82155 | 2025-08-17 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84350aab-dddc-3a81-9c94-51620d0059f3 | -8.98717 | -60.53039 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71fae89f-6371-30d6-b27b-36577d605395 | -8.99756 | -60.50871 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 421d3607-6de2-38fd-9db0-606ad8ea6c3c | -10.35549 | -64.50428 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f9b8e58-65e4-39a7-9dc0-74532002c7e1 | -11.42792 | -52.21886 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3aaedb5-b7be-30ae-9755-ce88ea2f2c55 | -9.14201 | -58.29243 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d10c8e5-ad30-3888-a744-833ab40229e8 | -11.43077 | -52.21648 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e94fdcb-41d7-342f-8a6b-c1e1afa0ca36 | -9.39275 | -60.54349 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c624f8b-d788-3f38-a7fd-8ee064da73b1 | -9.61597 | -65.37437 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d23a00f-6ed2-3d92-8d10-1d4ad876cde8 | -9.62369 | -65.37157 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ba4ae7f-4032-3101-9e3f-544badf2df02 | -8.98426 | -60.54929 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a016eee7-6925-39e9-8575-99ea19a71bcf | -9.50161 | -60.56329 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20cc3000-c069-3c08-8464-a597370df304 | -9.42496 | -58.91395 | 2025-08-17 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6cde59b-2e5c-3e3f-bcbd-ece62d917f98 | -9.51028 | -60.55291 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 72b76c86-2c48-39ac-9a72-a73c8d572af3 | -8.02697 | -72.50407 | 2025-08-17 05:31:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c1b35d2-3cbf-397f-a7e6-9588533a3d73 | -9.50797 | -60.54477 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa014d10-1d3e-3b80-a50d-f8e4401e497f | -5.45912 | -60.13236 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaeb182d-9340-3e59-a317-01aea41a9473 | -9.51724 | -60.53053 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 19677f17-2d20-390a-bfb2-9123ec51cbbb | -6.08596 | -59.93453 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f7f06d1-50ea-3e84-8241-4a606aa70737 | -6.08023 | -59.94899 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2d43e44-a56d-3f8f-8fc2-4d2935da059c | -7.42119 | -60.59676 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f221fa1-11f3-3c83-89a2-01230cb5e9ae | -10.35489 | -64.50797 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74f4ef44-f415-3844-85a4-7c60ae38fbd8 | -9.51665 | -60.53436 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 88b9395a-35ba-34b7-97bd-18ff179d66b7 | -5.4472 | -60.14175 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c51f4004-ff84-36ea-a9f5-e37d7582b97a | -9.50453 | -60.52078 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbe3cf41-d63a-3c1c-b1fc-5be8465d944d | -6.07795 | -59.96391 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18a936df-9046-35d8-b977-7683fc9144c8 | -9.17198 | -59.61773 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 787bd43f-84fe-39e2-9cc2-ba392aaf2e34 | -9.16295 | -59.62906 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8aa75d0-012b-3b36-a1d9-1ea450c7b40f | -9.53022 | -63.66488 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c533e6cd-cadc-3291-a140-09865063db71 | -8.99007 | -60.51144 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)

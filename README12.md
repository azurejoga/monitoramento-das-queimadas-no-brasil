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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 979c5e01-905f-31b6-9870-bd4d298d576e | -16.167801 | -43.832802 | 2024-10-15 00:59:48 | METOP-B | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 30ff2705-1d86-3d4d-b6bf-0fdd3ac23748 | -16.882 | -57.281799 | 2024-10-15 01:00:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f8956ac-b389-3a2e-8905-d92ed45b0b3e | -16.868401 | -57.264599 | 2024-10-15 01:00:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6765864a-0d51-3a3d-a907-9de7c33da5df | -16.8703 | -57.2742 | 2024-10-15 01:00:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d7a5180-5723-3ab9-ab8a-c8fa2802e47a | -16.858601 | -57.266701 | 2024-10-15 01:00:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea34f1dc-7f86-3719-81bf-9cf5aaa4f259 | -14.1037 | -46.107201 | 2024-10-15 01:00:30 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c890959d-7049-3100-a464-8ab5a8000633 | -14.1077 | -46.122601 | 2024-10-15 01:00:30 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1704d45-4b02-3b21-8e25-de554def2ea9 | -14.1116 | -46.137901 | 2024-10-15 01:00:30 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82cd2f5a-f8b4-36fd-850f-cd81fef1aaca | -14.1155 | -46.153301 | 2024-10-15 01:00:30 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81a45b41-7897-3b51-9113-7d0ecbffdda3 | -14.0883 | -46.1278 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75550692-5a39-3fbd-898c-1c8b36dc1f45 | -14.0901 | -46.094398 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b0cc478-5cd0-3bb5-a0b2-87e35ee5e8e4 | -14.094 | -46.109798 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ece28b9b-60eb-3fde-af65-c5dbb25ae1b8 | -14.098 | -46.125198 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d3f06d7-547a-3976-8913-ef395c2f6591 | -14.1019 | -46.140499 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dca8ea3b-2966-363f-b184-d8c94dd29ea2 | -14.1058 | -46.155899 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f24da85f-5197-3062-9bfe-f52249b61e71 | -14.0804 | -46.097 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7e67f11-36f2-3075-93ff-8843cb057234 | -14.0844 | -46.112499 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b76e4e1b-ccff-363b-a94e-f7e89790e781 | -14.0923 | -46.1432 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d783e49-b024-326c-aa7e-cb57f6d82fe6 | -14.0962 | -46.158501 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c7ce37e-a797-3006-99a2-cfa787e9d326 | -14.1001 | -46.173801 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab2e04b3-a7a1-374e-aa70-b027ce9a9d65 | -14.0747 | -46.115101 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea57775-bcd8-3aee-bae7-24c0f21a8d2c | -14.0786 | -46.130402 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c45c4f4-88ca-38cd-ab22-1d1c1c6ee06f | -14.0826 | -46.145802 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea7ce14-60b3-34df-bcd2-6532d38282a0 | -14.0865 | -46.161098 | 2024-10-15 01:00:31 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 937014cd-9c05-3edd-a5d1-a9ad5bbd667d | -12.8482 | -44.5751 | 2024-10-15 01:00:44 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b25a8c2-c4aa-3b9e-8f84-89e95d923d83 | -12.8535 | -44.595501 | 2024-10-15 01:00:44 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b4a5c9f-689b-38b6-aefa-607368f1a964 | -13.5929 | -49.7682 | 2024-10-15 01:00:53 | METOP-B | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 28acf12d-8625-319a-ac7f-cc6d491e6e64 | -13.5952 | -49.7775 | 2024-10-15 01:00:53 | METOP-B | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 311b923c-8a6a-316a-81a7-151d830d3f44 | -13.5832 | -49.770699 | 2024-10-15 01:00:53 | METOP-B | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e9d2d5be-ceb8-314c-a456-cd176769e0ec | -13.5855 | -49.779999 | 2024-10-15 01:00:53 | METOP-B | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f010415-39f7-3f57-82f6-4a7657b2c040 | -12.0588 | -43.8512 | 2024-10-15 01:00:54 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e65962b-f653-3f08-8a9d-b5d2d1047df0 | -12.065 | -43.874699 | 2024-10-15 01:00:54 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dad10f33-cd98-33ce-af6c-2fe98674ec32 | -10.152 | -46.2425 | 2024-10-15 01:01:07 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 158e0ae8-c0ac-3bb8-90cd-a6bfc16bb711 | -10.1564 | -46.259998 | 2024-10-15 01:01:07 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| caa556a5-2569-310f-b81f-c214f765b7cc | -10.1608 | -46.277401 | 2024-10-15 01:01:07 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5abd70b6-1230-37db-a180-fab1d7f5d474 | -10.1423 | -46.244999 | 2024-10-15 01:01:07 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90d82dee-744c-31f9-bddd-d79f76c97ee8 | -10.1467 | -46.262402 | 2024-10-15 01:01:07 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd14ea25-12c9-3f47-9796-f1b5cf7bf6eb | -13.1268 | -51.695099 | 2024-10-15 01:01:08 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 621aa862-4d21-3701-8279-d8063dfa112f | -13.1152 | -51.689701 | 2024-10-15 01:01:08 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99c84251-e5c2-31f8-b025-e28cd2860d4f | -13.1072 | -51.699799 | 2024-10-15 01:01:08 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e621cd62-0ab2-34a2-87ca-69f211ee4a96 | -13.109 | -51.7075 | 2024-10-15 01:01:08 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1805c94-4a6b-3730-9f13-c0a81040a7ab | -13.1108 | -51.715199 | 2024-10-15 01:01:08 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb608ee1-6664-3b86-bb48-0d0651db4c3f | -10.8269 | -49.223499 | 2024-10-15 01:01:08 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f5c21f6-8237-3c0f-8090-a782bba8b312 | -10.8295 | -49.234402 | 2024-10-15 01:01:08 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c1cbe0d-d82a-3d7a-a316-f6cd8e819c66 | -10.8172 | -49.226002 | 2024-10-15 01:01:08 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfd90f09-b508-3633-8356-a07590f969b1 | -10.8198 | -49.236801 | 2024-10-15 01:01:08 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64d88670-4b40-3a8e-a60f-2d1b2e708da4 | -10.8224 | -49.2477 | 2024-10-15 01:01:08 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48de001d-738d-323f-af61-f749168ceeca | -13.5115 | -61.716702 | 2024-10-15 01:01:08 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c523e816-ebea-3d17-83fb-4d6d18a7969a | -13.5146 | -61.733101 | 2024-10-15 01:01:08 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 223a5a4b-d7c4-3b9d-a41f-103a5e5c5d01 | -10.4488 | -47.844799 | 2024-10-15 01:01:08 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3eefce40-ebc3-3473-8c4a-c63a195c77c4 | -13.5018 | -61.718601 | 2024-10-15 01:01:08 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca65b9a-19d5-3ba9-af0d-64d8d994c9aa | -13.0992 | -51.709801 | 2024-10-15 01:01:09 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 33cba39c-062e-340e-bc3a-90443d566727 | -13.101 | -51.717499 | 2024-10-15 01:01:09 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32e26948-4858-32e5-a5fd-78cc0ae45a09 | -12.4879 | -49.556499 | 2024-10-15 01:01:10 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a8d77c1-7cad-3fd7-b479-3fe3ef71b3af | -12.4903 | -49.566399 | 2024-10-15 01:01:10 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09d325bf-2cfc-3968-b0cd-9924c26c4b12 | -10.4583 | -42.400902 | 2024-10-15 01:01:14 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8e278056-9723-3ddf-b68b-c66b4a524c16 | -12.9473 | -53.488701 | 2024-10-15 01:01:18 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca4948f7-4660-3ca0-a4fb-ce4effe904e3 | -12.9422 | -53.512001 | 2024-10-15 01:01:18 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af36eca2-4d24-3d3b-8103-4bd477d88c05 | -10.7438 | -44.8092 | 2024-10-15 01:01:19 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 93df17fb-350e-3899-a3c8-f436e7456388 | -12.8901 | -53.5093 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f541e465-a16b-3f99-9255-dda906c3fe3a | -12.8917 | -53.5163 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df482080-7033-3e2c-a8db-be3043f7917b | -12.8932 | -53.5233 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edb30813-2197-37cf-8387-021edc1fa5cc | -12.8819 | -53.5186 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d33052b-338f-3ff5-8c04-30185e8431b9 | -12.8834 | -53.5256 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7a2bd70-895b-31b2-a259-dd4f39838543 | -12.885 | -53.5326 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59f5f6ff-c0ec-31eb-a05f-72487c79a98c | -12.8866 | -53.5397 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e83676f-3b69-37f4-9ff0-b97dd4b7e737 | -12.8705 | -53.513901 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfbbd93c-418e-3672-b1fa-03486cb5045d | -12.8721 | -53.520901 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8c2f5c0-8543-3a77-8c71-9148c7da73f1 | -12.8736 | -53.527901 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d00eb027-5373-3ae8-b1da-7f8bddf65376 | -12.8752 | -53.534901 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80c1d504-405b-374c-89b1-e435820564ac | -12.8768 | -53.542 | 2024-10-15 01:01:19 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66c41c65-ed2e-31f2-abbb-1bd3145aa20a | -12.0701 | -50.272202 | 2024-10-15 01:01:20 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46b23ea2-1a79-3e2e-9e4b-caf45d6a2c41 | -12.0787 | -50.308601 | 2024-10-15 01:01:20 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1d2d750-7bcf-3a00-8720-82d76ba1c56e | -12.0646 | -50.2929 | 2024-10-15 01:01:20 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eae78225-2ad0-36ba-b4fe-054ef4ec4986 | -12.0668 | -50.301899 | 2024-10-15 01:01:20 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e4eb497-0543-3a91-8496-7051f478c641 | -11.6184 | -48.485699 | 2024-10-15 01:01:20 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8c4efed-366f-316d-8d4a-51123e69d7dd | -11.6213 | -48.497501 | 2024-10-15 01:01:20 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94608d4b-4947-32ad-8eb2-621be600bfd0 | -11.5815 | -48.419601 | 2024-10-15 01:01:20 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bab619f3-4d8b-3ad9-99c8-f43e8a96f32a | -10.4903 | -44.151299 | 2024-10-15 01:01:21 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d081e760-e48f-341d-b331-0adba3d28e94 | -10.4966 | -44.175201 | 2024-10-15 01:01:21 | METOP-B | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2d161f9b-b10a-3704-aa37-1b56c8120533 | -11.5718 | -48.4221 | 2024-10-15 01:01:21 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16aa42f5-807d-351b-afb7-a3679cec4b0b | -11.5552 | -48.4389 | 2024-10-15 01:01:21 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba4816e6-f42d-342e-8e1f-e571bde991c9 | -12.0949 | -50.725899 | 2024-10-15 01:01:21 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92b26a82-67f4-3b13-b40f-8fb788fd1e5f | -12.0969 | -50.734501 | 2024-10-15 01:01:21 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a99c138c-1399-3b54-add5-035bcdd5a011 | -12.0891 | -50.745602 | 2024-10-15 01:01:21 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3fff014-e585-3d67-abad-4a1f47b9d6de | -12.0912 | -50.7542 | 2024-10-15 01:01:21 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 75bd5cc8-bf08-3ad6-b592-2320d8a3fc91 | -12.0794 | -50.748001 | 2024-10-15 01:01:21 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 67b00203-ca8f-3630-9469-cc87318ec13f | -12.0815 | -50.756599 | 2024-10-15 01:01:21 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f93efdf8-e625-3872-ab47-4584b67c0630 | -12.0475 | -51.095402 | 2024-10-15 01:01:23 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34e32e59-b2f7-371f-a31b-244b1d3b4971 | -10.3787 | -44.791199 | 2024-10-15 01:01:25 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 02ab0828-371b-3a2e-b557-0543a7b66575 | -10.3843 | -44.812901 | 2024-10-15 01:01:25 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d069701-399e-34ab-900b-407cf9b68f5c | -10.3691 | -44.793701 | 2024-10-15 01:01:25 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c304a68-269f-3f9c-acca-3951afcba7e6 | -11.0899 | -47.682098 | 2024-10-15 01:01:25 | METOP-B | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 851c2e51-63df-3042-964a-6aa095cd9012 | -11.0933 | -47.695599 | 2024-10-15 01:01:25 | METOP-B | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3eaf91a-b386-3552-851b-e0d2eaced869 | -10.0678 | -44.187401 | 2024-10-15 01:01:28 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 22a48e89-4dc4-341d-9612-f6fede6ba07a | -10.0741 | -44.211601 | 2024-10-15 01:01:28 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a06b972b-f6c5-31e1-bc69-7cb0df28a131 | -11.9918 | -52.458099 | 2024-10-15 01:01:29 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61aa3792-423b-3cbb-a5c6-48693dfc8f71 | -10.6065 | -47.689098 | 2024-10-15 01:01:33 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee27f38b-b366-302c-8974-9de7a7378f41 | -10.6099 | -47.702801 | 2024-10-15 01:01:33 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ee1d888-6bd5-38d3-b839-9d0616eb25b4 | -10.7882 | -48.4272 | 2024-10-15 01:01:33 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)

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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6df6e66-2d11-31a7-a566-7a347a839f75 | -14.22331 | -45.45672 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fa40c37-ad53-36af-bb69-f9a1d4344760 | -7.71015 | -45.65931 | 2025-05-06 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 935f2fb3-c8ac-3ff7-a884-cffce5b22c12 | -14.23453 | -45.47345 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f066d235-fd47-3b34-b9e8-d7082c1aa30e | -14.21046 | -45.47329 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaad98e3-97fd-368a-96be-d5643d23076a | -10.72363 | -42.32531 | 2025-05-06 04:21:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1eefb121-6d01-3468-8f72-dc0403c4789f | -14.21604 | -45.45928 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9d5713e-25f5-3f8c-a2db-9f265d1dcb29 | -14.20765 | -45.46911 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 233a132a-651c-3e32-8c4f-7a6c1249cd7c | -14.23229 | -45.46563 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98d9437a-ec25-3eb2-b244-2986b2ac568f | -13.66673 | -47.84042 | 2025-05-06 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 703afeb6-3ebd-368e-86ff-b68657956f3d | -10.99228 | -44.44294 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aea05756-42b4-3ee7-9e9f-bffc846e8af5 | -14.2194 | -45.45982 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29ca718d-f40c-320f-979e-6229875a498f | -8.19622 | -46.76141 | 2025-05-06 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13c0798c-119a-3969-8e8e-58f92c76e427 | -8.0763 | -43.13424 | 2025-05-06 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| bfcce92e-2b3e-3c33-a7d0-d53efeed09d7 | -10.60376 | -44.76656 | 2025-05-06 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9325dd5f-df0b-3d8b-8a73-0e69400618ad | -14.23956 | -45.46306 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8af60a64-a72d-318a-88c2-4ded8e86056e | -14.21437 | -45.4702 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d32043d4-b175-3ee1-94b7-5e30b809a710 | -10.98043 | -44.42991 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59213797-d754-3e42-8e7d-21687bbfd117 | -14.22667 | -45.45726 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 314975c7-dc7b-32ac-aa29-135bb2b88b28 | -12.17857 | -44.34252 | 2025-05-06 04:21:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 305c103c-4a13-38b0-abff-bfa4980b430a | -7.55608 | -45.83709 | 2025-05-06 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 140e3e8e-ef96-3361-9c75-209ad7ec608d | -14.23395 | -45.45469 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8338241-88aa-3669-9528-fd9bdbe0c263 | -14.23845 | -45.47034 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 564710af-0f67-39a9-8f53-817b4da526ad | -11.96904 | -44.16018 | 2025-05-06 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fc19a1a-187d-30f8-bb4a-13f6217583c8 | -14.23173 | -45.46927 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfca43f1-f69e-34b1-89d6-058ae929c6a9 | -10.98608 | -44.43824 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f13e24c1-c00e-392e-99cd-b6002a2f421a | -10.97593 | -44.43666 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3dba3822-4dc7-37ce-8233-8e973826c31c | -12.83079 | -44.89159 | 2025-05-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84240291-63c9-367b-ae8d-1b36b3e6677f | -8.07688 | -43.13049 | 2025-05-06 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 1e1f3a4a-1bae-3ee4-9411-501339cae6ed | -10.60712 | -44.76709 | 2025-05-06 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 615dba8a-e110-3721-819f-54063c18180f | -10.97649 | -44.43303 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 449f2f94-9162-3b12-8679-313ff8ae2270 | -14.2334 | -45.45834 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab3d4b43-98af-3e37-9c0c-1205883e1d85 | -12.03689 | -54.24969 | 2025-05-06 04:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0586629c-99ea-3d23-bb55-18d473425610 | -10.97537 | -44.4403 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 685c7026-3247-317e-bb68-64479529842a | -11.00067 | -44.34337 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c9c086a-951f-31cc-8d58-55e91914385b | -14.22948 | -45.46144 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65cf48da-60ab-3a77-81b0-0d5128ccf9e3 | -14.22837 | -45.46873 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b12f7b44-f5f8-3ef8-95ef-d1c288ec76a1 | -14.21382 | -45.47383 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c97f293-c3a1-319e-a8a8-45ea83fdcf8c | -14.21662 | -45.47801 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2b5b595-83b2-3c5b-914a-bcf3c3147ef1 | -7.55551 | -45.84062 | 2025-05-06 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51d87a99-e041-3068-8f53-53645a96331f | -14.21659 | -45.45564 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c117e13f-fe0e-3bef-a78f-17f24eeaa81e | -10.98269 | -44.43772 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c17b7146-d20c-3216-919f-e282fe4d9e8d | -10.97705 | -44.42938 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19cbcf97-0965-36a7-ac8d-46f6f71c27c1 | -13.66897 | -43.79048 | 2025-05-06 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ec87bdd-e579-3e53-9aa5-3bf715f90b28 | -14.23901 | -45.4667 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b59bd86-4bc3-3e7f-8cd9-1c63799df9d1 | -8.306 | -48.04894 | 2025-05-06 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32b7f73c-ba1b-3a09-856f-99f7b4414433 | -6.94154 | -47.90182 | 2025-05-06 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed1b1104-0040-36dd-94ac-9b69aed29d3d | -14.2222 | -45.464 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a1b61a0-96d5-365f-8079-86752afbff35 | -11.19499 | -44.50809 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30a9993c-85b6-3d5a-891e-5efc8263949c | -11.96961 | -44.15641 | 2025-05-06 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0d0a7aa-8128-3030-b518-154992a7f656 | -14.22723 | -45.45362 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d63772cc-f101-36da-8628-d4c21d1287f9 | -10.97931 | -44.43719 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f1c7439-7fb2-3021-94a4-b64917f92d79 | -12.03714 | -54.25048 | 2025-05-06 04:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3014fe02-2f96-36f4-9ac5-483c33fbbe5f | -12.17515 | -44.342 | 2025-05-06 04:21:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ae6e0be-fc01-3c11-8b01-44629ab01c00 | -14.21268 | -45.45874 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc7f62a9-a026-33f3-ae22-8b547ca5cebb | -12.178 | -44.34626 | 2025-05-06 04:21:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99a0529f-e2c2-3d6d-a37b-b89d17ef7aee | -14.21326 | -45.47747 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cecd6fa-bc66-38c3-a8d9-704624dcb912 | -14.23509 | -45.46981 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0793fd9-06db-3c1d-ba5e-69808e39d345 | -11.19106 | -44.5112 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad2f9c59-7948-358a-9b8a-cf8426c54335 | -14.21995 | -45.45618 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7455771-4f54-3d07-8015-8b21f5f17d61 | -7.55942 | -45.83762 | 2025-05-06 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c78c9159-92d6-3fe5-8d22-b702a6db23bb | -12.04185 | -54.25069 | 2025-05-06 04:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0a64738-c85b-3412-814d-44601b2ea237 | -6.71436 | -47.59594 | 2025-05-06 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03e901d9-8c18-3d2e-95df-e2679a23c5b7 | -14.23004 | -45.4578 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88d4d93f-064c-38d2-8eee-c305bc3073da | -10.7273 | -42.32586 | 2025-05-06 04:21:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6aba3e4d-22ab-3f5d-91f1-bc08340596de | -8.07286 | -43.13371 | 2025-05-06 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 76b7885a-ce43-3bdb-adcf-8c807c3d5f86 | -14.21773 | -45.47074 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38b422b4-211d-3d7e-99f2-618a71ff1220 | -10.99284 | -44.43929 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 736b3f33-8308-3992-b146-dd6d9ffc3ee2 | -14.21884 | -45.46346 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04003fc9-685a-3403-9187-ea5dbc500d0b | -6.78583 | -47.5979 | 2025-05-06 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91f3fe23-981c-3839-853c-e21c6f6c1e2d | -10.98325 | -44.43408 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f55d3075-7855-35e9-b927-00ffd1f14a8d | -14.21157 | -45.46601 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b03733e6-d26b-3fdb-bfcc-fc7779710185 | -10.98213 | -44.44136 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a5a711a-2df5-347f-b006-a324d55ba1d1 | -14.21829 | -45.4671 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8be5c67-5eed-3815-b029-30490f5d7b90 | -10.98381 | -44.43044 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 451d939f-99bd-3634-badb-24792c58a87e | -14.23059 | -45.45415 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c19ef0b7-3661-36e3-9cec-cd2bab2c29c8 | -14.2099 | -45.47692 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 847cb5f9-2d77-3e79-b9cc-75e9beda704c | -10.99172 | -44.44658 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bc45416-53e8-3f90-901a-a4d3728fabf6 | -8.19963 | -46.76196 | 2025-05-06 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93839db5-a94b-376e-ab08-16b428065e9d | -10.97987 | -44.43355 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e9f25cb-5fb2-30cd-a72b-6b70a9b48747 | -14.23565 | -45.46616 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1fd4dc8-27f9-3d06-a030-365569a037f0 | -14.22892 | -45.46508 | 2025-05-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2b088f9-c211-3545-be9d-51c1c390faab | -10.97875 | -44.44084 | 2025-05-06 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e968efb8-1946-3d36-b09f-b63014aaec8b | -14.50558 | -46.68083 | 2025-05-06 04:23:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58246ebe-6196-3aa2-9d4d-449c77ed2aeb | -15.56974 | -47.8548 | 2025-05-06 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 733cea8e-f3ed-3054-8812-ff5866ce9969 | -15.08016 | -48.94627 | 2025-05-06 04:23:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93ff391f-a543-34e6-9f0e-eedecbd1e8fb | -15.60066 | -41.7929 | 2025-05-06 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4e504a57-83fc-3533-aba1-5ebe68672700 | -15.59662 | -41.79244 | 2025-05-06 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1d4d00df-cd2e-3c14-bc1f-0a8aeb7b3acf | -15.83173 | -46.57775 | 2025-05-06 04:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9477b3d6-1ae6-384b-898e-d20c36eebd94 | -16.93419 | -44.80872 | 2025-05-06 04:23:00 | NPP-375D | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ce59011-1c25-3467-821b-8b5d960d8ee6 | -17.09626 | -43.80337 | 2025-05-06 04:23:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc2db368-52cb-30b2-8085-2e8230b7dc92 | -15.59937 | -41.79461 | 2025-05-06 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 25e2ea7b-e0e4-3415-a17d-bfa685e5dff9 | -15.51314 | -41.67033 | 2025-05-06 04:23:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e78692e9-9311-3ed4-b860-b69b950da23c | -19.53147 | -43.91953 | 2025-05-06 04:23:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0323328-b59f-3fc0-a049-274b337cfc36 | -19.68012 | -45.37906 | 2025-05-06 04:23:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8f82a5d-5c30-3c9a-9944-88197e1b12bd | -17.781 | -42.8118 | 2025-05-06 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd6509de-7cb0-35c9-acb3-bff13cf8a8b4 | -19.57134 | -49.68507 | 2025-05-06 04:23:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 877c4e9b-d373-3eaf-a9b6-6eec66995cff | -18.60533 | -46.99603 | 2025-05-06 04:23:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eb6ab11-ef3b-3239-949e-9e26bb72726c | -17.15106 | -54.01426 | 2025-05-06 04:23:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3913b74c-86fc-339d-a0f0-834f7fc625fe | -20.05862 | -49.37395 | 2025-05-06 04:23:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0da07cd7-7990-393b-b3ce-98772b718824 | -16.82586 | -46.81546 | 2025-05-06 04:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)

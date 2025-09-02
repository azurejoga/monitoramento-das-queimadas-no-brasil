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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b979abc-c2b0-36af-b21e-598d48f760f5 | -12.6244 | -56.99862 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54903fe1-449e-344c-a495-64c3e1ea2438 | -9.95525 | -66.87065 | 2025-09-02 05:55:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cea7bb5-d548-3867-b1f7-1e0a6a0b044b | -12.92804 | -57.00467 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69d92ec4-c56c-3ece-b945-288d36246b8b | -12.91416 | -56.94128 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fdbf4d6-752e-39ea-b618-b6a395e12588 | -12.93125 | -56.95594 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ccc266a7-5b04-35fd-a2f5-8010b34cd8e0 | -12.92989 | -56.96802 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8a3c81e-1195-31ca-bcff-19d145f3c4ce | -12.90612 | -56.95259 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7955fcf-7370-3bdd-b301-60cf5d219326 | -12.91913 | -56.94164 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12356a1d-86c1-36c7-9e71-cac69a836992 | -12.62717 | -57.00085 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f87fddd-91fc-3f43-a563-edabb63017c6 | -12.92923 | -56.97389 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52b0994f-dc82-3955-bce5-ab2af7a5dc66 | -10.14595 | -68.95366 | 2025-09-02 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf7e209f-6054-3ab2-829a-b346b554a7ca | -12.93668 | -56.96869 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40659eab-bffc-3ecd-964e-28a41ee73c0d | -8.97675 | -65.96573 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8b8897-9eb5-35fb-8845-6ab8bd25c791 | -8.44655 | -70.13592 | 2025-09-02 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1a04449-e662-355d-b5c6-b7eb83243180 | -10.51939 | -69.23529 | 2025-09-02 05:55:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2e10110-8e67-3b66-b31f-d7e67e1680e6 | -9.95467 | -66.87457 | 2025-09-02 05:55:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b982bce-e0ca-36f7-938d-200be2ac837c | -9.835 | -63.87199 | 2025-09-02 05:55:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea308306-d801-36f2-8de5-0247720e8c79 | -12.93601 | -56.97461 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d78f7a64-5c43-395b-97cd-6b6ab5afcacd | -12.92315 | -56.96706 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9d5d61b-8711-3f2f-8377-f18fcc7726f4 | -12.62783 | -56.99475 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa785b17-3a43-3902-86b8-200355000d45 | -10.24903 | -64.3217 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9210b29b-791b-3ea5-99a2-4221cf6255ce | -12.41901 | -63.90471 | 2025-09-02 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8df4bf7f-de53-3ef6-808e-1506143a79e4 | -12.93313 | -56.9566 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84c4e1cf-e97d-3ff3-b3bb-1bde09b767ad | -12.42275 | -63.9094 | 2025-09-02 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eed1f39-b2c6-35c2-bb89-76221c60b902 | -12.92192 | -56.99789 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67d18c61-2612-33de-a119-24932b446494 | -11.65321 | -57.35887 | 2025-09-02 05:55:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| abf184e1-a8be-3434-bb8f-e52fe4ce13bf | -3.72361 | -58.83937 | 2025-09-02 05:55:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a06d3cf-1dd0-358c-bbad-14a3b855ba71 | -10.14268 | -68.95287 | 2025-09-02 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cd44ffc-9058-3445-ba77-bb32d050e42a | -12.93123 | -56.97457 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63dca131-7073-395a-a98f-6db080d64a66 | -8.61681 | -69.49841 | 2025-09-02 05:55:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5afda9a-3363-35ff-b9bc-4c8ed7f48ebf | -8.97553 | -65.97409 | 2025-09-02 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a02f7de2-7e3c-35e3-804c-0b512efed0bc | -12.89936 | -56.9516 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a9b97da-0044-3ffd-9566-2a668ca2624a | -12.93734 | -56.96277 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01e5a419-5baa-33df-a143-1dd7b98ba1ba | -12.91706 | -56.96013 | 2025-09-02 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 254da1dd-2f6d-3373-b20a-3dd3148474f0 | -11.1033 | -44.6548 | 2025-09-02 06:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 5865ef7f-6188-3bf5-ac93-efb6fd585de9 | -11.1037 | -44.6315 | 2025-09-02 06:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c653bf97-afc3-39b0-ae40-043fa2f90e4e | -12.996 | -48.1022 | 2025-09-02 06:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 559bfea7-68f9-32f8-8d58-7bbe6d334430 | -7.5476 | -61.3437 | 2025-09-02 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 753c57fd-59cc-321d-88ee-445b8b778aa6 | -12.9768 | -48.1049 | 2025-09-02 06:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f5cd5b7c-5281-3885-8834-1fa37b7430da | -10.0623 | -48.0978 | 2025-09-02 06:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| edc1e4d0-7778-3a7a-ac77-fae1d07d6944 | -15.5666 | -48.3469 | 2025-09-02 06:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 946de501-814e-3d89-8071-4c68bdfe8eb8 | -15.5671 | -48.3244 | 2025-09-02 06:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f5e3dfeb-199a-31e0-a5cb-dab8a64c1054 | -10.0623 | -48.0978 | 2025-09-02 06:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f125500e-21a8-3268-b534-9eaef7de05e9 | -11.1033 | -44.6548 | 2025-09-02 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b1290707-bebe-36de-ae7a-f6201ffa60f6 | -15.5671 | -48.3244 | 2025-09-02 06:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 538b28c9-58fd-3707-9e0b-6724beb40f6b | -15.5661 | -48.3694 | 2025-09-02 06:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| a2aba309-b3d3-3a72-86dd-5a479dd68160 | -7.9912 | -46.473 | 2025-09-02 06:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d2017fd0-d675-310b-8e11-26c2642b0e36 | -15.5666 | -48.3469 | 2025-09-02 06:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 52405b51-4a02-36af-947c-d6a0ad37057d | -11.1037 | -44.6315 | 2025-09-02 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b07fcaab-5a8a-33ed-aadb-5b72701c5d4c | -7.5476 | -61.3437 | 2025-09-02 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 242ea0a0-8e97-3c53-b896-71bbe5a33376 | -3.22616 | -47.12894 | 2025-09-02 06:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 45f4cb8f-d15e-355e-b24a-b5fa6be12ce7 | -4.30576 | -48.09581 | 2025-09-02 06:12:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 39132d41-efaf-3afc-98bd-468785963669 | -5.69479 | -45.94529 | 2025-09-02 06:12:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a8291b38-9aee-30eb-9ce1-05545160117c | -6.98315 | -43.22509 | 2025-09-02 06:12:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 96966192-6d44-341f-9968-d1b0910da532 | -6.17326 | -47.27729 | 2025-09-02 06:12:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4123c77a-c585-3013-8246-42da5094e92e | -6.26789 | -44.51065 | 2025-09-02 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 624cb00f-6e50-37a9-807f-71ef4a9978d2 | -3.22786 | -47.11709 | 2025-09-02 06:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| efa325eb-321b-3bee-8990-43cc6b846869 | -6.87141 | -45.55452 | 2025-09-02 06:12:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b05241c6-9636-3987-9b7b-9ea008783880 | -3.78742 | -47.56427 | 2025-09-02 06:12:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0be1719f-08a1-30a5-9ab7-9a4526af6612 | -11.65264 | -52.19735 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 2ad0562e-426e-3997-a03c-449d9f7616b0 | -11.67156 | -52.1911 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1ce0ae91-3ddf-3044-b705-dbab2dec0471 | -10.05001 | -48.08024 | 2025-09-02 06:14:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d3d983e3-9250-3f02-a27c-ab629eb2493a | -9.76026 | -46.92613 | 2025-09-02 06:14:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 44127db6-eeb0-36d7-827c-e5d6513ea476 | -11.66143 | -52.19869 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 955db748-f505-30fe-9e8f-f03bccddf0f7 | -11.84346 | -51.46671 | 2025-09-02 06:14:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| efe384c8-6d29-3211-ac80-6685b9779e0f | -13.71851 | -46.93052 | 2025-09-02 06:14:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 74310d78-0853-3fa7-81a5-47bbe3e295b3 | -11.65664 | -52.17059 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 9736cb61-ee6b-3843-89e6-f0f4d5db91e5 | -14.75884 | -48.14848 | 2025-09-02 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 27efac3f-01cb-37e8-ac4b-d844e083a182 | -9.83416 | -48.30927 | 2025-09-02 06:14:00 | AQUA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f383790e-4ac0-3d3f-87ee-5737d82d948d | -11.65131 | -52.20627 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3570f734-1217-3c6d-879d-38b7dfdcd4a5 | -11.64518 | -52.1871 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d49c8124-dda8-3c95-8ceb-fd73371744ab | -11.66277 | -52.18977 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| a527a23d-fbf6-3a90-8ffd-a54211dbda5e | -11.79793 | -46.39727 | 2025-09-02 06:14:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 04ffc84c-1006-3260-a834-d06d9ec92776 | -12.98911 | -48.09109 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| ef7c5209-60c1-3ddb-8953-732681dfc19a | -6.77166 | -52.80721 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 922bb930-8177-3c0e-ae55-976e584d161e | -7.97523 | -46.46665 | 2025-09-02 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ad88e372-3cdf-38bf-9c89-ff98bb0e49fe | -6.79871 | -52.81128 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f7b7a881-e920-34f5-9a8c-d95118c80ca5 | -14.61419 | -48.0248 | 2025-09-02 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c9e039dd-4970-3323-8565-ce79cfabfe1a | -13.47135 | -46.91673 | 2025-09-02 06:14:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 79d7e971-06db-3e21-9127-6a5c254cd272 | -11.05233 | -52.06372 | 2025-09-02 06:14:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e09cd0f-ad99-39c3-be08-8fbb5207f423 | -11.65397 | -52.18843 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d6851177-0f90-3a8d-8a66-7ed1c1f7bc5b | -7.68872 | -50.27507 | 2025-09-02 06:14:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 33a93784-8748-362e-a0c4-f09bfcb1e47d | -9.74135 | -48.96833 | 2025-09-02 06:14:00 | AQUA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4915556e-8c77-3fb1-8e36-d7ac57f42788 | -12.62147 | -48.17652 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 542769cc-4525-3572-ac3c-f0141ba607c2 | -11.66756 | -52.21786 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 853e6a1c-d45e-3b57-9b33-565e6218635a | -12.85695 | -48.05311 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b6a20ae4-72e2-35d0-9188-73a04484e8aa | -13.6891 | -46.9357 | 2025-09-02 06:14:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 699033ae-d9d9-31df-9160-a35c45bf0651 | -7.54702 | -61.33127 | 2025-09-02 06:14:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e1be9455-0825-3436-9c00-40c49147098d | -11.63873 | -52.04913 | 2025-09-02 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4452d3f2-ac67-3fd7-8b89-b477d2b9a822 | -9.61381 | -47.82828 | 2025-09-02 06:14:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2d888aad-3b51-3f9f-ace4-abecd434b27a | -9.91781 | -51.6217 | 2025-09-02 06:14:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8d2d5d02-a371-3d9a-82a3-c9236ea95645 | -11.46929 | -50.48509 | 2025-09-02 06:14:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 382982c6-ca57-3496-b7b4-49d6fe334658 | -12.61063 | -48.17477 | 2025-09-02 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a87cd127-5dc5-3d31-aa51-4b0cc5afb776 | -16.86061 | -49.56857 | 2025-09-02 06:14:00 | AQUA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5611f294-e4e9-3d22-a9d5-b891beaa24ad | -7.72878 | -50.25232 | 2025-09-02 06:14:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 161e3a9a-2a28-325a-91d5-af104b7a75ab | -7.92338 | -46.43649 | 2025-09-02 06:14:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 14cbe2a2-810b-3e60-976a-ac8a953e7b14 | -11.09043 | -44.62556 | 2025-09-02 06:14:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 864c304c-3b20-3eca-a83f-19af80016f0c | -14.59718 | -48.06825 | 2025-09-02 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| efd22f76-d339-3e19-8552-7ae1e68c9acc | -10.45509 | -49.06095 | 2025-09-02 06:14:00 | AQUA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0b0415b0-b871-3ce4-897e-d900b377840e | -15.14928 | -52.34284 | 2025-09-02 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |


[Clique aqui para ver as próximas entradas](README86.md)

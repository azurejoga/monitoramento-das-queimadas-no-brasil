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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d8b062c-90d1-3657-a9af-dc712be49e52 | -5.74273 | -42.81419 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 2bb40974-70e2-3ad8-b1d9-926a4773bb6c | -6.73897 | -43.36869 | 2025-09-29 05:38:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 8.4 |
| dc452bad-a6c0-31e1-b8de-eb66f225bc3f | -5.23805 | -45.35056 | 2025-09-29 05:38:00 | AQUA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3fc9d5d5-d1f3-303b-adfd-81f79e14f43f | -8.28881 | -45.53093 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 68ca1ae6-d786-3a0d-817d-f6c898c69592 | -9.31093 | -45.68346 | 2025-09-29 05:38:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cbf6ebdf-bf71-319d-9846-11134db22fdf | -6.82876 | -44.83072 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d297761a-871f-3c9e-8935-385b7f13d15c | -9.30894 | -45.69563 | 2025-09-29 05:38:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 158bf197-824e-3a2b-87ea-80fe009aaf4c | -9.305 | -45.71973 | 2025-09-29 05:38:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a16ff1d0-579d-35d4-b3da-85879f917cc3 | -5.74132 | -42.82342 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 4ef4b965-9308-3f80-be72-add9c6f28757 | -8.27209 | -45.50436 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a152d3d1-28a7-3ef0-9f22-d0842710d96d | -8.27403 | -45.49218 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 904b2b03-5cf5-3558-a294-43db38eec3eb | -3.09514 | -47.00131 | 2025-09-29 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 75d400ac-6507-37a7-9efe-ac432de960a9 | -5.95998 | -43.2728 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1b3f1955-011d-3725-af7d-fa3971b088ee | -4.29136 | -48.26319 | 2025-09-29 05:38:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 9960198c-594b-30ec-a1a7-970bf99b51a4 | -4.24691 | -46.95043 | 2025-09-29 05:38:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b5bcc191-c92b-3523-95ae-38048f8342ce | -6.83052 | -44.81937 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0fccbcb1-8f62-3505-9c0b-67d81bc34b71 | -8.28243 | -45.50512 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4d0c6da3-67ed-370e-a397-817ce3095c01 | -5.82198 | -42.78399 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d9dbe24b-dc13-3932-b219-5968af8d7147 | -5.71895 | -42.84869 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 978a9342-3f54-3bbe-af2e-a0faffed7ad4 | -7.22624 | -44.78536 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| e153d83f-d57d-3b0d-b3a1-da10b5803de5 | -6.73747 | -43.37836 | 2025-09-29 05:38:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 21fa17af-928b-34bf-92db-2d10f787a1f4 | -6.5667 | -43.40856 | 2025-09-29 05:38:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b6402e97-afad-3357-bafe-9be237318d63 | -7.22659 | -44.77855 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9329949b-b22f-3a5c-874d-0f2c1a26dcb2 | -3.09326 | -46.99598 | 2025-09-29 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| f5730217-967f-355c-bff7-390f3487fda3 | -5.82056 | -42.7933 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| c457bc7e-208b-3bb1-921b-f5d8dd1c20e6 | -9.76724 | -46.18365 | 2025-09-29 05:38:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4f444657-2c40-3d00-890e-025b18684acc | -2.57492 | -48.40292 | 2025-09-29 05:38:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 055305a2-a76e-321e-9d42-bc49941b986f | -7.21497 | -44.78833 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a060a6e4-9c90-3029-bbfc-5cb79fc6f127 | -8.29455 | -45.4945 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 293.7 |
| 39ae6535-a0d4-3e40-a73d-8085d3cc7a73 | -6.31344 | -43.44077 | 2025-09-29 05:38:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 98b7df18-2724-3061-bd36-c4df48d5c7d6 | -3.10304 | -47.01655 | 2025-09-29 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1219bdca-ab8c-3bd0-9033-d58985e70e8b | -5.81295 | -42.78274 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ef9fb7d1-de9e-35ba-bb1d-c336fcfaae25 | -5.71751 | -42.8581 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 221813a3-d050-3639-aecb-976ce81db3ac | -5.73701 | -42.67089 | 2025-09-29 05:38:00 | AQUA_M-M | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 91e7e4c2-0660-378a-b4a3-d57395df6932 | -5.70989 | -42.8474 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 362e7768-1bf3-30be-a163-09ebf3c12564 | -6.46676 | -42.91614 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7ad70c4d-fd44-33c1-8d0c-049a427a9610 | -3.1059 | -46.99768 | 2025-09-29 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 02e8f40b-8e2b-3bfa-a901-3cb105b6c8f4 | -5.68701 | -42.63807 | 2025-09-29 05:38:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 418575f5-fc41-3940-9b89-93633e32f6b4 | -6.3027 | -43.44913 | 2025-09-29 05:38:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f912775b-5c2e-334c-83d8-57f22ff70674 | -7.58247 | -44.80141 | 2025-09-29 05:38:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ae0e77a2-ea22-384d-a9d6-aa49825dec1d | -8.29639 | -45.48289 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| be5f4be7-9b1b-3e7f-a5eb-cb50e6b12345 | -9.77181 | -46.19117 | 2025-09-29 05:38:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f585afb0-9e7e-307b-a92f-5979b7c6ffb8 | -6.30421 | -43.43931 | 2025-09-29 05:38:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 82ba1f2e-f7fc-3c2c-b812-e71e75b9fbd3 | -7.81357 | -46.9857 | 2025-09-29 05:38:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 85d9ec4b-b4c2-3313-9972-97956075596f | -6.07471 | -42.46004 | 2025-09-29 05:38:00 | AQUA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c3f30bf7-3229-3a18-b2e2-80f338546379 | -8.29074 | -45.51865 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 513.4 |
| 2310e9bc-d4ed-33b2-ba85-2f59640a1f0d | -4.9336 | -45.58998 | 2025-09-29 05:38:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b7fd01cf-decb-3a1d-9f13-a8649a6f10f5 | -5.6884 | -42.6289 | 2025-09-29 05:38:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2c084734-fedc-3b6f-8a72-5df4a978fe7e | -9.04797 | -46.70514 | 2025-09-29 05:38:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1800e545-77ba-3ee4-8ef8-7bcbe7aadbeb | -7.80615 | -46.88855 | 2025-09-29 05:38:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ff7f6e66-0f77-3f6e-ab5f-f4accd9639a0 | -6.57439 | -43.41974 | 2025-09-29 05:38:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8d50604e-aa2e-38f6-95c5-4bf8a76c1de5 | -7.80717 | -46.89769 | 2025-09-29 05:38:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c6f74291-448c-3d47-af9b-37033d39a71f | -5.9042 | -43.70001 | 2025-09-29 05:38:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9ede5d35-ed30-3376-9290-d12a2be450cf | -6.74923 | -44.74322 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5ed95616-5809-3a4c-9c17-92717fe327dc | -7.80964 | -46.88221 | 2025-09-29 05:38:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e41e7d36-0626-36fe-85fc-39ababd189f5 | -8.28046 | -45.51755 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 710434c6-3fc1-3d17-b84a-2043c8951d79 | -4.39923 | -44.08254 | 2025-09-29 05:38:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bcf37af3-276e-3f2f-97a4-d5f2681f3e1f | -8.27017 | -45.51646 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 5dc5ff9f-7ccd-308b-a66c-c79317ed36ba | -4.71357 | -41.98952 | 2025-09-29 05:38:00 | AQUA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 152cb03f-ddfe-3e6a-ad3b-be782fce9ad0 | -4.71493 | -41.98057 | 2025-09-29 05:38:00 | AQUA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| bddcb492-0b14-3299-be27-2e930115cc83 | -7.21672 | -44.77703 | 2025-09-29 05:38:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| c43d23f9-44c4-304f-86e2-48c030e44e97 | -8.29266 | -45.5065 | 2025-09-29 05:38:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 949.8 |
| fa5b3ce9-145d-3d44-ab10-55abbd3baac1 | -4.30597 | -48.07962 | 2025-09-29 05:38:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| f0cf06ef-c4ca-3813-b020-a972e3e082af | -13.38101 | -48.16103 | 2025-09-29 05:40:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 2fbbad1d-e0d2-3fc3-b782-ccd21b5dcf96 | -15.86376 | -46.21524 | 2025-09-29 05:40:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 139c7f8d-6413-3509-811b-7f164e4536fc | -14.52078 | -48.39513 | 2025-09-29 05:40:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| aa2a3546-6105-3906-bf56-126449b6a329 | -19.74863 | -45.98475 | 2025-09-29 05:40:00 | AQUA_M-M | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9f408c58-1f7b-3767-8d4a-691c043f9f6a | -10.79537 | -46.68527 | 2025-09-29 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1cfc963f-6146-3986-a74e-931995fb1fc9 | -16.24488 | -42.2075 | 2025-09-29 05:40:00 | AQUA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 014b2c67-8cdf-3002-8d24-0ac54eb4ad0c | -11.93881 | -46.53676 | 2025-09-29 05:40:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b9c4a6bb-da60-372b-814f-5c8b023429e2 | -13.83365 | -47.47765 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f95ac133-1a75-32c8-a276-9a7ef4f89b92 | -15.25241 | -48.76626 | 2025-09-29 05:40:00 | AQUA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 1fad29c4-ec86-3f5e-9d61-94a2e44fd3ce | -11.26842 | -47.19429 | 2025-09-29 05:40:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cdfa4a18-4c84-3dbb-8ccf-b8b1047c0195 | -20.05489 | -41.33973 | 2025-09-29 05:40:00 | AQUA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 22b40621-30bb-3d55-8c36-f45fbe6a3c30 | -13.76005 | -47.90652 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e9688283-01d1-3249-8ea3-b03adfd80a2a | -11.44533 | -44.98373 | 2025-09-29 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 53619bfe-0980-3176-b9d0-2b9389899741 | -15.18766 | -48.48093 | 2025-09-29 05:40:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7d58dff7-b1a1-309b-83e2-f126cbdcad72 | -12.7936 | -47.7457 | 2025-09-29 05:40:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 262b71ee-915e-36b0-858f-76e9e0065b92 | -13.63267 | -48.04634 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3f1a08c2-04d6-332e-8ef8-45261f5b5e7a | -13.5647 | -47.30291 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0af2885d-29f8-30ea-9cd1-b0eba9ed12b2 | -12.94935 | -45.16607 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 64ff6fa5-8920-302f-a945-1311df971056 | -11.43724 | -45.0354 | 2025-09-29 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4ab0b167-b1ac-353d-bd8c-3a61ea8771fb | -16.49213 | -46.03062 | 2025-09-29 05:40:00 | AQUA_M-M | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0297b5e5-2ed0-3fc9-8177-529d799e232c | -10.40089 | -48.15164 | 2025-09-29 05:40:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4c35330d-8da0-36b4-9575-b7d46763155c | -12.57672 | -41.29083 | 2025-09-29 05:40:00 | AQUA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 6070e385-094f-3771-99b1-546007785ec1 | -13.77871 | -47.8642 | 2025-09-29 05:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3942fe07-5e6c-3621-9a9f-ef1ed53f28c6 | -11.8302 | -51.7971 | 2025-09-29 05:40:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 5fea1d21-2b53-3d23-b29e-c89ce4b3a50e | -15.46754 | -47.92532 | 2025-09-29 05:40:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 173447ef-fb8d-3911-89c5-87b64c7ad1e7 | -12.70143 | -46.89312 | 2025-09-29 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 16ea8a7e-661b-3e7b-8a9d-72492a5af24e | -12.9603 | -45.1574 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e6151a0d-744e-3047-a573-dfe23f6b2b78 | -12.58716 | -41.2826 | 2025-09-29 05:40:00 | AQUA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| a692d0ce-1596-343f-a489-2dedea2225b2 | -17.74195 | -48.76226 | 2025-09-29 05:40:00 | AQUA_M-M | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6398b040-9a89-39a9-8718-a7bbbb35c5b9 | -11.4002 | -44.90318 | 2025-09-29 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0349acc3-ce74-33bf-89c3-c939fd09580e | -15.04119 | -46.96929 | 2025-09-29 05:40:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a5c84ef3-0324-3d62-bc41-ff4a8c833533 | -15.16372 | -46.41274 | 2025-09-29 05:40:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| abccce55-bf99-31aa-acd8-6a2022bc8ddc | -11.71709 | -44.42581 | 2025-09-29 05:40:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 69b65f72-cb36-31bf-bd47-1cc783df8134 | -20.87968 | -45.54791 | 2025-09-29 05:40:00 | AQUA_M-M | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 4ab00cd6-a91d-3384-be94-33ec7c63ffc6 | -11.94071 | -48.00257 | 2025-09-29 05:40:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| e9d1ab39-8642-335c-ae54-187726e51696 | -11.27081 | -47.18032 | 2025-09-29 05:40:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 87e0b5b4-4112-38d7-a4bb-7267314baf8e | -10.38861 | -48.151 | 2025-09-29 05:40:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |


[Clique aqui para ver as próximas entradas](README80.md)

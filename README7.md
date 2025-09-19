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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d99d8ac7-5146-3301-9e57-e8603bcfaed1 | -9.14319 | -44.86204 | 2025-09-19 03:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ec73c7e-c71c-3325-b208-f814109c7604 | -9.51696 | -43.06653 | 2025-09-19 03:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e42cea56-e4b9-33bd-915b-efc3e2ef07f4 | -16.30935 | -43.11263 | 2025-09-19 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f67f7115-b8d9-33bb-871f-9c83d999e34e | -15.52865 | -41.43365 | 2025-09-19 03:34:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 735b53ee-556e-3acf-bb4b-fec2a5ba5b44 | -12.62132 | -45.06802 | 2025-09-19 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62a540a1-4877-3427-b181-5fb1c8680390 | -15.32387 | -42.0544 | 2025-09-19 03:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b5c2e862-88be-379b-b653-6fbf4eb17364 | -11.51162 | -40.64195 | 2025-09-19 03:34:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f523ba67-b777-3e38-b234-27e2a4fd8b37 | -10.37409 | -42.45901 | 2025-09-19 03:34:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d38f7fa1-2cfe-3c96-af91-cdd401f51de1 | -9.18617 | -45.303 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8a2bba3-0015-3bd3-ae69-db8a23c14156 | -14.58693 | -45.17829 | 2025-09-19 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 327d890e-3fdf-39f8-960c-d5511942589b | -9.18508 | -45.32665 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68b3693b-dd2b-3dd8-8a9d-26305bca6c70 | -13.6703 | -44.22565 | 2025-09-19 03:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4bc4ef4-7177-3857-a69d-3b0c962cdf7e | -9.14438 | -44.85602 | 2025-09-19 03:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2062ca37-5a6c-37c5-83b8-a79fb4de04f5 | -12.34976 | -47.05888 | 2025-09-19 03:34:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef7899bc-fa65-3b23-9813-6dd0d92e6818 | -11.98851 | -43.37855 | 2025-09-19 03:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed3a88c9-34ee-335e-aa7c-16b7d1a8f0a2 | -15.32865 | -42.05563 | 2025-09-19 03:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 3201f0ef-c36d-3433-941e-11602fa1e5fc | -12.09344 | -44.80904 | 2025-09-19 03:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1045d656-1a37-32cc-977e-9cbaf9d2cbac | -11.18177 | -45.37489 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c3c396b-7856-3cf1-aef1-c348591948bb | -11.9298 | -38.33257 | 2025-09-19 03:34:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d7bb5bf3-64fa-307b-b66b-dc5bbc76f7a6 | -9.18508 | -45.30872 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 148d66b5-bc2d-3748-9ee6-4d16f0cee367 | -14.12732 | -44.59464 | 2025-09-19 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58a00039-9c6a-3e29-9741-7407861c0938 | -10.91601 | -45.65838 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60dfca67-78d8-3057-93ea-abef2bdcc44d | -10.10148 | -40.93007 | 2025-09-19 03:34:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0b6582f7-3827-3b07-99f0-033eca88eb12 | -13.98406 | -44.99965 | 2025-09-19 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56843a2e-3685-3e40-a9a2-c70604a2f138 | -10.919 | -45.65248 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d0c12b7-b7d1-3337-a2d6-8677aa8ecf65 | -13.98497 | -44.99528 | 2025-09-19 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b47873e-ed2f-3ead-90f6-dfc7edf2422a | -12.09754 | -44.85184 | 2025-09-19 03:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec6ed8c7-2ecd-3efd-8bae-cbbc80f7ba5f | -13.12531 | -41.05446 | 2025-09-19 03:34:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6ec860e3-4939-3d80-a41e-8ed8ba889aa7 | -15.44821 | -45.4495 | 2025-09-19 03:34:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2ed1803-2041-3b15-9ebb-946604de037b | -12.69253 | -38.58837 | 2025-09-19 03:34:00 | NPP-375D | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2ec18e0-2754-3031-8f53-620e822c80e5 | -9.17631 | -45.31874 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 73d2fe34-2e95-3c5d-9456-786b52b41023 | -11.50612 | -43.61887 | 2025-09-19 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc551193-4c9a-3813-9735-d6e6495d94ec | -9.1796 | -45.31963 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5c2ccab1-c322-3caa-900b-05597a07be34 | -14.61016 | -41.04702 | 2025-09-19 03:34:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 12db191e-539f-34c2-ae0c-fc08d279e429 | -13.98187 | -44.9802 | 2025-09-19 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17da64b4-7e28-3563-9a42-ccc47bfbacaa | -9.51772 | -43.06257 | 2025-09-19 03:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8b1d591b-a27e-3227-981b-0b08484710dd | -10.91829 | -45.64729 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e483f1b4-4f98-3af2-9742-0e7f64955c11 | -14.69172 | -43.9857 | 2025-09-19 03:34:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bba8374b-e48e-3668-a923-9828f17a904e | -9.18074 | -45.33146 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2e0b834e-099a-38a3-bf8f-808ae9539abb | -13.67062 | -44.22392 | 2025-09-19 03:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce576a05-95b4-3e78-847b-6e430ba41ebe | -11.41594 | -41.4087 | 2025-09-19 03:34:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 091f949d-aabd-3f67-8d7b-9c491b9a37cc | -9.18727 | -45.29729 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8e2edb8-ed35-3c88-8c68-a1ebb3e5b7a0 | -13.66487 | -44.22286 | 2025-09-19 03:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb71bc79-8950-3779-b93d-5d3aded55a2a | -13.98089 | -44.98492 | 2025-09-19 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec2af0d1-087f-3615-84f2-2bcd4acab184 | -14.2543 | -44.38708 | 2025-09-19 03:34:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07481b39-05b4-3484-91c1-8d7deae4a596 | -9.184 | -45.31441 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cfe67c90-0a59-3f64-a5e3-4597790a8d00 | -14.93252 | -40.71075 | 2025-09-19 03:34:00 | NPP-375D | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 85c4dda7-2fd3-3a27-b7fa-f2c680b774bd | -9.18411 | -45.29684 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e2a8dc8-c084-34d6-9be3-5ffc1498bbcd | -11.45509 | -43.54531 | 2025-09-19 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dafdc904-6dc6-3ce6-821d-2786fe1cadb8 | -11.43515 | -40.65861 | 2025-09-19 03:34:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 74fc703a-1318-3275-af89-3e479b5df885 | -15.44225 | -45.44814 | 2025-09-19 03:34:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04d9dc03-f71e-3c51-af7b-c51bb949cdc4 | -9.16861 | -45.3231 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c06cdb4-29d1-3979-bed6-86a315a96f55 | -15.4447 | -45.44611 | 2025-09-19 03:34:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f8f8cbc-2f13-3221-8a81-98cbbc44a269 | -9.18732 | -45.3153 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c96d9f6a-50e1-313e-a8d5-0d7c62df57f6 | -12.34986 | -47.05231 | 2025-09-19 03:34:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0066927f-022b-3223-a43e-39dd59c63c86 | -10.36799 | -42.46146 | 2025-09-19 03:34:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f36d83a9-abe1-3f56-a12f-f302392fc15e | -16.11893 | -42.6239 | 2025-09-19 03:34:00 | NPP-375D | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9f0ab69-0a60-3f0b-bc7c-194b1576a247 | -9.18183 | -45.32578 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f57d69f6-8db1-3e74-9924-8a921a582613 | -10.36866 | -42.45794 | 2025-09-19 03:34:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 75b2cd2c-f2fd-3ead-8898-e1e8ca182ec3 | -9.1862 | -45.32099 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25bb7c6e-48c9-31ac-9ebd-3f07fd08316b | -11.92917 | -38.33615 | 2025-09-19 03:34:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 08a32c82-6cee-39fe-8724-c80cf93592a5 | -13.67115 | -44.22153 | 2025-09-19 03:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 077e4387-3ba1-3bde-b610-1493dba21a07 | -14.58095 | -45.17706 | 2025-09-19 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec2b2ec3-8a0c-36eb-95d5-4c64ad0f69e5 | -10.9168 | -45.66359 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2aa07e38-68e5-31a0-adfc-bf8ad8b6678f | -11.98779 | -43.38223 | 2025-09-19 03:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42abc2ae-82bd-3e9d-973a-91dd3e00336f | -17.22625 | -45.95533 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 898a88dc-fde4-3407-bab2-7c2c61e30074 | -17.06257 | -45.91539 | 2025-09-19 03:36:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e8533f0-1c50-3252-a1d8-245e838cedd2 | -20.78882 | -47.24273 | 2025-09-19 03:36:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5aae8189-6022-343f-b1bf-f8558bdd3615 | -19.82102 | -44.21627 | 2025-09-19 03:36:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e08d3af-60ef-32b2-83d5-7bf78c39dce4 | -18.64794 | -43.89732 | 2025-09-19 03:36:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f96190d-bba1-3642-ae42-d563421e5694 | -17.15912 | -44.78911 | 2025-09-19 03:36:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e115e65-2f88-3f51-8490-0069176a80f3 | -20.34641 | -48.79644 | 2025-09-19 03:36:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8c4ef7d-ff81-3746-8040-9122f11077bf | -18.04848 | -45.52312 | 2025-09-19 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b008208b-95ff-36f9-a9b6-ea763f0a4824 | -17.09018 | -43.34258 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ff4cfa7-2a9d-3d57-966e-bea5a6b06c7e | -17.21536 | -45.94798 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c898241-6312-3561-ba42-4bf1a960555e | -16.5139 | -43.54583 | 2025-09-19 03:36:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78f6f04f-fedd-3fba-9be7-10e38e43ac9b | -17.16383 | -44.79435 | 2025-09-19 03:36:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 983c1e6f-ed43-3fd5-a8ff-6b4f083a52bd | -19.95359 | -42.4202 | 2025-09-19 03:36:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e2253f6c-fded-3bed-b05e-9427373e12fb | -22.03971 | -45.58824 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 095fd456-e1a1-31ad-a1f9-42bb0a49eb11 | -20.20578 | -44.60888 | 2025-09-19 03:36:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9778930-1d95-3714-875d-d5f2ff351b07 | -17.08392 | -43.33132 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abb389ea-5f36-34be-a8ff-db1ee3f28c35 | -22.03889 | -45.59188 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ce458086-df53-398d-94f5-3691c47d91cb | -17.08628 | -43.34554 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71a83442-0e4f-33af-91a7-aad44132880a | -17.21634 | -45.94352 | 2025-09-19 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bda2664a-f831-3543-8178-e80accc35db9 | -21.35451 | -45.78593 | 2025-09-19 03:36:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36623def-f53b-3666-bc39-bcaef758633a | -22.04277 | -45.59054 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9db7302f-449b-3f68-b9dc-0029d2fab904 | -17.21733 | -40.93018 | 2025-09-19 03:36:00 | NPP-375D | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a6c9224f-6205-3d68-b5a9-306c848805e4 | -19.94908 | -42.41908 | 2025-09-19 03:36:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7f311ed9-d5f5-3699-926d-4a2ff2542b61 | -21.04714 | -48.4371 | 2025-09-19 03:36:00 | NPP-375D | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 726a66f9-4ee3-38b2-98a1-c914461dacbf | -17.08696 | -43.34226 | 2025-09-19 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fda9de68-c527-3961-b4b6-7e9525f8618b | -17.45377 | -44.7937 | 2025-09-19 03:36:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 183aa85a-dd5d-3d93-8a8e-0f4fa6067340 | -22.02064 | -42.20737 | 2025-09-19 03:36:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a7f837ec-51ec-3ef6-97f0-7c755ba04a73 | -18.04903 | -45.51674 | 2025-09-19 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea9e143f-39f2-3457-8919-16a1c87860f2 | -21.04577 | -48.44272 | 2025-09-19 03:36:00 | NPP-375D | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c86f52e-54a6-33fd-ba98-22aabe273bd8 | -22.04422 | -45.59304 | 2025-09-19 03:36:00 | NPP-375D | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c05a9ee9-8a8b-394d-b79b-c60032d13eb3 | -19.91763 | -44.14669 | 2025-09-19 03:36:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c27f0926-9993-3138-9355-b08f05d476be | -16.51368 | -43.54614 | 2025-09-19 03:36:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bd7dc2b-6a3b-393f-83e3-c304d56fe2b7 | -21.34909 | -45.78453 | 2025-09-19 03:36:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5d2d8083-9608-389b-b865-deee0bd43f39 | -19.92207 | -44.15082 | 2025-09-19 03:36:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 063be45f-a6a4-37f5-8c82-73536b7e47a6 | -20.7894 | -47.24348 | 2025-09-19 03:36:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README8.md)

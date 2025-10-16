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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a08a16a-6fca-3b8f-8bc6-67a8b1fcb6bb | -7.35415 | -43.86774 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 644bab7f-e202-337a-b973-c5d64af6532e | -11.43349 | -44.1606 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de22d559-1bf7-315d-a1a8-ca5f1945d15c | -13.65174 | -43.93256 | 2025-10-16 03:28:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93abe56c-d869-3e3a-988f-c5b617303772 | -10.65552 | -45.25636 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e6a056d3-de5c-3562-aef8-ab44eb8d20c9 | -7.4008 | -44.75136 | 2025-10-16 03:28:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 920d7b02-2089-38b6-bfc5-1d5a12104873 | -7.66369 | -42.38046 | 2025-10-16 03:28:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2cd1b516-6bd4-30e9-acab-ac881e316c80 | -10.04902 | -43.83152 | 2025-10-16 03:28:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5d540f0-9c62-3283-8b2f-b12104042338 | -9.71131 | -44.5223 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4cbe21e2-9fea-3b4a-be8a-a281e006608e | -12.83986 | -43.8171 | 2025-10-16 03:28:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 884ff5f7-8abb-342f-af34-7ce11c6cb94a | -8.24456 | -44.03353 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf26584e-cc66-35fe-801c-7e68b03a2a80 | -13.73255 | -44.23465 | 2025-10-16 03:28:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc51985a-bd64-3e84-83e4-e06a59cc579e | -8.45619 | -44.18637 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e5eb03bd-80f3-3b31-a560-4d257a9468be | -10.14019 | -44.54762 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cd1fabd-0079-3096-8698-e907e3df1f22 | -10.14696 | -44.54912 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 137b4632-6269-3b54-820e-0b3f07d46a4a | -10.6468 | -45.24029 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5047b608-d135-3264-85ab-34782865a62a | -8.29683 | -43.41069 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 428b70e3-570f-3479-9f5b-94c41554f718 | -10.52278 | -43.37386 | 2025-10-16 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95bbe94d-eb6a-3f4e-8162-1a47f84438c7 | -8.559 | -44.59495 | 2025-10-16 03:28:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db779697-035a-3e40-ab4a-a5f696906376 | -8.29122 | -43.43047 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 340a3fae-86e8-3438-802e-37b124b75527 | -9.71005 | -44.52859 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e5c55a48-d8b3-31f1-b8dd-84841377c047 | -8.18725 | -43.31996 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| f5bc978d-46df-3060-a349-bbf3a74092a5 | -8.24417 | -44.034 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4ee0bf9-6239-3830-85d4-583887c336d8 | -11.43444 | -44.16385 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 012952ab-e1ec-320a-8ac1-faa21b9c2ec7 | -7.481 | -42.74756 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f0355552-f8c8-3747-aaf9-1a216fefdf28 | -12.65087 | -41.25153 | 2025-10-16 03:28:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 805ab219-9073-32a2-b5bf-f25bffe9c282 | -9.15558 | -41.06589 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 5e3cd2fd-6cb7-32d9-b302-b128318622a4 | -10.83462 | -43.95466 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b87396e0-6578-33dd-93f1-2b57ac5179fd | -12.67747 | -43.43582 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36b41d3a-9c7a-39ec-88d7-4ab77864b747 | -9.55761 | -36.89747 | 2025-10-16 03:28:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 313baab6-de31-3766-94ed-0bde4aa1ba68 | -10.1482 | -44.54295 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1042855-7025-316f-ae5a-fe3c0b91e34c | -8.26496 | -43.36356 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7d9d1264-4105-3960-aa8a-b261f9ccc576 | -8.45489 | -44.19323 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bb483415-877b-336a-91c3-aac79af108ea | -7.35376 | -43.8672 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| c5b42c3c-d844-3ddc-b644-dd6686ac4a30 | -7.92726 | -44.13093 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 50f0350b-13fc-35f0-9bab-963c0b4d0dfc | -11.74209 | -44.22909 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b875e8f0-4bbb-3ff2-b86b-68522409efbe | -8.25389 | -44.09416 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34d592d7-86e0-3b89-93a4-8788249a4dea | -11.5753 | -44.06055 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3383ae4e-c0ed-3a14-9016-c4323a493656 | -10.69888 | -44.42695 | 2025-10-16 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c1cbb298-9ccc-38a0-a673-cf0a28781fac | -7.40794 | -44.75297 | 2025-10-16 03:28:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 88f80f46-e95e-3cbc-bae1-04608be66b6f | -7.53928 | -42.07096 | 2025-10-16 03:28:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 384914b1-7b6e-3450-b66b-8d4491130d28 | -10.70434 | -44.4344 | 2025-10-16 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| de45d789-c802-3966-97e2-0352257bb6dc | -11.47586 | -44.1523 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68fc45d6-0b02-37be-9307-0d47f48a16a3 | -8.46295 | -44.18815 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 94b7a6a3-98fe-384e-a7e4-341580e5617b | -7.11239 | -44.72075 | 2025-10-16 03:28:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9901822-1809-3d03-8323-9e83b6b222a5 | -10.81507 | -43.94448 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 314c9666-6b72-36b3-9af2-6b28a076e559 | -9.69076 | -44.51842 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ab5de2b-8249-3fca-92c9-a4e01bd7e364 | -7.47349 | -42.1513 | 2025-10-16 03:28:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cda68069-eb0a-313c-a1dc-80191ac72c23 | -10.50534 | -43.38605 | 2025-10-16 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| effe40fe-d170-363b-8d38-59dfcc0b500f | -7.93457 | -44.13199 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9a132db3-3d5e-3a55-9417-918bb6d01c21 | -13.63853 | -44.42195 | 2025-10-16 03:28:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba2072e5-dd88-3bc5-8f03-03c13134e33d | -7.57883 | -42.6923 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 99ac43b1-479c-372c-8d30-daceb35e39af | -8.44915 | -44.18449 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89342293-ff46-344b-841e-602923371559 | -8.24312 | -43.33583 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2dd5968a-eadf-3005-9bc0-26271a949932 | -9.6826 | -44.52362 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 550ade03-db70-3892-9eb1-da80099fa22f | -11.58303 | -44.08954 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 456698f9-7d69-3246-97e8-1b5f35891bf6 | -11.58521 | -44.07859 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 37ad7832-56cc-3066-b415-40769a355669 | -8.44788 | -44.19093 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8712b36b-d23a-31f5-90bd-80b59ed1d7eb | -13.89831 | -45.57088 | 2025-10-16 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8c32e04-8703-3b65-bc76-18b63eb44ec2 | -11.45168 | -44.1793 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e86b1869-3281-345d-8a89-9ab8048ec108 | -10.64999 | -45.24794 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aeb02c78-9336-32a3-a997-620381b3fdd8 | -12.83365 | -43.81573 | 2025-10-16 03:28:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2eeddbed-9f4c-3bec-9691-93ce6b204c26 | -11.45716 | -44.17731 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 250be365-cd34-3797-aadb-0a367da92eec | -12.67845 | -43.43109 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 628828a3-3e1f-3861-be89-3d2b2a026eff | -7.47897 | -42.75834 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 6d9e8855-5742-326a-8db2-e927ee84338d | -10.82156 | -43.94578 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bb8c7bb-129e-3dd4-9ad4-09c4855b241f | -11.42629 | -44.1301 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 859998af-b8d6-3052-a878-618f2e90dbe8 | -11.46938 | -44.15089 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5d30642-ffac-30f1-9932-33de7dce11e0 | -13.89913 | -45.57093 | 2025-10-16 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab943017-f119-31dd-9cd7-8bdfc8540c03 | -8.24335 | -44.03967 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 86668ae9-e857-3ee3-8d63-ead3453d946c | -13.65519 | -43.9347 | 2025-10-16 03:28:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9b81df24-8d7e-3713-bc20-c8835d86cd7a | -10.05323 | -43.84445 | 2025-10-16 03:28:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c900bee-7326-3572-abaa-7e5b69543f16 | -7.67494 | -42.56404 | 2025-10-16 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 12d94b49-f406-3c1a-a811-cd85b038cbaa | -7.64406 | -44.09177 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 252e7330-1727-3b3f-8c96-a0f17a82a336 | -11.43883 | -44.16755 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aa58f0a-45c7-3914-99d7-fe58a4af7666 | -9.55828 | -36.89356 | 2025-10-16 03:28:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c7daf6fb-3ddd-37a1-a52f-83fbed89862d | -10.61186 | -42.31532 | 2025-10-16 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 245d2e74-8cef-3424-b1a7-59ed7b766481 | -7.89441 | -42.96092 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad2124c2-71d8-3d73-8ade-7721705445ef | -7.9483 | -44.13483 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef6ad241-1bf7-314a-bd29-583b956c4b39 | -9.25866 | -45.27023 | 2025-10-16 03:28:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3a3fafc4-def8-3ec9-ba1f-2dc96252a2f1 | -10.6524 | -45.24862 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fd9aff92-4a9c-31b9-91c6-9bd3c6f63a41 | -12.65617 | -41.25273 | 2025-10-16 03:28:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b56ed0d2-7f26-3c2a-b549-7b624b931a47 | -10.1321 | -44.55268 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56fcdddd-d226-3c95-a42c-48ee9a3c17c7 | -7.4832 | -42.13346 | 2025-10-16 03:28:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf72e21f-81a4-3df9-af5c-54c8979e3bcd | -8.55495 | -44.59222 | 2025-10-16 03:28:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 297b560d-be5c-38d7-83af-153ec0f496b5 | -8.25148 | -44.10594 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27df97b3-000d-3d86-9d6a-040c43dd1016 | -8.20607 | -43.31707 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 947e7b11-0a24-30ba-b97d-63885e6044c1 | -11.43131 | -44.14576 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab25e477-90ed-324c-8eb5-8171422b38ad | -12.67303 | -43.42971 | 2025-10-16 03:28:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| af85cbdf-1ec5-3a47-aad2-fa6000811b93 | -10.64857 | -45.25463 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 11348c88-d5ed-3d95-b674-8157fd6f1160 | -8.23779 | -44.03204 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59806bfd-2410-3192-a996-2b29e36c37e1 | -9.68165 | -44.53091 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f01ced41-e4e3-36f0-b378-01f4dc2483cc | -7.33881 | -43.87138 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb0f5087-0d8b-3826-aa32-32ec3d48c8e8 | -7.54015 | -42.06621 | 2025-10-16 03:28:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c9049ea-aba9-30ed-a0c1-0e803ed16bf5 | -10.50689 | -43.38749 | 2025-10-16 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b306bea-ae04-3c88-8fe1-605fc679994a | -7.34569 | -43.87252 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 087a0212-8bb8-3d78-ba02-11b4cc59deca | -7.47797 | -42.76364 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| b5d1913b-26b7-3066-a245-573b414de88b | -11.05329 | -44.78484 | 2025-10-16 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9997baf-a415-3814-97a5-40dc0f5ffc29 | -10.52643 | -43.3788 | 2025-10-16 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef3e15f8-6583-3cc9-93d6-69d6115a855f | -9.71387 | -44.50953 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d765d9eb-0cc6-3df1-9733-6217afcea607 | -10.13205 | -44.58812 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README16.md)

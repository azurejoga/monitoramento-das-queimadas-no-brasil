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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 418ee8a7-114e-344f-976f-1eb8ab9d197d | -16.74562 | -43.98043 | 2025-10-10 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46d1a4f0-4edf-32f3-9056-37b41ba7fc01 | -15.33147 | -43.19361 | 2025-10-10 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 06260111-137d-37f7-9a3d-e8a18ef82710 | -12.63637 | -45.04914 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e535b917-55f0-337d-bcec-d5197c655d6a | -17.66638 | -44.45821 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d832d14a-ad3b-36a5-8612-221bc8a990c4 | -17.37809 | -46.67864 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec73ee84-ad56-3c89-900e-744153fe2574 | -14.67917 | -48.06231 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a26232c-c4d6-3e2f-a6c8-4f39b39ade04 | -13.34486 | -47.75132 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 14355869-7693-3291-ab91-fffeac1e5456 | -13.26601 | -48.02711 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ff81360-54a5-3bf1-ab7f-985cc760e130 | -17.66296 | -44.45759 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4035871-5ca9-300b-b882-105acba8c49a | -13.00844 | -47.90501 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69abfffd-ed38-318d-ac43-7da3d5471500 | -14.93455 | -46.75665 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e970e68e-e1a9-3a14-aaee-34ab011ca286 | -15.82746 | -43.77904 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2420de85-e412-34d6-943d-5bfac264d35e | -11.92734 | -41.52636 | 2025-10-10 04:02:00 | NOAA-20 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ba78a85-c12f-3239-81e0-0e017eb298f0 | -15.75089 | -43.66922 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdfea9cb-fa95-34f5-94d6-3b60145a393e | -12.47734 | -46.92699 | 2025-10-10 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1b317a5-e1c3-3ccd-bbe7-9e9234fd36e1 | -11.32148 | -47.52185 | 2025-10-10 04:02:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd8e2989-7fc5-3fc4-bea6-abc33e45a160 | -14.38766 | -45.9997 | 2025-10-10 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 416aee6c-28bb-324e-ab68-20dae893faf3 | -14.42595 | -48.00659 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e04672fa-c8c3-3cf5-a781-c0ab400bd122 | -15.91165 | -43.28868 | 2025-10-10 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 44b93d65-01d8-3921-80cd-c72835d5adf9 | -15.09172 | -46.58013 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0218193b-f753-3065-be4e-bdad309b13da | -16.63092 | -45.44231 | 2025-10-10 04:02:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a1590de-670e-3af5-8489-87b8f72a6750 | -16.68714 | -47.59551 | 2025-10-10 04:02:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 452a5628-7ecf-36ca-9851-42cf71cbde72 | -17.57652 | -47.16459 | 2025-10-10 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0286eade-de11-3984-b37b-3779410ad021 | -14.54583 | -47.00302 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f473ecc-b2a2-3527-892f-c40735c5d993 | -15.09291 | -46.59608 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eb4895e-0516-3000-ac87-e73ef4e89783 | -14.90019 | -46.8542 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48b25f88-f969-3884-8ac0-34640137e3fe | -12.22669 | -43.7946 | 2025-10-10 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35600198-0e37-3790-8bab-a51831cc71a4 | -15.91379 | -43.29672 | 2025-10-10 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04f2a1e1-9507-32c0-b4b7-dc03064b42c2 | -15.29222 | -46.18026 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bba0e41a-7b6c-3bf0-97b9-18865b43502c | -14.71603 | -45.18112 | 2025-10-10 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ff58d33-6a63-3171-b5fe-7857d78ce5a2 | -17.3884 | -45.06987 | 2025-10-10 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 379ef92e-0785-3dce-bb49-d0f6e1043740 | -13.25409 | -46.48354 | 2025-10-10 04:02:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 713dc376-6e22-36e8-ba99-2d48fa9c2efe | -14.94701 | -46.23933 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74f0012a-52e3-3598-85fb-2e1e19121de4 | -15.08715 | -46.60548 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6e3dec5-fd02-32d4-8a42-1fe49e8bd434 | -18.07717 | -44.47977 | 2025-10-10 04:02:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f602251-9759-340b-9c3b-1d4e857291bb | -13.35809 | -47.75285 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e27b3359-49e0-3655-8069-1b17a292b076 | -10.93747 | -42.84734 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 728b9e8b-c31b-38bb-b52c-8978e1dcab4b | -15.58055 | -44.79721 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b90211e2-d13a-302f-97df-0dd9ff9d3207 | -18.05606 | -44.47955 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fcb321a-ab4c-3e8b-b14a-40280674fe3c | -13.40995 | -47.25734 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0ada0a6-316f-327c-8458-0eda4e43a8b4 | -14.70807 | -47.44274 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83f07fe2-f237-3481-964e-8f38a31b2621 | -12.92336 | -45.05624 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0445f205-eda7-32ec-a071-e613da446c40 | -14.97371 | -41.68061 | 2025-10-10 04:02:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 57c7b85a-f157-3623-a4b3-5dbb43cc2474 | -14.2683 | -45.87952 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed6c13a3-1487-346a-8556-0b10740cad75 | -13.83116 | -45.79958 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 011fb4a9-f255-3372-8fb2-80d618cb00f3 | -13.32731 | -47.99372 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68c0de69-c004-3953-a740-c7c03d329f1f | -11.637 | -47.5286 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 612b0da1-0deb-3251-8d86-caeaf90203b7 | -13.37546 | -47.75637 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7767f1fb-e00f-3dd2-bdd7-e4e71c8ce337 | -17.08929 | -45.48272 | 2025-10-10 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6874a734-5907-3463-8547-686a3133d49f | -16.79673 | -47.5694 | 2025-10-10 04:02:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e8bbb31-3080-3dec-a645-c9cd3cba051b | -12.63104 | -45.0577 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3ac9b7a-5ac9-37c6-929f-ec6ed99db641 | -12.65888 | -43.42889 | 2025-10-10 04:02:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3fc77c3-9301-3fbe-9063-33339560da27 | -15.28127 | -46.153 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fcd6558-e4f2-31cb-9bc6-a46da2032897 | -16.17212 | -42.85601 | 2025-10-10 04:02:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b892e0ac-21ba-394c-bfa3-b2d6fd3a8d16 | -16.29937 | -47.15118 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2597ebbd-bb54-38c9-91af-6a98e42093c7 | -15.82065 | -43.77782 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 09dd8598-acfc-3f6b-a7d3-9c3d59456e0c | -12.10399 | -45.00254 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4ff108d-9dc4-384b-ae57-0fdb2c99a43b | -12.15026 | -47.91972 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62a89ff3-417c-3953-9b9c-006d341ed274 | -14.88836 | -48.2272 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3eab3215-0ade-338b-9dee-449f9b886dd8 | -13.8282 | -45.79401 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6565b6b2-bd99-37ea-a6b3-0824d03461ff | -17.92993 | -44.60227 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4e88867-4be6-3e03-9518-3b3334618480 | -13.41223 | -47.24445 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e169fcf-b6b6-3dd5-84f8-d2b539630afa | -16.73883 | -43.97911 | 2025-10-10 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f269d298-5cf4-35c7-ae51-18157dbb94e4 | -13.37569 | -47.20586 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7ecfb95-afb5-3a3d-b2a1-75acb124f089 | -11.72557 | -44.29807 | 2025-10-10 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79b5adfd-b51e-31ff-a1cc-f1fe6da26003 | -17.92877 | -45.02993 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee012d3d-d035-3aec-a6a2-6d5c974750e0 | -18.01825 | -45.01663 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2381a93f-0771-3eab-9218-0be8c4168104 | -13.26644 | -48.03411 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63914fd7-d323-3878-a62a-a623aff6d087 | -10.92935 | -42.85376 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5303674b-bc84-3db2-b604-ff0e48478e01 | -15.33207 | -43.18992 | 2025-10-10 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 824469c6-4687-374e-8026-6cffda5e5412 | -11.9762 | -45.20276 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1bb687a-0b06-30a2-a596-221d518eec93 | -14.88597 | -48.23987 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ebb67e6a-3285-3c3c-8e8a-d08afad98e1e | -15.42616 | -47.98915 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7543ce48-1016-389d-a748-774da9f334c6 | -16.43781 | -47.81406 | 2025-10-10 04:02:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c6be812-f7eb-31ec-99e6-c9ec9ed88226 | -13.80305 | -45.82467 | 2025-10-10 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f853f749-b29e-3685-9816-470d8eca34c9 | -16.68784 | -47.59172 | 2025-10-10 04:02:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dad9d99-48e3-3a70-8868-0bcc6d101d32 | -14.27006 | -45.91452 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6e3e6ecd-12ed-37d6-bda7-6602143093a0 | -13.84049 | -45.83652 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a764c279-6045-30da-9249-dcd1e319a26c | -13.26514 | -48.03172 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d82f3d56-b56d-311a-87d0-b15157d73209 | -14.26624 | -45.9138 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 94f3c1de-a240-327c-bfc4-bb225e1a4b51 | -15.39886 | -47.30941 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00180b7f-7271-3c1e-ad71-6cc2c46ebb3f | -15.39214 | -47.29995 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f66a29c-2573-353d-ab4d-03bcfcde9e34 | -13.31499 | -47.73931 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc64633a-59ce-3afd-8aa4-06b7e02928b5 | -15.23675 | -46.3799 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 50f20eeb-44fd-3052-9d55-78b9b3d45389 | -10.64267 | -44.41969 | 2025-10-10 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c52100e-a242-3881-9420-e15faa98eab2 | -10.77164 | -47.6092 | 2025-10-10 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfc54003-e19d-3c5d-81bc-38c34b0b1c2b | -13.84135 | -45.83159 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb9ad094-58d5-3f1f-9fb6-f7695dc67e4b | -17.35959 | -45.06857 | 2025-10-10 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6139d7c9-46d8-389b-841b-72a7f4e79e84 | -17.96187 | -45.00964 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bba5572a-1bec-3dfe-a933-eceb72218403 | -14.41737 | -48.34267 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 404b58d9-b7ad-330f-97ff-a5f846aaa43e | -18.069 | -44.97911 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4658f6d5-6cda-391e-917f-617117d1af3e | -15.46511 | -41.53509 | 2025-10-10 04:02:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7cecc1e3-5276-391d-8f25-63921f6af752 | -11.86263 | -44.91684 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e724eece-9ff6-33e4-8c0d-363563f86c32 | -15.09198 | -46.60122 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1bdf979f-3482-3bbc-bd74-6677127ff3e6 | -13.22979 | -47.61644 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2871f368-dfbd-30b7-b563-167226802b24 | -17.9322 | -45.00963 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e232a471-afcf-3bd3-a97e-8987d3611b2f | -17.39044 | -46.87552 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad080942-2770-3ca7-8af9-b68bc31c1ff8 | -13.06994 | -43.09104 | 2025-10-10 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f8b91955-614f-3964-a141-9ab233103a03 | -12.22444 | -43.78644 | 2025-10-10 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c289a8f-2b5d-3737-a4ff-e32021b9b1c9 | -12.72081 | -45.83346 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README28.md)

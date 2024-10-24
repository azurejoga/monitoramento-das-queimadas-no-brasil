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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fbcc039-f85d-312b-be16-0beb3f44438f | -12.42656 | -43.28162 | 2024-10-24 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 237bcd0f-bdc7-3491-9e99-8aa87b48d87f | -6.27508 | -42.08987 | 2024-10-24 04:34:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 45227720-aff6-33a7-b2ca-a82a159900e9 | -6.29272 | -43.37391 | 2024-10-24 04:34:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33614684-7790-3fe7-8353-756587d2bc52 | -6.28885 | -43.37332 | 2024-10-24 04:34:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd1cb668-c9ed-39fe-b5da-386c4f1a34f9 | -7.71989 | -43.76954 | 2024-10-24 04:34:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3f95d63d-079f-3060-9d36-4d716e8505a7 | -7.54651 | -43.19095 | 2024-10-24 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 97967e43-ea76-3a21-ad21-a6a8f78ce030 | -7.50253 | -42.91381 | 2024-10-24 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 545f4edb-086b-35e5-b13a-b5da4c991cdc | -7.06773 | -42.55565 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3debbbab-c000-33f8-a338-ef370e22a64f | -7.06719 | -42.55931 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cb2af536-19ed-3a3d-b310-fb5229cb7368 | -7.01799 | -43.14129 | 2024-10-24 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eebe821c-36df-36f6-ba19-e9ad82ba1810 | -7.56402 | -43.46212 | 2024-10-24 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed7310ab-07a2-3b07-b985-a610aa205c0b | -6.67511 | -43.04357 | 2024-10-24 04:34:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e2139b7-173a-3264-b856-696a79014c8b | -6.66217 | -43.04865 | 2024-10-24 04:34:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ce50b64-a9df-3dd2-a06e-7eee1372d711 | -7.71918 | -43.77439 | 2024-10-24 04:34:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 423e0107-f22b-3256-b986-96382e9609e4 | -9.12385 | -43.15018 | 2024-10-24 04:34:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b6b0f303-9914-3a29-9672-923dc46a4545 | -8.96939 | -42.98256 | 2024-10-24 04:34:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c42d83ae-6942-3e5c-94d6-518e38b6b29d | -9.34634 | -43.36756 | 2024-10-24 04:34:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9339b62d-d381-33f2-a37d-bea8f6b5128a | -9.64422 | -43.91144 | 2024-10-24 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 39935e96-cd24-3220-877f-650535229cee | -9.63706 | -43.9055 | 2024-10-24 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e2f4d3fd-b633-3cae-aa8f-de711a2191e9 | -9.641 | -43.90594 | 2024-10-24 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 745f6cde-1e6f-3de8-9814-bdd039b66be3 | -9.64494 | -43.90638 | 2024-10-24 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08c20cdf-6e2e-3f24-85c3-28b34426fdd7 | -10.61406 | -44.2761 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a2e4626-7943-316c-8ad4-b00054c2dc22 | -10.61162 | -44.26548 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c08ffd4-5c9b-3088-a365-d197cfdecb39 | -10.6109 | -44.27055 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0cfff31b-d1cd-3201-b168-958a8b44beb6 | -10.61018 | -44.27553 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cb48093a-55a9-39b7-836a-2ca101859ccf | -10.60946 | -44.28049 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 411f1d45-3f70-31bb-9679-3092bd1798ad | -10.60775 | -44.26485 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e7434ab-1f9b-367c-8543-fc942577b39a | -10.60702 | -44.26994 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b07b6eb3-5b46-3cd4-ae2f-fb5f3a9a7904 | -10.6063 | -44.27495 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cfb01a5e-938a-31b2-803b-5f076a74629e | -10.60558 | -44.27995 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fd3f334-14c8-3277-be3d-32c67ed8dd5d | -10.58158 | -44.28149 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| deac954a-0e93-3259-930f-0c510c596f57 | -10.58086 | -44.2865 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 99317dd2-8f25-341b-ab4e-cd69df78f642 | -10.58016 | -44.29145 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a02bae4-e134-30a1-a350-9d79ec041c65 | -10.57769 | -44.28094 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4dc7102-1fb3-3d23-b6f0-409c8f5bbb6e | -10.57698 | -44.28593 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dcf8aef4-3025-3a8c-b97b-cfeebf7753c8 | -10.57628 | -44.29087 | 2024-10-24 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cad9d336-e49e-319a-880b-a54a4dbb9d3f | -12.28622 | -43.83329 | 2024-10-24 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30665a7e-eaf4-3afc-989e-c1d6eeded122 | -12.13663 | -43.47623 | 2024-10-24 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8260c129-a69d-333f-ae0f-5cbbe6325575 | -12.07381 | -43.83776 | 2024-10-24 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee565a53-109a-3bde-8442-5754e75d91d2 | -11.99685 | -43.91545 | 2024-10-24 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 223afb8f-ff76-371d-bfe6-ae6b87125081 | -11.95103 | -44.16343 | 2024-10-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92fcd001-a70f-3a2d-b3f1-118f7623b7ed | -11.95056 | -44.16693 | 2024-10-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7791437e-f414-3228-a180-1dca667888fd | -11.94884 | -44.16277 | 2024-10-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 820aa00d-b722-30a2-9ad9-4ba81f99d1ff | -11.94835 | -44.16626 | 2024-10-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dabb3468-302b-3b1b-ab1c-8564c3935233 | -11.94705 | -44.16285 | 2024-10-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f83d5e0c-3c12-3ef8-a82e-eca43a6af087 | -11.91055 | -44.1749 | 2024-10-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e78c6f19-87f3-36a3-a916-31a963abbdc5 | -11.8838 | -44.71333 | 2024-10-24 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13c9d091-0f71-344d-a00e-31fc72c47964 | -11.77693 | -44.21169 | 2024-10-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89fa62bf-b5d1-3f5b-b5b4-ea00921a0bed | -11.77525 | -44.61832 | 2024-10-24 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5154c366-5943-3506-8cc6-8f5f29dfe87a | -10.87633 | -44.37976 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e22eaf1-382d-3a2b-b486-7e788934aafe | -13.51472 | -44.41305 | 2024-10-24 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0c4e290-4258-3651-a894-444335d94910 | -13.51072 | -44.41246 | 2024-10-24 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 415945b2-5825-306f-80f6-bf67d2f69e1e | -13.51023 | -44.41596 | 2024-10-24 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6ee5d19-8f28-3b33-ae9c-b17b8ed91f86 | -13.50223 | -44.4147 | 2024-10-24 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 138d37b0-9954-36ab-997b-762e860532ad | -13.4767 | -44.02719 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fd694a3-c1fd-3e25-b5f7-69833243c87e | -13.47584 | -44.02586 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e18d4171-2582-3c24-a49f-43e2585aa6e5 | -13.4355 | -44.35351 | 2024-10-24 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83b34eac-6f30-354e-a1d9-9301e0720de7 | -13.4329 | -44.35228 | 2024-10-24 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8bfe1af-173b-3ac6-912c-fc1e3bfdb39f | -13.43149 | -44.35286 | 2024-10-24 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b827a6e1-33ae-3013-b474-9178c4cd6ac0 | -13.36113 | -43.92902 | 2024-10-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bc2073a9-c58a-35fe-b1ec-676fa2adc407 | -13.3482 | -43.67846 | 2024-10-24 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2881332-d96d-3036-a45b-12dae05f0568 | -13.34768 | -43.6824 | 2024-10-24 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37e2ffb8-d4ec-3715-8a7c-21d4e2d86ac9 | -12.715 | -43.85651 | 2024-10-24 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bd7bb20-e5af-3ce0-bc79-6e3cb4ddb619 | -12.71089 | -43.85591 | 2024-10-24 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc0fa963-7940-377e-95b4-31ade3f432cb | -12.69549 | -43.84597 | 2024-10-24 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df85ccfe-315f-367d-9335-a5e64055309a | -12.6924 | -43.83783 | 2024-10-24 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32bf870f-e827-3c68-89f2-1a11efde969d | -12.69189 | -43.84159 | 2024-10-24 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b3983b4-9ee8-3a37-8959-ba3e395f1bf1 | -12.69138 | -43.84536 | 2024-10-24 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3c24ea19-9c9e-3125-b797-8f8256bde130 | -12.68829 | -43.83722 | 2024-10-24 04:34:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b87a27d7-026c-3d88-bbdc-c60aae5e2d5c | -12.68778 | -43.84099 | 2024-10-24 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2662edcf-86da-3279-8b8b-a7eb023b9ebe | -12.68727 | -43.84476 | 2024-10-24 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 75327a17-0fc1-3cd2-bcac-cd4b2e435c2b | -12.68676 | -43.84852 | 2024-10-24 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 054ec799-91ab-38f1-9635-cb2b6b1b45f0 | -12.68317 | -43.84415 | 2024-10-24 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bad7ce53-c608-3710-b96c-f64373e5f7b2 | -12.68266 | -43.8479 | 2024-10-24 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4ce69fce-8276-387c-8628-12809c529487 | -12.60045 | -44.18196 | 2024-10-24 04:34:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24f2af89-eb02-37a7-83af-07a01491a93d | -12.49146 | -43.37671 | 2024-10-24 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c58ea42-cffc-3573-a46d-7e1355ac35a2 | -12.49135 | -43.37732 | 2024-10-24 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df9ce87b-5b2f-332d-b3e0-0d292a5a9640 | -12.48722 | -43.37613 | 2024-10-24 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02e7583a-a14f-3377-b34c-bbf620b4c17a | -12.48712 | -43.37675 | 2024-10-24 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d66038b1-0200-3beb-9e2c-58dddff9d480 | -12.44686 | -43.74682 | 2024-10-24 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d11a8a80-5602-398f-a9f1-e7a749aa323b | -12.44535 | -43.75822 | 2024-10-24 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c28946f5-917e-3490-b09e-9b8257163935 | -6.41094 | -44.60539 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 999029f1-858d-3a25-819a-4f827e2b779a | -6.37006 | -44.70619 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0441fbaa-7f71-327f-934a-6105057dd875 | -6.25339 | -44.13271 | 2024-10-24 04:34:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f10f478b-5981-37e7-a5d3-8621b958c15b | -6.23733 | -44.06186 | 2024-10-24 04:34:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3640525-cae5-3e3e-bf2d-357d1eefcfbc | -6.19308 | -44.53682 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 277ebc41-a66a-3348-9925-9e969da53b66 | -6.19072 | -44.52783 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86c8d842-5f73-3c1d-8c43-d75b14bd9b8e | -6.18775 | -44.52291 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17323191-9c1f-3986-a572-5635e59ac6d0 | -6.07103 | -44.62608 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ebb0c279-4c84-364f-a913-87dfe6c977e8 | -6.06805 | -44.62143 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7179a471-1543-3747-900e-233889e04608 | -6.06743 | -44.62554 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5d95951b-9b21-33cd-81c4-b204ffcb22cd | -6.06681 | -44.62965 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c116c26-86d9-3ec4-b7c4-6a06c388be64 | -6.01756 | -44.86073 | 2024-10-24 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c00f19be-ec63-35dc-9afc-49e25131ea0e | -6.01696 | -44.86477 | 2024-10-24 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4b94cc8-82ac-32fd-9f1c-6a976f4574df | -6.01401 | -44.8602 | 2024-10-24 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccf17911-78fd-3ae0-9956-035e13376844 | -6.01098 | -44.52485 | 2024-10-24 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cfdfaa6e-5052-3d14-ab86-ee1fe64f2071 | -5.94837 | -44.88868 | 2024-10-24 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70279dc6-f1a9-3a88-b713-d1f9a7da2c02 | -5.93463 | -44.64071 | 2024-10-24 04:34:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17428586-42a6-332c-b0b9-be83ab8e5a26 | -5.93104 | -44.64018 | 2024-10-24 04:34:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4b402da-27c1-3929-817c-f4fb9ddea41d | -5.9303 | -44.11577 | 2024-10-24 04:34:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README41.md)

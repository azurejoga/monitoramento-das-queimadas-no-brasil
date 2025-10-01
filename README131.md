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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14246ce3-6062-3eb7-a14f-3bdc9d46f1f6 | -14.36134 | -47.14791 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 68d12f6e-883f-37ca-87e0-07a9e45a63b6 | -12.81909 | -56.55435 | 2025-10-01 05:12:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 615de8c2-3f92-3d6a-a8f2-ac9afe7437cc | -14.43778 | -46.35868 | 2025-10-01 05:12:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a23cc85-3507-3ac2-bf4d-f95d47bea78f | -14.88656 | -48.32404 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb2f1b18-c79f-37fd-83be-ae5f13583593 | -13.71046 | -48.6322 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 592e5bef-c6be-323d-afd1-49ad1817098b | -14.89371 | -48.11913 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1cf55bb4-22fd-3d63-936b-b005f8d83e74 | -13.77485 | -48.00918 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6516ff68-6d5d-3bae-8fd6-40a7f0450342 | -16.4005 | -47.03832 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0555dd1-f0c0-3eaa-8c44-02d3dc69e758 | -14.81563 | -59.70436 | 2025-10-01 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ab0805f-6aca-3e94-bbd7-cd4b6ab9aefd | -13.78283 | -47.99173 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0714087f-e6f2-3e95-ba7e-bc32581fbe72 | -14.39226 | -54.91016 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e40d478-d86d-3f62-8f44-606e4ea261f7 | -14.87244 | -56.446 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f2abb2f-8fa6-3ef4-a6e3-202e15346d17 | -14.61249 | -48.31047 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1271da6-2140-3529-ab57-2051c3425f78 | -14.68122 | -48.12604 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8463e44e-c3f8-347e-8b0f-64b888a0c72f | -13.73227 | -48.69367 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 688f86fe-3f2d-3403-84e4-8bdc0368978a | -15.28319 | -56.7952 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88828340-4d7e-3b0a-b622-c0e692c6bce4 | -16.0183 | -50.90464 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d060d5ee-0c72-3903-9430-dea7005bfa4d | -14.89689 | -48.11309 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0896726d-5d57-3153-81cb-3d4dbc030cdd | -15.30879 | -46.41517 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90de73e4-42f7-383b-a433-7af5945b739e | -15.8081 | -59.50729 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3210e0e-d2e1-37a7-b9e0-3447497107d4 | -14.18419 | -46.1181 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49104453-fad3-3704-954c-7fc67fb74702 | -15.0129 | -56.04366 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31eb192c-f773-334f-a202-e4971bd0a913 | -17.38595 | -47.1669 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5071433c-f873-3229-88ae-63a6d35a7d71 | -17.89661 | -57.58266 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 566d0c51-2457-3a53-bf38-a28fef14bd3f | -14.95659 | -46.88736 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 67e0ac1c-44da-37b9-a27d-77dc6487fa40 | -17.39936 | -47.16452 | 2025-10-01 05:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cf55a17-7375-3ac5-9945-3f430922ad35 | -13.81842 | -47.50093 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05561b61-24d5-3d96-9f57-2c5d463c5a11 | -13.975 | -44.88696 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acccd1aa-6167-31e8-a8e1-c063337bd907 | -13.9456 | -48.10816 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a2319c9-959e-332a-88ad-35223b5294a3 | -14.9019 | -48.12304 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a16eb077-8197-3eb1-84e9-02b0060c3e8c | -14.68788 | -48.12062 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce7f8a68-e0fe-3d0a-8c4c-286fe6a86d45 | -13.76585 | -48.40391 | 2025-10-01 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e0e1cad-1c7c-30fa-87b2-3f38f33f9b5b | -13.97195 | -44.89118 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 933108f2-8996-39a8-900f-24074f3ac8a2 | -14.90418 | -48.13386 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d00326af-dc5f-3a7f-93d7-122a101edf52 | -15.94509 | -48.13257 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 598de815-ada9-30db-b447-356f0fc3b9f9 | -16.02559 | -50.88628 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 475c396e-39ca-3032-bee2-9c968a629f55 | -18.71293 | -49.17048 | 2025-10-01 05:12:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6843678a-43a2-36aa-a72d-ffd2ecf3c6f0 | -14.43357 | -46.35801 | 2025-10-01 05:12:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 012709bd-e0c4-334b-ba21-00548cb5fba0 | -15.1745 | -49.07863 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e7858d5-7e2f-39ce-851e-af80dfeda68b | -14.14336 | -49.19773 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c381dc15-e941-353f-abe2-02fc81702d52 | -15.3396 | -56.95329 | 2025-10-01 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b55d6a63-223b-3668-9330-c72b6ef3c250 | -16.37791 | -47.06563 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f1abc89-2b19-3e80-ac64-6813c7d0a489 | -15.49265 | -45.92662 | 2025-10-01 05:12:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7676220b-3a60-3e7b-9430-16ea9fe1346d | -15.93894 | -48.12103 | 2025-10-01 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a72b5809-dfb9-3256-8db9-e5476157fea8 | -14.68285 | -45.28079 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3160167f-5e60-3256-b5b7-388206fd5a73 | -15.24694 | -49.72997 | 2025-10-01 05:12:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 589f22ce-7de1-393d-a2f5-7eda3d07a075 | -14.35494 | -45.90879 | 2025-10-01 05:12:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d849e78-0a8f-3c5f-a0a1-c7f79701fbbd | -13.7346 | -48.82071 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88784311-c9c7-31f7-8332-0eea300632f1 | -18.16063 | -46.10461 | 2025-10-01 05:12:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa1aa828-ca48-3cff-a8e1-d3fb4e6422a8 | -14.68731 | -48.23136 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d4d9192-52dc-3a99-8960-1a1f393c07bd | -13.68166 | -51.22673 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c182c8c-8b7d-34f0-afcc-767e03c91ebe | -15.14151 | -48.01438 | 2025-10-01 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9c76c96-2ac3-3b42-be68-dfd859f39790 | -14.51662 | -48.37881 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf85e440-1fcc-38dc-84ad-29017089a954 | -16.37282 | -47.05105 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13fb6de4-a16e-3fe3-b242-d3a2f2de20b9 | -18.90326 | -48.06699 | 2025-10-01 05:12:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aaf6ea03-5628-39df-b3ae-b1c5d8a4f756 | -14.49141 | -48.44498 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff93c9a0-eb97-3d5e-83e0-2cd19289bd24 | -14.71642 | -48.16228 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81646e86-2124-39e8-b1e0-f22123076b52 | -15.32014 | -46.40559 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd5e006d-27c7-3583-bc45-3ea030eb1c27 | -14.69068 | -48.12082 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b4554f1-7852-3056-ac51-21a0d908e2f4 | -15.30478 | -56.79443 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ec0904-4b3d-3dfa-9e5d-4f842c067ce4 | -15.70334 | -59.48309 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 745f5b9c-210d-3ba3-a5f6-3bb9062cb54d | -14.67444 | -45.29396 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efe54232-be21-3c5e-a821-9ed49980f0ba | -16.0234 | -50.90502 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aefed867-9194-3a5d-beaa-eb9b6c5b2c59 | -15.24169 | -56.81003 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de380feb-01ee-35c5-b584-9eda10019e92 | -15.34658 | -56.95422 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10d48acf-5117-388b-9e27-d31fac377407 | -17.89791 | -57.58636 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 28854434-61bd-385d-9d9c-b861e69b5e5f | -16.01581 | -50.88189 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 671e9ea1-f02e-3dea-8432-d5117cbcbd99 | -14.5176 | -48.37015 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffaa9b24-7764-3f83-a95c-275a21cde8f4 | -15.31239 | -46.41575 | 2025-10-01 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c119357-a444-387f-8a69-9fffa2adc4da | -14.50517 | -48.48027 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef1a4152-0845-3bc4-83ec-0cc0404ee8d1 | -14.09678 | -49.7447 | 2025-10-01 05:12:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a4ccf92-fecf-3995-9ffd-c1f3863a631d | -14.59364 | -48.2275 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c5fdc669-2261-3777-bb4d-8d55777740d9 | -15.15496 | -49.09971 | 2025-10-01 05:12:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e093576-d86d-3c2f-a3ea-9f89917a6f7d | -14.80728 | -59.71403 | 2025-10-01 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28247002-65ac-3eb3-a556-9e0b655df74e | -14.92143 | -47.81928 | 2025-10-01 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4c6c6c5-c4f0-3e21-bfcd-c8db035e856e | -14.34815 | -45.90795 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b956584-05f0-3f04-b9e4-5ce82e380b06 | -18.16638 | -46.10645 | 2025-10-01 05:12:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a144cd83-c872-3e5e-a08e-ea25449e16c2 | -13.77721 | -47.988 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a0a1d72-eec3-30fb-974c-a87920d70942 | -13.73505 | -48.81692 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 008b1651-f336-33c9-b376-ffdc167099da | -14.70416 | -48.21977 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0385498-515d-3802-9fb6-f6916cff6edd | -13.76645 | -47.97615 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 534dd151-fbcd-355b-95c0-d14d8b9f82c4 | -14.54349 | -48.24641 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25ac28ec-8d8e-3551-bd1a-7568a66702ec | -15.28495 | -56.78331 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d55191f4-c63f-307a-ba52-e5972f56ac56 | -13.76881 | -51.22902 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e3325c8e-0568-36d1-8b6d-c51b622d962a | -13.7681 | -47.96119 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa39ae83-a6c7-31ad-b6a7-e9381adaa14f | -16.39916 | -47.05044 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8780d863-720d-3e2d-9d2e-f1d299693ae3 | -12.90656 | -54.75122 | 2025-10-01 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f71e1a8-b51f-39e9-bda5-b0bfacd41c27 | -16.11966 | -48.40697 | 2025-10-01 05:12:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bea5acb1-60e3-35f4-97d4-3e4a9fbdaa33 | -15.34252 | -56.95768 | 2025-10-01 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37b1fd9d-7b2d-3c45-bb5e-b8acd83a1e6d | -14.18801 | -46.11492 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54d11c33-e44c-3b31-9b4b-b55bd777c575 | -14.90576 | -51.67634 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 99eb20bd-9e6a-3516-a244-21e4cbab9382 | -12.79292 | -56.96187 | 2025-10-01 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27159833-969f-38eb-9113-1df045a0e3be | -14.70572 | -48.12326 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 136a52a0-1d8d-3eeb-8676-cc97604d0940 | -14.56065 | -48.23692 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 607ad760-ac26-3546-b008-fd3d45ea9835 | -15.27092 | -51.47508 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 946125bd-3fc5-330f-862d-2eddbdaeb0f8 | -13.80092 | -47.49012 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 956fd5a3-a6b3-3e50-967b-754d17acde24 | -15.27007 | -51.47574 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59ad9642-adb3-3522-acca-a11d654d4e4b | -18.15938 | -46.1058 | 2025-10-01 05:12:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc8056b7-8d69-3120-9cf3-1a6e936d125d | -14.80395 | -48.33199 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ecda044-5875-34d1-b7c0-97b48399052a | -16.19406 | -49.99131 | 2025-10-01 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README132.md)

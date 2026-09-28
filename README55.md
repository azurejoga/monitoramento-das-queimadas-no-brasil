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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed1beb0b-c6ea-3f75-a9e1-21b497f640a3 | -11.68215 | -44.5258 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e781cd59-4205-3990-8c96-d04c778590b7 | -13.4195 | -51.34001 | 2026-09-28 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4fabc31-95b1-3aca-9a87-53e54f39e911 | -10.41076 | -53.81432 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6167bd4-76bf-3ca8-b55d-1bae179bb706 | -12.87842 | -44.79002 | 2026-09-28 05:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4078a813-f3a1-3078-8e54-d55655975750 | -12.59521 | -51.95716 | 2026-09-28 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6362e6f3-77a3-34e4-9ee4-69d7cb6e170c | -11.33795 | -54.11002 | 2026-09-28 05:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 499be5b4-13f3-37ec-9c43-01213bb559f1 | -14.72129 | -45.57691 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a63e2bb8-9795-3ba2-b806-9bccd26d5dc6 | -14.79526 | -45.95037 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6816834f-445f-3194-81dc-433f04fca70b | -10.40682 | -53.8174 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1d669c6-17cb-3db4-8551-65f7dd109e1e | -15.40712 | -47.91618 | 2026-09-28 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 30.7 |
| e250f837-aedc-3e8d-9ef1-41662e8b6534 | -14.11635 | -46.29166 | 2026-09-28 05:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80d6fd1f-7696-3294-bdde-0d52500919c2 | -10.55019 | -51.43694 | 2026-09-28 05:12:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e13bd40-dcb6-37c2-abd5-31b4df764d6e | -12.68526 | -45.02244 | 2026-09-28 05:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 129d1115-bf6f-3173-a773-26f88136982e | -12.16343 | -50.37562 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ad2443e-ccb4-3c04-b27c-956163e571bf | -12.70797 | -46.98878 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e22254c3-5b20-37a9-99f7-03c557cf553e | -11.70386 | -44.54639 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d009e37-4850-3a68-94a8-a5b49780f596 | -16.3197 | -46.55221 | 2026-09-28 05:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1b46a79-d5df-3921-b77a-514baacccfe8 | -12.73722 | -47.30321 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e8656cc0-506b-3e91-befe-11368f1b556a | -11.34133 | -54.11055 | 2026-09-28 05:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 588d4243-c950-39c6-8483-cfeddeb4a98c | -11.44456 | -44.93184 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fd432c3-ce76-3fde-a6f3-bc3d15dc7482 | -14.59729 | -45.58619 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf94b69c-5eaf-392b-9c6a-5b35eb2a486b | -14.73908 | -45.57553 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fe02520-0a20-3d14-8396-a55d8c435e91 | -16.32008 | -46.54882 | 2026-09-28 05:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 264f99e5-452d-39d9-8a7e-43b1515e15ef | -11.70928 | -44.55153 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9acd7d1a-7edb-3ac1-b2be-fd9254a9d67e | -15.16524 | -46.16099 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be05dbe1-5c4e-3b6c-b9f3-113c15e24f14 | -12.74372 | -47.29246 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| eb28730d-27f9-307c-8db5-96e5949d9816 | -13.45449 | -46.31771 | 2026-09-28 05:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82793d30-69cc-3229-b59e-811d75674dfe | -12.06595 | -46.4783 | 2026-09-28 05:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3b774236-5628-3474-8e7c-b0000ced2e0d | -15.16566 | -46.15728 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b7adf08-bb17-389d-98aa-5c1fb99428cc | -11.68108 | -44.53458 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0ace3d0-1864-38d9-8e65-f893fea08d83 | -11.68758 | -44.53096 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e4145cd-925c-33c2-9529-a8e589c9fff6 | -8.61071 | -64.06293 | 2026-09-28 05:12:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6b1cce7-05c6-396a-807f-6fb6bb396e42 | -15.62404 | -57.47982 | 2026-09-28 05:12:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e9fb296-a152-3d82-9615-5ea89c20a8e2 | -11.48099 | -46.85326 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00151aba-6683-3acb-9ce1-4195b33cfcb0 | -12.68292 | -46.98022 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 082a7358-c95a-3eac-8503-40719aff2fca | -10.92402 | -50.67327 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e5fe3fc-c087-389b-8f72-e225957e8fa3 | -14.09178 | -46.31115 | 2026-09-28 05:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 784b2bb6-cd88-347a-be09-a473bd58f46e | -10.8243 | -57.232 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f6ab240-cdf0-3bc0-8b5a-d1e6f7f602e5 | -14.09088 | -46.31886 | 2026-09-28 05:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bde6c484-2da6-3833-8190-b00760d7ea9a | -11.37957 | -47.4324 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 47df864e-2317-3838-ab12-1e215e84bed5 | -14.7957 | -45.94657 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83a302f8-e5bb-3093-9511-c0ca02452f46 | -12.62852 | -47.32333 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6a92bd51-3ab3-3dd6-9e9f-e1998dbcb52d | -11.27988 | -54.43967 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e46b13d-c20c-34c1-b8fc-40f47a287039 | -13.72038 | -48.81327 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e3d6c55-bd4f-3eb5-8f8f-bfd1fac82825 | -11.3817 | -47.42867 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3592b35-d025-3da9-9ecb-5cb7762f5a13 | -11.40762 | -47.42106 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d80464b-d0fd-3135-94fb-618cd91e5af1 | -11.67949 | -44.54773 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0e9f403-89e2-39f6-bf7e-e08017de8494 | -14.48808 | -53.63491 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad63f109-05b0-3f9f-bf0c-c4d6666f6f8e | -8.61235 | -64.0634 | 2026-09-28 05:12:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba17582a-9bb2-3739-b9d2-bec8ba435c29 | -15.74028 | -51.11205 | 2026-09-28 05:12:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ad23e36-a3e6-33a6-a8c6-550c9c2c396a | -10.70672 | -50.47171 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e2eadb5a-ecef-368e-ba15-a91a5224fa07 | -11.78435 | -48.33259 | 2026-09-28 05:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9c8ff8e-5515-30ca-915f-1263f4129c74 | -11.35884 | -47.43824 | 2026-09-28 05:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6bc4f4c-13d1-3bca-bbe4-5705a0c36cab | -10.42145 | -53.8346 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d79c1f11-84d6-3a68-96a8-23847d77c62b | -11.47629 | -46.84938 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ee51c7a-424c-3719-a323-8010a5ca8db4 | -12.75234 | -47.30516 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 02c540f8-65d1-3ec0-8530-e4eb592e4b43 | -11.37624 | -47.43234 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3681d23-400c-3b7d-8554-eff35c4c257d | -10.17 | -63.06057 | 2026-09-28 05:12:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8395cd06-2246-361b-a4db-b993f25f83e1 | -13.0795 | -47.44449 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b00c07fa-b091-3a71-ab4f-21f7565ab0b8 | -13.47343 | -48.59703 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd1a3639-a268-38f8-a474-5dff5b93e4c6 | -10.42652 | -53.77961 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b5f6820-9f97-3cb5-a56e-8fdd033cc9c8 | -11.37345 | -47.44075 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| edb5666d-19e1-3336-8688-8b976954e00c | -15.19421 | -48.43505 | 2026-09-28 05:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ad35ee7-75ce-331c-8ee9-dc1b3ff7bbf2 | -10.42201 | -53.83097 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 402dcbc7-de13-3add-926e-e9267cfe23e3 | -11.71198 | -44.52956 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42c3803c-e456-31bb-ba5b-aa5881e6c77e | -13.37824 | -51.31826 | 2026-09-28 05:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b98b4220-4e5a-3ee0-a733-6078266df423 | -12.07042 | -46.4854 | 2026-09-28 05:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| eec9831b-c11a-38eb-9e7f-56ad5297daec | -13.10374 | -47.4136 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0b9cb08b-db82-3b9c-8f92-908767d165e6 | -10.82457 | -60.74552 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8e6f2f50-c8dc-3de7-9e23-08b72b217b16 | -15.15719 | -43.60165 | 2026-09-28 05:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c176162-3be9-38df-85a7-fe2d3098c9fa | -11.86062 | -47.09425 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0de9c3f8-776d-32c3-afb6-0c26d6799f69 | -11.70332 | -44.55078 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 536b55ce-6b11-3396-b37b-0ebdd7b00244 | -12.74655 | -47.3103 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 570f77f7-91e1-33f1-a460-622954899da4 | -14.71598 | -45.57191 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd7ea43d-6a79-3c1d-b275-de0f1138c444 | -15.46961 | -46.15021 | 2026-09-28 05:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d709a742-6cf5-378a-8613-7cb9f065ad91 | -10.41301 | -53.82211 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f6082e2e-4b92-3805-aa82-78c62a132b3e | -10.40063 | -53.8127 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b97b5608-53e5-384f-8cd2-ae4260d40146 | -13.91917 | -49.36254 | 2026-09-28 05:12:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d47b8139-15d6-355f-9685-45db3f1e6562 | -9.07165 | -61.43785 | 2026-09-28 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2044849-84b9-3284-b0e6-7d83b647a170 | -10.92571 | -50.66692 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19cea701-eb0a-3c7c-925e-cdd85f7d020f | -11.30726 | -55.10842 | 2026-09-28 05:12:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91e45d32-cd84-3838-8a0f-2102c01c1f63 | -13.69676 | -48.81459 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e04387ae-6235-303d-bd53-e64f7911574a | -12.15987 | -50.37141 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b541bd79-e7ce-34cb-906b-cb01b69977e6 | -12.742 | -47.78631 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb5785d1-6995-3052-8d7c-89463a2915bf | -10.91731 | -56.51803 | 2026-09-28 05:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e066b4a-dbd9-3eef-94c3-e02dda01e64e | -11.02174 | -54.1464 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be8dd2e9-f771-35ee-a137-92579f24daa0 | -13.07562 | -47.43898 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 86c69792-f13a-3504-99a4-f549e8417ebf | -11.70547 | -44.53323 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58dfe64a-1539-3bb1-b6b0-01cc79283692 | -11.10159 | -51.3218 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3ee436c-ab0a-3c45-a07b-733f3d8d7bf0 | -11.35046 | -47.42648 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19765193-5f46-3981-b009-e762534476f7 | -12.62425 | -47.3168 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45dc3c37-f0b8-3765-b8a2-27d6b60f7dbf | -13.45477 | -48.59459 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eb433f4c-c393-37ce-bdc5-319fbc1ae801 | -12.30924 | -46.40601 | 2026-09-28 05:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90715d4d-9f64-3145-9684-d4216bdeee5f | -15.26592 | -47.6213 | 2026-09-28 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91e3c72c-90b8-39a4-89c4-4f7de8783da1 | -11.44558 | -44.92366 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc1dc2a1-0f60-3140-a559-617261b86949 | -12.65882 | -47.31622 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cbd7ec34-9d97-3f45-89a0-3b6a90e38007 | -13.04334 | -60.52234 | 2026-09-28 05:12:00 | NPP-375D | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a512895-0fd9-3393-8930-71f17596d8c1 | -9.92862 | -60.72217 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74696387-a13e-3658-8144-bae722a0ca6f | -11.37471 | -47.4315 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 13016c2d-94ba-379a-904f-9429c29704ea | -15.11682 | -53.88476 | 2026-09-28 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README56.md)

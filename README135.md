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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d212a6b-c252-3b95-9a2a-0c5853e2943e | -11.3793 | -51.3989 | 2026-09-20 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 179.2 |
| cbb762fe-f36b-31c0-a089-c44006429241 | -11.9885 | -50.0277 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| bf0dfdd3-3e4f-301e-9186-90b9d890335b | -2.9143 | -58.3401 | 2026-09-20 15:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| f1d89752-771e-3f53-bc8f-9acee05447b2 | -2.8961 | -58.3018 | 2026-09-20 15:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6ea085d6-bc7d-378b-8aa3-e890d3424da2 | -3.3492 | -59.867 | 2026-09-20 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| f962f450-cb12-3297-9c1b-9445aeefcf12 | -11.3813 | -44.0554 | 2026-09-20 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 47154e9e-56a0-3e0a-b352-dd39eb413a40 | -6.1358 | -59.9638 | 2026-09-20 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| ab590b4a-6871-3657-988f-d98880c7b6c7 | -10.5535 | -57.4567 | 2026-09-20 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6d18ecd6-487d-3ee7-995d-3daeb7e95a70 | -7.1203 | -42.083 | 2026-09-20 15:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 7416e709-3593-3b21-a741-30d3adea704f | -5.8088 | -55.7095 | 2026-09-20 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| ebb83afc-d9e6-3551-9f07-32e071863443 | -3.4049 | -59.5794 | 2026-09-20 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ebaa7ab1-5ae5-3d88-bc9f-6fd04fcdf2d6 | -3.6763 | -60.6029 | 2026-09-20 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 06743bfb-f173-3112-ab07-1cb49f1cb424 | -11.4736 | -45.3405 | 2026-09-20 15:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| bda61b6c-3edc-3b16-a3f6-9f64c022e4ee | -7.3564 | -44.4726 | 2026-09-20 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| da52c438-4f25-3dca-8880-c2224e6c3a98 | -9.6853 | -54.3318 | 2026-09-20 15:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 504cb87f-0203-38db-a694-742b93b4b8e6 | -12.8701 | -51.0148 | 2026-09-20 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 818a6a3b-c947-34e2-b0e9-2ee1f4420744 | -1.5858 | -54.4552 | 2026-09-20 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 3727011c-14a7-3bef-ad40-5cdc04ce1224 | -3.5894 | -59.0581 | 2026-09-20 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a60f4562-e139-3ab8-a168-4e529d99d2f7 | -7.0428 | -59.2173 | 2026-09-20 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d06e2e5a-5392-3501-bd62-9d8bcd5904ed | -10.7842 | -50.6133 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| d949d815-d107-3966-88a8-d8f19c383059 | -6.737 | -55.0674 | 2026-09-20 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 9a126c59-3350-360b-a9e9-44a952c60a43 | -12.1332 | -47.0185 | 2026-09-20 15:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| de4e3a9a-4e9e-357d-9c90-bd4e9a5cef7a | -11.0596 | -54.1755 | 2026-09-20 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 149.5 |
| f411dd82-39db-303f-a532-27be37870636 | -10.2787 | -50.2605 | 2026-09-20 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 0f5d9efe-07fd-3281-9d7d-db184d83b4d0 | -6.3656 | -58.2966 | 2026-09-20 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 0e9cf4ac-d28c-3faa-bf0b-61694cef3559 | -10.9692 | -57.208 | 2026-09-20 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 33e20b31-ba69-3b7f-a9fc-a4ace58be13d | -10.7612 | -50.9132 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 175.3 |
| dc758674-2900-3589-b8ca-0317a8006b8e | -3.1079 | -61.408 | 2026-09-20 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| c25ccaf4-fbfc-3034-b615-c48bc0afa1ef | -6.0925 | -57.6847 | 2026-09-20 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ab1e48af-4171-3d96-9ecd-aa34e6e8e276 | -8.4611 | -57.6292 | 2026-09-20 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 1b83ac21-4d90-316d-ae8a-534309a4a45e | -11.4537 | -45.3892 | 2026-09-20 15:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| cca17a86-c8da-338e-b32b-bed18cd03fac | -11.9352 | -49.7752 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| c63e6c85-3e0b-38bd-9d02-fe81b695ffc9 | -11.7351 | -54.5636 | 2026-09-20 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 0744e349-01bd-3d06-ae4e-b0a1a55d26ca | -3.6946 | -60.5835 | 2026-09-20 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 295.7 |
| 7b86f673-4609-3214-a725-c0a46feef7b1 | -11.041 | -54.1567 | 2026-09-20 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 7bfff339-8b4d-3cd5-ac62-106f75af7b40 | -10.7652 | -50.6153 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 362.0 |
| dd9dbbc8-878f-3fd7-a58a-a5a5479eb056 | -3.3493 | -59.8479 | 2026-09-20 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 806bf7a2-de38-38b7-a3e8-cead40f93c9c | -10.8364 | -50.9479 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 406a5b5b-6081-3d23-a149-86f268327b67 | -10.1145 | -48.4205 | 2026-09-20 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 1cabdba0-abe6-313b-b710-5abb198c7279 | -8.7733 | -44.2336 | 2026-09-20 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 639df8d6-2d3a-3c3c-975b-f8f50c419631 | -3.331 | -59.8483 | 2026-09-20 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0773a7d9-940a-3d12-8f36-d5b7c2023513 | -9.6665 | -54.3332 | 2026-09-20 15:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| fefbdfa9-9bc4-3ac2-a37d-17a61a3ef94c | -3.6076 | -59.0769 | 2026-09-20 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| cb5be68d-da35-3f3c-9c19-f9b102f5505f | -10.0953 | -48.4445 | 2026-09-20 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 193.2 |
| f5d22368-5db1-37bb-846e-218b4eb7228e | -11.4541 | -45.3662 | 2026-09-20 15:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b0f37080-867d-3bbb-8f17-9fd4100ef746 | -11.379 | -51.42 | 2026-09-20 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 229.0 |
| 24ab2cea-8b2b-33af-9473-565b79105632 | -6.8215 | -59.1879 | 2026-09-20 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1d980635-b039-3a5d-9851-00ff95fe3aea | -6.4486 | -59.9717 | 2026-09-20 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 513.0 |
| 4b60b549-a580-3774-b656-bf1c10780cad | -1.7499 | -54.9516 | 2026-09-20 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 18e6c911-fd24-391d-8183-b32561ba6af2 | -9.6668 | -54.3129 | 2026-09-20 15:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 72862e72-953c-3960-a16e-d309d454b651 | -8.1688 | -54.7432 | 2026-09-20 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 298aed73-fc83-3746-aa6a-09eaf821e8a2 | -12.0072 | -50.047 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 16780158-9969-30df-8b26-28b5ace86fcf | 2.1818 | -50.8985 | 2026-09-20 15:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 74.6 |
| dbef57e6-755b-3e7d-adbe-78f156174931 | -8.4737 | -47.0053 | 2026-09-20 15:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 7df89bbe-13f9-3d73-abf0-68ab4f7ff67b | -3.3493 | -59.8288 | 2026-09-20 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a5833a46-3e5a-3d84-b500-248aee6752d9 | -6.7666 | -59.1129 | 2026-09-20 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.7 |
| ed670831-46cd-3083-b0e4-bbef5644f930 | -3.0534 | -61.2767 | 2026-09-20 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| a3f89277-35ad-362a-9a3b-590523f1b323 | -13.5911 | -51.458 | 2026-09-20 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 786db269-6a65-3081-9fae-642077053d7f | -7.1014 | -42.0849 | 2026-09-20 15:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| b6617fc1-e2d7-3852-b521-4f3e530aeff5 | -11.0065 | -48.3187 | 2026-09-20 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 932aa532-03df-31e5-a529-df61439996b9 | -6.1231 | -55.6359 | 2026-09-20 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0ce93660-8579-3a3d-8a6c-6b3685e2daca | -13.9448 | -47.8494 | 2026-09-20 15:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d521c1f4-10a5-3d82-a407-476ff2a2cd75 | -11.7354 | -54.5431 | 2026-09-20 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 22bbc72f-e6ea-3c92-8c9e-c206c334c563 | -10.7609 | -50.9345 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 16a3477b-f568-3099-a4e5-0c618aec201a | 2.2003 | -50.8981 | 2026-09-20 15:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 612d8a37-5dde-3572-b16b-d3f3f48150b1 | -11.9678 | -50.1379 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 638ddfee-37c7-3217-8c1c-f365ae2f9dcc | -2.8974 | -57.7987 | 2026-09-20 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| bae21298-331c-3e04-b4f6-251ab1cd66f5 | -10.867 | -56.1975 | 2026-09-20 15:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 233de31a-d178-330e-8c42-f973352698b4 | -6.8433 | -55.7602 | 2026-09-20 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b113b028-3030-3caf-ab8f-eae393c2dd08 | -12.8893 | -51.0124 | 2026-09-20 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 214.8 |
| efe1b0c1-9c1f-3e35-b2a9-df139ff08409 | -8.1871 | -54.7824 | 2026-09-20 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 62e82971-84aa-3c8e-8c92-f1f138785fdc | -10.8668 | -56.2176 | 2026-09-20 15:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ddb7cebc-5882-3366-85ce-ff320959a661 | -11.0259 | -48.2944 | 2026-09-20 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5a3c8971-238b-3624-9027-d2a121048904 | -9.2185 | -46.2365 | 2026-09-20 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 0c41887d-e112-31a2-a776-b250b8112c09 | -8.3578 | -47.2599 | 2026-09-20 15:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0745f074-2a74-30f1-b94b-d1319c5ea25f | -11.0221 | -54.1584 | 2026-09-20 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e1559266-31d0-3d64-b4ba-b8eee88392ed | -3.4429 | -59.0804 | 2026-09-20 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 51524d83-3c00-3ec3-a83f-eec9484f2ed9 | -9.7049 | -58.1443 | 2026-09-20 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| cb45f658-ec90-360d-8d83-fbd9cc9af07a | -12.0263 | -50.0447 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 4e6e4e5e-bace-39b0-a66d-260e09776b37 | -9.0353 | -48.7704 | 2026-09-20 15:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 94.1 |
| f905853c-fc76-30ab-a751-062f4c13d9e9 | -10.7423 | -50.9152 | 2026-09-20 15:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 171be22b-17b7-3b9a-b2db-10998e22bcbd | -6.8411 | -58.9939 | 2026-09-20 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 7a658e2e-a937-3e92-9dd5-a89c6486573b | -6.8216 | -59.1686 | 2026-09-20 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9f7f5fe3-2e4e-3f35-af42-ae2349ac2680 | -7.2519 | -55.5994 | 2026-09-20 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| fc5b7397-c3c9-3ae4-bfcd-e58b88d81542 | -9.0355 | -60.3589 | 2026-09-20 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 88745e4d-651d-3abd-81c1-db9fc23753dd | -8.4549 | -47.0072 | 2026-09-20 15:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 95898344-37f0-35a1-88f1-ac2aa18f5911 | -12.0076 | -50.0254 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 55a41ca6-d8f9-3f2e-bb0e-56700b622f8f | -3.4428 | -59.0996 | 2026-09-20 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3964f6e7-7908-3e33-a661-f4418fa45f1c | -10.6143 | -50.5884 | 2026-09-20 15:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 3be71998-22c0-3984-9fc0-142267dc23a8 | -6.0927 | -57.6457 | 2026-09-20 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 6a09ff82-f150-331e-b6fa-fef94d7f7b37 | -3.3367 | -57.8673 | 2026-09-20 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 17977b89-33df-34f1-9855-2af9c54da20a | -6.3198 | -59.9572 | 2026-09-20 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 3c58a52b-56ff-37e3-94d5-f2ebe2b53d9c | -11.3437 | -44.0141 | 2026-09-20 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 05274750-4a01-3dd1-9755-0a1d85b5394c | -10.8672 | -56.1775 | 2026-09-20 15:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 4eed3d59-be98-3c40-bd85-4535db6c5780 | -8.1684 | -54.7836 | 2026-09-20 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| eec39c5d-8771-3b7f-b6f3-e625a63bfd78 | -2.8975 | -57.7793 | 2026-09-20 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ecaf6c79-19dd-30f4-8e42-59aab4f7667c | -11.6624 | -50.1954 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 88224f67-0bf3-3a71-b44b-0ef4e12470e9 | -8.1686 | -54.7634 | 2026-09-20 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| b9df389c-801e-31ff-8a3a-5044e071b055 | -5.9815 | -57.7672 | 2026-09-20 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| b62201ef-92e5-3347-9df1-b06f72045639 | -9.8397 | -46.4361 | 2026-09-20 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |


[Clique aqui para ver as próximas entradas](README136.md)

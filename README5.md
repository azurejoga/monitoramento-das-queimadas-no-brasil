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
| bd47f839-92f8-348a-bebf-6ef370c2d1a1 | -9.35841 | -46.74332 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ef0e8e97-4927-3a6e-a7c2-304b853ee095 | -14.12373 | -46.47488 | 2026-07-13 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8535e4f-9852-3791-a873-94349b8fc651 | -9.37163 | -46.72399 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5f3777e-7a25-3390-bafb-375ee0a1e81a | -9.36777 | -46.72695 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84f7bc99-b5be-391d-b436-59fc43ca6a76 | -8.71986 | -47.83172 | 2026-07-13 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eac6937d-0389-3ed5-b12f-5f023380fa3d | -7.5393 | -45.12944 | 2026-07-13 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe620b03-53af-344f-950b-dc55c3101e90 | -13.76235 | -46.24757 | 2026-07-13 04:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f2a7b48-f46b-38e7-b911-5859cf02d29f | -9.63871 | -40.59772 | 2026-07-13 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8f40556b-afbe-371e-bc78-b22b78589a79 | -7.26761 | -49.51503 | 2026-07-13 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e60fd553-94db-3f5c-b067-e3529d3948f2 | -8.88199 | -48.49676 | 2026-07-13 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| afc5c65a-5f61-34da-88b3-07d6ca8065c2 | -9.35346 | -46.75324 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e03165fe-6236-3b16-b218-da777f67438e | -10.17197 | -50.12637 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07317120-30ef-303c-9888-0bf81c884511 | -11.98974 | -45.14843 | 2026-07-13 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 288cd94d-2150-3f0c-995a-b97bb0c39617 | -9.38651 | -46.71565 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a028812f-4d5e-3994-8cd1-7a8bbb09ac1c | -7.91106 | -48.25453 | 2026-07-13 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f908ffb3-83e6-3d9c-af53-a5f4b5819984 | -9.42935 | -40.71245 | 2026-07-13 04:32:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e139a00c-3629-3bf2-9a04-36685b96d3e0 | -8.09096 | -47.08845 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a932e37-08a2-3474-a093-fa429d8eacce | -9.37492 | -46.70309 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c913931b-aea4-314c-a756-1a35624828e1 | -8.12754 | -47.87778 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ce047ef-cf9d-3a3b-8685-823884e63e6f | -9.36172 | -46.74385 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ac6efe6b-b9ac-3b52-9afb-2255a0299ddf | -9.35565 | -46.73931 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fca1c37f-8a8e-3081-992d-fc63b215f347 | -13.74987 | -46.28403 | 2026-07-13 04:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 231fa811-04c4-31a6-bffc-c0b7e6538e09 | -9.37547 | -46.69961 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7212358-d39b-3660-b5f7-a34bc82dcbae | -13.96094 | -38.94068 | 2026-07-13 04:32:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1d7d8a0b-715b-3272-9635-da63b20df794 | -8.08655 | -47.09486 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71e0c5af-5dfb-34e8-aca4-88494b71b656 | -10.81963 | -45.13787 | 2026-07-13 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35fedd05-3c17-3ead-86e9-7a88047a2bfa | -8.08986 | -47.09538 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fcfe095-d2f4-3d53-9425-cbe3be72d77e | -8.13479 | -47.87531 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0989a95b-66a2-3a60-af22-de9132548f2c | -8.08765 | -47.08792 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cde553df-7a43-3d7c-8bca-82ee4ba583ec | -10.25688 | -50.05354 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ce6629d-95ce-3e2a-ac00-2a08455226a9 | -10.82368 | -45.13456 | 2026-07-13 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ec623d8-671e-310d-a00e-fe4ccf21b32e | -9.35511 | -46.74279 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81a577d0-08f4-3d9c-a738-f56a9cb3400c | -13.19506 | -48.3257 | 2026-07-13 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| abe4d535-3a5d-371e-a5b5-1576e27c2114 | -13.96625 | -38.94131 | 2026-07-13 04:32:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| dd121014-af6b-33fe-97f1-e0a8bab273d6 | -8.13145 | -47.87477 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d644dc9-c428-3c6c-ad9d-79640f3d82e6 | -13.76178 | -46.25132 | 2026-07-13 04:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 206e86c1-7f57-385d-84c1-a2e6f9d64e5e | -9.36446 | -46.72643 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38e16e4d-7723-3af1-b616-5fd1549fffd1 | -10.82022 | -45.13402 | 2026-07-13 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0b9b3a2a-d476-3dc7-9f49-096024efc947 | -8.09316 | -47.09591 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c6c483a-96d4-3d49-8188-9e23e007785a | -8.12811 | -47.87423 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9360c739-5667-3b87-b8e1-b3cbd4c24300 | -9.86128 | -57.80774 | 2026-07-13 04:32:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ada27b84-1143-30f8-9aa0-1becf948d242 | -9.35732 | -46.75029 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0afcd368-7405-393d-9e98-9dbaf9ac8564 | -8.0871 | -47.09139 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bae822f-680f-3a3f-a49e-7f9397b492f3 | -9.36006 | -46.73287 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e5f0638-20c6-3861-bf53-631c9578a1ce | -9.36117 | -46.74733 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5df6275f-f43e-3a7a-90ff-75ecf6d9dba9 | -9.35951 | -46.73635 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ccbb00b4-6d5a-3519-b65e-91b309297f67 | -10.24982 | -50.05232 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96134c9f-8e7b-377d-ba6a-e7d70b910dc2 | -8.71929 | -47.83525 | 2026-07-13 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e1c0294d-ba99-3317-a8bf-ded8259f4799 | -9.63809 | -40.60212 | 2026-07-13 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d26da3db-cc81-35a4-a9c1-15e88db4f336 | -10.81618 | -45.1373 | 2026-07-13 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bbd8e770-c2c8-3dcb-89af-94e569571162 | -9.86123 | -57.80735 | 2026-07-13 04:32:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6aca4110-812a-3595-bce2-2baff8843c08 | -9.43376 | -40.71306 | 2026-07-13 04:32:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bdb91e21-6713-355d-a008-77c0f0dad3f2 | -7.39707 | -44.27641 | 2026-07-13 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7a8234b-3957-38f0-b44c-3352b1c2de28 | -10.47781 | -42.4213 | 2026-07-13 04:32:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 99596d35-8816-3374-923f-400df35678d6 | -18.96366 | -41.96703 | 2026-07-13 04:34:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2528b247-a38e-3b4b-8224-1fb2967e8e26 | -19.31252 | -41.39323 | 2026-07-13 04:34:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c01c5346-5693-38ea-b77a-6ddb56235658 | -19.31131 | -41.39307 | 2026-07-13 04:34:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5ccc4dde-df4c-35aa-8ab6-164dbb080d19 | -15.23839 | -48.57475 | 2026-07-13 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b8a9122-2dd9-3e32-af12-d7fcb4a4cea9 | -16.50014 | -52.60296 | 2026-07-13 04:34:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31a0ac45-fd7b-32c3-8eb2-6cd3b647df65 | -19.30696 | -41.39876 | 2026-07-13 04:34:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7815392c-b7ee-3205-89ef-82b82e69c15c | -19.31186 | -41.39887 | 2026-07-13 04:34:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dec9af03-e3a7-3dcb-b34e-1c32268e107c | -14.6546 | -45.86735 | 2026-07-13 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4f33bb4-081d-37a9-9fed-f7bca12bd54b | -17.16575 | -46.83377 | 2026-07-13 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53fc368b-1b32-34b2-a65d-aa5471c81173 | -14.6517 | -45.86285 | 2026-07-13 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ced61fe-9e8f-31aa-b92d-55eff6d33868 | -19.31068 | -41.3987 | 2026-07-13 04:34:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c5d598d7-c1df-3630-a2dc-ec7e72675430 | -15.79932 | -42.02168 | 2026-07-13 04:34:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3bd7a3c0-6bd2-34de-a227-8b49bb28c722 | -15.33727 | -42.90656 | 2026-07-13 04:34:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee92362c-5377-3396-b527-7b55d1a4df9d | -19.64242 | -40.18854 | 2026-07-13 04:34:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa7f08e4-ff00-3b3c-8472-55db3a9aa8e7 | -14.64705 | -45.87024 | 2026-07-13 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53bb9d9d-db2f-34bd-bcb9-e61055327860 | -19.64272 | -40.1887 | 2026-07-13 04:34:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ba3e5e72-865e-3cc6-8f4d-d93ee9bc1c7e | -14.65053 | -45.87078 | 2026-07-13 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ba13c9f-a757-3b5a-b05b-965b36072e01 | -15.33676 | -42.91037 | 2026-07-13 04:34:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b0d052b-b135-3798-a928-9682bc5e80a7 | -14.29284 | -54.17279 | 2026-07-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c05bd0fe-2726-3c28-8e5a-378d8f3df178 | -4.94782 | -48.25057 | 2026-07-13 05:16:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da485d39-0868-3a0a-adc4-54d1a44267d9 | -4.00777 | -48.95139 | 2026-07-13 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a21bed37-cdd9-37da-a5a2-39b1e31027dd | -5.79589 | -45.11426 | 2026-07-13 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2bd2031-d7da-3eed-81a2-b843042ce740 | -4.94835 | -48.24684 | 2026-07-13 05:16:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c801dc80-ddfa-33a9-8398-17e9c590b3f9 | -10.25078 | -50.04712 | 2026-07-13 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dff7bad1-f127-34e1-bf0f-4537ea36e37a | -8.13242 | -47.87799 | 2026-07-13 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 286f8db9-b46d-3351-a2a5-21b6671f39ab | -8.13305 | -47.87321 | 2026-07-13 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0007bc06-33f7-35ad-83f1-d1407dafb32f | -8.88622 | -48.50093 | 2026-07-13 05:18:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27e68cba-2f03-3f90-9623-c4ea0030f1af | -9.36149 | -46.73603 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2f7b7c6e-a0c9-3309-81c1-5924069615ea | -8.12578 | -47.87509 | 2026-07-13 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb4610a5-7349-39b0-ba62-b4446ac7600b | -9.36079 | -46.74192 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7fd93c02-ee2e-3c71-9062-5dfe6b888174 | -10.25032 | -50.05079 | 2026-07-13 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a3988004-292d-31b3-a8ed-789eb9291bbc | -8.8838 | -48.4999 | 2026-07-13 05:18:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca08c039-bbd7-3dff-abd8-cf5ca584f548 | -9.37637 | -46.72571 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7f138cf7-87e1-3e74-98c0-f585156ea8ab | -9.35769 | -46.74226 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b446b920-009b-34a9-928c-1d57396576eb | -9.35842 | -46.73642 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7e052844-dc09-3ded-a6ce-994299e187d5 | -9.35938 | -46.75385 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdc0474b-bf7d-3b2a-9cf0-a3dd8b36a534 | -9.35097 | -46.74143 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| abf6ca2c-8a63-3cdc-8682-81fc901fe166 | -6.54496 | -55.1535 | 2026-07-13 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fcbfa26-e419-3402-bf71-c59252d2651f | -8.08841 | -47.09927 | 2026-07-13 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26c4b139-0c0c-3c37-80a0-3afac8dde453 | -9.36009 | -46.74784 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbe046d8-4dd4-3b41-a61f-c9d7de9aaefc | -10.25585 | -50.05153 | 2026-07-13 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 74c91603-ac3e-3873-8f80-229f6aa92e0f | -9.37708 | -46.7198 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8f393f8-3873-306e-bc35-a182d56b7bd8 | -8.6059 | -63.45704 | 2026-07-13 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 652424e1-0e7e-3672-9441-9a7faf199e77 | -9.38381 | -46.72066 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df39f46a-86ac-39c9-8758-c944b2dba153 | -8.08905 | -47.09423 | 2026-07-13 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25ee051c-ffa7-3899-b862-169cfb7142d1 | -9.36219 | -46.73007 | 2026-07-13 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README6.md)

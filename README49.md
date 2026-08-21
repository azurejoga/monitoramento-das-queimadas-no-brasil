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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ef9d14d-a62b-36a6-b796-ab012185b871 | -15.7629 | -47.77173 | 2026-08-21 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dcfce61-c266-32e7-ab58-3ec33af93250 | -12.26875 | -43.15881 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 48bbe509-9088-307c-ae0b-9e153fa8728a | -12.26758 | -43.1681 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 48b79c7c-d725-38c6-94cc-e414e3c9bd70 | -14.07453 | -58.87573 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7650a0cc-f492-330d-ac8c-09823e9012f7 | -15.4416 | -41.38369 | 2026-08-21 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 6835a048-f324-3ec9-b0d6-81c1b9cffb14 | -14.34623 | -51.89366 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2909b494-2c7b-3d50-b481-14cb5ca3e7cd | -17.95553 | -44.39774 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1dd40fd-c1e1-3752-a5ad-32d3e7679a92 | -14.57175 | -53.01447 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01f04184-5c09-30d9-9b8b-3bf155ac75c5 | -14.45618 | -45.6252 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7f37883-48ff-3723-bf90-de89c541f788 | -13.43406 | -51.79789 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3abdfd58-fc18-3f7e-bdf7-87cbd060baf6 | -13.39677 | -54.38292 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 069b45e6-8480-394f-8576-4d1dd252434b | -14.10002 | -58.85559 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e162aef-e006-3f77-8be0-4c6faf030dab | -14.55134 | -52.9929 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 675c843a-099e-377b-922a-b2edc48597bc | -15.50974 | -53.94712 | 2026-08-21 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d40dfba2-a079-3968-bc1d-b2ff1d078700 | -14.46086 | -45.6258 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de021e96-45a0-38ce-bd34-b4bb9629c412 | -13.40538 | -54.37286 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea2ad700-1fe2-309f-ba22-17c331ad6620 | -16.30453 | -53.17188 | 2026-08-21 04:49:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15644f74-a1a7-3036-ae1f-eb876e022f0c | -11.21667 | -55.04492 | 2026-08-21 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cd59016-7c78-3c4d-8d9f-881f5667f60b | -15.5652 | -50.28117 | 2026-08-21 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3424a88b-028f-3523-94c6-615901502b52 | -17.3334 | -43.62788 | 2026-08-21 04:49:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e14fe1c-a2f9-3e50-a95e-3f81cd6059c6 | -11.17721 | -54.00888 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85c41d70-7171-3cda-874f-c7cbee869b6a | -14.57507 | -52.99316 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22da81d3-6baa-3088-b714-7a06b7ed5361 | -13.4385 | -51.79122 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdf10709-0b4c-37b4-918b-e4ad95bded32 | -12.9391 | -56.64937 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffa17128-1507-3afa-911c-672ec0bcb04e | -13.44186 | -51.8139 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f02bc56-ccc8-3491-a0ea-670cda7d04fd | -15.22033 | -52.79968 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec4b2910-61e0-3152-9a9e-88c9dd85ed0b | -14.72671 | -47.13614 | 2026-08-21 04:49:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6720206c-99c5-3936-a58a-81b8f855fbd3 | -15.00042 | -52.68313 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c923e845-41f4-31c2-ba88-7f923ed38286 | -14.45511 | -53.06416 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 647e8c15-35cc-3b4c-8bec-79fa17086faa | -11.68312 | -54.56984 | 2026-08-21 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de478932-7aa5-3fdc-9833-e249061fc588 | -11.19943 | -54.00111 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4adef0ba-8ffd-32b6-b58d-baa10433da40 | -18.03348 | -44.6125 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0935614a-bc05-39bc-a444-4b38769ca4f7 | -11.20488 | -55.05215 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7153542-1dcd-3ef8-9f42-8212375a0a03 | -12.51124 | -52.42791 | 2026-08-21 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30bb8ecc-f6c2-3e85-a82a-8284071eaef8 | -12.72062 | -48.48262 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce1a190b-d090-37a3-9009-93a9891ce759 | -15.01202 | -52.67406 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5499b74-9311-3e4b-b756-854358b57110 | -12.74081 | -48.47663 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95061543-3e42-3bd9-8343-f34aa832c1bb | -12.78558 | -48.4037 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b5b37d71-29eb-3d11-9022-d8fa632f3365 | -11.20402 | -55.05519 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f96ef43-44e1-3dfa-9d45-7e64c0e54974 | -16.30121 | -53.17133 | 2026-08-21 04:49:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 253b5161-6b52-3476-ba06-ebf2d78d6912 | -13.27053 | -51.62441 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4059b26-ef4b-3762-ad7b-d51f87e02511 | -12.51586 | -54.7617 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5f2ca54-86cb-3b1e-b1ac-1eb36f2f6df0 | -12.80798 | -48.41026 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 819e1ae3-0acc-300c-877e-d9697a845778 | -12.83438 | -48.44364 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb819ff8-503d-39da-be66-e85efe2a8057 | -15.81793 | -56.45265 | 2026-08-21 04:49:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0f296f1-8ed2-3fa3-af5c-fa130f16d42d | -12.8028 | -48.41956 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8d0a7d0f-a30d-3832-a334-c30961d6bee4 | -11.81611 | -56.59993 | 2026-08-21 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 166dd4c4-edda-3411-820f-48caf99429f8 | -14.31106 | -51.9063 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f885d79e-fc09-3218-9dde-d92b1a91bc5c | -12.76842 | -48.47201 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31e5d5b6-5e45-3e03-b917-191c36d3f1c2 | -18.06021 | -44.4154 | 2026-08-21 04:49:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84439cf8-527c-346c-9087-00857986ed15 | -11.17356 | -54.03125 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c27c0009-f5fe-3cdd-89f2-1279112dc4eb | -12.27417 | -43.159 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a1021172-bd40-3705-bd82-e9a96f0a6d40 | -12.9356 | -56.62479 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba072323-ad9e-3cba-a8d0-11a57934274b | -12.50203 | -54.75944 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7374d95c-2dda-3267-8787-4194beb84d71 | -12.76079 | -48.4712 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2eec4f94-0247-3e75-9f49-f5ca048c1b31 | -11.20422 | -55.05619 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa7f6c09-9bcf-3d9c-87e1-7aa851bb53a9 | -12.12514 | -57.20363 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 904ed303-50f2-3fc5-ae48-10ed50131cb7 | -12.50767 | -54.76828 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa5807e2-9842-34b6-8788-2cd57fb2f5c9 | -13.74413 | -51.85782 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1b3bbbf4-f32f-317d-8779-8749a27bc89b | -15.0087 | -52.67352 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50513242-b4de-37bc-adf6-c8511a5cd85b | -13.3787 | -54.38034 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 1c459dfb-b019-3c11-ad81-a79ab6687d32 | -12.25945 | -43.17305 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7737d59f-e588-3c7b-b052-607d261429a3 | -16.04958 | -52.16999 | 2026-08-21 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59656123-42eb-3c8d-a85c-7004138fa633 | -13.45125 | -51.77483 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b8ac083-59ae-3da3-ad76-24589a8e9597 | -14.11063 | -58.84514 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b413817-0ee8-3947-97e2-f72fb7387a4b | -13.93841 | -53.85728 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4257b37e-a9a1-3199-a7e3-0962de93d92d | -11.19142 | -54.00742 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5aa0d37d-85ba-388c-8d09-ac25a1a1d039 | -13.44128 | -51.79537 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd7b7073-1e50-361b-9334-ab61f48d58db | -14.3396 | -51.91493 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d2c2115-3c5a-3d1f-9a6c-c7101dc71270 | -13.37652 | -54.37233 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4368568c-3106-3fd0-bb3d-a9600f2b65b7 | -17.97424 | -44.4235 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b20b323-e64c-3f93-9f80-fd0a2dbb8ca1 | -12.00261 | -53.43352 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dd71c495-1bf0-3924-9f64-5193e9ba579e | -14.57948 | -53.00845 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56bc7a70-eacb-35f6-8875-aea9f0915b2b | -11.20756 | -55.0558 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 704fd035-ea2f-3ecb-8ef6-dd27558f583c | -12.37117 | -54.16334 | 2026-08-21 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3510e31-834e-3d4a-94b7-a327e0bb4ad8 | -11.176 | -54.01631 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd2c4b7b-a361-35cb-a195-9d57d7ec9115 | -12.25641 | -43.17049 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a042d6ae-7d34-3d1b-8adc-7a222205d62f | -12.00595 | -53.43407 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e1e5581f-1a36-377b-9b1b-72386df78fb3 | -13.94233 | -53.85423 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fee67ebd-c80f-3dcd-abcf-3ddf640ef68e | -14.31551 | -51.8996 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d110941c-40e7-3494-aa01-af2bfa2ef847 | -12.51868 | -54.76612 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aedc26c3-970c-3d42-996d-9433efe6db28 | -12.49512 | -54.75829 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a2ffab0-7fbc-3e19-9812-eedba48b24f4 | -12.76139 | -48.46686 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69857b94-693a-3d69-89c9-0275d5e15e98 | -12.73323 | -48.47555 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04447dd6-cca9-3995-af38-8f96be81dea8 | -14.3173 | -51.90388 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e2d08d4-8dcf-3072-bb62-50416e34313a | -11.16736 | -54.02637 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b5afc4be-4244-36c3-a4ba-c6e4892a0dac | -12.91521 | -56.63083 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| b5e33fd8-e504-3935-8bbf-adb8466fb3aa | -17.93923 | -44.39915 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acfd83d6-2a3c-3320-9d95-e77d834c3688 | -11.38644 | -50.7186 | 2026-08-21 04:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d79eba2a-e002-3e4b-ad27-8920744bedd2 | -13.3906 | -54.37806 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| bbd8d1f5-28fe-37d9-81aa-064dd9325539 | -11.1998 | -55.05866 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62f30e41-4cc8-3b26-9c02-82faaf830898 | -12.91896 | -56.63149 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| eedd2ea2-756d-3eb2-9578-24f96ce38f78 | -14.44267 | -51.81547 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06ea6549-d94c-3f97-bf2c-a26f5d04e8ed | -11.19883 | -54.00482 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cfecefe-0e72-3f6a-bbdf-8f324aff8c23 | -11.20624 | -54.00225 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8f6c7a4-84a7-3592-a006-f0ec592db456 | -11.1732 | -54.01202 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| af9eb2df-edbc-3435-b39a-1c9b1477c373 | -12.50958 | -54.75671 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85704f2d-67db-32e4-b1d2-db6a2643974f | -14.00943 | -53.66964 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b206f684-f3a2-3600-9b59-3774b3bb3899 | -12.74843 | -48.47748 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 447a0fc8-3bf8-39dd-9070-d14faf64e3f1 | -11.16858 | -54.0189 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README50.md)

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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7aafbcf-bffa-3b0b-9551-d38499fffda4 | -12.69078 | -46.95812 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc192beb-fd9d-3c59-99b1-ed0a6c072342 | -12.01925 | -46.48323 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 313a821b-a2e3-3834-943b-4b79e028c31b | -8.0901 | -45.44529 | 2025-10-19 04:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d1d5998-cbcd-3775-bc69-f9dcc0fe6a2d | -10.89114 | -46.07436 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a93eb1f8-320d-3946-ae86-e408da64bda5 | -7.9552 | -43.86449 | 2025-10-19 04:12:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 58a2bbcc-fca8-3144-ba0d-c901431bfed6 | -12.31693 | -41.38798 | 2025-10-19 04:12:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 399f1c3a-9433-3134-a0a7-a13fa39f8873 | -11.40902 | -47.6954 | 2025-10-19 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42a7d835-5a98-36c0-99bd-01a1b82d3f20 | -10.8592 | -43.94651 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7db4b525-891b-3a69-9c94-8de864651b49 | -12.14596 | -45.06439 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09d3efdd-1293-3c63-845d-ff683a4edf4e | -8.00939 | -45.14826 | 2025-10-19 04:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184480e8-ec4f-3ccb-948c-2d5d0fe577d7 | -8.49635 | -44.14847 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cfbe37e-6e42-3d3c-972a-6771f06ddb11 | -10.68929 | -44.53974 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfcb83db-9753-3eb9-ad17-e7269c3dcf9c | -10.58033 | -41.5024 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a01a8e11-b339-3631-b0ee-e58a1825d0e5 | -10.88746 | -46.07376 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f333b5d2-d551-3eb8-826b-728b9911839f | -13.71173 | -40.98397 | 2025-10-19 04:12:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 53a0d378-9c96-39ea-bbcb-071a33c979ad | -8.21161 | -43.95825 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32b999a1-ec56-3466-8b5b-4861ce373a5b | -13.89168 | -45.50957 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f92a401-b923-3400-b08d-357dedbdc181 | -11.34543 | -47.27822 | 2025-10-19 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 551031ad-c1a0-3286-86a9-1c1c686a2597 | -11.98045 | -46.92881 | 2025-10-19 04:12:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43742690-8bd9-3e10-9ca8-5f0025a4408a | -11.65223 | -47.31494 | 2025-10-19 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dedc2b1-236c-38ef-a8ad-dbbeab403339 | -10.67586 | -44.55695 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 254d760f-e212-3f87-8aeb-05fa25d00869 | -12.1433 | -45.07286 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 897dfe93-2803-3234-b448-ae4f29a40288 | -11.67864 | -44.96022 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4971dd9-b0f5-3b84-8893-2f8131100ac4 | -7.63092 | -48.39473 | 2025-10-19 04:12:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbe394e5-a79b-38da-99fc-0f54239b53ae | -13.18121 | -46.44244 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b84774a-012d-3a46-b9ba-4cb6b40c8a6c | -8.3169 | -49.49244 | 2025-10-19 04:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16f59c09-f449-3e76-891b-0d069471c181 | -11.62716 | -44.08018 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8f6c309-6692-3825-9e78-ce531d3945f5 | -10.49523 | -43.93166 | 2025-10-19 04:12:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a12d689b-0037-3910-a562-ec1ea2e18048 | -11.35014 | -44.27966 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa66aa1-7157-3e2b-b0d0-5b7ff2a87f97 | -11.64898 | -47.31136 | 2025-10-19 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b23baed3-9964-33ad-8272-2e1702177c99 | -10.86714 | -43.94035 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cf014ae-7c62-329c-b0ad-55fe694616f3 | -9.21987 | -46.05893 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f860c61-ab74-3655-9a7e-36e7dbd88d82 | -9.26387 | -44.34121 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e8d8d66-efea-37aa-983d-38b6e9c01229 | -13.27019 | -46.48832 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01e83f26-43ac-3001-beab-caced3edc4e8 | -10.87111 | -43.93727 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e5d0c9c-529e-3ae7-81da-1fe756b59c63 | -10.88756 | -46.08598 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 12a58ec2-6f67-358d-80ac-ea093dffd42b | -8.55326 | -44.57626 | 2025-10-19 04:12:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ac66955-a2da-3d27-8763-a820490cc70f | -9.25349 | -44.33951 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23f2d485-9551-3b6e-88b0-505db294e5ba | -8.56334 | -48.51604 | 2025-10-19 04:12:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af09465b-558b-32c1-8e34-ea8700cb50fe | -8.24393 | -43.99832 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f2af290-cabe-3b56-9e2a-593662ffe88c | -9.90582 | -45.95708 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7225335c-fdf2-39b1-a38f-59e293f2e90b | -11.47297 | -42.22236 | 2025-10-19 04:12:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| afe43f65-68ca-3827-9e18-119e7b57bbc7 | -11.41872 | -41.4226 | 2025-10-19 04:12:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 450338b0-b753-37bf-9594-8968ce7a2d21 | -8.89758 | -40.60684 | 2025-10-19 04:12:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b6c1ce5-d4d9-372a-9a65-d13f65ad1ef0 | -12.18592 | -45.10262 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f42747a3-ac89-3bb8-ba48-8f8b4fe44687 | -11.89441 | -45.44209 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f4f9e09-9b6b-3002-bb43-ded33a2e1bc5 | -11.00354 | -47.92015 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26a42ced-b8fd-3ae3-835f-4ee99d7d8005 | -12.49792 | -45.41956 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d1419cd-3c08-3d21-87ec-4b97fc747034 | -11.98424 | -46.92956 | 2025-10-19 04:12:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 335daa13-e70c-3642-a58f-21bb668bf8c9 | -9.94124 | -47.66154 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 310eeffd-cb73-3f90-8141-89f111ed2492 | -10.22742 | -44.04981 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6643c4b9-8f3f-3ad7-bed8-0fd17875ebee | -9.21236 | -46.05766 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0f26682-e09f-3b3b-b190-e8a9a5cd36ab | -11.00528 | -47.88559 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f31bcfbe-0736-3c72-8f28-f22b4f95e86c | -10.68461 | -44.54673 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 092731e3-98ff-3e77-8370-a5bf104bbf36 | -13.02795 | -46.9554 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edeefc90-467e-3cb4-91ca-5695b1dba964 | -10.89041 | -46.07873 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 76842a6d-1d09-3276-9813-0409a7abb7b6 | -12.14803 | -45.06575 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db16607f-15b2-3701-9ac5-17864c85c3ad | -7.81643 | -44.91354 | 2025-10-19 04:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98eaa09f-bcce-32f6-9fa1-844c9ed2efe6 | -8.29792 | -43.3867 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 558dbf6b-4fd7-32ae-8f89-3be71977cf11 | -12.98527 | -47.28672 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1842fdd-f094-3884-859e-485f58a5396b | -12.95286 | -47.30313 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68b76dcd-6c65-3ed5-a732-e26967b8f65d | -11.6367 | -44.08551 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70ed2c6f-5c40-3b35-8be5-48d5a21ad86a | -10.43089 | -45.01355 | 2025-10-19 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d629880-10c3-3fd2-adfa-f85af4275ba5 | -13.86005 | -45.46405 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7014fea-b09d-3bb6-bb07-6c49392a7fef | -10.86811 | -44.61954 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afa139fc-96fc-3d23-93e6-f41f0dfc0ec4 | -9.98407 | -47.05688 | 2025-10-19 04:12:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| dc01ac13-90d5-30e0-a904-aa4157e138c3 | -12.01554 | -46.48261 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa381f22-0edd-34c2-ad5a-9b773734d224 | -7.65403 | -46.66154 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2e629ac-d5da-3c8a-bc74-65403e5d3187 | -10.30205 | -44.0436 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 379e3672-5f2b-3707-aa9a-f79eb4e9b33d | -9.988 | -47.05759 | 2025-10-19 04:12:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1724067c-3249-3f1f-a221-464199bd801d | -13.39889 | -42.80881 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a11df03-acfd-3146-84da-158843194878 | -7.59497 | -46.06744 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9e3538a-fcda-31ca-ac67-7db3575f1063 | -10.91351 | -43.8252 | 2025-10-19 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| befabde1-23af-3128-9db9-6732ce6fbdf4 | -10.23368 | -44.89709 | 2025-10-19 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d71eedd-4b75-3dcc-8056-9c907de5adf8 | -11.62379 | -44.07962 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce94c936-ccbc-38f6-bc10-4132e6c5800b | -12.45761 | -45.44522 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6969d5a4-1e6d-3b99-a2bc-7cc5253269c7 | -9.21611 | -46.05829 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2dd54280-e84a-31d3-9fc3-8abe8eaf5f78 | -8.44368 | -44.16644 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1021d430-6577-3bc1-91c0-d8b4868e3439 | -10.86317 | -43.94342 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a66cebfd-f187-3b7b-a2d6-1fb2fbb481c5 | -11.64287 | -44.09029 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd2fb112-de10-3839-889b-2888a84fbc1a | -12.98186 | -47.26141 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d03ca8ff-e6f0-361e-bdf4-2468c7d9663b | -8.34795 | -46.20998 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d667883d-2a24-3709-88d9-d489fd4f27aa | -8.34719 | -46.21455 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f114c024-934d-34c0-8834-269406c4547a | -8.42665 | -44.14026 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e025dbb4-d973-3f4a-8f7c-4d64c98dd2d7 | -10.88823 | -46.09185 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5c4d7b30-a3fe-3a62-a307-5a435f88da0f | -12.19001 | -45.09945 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 768c6451-3fe9-3110-a686-5f56f77752a7 | -8.42949 | -44.14461 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bc20388-8ebf-38b2-821e-5ee5f0766860 | -7.80124 | -46.79247 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f5c75d1-e9bb-3912-b4aa-b75e617bd51c | -11.78309 | -47.5539 | 2025-10-19 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4c5a93a-c085-3e08-9839-b9af4c1c9426 | -8.42763 | -44.15596 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bcc1c38-94f2-3594-a5dd-7207d563c98b | -12.46177 | -45.44188 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af9162fb-0db5-3867-8f91-373bc2f13b27 | -9.2191 | -46.06351 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be054f2d-aeee-3ecd-a98e-d76e58e73b5c | -14.13992 | -43.17691 | 2025-10-19 04:12:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7aa8acc1-1315-3fab-b72c-8afc234d42b1 | -11.65134 | -47.31992 | 2025-10-19 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d85e0980-96f7-36ef-9594-6f6a437cf165 | -10.89187 | -46.07 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b3f9ac60-acbc-313d-be3a-0092a424a14a | -8.43355 | -44.14152 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1278a40-7b48-3679-998e-09b828d5741d | -12.18308 | -45.09825 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05ee3f99-7091-37be-a55e-aabf2436f4a7 | -11.47352 | -42.21883 | 2025-10-19 04:12:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c10a811a-1e56-38b4-b3fc-b446b6e430ab | -8.20606 | -43.95818 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5d694c5-cbcd-3118-87cd-9a1428600bc2 | -9.22362 | -46.05957 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README31.md)

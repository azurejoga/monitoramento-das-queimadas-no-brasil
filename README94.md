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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f17e4b3-520a-36bf-af33-06136d330618 | -20.35509 | -48.86151 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 47.2 |
| b200d5a9-aa05-3bd2-b9f0-12201328a01c | -20.35472 | -48.8679 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bb419ff3-e73f-3b08-9aee-454f25fb2784 | -20.35468 | -48.81972 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dafce68c-c443-3d7d-a093-676b9617abbf | -20.35464 | -48.8202 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f6d315de-d455-3892-87e2-fdaaff3184a1 | -20.35154 | -48.84996 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b5eb53c2-620e-3c21-94be-2b8f8b3a04cd | -20.35138 | -48.84944 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 80800b93-985e-347a-9b45-d912bb8476f6 | -20.35094 | -48.85577 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 579c9673-a98c-32a9-9da5-3a4da231da66 | -20.35073 | -48.85524 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 37deda2a-4892-35dc-b75a-08e3ecf2ee13 | -20.35034 | -48.86147 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 543689df-b341-38d1-9ab3-1efd2b9a5b4b | -20.3501 | -48.86093 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 47.2 |
| f041025b-04a6-3997-9c77-fe880e4c647f | -20.34974 | -48.86729 | 2024-10-08 04:59:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d31e891c-fb2b-3d79-8d4f-6cf0eff6685e | -19.76166 | -48.28428 | 2024-10-08 04:59:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d3ff968-b175-3ee6-8e23-60d3730b9aeb | -19.76131 | -48.28752 | 2024-10-08 04:59:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4b0cf50-2538-3f4a-a882-a31a5876f650 | -19.75652 | -48.28367 | 2024-10-08 04:59:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0e347b9-928e-3521-8c27-5dae1999fd5d | -19.75618 | -48.28683 | 2024-10-08 04:59:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3ab616c-59d7-30ed-bde4-508fff559941 | -19.5526 | -49.49526 | 2024-10-08 04:59:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff3bb801-f208-3195-aa6f-12cef9ca7957 | -19.54892 | -49.49042 | 2024-10-08 04:59:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0e79e7f-9f52-3989-adfc-15b7cd9d93a5 | -19.54849 | -49.48943 | 2024-10-08 04:59:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdd2a9dc-7b32-345a-945f-8ed0f3c3bfb0 | -19.54833 | -49.4957 | 2024-10-08 04:59:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75beff24-3610-3e34-a37d-f9326cf6d48b | -19.54787 | -49.4947 | 2024-10-08 04:59:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c4e5b24-03d0-3b76-ab7c-e43e943f72f1 | -16.41145 | -49.92871 | 2024-10-08 04:59:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bff68c26-406f-3d7f-8fdf-96e1c67baae5 | -16.35284 | -49.57029 | 2024-10-08 04:59:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a6a0a19e-8b4d-300e-81e9-ea3d2cd2952f | -16.15201 | -49.31347 | 2024-10-08 04:59:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84086527-8bfa-3a67-960c-09e5f2d056d8 | -16.1474 | -49.31311 | 2024-10-08 04:59:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c0a7204-d5ef-3e8d-94af-31e8984e1b2c | -16.35398 | -49.56091 | 2024-10-08 04:59:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| cc09163d-1bc2-374a-8414-b54e49bfae9b | -16.34951 | -49.55994 | 2024-10-08 04:59:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| aeb1dc04-f417-3d11-8430-2ed314ac87e1 | -16.152 | -49.31666 | 2024-10-08 04:59:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17b5e1ad-f511-3f03-8815-f882eab1ca96 | -16.41587 | -49.92921 | 2024-10-08 04:59:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 91c0d54f-5c2d-3ace-9ff0-87b44bb3547c | -16.40717 | -49.92923 | 2024-10-08 04:59:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8765b7f3-28e3-331c-ac1c-5ce0c6c7cc6e | -16.40705 | -49.9281 | 2024-10-08 04:59:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c0f739b-31be-3ce3-9b86-c8b35eddea75 | -16.40653 | -49.93234 | 2024-10-08 04:59:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f8ada8a-ceeb-373d-a028-1c6976039ac6 | -16.3534 | -49.56566 | 2024-10-08 04:59:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| ea85da0e-3a11-339b-8051-0f0dd5d02129 | -16.15259 | -49.31205 | 2024-10-08 04:59:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a881e082-e715-3b76-b133-3de48eeba88e | -16.14798 | -49.31173 | 2024-10-08 04:59:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5849a73-1375-30fb-84ec-406714ce0a02 | -17.58719 | -50.45735 | 2024-10-08 04:59:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22769ac5-cfbc-3dcc-bb3b-b82bea6f176e | -18.99988 | -50.23421 | 2024-10-08 04:59:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23489e19-5847-3403-896f-b74383c934ea | -18.99933 | -50.23878 | 2024-10-08 04:59:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4471826c-040f-3c1d-b56f-0944d1054ba2 | -18.99878 | -50.24331 | 2024-10-08 04:59:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d287348-566a-36b3-a3e9-f301b0f5330b | -18.98531 | -50.20432 | 2024-10-08 04:59:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38b1f9c8-004f-3612-a78e-396193915c06 | -18.98081 | -50.20394 | 2024-10-08 04:59:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c594056f-4d5c-322e-bc56-5cb1e8975376 | -18.97578 | -50.2079 | 2024-10-08 04:59:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86b139c3-b87d-39c8-a3f1-628519b222d7 | -18.9558 | -50.26119 | 2024-10-08 04:59:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 074c7885-bcdb-32a5-8b44-ff198ab663bc | -18.95133 | -50.26057 | 2024-10-08 04:59:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5a66664-86c2-37bd-871a-25f1f9c833b9 | -18.28575 | -50.542 | 2024-10-08 04:59:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4653ec9f-21f8-31a2-81d4-539a252957bf | -19.71589 | -50.37762 | 2024-10-08 04:59:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 365b7516-d506-3c32-b6f9-0fbbac524d5e | -19.71533 | -50.38224 | 2024-10-08 04:59:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 1671f169-1007-38ad-95db-ca2e8eb02a06 | -19.71086 | -50.38165 | 2024-10-08 04:59:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| dd34d270-2e85-3b39-a63c-89dbfd0dd065 | -16.6481 | -50.60209 | 2024-10-08 04:59:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bafcca9-05f2-3800-9577-cfbf68fb8c59 | -16.64387 | -50.60148 | 2024-10-08 04:59:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbf3c4fb-ad59-3be4-87bc-dce4ec7031ce | -16.4569 | -51.80665 | 2024-10-08 04:59:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11fa835a-2aed-355b-86e1-1e9b34f7a95c | -16.41328 | -51.8934 | 2024-10-08 04:59:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e38ad154-2d86-3d4b-9920-d211dd83470c | -16.41005 | -51.88801 | 2024-10-08 04:59:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 633d92fe-9715-3b8b-af98-4cb3a708fd76 | -16.3077 | -51.45626 | 2024-10-08 04:59:00 | NPP-375D | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ef3038d-0873-357f-92a1-eac3e9962371 | -16.30636 | -51.45488 | 2024-10-08 04:59:00 | NPP-375D | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec82b924-a627-39ea-9b9b-098e257cb5a8 | -16.30441 | -51.45037 | 2024-10-08 04:59:00 | NPP-375D | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11012c0c-1e87-3b7b-bfdd-9766b7fe6df4 | -16.30373 | -51.45564 | 2024-10-08 04:59:00 | NPP-375D | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc947a4c-93a4-3967-a7ed-4e77cb08f476 | -16.30305 | -51.46085 | 2024-10-08 04:59:00 | NPP-375D | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bd9ab10-b38e-3e66-a736-75298274695f | -16.30238 | -51.45428 | 2024-10-08 04:59:00 | NPP-375D | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 571aa53f-d8bd-3635-8fee-c9cc29a02097 | -16.30167 | -51.4595 | 2024-10-08 04:59:00 | NPP-375D | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe359a56-41aa-333b-b5b4-31ad965f4407 | -17.9847 | -51.6207 | 2024-10-08 04:59:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f4e3a31-98f6-39d4-a3ba-ef276bf89216 | -17.36441 | -52.00369 | 2024-10-08 04:59:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be34fe0e-70b1-38a4-8bdc-ab100d20e956 | -17.36051 | -52.00314 | 2024-10-08 04:59:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 93b335e6-ad96-3fa6-acd2-20d7d5308cc8 | -17.15779 | -51.70167 | 2024-10-08 04:59:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bbcc0e9f-e06b-3e83-bbee-92449c15e83c | -16.81227 | -51.2534 | 2024-10-08 04:59:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cc35cc9-1852-3102-b885-23efdb7779de | -16.80774 | -51.25648 | 2024-10-08 04:59:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de4dcfe9-d63a-37cf-8136-b30df74d90c7 | -19.40241 | -51.68271 | 2024-10-08 04:59:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86e284c3-8fbf-38ab-a218-d7e1a6e82ef5 | -19.38934 | -51.6937 | 2024-10-08 04:59:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6420424-e181-332e-9db4-b94f32feece8 | -19.38885 | -51.69744 | 2024-10-08 04:59:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1da8e183-9b2c-3a63-92ca-94ef5c94f0ea | -19.38868 | -51.69273 | 2024-10-08 04:59:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a087b7f-25c0-3d64-a7a7-9391c8a8d143 | -19.38821 | -51.69647 | 2024-10-08 04:59:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4688441f-ab32-3566-9f0b-a5d18d22461b | -18.54842 | -52.63861 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e877bf5f-a7a6-369a-afd5-94dae182befe | -17.66408 | -53.09631 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73b5d76b-cb73-3c98-a956-ba6f7fc12fd5 | -15.92433 | -52.23943 | 2024-10-08 04:59:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6ff4b9c-975a-3d3a-8d48-992c5bf60fec | -17.84448 | -53.77151 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 342e75e5-79e8-36ee-93c6-946f2966092a | -17.84149 | -53.76678 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f820f80-42da-3fd9-a126-4481b4bec059 | -17.8409 | -53.77102 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86528f8d-7a88-37e6-a755-37ea1cfbad1c | -17.83732 | -53.77052 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c544d22c-e8ce-3e2a-8948-754bbab010fd | -17.83373 | -53.77001 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88f717e1-6095-3cf8-b2f8-37230c183fd6 | -17.81641 | -53.76328 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b2c022f-8b2f-3a29-976c-0109c54dbd73 | -17.81545 | -53.75603 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1f5e984-9218-3ef8-8444-6712742892e7 | -17.81482 | -53.76034 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f4460a4-cc16-3818-b7fc-66bd1c7641b8 | -17.8142 | -53.76467 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 706373d8-5276-3ea1-86d7-f4428b5005f9 | -17.81186 | -53.75552 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fd247e1-4d62-3fb4-bc5a-95a98e4fac71 | -17.80828 | -53.75502 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58466863-8f7a-35e6-b163-f94cacb22ff2 | -17.80763 | -53.75948 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07697fcc-e423-3d8f-a585-66240486535d | -17.80593 | -53.74595 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5bd0c2a-5593-3611-b25a-3d770cb49557 | -17.80531 | -53.75021 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74ff7460-8407-36bc-bb9c-0c18f2154183 | -17.80469 | -53.75455 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e63e0087-553e-3dd5-afeb-e48cb4b774b1 | -17.80404 | -53.75908 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aec36dfb-b300-3f7e-bb62-4997cb020086 | -17.80172 | -53.74978 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d096884b-eda8-355f-a3fb-f09dd46c309a | -17.80108 | -53.75418 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecd37180-2e63-3f8d-9672-46e1cb1b9b21 | -17.78801 | -53.74334 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fc5b62e-a4aa-3dbb-9371-d24e6b1ccc68 | -17.7874 | -53.74767 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f483df10-e1c8-357f-9afd-dce9ad3212f9 | -17.78442 | -53.74292 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3251a218-c08a-3b74-91d2-dd92cefdbbcd | -17.78082 | -53.74252 | 2024-10-08 04:59:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6bfebd2-dac4-3d47-9168-d876bc30cb52 | -17.79242 | -53.05801 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de734362-8793-3e90-9bae-79aa11cd9f18 | -17.78873 | -53.05739 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc92e007-9e3f-32c6-a7fa-1f223b8f4b29 | -17.78543 | -53.10774 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38788714-d759-33df-9293-b763a913081b | -17.77945 | -53.06974 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9926a5b2-c6c9-336e-a342-8f195ccf2a61 | -17.77829 | -53.05101 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README95.md)

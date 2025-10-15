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
| 9e3dd336-a83f-33b2-8714-31e92fdc201e | -8.97302 | -39.92106 | 2025-10-15 03:47:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90008787-0bfb-3d6e-94b4-7e1009b0650c | -4.89586 | -43.46539 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9fb73c34-5d99-311d-be76-f1d15f7d1bf7 | -6.07182 | -44.30511 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 349b40d7-0525-3ee9-95e2-b8813cae33c1 | -8.2487 | -43.34558 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 01fa4a5f-ef6f-3072-b00a-97744bc5188c | -7.5724 | -42.71122 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f4c9df6a-4454-393a-b51e-1e789f5d339d | -7.15983 | -42.50679 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47e9595b-8401-378a-8840-cd49130b7aca | -6.145 | -41.75008 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eaa0e5b9-17de-33d5-9fa7-f8ef10262a74 | -6.05267 | -41.90554 | 2025-10-15 03:47:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6cd20ee3-1419-31af-b572-78088a181db1 | -6.91456 | -38.2628 | 2025-10-15 03:47:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7cc249d9-9f51-3ed3-9cb3-117335f3ff84 | -5.3459 | -43.75158 | 2025-10-15 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1cb5f8a7-3d33-3f86-967a-a1e12a01dd9b | -6.19439 | -42.5994 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 34c643fc-ca86-3986-86c4-c6164656e190 | -9.26105 | -44.36396 | 2025-10-15 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cec1cb9-5d45-3471-9e59-42457733394a | -7.93364 | -44.13586 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e123df44-ec77-3291-8117-c3707dc1dfe1 | -4.66214 | -43.12842 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0907ee67-1e47-3e11-8fd3-5a7f4c3f1452 | -9.17175 | -40.30857 | 2025-10-15 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e41f350b-8da2-39ff-b834-a08eff7a801c | -5.4603 | -42.36613 | 2025-10-15 03:47:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b26d732b-5c25-33f5-8ec6-d97c259e3a0a | -7.93876 | -44.1368 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c77042f-3d5a-3bb6-ac83-bc70e1b35491 | -7.64276 | -42.58419 | 2025-10-15 03:47:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 95bdcb66-52af-39a9-a570-838b0fd40d4a | -6.21668 | -42.49974 | 2025-10-15 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88ef069d-a881-317c-bafc-930ec4b25b89 | -8.81191 | -37.34174 | 2025-10-15 03:47:00 | NPP-375D | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 599e182d-2a13-3a21-ac68-f168f2b3b51e | -5.40125 | -41.15442 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 07e41824-c6b4-3a08-bb1f-5de90c17d721 | -8.21055 | -44.01448 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4da5a519-f03b-374f-ae4d-135cea3c75fc | -5.43142 | -44.22076 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5a0ad8c4-da05-3deb-bdf0-dc507e5e647a | -7.08288 | -41.94628 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1c7210c-26b7-3ea7-a060-40f22cc8ab6b | -4.65609 | -43.13344 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6460b3f3-7c6e-312e-9df0-a1b1bfd0cf0a | -5.98228 | -42.92279 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d589d50a-73af-3310-b3fd-64d6f495e29c | -7.57125 | -42.69062 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| db62df34-b786-3589-8f03-93b1faeb1afe | -5.79467 | -43.88835 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a7fab3f-f32c-3809-a52a-0863aba00a7c | -7.95033 | -44.14413 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4a53beb-9240-36d3-a04f-3ee10c59773e | -6.16526 | -44.38386 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b61af6a5-835f-3861-a8e3-7e32c3369deb | -6.15482 | -41.71975 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c0c222ff-9c7c-3472-ac50-e02c5928ee95 | -4.82645 | -45.44892 | 2025-10-15 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b492922-99ca-3d86-9347-4c7ee6503704 | -5.5648 | -42.99609 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2f9a15f8-3e4c-36a0-82d3-df127eb13b7e | -5.94738 | -43.75213 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e49ecbfb-dbdf-3655-b411-ff5c972273eb | -10.79742 | -43.95018 | 2025-10-15 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6d30654-26ac-362e-a55b-ae0103b3bf65 | -8.20075 | -43.99046 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3132dc45-5863-3bcc-87c0-d6697d539b9a | -6.06047 | -44.08924 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9204135d-6515-377e-b3ce-393a435b7b96 | -4.91128 | -46.70827 | 2025-10-15 03:47:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 630c93d3-8218-33e2-96e6-04e0a36e9996 | -4.90154 | -43.46314 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 32587fda-8cb7-3ccd-bc06-e6ef328a4b82 | -5.9155 | -42.83126 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 27cc1061-cea0-3f48-ab4b-2a8c42bddb72 | -5.56719 | -41.31586 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9789d59f-c989-3273-88c1-b0f249c60f28 | -9.25596 | -44.36311 | 2025-10-15 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ba541ec-7a0a-302a-857f-5173afd14a7f | -5.4322 | -41.34283 | 2025-10-15 03:47:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 27d2b0e6-839d-302e-ac1c-de3b07dc567a | -8.20477 | -43.99725 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7af9e531-45f1-3226-a9f8-4259217d79fd | -7.74948 | -42.45351 | 2025-10-15 03:47:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7139fea1-4815-30dd-a798-d453f925462d | -5.67505 | -44.25696 | 2025-10-15 03:47:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51dc9d96-b3f3-3d0d-9d14-8683495f5ca7 | -6.22906 | -44.16723 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 71048c32-f4fc-3046-99a0-c4f4cc1ca4b8 | -5.84178 | -43.9589 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fafebb9-d8e9-379d-8b24-c3b944895e58 | -4.64273 | -42.81838 | 2025-10-15 03:47:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3442d9b-5dc1-397f-b87b-e6682f9e7e50 | -6.53361 | -41.47971 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e243c292-5982-388b-8a34-c7f8ae476a01 | -6.17527 | -44.29483 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36bbc70d-d2b5-368e-a0e3-dcc8b4c3ae10 | -5.42354 | -44.42826 | 2025-10-15 03:47:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f75aaac-ac3a-3f2e-9256-8afd0e9c74a8 | -6.17 | -44.29351 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b6a6ed9-d1d3-32dc-a83b-e50e1bd1b4cf | -10.15015 | -44.91755 | 2025-10-15 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 940e58a3-52d8-3b64-a67f-88faaef25a2a | -5.91782 | -42.83283 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9ae10dda-a280-30b7-9c5a-e01c47aafb08 | -4.25907 | -45.58644 | 2025-10-15 03:47:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 210836fe-3ed2-30ab-b7b9-d151a48d0297 | -6.21946 | -41.55498 | 2025-10-15 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f12f9ed-6f9d-37cc-81df-3e71a81514b7 | -5.91392 | -42.82664 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6ddae44f-1940-38bb-b6d7-98f2372e770e | -7.55199 | -42.71746 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f5471689-4aac-3fb7-b774-83e5da0e9d7a | -6.07238 | -44.3019 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e80e515b-309e-3275-9c0f-f6bd71854605 | -7.57415 | -42.70135 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| daf86a43-c78d-352b-946a-596cbaf1c9ad | -7.02412 | -42.73187 | 2025-10-15 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1b368527-13d7-3030-8ede-bbec8a312962 | -5.86923 | -43.86306 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5c3da9c6-4ad4-371a-8d69-73d9bd4271e9 | -6.26 | -44.02508 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8e19674-c1d9-3542-b1e5-4d2e9f209204 | -7.9525 | -44.14871 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d355b204-21d9-35e3-b94d-1f9b43613e84 | -5.34637 | -43.7483 | 2025-10-15 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26392940-5150-3aba-a661-88538b6f2a69 | -5.91965 | -42.82248 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4f641767-22a8-3ffb-94ef-48af57ef4e05 | -5.86465 | -43.85862 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb17a40f-4641-3f18-b1ed-135029753b11 | -10.84725 | -42.76043 | 2025-10-15 03:47:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b0497a65-3eaf-3c75-a650-a374c88159fb | -4.807 | -45.71649 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb245264-5515-3756-8fa3-a58a97a802df | -7.56431 | -43.89654 | 2025-10-15 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a21c8d7-195f-3cf4-ac18-cf6f9057be6f | -7.07688 | -41.9543 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b68b4e7-f290-332c-93aa-d7dab8bfd533 | -5.44211 | -44.2229 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35ec5c4e-364d-3fb9-b947-51ad80fcad44 | -7.36466 | -43.64162 | 2025-10-15 03:47:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1432f94a-54a3-34a6-97c6-21ecc85073c2 | -4.83966 | -42.77429 | 2025-10-15 03:47:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 909cbaf3-f855-3faf-a8e0-8956bf8e67a6 | -5.87191 | -42.82341 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 783af5cd-9645-3d26-a472-feab86abd8e0 | -8.28579 | -43.41794 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 71759633-b6e9-3785-b774-2a13a8fbef5c | -8.20024 | -43.98531 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d811c1d-daa5-3ac4-9bb6-154fa3573ade | -8.20439 | -43.32559 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3296f0c6-23de-359f-936d-f0fa19cd86e1 | -5.28257 | -43.24089 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b3594fb-607b-3046-8060-c8cec9a684a4 | -5.91638 | -42.82605 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5f6ee312-fa6b-3629-8427-b0747b53038a | -7.67374 | -42.37936 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc76bec8-4f5b-3def-92d0-47328d6ba4f3 | -6.45823 | -41.83974 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3f0a5aec-0d15-3c59-9aa1-1d44c2ffaa03 | -7.15765 | -42.49152 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6b25cb90-4424-30aa-9c28-203367c3991c | -5.8617 | -43.87336 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc57074a-ce01-34f6-9806-1ed5c8ae27db | -8.21109 | -44.01152 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 599aba58-43af-3cfa-9ec8-c71f2d9abbd8 | -5.58774 | -42.84394 | 2025-10-15 03:47:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3e4e4537-12b1-3136-9fb7-d3848ad1b139 | -6.17714 | -42.61377 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a03397fa-2f28-36a6-bf67-757a88e8823c | -6.84386 | -42.78032 | 2025-10-15 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bdec490a-85d1-3dc1-bf4f-5690bcecb791 | -8.21345 | -44.02721 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fe77d93-3b3f-3db8-b546-68227551e8c7 | -5.25326 | -43.47456 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 734f4893-e658-3d67-ba5e-050298965ca6 | -6.23077 | -44.15774 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8600408d-2edc-3267-897c-6c0c752a91cd | -5.86524 | -43.85527 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18b91bcc-809c-36cd-988e-07a6332bb6a0 | -8.22073 | -43.31737 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c7e4054f-a0d8-3dc7-be33-96660dbd1856 | -5.43084 | -44.22411 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 84595e48-99f8-30c5-ab47-fa6145f83976 | -9.91134 | -36.385 | 2025-10-15 03:47:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 16bece71-16b3-309e-93c6-b2a557f05464 | -6.45962 | -41.85849 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fe010fe5-4467-3426-b882-5a9f9ef5dc95 | -7.08057 | -41.95961 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 487cb7ce-2f1c-34c0-821d-5e03f6633f69 | -6.05799 | -41.9017 | 2025-10-15 03:47:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f1e871f7-48e7-3f0d-a21c-b24b9efa1ccd | -6.23124 | -44.16101 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README16.md)

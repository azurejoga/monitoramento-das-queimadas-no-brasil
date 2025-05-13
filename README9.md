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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b117cfdc-f2ca-3b04-8c32-7b108a73993f | -13.9902 | -56.8058 | 2025-05-13 05:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| eeea0736-3752-3289-b5e0-5d1eecd417f6 | -8.0889 | -43.1196 | 2025-05-13 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| f65b0d92-59a6-32a6-9753-12f97db2bd36 | -13.971 | -56.8077 | 2025-05-13 05:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 184d67ea-6eb0-3b4b-863d-1530ecfe7dd3 | -13.9905 | -56.7855 | 2025-05-13 05:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 6aadaadd-2878-34f1-a870-6c591e3ec8b9 | -10.66542 | -44.41122 | 2025-05-13 05:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f9f20ef-9c0f-33ed-b12e-bb8340b4a9fc | -11.58147 | -47.60859 | 2025-05-13 05:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0517c14-c91b-3050-be11-3927aeda1075 | -8.7918 | -49.80368 | 2025-05-13 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80026bcd-5dc0-3f11-98fa-ae0711c2288a | -11.0065 | -50.76638 | 2025-05-13 05:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d39ac95-ac23-333c-abfd-73f995c2f033 | -11.58601 | -47.61599 | 2025-05-13 05:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c3f5ce6-9e57-3269-b72f-26ebd99b1a15 | -7.58873 | -45.86323 | 2025-05-13 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34ae4b78-b908-3e3c-b568-0824c52bf3ce | -10.49027 | -46.18147 | 2025-05-13 05:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71b3195f-9a03-3d75-b193-19ac5b991ef8 | -8.53039 | -54.99189 | 2025-05-13 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 612c5c48-f1dc-3cd9-b94f-809fba3532e5 | -8.79564 | -49.80872 | 2025-05-13 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9fb7a27-e5bc-34b9-9767-dba386f80eea | -10.65892 | -44.4104 | 2025-05-13 05:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b178234-3556-3d48-89b6-3141774366e7 | -11.80103 | -44.27557 | 2025-05-13 05:04:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5823e0a5-e4ec-365e-8480-aca7e0a945b1 | -9.2485 | -56.32948 | 2025-05-13 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33dd881f-28ca-35d5-b34f-f3f0e6dd6628 | -10.49607 | -46.1823 | 2025-05-13 05:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d56de95-f1f9-3965-a8d0-852d12aee820 | -8.31051 | -48.05359 | 2025-05-13 05:04:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 356e827f-0cdf-35dd-abaf-56f5f40dfe52 | -9.76213 | -51.98017 | 2025-05-13 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93affcb4-bbb0-3743-a8e7-b9def045d2c1 | -8.7912 | -49.80809 | 2025-05-13 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23ba6520-f15f-381b-a619-2d1784791b1d | -10.4966 | -46.17811 | 2025-05-13 05:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd918bde-a929-35be-a2f7-33a64ccb070d | -8.15629 | -49.78687 | 2025-05-13 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1904e098-e212-39b1-b06e-809b0bf9e99a | -11.00704 | -50.76227 | 2025-05-13 05:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b7b4b99-28ad-3929-9af7-bd132e159f9d | -7.59495 | -45.86006 | 2025-05-13 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa13f51c-08ea-364c-9506-299aaeda7b87 | -11.8004 | -44.28144 | 2025-05-13 05:04:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd493ef8-9132-305c-ab87-9f89c6a2e5c9 | -11.58643 | -47.61263 | 2025-05-13 05:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52874427-726f-39c5-b09f-ca51ac7a50de | -11.58685 | -47.6092 | 2025-05-13 05:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5156b290-c669-3deb-b47a-f83bd1b87968 | -9.94466 | -55.49924 | 2025-05-13 05:04:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eb06809-57c5-36fd-860d-140366fd3060 | -11.58559 | -47.61935 | 2025-05-13 05:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e196b372-f3d2-306f-a88d-93c2ef477fac | -8.80452 | -49.80993 | 2025-05-13 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a87cd47-af9e-3e2b-b704-0effff5e20bd | -8.08084 | -43.12408 | 2025-05-13 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| ab107801-25d4-38d8-924c-0a8bdf7e4e4f | -7.92972 | -61.55403 | 2025-05-13 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8144b47-9466-3a37-9a47-bc12c5643f38 | -8.07327 | -43.12933 | 2025-05-13 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 3fbf57e0-116d-35e5-90a3-a498815dd749 | -8.07404 | -43.12315 | 2025-05-13 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 7f53a08b-8cf3-395c-ad7a-c1cd42dbe227 | -11.01134 | -50.76289 | 2025-05-13 05:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f231ddb-a436-3f70-907a-2d2020fd78b1 | -11.00847 | -50.76424 | 2025-05-13 05:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eb453f3-5cd0-31c7-8201-80e9838c1eec | -11.80346 | -44.27646 | 2025-05-13 05:04:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3fed1b10-3e52-387b-8a6c-a66419f32949 | -11.58105 | -47.612 | 2025-05-13 05:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b4031fe-92ee-3362-98fd-49237a042a2e | -8.08007 | -43.13026 | 2025-05-13 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 48a3042e-164a-34ba-a2de-8dc4981bdda0 | -8.71814 | -50.24456 | 2025-05-13 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d73a920-ddb4-312d-9002-129d701999fa | -12.90549 | -55.04269 | 2025-05-13 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b02dc8ba-197a-3a37-866c-b3e5acc623a8 | -13.97628 | -56.8066 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9d2d87e8-7a0d-370a-8a26-f9f159332af3 | -13.98069 | -56.80001 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e3676620-1811-3662-949a-7cf5f321c345 | -12.18261 | -46.71033 | 2025-05-13 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa996c22-ed58-3936-92e7-bef63f46bb42 | -13.98678 | -56.80462 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ea73dd5c-c823-336c-8e05-e35528841745 | -14.19599 | -45.48337 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c824118e-64e4-3d0a-9221-02a371369a88 | -12.646 | -54.08792 | 2025-05-13 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82bebabc-cdd9-3ab1-9716-fd790cbbfad7 | -11.7758 | -48.69775 | 2025-05-13 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2477147-b91a-34b6-ac2e-0c16dc0ae8e0 | -12.15631 | -48.01431 | 2025-05-13 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 455c00e1-bfdc-3167-bd67-9302c07ca3a0 | -13.98623 | -56.80818 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 83c3ee65-587e-3ab3-aaed-2d60419614c8 | -13.39737 | -47.63651 | 2025-05-13 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb155002-bc5a-3be5-b3f4-cde3e15f7917 | -15.29387 | -53.20942 | 2025-05-13 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85576b63-b7e9-3b82-a978-eba5ec2e8380 | -12.01024 | -62.8367 | 2025-05-13 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2754755d-58e0-3cd7-b3d4-5f145f2ca112 | -11.77557 | -48.20181 | 2025-05-13 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d885074-e68e-3903-ab64-c6790460542c | -13.56009 | -52.86511 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 08078dcb-338c-3682-b7d3-3d8eec344868 | -16.60444 | -53.40296 | 2025-05-13 05:06:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baf21e05-e65c-34f1-873b-345c2fdadb48 | -13.98732 | -56.80106 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dda2a858-9cf5-3950-b6d1-3f634aee3057 | -14.66279 | -45.12659 | 2025-05-13 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e03d749f-d6d5-3a76-9694-8be69296f68d | -13.04595 | -53.72166 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa482a67-be89-32d1-a19e-d96ef0cf6b70 | -12.21847 | -63.78191 | 2025-05-13 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb78da83-d919-3baa-bb8e-40d21d1c5667 | -15.22634 | -59.35799 | 2025-05-13 05:06:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06dea2ea-113d-3851-a8ff-82eac1a008e0 | -13.56648 | -52.87631 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| aba9c440-cb2c-3a2e-96f0-be16894f97ec | -15.29455 | -53.20448 | 2025-05-13 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eeea1109-67c0-310e-a602-c98566d70dff | -12.21654 | -63.78451 | 2025-05-13 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4d47eca-72c7-36ea-9996-4ff65450fab6 | -11.77407 | -48.20028 | 2025-05-13 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25ba9bfa-193c-3591-bf29-c7283cddbe40 | -13.04164 | -53.72556 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc82e1f6-ab04-3b7e-b06d-b3713063fbbd | -12.15671 | -48.01102 | 2025-05-13 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 359093ff-aa65-3d92-a2b1-d0b4fe797364 | -13.56579 | -52.88133 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d286e0e1-e4d5-3204-851c-b6fb3fc29c4d | -15.56886 | -47.85635 | 2025-05-13 05:06:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf0e8d8f-690d-3580-ab06-2fa39ed6fd22 | -13.67674 | -53.93522 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9b39a9d-b4c9-33b3-983f-ac153e3eb662 | -13.0533 | -53.7227 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d06b7320-8a6c-305b-ad0a-6edc722a5c81 | -11.77542 | -48.70068 | 2025-05-13 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b26aecc-2298-35c3-8a36-de26712d90bc | -14.18625 | -45.47726 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8be69ac7-57db-3ddf-933f-1fe1e967e8dd | -15.07849 | -48.94426 | 2025-05-13 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 682a7044-1437-3dec-a2d7-994d63dc0dd9 | -11.78042 | -48.70138 | 2025-05-13 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6b2eec4-4246-3147-a4f7-fb501e9dbcb1 | -14.18964 | -45.48264 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36bdac87-c19c-329c-8083-859b39c79dfc | -13.56968 | -52.88186 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 10c7616d-3311-3d60-ac17-fd9d1401641e | -13.57105 | -52.87185 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 38da6ee9-e117-3beb-9489-105d8b08cf99 | -11.39021 | -52.93876 | 2025-05-13 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb7d2849-711e-3cad-9895-dc183e81c822 | -12.01443 | -62.83747 | 2025-05-13 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa0ad10a-087f-3d23-8544-d0ef8b3392e8 | -12.18787 | -46.71518 | 2025-05-13 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38186a8f-1204-36ce-80ba-3a9a012b1aa4 | -13.55621 | -52.86452 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2cfc8888-8cac-3482-88c7-f9d101730062 | -14.18732 | -45.46657 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d84d4253-f79d-3392-9062-3ba7c5e863b0 | -13.99009 | -56.80515 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88326d77-5f82-39af-8a5f-c819ac05cc71 | -13.67307 | -53.93475 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cec8fe6-13fc-308b-97d3-119ba7386407 | -12.00955 | -62.84062 | 2025-05-13 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e625af6-7451-33ae-8569-44327939c7d4 | -13.97791 | -56.79592 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a8fc79f4-25af-3d6b-a8c0-62f12f76386a | -11.26325 | -52.47085 | 2025-05-13 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 744789cc-948d-3b18-8f6b-18bb6a15ac71 | -13.06239 | -53.73767 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 533a71c0-000d-3ef6-b2a9-58f36a8fb5c8 | -13.5795 | -52.86795 | 2025-05-13 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b120cd79-c939-3e58-899e-b76ba5f5dea6 | -14.19079 | -45.472 | 2025-05-13 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 041f3942-388b-3f82-9a22-8256f14c826a | -11.9171 | -54.40301 | 2025-05-13 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c031d25-bfad-35bb-9526-32f6914d906e | -13.04899 | -53.7266 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 264d0e4f-858c-33b6-ad60-6d2b3b70309d | -15.42931 | -60.19761 | 2025-05-13 05:06:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b7d6a75-56c5-370c-8ff0-4aba37d39ee7 | -13.98346 | -56.8041 | 2025-05-13 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5737ed17-8340-3c9c-b6d5-823306063b3f | -13.05266 | -53.72712 | 2025-05-13 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff78b170-c07e-33c5-995b-fe33085be5f3 | -12.50554 | -55.19028 | 2025-05-13 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7998c49a-1957-3e90-b0f3-82706fecd097 | -11.91652 | -54.407 | 2025-05-13 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4002663f-3cb7-3517-930f-e2a33769e176 | -11.2594 | -52.47026 | 2025-05-13 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6b79478-13de-3954-8ff3-fe74e3240ce6 | -12.15184 | -48.00708 | 2025-05-13 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README10.md)

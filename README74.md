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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27c87075-3100-3e2b-99cb-9e2ba379919a | -6.5781 | -45.3158 | 2026-09-14 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| f42f0c39-fb24-39ef-ad45-f1d7255ba4ff | -6.1111 | -57.6645 | 2026-09-14 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| ec5a32bf-f045-365a-b12b-c259f3f515cd | -3.1514 | -58.644 | 2026-09-14 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| cda7f40b-03b5-3896-8892-2d4b53174e1e | -8.5415 | -54.7187 | 2026-09-14 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 3da23d46-c7da-3852-b1f2-861e697a1b15 | -3.314 | -59.3706 | 2026-09-14 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| a9b9a531-8805-3496-a5c3-0470decb448f | -10.81 | -46.2726 | 2026-09-14 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 35c5d808-8f14-30b6-9211-912080b93405 | -13.2867 | -51.3046 | 2026-09-14 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 8766c399-4fbc-3c15-83cf-05a2d768b14f | -6.0071 | -59.9491 | 2026-09-14 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c2d95dc0-783c-33c9-8baf-d07546c283ba | -10.7715 | -46.3001 | 2026-09-14 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 83c07812-44b8-3d3b-8404-027770bf9a97 | -10.7719 | -46.2775 | 2026-09-14 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 5fd933a3-7f95-3c71-9b0e-5fadd090042f | -10.6958 | -47.5175 | 2026-09-14 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| c1f0f3f9-2143-3a38-9e89-2168355fa71b | -10.9506 | -57.1895 | 2026-09-14 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 5c622ff2-11dc-388c-9b43-4e9ccf541cc6 | -11.354 | -46.7874 | 2026-09-14 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 61eebff4-1e75-3eb1-b118-1900ec01eed9 | -10.5667 | -51.3349 | 2026-09-14 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c500c837-c773-3754-be18-6f073838a4c1 | -10.7909 | -46.2751 | 2026-09-14 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 78d2568b-4341-31ac-9198-f79d3332b439 | -2.9531 | -42.8469 | 2026-09-14 14:30:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| f4f9290d-f156-39cf-aed1-987ca2f7f9b1 | -3.5893 | -59.0773 | 2026-09-14 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 223abecc-7753-3709-8920-8bbcb8eb71d9 | -10.8093 | -46.3179 | 2026-09-14 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 340.1 |
| 38e30452-3408-3ea0-81ce-4f06e6ce3f01 | -5.1255 | -55.955 | 2026-09-14 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 170.9 |
| a6fd50ee-c6d0-3051-be82-d5ed9b86a130 | -3.3809 | -50.7623 | 2026-09-14 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bf093f82-9d4d-3c89-9542-3c5682391362 | -12.3919 | -44.391 | 2026-09-14 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 771600c5-6975-3a50-a7ad-c1266cd0dd8e | -6.1108 | -57.7035 | 2026-09-14 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d86cc942-58a6-3be9-bdd0-a26db086b210 | -3.4089 | -58.2142 | 2026-09-14 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 1e752cc7-17e8-36fa-a165-8970e2e0cde1 | -3.3494 | -59.8097 | 2026-09-14 14:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| bbd330a6-4ab7-3493-8b3d-55c145e35c1e | -10.661 | -51.3465 | 2026-09-14 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ecc632cb-665f-350e-a761-9cadbd1b1d0b | -3.728 | -61.7555 | 2026-09-14 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| be22ee54-9b1a-373b-b087-6f6070b5f518 | -4.1333 | -60.6882 | 2026-09-14 14:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 878ebcd4-48bd-3f5f-86b4-f1c908f46281 | -3.3871 | -59.4075 | 2026-09-14 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 48156951-0713-37c8-8dd3-ebae18f9c0b6 | -3.4089 | -58.1949 | 2026-09-14 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| ac32f467-ba6d-38b0-865d-e17efd8c4025 | -15.5572 | -48.7953 | 2026-09-14 14:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 7937be60-58c6-3609-a054-94e1c0e77240 | -6.5838 | -58.8304 | 2026-09-14 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 72d42be9-e3ee-3a52-96f7-47101c377d76 | -9.5126 | -45.4796 | 2026-09-14 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 258498cd-9516-3dfc-b7f9-41597f472315 | -10.7276 | -50.5979 | 2026-09-14 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| a58b1f3e-b86e-3a20-9ef1-cf1bc29e554a | -11.3352 | -46.7674 | 2026-09-14 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fec78f50-112f-32a8-905d-08e3a7687e6f | -13.5526 | -51.4629 | 2026-09-14 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| a95286c7-3630-3b85-b44b-113724ab0440 | -10.6832 | -54.127 | 2026-09-14 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 3406b31e-2b9e-314d-8e07-68430d1df6a5 | -2.9025 | -50.4004 | 2026-09-14 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 6b449c53-fc14-36ea-b1be-d6f60dd241b4 | -10.7842 | -50.6133 | 2026-09-14 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7bfd5795-9ffb-3bcc-a945-50c4691e41f6 | -8.5809 | -44.486 | 2026-09-14 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 898f5506-c33c-31aa-b438-ce5096370b44 | -12.4901 | -41.4012 | 2026-09-14 14:30:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 1f6b2f99-ffd6-3ac2-a06d-35c2610116c7 | -4.1334 | -60.6692 | 2026-09-14 14:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 78fe4d69-238e-381f-b6bc-7c5845ca0409 | -10.6827 | -54.1679 | 2026-09-14 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 45086996-c3db-3157-ad34-c48d92f4321a | -10.6522 | -50.5845 | 2026-09-14 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 3b1d3bec-c870-3a35-99ae-a16c7ad6beab | -15.5768 | -48.792 | 2026-09-14 14:30:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 2ec6ef09-1185-3f2b-b727-5c75ead8a286 | -3.3676 | -59.8285 | 2026-09-14 14:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 0a0ee700-7a3a-36fa-9373-05f0bf96231e | -15.5763 | -48.8144 | 2026-09-14 14:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| debf2042-226c-3bf7-b7f7-658da13d9e05 | -9.7036 | -54.371 | 2026-09-14 14:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a32bbb14-3ce3-37c7-bd23-c40fa2b8a5e3 | -3.3493 | -59.8288 | 2026-09-14 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 147.9 |
| d3754ab9-f953-35a7-8a80-de2e38e3bbe9 | -8.6194 | -44.4357 | 2026-09-14 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 224.1 |
| bc3e3e67-63e5-35f9-a440-94ca6a3af084 | -13.5719 | -51.4605 | 2026-09-14 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 6b1187db-d03e-3451-bb11-3dbfa4ea04de | -7.1048 | -41.7971 | 2026-09-14 14:30:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 7e08acbd-717c-3119-8981-651add20bee9 | -7.0166 | -44.6184 | 2026-09-14 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 42ca7052-0201-3245-b886-9d9cbb91c766 | -11.838 | -46.3834 | 2026-09-14 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| f1a8382e-cc98-39e8-aef2-29539d78b820 | -10.6829 | -54.1475 | 2026-09-14 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 213.4 |
| 1f02370e-99f0-3ac8-8d35-1b7ccdcd1366 | -10.7145 | -47.5374 | 2026-09-14 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 1caeabe3-eeee-3318-af8c-80d4d56b2fea | -6.1109 | -57.684 | 2026-09-14 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 222.6 |
| 330fd0b4-d7bf-3106-b7f9-27b84af8e471 | -1.7133 | -54.9521 | 2026-09-14 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4a0deaab-459b-3067-9a54-ee3fd05b8d83 | -14.205 | -47.4039 | 2026-09-14 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 060df006-d64a-328a-9bf8-d18d24f796db | -6.3436 | -55.8243 | 2026-09-14 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 2c4a3cb6-7458-382f-8cc2-020e711bf909 | -8.6001 | -44.4609 | 2026-09-14 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| fb86a089-4298-363a-ad54-a8608ae24519 | -15.2859 | -53.9037 | 2026-09-14 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 83ddb09b-4088-3abf-bbd2-f5b3cf7be6de | -8.8081 | -45.8753 | 2026-09-14 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 8baf3e6d-61b1-3bdf-9ca5-213a6039481b | -2.8839 | -50.4428 | 2026-09-14 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 606c5674-db54-3fc9-a438-ff167517a252 | -10.433 | -48.6474 | 2026-09-14 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 67706234-924e-3fd7-8527-84104f329007 | -10.7839 | -50.6346 | 2026-09-14 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 59a4c434-6441-3f0c-a8c0-91d60be373c4 | -9.4936 | -45.4818 | 2026-09-14 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 174.9 |
| a6b3ff79-bb90-3142-a62e-4f5301d09f2d | -3.6077 | -59.0577 | 2026-09-14 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7c70f8c2-ba76-3621-b343-eb6cd514ebc7 | -13.4458 | -43.8128 | 2026-09-14 14:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| b3e9f73b-cd99-3075-b333-ce627e349ccc | -10.4516 | -48.6672 | 2026-09-14 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 51c1e261-dfc7-3533-a87d-19296a00ad61 | -11.3349 | -46.7899 | 2026-09-14 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 16f38e09-deb4-304e-a213-0fe975f0ba9a | -10.6525 | -50.5631 | 2026-09-14 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 21970d23-69a7-3791-b227-93a0414c7767 | -9.8989 | -47.6095 | 2026-09-14 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 3655da60-1614-375c-9fe6-391e13a68066 | -10.7906 | -46.2977 | 2026-09-14 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| fdc4d703-fac7-3d10-b82e-627628b8b9c4 | -7.0859 | -41.799 | 2026-09-14 14:30:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 96e3ee0e-d38f-3f2e-9f99-31d1b8dc3650 | -2.9024 | -50.4423 | 2026-09-14 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 654dd3f3-4356-35ef-b3dc-c92b2b7d1734 | -10.4519 | -48.6453 | 2026-09-14 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 4a23af2e-4ba0-33d2-bcf6-5f361f94652f | -3.3141 | -59.3515 | 2026-09-14 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d3068c34-2342-3407-ab16-9bd44880e1ac | -7.207 | -46.1187 | 2026-09-14 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f7ab509c-fcc3-39ea-8a6f-8b200273397e | -6.0925 | -57.6847 | 2026-09-14 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b204c951-26a3-3e30-9e15-6335c67dd3db | -11.8365 | -50.0028 | 2026-09-14 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ea2c2639-67c2-3699-ab9d-405b843970c4 | -9.4325 | -50.1299 | 2026-09-14 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 287.7 |
| 20fd8eca-64a9-3d8b-a2cb-82c8cdb37d74 | -10.6335 | -50.5651 | 2026-09-14 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b4ed4b6d-e5ba-3d34-8981-166ae26896b0 | -3.1697 | -58.6437 | 2026-09-14 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 0fb4553d-b1ba-31c7-8058-55f248893c5e | -6.8446 | -55.5611 | 2026-09-14 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| b6e552a6-2659-34e6-8c1d-dfa1fc9744e3 | -10.7274 | -50.6192 | 2026-09-14 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 5fb6d393-84f2-3d44-9eea-0b4540cd2442 | -9.4936 | -45.4818 | 2026-09-14 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 66b54b95-9c0b-3c27-bebe-18ea54c01a0b | -12.4341 | -47.3349 | 2026-09-14 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| fa32fccc-cfab-3a18-80e9-90dbbaeec05a | -6.1109 | -57.684 | 2026-09-14 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 311.3 |
| 4a9c8e20-3329-39c1-9129-49d003354d67 | -6.8446 | -55.5611 | 2026-09-14 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 92f561d0-1813-3988-935a-970c4be31db6 | -6.4291 | -41.55 | 2026-09-14 14:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| cd8dcbb4-fdfe-3447-b128-53d820bac19c | -10.7276 | -50.5979 | 2026-09-14 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8d1b627f-f54a-3511-9ef6-3001d4cd0925 | -8.6194 | -44.4357 | 2026-09-14 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 163.8 |
| a70b0aca-18fc-3fe4-ac70-a534feef411b | -10.3116 | -45.3136 | 2026-09-14 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 169.2 |
| d16ca092-5de7-3ebe-8279-a0ca943e2806 | -3.3871 | -59.4075 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 0e1148a1-7980-31e2-a919-46179a4f0300 | -6.1111 | -57.6645 | 2026-09-14 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 528c59ec-79f8-3ad9-9313-6c0b285cd2e3 | -3.6076 | -59.0769 | 2026-09-14 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| f9970d22-7869-3972-811a-21fba6116e40 | -3.4089 | -58.1949 | 2026-09-14 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 81439da6-5392-3c98-8c6f-0b635bbdbeac | -5.2023 | -49.3348 | 2026-09-14 14:40:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a1b3ef66-5e15-398f-952a-06c1fb35153a | -2.9025 | -50.4004 | 2026-09-14 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 892445cf-3b3b-3cd3-9e8c-6f740e33837a | -15.5768 | -48.792 | 2026-09-14 14:40:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |


[Clique aqui para ver as próximas entradas](README75.md)

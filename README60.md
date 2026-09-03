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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bdc9bde-ee0e-36db-8d31-c52110f3d318 | -11.3224 | -51.4049 | 2026-09-03 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c7c206ce-fc04-32ff-98e6-b29e7cb78663 | -3.3685 | -59.5036 | 2026-09-03 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 7eede0e6-e6bc-32f2-adc9-d8725fd17ee8 | -1.4752 | -54.8157 | 2026-09-03 14:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 840cd607-f79b-3198-b507-ee73b68a2688 | -9.6839 | -48.1386 | 2026-09-03 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| af3cb431-5b1d-39b7-a746-6f5279dab727 | -10.8635 | -45.3101 | 2026-09-03 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d5f35ba2-371d-3569-9475-31551c6add48 | -13.3625 | -51.359 | 2026-09-03 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 5344b340-7048-3617-996f-b20845ddd242 | -3.2486 | -47.2438 | 2026-09-03 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b0b6c818-f84b-3885-9271-3ed68ddf3bb0 | -8.4049 | -44.964 | 2026-09-03 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 10423212-6e92-37bd-a746-950e41638a08 | -14.5634 | -52.0344 | 2026-09-03 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 65cc442b-2c1a-38db-b605-bf5308194160 | -10.8826 | -45.3075 | 2026-09-03 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| dc364684-4ad4-328c-91d4-335f9acf0ec2 | -9.2144 | -47.99 | 2026-09-03 14:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 0363f61d-8d9f-3bb5-9b8b-731b90874527 | -12.1265 | -44.199 | 2026-09-03 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 8d992b12-38f0-3ef5-92dc-2fb91fd9fe33 | -8.43 | -54.6858 | 2026-09-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 8e228ae6-ca5d-3673-83d1-b15a0beb4a3c | -10.5278 | -49.9993 | 2026-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 817b723d-1aee-3923-ae23-4a9c11d03f4d | -6.6697 | -59.9635 | 2026-09-03 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ef9da32d-300a-3699-8da0-10c4bf0387b3 | -5.3264 | -60.143 | 2026-09-03 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| b169c242-321d-3770-b147-e6c0bceb5ceb | -10.1842 | -50.27 | 2026-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e614568b-5181-3f07-b468-ffe0faf2b0f8 | -11.0752 | -51.4731 | 2026-09-03 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2dc64fa8-4c4b-3e1f-9be8-f60c20b6fe62 | -11.2879 | -54.0317 | 2026-09-03 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 1ab2196c-67e0-3ec5-bbee-40786d25f2ca | -11.5287 | -45.4703 | 2026-09-03 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b17e6f0a-3d04-3bf0-be32-2e95d6b489be | -10.9204 | -45.3253 | 2026-09-03 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 1efed1de-fdac-3878-80dc-7bf809e29156 | -13.3813 | -51.378 | 2026-09-03 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d2f751a5-d554-3c75-a72a-ab7f47d8e3b0 | -8.4298 | -54.706 | 2026-09-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 677c68f3-6ae6-3857-a173-65f45ee46952 | -8.4481 | -54.7452 | 2026-09-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 275.1 |
| cb05c48a-2f5e-3a18-a83e-5669fefca8c8 | -7.6169 | -49.9439 | 2026-09-03 14:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1946094f-7248-3fc4-a6d9-caa94e2a962f | -13.3817 | -51.3566 | 2026-09-03 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 322eb954-84c5-342f-ae27-baf4a8ff09a0 | -12.1457 | -44.196 | 2026-09-03 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4c34e8c0-c7df-30b3-8495-e3a311bc28e8 | -7.1187 | -42.2264 | 2026-09-03 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| f85ce9ab-6ad2-388e-b790-533b8761a595 | -10.9395 | -45.3227 | 2026-09-03 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 0716a6ea-0b5d-36ec-ab40-bb5c6cbd61e6 | -1.8019 | -47.9586 | 2026-09-03 14:20:00 | GOES-19 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c638f520-3972-3d0b-a093-1734d704299e | -11.1496 | -51.5708 | 2026-09-03 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e734ae5f-cfea-34a9-aeba-3b0024dbc04a | -6.8387 | -59.4186 | 2026-09-03 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 4e271563-466f-3d93-a04e-d6135d03bbde | -8.4235 | -44.9849 | 2026-09-03 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 354d8ac5-d5d1-3198-b350-159ab0a3e957 | -15.287 | -53.8407 | 2026-09-03 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f34f8cef-4d85-3654-9b0c-f5b0c50a2105 | -13.8563 | -54.0967 | 2026-09-03 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 24587ce3-ceda-3e77-be06-46f8bf7f20cb | -10.2403 | -50.307 | 2026-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f9b80c23-6ca7-39ad-9898-def895a8c68e | -5.5098 | -60.1947 | 2026-09-03 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 7127268a-9e84-3ab7-ba83-92509a2a45c1 | -3.6232 | -54.5931 | 2026-09-03 14:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| db01b7e5-88d2-3892-b7a8-2d84d7c42848 | -10.1456 | -50.3379 | 2026-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d4d72ae0-befe-3709-8ddb-593d18354e74 | -9.6293 | -54.3158 | 2026-09-03 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 8eaa078e-5f21-3f53-aee3-7e137e02e7cf | -9.5964 | -47.6204 | 2026-09-03 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ed56f4a8-d385-3c0d-8f36-a505c2ab13a6 | -8.4485 | -54.7048 | 2026-09-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 63c6fc43-83b9-330b-b02f-3e767e7dc2c7 | -9.4532 | -45.6682 | 2026-09-03 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| cb36c201-ecd5-3a74-8c7c-702305bd124c | -11.1634 | -50.5727 | 2026-09-03 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c8058873-7076-3cc8-8bd7-c546254d6a91 | -6.8172 | -59.9578 | 2026-09-03 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 881ee3ab-fc71-3555-ab64-387c92eb59df | -8.3857 | -44.9888 | 2026-09-03 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 601e040e-eecc-3cd0-87f5-240b30117935 | -7.5138 | -60.7728 | 2026-09-03 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f659de57-878b-3762-a37d-17c0e356d7cc | -10.2028 | -50.2895 | 2026-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a5eb1236-a26b-3fdc-bdb4-49c84befacf0 | -9.6676 | -47.9429 | 2026-09-03 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| cb013364-ec7f-314f-8cad-5ae583006445 | -6.6357 | -59.4459 | 2026-09-03 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a61478ef-a8db-34d7-beef-2494d7f059ec | -10.1653 | -50.2719 | 2026-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| eeae14cd-947d-36c9-b426-32edeb95dddd | -6.6698 | -59.9443 | 2026-09-03 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 128.7 |
| cc51e05e-9af8-3be4-8c3f-952639442cbd | -10.8249 | -45.3382 | 2026-09-03 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 27c06b1d-c8c1-307a-bd22-006f827ad41a | -9.4345 | -45.6477 | 2026-09-03 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9cfe0e5f-2e0f-3ade-96af-19036a2da1dc | -11.1126 | -51.5114 | 2026-09-03 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 58c694bb-f6c2-3d23-9d09-3d96cf5f0bfa | -8.4677 | -54.6429 | 2026-09-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 295.5 |
| 18cd7120-a2eb-3aed-8daa-90c7108114d2 | -6.6883 | -59.9436 | 2026-09-03 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 4f6ad9b0-48a4-3ac3-b401-03aa2bf6192c | -12.3814 | -48.1655 | 2026-09-03 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 101b601e-df6a-34d0-bed3-93e2bcdd6cf9 | -10.1087 | -50.2776 | 2026-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ec925cf4-e05d-3a64-9b23-d5c3a462174c | -11.131 | -51.5517 | 2026-09-03 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 91eee856-5c64-39c7-a2ac-50b38245c054 | -13.3555 | -51.7855 | 2026-09-03 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| c811de4b-5dcd-3a6b-aa4f-2f06d5ea77e4 | -5.8887 | -51.9412 | 2026-09-03 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 65a25105-41fa-3238-bcbc-c1bd44791267 | -12.1462 | -44.1725 | 2026-09-03 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 8bb2d16d-20d3-36d3-83fc-a4ce1bf30d1c | -12.3434 | -48.1485 | 2026-09-03 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| fa722042-bf2b-3314-b4a3-787b75688b01 | -6.6541 | -59.4452 | 2026-09-03 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 21971f79-041a-37a6-a827-55214a190a20 | -5.565 | -60.1739 | 2026-09-03 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 7026d6ca-f9b1-30b6-9b3b-d606ad0fd217 | -9.4535 | -45.6455 | 2026-09-03 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7938c181-6b70-3dbc-adc0-068c847efafc | -7.1123 | -42.7727 | 2026-09-03 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| d8ed87c3-3747-3360-993f-d599f57abfcc | -10.8582 | -50.7332 | 2026-09-03 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 82df5bf2-9a92-3819-8f23-e509afb8c0d1 | -10.1273 | -50.2971 | 2026-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 964ea19f-7951-3078-bed3-c15bc17041db | -8.4483 | -54.725 | 2026-09-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1c65cb1a-ca61-3b84-bafc-59c3e3defee7 | -6.966 | -59.7407 | 2026-09-03 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 42afe474-1d5e-3d31-9473-94f385a71bc2 | -3.3872 | -59.3692 | 2026-09-03 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d763245a-5eba-36aa-9356-0f7ae4381172 | -8.4488 | -54.6644 | 2026-09-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3715559d-98cd-3c96-b132-b5ab2c9c43a7 | -11.5287 | -45.4703 | 2026-09-03 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 96e0df14-b440-341e-952b-a26412f7a9c8 | -6.6698 | -59.9443 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 6dca720c-e3b6-3841-913f-ec4f3a27dcc6 | -3.8604 | -44.0585 | 2026-09-03 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 49824091-fb17-3871-a24b-0c3f283cd734 | -7.3117 | -60.6089 | 2026-09-03 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d40148de-58e6-3cfc-9e6d-ce649724177f | -5.4553 | -60.0626 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 1a20912a-f7b4-3599-b974-c212fad6e2fc | -8.3857 | -44.9888 | 2026-09-03 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e55ae85a-5223-3000-9add-0f03a411feac | -11.0057 | -49.6677 | 2026-09-03 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d007c0f7-1e2b-3973-8a37-5f31694c802e | -13.3813 | -51.378 | 2026-09-03 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 16774b16-0b8d-3ae9-a527-d8ad663bd4d7 | -3.6232 | -54.5931 | 2026-09-03 14:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 26f60e15-cd2d-3067-b74a-7f6df348b78c | -3.3685 | -59.5036 | 2026-09-03 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 0def331c-48aa-3c44-bace-50962538890a | -9.4342 | -45.6704 | 2026-09-03 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2d5b9f99-122e-3d36-89fa-84a4ee5d93d9 | -7.4954 | -60.7736 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b10dc018-bf93-3b13-adc7-4dbcf3a963b2 | -9.2144 | -47.99 | 2026-09-03 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| eaa4160f-ede0-3e0a-95f2-e3df1e0009e7 | -11.0566 | -51.4539 | 2026-09-03 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 15cd6eab-dbcd-3b8f-b85a-be0381c0a693 | -11.1496 | -51.5708 | 2026-09-03 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ebb82c3b-e344-3e7d-992e-84b8374aa1b9 | -12.3626 | -48.1459 | 2026-09-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 5b8ebef8-fad8-3268-a086-77eca8ec8468 | -7.6169 | -49.9439 | 2026-09-03 14:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 9a9a5822-a36a-31b7-ba4e-4834311717c5 | -8.4483 | -54.725 | 2026-09-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 51c76117-1318-3d02-9f99-6ae2f811c153 | -11.006 | -49.6461 | 2026-09-03 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2a827c29-55f7-31c2-b66f-740cda723a40 | -8.43 | -54.6858 | 2026-09-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 05df69a5-6fc9-3755-a75a-1e040bcf1c70 | -13.3817 | -51.3566 | 2026-09-03 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 97c6f422-159a-3a4b-9670-b87fa85754c9 | -6.7648 | -59.4408 | 2026-09-03 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 172.8 |
| 4d1189c2-ee82-37b2-9dec-de6dc271495e | -7.5324 | -60.753 | 2026-09-03 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bd2361d3-2a66-3e80-9137-c442385bddac | -12.3434 | -48.1485 | 2026-09-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 7e87bbfd-441a-3c05-aa73-28c6c4ac73cc | -11.2391 | -50.5857 | 2026-09-03 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| dcfda0ee-b8a9-32b7-a44f-c8bd4d2a5963 | -12.3622 | -48.1681 | 2026-09-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |


[Clique aqui para ver as próximas entradas](README61.md)

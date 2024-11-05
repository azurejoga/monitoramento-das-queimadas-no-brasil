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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04aa117b-ba15-3d03-81a6-d41f918cd35b | -3.5444 | -47.4073 | 2024-11-05 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| a01b886f-7db6-31b0-8920-011ddb0721d0 | -3.5632 | -47.3629 | 2024-11-05 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 1fb9ad28-d953-308f-8bdf-a378d1431034 | -3.5631 | -47.3847 | 2024-11-05 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 310.0 |
| cef25871-b89d-36c5-a34e-280bd6f76e97 | -6.5919 | -45.8107 | 2024-11-05 03:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 7fffdd92-d84c-3ac0-a604-f76ea33a5c39 | -3.5446 | -47.3855 | 2024-11-05 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 384.2 |
| 4cd9314b-b9e0-3e60-a802-28aa3db71bd4 | -4.0667 | -46.9246 | 2024-11-05 03:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 1bd7897b-ec44-320d-910a-189194fe466f | -2.1173 | -54.6472 | 2024-11-05 03:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8cd950e0-9ca8-3a2a-a038-591a7487cc4d | -6.1041 | -43.9593 | 2024-11-05 03:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| c4f215bd-97f3-36fe-920a-41d2249ba6b9 | -2.6507 | -48.5629 | 2024-11-05 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| a126155f-3851-3da7-9106-6bc2aa93a9ba | -2.6691 | -48.5624 | 2024-11-05 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 9ae49684-a51b-31cd-9dd8-0559510c7bfa | -3.5447 | -47.3636 | 2024-11-05 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| eca5b870-ce31-32ec-b698-f89ba556e5e8 | -6.1041 | -43.9593 | 2024-11-05 04:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| f66a29fa-d9b6-38ec-a92e-269c78df468c | -3.563 | -47.4066 | 2024-11-05 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 3d449268-e12c-3582-91e7-b428516ae9ee | -2.6507 | -48.5629 | 2024-11-05 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| fdee54ab-9720-3e27-9bd8-1ecebfcf278f | -2.6506 | -48.5844 | 2024-11-05 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f4decfca-fccd-39a9-b4c9-fbf73536615d | -2.1173 | -54.6472 | 2024-11-05 04:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5400f927-dc63-3cb2-a943-de83fc7a175e | -2.82 | -52.9409 | 2024-11-05 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 775106d9-ff61-3301-a90a-b5cd0a33e4f0 | -3.5632 | -47.3629 | 2024-11-05 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 0f711c8c-48a0-39af-abf5-140c908d29ff | -3.5631 | -47.3847 | 2024-11-05 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 371.5 |
| 71786c4d-ea50-35d0-b385-8f6daf65ff6a | -2.6691 | -48.5838 | 2024-11-05 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| bfa6e6b6-88ca-3fd3-ac0e-1a95a645fb21 | -3.5446 | -47.3855 | 2024-11-05 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 291.1 |
| e31853e9-6643-3c50-b450-ca7eeda5ed7f | -3.5444 | -47.4073 | 2024-11-05 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| e5e25486-9be1-3f27-a3da-c3fc5255df73 | -3.55 | -47.35 | 2024-11-05 04:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1398a39-885a-3ac8-b7df-ee7dbc8a1443 | -3.56 | -47.4 | 2024-11-05 04:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62d06edb-d4ee-3a3a-8293-93cf0d290f9f | 3.4991 | -51.25662 | 2024-11-05 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b21772-edd5-3d35-8cbf-bf9c79622f4f | 2.68896 | -51.36419 | 2024-11-05 04:06:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e238bec0-2a0b-3bfa-a347-7a0572e7bac2 | 3.50549 | -51.25572 | 2024-11-05 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9b15f6f-dfa0-30a2-b597-d9a0965380ed | 3.49985 | -51.26183 | 2024-11-05 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c8c0970-db68-3835-ad9f-424f84dafcc5 | -4.11664 | -47.96452 | 2024-11-05 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88440264-30e2-3ccd-9a7f-bb7370b80071 | -3.55317 | -44.63017 | 2024-11-05 04:08:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8fe8ea28-d988-3e0e-ad47-57e7e5207e2c | -4.88987 | -46.71609 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67b66625-fe57-3a55-ba5e-a81602c965dd | -5.65018 | -43.07179 | 2024-11-05 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 53cea7d2-7918-3fde-b666-f222c4d7596e | -2.81047 | -46.64079 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f27dba4f-1fb8-3c6a-9495-34beab295ae6 | -4.07827 | -48.31329 | 2024-11-05 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b5bb71db-8ec9-3f94-937d-1ee899f8c3da | -5.43132 | -42.71915 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5aa67faa-89a1-3343-b945-bb5604f09392 | -2.25583 | -46.47419 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a168711f-10d5-364a-9f69-42e34ac40173 | -2.78241 | -48.71826 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5a680b2-3a5a-3b8a-a9ac-3b10f61c58b6 | -4.11436 | -49.53228 | 2024-11-05 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbad172d-105f-39dd-98d0-4523de53b023 | -5.42442 | -48.14365 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94207312-28ce-35ff-ac8f-66857f907c64 | -2.17822 | -48.85814 | 2024-11-05 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5672b165-a998-39ae-ac3a-52f85a06e143 | -7.25863 | -38.94855 | 2024-11-05 04:08:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7309c96b-c6a1-3f05-b736-c35902cd2349 | -5.50291 | -41.65467 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 20a4ef36-d581-365f-92b1-208f5240bfab | -5.69699 | -45.83226 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36a587f1-d3e2-3727-9f98-fb77ec58d562 | -3.03293 | -53.26511 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3092948-346f-3379-96f5-c35d3bc73ee0 | -5.5156 | -41.66432 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d1afac58-5045-324b-b71d-4439f86e2e5f | -3.12055 | -51.11106 | 2024-11-05 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2a7d2e1-93c7-31be-b26c-a096f512d8cf | -3.12695 | -51.10813 | 2024-11-05 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 113f0038-0bf7-311b-aee3-eab05f021aa3 | -4.21457 | -44.29248 | 2024-11-05 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4fb47f6-711a-3597-bed7-7bb06e072933 | -5.49734 | -43.30327 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70373d1a-cc4d-3e9a-b746-a332513fb3de | -4.64025 | -45.06857 | 2024-11-05 04:08:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 806f1ed6-bb4a-3d8d-87a5-ac7113853767 | -6.17934 | -43.58549 | 2024-11-05 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1753f54-c72d-3874-b101-f195f17f9485 | -6.12268 | -43.9755 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7d6627d-ed28-3e7d-998d-3d77fdcab992 | -6.84228 | -38.90132 | 2024-11-05 04:08:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 479cc2b3-3081-3083-8df5-5859697f4047 | -5.60794 | -41.63629 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8f022dff-6b94-3ad9-a0e4-d0b4e0b8e0a0 | -6.94831 | -39.80476 | 2024-11-05 04:08:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 29be3979-7f1e-399b-943d-7ab51bdebf2d | -4.65874 | -43.82322 | 2024-11-05 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 42f26c21-3ab2-3f26-9530-81169e8134eb | -2.64694 | -48.5626 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c6ab359-6b75-310f-a148-d8269d70ef41 | -7.80577 | -46.57702 | 2024-11-05 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e6d21f77-be27-3083-80f2-2e508ffd7612 | -5.61132 | -41.658 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f9d474b3-c886-3d77-8c69-e87d7b6f2a6b | -6.2285 | -41.62859 | 2024-11-05 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bcd4a8af-44d4-3412-897f-94abf0017036 | -5.15595 | -44.55212 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4b21f10-1994-39f8-aa56-abadc21679d6 | -4.06079 | -46.93058 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f638c09b-42e5-3f42-be97-a5f46ed68834 | -2.80019 | -51.49147 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 963f07bc-fcf0-33b4-8f46-fb665b48e744 | -4.23432 | -44.9367 | 2024-11-05 04:08:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2360a11-4771-3b1c-8799-5fe48f4394aa | -4.55917 | -45.80105 | 2024-11-05 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b32c69e-ca5e-3cb3-b420-d82b159fea92 | -5.61017 | -41.6437 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96838d43-1693-33e3-bb10-feb167bfc85b | -6.91857 | -35.03777 | 2024-11-05 04:08:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bd553164-fe7d-3ab4-b2b6-80461da8f631 | -4.63825 | -40.72175 | 2024-11-05 04:08:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7d2293e-f723-3d31-bd37-cb2ac2f2dbac | -2.80748 | -51.48409 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c3c11e5-4da0-31b2-abf8-d12140213d18 | -5.30662 | -46.25733 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94ec9374-c5e8-3d9a-ad0c-d8c0f7e03d15 | -5.98691 | -43.42593 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24061693-240b-364c-8e50-5d10136b360f | -6.30338 | -42.04021 | 2024-11-05 04:08:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 34e191a9-0c35-3a0d-b2ad-e07f95c5622e | -4.71971 | -46.42658 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe0108b5-f4e8-3a7b-989c-5bb960a606f2 | -5.81012 | -44.13248 | 2024-11-05 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 712fcc46-b969-3a9f-b930-2bbf97dec727 | -5.21337 | -46.72995 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97f8744d-2a10-3e45-99de-f2b10410e5b8 | -7.13117 | -46.00925 | 2024-11-05 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 293a19f8-db24-367c-9fcd-06a5720d73e3 | -3.3687 | -44.2617 | 2024-11-05 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb64f12f-ae15-3ca5-b661-f20916cec42d | -3.49487 | -51.08264 | 2024-11-05 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 655b57f0-1041-37ab-9b19-b86371d49a96 | -4.40425 | -45.86099 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6d5c46f-9802-3cdd-8304-62059a790460 | -4.78737 | -46.47267 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a47fb89a-daa2-3497-b001-d37983931157 | -8.67872 | -40.20996 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 201a5a8a-0498-3995-ad67-4376a295ebea | -5.53553 | -44.48381 | 2024-11-05 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf76605b-c0e1-36c9-9d22-bf1376a0abf4 | -4.35359 | -45.90271 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 409d0291-4b4c-3c78-9bc9-e40d0226f8bf | -5.2181 | -46.72694 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3521dcdb-962b-369f-be1d-52a3020a5015 | -6.83149 | -40.18624 | 2024-11-05 04:08:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5ca0daa1-a122-3c1d-987c-66c2ab3e1960 | -5.60801 | -41.65749 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 98a87d3c-efb4-3f14-a7a6-2a7bcdaae197 | -4.48036 | -46.46024 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9699e08-25f2-3784-94be-4da96826f961 | -5.29238 | -46.24403 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5a1601a-d9d4-337b-a223-d9b91b84f71a | -5.98974 | -43.43018 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 325e4507-15e7-3cc3-9c2b-1b802f65ff1e | -2.29878 | -46.50525 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 719e7c1f-36f1-33ba-bdf2-66dcd4af83f2 | -5.61631 | -41.66938 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ce8e31b5-c5a4-38ca-99ec-b6e50080ffa1 | -3.95619 | -46.37188 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bba7923b-dccf-3486-8091-5a06dceeb3de | -2.64964 | -48.5649 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8190e55f-ac33-35c4-a338-6a476aeac8b9 | -4.44381 | -45.4173 | 2024-11-05 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22823b87-62bd-3fca-bb5b-a04a46eb4447 | -5.30983 | -43.07049 | 2024-11-05 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 844fda5a-e2bc-3095-bc77-63d3a77b4be5 | -5.15633 | -42.60256 | 2024-11-05 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16f4eb64-2168-3d26-a0f0-b98d399fa714 | -6.19142 | -39.22673 | 2024-11-05 04:08:00 | NOAA-21 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24c9a20b-6825-3235-9d2a-c92ad2af65c5 | -4.77833 | -43.6456 | 2024-11-05 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a8c36c5a-13c2-3ab2-88d7-bc626676466a | -5.64679 | -43.07125 | 2024-11-05 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 33a16b88-b4bc-36d2-85d8-8d065d0d7662 | -5.48339 | -42.08489 | 2024-11-05 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)

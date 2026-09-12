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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c7c5391-7279-353a-8755-cdd71a2c190e | -3.2314 | -46.9376 | 2026-09-12 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| a7b277cb-0a19-3084-bcf2-dc7d6fd3906f | -5.7567 | -45.1067 | 2026-09-12 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.9 |
| e6143048-a5a1-3fb6-9039-1a376ce93c3e | -10.7018 | -54.1458 | 2026-09-12 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 7432b2cd-fba2-3d50-97dc-d7cc7c73283b | -2.7331 | -57.6465 | 2026-09-12 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 2654939a-559f-3455-85cf-8fa59cd983cb | -18.8868 | -46.9692 | 2026-09-12 01:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8e8e4706-bb72-31a9-a153-603291b94fd5 | -9.6451 | -49.6817 | 2026-09-12 01:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d771ab13-bb5e-3bc3-8667-2e11b9c454c3 | -18.6668 | -41.9962 | 2026-09-12 01:30:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.0 |
| b06b48f0-764e-3e1d-9df8-f27864ac1faf | -10.7015 | -54.1663 | 2026-09-12 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 284.9 |
| 0dded8d0-4606-308c-a72e-c468aa6a7d81 | -5.7754 | -45.1053 | 2026-09-12 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 4c57932f-ea7c-348c-b283-5e006e9bb961 | -5.7569 | -45.084 | 2026-09-12 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 231.8 |
| dda24cb5-bd22-31e9-944a-60e5626c2725 | -3.7462 | -61.7552 | 2026-09-12 01:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fedb5483-d290-37a0-b188-fa7cee24a5bd | -3.2128 | -46.9602 | 2026-09-12 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| de587e79-c3d6-3d63-91c2-a52c676d0bcf | -10.6827 | -54.1679 | 2026-09-12 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 162.0 |
| a9f944e7-32d1-3cf2-be52-68f2e1fbbdea | -10.6829 | -54.1475 | 2026-09-12 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 677e56f4-1c71-3f07-9e7e-7e3250c746d8 | -3.728 | -61.7555 | 2026-09-12 01:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d8b84f4a-9d03-30af-8042-588f8c9fb206 | -6.6206 | -58.8483 | 2026-09-12 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 73ac98f3-b524-33a1-ae15-c3750f857b2d | -4.3587 | -47.7853 | 2026-09-12 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| bd710878-220f-3717-a2e2-3b8f18c4b272 | -2.7148 | -57.6274 | 2026-09-12 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e958fea5-b553-329b-bea4-986de1bf420a | -9.1799 | -68.2194 | 2026-09-12 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 76760113-aaaf-3219-8bd8-79c422b93bde | -9.1798 | -68.2378 | 2026-09-12 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 90e9c031-a86f-3148-aab2-0a1db65af73c | -6.2243 | -51.6949 | 2026-09-12 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 012ddf33-38ec-3dec-84c8-f0fb3eb47a6f | -6.961 | -44.5546 | 2026-09-12 01:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9fbac511-0496-394b-bb98-a935caa1c0a9 | -5.7756 | -45.0826 | 2026-09-12 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 335.5 |
| d79febdb-68e1-3b43-a2b2-a76b4446fdf9 | -6.2607 | -47.2572 | 2026-09-12 01:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| dc7e836f-d161-3227-8b43-475a5739ce51 | -2.7331 | -57.6271 | 2026-09-12 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d4b88d3c-165f-3a37-882b-05508d06bd87 | -9.7133 | -64.9637 | 2026-09-12 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 2ae207e6-7284-3226-bdcd-29fc07795900 | -3.2313 | -46.9596 | 2026-09-12 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 194.2 |
| ccea08ac-1512-33bd-bc80-74ad11232e8d | -10.7018 | -54.1458 | 2026-09-12 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b6c80a62-c15f-3b7d-bd38-547b229c6e01 | -2.7331 | -57.6465 | 2026-09-12 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 4b0b1456-487d-3ca2-9e45-8d8500accc6c | -6.2243 | -51.6949 | 2026-09-12 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 12efcb9f-fbfa-3591-8a1e-f699b4841c1d | -2.733 | -57.6659 | 2026-09-12 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 53914abf-0b9f-30da-9613-5415de5b0e40 | -10.7015 | -54.1663 | 2026-09-12 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 222.4 |
| 096518ac-6d31-3b68-9a17-c8ff7b25e40c | -5.7754 | -45.1053 | 2026-09-12 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 270.7 |
| 2e99baea-d4bc-3b2f-b25a-b6618ab1e594 | -10.6829 | -54.1475 | 2026-09-12 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e01a35eb-aa2b-37d0-8a77-4cc566a77acb | -2.7331 | -57.6271 | 2026-09-12 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 1597c35b-ae8c-34f0-aa79-3b6a71c215c9 | -2.7148 | -57.6274 | 2026-09-12 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 29999c04-6644-3902-a75f-c9c8d69ed545 | -5.7569 | -45.084 | 2026-09-12 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 230.9 |
| f389316e-910d-3a5e-b8fb-b4d3077b04f4 | -9.7133 | -64.9637 | 2026-09-12 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d6097d95-cfca-336f-890a-ea177e2c87cc | -18.6668 | -41.9962 | 2026-09-12 01:40:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| d59ab782-8119-38a4-9282-025ea0be2d3e | -5.7567 | -45.1067 | 2026-09-12 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 2f79ab13-c454-3786-a21a-22d6ec4480b8 | -10.6827 | -54.1679 | 2026-09-12 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| a68dd01b-e5b7-3bab-8357-80f7b8c04e32 | -9.6451 | -49.6817 | 2026-09-12 01:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2c5a8ff5-6c3e-32c3-8c8b-22d8d78b10bf | -4.3587 | -47.7853 | 2026-09-12 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 64fc206f-7452-3dec-9175-20c9ad04b8b5 | -3.2313 | -46.9596 | 2026-09-12 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 205.2 |
| 095cd426-aedb-31fe-a1ed-b52db7893bca | -3.2128 | -46.9602 | 2026-09-12 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ded240a4-7aae-3dbf-b76f-cc830ff86f5d | -3.7462 | -61.7552 | 2026-09-12 01:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| de710886-f591-3aa4-a9be-f1acc44801bf | -3.2314 | -46.9376 | 2026-09-12 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 380c6613-1a14-341e-bfb1-7a10eeee4718 | -4.2951 | -49.1234 | 2026-09-12 01:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 51f05cdb-a2b1-31ec-99bd-8f2ebf1e9ca1 | -10.7013 | -54.1868 | 2026-09-12 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 88355a43-e76b-3613-94f8-e89be7a54c68 | -5.7756 | -45.0826 | 2026-09-12 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 278.3 |
| 15e49ba5-ee62-3aa0-bde0-5fa22b56f16c | -18.8868 | -46.9692 | 2026-09-12 01:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 81da8475-e563-3251-ad47-9f394d8c5910 | -6.2429 | -51.6939 | 2026-09-12 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0c9527f6-2312-3b46-af80-8792a5cdc397 | -9.6947 | -64.9644 | 2026-09-12 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0e8228dd-dbe4-3472-ad54-66e208860041 | -2.7148 | -57.6469 | 2026-09-12 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 9e7bbf09-fc9c-351e-aa73-a9c13751c570 | -10.7018 | -54.1458 | 2026-09-12 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 4a08edc9-2160-3c13-9713-d919e487d607 | -5.7569 | -45.084 | 2026-09-12 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 800c531c-6a2a-3b19-a42e-c8104e728157 | -2.7331 | -57.6465 | 2026-09-12 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 144.2 |
| a6f4222f-be4e-3d95-b502-8b5042cf839a | -2.7514 | -57.6462 | 2026-09-12 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 43eb9268-7756-36e8-9900-91fef5c2cebb | -18.6668 | -41.9962 | 2026-09-12 01:50:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| c26775b7-0588-3bf5-98c3-acf234fc261f | -2.7148 | -57.6469 | 2026-09-12 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| a762ce28-e434-3c8d-91d1-f9e4f48a30bf | -3.2313 | -46.9596 | 2026-09-12 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 208.2 |
| 3c10acbe-8680-3394-ba01-8572a5041762 | -2.7148 | -57.6274 | 2026-09-12 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 329c532d-ee5d-3b8b-b399-1b225bb1e1b2 | -9.7133 | -64.9637 | 2026-09-12 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 166dc987-739e-3669-a52d-92d4bd0fba3f | -5.7754 | -45.1053 | 2026-09-12 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 298.6 |
| f564b744-2065-352e-a6ed-8115b554d475 | -3.2314 | -46.9376 | 2026-09-12 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 54582b36-2b25-342f-80ac-69ac2abe23db | -6.2429 | -51.6939 | 2026-09-12 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a6735947-cf87-3e80-b460-8b88ce13b5ea | -6.2243 | -51.6949 | 2026-09-12 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 4c717ba5-30ec-34cd-851a-724fbb97cfd7 | -10.7015 | -54.1663 | 2026-09-12 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 191.5 |
| b2ac7812-73ec-392f-8ffa-0fc1781fd229 | -5.7567 | -45.1067 | 2026-09-12 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 0e46562d-6f19-3d38-bae8-9ea1ecfb44f1 | -5.7756 | -45.0826 | 2026-09-12 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 286.6 |
| 578d2b5a-fe82-3f19-95c0-6da93a205f73 | -10.6827 | -54.1679 | 2026-09-12 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 0d85f429-1393-364b-a225-5f41b6a9f6f7 | -3.2128 | -46.9602 | 2026-09-12 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 5b6a789c-14a0-3869-9777-b7092f3be071 | -12.1501 | -64.1414 | 2026-09-12 01:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 77e0ad97-df80-3299-816f-3a9caccfa2a8 | -3.7462 | -61.7552 | 2026-09-12 01:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e534943a-7b5b-3189-88dc-4995a8d78193 | -18.8868 | -46.9692 | 2026-09-12 01:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| ca28330e-df89-3e49-acab-9fc443039661 | -2.7331 | -57.6271 | 2026-09-12 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 3e6dbbed-8a29-3210-a07a-fc538ebfc0ea | -4.2953 | -49.1021 | 2026-09-12 01:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ffa2da00-c9df-39fe-9180-2d78b3504817 | -6.6206 | -58.8483 | 2026-09-12 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| fe3d0154-84d5-31eb-b44f-730316a8005d | -4.3587 | -47.7853 | 2026-09-12 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 902923ab-5d08-3d8f-adec-8d109f1e7733 | -18.6668 | -41.9962 | 2026-09-12 02:00:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| 6dcdabe7-4620-3467-b276-b3487265d64b | -2.7331 | -57.6465 | 2026-09-12 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 151.4 |
| e0f1775f-b25f-3a94-9972-1a4664fe7445 | -10.7015 | -54.1663 | 2026-09-12 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 36e6be8a-ba39-335a-b48a-4ba819c9243d | -10.2206 | -50.373 | 2026-09-12 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 7d7c4456-e02a-34ed-b019-d2fccb79642e | -10.6827 | -54.1679 | 2026-09-12 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 21acfdea-7d8a-3864-8b53-039562c3ce69 | -5.7754 | -45.1053 | 2026-09-12 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 226.0 |
| debc6c9e-282f-36a1-babf-9dcab2abf78c | -5.7567 | -45.1067 | 2026-09-12 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 84d34477-be30-39e5-a016-a6e95a9f104b | -6.2243 | -51.6949 | 2026-09-12 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d161c4e6-ecc3-3e2f-a576-c3e5a8f65b51 | -10.7018 | -54.1458 | 2026-09-12 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b328f63f-5878-3409-848d-b082149d9854 | -2.7148 | -57.6274 | 2026-09-12 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6350baf7-3d74-3268-95f8-bede9c4ccd30 | -10.6829 | -54.1475 | 2026-09-12 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b7d62f04-71ef-32e6-a992-a67804647bd4 | -4.3587 | -47.7853 | 2026-09-12 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 92a308e1-d615-37ab-875b-4532575928c4 | -3.2313 | -46.9596 | 2026-09-12 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 182.9 |
| faba2b41-c559-3416-a35a-8f35ecbef35e | -5.7756 | -45.0826 | 2026-09-12 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 312.5 |
| 895f1052-e64f-32cf-8e8d-e5151bc9e562 | -2.7331 | -57.6271 | 2026-09-12 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4e5d11fc-e976-36d9-96af-e289a3e33e3a | -5.7569 | -45.084 | 2026-09-12 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 187.5 |
| e9c0c5f3-4bff-35ff-8cb1-9c73a5776974 | -2.7148 | -57.6469 | 2026-09-12 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e39064a6-04a3-3670-8ade-4dc54be1f506 | -3.2314 | -46.9376 | 2026-09-12 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 8173b463-a134-38d1-8338-37b6c1a7eb39 | -6.2429 | -51.6939 | 2026-09-12 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d84ccc25-4ac2-38a7-a0e4-37d16d4a0083 | -3.7462 | -61.7552 | 2026-09-12 02:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b5c42afc-9cfb-3ecf-965b-ad5c16d39c73 | -9.7133 | -64.9637 | 2026-09-12 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |


[Clique aqui para ver as próximas entradas](README9.md)

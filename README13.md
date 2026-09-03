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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2823effe-a563-3065-a5ec-4e3e04cb0a9e | -3.2486 | -47.2438 | 2026-09-03 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 3730fd96-7b82-38d4-bc90-86e2e7a16429 | -6.6883 | -59.9436 | 2026-09-03 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 97cf85f7-478d-329b-9c5e-5f57f5a54165 | -18.776 | -48.9226 | 2026-09-03 01:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 1976041a-9485-3dbe-bbbe-33bd80ba2896 | -9.0415 | -65.7349 | 2026-09-03 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| bc54f2b9-6803-3d86-929d-44fe5e84e4cf | -6.3237 | -56.0434 | 2026-09-03 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 20eef1b5-e3e2-313c-9b81-033157c7a983 | -10.2028 | -50.2895 | 2026-09-03 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 22677507-4e97-3dfa-967d-74765b313c0b | -8.4677 | -54.6429 | 2026-09-03 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 60aa6f8e-ce76-3b66-bcb4-67752e4c2ed7 | -6.6542 | -59.426 | 2026-09-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 28c7185f-364d-31d7-b923-b9b30c9ea536 | -6.4209 | -58.2943 | 2026-09-03 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| bcf5958f-c3ae-3710-8a51-8fd9f79c027d | -6.6541 | -59.4452 | 2026-09-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| c3c0749d-d31c-346a-a65e-74a8d22bfa97 | -12.4037 | -44.7856 | 2026-09-03 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d8f05f7d-5869-3ddd-b2ac-1ec0ad3de99f | -11.0006 | -45.0847 | 2026-09-03 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 21152c13-6d2c-3fd1-a515-7c30bc47fff6 | -6.6882 | -59.9628 | 2026-09-03 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7ff5aec9-719c-3d99-a558-5cc6b4bf9689 | -6.6697 | -59.9635 | 2026-09-03 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b7b2bf9e-66ea-32c7-9e1e-4c26cee953dd | -11.001 | -45.0617 | 2026-09-03 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e5a7050d-e1f5-3ef1-bb3a-bccfce0c094d | -8.0737 | -50.9656 | 2026-09-03 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 24bfffdc-9afb-31ff-bdc4-462cf433780d | -10.9815 | -45.0874 | 2026-09-03 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 285277b4-ab0f-330d-9dcb-671014ffbfea | -6.6698 | -59.9443 | 2026-09-03 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e5812ed1-217a-3fb3-a051-b536c670674d | -8.5916 | -67.1788 | 2026-09-03 01:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b6c01d5d-c39f-355e-85c7-b8cfbd0b3fc0 | -18.7766 | -48.8999 | 2026-09-03 01:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 11ef1ac5-1de1-3b90-978a-54e9da9b73fe | -8.0924 | -50.9642 | 2026-09-03 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| d3a2923c-c667-3e5c-a677-28b00fbc22f4 | -6.6357 | -59.4459 | 2026-09-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| c8ce0139-af15-3327-9cd7-a90d7b39ee55 | -9.5721 | -40.3475 | 2026-09-03 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 22dfe7e1-9b85-3c7a-9b46-ee7b2641ccd6 | -18.7766 | -48.8999 | 2026-09-03 02:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 9e230dc6-7a10-3a1c-a203-a816f1c9f586 | -6.4209 | -58.2943 | 2026-09-03 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| b0fd4682-0911-38ad-908a-07779139f30a | -6.6883 | -59.9436 | 2026-09-03 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 9e12efd2-13ff-3445-b7d6-bec33c387a16 | -8.449 | -54.6442 | 2026-09-03 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b9247433-f6c8-3e4b-bcb6-2b8c52c3794d | -9.0415 | -65.7349 | 2026-09-03 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d7de09e0-b48d-3966-adcb-30a3a48bbcd8 | -6.6698 | -59.9443 | 2026-09-03 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ec408454-498a-3fbe-ab57-d9e6c53702e0 | -8.4487 | -54.6846 | 2026-09-03 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0a76b653-c6d4-324e-85de-de943b6f2b21 | -8.4675 | -54.6631 | 2026-09-03 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| db94316d-b04f-30df-920a-bc1afdcfc418 | -6.3237 | -56.0434 | 2026-09-03 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f221147e-c5ba-3d34-85ff-7e34ca2d0a1e | -8.5916 | -67.1788 | 2026-09-03 02:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c53f1fc3-44f7-3ae1-97ce-7e29d7044396 | -6.654 | -59.4645 | 2026-09-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 17d36ede-1db9-3d7c-a07f-fc3c639eeae7 | -6.6541 | -59.4452 | 2026-09-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| e3449754-3be8-33ed-97a0-3db9cf4c273d | -6.3051 | -56.064 | 2026-09-03 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| fd0b0888-1224-34d4-8d29-59843be84bc2 | -6.7648 | -59.4408 | 2026-09-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| c598b127-7ef9-3c93-90da-e15d6e6a5998 | -12.4033 | -44.8089 | 2026-09-03 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 0907b7fa-33aa-3392-9332-85e479ff36f9 | -6.3052 | -56.0442 | 2026-09-03 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| aad1a2f6-efe9-3a5e-8351-c71c1891e17a | -6.6542 | -59.426 | 2026-09-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0214ea4e-ddb2-38df-acf5-e78e0d2fd1d2 | -6.4208 | -58.3137 | 2026-09-03 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 5bf07a0a-f9fb-398e-a44b-d169d0b4cc35 | -6.6358 | -59.4267 | 2026-09-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| ed13f340-67dd-3115-94b1-b7ca000df1f9 | -12.4225 | -44.8059 | 2026-09-03 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4b23757f-4294-3334-b17a-2139178d011c | -18.776 | -48.9226 | 2026-09-03 02:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 71dffcfb-6727-37b2-a26b-f7fa2a1e6d12 | -8.4488 | -54.6644 | 2026-09-03 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| ea1726dd-c51f-3e92-8a54-94097146d183 | -11.0006 | -45.0847 | 2026-09-03 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 56f701dc-c9e4-38f3-9a8e-fb01b607215b | -6.6356 | -59.4652 | 2026-09-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| fccd8fb5-a244-3d50-871d-b9331a771f95 | -10.8826 | -45.3075 | 2026-09-03 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 54ff7a4c-15ba-3697-8c44-725600739c67 | -10.2217 | -50.2876 | 2026-09-03 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 3ce08ba7-0c20-36b7-ba1e-74de3be90755 | -8.4677 | -54.6429 | 2026-09-03 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| ddf80574-2a08-36c6-a4d1-1967ddd7450b | -3.2486 | -47.2438 | 2026-09-03 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| bc60dfad-80b9-3210-9e2f-bd7ce5a7eb8c | -6.7463 | -59.4416 | 2026-09-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 310406dd-fa41-3e76-92c7-6e6a49038c01 | -8.0737 | -50.9656 | 2026-09-03 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2211e86e-db8e-3ee7-972a-480f45152cd1 | -6.6882 | -59.9628 | 2026-09-03 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1b9393ee-8bcd-3b15-94c6-3696046f2a2f | -6.6697 | -59.9635 | 2026-09-03 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 1df38ad9-f93d-35a8-a8ac-6ba243667ef3 | -3.2485 | -47.2657 | 2026-09-03 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 560698ed-2d0d-3018-b263-d9ce32589749 | -7.4954 | -60.7736 | 2026-09-03 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| d809ba64-21a8-38e5-8ad4-5774eca1cce6 | -10.2028 | -50.2895 | 2026-09-03 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| fc534aa1-4c9a-3cd4-92bb-f61fb1076042 | -10.9815 | -45.0874 | 2026-09-03 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| bd7c41c7-e879-3d33-942b-baf3f0217876 | -6.3236 | -56.0632 | 2026-09-03 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 6287ced7-bb7b-3b90-a9e0-5461aaab7663 | -6.7648 | -59.4408 | 2026-09-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e5bab7b9-e101-3b41-8ed2-f326b0edf1b8 | -6.6698 | -59.9443 | 2026-09-03 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6575dd7c-d0d6-3b6f-93fc-a2c9493bf506 | -7.5138 | -60.7728 | 2026-09-03 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8051291d-270b-3764-be17-de5487cf6643 | -10.9815 | -45.0874 | 2026-09-03 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 22fc54c1-77f0-3182-b783-e1935513da5c | -8.5916 | -67.1788 | 2026-09-03 02:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 77eb89f1-0fe1-32b5-9fb4-fc96951a7041 | -6.4208 | -58.3137 | 2026-09-03 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| ab8ae523-5e27-3c9c-aa74-fda2903de832 | -6.6357 | -59.4459 | 2026-09-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 209.2 |
| e63f461b-4616-3e91-a266-21589e046293 | -6.3236 | -56.0632 | 2026-09-03 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 26c5c027-29c8-3e1e-86e1-be5aa2300b93 | -6.6541 | -59.4452 | 2026-09-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 44517974-d27d-3cce-bf09-6d6730ee08c1 | -18.776 | -48.9226 | 2026-09-03 02:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 117.6 |
| a13f4597-08c0-3178-9cc4-cf14d1efe820 | -10.2028 | -50.2895 | 2026-09-03 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 885f2458-a1c2-3492-8f55-44af4b35f13e | -10.2031 | -50.2681 | 2026-09-03 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d9f6d7f3-7aa6-3e1c-874b-1b2bbff33e22 | -3.2486 | -47.2438 | 2026-09-03 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a126f5f3-7c3d-3347-af0e-db70661dc891 | -12.4033 | -44.8089 | 2026-09-03 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 77066abc-e4ed-37ab-93b2-505df5a38983 | -11.0006 | -45.0847 | 2026-09-03 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| c2624372-6677-32b7-b920-4c0c9c65375f | -6.7463 | -59.4416 | 2026-09-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 82dde848-ddb1-3855-9208-da35fd33a601 | -18.7962 | -48.9186 | 2026-09-03 02:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b6aad6b7-fc9f-33cb-82e3-61a9a5991c45 | -6.654 | -59.4645 | 2026-09-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 7530d4f6-2f87-3595-b04f-317b2ee078d7 | -6.6358 | -59.4267 | 2026-09-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 10962518-5c02-3c03-aec5-aba6f8b01075 | -3.2485 | -47.2657 | 2026-09-03 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c1263b81-acf9-34d0-a245-265bf1e2974c | -6.6356 | -59.4652 | 2026-09-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| eb688c4e-ec64-33b4-a90c-c5ec32715ae2 | -18.7766 | -48.8999 | 2026-09-03 02:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 0ecffe24-c7b2-3f18-a355-a3947287853c | -9.0415 | -65.7349 | 2026-09-03 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5ed006e3-c6ba-3940-b445-6ab3a5baaf2f | -8.43 | -54.6858 | 2026-09-03 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 36adac93-c9ee-3df6-8060-679e565cd0e9 | -8.4675 | -54.6631 | 2026-09-03 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 525bf58a-d2b1-33a7-9173-87368ec62224 | -10.5281 | -49.9778 | 2026-09-03 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b3781efb-16d7-3023-8993-dd15f57638aa | -6.6883 | -59.9436 | 2026-09-03 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.5 |
| a3d20b20-5054-3f18-b0c0-13ae18c828b5 | -8.0924 | -50.9642 | 2026-09-03 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a49e4877-24c6-343b-870d-448d36e25a8f | -6.3052 | -56.0442 | 2026-09-03 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| fab339b0-5332-3bc2-a8fe-bf248ae632e0 | -6.6882 | -59.9628 | 2026-09-03 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 90d2fd57-c8fa-3eb3-a3c8-a3f1db4fc12b | -8.4677 | -54.6429 | 2026-09-03 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| f2eefee8-add2-34a5-b5b1-7ba20c0967e5 | -10.8826 | -45.3075 | 2026-09-03 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 2b6dc5d6-fcf2-38fe-a919-a96037535d9d | -6.3237 | -56.0434 | 2026-09-03 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f5e97d95-cc95-3f27-983e-cac4cbb50b71 | -6.6542 | -59.426 | 2026-09-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1fd90f5a-868e-301c-9fa5-0923bac76cca | -12.4037 | -44.7856 | 2026-09-03 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4f395639-9077-3294-8314-19a665207e7e | -12.4033 | -44.8089 | 2026-09-03 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 510eacde-6b74-30cf-9baa-6be04e022f69 | -6.3052 | -56.0442 | 2026-09-03 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 43068c73-0e69-39d4-80b6-b6c434d1ad59 | -10.9815 | -45.0874 | 2026-09-03 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 13ea4773-8946-3f63-b254-e0aac95aaf77 | -12.4037 | -44.7856 | 2026-09-03 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 11548974-8953-3282-a04d-b0cd91185961 | -6.6697 | -59.9635 | 2026-09-03 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |


[Clique aqui para ver as próximas entradas](README14.md)

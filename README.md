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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cf44545-84ae-39fc-8d0c-7ee94515dd14 | -17.7603 | -50.5894 | 2025-07-21 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| bcd4710c-b80e-3508-a2be-b93fcdfe1c5e | -17.7802 | -50.5859 | 2025-07-21 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 2e21a497-6590-3bff-a3a1-20bb28dedea1 | -17.7797 | -50.608 | 2025-07-21 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 8d4029d0-f46f-3eef-9b9e-d52afc4bac0e | -3.042 | -47.8607 | 2025-07-21 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 2aa95b1a-3518-3e6c-9614-ea4bb8a0be9f | -8.921 | -47.3595 | 2025-07-21 00:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| fe166faf-2abb-34de-9df4-974c206195a2 | -3.042 | -47.8607 | 2025-07-21 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9a9129ee-c38b-3838-91f1-a252f1cbba45 | -17.7603 | -50.5894 | 2025-07-21 00:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9f3ed06d-d54f-30b4-a693-6e322c98d512 | -23.6991 | -51.7459 | 2025-07-21 00:20:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| b9b46b21-449e-3f35-bc44-44ed316bcbb0 | -17.7603 | -50.5894 | 2025-07-21 00:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 2cb596ca-519d-34b6-b221-ead3999d0515 | -23.6997 | -51.723 | 2025-07-21 00:20:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 87.4 |
| f706ee80-b8e1-3015-8f6f-3c93b441c22e | -10.1546 | -49.6519 | 2025-07-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| af0985fe-3142-3eee-83a9-64d619cb3180 | -10.1357 | -49.6538 | 2025-07-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| eb15ad99-e00a-377e-a1c8-263bc3ab0a8b | -17.7603 | -50.5894 | 2025-07-21 00:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 8ef02e15-9693-3a9b-8b26-6da0b6b525fd | -17.7603 | -50.5894 | 2025-07-21 00:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 7e056aa2-96dd-3144-9121-dafea1a6640e | -15.7676 | -49.9555 | 2025-07-21 00:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 1a103d4f-1067-3b9a-ba8b-706f68b9dfd4 | -15.7876 | -49.9303 | 2025-07-21 00:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 6b581a48-903a-3e49-8ecd-4a340f95c3fd | -15.7872 | -49.9523 | 2025-07-21 00:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 470ea41d-8aa6-332d-95ee-d6da0bc3fee0 | -10.1357 | -49.6538 | 2025-07-21 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f1dd9e50-f001-3e5f-a869-ed56c606fde6 | -17.7603 | -50.5894 | 2025-07-21 00:50:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| af4d1ee0-333d-3b64-8297-86072d5e605f | -16.0997 | -49.9677 | 2025-07-21 00:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 46.1 |
| aacced33-ade8-309d-9d9b-aabc5a47a385 | -16.0997 | -49.9677 | 2025-07-21 01:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 47c5047d-08b1-3a81-86ac-fb64ff4da6f4 | -3.042 | -47.8607 | 2025-07-21 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d730ae72-6a30-3c48-9fda-ce0fadf4dfdc | -10.6693 | -46.7628 | 2025-07-21 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4b783f12-e51d-328a-8ba0-7113dc4d91a5 | -10.6883 | -46.7604 | 2025-07-21 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 9f688fa3-1ab0-398b-94a7-b65d2a7c761d | -10.6689 | -46.7853 | 2025-07-21 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e8cc51f2-17b6-3be1-9219-4acf667790a4 | -10.688 | -46.7829 | 2025-07-21 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 4f55d505-8bff-3532-956c-4450477c894e | -23.5558 | -51.619 | 2025-07-21 01:20:00 | GOES-19 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 89.3 |
| 89edacc4-8e16-3899-a80e-26849ea4d005 | -10.6693 | -46.7628 | 2025-07-21 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 50a527ee-cdb5-39e8-bace-f497fba917d4 | -10.6689 | -46.7853 | 2025-07-21 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 6d115186-4358-3f9a-8eec-0a51a3d78aae | -23.55158 | -51.62799 | 2025-07-21 01:22:00 | TERRA_M-M | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 46.1 |
| e7d56e69-c5dd-32ef-a104-cf155f404126 | -17.76522 | -50.60479 | 2025-07-21 01:22:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 874a8fce-4fc2-35c9-a7b7-b8f77440e7c7 | -20.26981 | -54.80274 | 2025-07-21 01:22:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c3541110-ec07-36d1-8a06-8bbc4da17ec5 | -7.27785 | -60.17577 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| bf3e3110-c3cc-35b5-9904-a6e43c45a02d | -7.26898 | -60.17705 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 046c487f-a3fa-3079-ac34-84f2cf59bd2f | -10.29475 | -60.54849 | 2025-07-21 01:24:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2af2f8ae-00fe-3914-8c46-5b82995c087d | -8.95861 | -62.22109 | 2025-07-21 01:24:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fb33e4cc-0506-3f6d-92e2-03bea8b919f2 | -7.27909 | -60.18468 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 902b7145-da0f-305c-9ea8-950e57ced835 | -7.23477 | -60.19104 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 219.2 |
| 61302baf-96a0-3961-a261-bb1b477b4ef5 | -10.29351 | -60.53948 | 2025-07-21 01:24:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 18dcbe0a-2be3-3827-98c6-4902d4f00bbb | -13.45328 | -60.97566 | 2025-07-21 01:24:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6181e00c-33df-3922-9a57-e7030e004961 | -7.27023 | -60.18597 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 8f572b9c-c0ea-3567-96c0-74ad95fafa6e | -7.16647 | -59.64085 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cd2d95ad-cc3e-35d1-b3df-b795a518ac72 | -10.03825 | -59.09967 | 2025-07-21 01:24:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 76cfc7c0-8509-39fb-8e46-1ad957cc1141 | -7.24488 | -60.19868 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 4de29d7b-d515-3c35-af5e-733e49e20631 | -7.29434 | -60.16431 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| cd4a7fc6-8117-3788-814f-0df8e90131be | -7.28671 | -60.1745 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 184.1 |
| 538b5b6a-2774-36e1-9dbc-9b0650c8d674 | -7.26136 | -60.18724 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 14359515-4c23-3885-a9aa-f228975a4cc0 | -7.28547 | -60.16558 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 2e03db17-7f01-3836-8251-629129437088 | -7.24363 | -60.18978 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e4ff542a-d500-3fe7-9280-003382fe61f2 | -7.27661 | -60.16686 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 2f474fca-0f22-38c5-bc76-aa045139b405 | -8.49686 | -64.03724 | 2025-07-21 01:24:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| edf9809d-0350-3fec-9e96-30223356bb1b | -7.29558 | -60.17323 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 073f9dd9-d1a2-35d6-afa2-f739fedb94e2 | -7.2525 | -60.1885 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 68faf451-bacb-3663-9465-0263b7e4e4c0 | -7.23601 | -60.19994 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| cf89d454-2a2c-35c1-8790-a724e50562e1 | -7.26012 | -60.17832 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 0e97dc93-3f10-31b1-8a60-18b1bb552517 | -7.23726 | -60.20886 | 2025-07-21 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d4a34b5f-8f24-3199-b55b-cadacdc07463 | -17.7802 | -50.5859 | 2025-07-21 01:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 064f4d03-e4c4-3e0c-a2ed-8ebc5e48095a | -10.6689 | -46.7853 | 2025-07-21 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1d978265-b8bc-3d4c-a506-6cddb1cb6975 | -10.6693 | -46.7628 | 2025-07-21 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| af576be9-0530-32bc-8070-dc604278a4f7 | -7.2957 | -60.169 | 2025-07-21 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 361dcdca-cd8e-3df8-a09b-99546990b2df | -7.2402 | -60.1904 | 2025-07-21 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| c972982d-dfa8-3d82-8dc4-58d2133fd55b | -7.2772 | -60.1698 | 2025-07-21 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 198.8 |
| 36dddaac-efde-3ea3-951f-57abe23dc2d7 | -7.2771 | -60.1889 | 2025-07-21 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 74bae56a-619f-35cd-b5f7-a094871c9788 | -10.6693 | -46.7628 | 2025-07-21 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 88b5981d-8bd2-3192-94d8-7f04d04054c2 | -10.6689 | -46.7853 | 2025-07-21 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8f33f40b-5f12-33cf-867d-f87aa1dcedbd | -7.2588 | -60.1705 | 2025-07-21 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 30085bd5-ebe6-314f-aeaa-9f18493189c1 | -7.2587 | -60.1897 | 2025-07-21 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| c5521517-9b3f-3b15-893c-147cb09d9974 | -10.6689 | -46.7853 | 2025-07-21 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 25eb51d0-15e7-314d-a0d8-ea71fad86c28 | -7.2587 | -60.1897 | 2025-07-21 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| acfb7fba-7a4b-3da7-89f8-2ad614b3c9f0 | -7.2771 | -60.1889 | 2025-07-21 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1d3e0756-2078-3322-b2e5-ee225caabf87 | -7.2957 | -60.169 | 2025-07-21 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 0e10d465-1fae-343d-8013-5585742a0858 | -7.2772 | -60.1698 | 2025-07-21 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 167.5 |
| a16d47ed-a1fb-3ac1-bbba-d9ecb615ddf3 | -7.2402 | -60.1904 | 2025-07-21 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| ec2fac38-9b9f-3ed0-bb9c-b4bc1791cac2 | -7.2588 | -60.1705 | 2025-07-21 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a215e3dc-3695-3966-9a37-268571ab7ce7 | -7.2402 | -60.1904 | 2025-07-21 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 4dedc5e7-30a1-36f5-8d1a-9d9c15de6a9d | -7.2587 | -60.1897 | 2025-07-21 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9c980d09-180a-3651-8e83-6d3961716399 | -7.2957 | -60.169 | 2025-07-21 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 03fe132d-da94-3ea2-92eb-17c5bc054415 | -7.2772 | -60.1698 | 2025-07-21 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.2 |
| c2531931-5cf7-390e-bce8-7402b3c48b22 | -7.2771 | -60.1889 | 2025-07-21 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 1b2266d5-1629-3cf8-a609-04d48eb2942e | -7.2402 | -60.1904 | 2025-07-21 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| ab61d6b7-59ea-3a3c-a936-ece1f22d885d | -7.2772 | -60.1698 | 2025-07-21 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 22ab3e6c-b4de-3e0c-820d-8040a82b69ca | -7.2771 | -60.1889 | 2025-07-21 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 43786815-9c47-398e-ad65-09490ad77782 | -7.2957 | -60.169 | 2025-07-21 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 3ec47660-5f04-38fb-a377-996f5cce9bd0 | -7.2587 | -60.1897 | 2025-07-21 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6f7c7c1e-438c-3cc9-bc4c-7cd9ad2d4fd9 | -7.2772 | -60.1698 | 2025-07-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 6ccef1d0-c243-38ea-8571-fbb0e209cf37 | -7.2957 | -60.169 | 2025-07-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 8c88c8cd-babf-31d4-a976-b7fe7ca8b5d4 | -7.2771 | -60.1889 | 2025-07-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ba47f265-a3f1-3088-a8fd-c968c2d344ea | -7.2402 | -60.1904 | 2025-07-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 64e1d97e-6048-3662-9867-a99f98225c59 | -7.2587 | -60.1897 | 2025-07-21 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8637c4d2-d26b-3217-8a6e-981c5a7c54b7 | -7.2587 | -60.1897 | 2025-07-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0f3ce908-dcad-3b04-b47e-bdd5e93e8bdb | -7.2771 | -60.1889 | 2025-07-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 244797ea-cdec-3267-ab3d-8d15fd1480cf | -7.2957 | -60.169 | 2025-07-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a9ebc3dc-c2a2-3dbd-87d0-3d0c1a5fe168 | -7.2772 | -60.1698 | 2025-07-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 5414d7ee-b121-3667-ac47-c51becb4db2a | -7.2402 | -60.1904 | 2025-07-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| aa9671f8-8123-3a09-9691-800bc0921735 | -7.2771 | -60.1889 | 2025-07-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 235f68eb-22c4-33c9-a1c0-e2865b740127 | -7.2402 | -60.1904 | 2025-07-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 86838a78-3a66-3299-94fd-38412a879e2d | -7.2772 | -60.1698 | 2025-07-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 6720a5e5-6b19-3d21-8b93-44714fd4a93f | -7.2957 | -60.169 | 2025-07-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 2fb62aa1-5286-3693-b48e-7e0db7aeea20 | -7.2587 | -60.1897 | 2025-07-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 79a03878-5ca4-32ec-8bd3-6bce13f96a34 | -7.95095 | -43.97804 | 2025-07-21 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README2.md)

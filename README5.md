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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d03b711b-8e15-303f-8c2e-6a109cf8ba6a | -3.1787 | -50.5807 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 16103c1b-7913-3fda-a026-7f38f080a474 | -3.2171 | -50.2021 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 7d15e3c0-f1e6-398e-93c0-5967d2d096b2 | -3.2172 | -50.1811 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c26a6699-afda-3753-a3d4-5d2cfbee1908 | -3.234 | -50.5999 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 59d43640-4f34-3dd9-9b82-b504fe95668b | -3.234 | -50.5789 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f617fdca-54b5-35dc-9884-be907c791eb8 | -3.2534 | -50.3689 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d6bf436d-b6d0-34d6-aa8a-3a3d4a4b25ec | -3.2535 | -50.3479 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 02373559-cad3-389b-a12e-6ddf37b3d8b6 | -3.2535 | -50.3269 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| e48f8f2f-457c-3010-ae31-8b19ec1f9830 | -3.2719 | -50.3473 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d4edcb69-44b1-347c-98ee-cf6e955f366d | -3.5171 | -49.2402 | 2024-10-30 00:15:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 89cce6aa-ef91-3bb4-8429-c945b0192e39 | -3.5172 | -49.2189 | 2024-10-30 00:15:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a6c1e10c-5457-340a-bd0f-264bebb32d9c | -3.5356 | -49.2395 | 2024-10-30 00:15:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| bb7d1e88-0039-32b9-83b3-27bd253c534a | -3.5357 | -49.2182 | 2024-10-30 00:15:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 29d56390-9b37-3c92-9371-eb03aa8ec8a6 | -3.563 | -47.4066 | 2024-10-30 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 01f0c10c-a3cb-3fe0-a51c-0caf3134d782 | -3.5631 | -47.3847 | 2024-10-30 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 329.5 |
| b30e289b-df12-373e-ac2d-ef59bb245813 | -3.5632 | -47.3629 | 2024-10-30 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 44929c4d-d85d-36a9-9851-8ffa796c72d3 | -3.5688 | -50.043 | 2024-10-30 00:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| cd32683e-b23b-3fe7-8a6a-0a9222341e9a | -3.5689 | -50.0219 | 2024-10-30 00:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| dcb75d4d-dd1b-3b2e-83a3-fe0b39e31796 | -3.5817 | -47.384 | 2024-10-30 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| f3472619-f834-3ec7-b747-d10d67493e03 | -3.5818 | -47.3621 | 2024-10-30 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 8aaf1e8e-9c63-3e73-94b7-1a8ec96f0170 | -3.7852 | -51.1651 | 2024-10-30 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c9431deb-3aa4-3859-bf40-01f070125575 | -3.8036 | -51.1852 | 2024-10-30 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3537fd18-c68b-3e22-9ae9-d388f914d27e | -3.8037 | -51.1644 | 2024-10-30 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 214.4 |
| 079b7fee-1e64-35a0-bc3d-5942877fa9d7 | -3.8038 | -51.1436 | 2024-10-30 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| bdd8209a-8074-3e5d-a21c-ae5ac0b436a9 | -3.9326 | -41.4957 | 2024-10-30 00:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| c825a40c-792d-335d-9a99-c7f957ead6e1 | -3.9327 | -41.4717 | 2024-10-30 00:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 230a132e-dafd-3e5d-8533-f3f0469d17f0 | -3.9513 | -41.4946 | 2024-10-30 00:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 3bd233c6-f221-3c43-a7da-9fddb79e222f | -3.9514 | -41.4706 | 2024-10-30 00:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 247221ca-1829-3c39-affc-5c6ea767f2fe | -3.9486 | -48.1291 | 2024-10-30 00:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 20b93508-3f6d-335b-a19a-d774520d2a35 | -4.0705 | -46.2836 | 2024-10-30 00:15:29 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 52df37aa-d057-3755-b292-8f80f4e9d8bf | -4.0681 | -50.024 | 2024-10-30 00:15:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| da9b6572-b1b7-3cca-a758-a4d4f00377a5 | -4.0682 | -50.0029 | 2024-10-30 00:15:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 74ad8098-85f9-3b41-91e9-22a946b48f93 | -4.0911 | -45.9488 | 2024-10-30 00:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 4d0f5fef-6bbe-36ba-ac8f-6b3b24b2caf4 | -4.2561 | -43.46 | 2024-10-30 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| f17b1508-7a88-3c1e-952f-a41411fb129c | -4.2563 | -43.4368 | 2024-10-30 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 189b4370-81d5-33ed-8c27-319a72320c36 | -4.2748 | -43.4589 | 2024-10-30 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 107fc88d-7c3c-31d8-987b-dbd7f4506db5 | -4.2749 | -43.4357 | 2024-10-30 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a99462e0-876d-3c3f-bc0d-95709e7a3597 | -4.3473 | -43.779 | 2024-10-30 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 620b4dca-f9cd-355f-b50b-701bb1079f0c | -4.2496 | -50.6677 | 2024-10-30 00:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7eec59c5-766e-31a5-bf18-0582eb5b440b | -4.2679 | -50.6879 | 2024-10-30 00:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4dd3c353-6ba3-3188-abba-4df5de577812 | -4.2681 | -50.6669 | 2024-10-30 00:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 804fa31c-dff0-30a1-8fbd-3765868fbc0d | -4.2682 | -50.646 | 2024-10-30 00:15:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| c753deff-22d4-3bf5-a27b-31c92c9c462a | -4.5012 | -43.143 | 2024-10-30 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 60e3d0d6-6e58-33f5-b5fe-0b0c897b004c | -4.5014 | -43.1196 | 2024-10-30 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| a45bed66-7df9-30c7-949f-eb9179997f6a | -4.5201 | -43.1185 | 2024-10-30 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 02e47fcb-7032-31de-9065-7895bf4cfc1f | -5.2306 | -47.9566 | 2024-10-30 00:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8a88c1ba-8453-3fd9-80bd-03f3c182292a | -5.2308 | -47.9349 | 2024-10-30 00:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 762d4481-7672-3570-9d2e-a8d840293b67 | -5.9788 | -45.3621 | 2024-10-30 00:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| edc88063-9b04-31ff-b969-1b6a5431ecea | -6.8408 | -59.0519 | 2024-10-30 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| fe32f8f5-f2b3-3742-b603-e7fc0e884a9f | -6.8409 | -59.0326 | 2024-10-30 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 47319d7a-0077-3ffd-9d1d-5f512ca95fd5 | -6.8591 | -59.0705 | 2024-10-30 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 79c505d1-599f-38d4-9c2e-12c2779428b2 | -6.8592 | -59.0511 | 2024-10-30 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.2 |
| a77ea524-fdc2-3679-a2a2-cbd8cfe9bd6b | -6.8593 | -59.0318 | 2024-10-30 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 892c8d54-adf0-3d76-a874-d197c7181d9f | -7.8736 | -46.9065 | 2024-10-30 00:15:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| d656e204-e2c6-37bc-99de-74f2920de9e3 | -7.8739 | -46.8843 | 2024-10-30 00:15:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 7a934795-1226-3afa-9306-f14d5c56be7e | -9.5563 | -63.1411 | 2024-10-30 00:16:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1a7e35dc-98a7-3b62-9c70-1d15e8b6390a | -10.1577 | -36.4886 | 2024-10-30 00:16:02 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 70.7 |
| bae7dc71-32c4-33cd-a5c9-00c70b68320e | -10.177 | -36.4852 | 2024-10-30 00:16:02 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 101.2 |
| d6dde683-b4a0-372f-8896-b206507a0afb | -10.1775 | -36.4582 | 2024-10-30 00:16:02 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 72783066-18ff-32e5-9673-7d6194e0fa91 | -10.6984 | -44.9186 | 2024-10-30 00:16:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 67a12739-8675-35a5-9af4-fb6a6e22348d | -10.7171 | -44.9391 | 2024-10-30 00:16:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e765d7b9-de0f-31b2-ac56-9d42d75fa164 | -10.7175 | -44.916 | 2024-10-30 00:16:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 183.6 |
| d52367c2-617f-3ba3-9e5c-9497d8dcf2ee | -10.7366 | -44.9135 | 2024-10-30 00:16:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 86e40b98-6012-3285-a0e4-a3f2df1b94f1 | -12.899 | -45.0549 | 2024-10-30 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 84003924-b8aa-3bbe-9007-45fe0c1284aa | -13.6891 | -46.1017 | 2024-10-30 00:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 75c83529-7f7f-3a81-9af1-7a52b7bf6946 | -18.2454 | -55.9793 | 2024-10-30 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| b2078a7f-1e1b-3b3b-8aaf-9a241d196e08 | -1.063 | -47.6452 | 2024-10-30 00:25:12 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 6a7df68a-da2a-3c72-a241-39f8f02ad039 | -2.2011 | -50.5852 | 2024-10-30 00:25:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 61b0bc34-c7c9-3f6b-8cfc-ecf45c47ab3a | -2.3906 | -48.9337 | 2024-10-30 00:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| b5bf2a0f-3bcd-3b15-886b-3483433ecd6a | -2.833 | -49.2413 | 2024-10-30 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 247e2548-2003-3db6-8ea6-59503f513b03 | -2.8331 | -49.22 | 2024-10-30 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 8e87b899-1161-35e4-8a5a-348052ca02d3 | -2.8515 | -49.2408 | 2024-10-30 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| cf88e6b0-8921-3567-972c-61777f18a471 | -3.0543 | -45.096 | 2024-10-30 00:25:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| bafd410f-0dff-3172-a992-15f172143f13 | -3.0734 | -54.167 | 2024-10-30 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 4f80d24e-4ae4-339d-8f0c-933f9e0e7687 | -3.0913 | -54.287 | 2024-10-30 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 26c90efc-057f-34d0-b87a-c4dcfeca01e1 | -3.0914 | -54.2669 | 2024-10-30 00:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ad480bb8-b7bd-3039-ad86-a2b0c85c0379 | -3.1028 | -51.1041 | 2024-10-30 00:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e1aa9beb-b6ab-3f88-8885-2afb870a8687 | -3.1097 | -54.2865 | 2024-10-30 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 5524792b-eb0a-36ae-a654-1b19097f1922 | -3.1098 | -54.2665 | 2024-10-30 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| f1c0a608-2ce2-3506-8797-6bdfef949de4 | -3.1281 | -54.266 | 2024-10-30 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 20549843-5eb5-3a5f-af89-87fb55c98d29 | -3.16 | -50.6231 | 2024-10-30 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 6e9b6565-0def-3a17-b12f-fd34bd87003b | -3.1601 | -50.6021 | 2024-10-30 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 296a8660-f6a9-3b48-9445-cfbf3f34116b | -3.1602 | -50.5812 | 2024-10-30 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d09dbad8-1671-30c7-bbfa-4799b71a83b1 | -3.1786 | -50.6016 | 2024-10-30 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 699ae44a-1291-31c7-a72e-9bae996a5122 | -3.1787 | -50.5807 | 2024-10-30 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d198614b-a729-3b11-ab84-de8d2221872f | -3.2172 | -50.1811 | 2024-10-30 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| befd32b8-e85d-3675-a61b-44a9abe3bc43 | -3.234 | -50.5999 | 2024-10-30 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 06a3bad0-59a7-321c-9509-9f06d07b2dff | -3.234 | -50.5789 | 2024-10-30 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| ea109984-50ff-3573-8e1d-7f2ba3015f68 | -3.2357 | -50.1805 | 2024-10-30 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 4504b5fe-c8b1-3889-a163-726014cf63a4 | -3.3385 | -44.0599 | 2024-10-30 00:25:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 25cbb4d5-a61c-3d67-ade1-75ddc8a385a4 | -3.5171 | -49.2402 | 2024-10-30 00:25:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 8acb0f18-9888-32cc-952f-fe3eb104d6f4 | -3.5172 | -49.2189 | 2024-10-30 00:25:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7b51350c-3175-34b8-b3e4-2e4a610ce7e4 | -3.5356 | -49.2395 | 2024-10-30 00:25:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0ce15daa-0618-3568-bed8-9ea3056cb40b | -3.5357 | -49.2182 | 2024-10-30 00:25:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 856eaab9-7f05-3d8c-a284-782b6d34a620 | -3.5631 | -47.3847 | 2024-10-30 00:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 353.5 |
| d14806b0-ea15-3ed5-90ec-399209be1e93 | -3.5632 | -47.3629 | 2024-10-30 00:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 126c4eda-0255-3891-bb11-d8d87cc9fe2f | -3.5688 | -50.043 | 2024-10-30 00:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 2491c6a7-b009-32dc-afb4-9fcb43c6b2cd | -3.5689 | -50.0219 | 2024-10-30 00:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 70e5e6e6-ee3a-3036-bad2-d5c3244f5a41 | -3.5817 | -47.384 | 2024-10-30 00:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 178.9 |
| 56074028-92bd-3e1a-9856-76b4ef8c0cad | -3.5818 | -47.3621 | 2024-10-30 00:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |


[Clique aqui para ver as próximas entradas](README6.md)

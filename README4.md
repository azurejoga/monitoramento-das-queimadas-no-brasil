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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d86ef73d-c593-31ac-b93a-fbfe841f5bb1 | -4.4523 | -44.804 | 2024-11-12 01:00:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5a23e9f0-7182-3375-ba3d-7aad5b6bfe34 | -17.6086 | -57.4276 | 2024-11-12 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 837aed5d-5ffe-3567-b213-5003ddd7a062 | -2.7737 | -50.3201 | 2024-11-12 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 228ac9d8-49cf-3a20-a8a6-69463537af32 | -2.9912 | -51.3563 | 2024-11-12 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c661ee61-2f7f-33de-be3b-40d59cb09a97 | -2.7588 | -49.3285 | 2024-11-12 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4774543f-8758-368c-9244-e003c3a0fda3 | -17.6477 | -57.4434 | 2024-11-12 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| fc828e13-0124-3e86-aace-4b3a8efb8f5a | -2.7587 | -49.3497 | 2024-11-12 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 9c2bddc5-fc2e-334f-a339-e0ba272ad695 | -3.0913 | -54.307 | 2024-11-12 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5f8190de-895f-35dd-b66c-20b926ac5ae9 | -3.1097 | -54.2865 | 2024-11-12 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| fd970c06-8688-3eda-b6d2-19fe11c73bf9 | -2.9913 | -51.3356 | 2024-11-12 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| ce67704e-5031-3b1a-ada1-2f7c7e3ab7f4 | -2.7921 | -50.3196 | 2024-11-12 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 081afaed-ccc6-3264-aadc-473f196a7077 | 1.048 | -60.5986 | 2024-11-12 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 386adbcb-7777-3419-aa08-637bc4b76d71 | -3.73792 | -50.19501 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c20807a7-057a-31e6-a835-1faf6b035261 | -3.28723 | -51.06114 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| ebbc421e-caf6-3b3c-84ee-db2bd2860514 | -3.22484 | -50.28627 | 2024-11-12 01:00:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b5287014-9524-3ac0-af9f-4e2a05acbc17 | -4.15179 | -50.79346 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a98af721-f51e-3364-b54e-da90b9d813c5 | -3.77491 | -50.79845 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 97db6ef1-d447-30c3-b294-19fd6c76605f | -3.2849 | -50.05576 | 2024-11-12 01:00:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 716be9a1-93da-32cd-8897-24c39d73b620 | -3.16853 | -48.36792 | 2024-11-12 01:00:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2ad98e1-640c-30e9-8428-384f3471629b | -3.0827 | -49.2042 | 2024-11-12 01:00:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a261444d-2ce0-3042-a54c-17a02f43102f | -3.5207 | -49.95924 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 12f6bd01-1e93-33bc-a2bc-90c84d50defc | -3.51185 | -49.96049 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d001d8c8-ccf9-3054-bba0-22214f36a900 | -3.29891 | -50.02678 | 2024-11-12 01:00:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1b76d07a-6a4a-36c0-a7d8-3d8961e23cc3 | -5.92403 | -42.97794 | 2024-11-12 01:00:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 26000921-6062-3821-80bb-e02799429860 | -3.85519 | -52.38547 | 2024-11-12 01:00:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8241502c-e5c4-3ac2-9a7f-5d7479af71f2 | -3.58404 | -50.9464 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fb2dda84-de4e-3936-80b5-5c39d16f0ffa | -3.69947 | -52.11012 | 2024-11-12 01:00:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4dbf6c05-a0db-39fd-98bb-04c352b8eabf | -3.52194 | -49.96807 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| edcb49f0-92a5-33ba-8b42-bdc5f36fd2d6 | -3.74553 | -50.18494 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| cf8cac57-3dee-3292-8e02-a865581fdc7c | -3.70725 | -52.11263 | 2024-11-12 01:00:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0549f42f-ef4a-359b-a948-ced2a5205465 | -4.08778 | -50.33355 | 2024-11-12 01:00:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bdfcbcc4-04db-3c44-826e-ca28c78c7d6c | -4.31161 | -50.81336 | 2024-11-12 01:00:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7b556caa-ccf2-3295-ab99-90b67a033d48 | -2.89943 | -48.30756 | 2024-11-12 01:00:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fd7f2a9d-f6dd-335d-8f15-b4e113ee58db | -2.65366 | -46.81372 | 2024-11-12 01:00:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 14f66fdf-e8de-3034-ab83-a8168f4a1a02 | -3.28367 | -50.04694 | 2024-11-12 01:00:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3a261da0-3dff-3311-bcca-e4ecbf048c9a | -3.70856 | -52.12228 | 2024-11-12 01:00:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad60700c-82ac-36c9-9d24-892d5adbc625 | -3.07368 | -49.20548 | 2024-11-12 01:00:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 131d6efe-a5f0-36b6-b144-9a2dc7e25ecc | -3.74676 | -50.19375 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d87d9978-ec5d-3f04-9492-f9410dce81d4 | -3.0049 | -49.1085 | 2024-11-12 01:00:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d9e24f50-cff9-3aa3-a439-70915ffb5177 | -3.70082 | -52.11976 | 2024-11-12 01:00:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 58cf0cb3-9b8a-36dd-9e9d-84a56f2c8a4d | -3.69254 | -50.93428 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ddd54c4c-8b6c-314a-b169-ec3e6e1db5f7 | -3.2584 | -48.75217 | 2024-11-12 01:00:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a4b5e581-2cdc-3f92-b718-74caefbe5425 | -4.14841 | -47.75265 | 2024-11-12 01:00:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 41ece45f-c069-3a96-9343-842826e24bdf | -3.1971 | -50.28122 | 2024-11-12 01:00:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b35bee51-41e1-30ec-ab95-d0c4a5acae3a | -3.85578 | -51.91021 | 2024-11-12 01:00:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ccb55f53-6b05-3f1b-90ac-9840d63c57a6 | -3.4599 | -49.20053 | 2024-11-12 01:00:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6c6d5a42-0852-3911-966f-dd4b178f8a79 | -4.08842 | -47.70397 | 2024-11-12 01:00:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 7ff7b0a8-9a34-3119-8036-b2226a913b29 | -3.35476 | -51.68598 | 2024-11-12 01:00:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d10f57e5-3aef-3490-8e72-8e2e232af597 | -4.08988 | -47.71439 | 2024-11-12 01:00:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| c9434943-8c47-3591-9eb6-8d7be5796159 | -3.25975 | -48.76163 | 2024-11-12 01:00:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a1ab57f6-8ae6-3ef0-bbe1-47570620da0b | -3.62164 | -50.61894 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 659ac5ff-8dcb-3d57-aada-e48f3dabf8aa | -3.07497 | -49.21465 | 2024-11-12 01:00:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 483167f6-cd3d-3ad7-bd24-97073d7c60a9 | -3.2462 | -50.31018 | 2024-11-12 01:00:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 89666aab-ae00-3e46-84a2-b80d56a82173 | -3.27657 | -51.05945 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1ee1db6b-fd66-3b03-ad88-ee38d9bf534f | -3.15718 | -49.73669 | 2024-11-12 01:00:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9b740b1a-18ab-3fdb-97ec-c0cf9c1da4f7 | -4.44501 | -44.81841 | 2024-11-12 01:00:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 9593b6ea-2cc6-3a44-bfb6-625649e00713 | -4.06636 | -43.95812 | 2024-11-12 01:00:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 5f16bccb-3095-3344-aa55-7d34a2b3a12b | -3.73669 | -50.1862 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a3a1ba63-c506-3ade-8567-76662f7c7d42 | -3.24743 | -50.31898 | 2024-11-12 01:00:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d74b5d9f-bbba-3d61-8e68-514bd38b4d3c | -2.53211 | -45.39983 | 2024-11-12 01:00:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 28.4 |
| e234d4ed-526c-3542-ada8-256fcb8247b4 | -3.748 | -51.93127 | 2024-11-12 01:00:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 83893379-b670-3f2f-97c8-03c078f4f461 | -3.70847 | -50.64536 | 2024-11-12 01:00:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 10e6e5f1-a692-3c25-8c86-fecca5af1050 | -3.26755 | -48.75086 | 2024-11-12 01:00:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 36e81277-db39-33c8-b2a5-3d7b2301e073 | -2.98435 | -51.3382 | 2024-11-12 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 8d321914-af13-316a-82fc-841c457bba49 | -1.86266 | -48.01014 | 2024-11-12 01:02:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2e110a28-4b33-33ce-978e-3de59a397ea8 | -2.76067 | -49.33974 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 849f3bed-3ca6-344b-a85e-16cd13ecb4e6 | -2.7594 | -49.3306 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 90bdbc63-177e-35ba-9567-1b212f3a20fa | -2.62847 | -48.07527 | 2024-11-12 01:02:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7ad41bf3-3662-3dc3-bc13-c165c3e11386 | -2.99329 | -51.33696 | 2024-11-12 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d86b26b9-f4ca-32eb-902f-a27ebfa5aa2a | -3.0938 | -51.07005 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 576e0059-9b79-33c3-988a-124e538f7211 | -3.10162 | -54.29186 | 2024-11-12 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fd208ec0-d1b6-3dd9-b3fb-ba479e028337 | -3.02691 | -50.97978 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ae94216d-411b-3316-9dae-c037901ceca8 | -2.79309 | -51.75405 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| b2d96fc3-8fb9-353f-aaf7-25fd5b8667a7 | -2.78406 | -51.75532 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| ab5f2dcc-f74f-336d-bf51-f827fd778107 | -2.77626 | -50.30817 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 5141de35-6a0d-3f39-a03a-dc438452ccca | -2.32008 | -49.08792 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 52aad407-3221-3c1e-860f-c6d195a7ff1c | -2.98559 | -51.34717 | 2024-11-12 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a020b522-17bd-3d77-9660-d46fb6078e55 | -3.04368 | -49.71329 | 2024-11-12 01:02:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b954e04b-6c0c-3ea3-aa2e-21739a42c771 | -2.78357 | -48.587 | 2024-11-12 01:02:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 46526a07-8f6b-3b3e-a4a5-a0a0e95db0b2 | -2.77055 | -49.3413 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d7515bff-d053-36b9-bd0a-e497714eb4db | -3.02568 | -50.97091 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6157035c-26ae-3c32-9ae4-5288cc60b7ab | -2.39417 | -48.50751 | 2024-11-12 01:02:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 341fe080-7140-3950-b45b-071001406318 | -2.78219 | -48.57732 | 2024-11-12 01:02:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 25c0e053-a26d-35c6-9572-a71610e35f0d | -2.90501 | -49.25103 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d12122fe-3fe2-37de-a430-4bcf726d3fa9 | -1.43835 | -47.47544 | 2024-11-12 01:02:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 64c0c2c5-775a-3323-95a4-8e4d7005c57b | -3.11385 | -54.30317 | 2024-11-12 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 297fe1a4-7c4b-3206-9697-3f37c59b4bc2 | -2.79182 | -51.74485 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8773d484-ce9e-33e1-a79e-529c783bd048 | -2.75295 | -49.35015 | 2024-11-12 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| e665e41f-71fd-3375-83c3-6f29807752d6 | -2.91909 | -49.81585 | 2024-11-12 01:02:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 574d740f-7396-3137-be39-7619f23e4e52 | -2.37693 | -48.52004 | 2024-11-12 01:02:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e3c7472c-35b0-3471-b229-3d959d0599a3 | -3.10335 | -54.30466 | 2024-11-12 01:02:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 00ab22af-5df7-3e14-8068-f4df252e2c4d | -1.6084 | -47.52069 | 2024-11-12 01:02:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 63f5d41b-1604-3017-8df2-44a23cfabf78 | -2.55101 | -47.53071 | 2024-11-12 01:02:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 022f15d0-6c5b-3bd9-93a9-1be09c40e7e5 | -3.01831 | -50.25583 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b9d584b0-75a3-3938-ae3d-899d84cc4cc2 | -2.3701 | -48.51687 | 2024-11-12 01:02:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| cd4cdf0b-952b-3d4f-9477-93b93705166a | -2.39413 | -47.72227 | 2024-11-12 01:02:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 33b60bab-a48c-36e5-b342-82fd5b58408e | -2.99453 | -51.34594 | 2024-11-12 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| a2087814-5be9-3c4d-8049-ddef607d832e | -2.98683 | -51.35617 | 2024-11-12 01:02:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 008bc7bb-3814-3048-b0e3-ccb26a557e05 | -2.78279 | -51.74612 | 2024-11-12 01:02:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 89a57db1-6e56-3294-90ea-795017ca0c79 | -2.89716 | -49.52085 | 2024-11-12 01:02:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README5.md)

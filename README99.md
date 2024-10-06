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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aad264e3-eaf5-38c5-99e3-9d1992b05e39 | -3.14381 | -50.23145 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5fe3b326-d5fb-36ad-a665-1ab5fd7939ef | -3.14005 | -50.2264 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65578a42-7909-3ae5-8d7f-21e31d7f5248 | -5.01499 | -49.77197 | 2024-10-06 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b706c54d-7b3a-3727-899e-26d7761371b8 | -5.01424 | -49.77697 | 2024-10-06 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 63b2790d-efd9-3439-90e7-d42180a02bc6 | -5.01238 | -49.77384 | 2024-10-06 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9762a222-997d-3abf-b161-5b28b7e6eeec | -4.9479 | -49.63844 | 2024-10-06 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5dfd1974-c107-3f4b-9465-df261e7d75f0 | -4.87065 | -50.76839 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de27fb06-189e-3800-be69-b833f9ef8126 | -4.86566 | -50.77208 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c484583e-6fea-3361-a661-c243c0badb5c | -5.01778 | -49.76956 | 2024-10-06 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b383e96f-6bf9-3498-be31-0a77c90b5b3d | -5.01707 | -49.77455 | 2024-10-06 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96f71aa1-1759-3610-883a-02ce214c5d11 | -5.01309 | -49.76883 | 2024-10-06 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fcaf083d-d6fd-308e-89ce-be4fe0c4681f | -4.94716 | -49.64358 | 2024-10-06 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 30e80dd2-02f3-3f5f-8d4f-99e7ad6e1c55 | -4.86947 | -50.76954 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d264bbda-71fc-3a75-b316-072685e2cec0 | -4.86627 | -50.76777 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cef82d3-74a0-328b-8b28-121700f426a0 | -4.86445 | -50.77323 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2606f8cd-f2b9-3f61-a235-bc14df0eca7e | -4.66468 | -49.52905 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0c37383-4844-3e63-a1be-f77afff614b3 | -4.65994 | -49.5283 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00f86758-1559-3570-a53d-025d95cfcfc9 | -4.45367 | -49.7898 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ace52519-c6ae-3a04-b58c-9999679cba19 | -4.37699 | -50.81313 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99da2fcc-1f02-3911-bbb6-864447da2c65 | -4.37639 | -50.81721 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9aad9f1-7583-3597-b9f4-80b5610c8924 | -4.37268 | -50.81242 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d875ebc-472f-3f1d-adce-71ed3f756457 | -3.97979 | -50.54601 | 2024-10-06 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e208bd01-2d51-3a18-8a99-fa5a68f68062 | -3.92676 | -49.67149 | 2024-10-06 05:10:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8938b867-fe10-39c5-9c75-a893e20f19f9 | -3.92599 | -49.6766 | 2024-10-06 05:10:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 438d2b4e-419f-3825-8b2d-32eb59e6b98f | -3.92522 | -49.68174 | 2024-10-06 05:10:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2e12808a-fcda-31bd-bd94-915cce0c29cf | -3.79187 | -49.46778 | 2024-10-06 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 535f91c4-b40b-3b8a-aa0f-3b988f99a670 | -3.78716 | -49.46707 | 2024-10-06 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e2414eb3-8645-35b8-ba64-6b3605c9e2a3 | -3.59296 | -50.57801 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb8eb911-50c9-398a-9a19-46aaef646ec1 | -3.56889 | -50.54957 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61889194-0109-3dbb-861d-9052f0439eda | -3.56875 | -50.57979 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39e96b57-883b-3734-bb33-f02271362cb5 | -3.56454 | -50.5489 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b531cc5-ad98-325f-ba2e-c934c695a69c | -3.68586 | -50.25122 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75a374d1-43e3-3c48-b93b-900f298b4af2 | -3.58306 | -50.39643 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbbf34f0-f8a0-389b-9814-cb512eeb5c70 | -3.57867 | -50.39577 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ee7d636-0cd1-35b1-943d-37985a2684ab | -3.56494 | -50.36728 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ded00fdf-29ed-3604-ae2c-18dc73d1f64e | -3.56054 | -50.36655 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3df5dcf-42c9-3ce3-bb8b-47eee3eff464 | -3.55989 | -50.37095 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a342ed9-7874-370a-a53e-9b937f40a178 | -5.34058 | -49.52854 | 2024-10-06 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be9566c8-f369-39d7-8af8-156100e3abd0 | 0.35906 | -50.71888 | 2024-10-06 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4285aef7-2a5d-359e-a8a7-a3ebd6a39e42 | -2.13835 | -50.99216 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7eff6820-29eb-30bb-91d5-7ec322a94ca4 | -2.13422 | -50.99149 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59ee16c6-eaf5-3aa2-bdac-6fd2878b4539 | -1.83203 | -50.98078 | 2024-10-06 05:10:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b0bf72c-390e-3157-b024-6576a89b263a | -3.09503 | -51.22511 | 2024-10-06 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b294169-c943-3cb8-96a1-5d8f3658a34e | -3.09448 | -51.22876 | 2024-10-06 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc74758f-b35c-3a91-806e-026bdc6f2c73 | -3.04374 | -50.98657 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcbc5d83-ed50-3cb4-b0bb-fa063ed16f86 | -2.88045 | -51.67314 | 2024-10-06 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc73a02f-88b3-31e9-9f0f-b2865eec75d9 | -3.66378 | -50.95187 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c69519a6-1653-3593-8ebc-b37e37f8a82b | -3.51584 | -50.84214 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d700496c-c018-3fef-8333-9331d5413d0b | -3.51523 | -50.84616 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79d0ba63-72c3-316e-9aca-f63508261f1f | -3.51159 | -50.84143 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5755999-3947-3c8d-a47e-d82f7804b91c | -3.49079 | -50.80572 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3115385-cf07-33da-90bc-b9edc3a69566 | -3.48653 | -50.80503 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 43de04da-bd07-3afa-b750-c4f4d0653f4a | -3.44727 | -50.66799 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27eb6c4e-179f-3cdd-955d-fc60cf72a1c7 | -3.44421 | -50.65912 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933b8791-6441-3a63-88c3-ff6f9ba780f5 | -3.44359 | -50.66323 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8459a7c8-c1ae-3a3c-bbff-fcd3699f0b60 | -3.30485 | -50.66085 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 504f2841-3046-3528-b4e8-1d7882ee9959 | -3.29459 | -50.75845 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91b85a4b-88f4-38a3-9178-80115f45e7cb | -3.29092 | -50.7538 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60a07994-cf88-3b9c-9db3-997671022636 | -3.29032 | -50.75779 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 804c479f-8a80-3207-b120-e11efadd36b0 | -3.23563 | -50.83525 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02033dea-e584-3403-b1ad-39a7b57c3e09 | -3.23538 | -50.83477 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04922b1c-e568-3704-a0d7-6cd39d6934ee | -3.23502 | -50.83918 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5590982-2ec5-3547-bdc7-0bbeb7e46dbe | -3.23481 | -50.8387 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebdaaa09-c9ff-3a93-afa0-2f58fda63b5d | -3.23441 | -50.84309 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 15c89cca-67e7-337c-b929-8145d6830e25 | -3.23423 | -50.84263 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25a97bcd-0a87-34c2-b612-b50cfb9eda2e | -3.23365 | -50.84656 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ad081d3-be6a-328e-818f-341d6955bbc9 | -3.23138 | -50.83463 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ca5054b-af87-317f-8052-ded6b6be2841 | -3.23114 | -50.83414 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02963899-572c-3df9-bbbd-91e85f949297 | -3.23077 | -50.83858 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97a6acfa-9290-3282-93bf-76e113dad4a9 | -3.23056 | -50.83811 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe093d30-5f5a-3913-82ec-e26eb9d24a64 | -3.23017 | -50.84251 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5b03560f-2f7d-3920-a317-96e03fea019a | -3.22998 | -50.84204 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5d0c58cb-dc29-3942-841a-b5086083cff4 | -3.22956 | -50.84643 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c9936d1-5950-3f26-8f5c-c57ee9dc3ee0 | -3.2294 | -50.84597 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3b2cef84-f461-3dc8-ad24-a3eb25445469 | -3.22714 | -50.834 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6af2dda2-29ce-35be-9cd1-81507e6eddeb | -3.2269 | -50.8335 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91cce99f-1544-3d94-9a6e-d62d87606cc7 | -3.22653 | -50.83797 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb82fe85-f961-3780-9964-3c2e7287b326 | -3.22631 | -50.83749 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 314301a5-9084-3d40-b5b4-fcbdbfecc483 | -3.20425 | -51.16135 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea063555-790f-3180-9562-60cdbcf740a7 | -3.2037 | -51.16509 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4832ea7-ba58-3120-b3e7-9e7198116e3f | -4.67126 | -50.98732 | 2024-10-06 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb7d2d56-9fcc-33a4-acb6-a7b9f3a999b1 | -4.67066 | -50.99133 | 2024-10-06 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 576040d9-60bd-3b3d-b59a-a886bc1b6cc8 | -4.66697 | -50.98665 | 2024-10-06 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4883b53e-5bd2-3b76-8633-f108df45ca11 | -4.66638 | -50.99068 | 2024-10-06 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e28d3856-fbdf-3c21-9f9a-ffbbf3d0321d | -4.10501 | -51.09919 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48b8ac82-4415-31fc-b740-a4897e9b699a | -4.10445 | -51.10297 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a9c5373-38e4-3191-aa93-0872ba89bef9 | -4.1008 | -51.09847 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54e9fc90-d959-366b-8775-14af2517f769 | -4.10023 | -51.10229 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b4e7dad-d40e-326c-88bd-b4ab5cb40d89 | -4.05512 | -51.11605 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95cc2248-2be2-3cd3-9053-b64837630f6d | -4.0551 | -51.11337 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06218a1e-f6ba-31f0-9ffb-1004c07a419b | -4.05447 | -51.11745 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e1d9514-e4f3-3aa4-93d7-7b41364ed84c | -3.91419 | -51.24198 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 911d5ac8-6894-3d98-bd46-43cd081e1b3d | -3.9106 | -51.23754 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5493cc76-6a9b-3b31-9370-e1f4358af30d | -3.91002 | -51.24133 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45f1801a-020d-3af5-9ffd-87f33560786e | -3.90944 | -51.24512 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d188fa4-1eef-379f-94e0-9b3e30538205 | -6.28494 | -52.43734 | 2024-10-06 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f663daa1-b63e-3d92-aafd-170970b5909e | -5.60399 | -51.55304 | 2024-10-06 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b195b6-30ba-33b9-80ba-cb4a6bcb8f33 | -3.04225 | -53.03877 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5f759ea-8116-3f66-b4bb-e51d9c13cd4c | -3.04159 | -53.04311 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38f68e36-65f0-303e-94f6-d82d5bfc18ca | -3.03857 | -53.03819 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README100.md)

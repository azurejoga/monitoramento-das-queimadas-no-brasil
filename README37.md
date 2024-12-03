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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f32a50e8-e962-3c61-b673-57f73a81f85c | -4.44242 | -45.36593 | 2024-12-03 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d76b56b3-82b4-3be1-947c-20a101bd679e | -3.9281 | -47.98354 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de234b1e-2059-356b-8f7c-cbdcc2fc7e16 | -4.74766 | -45.11524 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39cfbbb6-2e1d-3014-8347-733460b541d8 | -3.95872 | -47.66138 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a252add1-6f49-302c-8fc8-86e60718460a | -2.56608 | -46.34234 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfd8ddbd-f5e1-3853-8243-3811942c51ae | -2.56958 | -46.40649 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2655a88b-9828-333c-9193-beb1fd15f43e | -4.04802 | -48.0845 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c29e0c36-ab3f-3f3b-aab0-4dce20e45fc0 | -4.26638 | -50.85068 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37caead4-2629-3aa4-92af-bfdc89d5e5e8 | -3.23679 | -46.41864 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd6a986-cac9-3535-a407-cf3dd1803377 | -3.75479 | -48.15305 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db707761-3862-31aa-b57d-bdfe6513025d | -3.91828 | -46.53525 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00eee7bc-c79d-3bcf-aacc-5809464d2fc2 | -3.90211 | -46.66051 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b89d46e-be48-36b0-8826-19f92bdd826e | -2.59736 | -46.27282 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3909897c-1ea8-34a6-94be-19ec3600cc22 | -2.6759 | -46.11831 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93675173-04b3-38a0-b6ea-0df271cab815 | -4.11134 | -48.48022 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b21a63d-00a4-3706-91e5-0d2f5512da84 | -4.07492 | -46.68388 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d03f96f5-4bab-37e4-a62e-2cb90db3d67b | -3.93644 | -46.89559 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 486e6797-1128-370b-98b8-321220d0ce3c | -3.01732 | -54.03407 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88845b88-763a-3812-a380-13c6865d991c | -5.82386 | -46.35535 | 2024-12-03 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98bc8672-e70d-34ba-ae2f-f7c74c9b6bb2 | -4.03409 | -48.88062 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77b8548a-c7be-33e4-bfa9-e2a4926c350c | -2.81986 | -53.05075 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 012d526e-11cd-3008-95c9-bbe497230b7b | -3.3008 | -53.66277 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 8471c9b8-e7a2-35a4-9893-61ea6e0cd6fb | -1.73815 | -52.6482 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f24a83e-5e4c-3f35-b081-020f0147f802 | -4.04923 | -48.27152 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11292917-2b3a-31c5-9571-53ff2abb409d | -1.73766 | -52.77539 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebac1e94-ff45-38ef-a1d5-1d8298e6cb9f | -3.40666 | -50.25489 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae65e3fe-63f2-3aac-852d-56bb571e7989 | -4.2534 | -46.36638 | 2024-12-03 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4ecc3c9-0da2-3e08-a6a8-2ee0d037bc23 | -4.34523 | -43.74702 | 2024-12-03 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 343e792f-ece5-3227-9871-052de344b627 | -5.07891 | -44.03605 | 2024-12-03 04:29:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45ed7257-ead5-3ea5-91d6-865d64d7d5e6 | -1.73878 | -52.64416 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83198e3b-892d-3f90-8956-2666fb62570a | -2.68288 | -46.61501 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04699b94-8710-3863-a0cd-441e3df512c5 | -3.33744 | -51.20439 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78cb9286-4b89-3684-a591-ecef03cba34d | -2.56069 | -46.57098 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7ff6ecf-817d-3064-bfef-6fc89d49d71d | -2.73048 | -46.24765 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b97082ba-eb42-30d1-8ed6-6de790f98f09 | -3.69991 | -51.82174 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f4820b34-9e5d-3d2b-a8ac-a1aa63250a4e | -5.17235 | -44.80369 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50b1ce7b-5f58-3aca-a575-ad854cae2aa1 | -4.29474 | -48.22002 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ccd1f1c-0287-3cd4-a33b-0b8f17e7ff2f | -1.73034 | -52.61387 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6819cda8-2adc-3778-b775-aa98ad81a407 | -2.29915 | -47.49966 | 2024-12-03 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73d35e59-b796-3de8-9a32-1e07653244ca | -5.8124 | -46.47354 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f2573453-189e-3a5f-b955-cd5ea5ec7a75 | -2.52013 | -47.06835 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa38e133-153f-38b7-a548-78a6dc595bbb | -1.4395 | -53.39404 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aae77f10-947d-3865-8071-780cfef10372 | -3.85581 | -46.52169 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1211c66-488c-38bc-aa6d-cf3eacc99eb4 | -2.69809 | -46.12886 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f17b1c0f-663d-3ab3-b59b-71fa08312d74 | -5.69165 | -46.59595 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c5ffc57-8585-33f5-b36c-ec333f99effe | -2.29005 | -46.36972 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db383f91-2407-330c-9a2e-8f862306aedc | -2.64567 | -46.11687 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bdd22c7-9cea-3239-995e-39ff753620f0 | -3.20289 | -54.274 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 562e97a9-339b-393e-b95e-16441bfd9cdc | -3.80297 | -46.94492 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c52d44f3-3821-3061-be48-fd1d7c4c18eb | -2.97744 | -53.87967 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8a2cf2f-7d5d-386b-ad8d-04cb51cc1f38 | -5.21876 | -44.92353 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa0dff8a-e00b-3348-afef-c6d1959e6b4d | -2.47061 | -46.53929 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 017e9d60-c0c9-37ab-a80d-dfe6f06a877b | -2.65564 | -46.11843 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55794760-2f93-307f-ade3-272ed3e99bb9 | -2.47728 | -46.56147 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26576542-db36-3b9e-893c-8ccf73e310de | -1.6684 | -52.40125 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0344b67b-6786-3190-8a9c-5035a0ceaba0 | -5.8085 | -46.47657 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e2588811-6006-3eb6-a9d6-cfb07b74f6c8 | -3.3448 | -46.05323 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3a6780e-b0ff-3e7a-9135-237a86f4459e | -6.02629 | -46.25028 | 2024-12-03 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c24c8f70-61c0-3651-9220-b1d60a2e087a | -4.03643 | -48.26588 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fb59e79-2d98-3c47-a298-2bce906e7bb5 | -2.46953 | -46.54617 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7cca077-cf71-30e9-bcc2-482429dedc92 | -3.34146 | -46.05274 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 86a9358c-34b7-3d47-8a86-6a49d8196f49 | -4.73983 | -45.70823 | 2024-12-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39302102-5949-3aec-9661-dc3403a7b7d6 | -4.13013 | -45.82546 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e52058d0-ef69-3b09-8bcf-0bdd99a24456 | -4.30919 | -48.21512 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4047611c-b22b-368b-81c1-a967f2cab37c | -2.6628 | -46.09458 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b641cf19-5e05-319b-bebd-234e888b01e8 | -4.07248 | -47.09005 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84c29b71-e184-3682-a185-8a3b37d7489a | -3.40258 | -52.87546 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c30e9038-80e5-3c38-b7da-63fb18772ab4 | -4.18485 | -51.18977 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2858b3fd-902e-38b2-a68c-346306c21ed2 | -4.09463 | -46.94896 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ef7e3cd-9405-3ef2-b13a-0ae6bfc3cee3 | -2.89062 | -54.15781 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e9b40a3-36f3-341e-a3b3-dd0f0d6d89ee | -3.34609 | -52.65977 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d37e0c9-9c45-342e-87d1-03820145d514 | -3.35029 | -52.66039 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68dcd9e9-f7f5-35e3-96c2-6f600ecaca31 | -3.43119 | -53.89322 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a840f536-cb14-32f8-b49c-27db38441f54 | -2.21963 | -51.78368 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| feb2bbb8-d3ec-32d3-8d3c-32ba42c36310 | -2.5685 | -46.41339 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f7f6244-0e71-31ed-a1eb-660126a3ab4c | -2.67626 | -46.61399 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 074fa930-fa8c-3df2-a03a-853ab5731c02 | -3.29552 | -53.68203 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3bf0492-aa21-35ef-82c5-c5bc9fd981bc | -3.13693 | -45.99269 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61d96fc0-c40b-3b3a-b68c-84e5541bea32 | -2.35351 | -45.70585 | 2024-12-03 04:29:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea1f18a3-85dc-3e30-985c-e339e637cfac | -3.75367 | -48.16005 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 746272b9-b90c-37c0-ad3f-d0ae858939b3 | -3.34356 | -51.21504 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4732ef4-1ed8-30f7-83d3-7d987efd2a80 | -3.26889 | -46.92832 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f83f75d-0e20-3c57-b92d-0719f40cd351 | -2.17847 | -55.81687 | 2024-12-03 04:29:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a04d2cc-869e-3db2-b0ff-e0c0d36a152c | -4.04589 | -48.27098 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 317e16e0-2dd5-3474-bc28-5f70c4c9811f | -2.64095 | -46.25508 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea6baab8-dad3-333c-81d2-98b2363f6afc | -1.14057 | -54.15527 | 2024-12-03 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d6b4baa-5a37-3c7c-ab3a-84a94d12dedc | -2.69884 | -52.91165 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ac12b28-8fcd-37fd-b087-0caadcf8affe | -4.0315 | -46.93872 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9a6a239-4d48-393c-bf3b-36c1851bd681 | -4.31146 | -48.09369 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f11baac7-e05a-35c6-9e04-43d4c8e2b393 | -5.8057 | -46.47249 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74914b5d-0b8e-3d2f-9e13-77cdd6df2437 | -5.39525 | -45.95208 | 2024-12-03 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c55d4e7-2d2c-3070-a405-449ceaeede03 | -1.90305 | -52.89752 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 849be414-25ca-337c-a914-74bfea10ef66 | -3.36065 | -54.06398 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fa04fb4-5b31-3907-a29a-62343fbac589 | -3.30007 | -53.66714 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fdf31772-e1e1-3763-a21c-f71475a61a6e | -3.11423 | -45.98891 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d6cea1b-85b8-3e13-8b3d-260f4c56d9f2 | -3.89844 | -53.43666 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77690a43-80fd-3d66-b66e-7b5adadf4873 | -6.44994 | -49.91141 | 2024-12-03 04:29:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a029dcbf-453a-378d-9dee-c8f3f78bdc61 | -4.14875 | -48.24353 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04b7dfcd-2137-3e7f-86ad-210672a69e7c | -2.59552 | -46.00206 | 2024-12-03 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff653297-f0fd-3ddd-822f-75dc1ab4160e | -3.33442 | -53.3262 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README38.md)

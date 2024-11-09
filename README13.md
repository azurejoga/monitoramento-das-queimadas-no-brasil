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
| b12d8136-e953-30ca-8044-c9ae94e5f67f | -4.2486 | -47.5729 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| c724cda1-4779-3451-a2f0-651e6183edc0 | -3.9668 | -48.1932 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 155.6 |
| afc287b9-f53e-3d5c-96d3-e8dab354c777 | -3.8277 | -46.4944 | 2024-11-09 01:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d51f62d5-27c2-3ceb-ab6d-227e746a4b3a | -3.9483 | -48.1724 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4b0a475a-2db4-341c-92f4-cf8bdd589448 | -2.2295 | -53.7631 | 2024-11-09 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| f2208fa8-0b6e-332c-a214-5239f31903d2 | -2.2479 | -53.7627 | 2024-11-09 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 265ca8a1-e238-3c1d-bf52-797d7f7592ce | -4.2033 | -45.8538 | 2024-11-09 01:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 5bf831d9-994a-3ce5-95a6-836c82186500 | -3.619 | -47.3388 | 2024-11-09 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 3c207270-ca8b-38c8-ba34-7cad319ff638 | -3.5819 | -47.3403 | 2024-11-09 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 528.6 |
| 6154e94d-068d-3210-8688-a61fc6f106b9 | -3.151 | -52.9934 | 2024-11-09 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 1cf237c1-eaa2-39a2-8ced-d2c7a24ef51e | -3.1327 | -52.9736 | 2024-11-09 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 177.3 |
| 741a1119-caf3-3cdf-b978-15bc7f4e99ea | -2.2479 | -53.7829 | 2024-11-09 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 0e2fcbba-b3ae-3098-ad86-da9ee6b8137b | -1.5078 | -47.1813 | 2024-11-09 01:30:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 0925c864-3a2a-3222-93f7-9f43ee961426 | -3.5818 | -47.3621 | 2024-11-09 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 466.2 |
| 2e16bb79-6e4d-3d3b-b0f6-9cb269c07b14 | -1.5078 | -47.1595 | 2024-11-09 01:30:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b3e7dea6-a591-34d3-8c06-67a3ed7bff3c | -4.2058 | -48.5491 | 2024-11-09 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| a1a691a4-aae4-3573-a783-6956c32da923 | -3.1512 | -52.9527 | 2024-11-09 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 349465af-ce40-32e0-82eb-5e0498c62572 | -3.1326 | -52.9939 | 2024-11-09 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3931f8ce-552a-34b3-988c-7f14400f397c | -3.1511 | -52.9731 | 2024-11-09 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 439.2 |
| c209bfe5-306e-3f0c-bfa3-071b781d7450 | -4.2487 | -47.5511 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0e3cac39-7b2d-3f0a-a0d1-719cc6f52144 | -3.6189 | -47.3606 | 2024-11-09 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| ce394ee9-b6be-3577-9dfe-f0e26de470ff | -1.5163 | -52.1901 | 2024-11-09 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f5893d53-7d14-31a5-8b86-7a3108ab511a | -3.9854 | -48.1708 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| db642ae6-c727-33a3-ab5d-2c47707aab47 | -23.9095 | -54.0606 | 2024-11-09 01:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| 24bea4dc-f94f-33aa-8d9a-44906397b798 | -4.4417 | -43.6348 | 2024-11-09 01:30:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 726d4f49-fd47-3ca8-9e3a-323e4aab5517 | -2.6764 | -51.8189 | 2024-11-09 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 42587e87-6b19-3160-a4a6-062984afa244 | -5.4699 | -43.6603 | 2024-11-09 01:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 92470f98-0c24-332b-bafb-a0cef33bb613 | -4.2059 | -48.5275 | 2024-11-09 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 36e2698a-27e6-3b7f-9287-41920135702e | -4.2484 | -47.5947 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 297b12e0-5dcc-35eb-ab71-2fe9cdf1b632 | -3.9669 | -48.1716 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 229.2 |
| fa82adb3-44af-35d4-a6ed-8a388385c6d1 | -3.1328 | -52.9532 | 2024-11-09 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5fd90ab5-9ca6-3617-8dc7-f95c714825e0 | -4.23 | -47.5738 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ddf91812-6782-3d18-bb62-3552c1f3c043 | -3.967 | -48.15 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c435428f-4770-3b12-923b-748b421df952 | -3.1641 | -54.4854 | 2024-11-09 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0e57a103-104d-3e5f-9e11-ce780924d57a | -4.4415 | -43.658 | 2024-11-09 01:30:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e09b13bb-d09c-377c-aa60-a91d623fe611 | -3.6003 | -47.3614 | 2024-11-09 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 600.1 |
| d07c4e3b-6a3c-3b62-ad95-712872a2dac6 | -5.4701 | -43.6371 | 2024-11-09 01:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| bce0f3cd-133f-3034-bdc7-72d4894dc415 | -2.4104 | -48.5265 | 2024-11-09 01:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4f5988df-cf0e-39d8-8fae-842974124bef | -3.735 | -54.2292 | 2024-11-09 01:30:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9406257b-925b-386b-a581-8ea6553ec3a1 | -3.6004 | -47.3395 | 2024-11-09 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 759.6 |
| 36327263-bcc5-3523-a057-dcb636810e00 | -4.2032 | -45.8762 | 2024-11-09 01:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| e0c9814c-1a9f-3787-bfb4-000f100c5f9f | -3.5649 | -43.5654 | 2024-11-09 01:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| be68352d-66b3-30fa-984c-6c69e9789622 | -2.2295 | -53.7832 | 2024-11-09 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| e324b5fd-f256-3391-b79a-fd2b4cb84f7f | -1.5164 | -52.1696 | 2024-11-09 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| cbecdab0-b913-3b31-9f52-eef0208e16e3 | -3.5462 | -43.5663 | 2024-11-09 01:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| fb77f315-e4ac-3a2a-b470-97b0bd410fd4 | -3.6003 | -47.3614 | 2024-11-09 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 477.8 |
| affe2b34-724a-34da-bd94-da3d9d5f346d | -3.9854 | -48.1708 | 2024-11-09 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2c2549f6-cfe5-39e9-a0e3-e86536fbc15f | -3.619 | -47.3388 | 2024-11-09 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 4f9fc91a-e278-3bbb-b13b-a524435acca0 | -1.5164 | -52.1696 | 2024-11-09 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 3a0b56d7-985a-396b-aaa3-ad29b03f65e6 | -2.2295 | -53.7631 | 2024-11-09 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 8c4b759f-5366-3289-964a-4f5e5912863b | -4.0153 | -46.1752 | 2024-11-09 01:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 6af5c2c1-b4fc-35f3-8a2c-d92e4b51c403 | -3.5818 | -47.3621 | 2024-11-09 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 367.7 |
| 573158b1-64e5-3eed-a4a1-0baae065b333 | -3.1511 | -52.9731 | 2024-11-09 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 384.4 |
| 2d985b38-9d87-39a8-9d6a-aafaaeb0ba62 | -1.5078 | -47.1813 | 2024-11-09 01:40:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b7aa1242-9d87-3860-96cd-52d078a3a134 | -3.967 | -48.15 | 2024-11-09 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 1ca79692-f450-3471-ba81-a6b2495f3649 | -4.2487 | -47.5511 | 2024-11-09 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8da7af47-075e-3e7a-87dc-19ea8e6afdae | -3.735 | -54.2292 | 2024-11-09 01:40:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c4ce4850-415f-3bd5-b1c6-6ab64891b481 | -2.2479 | -53.7627 | 2024-11-09 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 04581f31-1163-36e3-8dae-77310ad63e0f | -5.4701 | -43.6371 | 2024-11-09 01:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 9bb9869d-6c8b-36f5-8d9c-05856ff20d81 | -2.6764 | -51.8189 | 2024-11-09 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 328284fe-f1b1-3727-b325-1df876d871c4 | -4.2058 | -48.5491 | 2024-11-09 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 51496180-5523-366c-9f24-1727f79623f6 | -3.151 | -52.9934 | 2024-11-09 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 6d943595-4548-379f-86b5-9ccd4008d68c | -3.5649 | -43.5654 | 2024-11-09 01:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 697565f4-518e-375c-8641-7038aeea11ab | -3.1512 | -52.9527 | 2024-11-09 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 72a8d5d4-c3f6-3bc4-8452-5a8937536c18 | -4.2033 | -45.8538 | 2024-11-09 01:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 8c2709d9-c6ad-3a3f-9bf5-d133929b6fb6 | -4.0339 | -46.1743 | 2024-11-09 01:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 91.0 |
| a678d77a-c5b5-3d60-9c37-2e802d6c5c91 | -4.0152 | -46.1974 | 2024-11-09 01:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 35c39c9b-48b1-33fd-9538-283bc893ddb7 | -3.6004 | -47.3395 | 2024-11-09 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 759.4 |
| 5a96d876-0287-34ca-b830-700114b8cd75 | -3.9483 | -48.1724 | 2024-11-09 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 79c8cb65-86a2-3dfa-8a75-7983c1df0927 | -1.5163 | -52.1901 | 2024-11-09 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ba0218fe-7d39-3749-a2ba-3cb1ce712981 | -3.1327 | -52.9736 | 2024-11-09 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 144.8 |
| b3a2f14d-52b8-30dc-98b3-1a159839ac6b | -4.2484 | -47.5947 | 2024-11-09 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| acab9340-4e62-35d9-b937-4a0fc530622b | -4.2486 | -47.5729 | 2024-11-09 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 9c5c406e-ac44-3881-85de-99915885bba1 | -2.2479 | -53.7829 | 2024-11-09 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 48324080-280b-3b5f-87db-99053e9725d8 | -3.9668 | -48.1932 | 2024-11-09 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| fcdc986f-57e9-3e0a-ae6f-3ce509bff9cb | -4.2671 | -47.572 | 2024-11-09 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a524dd60-7449-3f09-80de-759b68c808df | -4.0338 | -46.1965 | 2024-11-09 01:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 9e514b7e-9ed2-3ba5-8908-aff8c0aaab7c | -5.4699 | -43.6603 | 2024-11-09 01:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 4cfe99ae-e617-39bd-beda-5be6da35b801 | -4.2032 | -45.8762 | 2024-11-09 01:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 3216ac3b-eb8a-357b-8cb4-4008fef9b0f7 | -3.1326 | -52.9939 | 2024-11-09 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 289ccee8-75fc-31b7-8497-b42bed8f45e0 | -2.2295 | -53.7832 | 2024-11-09 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 58bbdd9f-53fd-3636-a35a-0923a17c1e95 | -2.4104 | -48.5265 | 2024-11-09 01:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 79e68b45-d9b8-3717-b579-950adaac1669 | -3.9669 | -48.1716 | 2024-11-09 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 238.3 |
| 82cf8efa-258d-3d2c-8f14-76d37fc70bd9 | -23.9095 | -54.0606 | 2024-11-09 01:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| c367c83d-8c5e-33b6-a58c-862146981949 | -3.6189 | -47.3606 | 2024-11-09 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 5d707231-5d0b-3f1c-8517-1817c850cf27 | -3.5819 | -47.3403 | 2024-11-09 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 521.9 |
| 84720794-bced-3232-9760-eec6527efa57 | -2.3605 | -46.8557 | 2024-11-09 01:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| bd6664b4-8e29-3417-a301-5f49c38a26fa | -3.151 | -52.9934 | 2024-11-09 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 099b71d1-0752-33cb-94cf-b27716946d51 | -4.2486 | -47.5729 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 21f94148-95bc-3f50-a3e7-8f4f4ee0ddf7 | -3.735 | -54.2292 | 2024-11-09 01:50:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 7f6b5070-b748-32dc-968a-9ac6d4ce9962 | -5.4699 | -43.6603 | 2024-11-09 01:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 03dce56c-e0fa-3f66-be89-8dc8b9149b2b | -2.4104 | -48.5265 | 2024-11-09 01:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 01ea2ec3-fbca-3bfc-ae9a-46a93d45da7d | -2.2479 | -53.7829 | 2024-11-09 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 87749cda-fc1b-367c-aa93-e0b5b3b0535e | -4.0338 | -46.1965 | 2024-11-09 01:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2b4501b4-9c9a-3997-abd2-65689fd3a958 | -4.2487 | -47.5511 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 6fb129f7-5df8-3771-aec2-6b161c25ea8d | -3.9854 | -48.1708 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 640779ef-9eb9-325d-bc72-961e27b9cbd7 | -2.3605 | -46.8557 | 2024-11-09 01:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0b79d4c9-5e06-370c-919f-01d8c535070b | -1.5164 | -52.1696 | 2024-11-09 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 888eb89a-1d50-393d-890c-8a181538fe2e | -3.9853 | -48.1924 | 2024-11-09 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 61882ca3-1e77-32e4-95df-d86dd4ad3cb5 | -3.1327 | -52.9736 | 2024-11-09 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |


[Clique aqui para ver as próximas entradas](README14.md)

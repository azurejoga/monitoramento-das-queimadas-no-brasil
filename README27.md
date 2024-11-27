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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2ec6923-ef9d-3331-96db-f46216d2403b | -6.83263 | -44.39315 | 2024-11-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e166c69d-b89b-3006-a061-173a5ba6ed2c | -2.68067 | -48.59332 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1911cf29-f061-355b-b334-96fb06d6915a | -9.7685 | -36.41882 | 2024-11-27 03:55:00 | NOAA-21 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f1686f1d-2513-3029-b5c0-de6bfd35a751 | -1.71927 | -45.37991 | 2024-11-27 03:55:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 745d99cf-f946-33b7-8b34-865b9843c1fe | -2.84809 | -49.40511 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf233de5-9d06-30d4-b94b-c39c50216f83 | -6.91096 | -35.0421 | 2024-11-27 03:55:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 05e44061-76ca-381b-9a24-6b989b87efc0 | -4.21109 | -50.88729 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f0335ad-8544-370c-9ebd-113ad0b7c7fe | -1.94252 | -45.72451 | 2024-11-27 03:55:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2211bb0-bfa5-3a1d-95d9-db508fbb2b8d | -7.22153 | -45.30599 | 2024-11-27 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4eca23ff-99c2-3a9f-8763-fe0aa9c50f1a | -3.71977 | -42.29279 | 2024-11-27 03:55:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5489f087-387b-3da2-9b84-f44ab2afd8f6 | -3.86417 | -40.44459 | 2024-11-27 03:55:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e2693c09-c9eb-38a5-b780-137fcc3627c4 | -5.54756 | -39.20362 | 2024-11-27 03:55:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2dbb93e2-1050-33b8-904e-8232641c8a91 | -4.15158 | -43.80096 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dab75595-e37f-3cb2-bead-630514d449ab | -3.24922 | -50.61695 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79ad5417-087f-3a5a-b676-a8a73d780118 | -3.95335 | -46.91428 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10a1a9a9-759a-3f5d-bde8-b09dc537ac1c | -4.16068 | -46.18355 | 2024-11-27 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec082ae7-b081-3d83-8e6c-eb9373388c82 | -4.22107 | -47.21919 | 2024-11-27 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f452567b-924e-3fcb-b991-ace5e6c90177 | -6.13127 | -46.91722 | 2024-11-27 03:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff84f1dd-2c98-39fb-9042-805d82b10991 | -6.73366 | -39.90437 | 2024-11-27 03:55:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2fad0a86-1b74-3beb-b17e-dadeb32e9192 | -3.51892 | -50.21848 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c831c093-1274-34f4-897a-e86a02f331d4 | -3.57853 | -41.96076 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9e052e06-ad45-370b-b746-9d7f6463598e | -4.22058 | -47.21302 | 2024-11-27 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03af5373-6b21-3025-8831-6fb201214887 | -3.69839 | -50.22251 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| efafe8b0-9019-3248-9616-81b02fd34eb2 | -4.4802 | -48.10967 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9285d23f-db3f-35b1-86c8-3834a10f53d1 | -3.24392 | -50.14701 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ca871832-27f4-3688-ada7-7f1e9f446a12 | -4.91945 | -47.85997 | 2024-11-27 03:55:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93d25c57-cf62-350a-ab26-49c79cfed61a | -4.13988 | -43.84671 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bbfe85f-1953-356c-aca1-ad4943d78744 | -3.56589 | -42.04062 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2a43e258-4c05-3bbd-8fd1-67b95c8090e9 | -2.9373 | -48.01885 | 2024-11-27 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66b8551b-884f-3ae9-941d-a8f0c8162434 | -3.69097 | -50.22664 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 758317fd-275a-318d-b0e3-30f8d9aba996 | -3.98104 | -46.64893 | 2024-11-27 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f6d5724-d04a-323a-ad0a-6651b075aef1 | -4.24071 | -48.67441 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 45234dc5-40c8-3420-b0f1-1c5fb3581f2a | -4.14707 | -43.80379 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d86e09b1-be1d-3e59-b199-4e2d0e1e16c8 | -6.48925 | -38.4907 | 2024-11-27 03:55:00 | NOAA-21 | JOCA CLAUDINO | PARAÍBA | Brasil | 2513653 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26f88b41-ce38-31ed-9b43-d66349017733 | -4.44573 | -46.59767 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b753ca3e-1158-363b-a3c7-4d431079c1e3 | -3.57969 | -41.95275 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| eec44bf5-109c-3590-a630-69d4285da3e8 | -3.2718 | -43.03595 | 2024-11-27 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 311db6b7-4943-3531-8593-c323159586a2 | -5.98611 | -45.36477 | 2024-11-27 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| c994f179-f575-3f2c-b846-72f6e7686ce3 | -3.10866 | -48.02246 | 2024-11-27 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d2055e0-ca14-3559-a2f1-d55e4ac3b9bf | -6.83198 | -44.397 | 2024-11-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cfafe9f-395f-3096-8ec4-b868878e8e99 | -3.57446 | -41.96133 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 80dba430-567e-39e4-b75c-8c8df9fc5211 | -8.0269 | -37.84864 | 2024-11-27 03:55:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97518a88-4d6f-38a6-9db5-4eda1bf3c5fb | -6.18663 | -35.28292 | 2024-11-27 03:55:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b2b50a01-bae5-3711-aca6-73c90ae34dcc | -3.16544 | -48.43892 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 516f87a6-81ea-31f4-a818-03e22b8e6f87 | -3.91175 | -50.60904 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ec8227d-24a8-356c-8c1e-d0b455c04ed2 | -3.91322 | -42.41761 | 2024-11-27 03:55:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 7e019f05-cb88-348f-813f-b1f764fea15c | -7.54209 | -35.09709 | 2024-11-27 03:55:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bd87f2f0-24f5-3d0e-b6f3-0bdf13834a38 | -9.84741 | -35.99799 | 2024-11-27 03:55:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 49e9026f-5b5e-3547-a613-5d38069c1021 | -4.21008 | -50.89305 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e85c65b9-84b4-3386-bd6a-623c2d3d8dcf | -6.90666 | -38.10163 | 2024-11-27 03:55:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4369cca1-601f-3df2-a013-1a553a1c973d | -3.61072 | -45.11517 | 2024-11-27 03:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 380165ba-ae25-320a-848d-2786c0c0d17b | -4.93172 | -38.75016 | 2024-11-27 03:55:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 071e4f4a-2b6a-3e91-a09c-843a7ba7d98c | -4.01295 | -47.65413 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61226395-a07a-3989-be56-63e989b2cd06 | -2.78709 | -49.20684 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7d83c476-3f9e-378d-8eb0-99683cad21c8 | -6.13179 | -46.91427 | 2024-11-27 03:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6809f4f4-4d05-3846-8641-b210da4ca4d7 | -3.10296 | -48.0215 | 2024-11-27 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 115819b0-9a6c-3b55-876c-91c82892291b | -3.88743 | -43.15389 | 2024-11-27 03:55:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 484f7a6b-5d24-3e71-8d67-0dc3eaaab378 | -5.90522 | -43.40947 | 2024-11-27 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2fdbd62-ff85-3a28-8e25-edd73847947d | -3.26801 | -44.54523 | 2024-11-27 03:55:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b00f7e92-ed03-3cbc-bf88-0d17152fa455 | -9.24304 | -35.67945 | 2024-11-27 03:55:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7d056b65-65d4-3f6b-8d41-f478057ab5ab | -3.5107 | -50.30772 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2a574125-136a-3ede-b038-b2c2a294c6ea | -3.97649 | -48.06307 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddc2f2a0-a5b2-3716-92a7-f907c0eb2ade | -6.19323 | -44.42611 | 2024-11-27 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 474899a3-8ae8-3a4a-a428-4ac70f0636ca | -3.23032 | -45.9291 | 2024-11-27 03:55:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0783942c-1cd2-3fe8-adb7-b3b61d8e0396 | -2.81981 | -48.60558 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a770236-27d3-3dcf-aeb2-57f629c0b0eb | -3.58202 | -41.96257 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 20a49dfd-8ae7-3b25-b605-e7e808e0696f | -2.99573 | -45.46508 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8e1c9f73-225d-3a3d-8f84-c594db2d28a2 | -3.97262 | -48.06679 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df68d7cd-ee16-33e4-819e-596dbd1fb0eb | -3.96753 | -48.0812 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 93758cc3-b640-3c47-84cb-7fb9ae7e7de6 | -3.57825 | -41.96192 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a195c520-b063-3390-8277-da4d78b1b003 | -4.2737 | -42.43596 | 2024-11-27 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b7a2ac56-997e-3716-b533-c8536477a830 | -4.23741 | -41.9234 | 2024-11-27 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 98fa7138-1a39-3e51-b552-7139ffe0475d | -4.4833 | -45.92169 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01ccc96d-48c2-3e5f-b687-38966f65fc45 | -3.78751 | -50.13174 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df31733b-ba01-39fa-be4c-8260c3177364 | -2.69914 | -45.65814 | 2024-11-27 03:55:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5886d3a1-6fec-3e70-9220-849fe738a743 | -3.50341 | -50.30538 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d2194f1-dfb7-35c9-8215-f908c6dac282 | -7.69324 | -42.97403 | 2024-11-27 03:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 6be939f1-27fd-38b8-9e08-37187dfc2f21 | -2.58379 | -50.64425 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc58f5c7-a91e-39ae-a2bc-f739bb61f1fb | -2.47168 | -48.7957 | 2024-11-27 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9adb8bd-a0cd-31ed-99a7-7455f284c805 | -4.65174 | -43.82092 | 2024-11-27 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44d96a1a-05a6-3d32-ad41-411581bad5ba | -5.60488 | -39.44613 | 2024-11-27 03:55:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fbce109c-6c2d-3b0e-a9ea-b63fe612f647 | -1.71733 | -45.37745 | 2024-11-27 03:55:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bb67a031-87f9-392f-8c86-b1e737e55973 | -9.69276 | -35.80093 | 2024-11-27 03:55:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 10a5ac69-173a-3e45-a461-fcdddad13eb6 | -4.38117 | -45.97545 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75e6785e-e50d-3f2e-9eba-5816fdb9b621 | -7.69401 | -42.96939 | 2024-11-27 03:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f8f96d21-2b58-33d6-b9d8-1c09d64503cb | -3.71085 | -47.66608 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0be6f087-b94d-33c6-846b-2a99c2bd1064 | -4.17677 | -49.41026 | 2024-11-27 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a94a749-5154-3a93-b305-68c36964ada0 | -3.70949 | -51.80573 | 2024-11-27 03:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f88dc6d-1f75-3d84-8922-dd401ae90a06 | -3.97021 | -48.06581 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2418ec58-0600-371a-b749-acea16bb90cc | -2.93159 | -48.01787 | 2024-11-27 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f30eb0f-0343-3679-a9e9-6b6eb7f6e5c3 | -3.11612 | -51.25945 | 2024-11-27 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a93fe66-1747-3b0c-bb0b-6e97a70f6151 | -3.57897 | -41.95731 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4e4e2c41-90ac-3122-abe5-5558f83cf280 | -3.89272 | -46.09762 | 2024-11-27 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9d8f1fe7-0e52-3674-9902-ecaacab8a338 | -3.97322 | -48.08194 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2ca1c25-45ac-301f-97ad-bfac4ba99d4d | -3.96617 | -48.089 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f48c622d-27f9-3bc3-8730-694748e25e33 | -2.09803 | -46.56149 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d6e8baf-20d4-329c-a116-ab6aaeec88be | -3.51801 | -50.22392 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24854368-147a-3ce9-af3d-448668247d7d | -5.99699 | -39.04972 | 2024-11-27 03:55:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eb07f3be-10c2-3ff3-8e7b-93f2d08a49bc | -5.42943 | -37.60785 | 2024-11-27 03:55:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dce2d185-1fbb-364d-9af2-6b759700fa5c | -4.00038 | -43.25652 | 2024-11-27 03:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)

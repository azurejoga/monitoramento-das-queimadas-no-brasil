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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 121a9658-4c95-3515-a4ad-bdcfae7e1ec5 | -5.80466 | -38.10482 | 2024-12-28 03:19:00 | NOAA-20 | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 540f1614-e811-3800-b841-439f1b818d79 | -5.80779 | -38.10191 | 2024-12-28 03:19:00 | NOAA-20 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4fa39bc4-b84a-3da5-b9f7-d3115b070579 | -5.21217 | -41.24011 | 2024-12-28 03:19:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9cce238d-2438-36c8-bcd4-3b8e58c733a4 | -5.59163 | -39.53612 | 2024-12-28 03:19:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 69548a73-5e4d-33c1-8793-10e60931939b | -10.16392 | -36.36007 | 2024-12-28 03:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fad1de04-8fd9-3bc9-a772-60dbfe8dfec7 | -11.13718 | -43.30793 | 2024-12-28 03:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e2629bba-ee5a-31e0-bb0d-cedd5dff71ed | -10.10384 | -36.15237 | 2024-12-28 03:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c9ef6b26-8cc5-37af-9487-52d92fc7399e | -6.00387 | -39.27901 | 2024-12-28 03:21:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f67ffe7d-fcfd-3345-a413-1226cbcd614b | -10.15988 | -36.35938 | 2024-12-28 03:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8d438e61-a0e2-381e-9c97-813207ae1f76 | -10.69467 | -37.04948 | 2024-12-28 03:21:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5f651641-19b0-3514-9948-5cb19437f24c | -10.10445 | -36.1489 | 2024-12-28 03:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 274ac82e-19b7-350a-b36c-f55abcc36b07 | -5.90364 | -43.48874 | 2024-12-28 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d63437e9-8290-33ea-973f-19cdca5c56db | -8.98733 | -40.62561 | 2024-12-28 03:21:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 730fd99b-cf76-3189-9fc5-78db3ead5e97 | -5.63243 | -43.72842 | 2024-12-28 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30c42b0c-04e0-3c13-b6fa-75e2686f06bf | -9.25497 | -40.95921 | 2024-12-28 03:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e4ade061-0346-3aff-a2aa-bf17222a55e1 | -11.13475 | -43.30791 | 2024-12-28 03:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e5ae050c-0be5-342e-8dbc-2a3b89805165 | -12.8295 | -39.41941 | 2024-12-28 03:21:00 | NOAA-20 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6558f98-cf78-39ac-b01c-ec508d663133 | -9.55283 | -40.9133 | 2024-12-28 03:21:00 | NOAA-20 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cc2fb46c-48a3-3f79-84a7-4ff445e945d8 | -12.8328 | -39.42331 | 2024-12-28 03:21:00 | NOAA-20 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 21f1e860-d371-378a-a93d-6ec0aea34775 | -6.0097 | -39.2767 | 2024-12-28 03:21:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a5fbcd3c-a607-3287-8c75-55e1f2e30745 | -10.87781 | -41.24155 | 2024-12-28 03:21:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dec146f8-314e-3cf2-8815-3835335d75ff | -9.26122 | -40.95657 | 2024-12-28 03:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bb2711f7-d1ea-3e2b-b13c-7f7d348659bc | -10.6354 | -40.21532 | 2024-12-28 03:21:00 | NOAA-20 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0020d30d-38ee-3e48-a3ec-48159ee02854 | -5.63942 | -43.7296 | 2024-12-28 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1272c2bd-06f9-341b-9130-12efb481c3c8 | -5.6407 | -43.72263 | 2024-12-28 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8383f9e2-28f4-3c30-9f54-163be1e0bb27 | -5.91056 | -43.48965 | 2024-12-28 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6978f04c-f5f6-3670-a034-d3ac0e0f5f9a | -10.63657 | -40.21527 | 2024-12-28 03:21:00 | NOAA-20 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d68045f9-d18a-3d79-994b-7a4c6ea524c9 | -6.58818 | -39.2679 | 2024-12-28 03:21:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 940387e1-1b85-37c0-835d-cb6434ed31ba | -10.16796 | -36.36079 | 2024-12-28 03:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5594b4f9-ef38-3d9e-9240-49957a276660 | -9.26052 | -40.96035 | 2024-12-28 03:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8b05b7dc-17b9-3bc5-b808-c0faf20adac1 | -6.00914 | -39.27995 | 2024-12-28 03:21:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b5242b95-329c-3649-a48d-65d9a4a65cb8 | -12.8337 | -39.41839 | 2024-12-28 03:21:00 | NOAA-20 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 600e9de4-9db3-36a6-9a52-21b48bc26875 | -8.98188 | -40.62449 | 2024-12-28 03:21:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 033fe27e-296f-3814-9f22-dcf63d4d8cba | -6.00332 | -39.28223 | 2024-12-28 03:21:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6e9b3fe0-0a39-3cbf-95e3-0af306e51bfd | -11.13096 | -43.30659 | 2024-12-28 03:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1be394a6-35f6-3d7a-9bd8-dd547226b9a8 | -6.39148 | -38.91165 | 2024-12-28 03:21:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 696345bd-8f4c-31c3-9d81-615406730149 | -8.98253 | -40.62096 | 2024-12-28 03:21:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 394c885c-6666-3781-92e8-367fab39fbcf | -11.13575 | -43.30291 | 2024-12-28 03:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f7d55d02-8271-321f-bf29-d0ef8f83d83c | -10.55657 | -37.04225 | 2024-12-28 03:21:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f7bc5f88-d45b-3d03-88fe-bc3c451c43d7 | -12.83426 | -39.42009 | 2024-12-28 03:21:00 | NOAA-20 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 646353d7-893b-32f6-88a0-f02b9c3aa1fc | -9.55837 | -40.91426 | 2024-12-28 03:21:00 | NOAA-20 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 87727043-eec3-3019-a55a-0f0a24894151 | -10.87822 | -41.2411 | 2024-12-28 03:21:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ffdc7cbc-a54e-3a69-8d5b-628d7125615c | -17.83419 | -40.03427 | 2024-12-28 03:23:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 44e972b0-0d16-38c1-8d59-665fe8b20198 | -17.83619 | -40.0327 | 2024-12-28 03:23:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0e710114-a107-317f-acb9-ffe70475120c | -2.39318 | -51.91432 | 2024-12-28 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe30677d-6055-3351-a100-4e3378d134ae | -3.80307 | -46.86256 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2877d623-0ba2-37bc-be16-385274a0ddfb | -3.97424 | -46.34859 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d55ab69-6fa1-3434-8b03-bb83349f9d23 | -3.03115 | -40.0035 | 2024-12-28 04:14:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0b12182c-467c-3dd2-b4ed-64c161554960 | -4.55809 | -44.12658 | 2024-12-28 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2efe777-0619-3772-b660-430f3fe9b560 | -3.89517 | -46.991 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7b452b3-ebd3-3d6c-916a-061aa318fc31 | -3.75816 | -47.22096 | 2024-12-28 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44681b89-8835-3bec-96f5-2e32dc1842ed | -5.31521 | -46.05684 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ea38e5f-461a-339c-b938-4c6310ceebf8 | -3.88892 | -46.95611 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9ce2543-704b-3df9-be98-743a6a60d89b | -3.84188 | -46.49716 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f4cd112-2d20-37c3-81cd-b0c8d4218bbf | -5.52117 | -41.74306 | 2024-12-28 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 03a81a8a-b11f-3323-9f7a-90c7440636a6 | -3.93921 | -46.76226 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 64a2ad71-a839-3081-bc9d-4f8555672e53 | -3.84081 | -46.67339 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aee1151c-3d14-37d4-a8ff-d7010a910a75 | -1.71688 | -46.21497 | 2024-12-28 04:14:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7810f4f8-9798-30f7-ab0f-75e7b1c46099 | -4.03239 | -47.0481 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 899d13c4-7801-3407-b4ec-ffe105ad57ae | -3.91469 | -46.98264 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 735c1798-6dba-3b4a-92ad-172e71ba92ea | -3.75737 | -47.22598 | 2024-12-28 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eb9ce76-d7db-3aca-b1dc-d224f83341bc | -4.74422 | -44.64298 | 2024-12-28 04:14:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 529b244a-72e7-3927-b626-44cb8b6d71d5 | -5.37211 | -44.84617 | 2024-12-28 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc09ee76-0081-30d0-96d9-aa4092b0adb3 | -7.17976 | -39.66706 | 2024-12-28 04:14:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea04a6ca-1562-376d-85dd-af494879ab5d | -3.95128 | -46.75949 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 956fc4be-2562-36a5-901c-d4745ce1a65c | -3.99294 | -46.67075 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24690384-1fc7-392d-87a1-13ea451c4855 | -3.92058 | -46.66035 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1253fcf6-96a7-361e-b2d0-c18a55a5829e | -4.44794 | -46.83406 | 2024-12-28 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcbb8242-f0e9-3d08-98f4-97095637df4e | -4.75829 | -45.70702 | 2024-12-28 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 661e8ec6-2069-30cb-b0b9-ba4ff77508ba | -5.66554 | -39.53581 | 2024-12-28 04:14:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 32694ec9-499f-34e5-baa1-5808d3fb0eaa | -3.82025 | -46.63263 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 670e04ee-251c-329d-ac6e-9dffbf320b76 | -4.01724 | -46.71163 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 904d7880-0eb6-306c-a760-d9f35eeecc4c | -4.05772 | -47.1112 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9033cfae-08e4-3111-ad4d-adfe69e7ab50 | -3.9032 | -46.98074 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3735c7f-7436-3dcd-97b2-149b281434f3 | -3.79925 | -46.86195 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6c6bc97-137d-3ef6-8230-a00d786d0ba8 | -3.89902 | -46.99154 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 67f26d34-5631-35ef-80c1-14ce63bc38c7 | -4.23623 | -46.79868 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c2cf45a-5a2b-3852-9ab7-5b0a76d8c162 | -5.94655 | -39.68387 | 2024-12-28 04:14:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2890a6a0-39d8-3061-9a82-f9d257e68590 | -4.23547 | -46.80342 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9df52698-388b-3605-81fa-b052e3dd9014 | -4.61561 | -43.73868 | 2024-12-28 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39a52e73-e5fc-336d-8b6d-c383b99a8c56 | -3.96892 | -46.67601 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fab27972-8a7c-3ad5-95c1-42091b8f0a7f | -3.81846 | -46.71663 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5a4141b-03ba-3c4a-b9cc-3332146c5e2a | -3.97633 | -46.3355 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7ccc78e-bb0b-38a7-be09-21a7bfe4836a | -5.71177 | -43.259 | 2024-12-28 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 906afbcf-bbdf-35b1-9979-392b07cacd34 | -4.06093 | -46.99373 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 42a38f7b-7924-3953-a951-d1ba3a90c907 | -6.2005 | -41.56643 | 2024-12-28 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9c78e4f9-211f-38fd-92cb-e17da202fa74 | -1.93108 | -46.4337 | 2024-12-28 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b8bc31b-1fee-342f-b052-d448d1c15556 | -6.61081 | -41.75086 | 2024-12-28 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a4d99cd-c36c-35c2-b259-8168a07afed4 | -1.999 | -45.58918 | 2024-12-28 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9bbaaf3b-41e3-3536-819a-4ce1481b1343 | -5.63902 | -43.72202 | 2024-12-28 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8c0ea1e-3ded-3501-bc85-d81f1438f857 | -6.49686 | -44.17245 | 2024-12-28 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| baccb37f-dc35-3487-aafe-40e138980d92 | -4.74703 | -44.64715 | 2024-12-28 04:14:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 687d2689-02d3-3e6c-bde7-0a0f1dfa62b7 | -2.8415 | -48.10822 | 2024-12-28 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9b28e5b-5b53-311b-a3bf-8ab3848351d4 | -3.91028 | -46.92045 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40505742-f403-3107-b40d-f7df8e7e21dd | -4.56806 | -41.29362 | 2024-12-28 04:14:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c15cb2e6-1cef-3d85-8af8-e6241e0da84b | -4.74363 | -44.64663 | 2024-12-28 04:14:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2097e279-5575-3c68-8bfa-cb6ded22685b | -3.8808 | -46.69138 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de137791-5e4e-3371-b0b5-2e2a81230cb3 | -4.01347 | -46.71104 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39da9d4f-9aa8-307a-8ce4-09d26324cac3 | -2.8457 | -48.10888 | 2024-12-28 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8b80351-2fa9-3167-bb7c-79037b6f06c1 | -3.98285 | -46.5588 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)

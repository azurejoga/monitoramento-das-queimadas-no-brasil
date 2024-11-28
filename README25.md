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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf6952d1-9772-3817-ba10-8ff0fd8e4b48 | -3.1113 | -53.8242 | 2024-11-28 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 82214634-4b6b-30bc-bd34-f2b361633186 | -2.861 | -46.8406 | 2024-11-28 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4c1c602a-df7d-3db3-a146-4b4d1f292019 | 1.2538 | -55.927 | 2024-11-28 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 879ce1fb-769b-3eee-b818-bc9a87be81b2 | -5.979 | -45.3395 | 2024-11-28 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d0f4e63c-5e5e-36d4-b645-da895ba2def9 | -3.4022 | -50.1119 | 2024-11-28 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c787e30f-ef97-38ca-94d8-0e0b9877a339 | -1.5713 | -52.2713 | 2024-11-28 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6d28aad8-3f88-33a7-b1f0-1c3a742138e3 | -3.3837 | -50.1125 | 2024-11-28 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| f289a52f-5e16-34be-9917-cc24578793ad | -5.979 | -45.3395 | 2024-11-28 03:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| cf42c07a-125a-33d8-88c1-d5f73294d95f | -4.0899 | -46.1493 | 2024-11-28 03:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 1114cba1-3b25-3742-a38a-4cde7fe9c87f | -1.3329 | -51.9463 | 2024-11-28 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 12731f7b-a4b5-302b-8504-6218a557feef | -2.861 | -46.8406 | 2024-11-28 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 5562df5e-b48c-38f1-9814-7c309f058cb6 | -6.1735 | -42.6221 | 2024-11-28 03:10:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| cd61877e-bb67-3335-a8cf-d46cba7dab62 | -5.9975 | -45.3607 | 2024-11-28 03:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 7bd77ad8-def6-3c72-988a-7b7245dfbc4b | 1.2537 | -55.9664 | 2024-11-28 03:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e710817e-5de9-3c8b-bdc0-e5b5cd79ede9 | -5.9788 | -45.3621 | 2024-11-28 03:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 9cbf0d9e-da86-373c-be19-83d0877ca2b3 | 1.2538 | -55.927 | 2024-11-28 03:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 76ead0ef-4f86-3800-88ba-b2286a65d348 | -6.1041 | -43.9593 | 2024-11-28 03:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| befad6b9-8ce2-3964-a94f-986f73bb53a1 | -6.1737 | -42.5985 | 2024-11-28 03:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 62573026-af0b-3bb3-9757-4c0ad605f551 | -2.7234 | -48.9034 | 2024-11-28 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 66bafe9c-dc49-35c4-81cd-2c7dacec2892 | -3.1113 | -53.8242 | 2024-11-28 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| befea62a-11f1-3f60-ba67-8ca9e5330cf6 | -2.8609 | -46.8626 | 2024-11-28 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5d943631-c072-3817-91ec-e8a5ac510deb | -5.9601 | -45.3635 | 2024-11-28 03:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 89d917a1-29d8-39db-8395-7fdb5a2673f6 | -3.9674 | -48.0851 | 2024-11-28 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 43524d03-94e2-3123-a324-122d2b4ed85d | -1.5897 | -52.271 | 2024-11-28 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 1752fa50-852e-3079-a0ae-ed74fb4e41a6 | -1.5713 | -52.2713 | 2024-11-28 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 97120db9-b30d-3ae6-af00-6b7f3a0e708c | -5.9788 | -45.3621 | 2024-11-28 03:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 1d40b3a3-593e-3e53-a51a-3062e97b15d0 | -1.5897 | -52.271 | 2024-11-28 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 9006a8c7-2b7c-3df6-b927-22b756cb4100 | -2.8609 | -46.8626 | 2024-11-28 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0f033f88-eba2-3313-aa01-cd6f712d98b2 | -1.3329 | -51.9463 | 2024-11-28 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 71386b1b-0e3e-3904-8caf-c26f01ab9802 | -3.1113 | -53.8242 | 2024-11-28 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 42170779-628d-3fdb-bc73-be1557de997e | -3.3837 | -50.1125 | 2024-11-28 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| e15af999-803a-3548-8eff-3a3ec0164468 | 1.2538 | -55.927 | 2024-11-28 03:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2dc9051c-a26d-37b1-8c58-3227f0317f90 | -2.861 | -46.8406 | 2024-11-28 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 276ddf72-5b2a-37bf-900c-617c0dd2a27f | -5.979 | -45.3395 | 2024-11-28 03:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9d15b1c9-fb91-3026-a4af-1e2d79c04d7b | -3.4022 | -50.1119 | 2024-11-28 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 554e3a31-9cea-3151-838b-5adea1fc1a97 | -6.1735 | -42.6221 | 2024-11-28 03:30:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 8660e14e-2c15-32ce-a69b-f36f1e1d6a92 | -3.3837 | -50.1125 | 2024-11-28 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 4d5b9520-1bdd-33b5-965a-edca17c130bd | -5.9788 | -45.3621 | 2024-11-28 03:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 888d3a76-97a5-3192-9098-cc1cfe7962a6 | -2.861 | -46.8406 | 2024-11-28 03:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d45280df-ec92-3593-bb1d-ca1558d1dcdb | -3.4022 | -50.1119 | 2024-11-28 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b18a0ba2-359c-32bf-beb1-31a86a54ad07 | -5.979 | -45.3395 | 2024-11-28 03:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| fb82d028-5567-3add-9f77-84c82507823e | -2.8609 | -46.8626 | 2024-11-28 03:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e74d5e72-1781-341e-9e83-f87322067ddc | -1.3329 | -51.9463 | 2024-11-28 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| bdbe9c8d-2255-3e16-b55c-58590512bf52 | -1.5897 | -52.271 | 2024-11-28 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 46b3886d-31c0-35d3-a689-cdf2ce9dbc4e | -3.1114 | -53.8041 | 2024-11-28 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 348ce52f-f3f1-3967-a132-b1d52992afdb | -6.1737 | -42.5985 | 2024-11-28 03:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 47.9 |
| 7b3a6d50-3628-3c25-a961-81d7d840906f | 1.2538 | -55.927 | 2024-11-28 03:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1d3389f8-7055-333a-b152-0a0931cf13e6 | -6.1041 | -43.9593 | 2024-11-28 03:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| b75770f7-c483-373d-ab0d-10cd430f350a | -3.1113 | -53.8242 | 2024-11-28 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5b65421d-b248-31a7-9210-05693572d6c0 | -2.84237 | -46.83653 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1541792a-50c6-3f69-899d-08a056d407bc | -3.20053 | -46.59164 | 2024-11-28 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9b37ba29-f75a-3239-b10f-c7f3e93b65b4 | -2.8651 | -46.85364 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a100ef0a-b31f-3288-8cc4-9493e37d53f5 | -2.86626 | -46.84691 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c73022f5-00e9-3b49-bbca-b7874872f4eb | -2.84363 | -46.8507 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc20b661-6700-313f-9084-a09e0dfa279c | -3.29502 | -45.51456 | 2024-11-28 03:36:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2d9b169f-f5a3-32e2-a12d-62435bfa912e | -2.27379 | -46.37225 | 2024-11-28 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0f5a593-ca8b-3332-85ae-8e70172e3235 | -3.47704 | -45.04067 | 2024-11-28 03:36:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f148830c-bd94-31c6-8872-cb1aff8d8a97 | -3.94894 | -41.49176 | 2024-11-28 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e69b5d4-84de-3232-8a13-a0e52eb332ff | -2.01592 | -46.39462 | 2024-11-28 03:36:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ff77c7f-a87c-3e29-9abd-94d851a4c56f | -2.87336 | -46.84821 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bba9bf2f-c87e-3848-944d-ec2202935b58 | -3.46256 | -43.52495 | 2024-11-28 03:36:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e4f27de-56a9-3365-a001-a6112f1f33ee | -2.83993 | -46.87203 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c587bb1-2189-3556-b7fa-94fb6760a340 | -2.85668 | -46.85999 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1280d505-3ee4-3aba-acd1-20b5210dbaec | -2.01479 | -46.40138 | 2024-11-28 03:36:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3973a63-4866-38ce-ae47-446cb372b420 | -2.01288 | -46.40109 | 2024-11-28 03:36:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1125e5c6-1463-3b82-b53c-d2e5bf534ed5 | -2.8483 | -46.86604 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17d7f1d8-b947-362a-99c1-8a5ce4bfcefb | -2.85076 | -46.85184 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73de1191-d00f-3b35-9f8a-8246d8687da3 | -2.86973 | -46.86935 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3af0403d-c319-3c14-a707-835e435fe510 | -3.20637 | -46.59934 | 2024-11-28 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 295348e8-51cc-3da4-8676-539bb5a740e3 | -3.20098 | -46.59798 | 2024-11-28 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 1de0552d-8ca2-31d4-819c-b0030eff353b | -3.29406 | -45.52014 | 2024-11-28 03:36:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 04f04b94-c456-3eb9-bd14-f4426610a2e2 | -2.87571 | -46.87727 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f5b8623f-4782-3a67-a455-b2bc55dd9ece | -3.95395 | -41.49253 | 2024-11-28 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 69475ff5-1c24-3e07-81bd-32a5b4819185 | -3.70513 | -43.42981 | 2024-11-28 03:36:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c23dc699-ea41-373c-a793-956d433eaa03 | -2.26796 | -46.36437 | 2024-11-28 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2454b26f-97a3-3762-ac5e-90e933d6acbc | -4.25888 | -40.70161 | 2024-11-28 03:36:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc6d044b-06a8-3936-ae56-815b799229b2 | -2.84834 | -46.84467 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce581291-5d48-31cf-ba4a-f7e0417e6ac5 | -2.84119 | -46.84361 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61ac9330-9cd2-3ae5-918b-c4b20ba22bce | -2.84116 | -46.86495 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3290c0b0-e935-3523-b663-fb3b726cce1d | -2.87091 | -46.86247 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ae847ce4-592f-3d3d-9de8-3c5a2e086302 | -2.60085 | -46.83652 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef525f21-e93c-37b3-a772-46e2b8598fae | -3.7058 | -43.42582 | 2024-11-28 03:36:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bed79b5d-12ca-3543-9c56-49a54129b17e | -2.84716 | -46.85173 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f764b9b0-992f-3b1b-a72c-0adc356bf9db | -2.84954 | -46.85891 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0d2195d-6c5b-32ef-a42e-9b7ac5f8c070 | -2.83892 | -46.83564 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a8e23ba1-5d44-30ff-8858-e937b377be3f | -3.62727 | -42.40233 | 2024-11-28 03:36:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 25fde0b7-10aa-3c5b-8ae3-2392c0e1c862 | -4.144 | -38.28627 | 2024-11-28 03:36:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ccfbab46-7d6e-3083-a422-194b1ca5eff2 | -3.49555 | -44.60741 | 2024-11-28 03:36:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8afaac4c-3dc6-3300-8477-38a78f8692f7 | -2.80672 | -46.83091 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8ecda6d1-1874-397b-8f2a-89595d753e88 | -3.86003 | -40.70974 | 2024-11-28 03:36:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 818268a0-2f1b-350f-93d4-1a329a01970f | -2.14034 | -46.48774 | 2024-11-28 03:36:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b7dc21a-2c8e-3da4-b5a6-650e982523ba | -3.70757 | -43.42555 | 2024-11-28 03:36:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 942f3a9a-ea57-32d6-8711-3c2e00fd64e2 | -2.87926 | -46.85655 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1c5535ba-4356-3891-958c-0ce888024b99 | -3.94845 | -41.49466 | 2024-11-28 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 827be8ca-2636-34f1-b67b-138180cf6c3e | -2.84478 | -46.86603 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c965e4ff-5cf5-3d96-82ff-f7f2a7cf2aa2 | -2.86033 | -46.83886 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fca5c500-b247-3dfa-a865-36fc73b59735 | -3.49636 | -44.60261 | 2024-11-28 03:36:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9b3adee-0d3c-30a9-941f-97d7fb522962 | -2.8532 | -46.83772 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 601052ca-6e27-34c1-afe2-5e7fab02d4bb | -2.84597 | -46.85885 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c8f10e08-d0fa-3746-9dd7-09da61763ddd | -4.18867 | -40.5583 | 2024-11-28 03:36:00 | NOAA-21 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)

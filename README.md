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
| a0cebb93-89f3-3456-b2f7-b600240d2b43 | -3.1641 | -54.4854 | 2024-11-09 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| e63bbd52-5d53-3229-b9d0-bd6a78238934 | -3.0321 | -50.3128 | 2024-11-09 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d107703b-f007-392a-a452-dc791cc24ee8 | -3.113 | -53.3191 | 2024-11-09 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ce42fccc-37f6-3437-a775-a53d5456f41c | -3.2808 | -52.7251 | 2024-11-09 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| c3ba63f5-ed01-30f0-924c-94f7ef39b4ec | -2.4104 | -48.5265 | 2024-11-09 00:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e5c3fdb5-b6fe-3a20-b1f8-bfa87557b0c2 | -4.2219 | -45.8529 | 2024-11-09 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 105.7 |
| d60a5dba-fda0-35c8-b34e-d706ebf852f9 | -2.4365 | -46.3019 | 2024-11-09 00:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0dc4d36c-78be-3744-be3b-2f10d8afceec | -4.1872 | -48.5499 | 2024-11-09 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 35a87bfb-f2c0-354a-a64a-4b1a39fc536b | -3.2353 | -50.2645 | 2024-11-09 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 74708bfd-ab69-3f1c-965e-f957fd835ecd | -4.2486 | -47.5729 | 2024-11-09 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| e3c14697-cce1-3723-a218-5d75008dcecb | -3.0864 | -50.5835 | 2024-11-09 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 32385beb-e518-33b3-a472-c4f6eeab3306 | -5.4699 | -43.6603 | 2024-11-09 00:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8a99da14-8e3a-3fc8-b752-19fca391655c | -3.5462 | -43.5663 | 2024-11-09 00:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 142999dc-9e9c-30e4-874d-843d390c50d7 | -3.5649 | -43.5654 | 2024-11-09 00:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 6bf9ff1a-5155-3db7-b56e-19b079c3fa2a | -3.735 | -54.2292 | 2024-11-09 00:00:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 31029fcf-a583-3944-8859-5551c62cf42b | -3.1512 | -52.9527 | 2024-11-09 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2f1179e6-61d4-3b17-a68b-195492e73e88 | -4.2058 | -48.5491 | 2024-11-09 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 317.8 |
| 598aafda-d3c0-3e71-9bfb-245bc845b239 | -5.4701 | -43.6371 | 2024-11-09 00:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 93684345-fcfa-34b7-8f6c-8b79a6f9552b | -3.9483 | -48.1724 | 2024-11-09 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 95f9b32b-ee5b-32e1-a91f-8530deb5001a | -4.2056 | -48.5706 | 2024-11-09 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 68c977b0-6163-3b48-8524-005eadfa722e | -4.6268 | -46.5435 | 2024-11-09 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 56db3c54-8d03-3aea-8027-4c4292d1e149 | -4.2243 | -48.5482 | 2024-11-09 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 4c0ca860-b9aa-386f-bd0e-57199730f8a2 | -3.9669 | -48.1716 | 2024-11-09 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 196.5 |
| 76ba6ec4-a9a7-319b-96d7-f8961bc88bb1 | -1.5163 | -52.1901 | 2024-11-09 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f7352ac9-eb40-31b0-a7d5-9f30528eeb5a | -2.6764 | -51.8189 | 2024-11-09 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| fc0d9073-935c-3657-af9b-b57d04a87cb2 | -3.068 | -50.5631 | 2024-11-09 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4e8e488d-9423-3680-856b-3bd7ac738d3d | -3.7564 | -45.9422 | 2024-11-09 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| d7a580d7-6652-3b9b-ab27-7345485dfcbc | -23.8884 | -54.0649 | 2024-11-09 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 90.5 |
| 35154c71-1476-3807-9c69-87b2a72facb4 | -4.2033 | -45.8538 | 2024-11-09 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 388.7 |
| e68541c9-1a0c-38f5-945c-629646cf3ff0 | -3.0865 | -50.5625 | 2024-11-09 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 47d9723a-5f89-3c05-9cd7-87b5f7be0c3c | -23.9101 | -54.0383 | 2024-11-09 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| ab303ef9-0d53-36e7-bed4-72495edaf1b9 | -3.4027 | -50.0066 | 2024-11-09 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 3e3e73bf-f093-3015-801c-9f7deeee78d6 | -2.5448 | -47.1137 | 2024-11-09 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3915c446-77c9-3427-9297-3f0d996078ab | -1.5164 | -52.1696 | 2024-11-09 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3bdd94cd-0ca1-38f7-80fa-f5306b988f88 | -3.9668 | -48.1932 | 2024-11-09 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 35f889ac-6252-3c85-8732-ea17d13f622e | -4.2671 | -47.572 | 2024-11-09 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ed108453-8205-30de-98b2-653150eb46f3 | -23.9095 | -54.0606 | 2024-11-09 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| dabb4232-4b2e-3d92-9cb9-b5165cedd2ef | -4.6269 | -46.5213 | 2024-11-09 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 3f4f1690-5b2f-33e7-b4b7-eb1a88c374a1 | -2.2295 | -53.7832 | 2024-11-09 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7c118098-9c50-34b4-adad-31e2090d0ef5 | -3.2624 | -52.746 | 2024-11-09 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| d807b558-7853-35c2-af01-ff1a7a3dff0f | -3.7563 | -45.9645 | 2024-11-09 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 46ec1fbc-c0e6-3b52-8488-1ab29a1657c4 | -2.7946 | -49.6455 | 2024-11-09 00:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a2b2876e-44bc-342d-a42b-dfe7ef834ed3 | -3.0947 | -53.3196 | 2024-11-09 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 9b2909d2-8e8e-3c78-bb11-57da1a562bc7 | -3.9485 | -48.1508 | 2024-11-09 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3c6606db-fa8a-36aa-bdfc-875f75e15ae8 | -4.2032 | -45.8762 | 2024-11-09 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 0c902687-e329-3faf-8e38-37b8138895b1 | -2.6078 | -45.1793 | 2024-11-09 00:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 468da4e2-be18-3b37-aeea-2123666e8a33 | -4.2034 | -45.8315 | 2024-11-09 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 35cad151-3c11-3c55-a01b-aa2a6c26d45e | -2.2479 | -53.7627 | 2024-11-09 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| dc067ec4-14d6-3c71-8a62-0b007e33a170 | -3.967 | -48.15 | 2024-11-09 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 4f334fda-26d6-3735-9d4b-d213b76173f4 | -2.5448 | -47.1356 | 2024-11-09 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d44355e2-c724-34cc-8254-797269967f84 | -2.6079 | -45.1568 | 2024-11-09 00:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f7011a64-5d97-3a16-9410-f169847dc2b1 | -2.2295 | -53.7631 | 2024-11-09 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| abb4c9c9-d958-35a0-825a-f50a1561a09b | -3.9854 | -48.1708 | 2024-11-09 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 18fb837d-b3b6-33cd-9295-45d3ab9da669 | -3.1511 | -52.9731 | 2024-11-09 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 233.1 |
| 3b903aba-417e-35b2-b086-4297269ce802 | -4.2059 | -48.5275 | 2024-11-09 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| aebcafdb-1052-352d-aab4-6dd685869f0d | -3.1327 | -52.9736 | 2024-11-09 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 54887ee7-7075-3c27-a022-8b5c15d3fa3b | -3.2808 | -52.7455 | 2024-11-09 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 5124cff0-e262-349f-b61e-a56abd87ee77 | -23.8889 | -54.0426 | 2024-11-09 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| 25e21ac6-7490-3f81-ab60-3d2f6bd072e6 | -3.58 | -47.3 | 2024-11-09 00:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c382e42-94df-3138-ae56-ff964cf818d1 | -4.18 | -45.86 | 2024-11-09 00:00:00 | MSG-03 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ccf8703-3302-3df1-903f-a31677f7e551 | -4.21 | -45.86 | 2024-11-09 00:00:00 | MSG-03 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9c9f72b-1f01-3580-a1c3-7173c504f944 | -3.55 | -47.35 | 2024-11-09 00:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5641c5d9-ef45-346e-917f-78046219b319 | -3.61 | -47.3 | 2024-11-09 00:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58fa5527-0c81-3af1-8245-3fc0bd5a1dd2 | -3.58 | -47.35 | 2024-11-09 00:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bd3a2b8-5ffb-314e-a48c-de88d6ddf623 | -3.58 | -47.4 | 2024-11-09 00:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d357b3bf-a960-3a26-af7d-33d2eaa96e5d | -3.61 | -47.35 | 2024-11-09 00:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ebc6279-e904-3e5d-9c48-e97b37e8b6d4 | -3.2808 | -52.7455 | 2024-11-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 436c7606-bc23-39c6-9774-e7c0c8af7d6a | -4.2033 | -45.8538 | 2024-11-09 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 325.2 |
| 81ecf47b-9e64-39f3-8b0b-226ebb7df976 | -5.4701 | -43.6371 | 2024-11-09 00:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b688a6fd-488a-34b2-b57c-10a3de8ce9cf | -4.2059 | -48.5275 | 2024-11-09 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 978fa5cf-3218-3f18-b99d-ddc58a3f51ab | -4.1872 | -48.5499 | 2024-11-09 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 252ee9c9-0d7f-351e-b706-a33d27f5b7f8 | -5.5616 | -41.7925 | 2024-11-09 00:10:00 | GOES-16 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 9ed5dd7f-25c6-3a24-ae51-c7b16f1237f6 | -3.1327 | -52.9736 | 2024-11-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 8234d2ae-d74e-3174-b8d7-b8a2e286495d | -3.2808 | -52.7251 | 2024-11-09 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7196ba3b-1bc8-322e-bd6b-c06df2f4030e | -4.2219 | -45.8529 | 2024-11-09 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 18c8ae86-a54c-3743-8900-073ec5a9cfd4 | -4.6269 | -46.5213 | 2024-11-09 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8d47a8c4-8c55-35f4-8b6c-1a5a2b0c504d | -2.4104 | -48.5265 | 2024-11-09 00:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| dd5307f3-b95b-386f-9b0a-90ae19bfc82b | -3.151 | -52.9934 | 2024-11-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| a1fca87d-71ef-3086-9b22-f6fc63573fea | -3.1512 | -52.9527 | 2024-11-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 0dd6cb58-b073-3fcf-8cbc-ee007a9f3b8f | -5.4699 | -43.6603 | 2024-11-09 00:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| eba341ad-3b0b-380b-8d74-c0d663602168 | -4.2032 | -45.8762 | 2024-11-09 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 214.8 |
| dac141f0-1a85-302b-b1ef-6a89605082d8 | -2.6764 | -51.8189 | 2024-11-09 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 0ef9c707-59e7-3647-ae86-b7658541fe03 | -2.6387 | -46.7817 | 2024-11-09 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ab0ce7e6-58f6-3f83-95a0-aa38ff86c33a | -4.346 | -46.8231 | 2024-11-09 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 4bd1bca3-ba57-33bb-ae73-a8c8df8f7a21 | -2.2295 | -53.7631 | 2024-11-09 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| dd2855a3-a9e1-357e-90fb-e005179feace | -3.0947 | -53.3196 | 2024-11-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| c9232cae-5141-3309-a368-29f3599e431b | -2.4365 | -46.3019 | 2024-11-09 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 458bc888-b7b3-360d-b699-e79933ceb519 | -2.2295 | -53.7832 | 2024-11-09 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d1238fe4-4213-3860-affe-1ff7ea85a9af | -4.2243 | -48.5482 | 2024-11-09 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d7695744-d204-3d81-bd57-37febce8b1ac | -3.2353 | -50.2645 | 2024-11-09 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| dc12dedb-4cde-352a-9a0b-24a699076a3d | -2.5448 | -47.1137 | 2024-11-09 00:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ca437dc2-6368-398d-b062-5436e6a8db63 | -3.0321 | -50.3128 | 2024-11-09 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a5bafb31-ed77-36d5-baa4-8d9f8d9d1ae8 | -3.0864 | -50.5835 | 2024-11-09 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2218b233-e749-3b1b-a3c4-7ed4bf6656ab | -3.068 | -50.5631 | 2024-11-09 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| ec2f8537-c143-30e5-b883-3d19b7024fa6 | -4.2058 | -48.5491 | 2024-11-09 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 165.7 |
| fc76ee2e-9081-35d6-9eee-126852392f38 | -2.5747 | -49.1421 | 2024-11-09 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5beecf39-3ebb-30c1-9104-6b1442926ffb | -3.5648 | -43.5885 | 2024-11-09 00:10:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 2f59f03d-9d07-3665-bade-5f3a4676e905 | -3.5649 | -43.5654 | 2024-11-09 00:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 06fa5742-6f20-3baa-87e1-90dad94d89db | -3.0865 | -50.5625 | 2024-11-09 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| dde0cb0e-8ac4-362c-9824-8ea7f4bf8514 | -3.5462 | -43.5663 | 2024-11-09 00:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |


[Clique aqui para ver as próximas entradas](README2.md)

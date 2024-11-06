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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79059bbc-6176-3c09-b0c2-68604071ae7e | -4.1324 | -43.56983 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61567d9a-b602-325e-a31b-929bbaecef09 | -3.95219 | -48.3607 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d946290b-a4e9-37cf-89e1-cfe5fd568e57 | -2.4995 | -49.08425 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a486d7bd-160e-3236-8702-e07629461ba8 | -2.78659 | -48.57692 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f75c430-7317-35dd-838b-47e4b29a9139 | -2.82526 | -52.92513 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 797a2a96-f488-372d-9a5b-b4dd48a11244 | -2.61939 | -51.9222 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa3b8cec-edb0-3e81-8ca9-81fa70b9ada0 | -3.11032 | -53.71933 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba236b85-b6b4-3658-9090-0bf703f84152 | -2.91322 | -51.04236 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 373c8ca2-8cb3-3e88-8797-b9d721030799 | -2.79944 | -46.63846 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49083976-aa5c-3e22-a187-b6ca736a2999 | -5.2155 | -47.46487 | 2024-11-06 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a5a80bb-ab8f-3d0e-b679-71b17d35c407 | -3.82789 | -51.68955 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e37415d7-abd0-3cc6-b8ed-ca26b262fcc4 | -4.48563 | -48.48987 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a222018c-52eb-3684-94e9-878e0466605e | -2.91035 | -51.03799 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f952895-dbe9-31d4-a4e0-e3a290bd60f4 | -2.928 | -47.87115 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73dd9a14-ea81-347d-9288-0ffb87cd88aa | -2.8508 | -51.76747 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 00dd16e1-f959-3e12-b037-84fa2649d44b | -3.03794 | -49.52734 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d357cb7-5d04-30dc-86d7-f769d69f4976 | -4.15771 | -46.57733 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fe82ace-286e-3b3d-8bcc-3aa5b50c10e6 | -2.80915 | -46.64378 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2496494d-726b-3f27-8250-5ce5c562940e | -3.17363 | -54.47058 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f6c1133-769d-31b5-9bde-550cb3716c09 | -2.84838 | -48.44569 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d5eb106-6115-3628-9490-2798d93cc840 | -4.12934 | -43.57924 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 13b0cd73-89cc-3ffc-a61d-1a93624f0613 | -3.09861 | -54.28804 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef489db6-185d-3dce-b542-0864ccb95d74 | -5.22725 | -44.9128 | 2024-11-06 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d102b51-af34-3cac-ae66-14d8c15c5e8d | -3.14872 | -51.15279 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4311d09d-3fdd-3b50-b98c-ef75a93f2fb3 | -2.52377 | -51.16902 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 483ada29-c3f7-3548-a937-edcb6c749714 | -4.38178 | -45.80042 | 2024-11-06 04:36:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a12a167-7ec8-3a65-9ab2-067fff1aadf6 | -2.67766 | -48.51419 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d698367-5ef2-31f8-8968-67e580007aa1 | -3.09884 | -53.71386 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25f3015b-1a14-3332-8015-49aa657bbbe5 | -3.01991 | -51.44103 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b53a61f-5b4e-3143-8abb-bcd7fa408266 | -6.05339 | -39.43435 | 2024-11-06 04:36:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b4ad4810-4c30-3a28-859e-4de1e82e860a | -3.58405 | -50.26342 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbe80f98-6cd8-3eea-a342-b9b609381cb1 | -2.00998 | -46.80577 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7582d091-a8ac-32e5-97e2-f48f758fb2f0 | -2.95719 | -51.05719 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d82d8d8-8d92-3c4d-96e4-fda4e7334b73 | -4.19593 | -51.02464 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f96aa156-df09-3ff8-9f27-79126fca96b3 | -2.75405 | -53.2176 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4839e9e4-b3fa-3aa1-804b-9bf7bfacf3bc | -2.65805 | -48.57441 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 124d3e13-68e3-311b-8b1e-15ddf0067441 | -3.60855 | -42.86166 | 2024-11-06 04:36:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac9ca218-13c6-3565-9201-5528cac39d58 | -4.10933 | -48.50543 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d308a40a-bfc2-31f1-9404-a6573bd73b4f | -4.30869 | -45.83383 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ee15aad-a0af-3974-8985-3b9870f90058 | -4.35755 | -46.52704 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52fee9ce-7a3e-3f11-ae7d-4d4ac40f8490 | -2.77716 | -54.72733 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4a00125c-10fb-36c0-84cc-598f9e1f3be8 | -3.7095 | -48.99622 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44185906-549e-3b74-99d7-b471e9ee4e56 | -3.5498 | -47.38591 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 03c0f9c8-51ae-3947-be57-0a26d1ecb383 | -3.22966 | -45.55531 | 2024-11-06 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48c6297f-b893-3185-ad93-bd6ef0e5edf8 | -1.39121 | -52.1983 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d7b3f8a9-0254-3b30-ab95-3746252e5ce8 | -2.89913 | -54.24163 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 711c3683-6f0e-3bc0-8efc-dd6fdc2d10a6 | -2.47234 | -49.01999 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea018fc2-54af-3317-ba4c-bc19fe5e1907 | -3.74994 | -44.56401 | 2024-11-06 04:36:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16982b3b-5097-39a9-b353-2ca92d2e3d7f | -2.64555 | -46.77114 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0a572e5-1ec3-3a22-b146-a785ff601837 | -2.30782 | -46.73505 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f94e6d7-e19d-384f-b943-959e03ad6977 | -3.67022 | -50.2325 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ef01d4e7-8953-3397-9f89-cad499769266 | -5.28373 | -46.2635 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04d9c052-6e71-3d34-90f7-7c8e58d4cbc9 | -3.64074 | -51.79306 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cd02397-c22e-315f-a708-042d6863cb20 | -3.06857 | -47.77509 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b25aecc0-d120-3744-bc10-38d7062d5b84 | -3.06676 | -52.50288 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 86125eae-1b57-3c1d-8bc9-8242abc27f94 | -2.46738 | -48.05843 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70657385-f40c-3fda-b6fc-3dba02cf094b | -3.55372 | -47.38285 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cca00d05-d1e8-3d33-beda-79309a9d804a | -2.6105 | -51.76347 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6de03450-3a6d-37c0-896c-d2d6540122a1 | -3.10876 | -51.13457 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5b8f34c-d2e8-343c-98af-3f64e93fe1d0 | -3.2957 | -53.11752 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0a751e6-dc5d-383a-98ef-b7c59ab2717a | -3.04218 | -51.25901 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8469b115-4046-3a28-a314-37b5bbb69f40 | -4.12958 | -48.87558 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52602212-921e-3931-b839-452849abbf7b | -0.03699 | -50.79244 | 2024-11-06 04:36:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1ab3595-babd-3208-b714-ed55309cb6bc | -3.89419 | -50.25681 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5a45d67-5f3c-32ec-87d8-360ef882fa0a | -2.60689 | -51.76289 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f15d4620-4a89-3d55-9efb-f9f5577201d8 | -3.73431 | -49.8727 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2d86527-673e-30b1-bb90-b1eff49cdb5e | -4.0878 | -51.04223 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88a4cda5-4fb8-371e-a3d4-a4792c6ce20b | -2.93633 | -51.05389 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ad2049e7-fb9c-3f10-8c9f-6014d1436f85 | -4.24782 | -50.2571 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cefe98cf-4839-3342-b935-f63d5682b33f | -2.42678 | -48.59763 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a644720f-74af-32a8-8b36-186b031340a6 | -4.23724 | -48.53635 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 591a145e-4dd4-3ff5-8bab-2dda6cbeca1f | -2.60767 | -49.23957 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c24b300c-d3a3-3a66-8e51-716063b3cfcc | -3.7634 | -51.774 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c6b6760-77c5-3230-9078-7df6b41257ab | -2.80945 | -51.48789 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 389d7d6b-cc2f-391b-8f36-597dc5fac3dd | -4.21844 | -50.63922 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdfbc2e0-75b5-3370-9101-131132c5c033 | -4.58226 | -48.0665 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ecc9b057-ba46-33da-9d6c-cb6311c0eedb | -3.90935 | -47.95923 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71072bb8-3645-3288-ac9a-a6ba05eeb41f | -3.02778 | -51.0945 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb796364-dbe1-3484-a85f-d583b6d58fb1 | -3.21041 | -49.2317 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4fedf45-cafd-331e-a636-e402d13ccf0e | -3.70838 | -50.18736 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fdc0f11-ddbc-37d2-a5d6-0401438bfc6b | -3.73029 | -53.39324 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f7cc6e7-bd3c-322c-b80e-60fc09bcdcaf | -2.9168 | -49.34832 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d914c40a-0ff7-3c23-9455-0099f58ff251 | -2.86568 | -48.70153 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24758630-99a1-3836-83f5-02fde0f4fd77 | -2.85453 | -49.48405 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98abc49f-7902-3ed0-97b1-541485b65e04 | -3.96356 | -48.1569 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 716f882f-028a-3cf0-9269-d4324f2d7674 | -3.27457 | -50.35524 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 760260b0-6d45-3801-809e-70f922cf3504 | -4.82058 | -48.56402 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edd5d9b6-85f5-3ecf-ad39-7001e28b1c22 | -2.84346 | -48.45548 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70b5a03b-f067-31e6-bd6a-94fa7fc3d10b | -3.09565 | -50.24286 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8609c1d4-f68c-3f1d-b5b2-d2478f82c7e4 | -4.60284 | -48.6959 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c6bdeaf-d158-36ba-9e0a-17e074114c96 | -2.80106 | -51.49474 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 90146eca-b351-3674-8df1-03c47f0e88c1 | -2.58598 | -46.18613 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f71a6155-4aab-3591-99f9-21a954842c79 | -3.74044 | -51.08611 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f67efc31-0526-31ef-8230-8c746a5ac1c8 | -3.16611 | -51.29785 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dcfd0514-3e03-37f5-b062-a6ae10908c6d | -2.84953 | -49.47258 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 566a77fb-7f68-3507-bd85-315adef7c0bb | -3.24454 | -50.19559 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 342db19e-eef4-318e-a0d4-0e01929e3b02 | -2.15942 | -53.66623 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1905bfa7-61f8-3fa2-b99f-a4784b15d073 | -3.29131 | -50.03119 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| caa27e9d-9b30-3e30-9932-cdc5532ec1a0 | -3.96815 | -49.94205 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55b527d5-f25f-3802-8dc3-380d19a041c6 | -3.53161 | -50.3324 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README32.md)

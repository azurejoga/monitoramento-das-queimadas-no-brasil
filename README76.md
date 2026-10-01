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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cd2cd22-d0f8-3622-81f5-00958fc44fdb | -4.06288 | -51.10754 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5384ccca-a07d-355c-a139-e821acfc9357 | -3.09616 | -50.26661 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11511700-d2bd-3c9c-9c6f-2c13340a987c | -3.79887 | -50.60854 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 38603bdb-a6fc-3c14-b1e7-b9aabbaf3481 | -4.44307 | -50.66632 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f258e978-1e19-31c0-80e2-39152decb552 | -2.98469 | -51.03601 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe287875-3669-3ad5-9d21-c0667dd2843c | -2.98546 | -51.03095 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7ffb5085-e0bf-32b5-b8e5-872c54052ee6 | -3.29598 | -53.85757 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59f7dc0a-03e2-3e40-97cc-804d88c94e6e | -2.98622 | -51.02591 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 65c97148-38ca-33bc-8413-d3f150dd9704 | -3.14032 | -53.74499 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 53ed0b67-ad04-3caa-b3e6-196aacfa994e | -2.90282 | -54.14766 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 558b0fdd-45c0-3fed-a160-ec2990c5238d | -3.74262 | -59.41487 | 2026-10-01 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 578bf207-9bb1-31f3-94b9-dd77e0e04562 | -3.68915 | -47.12347 | 2026-10-01 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebfb2dc4-8042-360d-949a-41b6c5d5bd29 | -4.25306 | -55.04256 | 2026-10-01 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a258df4-9b45-3047-b7ea-0f484613aaec | -3.02884 | -53.87303 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c679d2b8-8537-322a-a21b-cdc638a8a815 | -3.18297 | -51.24633 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f289c866-1f6e-3f61-acf1-d04d087d2b85 | -4.29789 | -50.77439 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 75c36567-93ea-351e-97d0-d6c655ea7df2 | -3.01179 | -53.88048 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 389f9f8d-25ab-35c0-a356-269a26ad1493 | -3.48654 | -59.52838 | 2026-10-01 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2ab060b-d733-3cd8-bd34-a472b3174461 | -4.46111 | -47.91872 | 2026-10-01 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dacaf99b-4c86-3d47-bf23-e3ef6249b6c3 | -4.28481 | -50.761 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| f68db91b-efea-3bdf-ab8b-0da7a6275577 | -2.9875 | -51.02737 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f7f9106b-4efd-303d-8392-55683c9ae096 | -3.00733 | -53.87814 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3744dff9-77d1-38b5-9d76-802a9405e741 | -5.86987 | -50.16294 | 2026-10-01 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 516d2468-ec32-3884-acf5-f71088f38a81 | -4.14918 | -59.92179 | 2026-10-01 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03462475-319f-364f-9ba3-42b64ee7a1ed | -3.14778 | -54.57818 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a920db59-24ac-36b9-b845-a793e3e4857d | -3.24856 | -50.81593 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22ee81c9-28ad-341d-8252-c2989dafc78c | -4.03962 | -54.23269 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2cad2b4a-dcf3-3b10-b061-d35180182824 | -3.21778 | -48.81649 | 2026-10-01 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| daa21d7e-7045-318b-8ff0-4acb0f18ca68 | -1.74362 | -57.18138 | 2026-10-01 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06823d0a-414b-3a18-ac57-353056872fc3 | 1.84024 | -55.5601 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3af826d1-efb7-354e-bda6-8f62ea39230d | -4.30458 | -50.89795 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56521845-1f83-3d69-b3ff-f2184588368d | -3.76538 | -58.83794 | 2026-10-01 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d609245-faed-327e-b328-5b397d3c0b9c | -0.44955 | -52.00962 | 2026-10-01 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d55d2ce-e1af-3667-b691-6751910d7889 | -4.28999 | -54.7937 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7acd6207-d575-3095-b962-c1d8aeba3a4f | -3.95713 | -48.12593 | 2026-10-01 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c62f00dc-1a75-321d-a713-c242523028fa | -0.93862 | -47.5555 | 2026-10-01 05:16:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd46ee46-1a40-33fd-aaf4-af2bf5f3fecf | -3.29674 | -53.85261 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 86959c5b-2c1b-3eda-927e-4dc0b38b2d7c | -2.90688 | -54.09494 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75b3788d-0163-3803-9148-4efd1741a4eb | -4.29218 | -50.77916 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 7252fdba-65e0-347a-b6c5-50189c5cfb9b | -1.41991 | -48.90194 | 2026-10-01 05:16:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9965d90-e1c1-398f-a0b0-055b78f07145 | -3.01495 | -53.886 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88bda914-7ba0-34e3-b3f2-bf4560a357e6 | -3.00995 | -51.07198 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d1615ab-fa86-30c9-b62f-6614dea52dd2 | 1.10564 | -59.47486 | 2026-10-01 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0c56957-3e69-39e6-98d2-3a76b0c31ce8 | 1.64596 | -50.90336 | 2026-10-01 05:16:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1c5cf58-a19c-3880-b65c-b339c32d8f75 | -3.02031 | -53.87675 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1e82455-7c67-362e-99d2-026253432429 | -3.18268 | -57.83859 | 2026-10-01 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdd3c71e-1ee5-3c8e-a99b-bbcb8fadfb7b | -3.2704 | -53.99957 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b137c3d-df15-3585-a714-1c91579f746c | -3.16328 | -54.09465 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d909278-71d8-37e6-ae65-ad021bda8e39 | -4.16481 | -48.89954 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4950cb54-e4c6-3119-8161-3d2c3c3127b1 | -3.15321 | -54.08323 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50666c9a-26bb-3578-81c9-a042e06a5b0b | -3.41626 | -48.33605 | 2026-10-01 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 116c36e9-53c2-3a10-b2e5-6d2267da693e | -2.89608 | -54.08845 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f74fe1c-2a7e-3421-a30b-fe0c4f100c3d | -2.44684 | -49.21971 | 2026-10-01 05:16:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9011e67d-3942-3799-921d-64be691b0999 | -1.21024 | -49.28642 | 2026-10-01 05:16:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21b6c5af-f41b-3c8f-a97c-373f1039be50 | -3.47377 | -59.5228 | 2026-10-01 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9e71fe6-7f08-3a4f-9068-7173bdfac674 | -2.99694 | -51.02886 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ce94bc2-1455-34e6-874e-074eb53b2cac | -2.97602 | -51.0295 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4147e42c-2a8e-34ce-a31b-306145aae4aa | -3.48362 | -49.92339 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1068aaa1-811c-3e46-9ec8-8a777766501d | -4.26692 | -50.78072 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| b9468e3d-a196-328d-8ddd-9f7e2b7b9dad | -4.39297 | -54.83018 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9d1c556-45b6-3ada-a584-9d587c6fbd2f | -3.3818 | -50.94077 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b8428d4-2bcd-341e-8a4b-8872df33dc44 | -4.04345 | -48.99497 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5278872c-67be-3cf7-b75b-755351c67173 | -4.28159 | -50.78313 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 387c2833-bd2f-3065-aae2-96323ec6fa00 | -3.21495 | -53.94539 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1363958-4502-3687-93ef-06c1f9dba499 | -3.68847 | -47.12829 | 2026-10-01 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca1e5bc7-c92d-3647-9522-2fdad78345ae | -4.29748 | -54.79491 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6db81e4-aca2-3945-84dd-3fa3e0f6274c | -4.15424 | -48.89418 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d07021a-0774-35e0-9fd0-326d5305bb5d | -3.37551 | -50.95029 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b648858-5395-3384-b48e-fe880d9407d3 | -1.46687 | -48.91619 | 2026-10-01 05:16:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 177b08e2-b491-3262-830a-bbb70307c1d2 | -3.57479 | -51.47428 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 52f375e9-ccd7-3c97-bc7b-895e79f7d54c | -4.2709 | -50.75322 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 89b61a7d-9c79-3b0b-bc39-b94a9702d5e3 | -3.3803 | -50.95097 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e7e4611-dc76-385d-acad-688835043dbd | 2.5431 | -60.60802 | 2026-10-01 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e15c5e3-502f-35eb-86b7-26949ed89715 | -0.44168 | -52.00438 | 2026-10-01 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef4bd45a-3aaf-3331-bfa2-402997450093 | -5.17719 | -46.18975 | 2026-10-01 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 439ca983-adb2-3c73-9149-09cd1e36edbd | -2.92828 | -57.65723 | 2026-10-01 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0117f2d-637e-3999-a984-c7f46d67c789 | -3.2506 | -50.12213 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e113d519-ab09-3a72-b577-6c609b112952 | -3.56881 | -51.48309 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 96247240-df83-3331-9bed-c7e4ad547942 | -3.16713 | -54.09527 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 179c109f-6274-3c3b-92f2-01f5dc8185bf | -2.9076 | -54.09019 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 608abeed-51f1-3de9-b0a1-1cc78a4f0548 | -1.85821 | -50.66813 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c053c45-2d56-37a7-8be0-1ca3df15b146 | -2.55429 | -57.85337 | 2026-10-01 05:16:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb6e8a5d-f6da-39ab-b2fa-b806c9fc4074 | -4.29871 | -50.76883 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 644f011b-09ad-3776-b487-27bfc859d30a | -2.03662 | -54.05793 | 2026-10-01 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8aff78ae-50d7-3f2c-800c-14420d2e3942 | -3.79968 | -50.60317 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5a6b3853-cc97-3a4e-98e7-c4c163f1a962 | 1.70451 | -55.90555 | 2026-10-01 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a060f118-34aa-3f01-8913-405ffbed81aa | -3.47814 | -55.41217 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b1dca74-5a2e-3834-be5a-ee108274dada | -2.99094 | -51.02664 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 41566174-e238-3f8b-b9c9-6edfc3108f1c | -2.96427 | -54.07942 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 829b5443-d2c5-3fe4-92b4-550d8c5e6e5e | -3.1818 | -54.10232 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 3e467c71-dafd-364e-b1a9-c9560315988a | -4.06355 | -51.1012 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8bb15a4-f453-388e-9912-4ed65c87f371 | -3.01106 | -53.8854 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4bb0e68d-79df-36c0-96d9-cae867c3adbf | -2.88224 | -54.87408 | 2026-10-01 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3f8be6c-c740-3827-8fe2-d8284b33da74 | -7.48947 | -54.99916 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a649ac5-5e5c-3b67-a178-a0d5f94a86b6 | -6.92064 | -59.28623 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3350da83-a07a-390a-adc4-d5eda03305e6 | -7.49019 | -54.9943 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f77a4dc-77ca-30cc-b053-678dd54f7a54 | -11.40264 | -51.02633 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae6f903d-061d-31ab-9c03-cadd93f13c35 | -11.28681 | -50.9679 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d2ac8d8d-39ce-3406-8226-38925594513b | -6.65496 | -58.87311 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beb0ac19-4081-3910-ae82-365e566d34c9 | -5.86447 | -57.76277 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README77.md)

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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cf0f2d4-47ba-352b-9772-74497ed9dcb9 | -3.45568 | -40.23492 | 2025-10-03 04:29:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bf2b8950-80ce-30a5-b9e8-428b522dce2b | -3.4513 | -40.23548 | 2025-10-03 04:29:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 10ab32e5-c481-3c7a-b564-66895666e4ba | -2.38364 | -46.47314 | 2025-10-03 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 766aa9d0-4666-3707-a938-eb27fe23c05b | -2.2566 | -46.97791 | 2025-10-03 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 454bb42b-4286-3c04-8fe0-056daad59cfa | -4.44448 | -43.23444 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c168a7af-db30-3931-b07b-910c5a016274 | -3.84347 | -41.58865 | 2025-10-03 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 94e0d51d-2457-30a1-b730-1a47a384b6a3 | -4.93836 | -37.99958 | 2025-10-03 04:29:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b1c3e3e4-2122-3783-998f-835060efe7ee | -3.9374 | -47.5638 | 2025-10-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0cfc52fc-e5d8-35c1-9473-5e9b6c40d892 | -3.50374 | -50.2107 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff3ab1c2-a7b4-3ff0-b274-1517d70413de | 1.79036 | -55.82104 | 2025-10-03 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5c3e9ce-67af-3790-84ee-707bac2248eb | -2.93203 | -54.18142 | 2025-10-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67b1cdf4-fea1-3db8-b5b3-edb64edb5bdc | -3.09071 | -47.01034 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8206532b-a3af-3bbb-9e60-d6260fefb68a | -2.57261 | -47.49372 | 2025-10-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff97f266-6e8e-3bc5-865d-e6a7bcecb569 | -4.20649 | -46.43863 | 2025-10-03 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0528236-cc9f-3f48-a89d-e5318ba667be | -3.66923 | -38.81211 | 2025-10-03 04:29:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 75dbdde7-0665-3a38-8b00-d58fa1fafff5 | 1.52519 | -55.84696 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f35bb00a-f3e8-359b-80c2-bb761d1b5fd1 | -4.70311 | -37.37369 | 2025-10-03 04:29:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 23e66633-be86-3932-ac36-123b1816ad16 | -3.84405 | -41.58485 | 2025-10-03 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b3533212-e633-3f25-8950-e302c5ec4415 | 1.52074 | -55.85546 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 104dc1b6-65e1-3c80-96c5-72965a19a2c2 | -4.18284 | -48.13972 | 2025-10-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 458727a2-1ec1-34a2-afd1-78898f3df464 | -1.08374 | -53.67924 | 2025-10-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f3cbb0f-f4c9-3c9c-8087-315e652e5a98 | 1.79093 | -55.8249 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b829f5b8-db4c-3ad4-b17d-4b722d56f2ea | -4.44758 | -43.23966 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ee6a06f4-8998-3530-b1b6-fad1db3e9caa | -3.84157 | -41.57286 | 2025-10-03 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2ee2affa-c0b8-33a5-8e08-df24fb6cced4 | -4.65304 | -45.8005 | 2025-10-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96756149-c25e-3374-b0a1-46a4c8fe155e | -3.17013 | -48.60763 | 2025-10-03 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d9df73d-6bc2-3b63-8b16-3cbe0864954a | 1.51899 | -55.84404 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 26643cff-7f8f-3f3e-99e8-16ad7cd0d03d | -2.30331 | -48.14472 | 2025-10-03 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be8874e8-3d91-3eda-b603-52084fd5f953 | -4.00875 | -43.2763 | 2025-10-03 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 697eeb36-5f4c-3a3c-9b51-a2bc350bb5e8 | -2.94094 | -51.27751 | 2025-10-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 601f49af-cbf7-3b1c-ade1-6275b96be10c | -3.93354 | -47.56673 | 2025-10-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb0eb4a8-f821-39a1-bffd-5c7f6084c505 | -3.45586 | -40.23615 | 2025-10-03 04:29:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b617caf-98b2-33e9-ab0f-3930b00ed8e1 | -3.32569 | -48.70572 | 2025-10-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e63f476-0b8e-3228-b3e4-bcd9d1da6328 | -4.4343 | -43.37831 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88058f9a-3998-3812-abb7-d2d4f795cee3 | -2.73605 | -47.14862 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3c69d52-6a52-3008-a831-5a1ff534ef37 | 1.78778 | -55.82425 | 2025-10-03 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59bc7fde-3bfe-33e9-9952-c641d54dae7a | -3.84576 | -41.57349 | 2025-10-03 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9cb7f444-67a5-320f-903d-ddc793b76a10 | -5.06837 | -42.73551 | 2025-10-03 04:29:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9621f457-d233-3b08-ae96-eee2a8f52526 | -3.49743 | -50.27354 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c4968a2-26ba-37ab-a94b-16fde3bdd42a | -3.33446 | -52.05216 | 2025-10-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ebd9a789-2d78-39d2-afec-cac17c6857ff | -3.49341 | -52.4669 | 2025-10-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31751eab-f294-3864-80e8-808d67dfd87e | -4.44378 | -43.23908 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d34b5d8d-6e59-333e-8333-3ab2c4a23ee4 | -0.90331 | -47.54621 | 2025-10-03 04:29:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 392ecc5a-bc93-3fab-a091-ec4977e92006 | -2.94173 | -51.27274 | 2025-10-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c07521dd-e086-376a-af75-19fa33ea9e16 | -3.30561 | -53.85344 | 2025-10-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67c6186e-9e5c-3121-996e-eefd6cc78dbf | -3.4027 | -46.90456 | 2025-10-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08484240-1206-3a93-896c-171e81c71e6c | 1.52226 | -55.82785 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92ee6d64-d9bc-37dd-94d7-526b31520f58 | -4.65418 | -45.79327 | 2025-10-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ec24b9b-c720-35da-b073-b6fc95f9d53f | -1.14367 | -54.19148 | 2025-10-03 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 454d8af6-3458-346a-bdf5-1a0405bb081e | -1.07911 | -53.67835 | 2025-10-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0eed7f2b-719b-3c59-854f-5fb4ebbaa4ee | -3.69856 | -49.00813 | 2025-10-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b3db986-a682-30c7-8483-e94d50644a47 | -3.69797 | -49.01181 | 2025-10-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbf7e5bf-30b2-3bb9-a01f-f30b36d92b86 | -2.62844 | -46.83918 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46cee42e-882c-3704-9271-cd55af9e5aef | -0.89997 | -47.54569 | 2025-10-03 04:29:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 408244e1-8785-380e-853d-01260a351f34 | -2.95798 | -53.06548 | 2025-10-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62b812d2-dce2-3745-be00-8697c2e47742 | -2.25363 | -47.88015 | 2025-10-03 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 472f0a29-f104-3ad2-b9ab-e5de6f3583d0 | 1.52048 | -55.81627 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bec9945-3add-38d8-8f5f-512cb0f7c553 | 1.78838 | -55.82811 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aecb75fb-7ae0-3c0c-aa10-ccd213c96f57 | -2.97119 | -53.09306 | 2025-10-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbe66ea1-d688-33d3-9cbd-371fd2524b0e | -4.43292 | -43.3874 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c3028d3-3b15-3a16-86f0-2489959208d4 | -1.08297 | -53.68404 | 2025-10-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ecf8d7b3-d9bf-3eef-9d3d-38afbfd58efd | -3.46346 | -50.09443 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56d2a4ac-0d2b-380c-8102-7101ebeb783b | -1.07371 | -53.6822 | 2025-10-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2977e89b-1a0e-3634-87ac-2a40ca9b6e04 | -3.49381 | -50.27296 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a402483-c543-3dad-a805-7fbeaf334c5d | -3.56309 | -49.45702 | 2025-10-03 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 816eca3b-4f22-3511-82fe-6ffcb4ccd556 | -3.08962 | -47.01721 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 32ac4ef2-6f38-3bd5-9202-51707923bb59 | 1.73153 | -55.87167 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8063394-809a-3ae3-acb8-05c92b5655bd | -3.93685 | -47.56726 | 2025-10-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4cca567e-a642-3c29-ab6b-37678d23644a | -1.0168 | -47.79185 | 2025-10-03 04:29:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 984d8256-f27a-3e18-9e1f-23203315ed77 | -3.19477 | -51.02977 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b0d11854-f737-3ac4-90d5-0a7d01ae22f8 | 1.52578 | -55.85077 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 232dc551-ef46-3b2f-a216-9a5a98a840c5 | -3.30807 | -44.89985 | 2025-10-03 04:29:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b68510f2-4616-3d34-b4af-57ddc581347d | -10.0148 | -50.2443 | 2025-10-03 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| febfe097-1d4a-3c4c-a0ac-1774b7d8dd55 | -10.0151 | -50.2229 | 2025-10-03 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 6db60ddc-4721-31b7-989b-622effcc25b2 | -9.9962 | -50.2248 | 2025-10-03 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 4cece869-136b-30d9-a8bf-a3dca6b844c8 | -9.9959 | -50.2462 | 2025-10-03 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 24bdcab1-368a-3ad3-b2d8-201f756d79b7 | -9.48775 | -45.91935 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0dc75bef-033d-3af5-84ed-2fc6d9e85914 | -11.81043 | -45.03938 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9fa0cbc1-06b8-38fc-b2f5-c6715abd934a | -8.52841 | -47.24389 | 2025-10-03 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| feadc80c-7361-3d02-95f7-d66060659ae9 | -7.76196 | -46.26717 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 9b0853b5-e3dd-3554-881a-c617a8830f74 | -6.24137 | -45.36512 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f376d36-59b0-3daf-944a-e5b86a19a408 | -7.29402 | -44.18571 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a9f218e-b283-302d-a534-c40e1aeef1dc | -5.74982 | -44.61052 | 2025-10-03 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95ceb1e3-22a6-3e8e-a23b-af96ed0c23a9 | -11.12299 | -47.86778 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d608b41b-3ee4-39b4-b191-e81d01de3721 | -10.93729 | -46.71862 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e935459b-312b-3754-a118-521964485910 | -9.05842 | -46.64709 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7f4dbd2-aff6-3b9a-9f88-082bf3de456d | -6.55667 | -43.89715 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba070947-390a-37a7-ac68-1939d8a33d93 | -10.87944 | -46.71022 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35d2af56-9908-3ef6-b900-37d6229607a4 | -11.28173 | -47.83047 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99aa14bb-f648-3d5f-863b-58462e8aaba7 | -7.55998 | -42.39792 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5569e846-94d5-30df-b2cc-dee655ffab6f | -11.1347 | -47.19527 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fe8c9f5-1f2e-3748-acd7-6a78295fff37 | -10.82483 | -49.37661 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75713194-3e56-359a-b215-cbf81be8f243 | -10.8403 | -47.21836 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14588394-d1f0-37b3-9f04-2d6c37310d85 | -6.67259 | -42.8266 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e4930a6f-4301-37c1-9c38-9edef15d21f7 | -4.66596 | -49.51377 | 2025-10-03 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47604445-11b1-3034-9fbf-7324ecd56253 | -8.62935 | -51.07792 | 2025-10-03 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23e29361-a611-34e4-94b4-47bb56bb4da2 | -10.3465 | -43.73134 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13223514-d84a-3510-8ee2-16a4a5996fa3 | -10.27975 | -44.3318 | 2025-10-03 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c51712f-f017-36fc-808e-58316880d7b2 | -10.2917 | -47.93306 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20bad1f2-6d52-3b1e-9f03-0ee99d0f49fc | -6.23625 | -44.25863 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README87.md)

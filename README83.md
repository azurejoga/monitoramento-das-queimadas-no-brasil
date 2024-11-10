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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb719ed0-c03b-3b9b-85ad-3faeee425330 | -2.6042 | -49.18646 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 398a9d65-801d-3fb3-aa14-93c2ac33cc27 | -4.08253 | -42.93511 | 2024-11-10 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1ab9789-3737-3aac-ad72-ba13f28e34c2 | -4.06891 | -50.01005 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0da1d13e-2f40-359a-bc4e-537916682902 | -3.82597 | -48.88505 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 082e7af0-9b6a-3384-a3b0-b3d709b09b39 | -3.69947 | -47.64114 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32d5f736-60ba-30ac-b327-09fd918ef515 | -2.27167 | -50.63723 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dafd04d0-5b17-31f8-b005-d7371561fdf8 | -2.71153 | -49.29945 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bf14ba8-bc1a-377c-923b-0a93c5c0f962 | -2.92047 | -51.47868 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d12842b-34b2-3fce-b4a5-dc2c7db6f59d | -3.23002 | -50.25889 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e1b1fcc-edd5-3986-8c1e-5ec435e51e42 | -4.88835 | -48.60925 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e6c73bb-de18-3c61-b4e2-cdf0b4fa8e51 | -2.35222 | -53.74949 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28745f40-5649-3f3f-a737-0ad7df756c3d | -5.56934 | -43.97926 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c948e56-c525-399e-88cc-0d75032357e7 | -2.66556 | -48.64985 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5384cd68-1581-3119-a178-9c0f42126e48 | -3.43961 | -50.3022 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c4d8a17-ace6-3f01-928e-3afbb6293809 | -3.09239 | -50.46725 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 112a5ecd-ccb7-315b-b6c3-4215ac492a0c | -2.19448 | -50.53292 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9299839-95c7-3414-af63-58ec759005d1 | -4.12145 | -46.92228 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a736fd05-9319-389a-90cf-b015c14d4990 | -5.31593 | -46.23481 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 106838b4-bc7a-376a-98f1-5d9d3144f455 | -3.28451 | -49.63361 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be8242c7-1fc8-311a-a8c0-e902f834cb44 | -2.93526 | -49.42799 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 042d2520-bf32-39dd-8221-307986215dbe | -3.08432 | -51.22002 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba968f8b-07e6-3d63-b0f1-d3243c3c6104 | -5.84895 | -44.49426 | 2024-11-10 04:38:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fe3e6622-8242-3670-a04e-d83a619401cf | -5.56583 | -47.77767 | 2024-11-10 04:38:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c761a0fa-287e-317c-9dae-a4de50195326 | -3.03113 | -48.04631 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aff8f801-6b75-396b-be7d-0a9c006e67d0 | -3.05883 | -48.04351 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1962346d-5342-3cfd-b858-65c7531103d0 | -4.61041 | -49.57652 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 921b5d6b-d3e3-3bcd-b863-08eaaabef0ee | -7.63058 | -43.55764 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6468e2ca-fe78-36f7-af5b-721e2090e314 | -2.59795 | -48.19831 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e4c9853-928d-33a4-a9fa-45dfb44190e2 | -3.27202 | -46.31835 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c188a3f-dfbf-317f-95b5-02444cf85119 | -8.40418 | -44.12094 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fd5ed1c-372b-3970-82c2-a90df8ea7a81 | -2.93861 | -49.42852 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8d5ee75-ee96-3f0d-8530-57e1399b30af | -2.40455 | -50.30819 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f359fcc4-762e-3d1f-bf1e-ba11cb2796f6 | -4.13034 | -50.2399 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7938659-8208-347c-8994-d6e8f7f5047d | -3.32465 | -50.23613 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 064cd3e7-f9a5-30c1-9316-33021f42341e | -3.7116 | -50.43814 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e92ff140-9a8c-334c-84b9-fbb81acaeadb | -3.24507 | -48.75116 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90ab9082-f16b-3bfc-9cca-24f6fd32c533 | -3.901 | -50.29969 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c0b453c-416f-3db6-98b9-7ba021194bcf | -2.81636 | -49.43111 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2b19d3e-0a03-3e9a-b167-20fdd23b3213 | -3.23741 | -50.45544 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a000fad3-b1ce-3885-8aac-b7b7caa634db | -2.84914 | -48.44904 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86c55772-e4dd-3f57-ac1e-0b395ea8bb36 | -2.75724 | -49.35672 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dd6d0aa8-b7ad-3901-8bf0-fb9e4287832e | -2.87642 | -49.37595 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9ba6a80-7127-3138-9ac9-94fdf800ee82 | -8.39098 | -44.12291 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90e2031f-43e1-3fb8-b2ad-adfa5356c9bc | -3.30576 | -50.13663 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7355efdb-c90a-34d6-8f54-d0c2448368af | -3.19234 | -48.65843 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c0c2083-f1bc-3d06-83bf-c3b52297232d | -4.38583 | -47.23969 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 337a03b5-0c0c-3749-a363-26c3a2149472 | -2.35575 | -53.75394 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e49715e7-53a1-3ad0-a45b-cccd62cb279f | -2.88558 | -49.23081 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa50e86e-1c4f-37ed-b33f-4a929e6f3085 | -4.11432 | -45.70597 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52e1e955-c901-3741-a768-27c5e8e72ad1 | -2.13951 | -50.81029 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5049ec3-b363-3ff8-995f-a1a2fb18fd8b | -4.08509 | -48.51181 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23fbd0c9-13b8-3d17-b4de-554e59121bc6 | -7.03741 | -48.27734 | 2024-11-10 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ef090e5-be73-391c-a113-ecab794ea78c | -3.14679 | -48.5807 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccc6a062-44a0-3ba1-9e9c-88910ae1f1d5 | -1.48313 | -55.4428 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 72bd9321-f227-3ad9-a36d-038a1a717efa | -2.9012 | -46.8212 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bece714-952a-308b-b9f3-7f931bf691f5 | -4.85087 | -48.48271 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8999a655-10da-3130-ab11-cecdb1fc138a | -3.24399 | -46.47755 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c61fa83-1e01-38b5-a562-0ac49fd968ed | -3.18721 | -50.44004 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93925ae9-7232-3824-bd39-59343998af16 | -3.25171 | -48.7522 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10afa7ec-5f5a-3809-8c91-a207223c8066 | -3.09717 | -49.40631 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0ef5be15-bec6-3fc6-92c3-9cda2addaad2 | -2.21274 | -50.77824 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0090b07b-9e2a-309d-9383-f82272b5dfbe | -3.10171 | -53.33057 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72db6953-6a84-30ee-b009-f04a1d9ca706 | -3.67548 | -50.22394 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd30d086-6e1a-3546-90ab-53935efcaafd | -2.87418 | -50.41079 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4805c04e-4dde-3b47-a9d5-4becee27712b | -2.4853 | -48.80584 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2a22ddd-419d-36c7-8eb5-d0c13c66f1c1 | -3.67367 | -54.04435 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16615a89-b84c-33a4-8cf9-524fe3c7976b | -2.7651 | -49.39382 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20b88bc4-8b17-31a6-8888-570fbd216f7b | -3.12835 | -45.96334 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd8fd3c8-22d7-3fa5-ab9b-10071bf0bdfa | -5.1756 | -47.61508 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cf88e699-4fff-33d0-9480-e33b1797ce0d | -3.94745 | -48.91119 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85534c0f-af8e-3979-98f6-f8c5395f8192 | -2.6201 | -51.30175 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a85dda9-6024-397c-98b5-7bc67f6d9e7f | -6.23669 | -44.14422 | 2024-11-10 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0b5e3ba-86b0-39ad-96b6-c8ce38cb21a6 | -4.27442 | -50.67605 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e3728c0-725b-3474-90ab-10d0d03ecfbd | -2.84858 | -51.36417 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12a43772-3687-3ade-8f54-f17ce63e1db0 | -2.21179 | -50.53565 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e1fbcee-ae82-3de2-be12-d981beecb4e5 | -2.9663 | -48.02855 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad9969cd-521b-3043-b0f0-9557d046d314 | -2.57265 | -49.82067 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b2bb454-8ba7-32d2-b5d1-1ed605cb287e | -3.885 | -52.39783 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a1f42f6-2da0-3955-bfbd-18ef851c889a | -3.0914 | -50.42923 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8170022-a6b9-3ca2-acf8-cf6fbf5b5fbe | -2.26819 | -50.63669 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85e7236f-e8fe-3df1-adb0-f12372fc7e2c | -2.14978 | -50.70136 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 079dfc69-622e-32e0-990d-1ad8dba06f1b | -5.84498 | -44.4937 | 2024-11-10 04:38:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59aa5f91-8737-34b4-8d2f-0b8811861a08 | -2.62401 | -49.47268 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c2b35a4-ce12-3029-a4b3-8b1ac971ec02 | -3.56073 | -53.94752 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e3f5b1d-f749-3d29-be06-f1a8fc1e3463 | -3.51026 | -51.66563 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19bec60c-2b6d-3e1e-9239-55d4ba05f0a7 | -4.56044 | -49.38294 | 2024-11-10 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47f3d6fd-022f-37ff-a36e-72689af717e9 | -2.83144 | -49.46582 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0a8dbd1-6f99-3d72-af01-11c594b2f960 | -5.50547 | -47.17362 | 2024-11-10 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3867d65-e2bb-3879-8dd0-46d8f1236b8c | -3.13418 | -45.31865 | 2024-11-10 04:38:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad0b6057-b19a-3d2e-8579-62149814eaa3 | -7.10244 | -46.90143 | 2024-11-10 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf978801-69f2-3547-bd9f-adeb4453c882 | -2.86899 | -49.27105 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ddadae-b60d-392b-9d8c-38371f1b40ee | -2.96188 | -48.03497 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2deb696-599c-34cd-8437-58e510855736 | -3.96999 | -46.16122 | 2024-11-10 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf82010b-41b4-31a4-a318-711041567694 | -3.19747 | -50.30985 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc37b861-e620-317e-a9d6-4aafbc717765 | -2.68224 | -48.50068 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f8d5c38-0116-339e-a020-8a0d9a585bbc | -2.42181 | -51.96091 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 535eb37c-7e26-364a-8530-cad794a420f7 | -4.09051 | -49.12103 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 805cb7ea-c8b7-327c-a299-3cc8aad1f1e6 | -4.23799 | -43.82359 | 2024-11-10 04:38:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f2e96d9-4013-3239-9179-3b49f983b666 | -4.37061 | -48.15144 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e5a50d0-90f8-3b7e-887b-f90a996165b8 | -3.07526 | -50.57509 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README84.md)

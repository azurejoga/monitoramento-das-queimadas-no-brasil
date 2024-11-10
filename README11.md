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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a34f640-7e6d-3fd7-a762-17aa32250160 | -5.33204 | -45.08023 | 2024-11-10 01:19:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| bd11a8be-2874-3deb-8fcc-051b41074855 | -3.2829 | -53.25333 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 629848a3-2ecf-3d07-abfc-f2cc90eee407 | -4.08062 | -50.02203 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4c3d3e2f-0834-3198-9dd1-3340996f3104 | -2.94368 | -54.12318 | 2024-11-10 01:19:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8f1abb23-dce3-32c1-9b2e-d3bec96e08bc | -2.24195 | -53.78159 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 54bef797-6eeb-3734-8917-f64244156c89 | -4.21065 | -48.14355 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 51ef9534-ebfb-3d7b-80a7-f2c8fb7bc086 | -3.28755 | -53.68216 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8bb0c06f-fbfe-3b06-9e84-6997aa846eaa | -3.10011 | -53.33048 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8ae90e92-c297-3bdf-a084-010bffb7e3b3 | -2.17565 | -53.23867 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2c0135de-ddca-3200-9455-fe9be6cfd23e | -5.17855 | -47.61729 | 2024-11-10 01:19:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 1e22cc83-60ff-3c07-8d71-4176100736b5 | -1.52223 | -52.21346 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 3c2d933a-54c8-3cb3-8fd3-8ea586b331ed | -2.56464 | -50.67592 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 42bd5085-67d2-3a10-acf6-b5fdc9345839 | -4.29711 | -48.64949 | 2024-11-10 01:19:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0a176ec4-cd9f-3d50-9f71-eee1bbe65e47 | -3.69043 | -51.28376 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 87100eae-c7fd-32ed-a11c-57c54b445b11 | -3.30858 | -50.08483 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e05fcc42-fcbb-32fb-87d4-24a88bd166c9 | -3.94831 | -48.15226 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 4b8ef9a6-71fd-3e4d-98c7-386a1071b060 | -2.08194 | -52.05057 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 89bd90c5-9489-3bb0-b973-c5db95c9c7f1 | -5.21064 | -48.345 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 30.1 |
| bede37e3-3341-33d0-b69d-eaf13f8574f6 | -3.1017 | -45.29537 | 2024-11-10 01:19:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0bb6d054-340a-30a3-a649-3f0bb008c672 | -1.55266 | -54.25565 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0d532bf1-9a0a-3b33-8183-da46de419937 | -3.14021 | -50.43426 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 21aff6bc-e709-355b-b921-8b536bf4b3cc | -3.04781 | -49.53933 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 48512d07-e98e-353f-b6e5-892269558740 | -4.11326 | -50.72943 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7faa7945-f67e-39b8-9d1c-c299a5c3d25a | -3.20269 | -50.63815 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 4bd69a35-8d08-359e-8725-7c2940010fe9 | -4.05381 | -49.21246 | 2024-11-10 01:19:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 8c6f3746-9853-386a-98b4-920f77a4a657 | -2.92262 | -54.42686 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 26f1011c-7ce8-326f-9d5d-3173abf70a84 | -3.2934 | -53.26157 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| dcc3b1f1-6f65-3d7e-8bb0-ef76e67ab700 | -3.12918 | -50.43594 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 224.9 |
| 5d3a0726-0360-30e1-9a9a-c88a63edaad8 | -2.94536 | -54.45991 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57484d32-cec2-3b2c-abaa-266bcf5e6897 | -3.35972 | -53.40942 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| fe0b6cb2-2b4f-3770-a0b9-843c3653948f | -3.42048 | -53.05453 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c82893d6-14e8-3559-99f1-d1e0017957c7 | -3.81445 | -54.61549 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 92ecba00-5312-372e-987e-b7e957d8b406 | -3.18366 | -54.3173 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b3d0a1c2-d434-34b4-9513-0d0b7c72d529 | -3.47258 | -59.40215 | 2024-11-10 01:19:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e7df01a2-f5b2-3b84-a87a-f4051cf2249d | -3.10634 | -49.43239 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| fde84e3a-2ba7-3b76-a833-5dbd2d81c22e | -2.81397 | -51.80302 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 01e5848f-22d8-3b01-942c-836d73aaa7cb | -2.98865 | -53.9819 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 94590435-c985-3928-a37f-6f3d54bb803f | -1.24269 | -51.76503 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 6ae5ddda-aae7-3bde-a485-012676456d13 | -2.08073 | -48.81223 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 29ae9a41-829d-3e72-91c3-1eed65a985ff | -1.95849 | -53.07058 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 09e2d750-236e-33ea-8e47-de48bc70d038 | -3.43334 | -50.30854 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 7ea3ac15-4c1c-36a6-af27-1babe64cef82 | -3.44034 | -53.06163 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 33daa845-fff2-3f56-8191-e7c8f7753fbe | -3.30464 | -50.14064 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| dec3298c-d61f-3dc5-815b-ea2fa5124b2b | -3.03239 | -49.55271 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 69fbcc06-1266-342f-8f37-f9749489602f | -3.35707 | -53.39064 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9ab47c94-1965-3f94-8d03-78f1eca29f19 | -2.92999 | -49.35501 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 15c712da-f7c7-33bb-8b0b-ec7ae38af931 | -3.8737 | -50.26276 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1983f689-addb-372d-bffe-7ac3e08b1668 | -4.68812 | -45.15525 | 2024-11-10 01:19:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| de6364ac-be3b-31a1-832b-76bfb589634e | -0.04142 | -50.77762 | 2024-11-10 01:19:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| c8fcf4ec-8965-3954-9fbf-0c0288489ab3 | -2.26727 | -50.68019 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3898d36d-1033-3ad2-b1a9-271f1bdfc33f | -2.69096 | -49.86553 | 2024-11-10 01:19:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 3625b89b-e180-3af5-9feb-365d9e2be804 | -2.42094 | -53.67754 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 968e1f79-d0a2-3293-bbfe-c55ab028b986 | -3.20283 | -53.40577 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 52563249-3353-34e6-a07c-a455b6a91147 | -1.25472 | -51.7757 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3bf6397a-353c-34bd-aaee-e6144b27bb70 | -2.04794 | -51.15828 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 10cb673a-4943-3fc4-ae20-707c085ceb0c | -2.44793 | -53.93737 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c9074c2f-744d-3a1b-8ef5-2d74f8e3a00f | -4.89578 | -48.61018 | 2024-11-10 01:19:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 1024b526-8a33-3afa-8b52-cd60270456ea | -2.81607 | -52.95815 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5d560cfa-6493-358c-8141-91970362b9d8 | -0.97914 | -53.71558 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e381a56d-37fc-3165-96bc-ecde2ea3904d | -3.87278 | -51.97565 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| a2c490fb-54d1-3f69-8fdb-4e7e9145e1b0 | -1.46826 | -54.31069 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d53e9747-b2d9-307a-a472-2b1f217313a2 | -3.27722 | -53.67426 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e04d6884-75be-3905-aeee-8110df40dfb8 | -1.39873 | -52.35722 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 7899ca57-105a-3056-b0cb-bb2e40b45c2d | -2.258 | -52.20701 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d5295262-799b-3370-b2d7-bfee0ef7b88c | -2.93692 | -49.36528 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 350a4599-6a60-3853-943f-a9fa2c9a0fd8 | -2.60365 | -54.18994 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d66b7cf8-9bcb-35f3-8ab7-11d56af1860d | -1.20436 | -55.72316 | 2024-11-10 01:19:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e97feaa9-6f58-3147-984c-b94fdd889e99 | -3.02403 | -49.54277 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ca6f6ffe-0480-311a-bf4c-4a63ca8eb1e7 | -1.43953 | -54.50493 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 095175d0-8d71-355b-876c-ecc4b6458dae | -3.95404 | -49.40539 | 2024-11-10 01:19:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6cf9f423-0962-3b83-b001-88e3ddc35319 | -3.28424 | -53.26292 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a7fc5679-c3fe-3383-845a-67e0ca1af1c6 | -3.23748 | -50.30548 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 4c2819e6-41e6-33f5-abf6-58fd3a5c4d6e | -3.0986 | -49.42296 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 8678409c-b5a5-3bed-9300-7724411121ce | -2.04211 | -52.05631 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ae58938d-5135-38b9-a69a-5876536dd548 | -3.43073 | -50.30074 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 196796d2-7108-318b-b089-edf41bec76da | -3.16978 | -54.48817 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 82ff2326-88cd-3da0-bd70-4e999cb7ed00 | -2.26465 | -51.89543 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4582ea62-ad6c-3f3e-994e-2fcaa92a0958 | -3.67322 | -54.66564 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51bcc2a5-16f2-317b-b3da-0855e1931e07 | -1.28426 | -52.19685 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 37268370-75dc-388b-8946-6fbf326a354d | -3.1938 | -54.32495 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 269bbce9-2914-3fd8-9510-8e2270b6dc4e | -3.60819 | -47.35039 | 2024-11-10 01:19:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c1691ebd-d06d-3b67-862c-2f907b998813 | -2.09825 | -50.2184 | 2024-11-10 01:19:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| febfff40-4f5f-32be-a721-3bcbbc012a20 | -4.09663 | -49.13079 | 2024-11-10 01:19:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| d996daf7-61fb-34cd-bb17-33e83ebba35f | -1.66469 | -53.80548 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 53e10449-14f2-304f-9b55-c045d32f8d82 | -4.27923 | -50.67928 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 17f46ea6-1ea1-3584-9936-a8120053db20 | -3.53597 | -51.48912 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6e101100-03d1-3c9d-8476-196a6e112918 | -3.67191 | -52.29581 | 2024-11-10 01:19:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 61c4cab6-da10-3e32-a7a3-122a42655f33 | -2.65074 | -49.41391 | 2024-11-10 01:19:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a9910fac-a028-34b8-898f-2f6f9e57dd7e | -3.0921 | -53.27329 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9c1ef42c-9d85-347f-9664-861bae6b0d4c | -2.24456 | -53.66716 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5730f06f-a12f-3d6e-9a40-d06088693d29 | -2.92225 | -49.34972 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7c734bf9-c785-3743-940f-d73e7509732d | -3.24932 | -53.41233 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| abfcd35f-43c0-3390-a1bf-0a93d0e41468 | -2.15636 | -53.69506 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4995312f-52be-3208-9929-d30cea55ae72 | -1.47272 | -52.08133 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1beacdc2-980c-3bf4-afdf-32fe58218c59 | -3.19042 | -58.84207 | 2024-11-10 01:19:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 885a0c06-7ffb-3b72-bb81-f1688cdf85da | -2.80589 | -52.54572 | 2024-11-10 01:19:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c9d6bf29-a81c-3171-81c1-66797d2a12bb | -2.24066 | -53.77232 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 56e8c535-146c-3589-a725-38f159feea34 | -3.25711 | -53.40168 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 11db221e-18f0-37c4-946c-f36f677c2c7d | -1.87483 | -54.18556 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ad7c47e5-4891-30b7-a739-54756bd2b271 | -2.65515 | -49.40762 | 2024-11-10 01:19:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |


[Clique aqui para ver as próximas entradas](README12.md)

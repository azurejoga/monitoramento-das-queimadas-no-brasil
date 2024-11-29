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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baa45f04-14be-32f9-aace-8bcdcdfa071a | -2.8065 | -54.14538 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5694e3b9-3e58-3e90-be12-a29fee658e4d | -0.99332 | -51.72309 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10fbddea-2059-3315-8325-bbbb9bbff5f5 | 0.93815 | -50.73764 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58fe1e42-aa65-32e1-9145-b7b6507cdb70 | -1.69735 | -52.44669 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9f36ebbb-3816-3c7d-aa56-4858fc6ff8e1 | -2.98745 | -53.2899 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 0a9a8c1e-d4e2-35e7-bf49-8807ea41f2e0 | -2.84169 | -54.11547 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6767761f-9b05-31f1-9599-cd2e3ce7975d | -2.73662 | -52.58638 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02d03e1c-2dd5-31dc-9e58-14b7797bf68c | -3.31485 | -53.70012 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd2cbae4-9a59-312c-adbd-0ab73d90dc12 | -0.88204 | -51.71724 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26698836-0032-3302-a6f4-788d306be1c0 | -1.74619 | -52.09028 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cdef727-850b-3e90-b376-fb4bb0ee1707 | -5.22602 | -44.92335 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a280147-993e-3e38-844e-32217da17df5 | -2.85889 | -54.00526 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 477be608-ab4f-3dce-875a-ed9ee0234b10 | -1.06231 | -53.37866 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35c1b105-36d6-3d54-bb06-7dd5b6e8905a | -2.81035 | -54.14244 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b38f9cfb-0435-3e2a-810e-c00e563faa8b | -2.79597 | -54.12608 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 832eef18-8c06-34ea-9991-3fdd86419968 | -3.31341 | -53.75265 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 625572f6-ee5d-3e75-9c90-7e3af7095533 | -1.80504 | -48.77173 | 2024-11-29 04:57:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 16118ad1-aec4-32c9-923b-b6ac539c8706 | -1.09149 | -53.38666 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13542b30-b942-3434-b529-0c75745f1cb2 | -3.27672 | -50.61755 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb17575e-0074-383a-bc96-7f112570a3cb | -3.2382 | -53.93099 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2803f1c4-7f58-359a-bee0-bf982a41cb99 | -2.89993 | -51.37204 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8891c591-2441-34d0-b699-575559cb622d | -1.72375 | -52.49419 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 368b8629-d08b-3534-97c6-9a78b1fa2b37 | -3.6459 | -49.39611 | 2024-11-29 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cace3ae5-52b2-3ba5-afab-686a4a16fa9f | -2.77369 | -53.98428 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a2e7d78c-037a-3413-98a5-c9f49864b83e | -3.8187 | -50.95237 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1a219b3-c129-3cbe-9101-7edbf2fe0a63 | -2.74873 | -54.07917 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4a234c5-1aec-3b66-83da-8a3e26bd73b7 | -2.98717 | -51.32602 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce3af0ec-3fd3-3f6e-a47d-fdf9fe89757f | -2.91014 | -54.17908 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20a9ecdf-829f-3024-8d17-a06d65eb55ab | -3.18834 | -46.60692 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a65664d1-6bc7-3e5d-b7db-ceb5da446b5e | -2.29358 | -51.98034 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d715afba-abc1-3940-b98a-1e05bddf80aa | -2.65876 | -48.78218 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fa47bec3-2def-33d6-9488-2d35d8b65b21 | -3.4158 | -50.2487 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c786ad7a-dfe0-3faf-ad83-2a99d0328a60 | -3.23651 | -53.92017 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb95a8d-e57e-3b40-b47c-bbcaeee155d4 | -3.11821 | -53.26076 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98eb1a99-a6d9-3302-a08d-dc472b0c13f3 | -1.1885 | -53.87746 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 073750fe-62df-3036-8265-34792e50421c | -3.11196 | -53.99928 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfc498b2-7089-3871-bf91-3625703659aa | -2.72634 | -48.67231 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bb3ecc5-3e59-3d40-8d9a-12e4c5a5567e | -2.36403 | -50.42133 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae9e2f0a-4ee2-3bba-a1c9-3750e38b4027 | -4.50273 | -42.07557 | 2024-11-29 04:57:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0645d2a2-3b27-3305-b62d-6d64d76633b9 | -3.49289 | -50.45559 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3cbd69-0992-3e75-890b-daba108d6e59 | -2.80553 | -54.0217 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1150b2c6-9137-31a5-99ea-d1d3f713831d | -1.85461 | -50.81973 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86dfe5b1-14be-38ed-a095-247549ce748e | -1.69184 | -52.46014 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2173b332-0bf9-3339-9b61-852f1b9c4f0f | -1.31618 | -52.79577 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b701465-610b-3612-8e17-e6223fb3a55e | -3.37953 | -50.11364 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94dc084c-228d-3726-a577-c04a466a5ba1 | -3.92259 | -53.66529 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7237b681-b861-3eee-97fd-efac9f1ac146 | -4.04753 | -48.33181 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 870105dd-f339-37e0-943b-1c6d37798203 | -2.84699 | -54.05982 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d55c7dca-b7be-30da-992c-b68f53bc1ea1 | -3.07172 | -53.29585 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b55a8fa1-161d-37fd-81f3-60788d215755 | -1.48808 | -52.41464 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7469c346-a0b2-3f7a-9fa6-926006517261 | -2.9386 | -48.33796 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cce8f1ea-5c64-3331-8a9d-2deacd7f29e2 | 1.24854 | -55.99065 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7339c180-4977-3b59-a3fe-2e49b96f4d89 | -1.25478 | -54.54211 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12f758fb-f32e-3d4a-8074-2feda82f2ee1 | -1.57352 | -53.82836 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e5be580-f996-3da1-96bb-4774fee451b2 | -1.69964 | -52.47563 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a9538a6-5c04-3ecf-a71f-45aace54d718 | -1.62763 | -53.87551 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd7dad96-c256-3ee9-abaf-a3b43cecdadb | -2.7472 | -54.11071 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca033df3-a530-3999-a1bd-e4718c83dd95 | -2.01905 | -51.19097 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e6760a9f-8dc0-316b-9c2c-99c303ac9dd2 | -2.46051 | -53.70304 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f73a9e74-f86b-30e3-8a9c-753ea6c8b07f | -2.61847 | -48.16603 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cbe7f34-55f9-378c-9ec4-d8acf23807e3 | -2.46873 | -53.69377 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 949f575e-0c8d-31d6-b8e7-71362f2dfcab | -2.88751 | -53.99915 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17b3e010-ffe7-3da8-b446-2dab36b0bd0c | -1.04547 | -52.41695 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1906f7ba-c225-348f-8360-ec4e6783e7c1 | -3.49514 | -53.80961 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e930685-df6d-396f-b58a-0527500bb4d5 | -1.76879 | -52.70748 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d184aef3-a148-36f9-b129-9ef1240f0a33 | -2.8025 | -48.68399 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b78ebfe-80d1-3404-977f-4a4118c337c7 | -1.39527 | -53.55375 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 705290bc-ec0b-3128-bb53-b218f7d33019 | -2.86644 | -46.87476 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 107806d8-76fd-3d42-a623-9781f1f68eb6 | -3.07039 | -53.91488 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0dd1dd1-dd35-33d0-946c-cbf091a4950e | -2.77422 | -54.0486 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd10ed08-5851-361e-bacd-a1b035e0899a | -3.94927 | -46.72724 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e9b0394-253b-32d2-ae38-89aa9cd39d06 | -1.7055 | -52.76503 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 813ab7ac-7b79-3e07-8f4b-755b149cd526 | -3.21498 | -53.62126 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eefb4b9-7741-3590-8603-4bd8e0a178e4 | -1.32872 | -52.80531 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 862fbe83-893b-307f-8874-1d25881fa81b | -4.18905 | -50.68009 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a45fbf4c-fc3d-3043-b44b-55907549aab3 | -1.55646 | -52.02154 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb73705f-ad9c-3621-986d-3a44d51f94dc | -1.42847 | -55.27625 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfe0d052-8c08-36c6-852a-fffb963e340b | -1.93606 | -52.87836 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f294169c-4a37-3e72-b2da-2e9fd6d54e7f | -2.98455 | -53.89799 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90793862-db00-34fe-9567-294da5741d08 | -3.50237 | -53.82831 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 962f40b2-746b-3307-8a93-8174119f4d87 | -2.89394 | -53.95795 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a37cdc8-46fe-3ffd-9ecb-a08720ed13ce | -2.22753 | -53.23399 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af7670ba-9545-3f6c-b5a2-53d63af9e4d4 | -0.24037 | -53.76148 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 538d0279-7776-38a1-bcec-e42ba7b4d51e | -1.3097 | -51.92158 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65af667d-f31b-3da6-a966-b0dad93823cf | -1.05357 | -53.65133 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7f73e86-aca5-33f6-90a6-ea43ca9e6c16 | -1.3489 | -51.99294 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec0a1f08-5a17-331e-9e21-a483b67224ac | -3.09611 | -54.0356 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e991669-f8e4-32f2-80d7-fdd13b05def7 | -2.58726 | -54.06842 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 108cbac2-1809-3895-a7ab-9e87c9bd1b46 | -3.71173 | -53.75172 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b7de134-8420-3e1d-be73-483c9ff85189 | -1.10546 | -53.18876 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea26a9af-e621-374c-bdca-47404e513ca0 | -2.69388 | -51.98165 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5c0784f9-5c15-303f-9b8f-9af17a598577 | 1.64436 | -50.91715 | 2024-11-29 04:57:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2700c0c0-467a-3ddf-a4b2-57257a098fc1 | -2.58059 | -54.21939 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3f61bb9-2852-3165-986b-208e9fb385d4 | -2.83768 | -54.07602 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2508a480-b238-3c55-b846-842abd43ec39 | -2.58956 | -54.09705 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb146af7-48e9-3089-8eb1-5e29ece287be | -4.09589 | -50.33245 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 844b09a7-54e1-3ae8-aa11-b29ffc5b5dfe | -2.6778 | -46.15049 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53701b89-17e3-3015-bd9f-e949fd09e32f | -1.31391 | -51.73883 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faf5b346-762e-3f36-a6ea-8300621a484e | -2.86596 | -53.98168 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b49d05d9-f673-39cc-9cf7-9776cd99b594 | -1.34613 | -51.95271 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README42.md)

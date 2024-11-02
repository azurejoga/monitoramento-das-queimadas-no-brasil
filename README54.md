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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d96fd67b-7a26-3d84-9c41-49cf926d2289 | -3.0734 | -54.167 | 2024-11-02 04:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8564cc16-69d2-3519-9f4d-2f0a784fb1e9 | -3.1282 | -54.2459 | 2024-11-02 04:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 36438a87-009b-3062-8e45-6c6059bf09a0 | -3.1097 | -54.2865 | 2024-11-02 04:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 915a9b4d-abe2-3047-87e6-14faf18a8b51 | -3.1281 | -54.266 | 2024-11-02 04:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4dda0dd5-dc70-3bbf-a432-1c19b50c2f0a | -3.7701 | -43.5554 | 2024-11-02 04:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 094a7188-3816-32c7-9843-ea963d71a3c8 | -3.9473 | -48.3666 | 2024-11-02 04:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3613a1be-74de-35db-a924-3ae280cb1153 | -3.9474 | -48.3451 | 2024-11-02 04:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| e1d73ca0-9910-3f9c-8974-619462be2812 | -4.2032 | -45.8762 | 2024-11-02 04:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 0cdc9a4d-ab6f-340a-9a38-e4c58d5090fb | -4.3536 | -48.6283 | 2024-11-02 04:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| d268d26e-90fd-3a31-a0ca-645bf2a1bbda | -4.3537 | -48.6068 | 2024-11-02 04:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f977a1af-f3f6-3c7c-b54b-866baf212f15 | -4.4054 | -43.4746 | 2024-11-02 04:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3f961a57-6fed-3cad-8b6d-81d7be304ee9 | -4.5575 | -43.1162 | 2024-11-02 04:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 9362647b-89af-3dc3-9333-6a761469f4b2 | -4.5577 | -43.0928 | 2024-11-02 04:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 62d33d17-7f43-36d1-8cee-aec4dd50e885 | -4.5764 | -43.0916 | 2024-11-02 04:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ea736059-9ebf-323e-82fc-c9489b4da851 | -21.65697 | -42.11067 | 2024-11-02 04:17:00 | NOAA-20 | APERIBÉ | RIO DE JANEIRO | Brasil | 3300159 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 791acf6c-7b4c-3679-8ae3-95b3b34a3790 | -22.57757 | -42.17397 | 2024-11-02 04:17:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b7e7223e-ddab-34e2-af13-f3853eb99a8a | -21.17867 | -43.98125 | 2024-11-02 04:17:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83de78fb-17a1-360b-9166-1ad1eb2dfd0d | -29.81546 | -51.17682 | 2024-11-02 04:17:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 73a28d53-9627-34c9-9e0b-60ce693765bc | -19.68947 | -45.22985 | 2024-11-02 04:17:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bae963e3-84dc-3f7f-af00-8bf931d0a3ce | -20.98314 | -47.20991 | 2024-11-02 04:17:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b9c9a96-fe2a-35f5-8b5d-649c1b819cb9 | -20.4249 | -47.46211 | 2024-11-02 04:17:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70358469-5980-3fdb-ba67-3b032cf1a3ff | -21.05055 | -47.19167 | 2024-11-02 04:17:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65bb6551-d915-37f3-8d5e-419626a7cb57 | -21.04995 | -47.19539 | 2024-11-02 04:17:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da074b8e-e9e5-3c79-b96e-1b964b020f35 | -19.27226 | -39.89508 | 2024-11-02 04:17:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4f5d2803-75b6-374a-9a83-7a5798e209c9 | -19.26797 | -39.8945 | 2024-11-02 04:17:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e1cdca3-2da1-3b74-b6a8-674087cde77e | -22.85612 | -42.98264 | 2024-11-02 04:17:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 19b2467f-b117-3ac9-83cc-9067fd66c1d0 | -21.94924 | -46.4486 | 2024-11-02 04:17:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c0197c4f-0003-3931-8e29-189f180f5878 | -23.63173 | -46.42795 | 2024-11-02 04:17:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 117d92dc-c7af-34f0-81ea-c5cc812f1378 | -23.6102 | -46.83523 | 2024-11-02 04:17:00 | NOAA-20 | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0bb67f28-0beb-3b0c-9f33-038a2bb7ae46 | -23.58255 | -47.03493 | 2024-11-02 04:17:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1e980e88-4f6c-3171-8be7-b5040102b387 | -23.57379 | -47.0256 | 2024-11-02 04:17:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9d16e07f-c846-329d-88a0-02ffc7ac1269 | -1.4717 | -46.7214 | 2024-11-02 04:25:14 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d99b84bf-95f2-3781-ac79-7befb65f3566 | -2.2663 | -53.7422 | 2024-11-02 04:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f8278fc9-9a11-3580-8fb9-c80bd48ae59d | -3.0734 | -54.167 | 2024-11-02 04:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0dc08726-92ea-38a7-acff-b095112467de | -3.1281 | -54.266 | 2024-11-02 04:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a77b278e-8e28-3835-9b36-4f72641e2cfd | -3.1282 | -54.2459 | 2024-11-02 04:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e91d5d67-5dce-37c7-a001-542c04fd76cd | -3.2047 | -53.4179 | 2024-11-02 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 50047f1a-b014-383a-befb-a2552a3da336 | -3.2231 | -53.3972 | 2024-11-02 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c2e26361-4d64-30a1-97a1-735fbf700fa9 | -3.2415 | -53.4169 | 2024-11-02 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c2bb31b7-47db-3d5a-90ec-efa86df9aeae | -3.2415 | -53.3967 | 2024-11-02 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7a13b23d-9ebe-3984-abdf-003e7997b691 | -3.2599 | -53.4164 | 2024-11-02 04:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 6816c891-c953-3df5-a43f-48ab4270ff32 | -3.2599 | -53.3962 | 2024-11-02 04:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f067c111-3ed7-38e4-9701-4dcbb0b9c9e8 | -3.7701 | -43.5554 | 2024-11-02 04:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| fd1791cd-5fac-3c29-98cc-d600f4d0ef51 | -3.9473 | -48.3666 | 2024-11-02 04:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 592dd218-3129-3021-a012-5734ebd50a2f | -3.9474 | -48.3451 | 2024-11-02 04:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d036da5c-a8bb-3c1b-860d-4c2d52984b29 | -4.3537 | -48.6068 | 2024-11-02 04:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 61557558-3d67-3580-ba3e-0de0b6c57a37 | -4.5575 | -43.1162 | 2024-11-02 04:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a13e006c-a6c7-3a87-aafb-b23fb46c2f17 | -4.5577 | -43.0928 | 2024-11-02 04:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 40a34194-66dc-32da-ba2d-0a0c4d61dc0f | -4.5762 | -43.115 | 2024-11-02 04:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 557b08e6-bf1a-3d54-896a-ed38f80105e0 | -4.5764 | -43.0916 | 2024-11-02 04:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| f2f0d6ec-9321-33ae-975f-5adbb6f53ce7 | -2.2663 | -53.7422 | 2024-11-02 04:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| e8a17f2f-98da-3ee2-b1b1-a8909876e3f1 | -2.7795 | -48.7307 | 2024-11-02 04:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 80ebd4e0-17da-3518-bd50-3855c530ff90 | -3.0734 | -54.167 | 2024-11-02 04:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 19b2dda3-df0d-3b16-8a0d-c8845f3f988e | -3.1282 | -54.2459 | 2024-11-02 04:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4a964f8c-c710-3148-a965-b09e45b147d6 | -3.1281 | -54.266 | 2024-11-02 04:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 5d55ae82-3cd7-3c97-ab1f-a9cd2061b615 | -3.9474 | -48.3451 | 2024-11-02 04:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| f66a5287-7237-388f-ba42-74fd5c4c2b3a | -3.9473 | -48.3666 | 2024-11-02 04:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a406fb52-80fd-3fdc-b524-9babb0d96e1f | -4.3537 | -48.6068 | 2024-11-02 04:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 4ca71992-25f0-3d68-b8c3-f3f3de6c0a06 | -4.5764 | -43.0916 | 2024-11-02 04:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 7c9d7e17-8d26-3527-a5e1-eb94cb57945b | -4.5762 | -43.115 | 2024-11-02 04:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 471e6978-dd4f-3be1-a005-dc3dc6ea11a2 | -4.5579 | -43.0694 | 2024-11-02 04:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 7e4fa5d8-709b-39a6-804b-248b94f35a45 | -4.5577 | -43.0928 | 2024-11-02 04:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 275.8 |
| 55bbce46-dbbb-3e1a-9b9b-437513699392 | -4.5575 | -43.1162 | 2024-11-02 04:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 43d96967-c4e9-37f2-88d6-d7283f7cc435 | -1.2014 | -53.9184 | 2024-11-02 04:45:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 5a5118b4-72f4-3c3d-9654-cd619c73feab | -1.4717 | -46.7214 | 2024-11-02 04:45:14 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6d9423f8-4447-35fd-b93e-f71e870a410b | -2.2663 | -53.7422 | 2024-11-02 04:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4b191765-1922-3a06-8ebe-4808a9fb2589 | -3.1281 | -54.266 | 2024-11-02 04:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5c981835-0e37-38f5-b41c-0ca1215e3787 | -3.0734 | -54.167 | 2024-11-02 04:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7546ef8e-6f29-32e3-ae20-09cb996ab7b4 | -3.2599 | -53.3962 | 2024-11-02 04:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 293f2ee1-14cd-3f8e-9828-bf7d1264163e | -3.2599 | -53.4164 | 2024-11-02 04:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 7b8fc5fa-0734-3a85-8c55-8107c2ade5ce | -3.2415 | -53.3967 | 2024-11-02 04:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f77eb6b4-f7f6-3d38-9910-93b5b9a60051 | -3.2415 | -53.4169 | 2024-11-02 04:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| fc17a451-8e76-38e7-9ba2-d357d8b38a3f | -3.2231 | -53.3972 | 2024-11-02 04:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5e41074f-3775-3c05-a83d-6ce8c963cc33 | -3.2231 | -53.4174 | 2024-11-02 04:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| cbdcbdba-391a-307c-81b3-ae49ec6fdaff | -3.9474 | -48.3451 | 2024-11-02 04:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ea629af6-9a0f-3fc5-823f-b1784cc6f09d | -3.9473 | -48.3666 | 2024-11-02 04:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| d13ff374-7065-3fd8-93b1-951dd9e8f3bc | -4.3537 | -48.6068 | 2024-11-02 04:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 178ee677-1ae7-39d7-817b-774552db02e7 | -4.5764 | -43.0916 | 2024-11-02 04:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 639c697e-fc6f-316d-a735-62c8f38c8cd9 | -4.5577 | -43.0928 | 2024-11-02 04:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9baea97a-59bf-3363-bfed-5a0beb83f980 | -1.2014 | -53.8983 | 2024-11-02 04:55:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 84773185-ce5c-392b-a3ba-b1f60e85390b | -1.2014 | -53.9184 | 2024-11-02 04:55:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 2c93f370-ebce-347a-90c4-21fa95b095ad | -1.4717 | -46.7214 | 2024-11-02 04:55:14 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| d27cdb7f-a197-3f5f-b3f4-30fb79103cb7 | -2.2663 | -53.7422 | 2024-11-02 04:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2a606805-a790-3e96-a414-f01e4a47b796 | -3.0734 | -54.167 | 2024-11-02 04:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 012510b7-5bbc-3a35-98cb-452737f2b60c | -3.9289 | -48.3458 | 2024-11-02 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 45d2c553-db80-386b-be93-5a6c7b9962cb | -3.9474 | -48.3451 | 2024-11-02 04:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 9b6eaec1-ac1e-3f32-8246-7d8c1f9dd1be | -3.9473 | -48.3666 | 2024-11-02 04:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| cc25ee21-2c29-35f3-a2a8-0cfad2317c35 | -4.3537 | -48.6068 | 2024-11-02 04:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f0351187-7ef7-31a6-bb5c-10f44a4ec5d1 | 2.33273 | -50.80541 | 2024-11-02 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5aef1f0-182d-3974-adab-9a6234dd947b | 2.27843 | -50.76374 | 2024-11-02 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c735c885-10a6-3895-937a-24ea6a716451 | 2.25943 | -50.84526 | 2024-11-02 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5404e565-6122-3608-a954-b7a1162e23fe | 1.07647 | -50.95349 | 2024-11-02 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b49b6133-c9bc-3ac6-917c-6f0f7a81d3f2 | 0.84514 | -50.21222 | 2024-11-02 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feab52eb-4cb7-3901-98ba-fa158534b8e3 | 0.82776 | -50.22424 | 2024-11-02 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a268a79e-bb92-3f93-99d5-b4f0406d34d9 | 1.85089 | -50.50894 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fb821ed-adf8-3edf-8ffb-4a37ed302bfe | 1.85021 | -50.50467 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6d8346e-9820-3e90-b663-4f1599076f52 | 1.83106 | -50.91174 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d22247a1-2e6f-3de5-9998-7c7439912139 | 1.83043 | -50.90767 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41ee8b53-4790-32b8-8cbe-647853198482 | 1.79546 | -50.4431 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 372c8ac3-06c1-39cc-b592-29386f979604 | 1.79111 | -50.43937 | 2024-11-02 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README55.md)

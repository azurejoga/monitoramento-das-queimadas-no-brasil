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

## Dados Diários - Página 229

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebffd712-49d7-3049-a9ef-9261a03e7eef | -2.76117 | -54.09721 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c793cfba-754a-3ad0-a6e1-b23dd5c7a705 | 1.34977 | -56.13514 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eb6534c5-863f-36e4-b84b-85d95fe1ad36 | -3.58934 | -55.56373 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 820e1565-9ef8-34de-84b4-3031025642c1 | -3.8421 | -50.31283 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c1b18198-615c-3b37-82f9-a50191f912c8 | -3.0312 | -57.48558 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 7081ea75-f327-3531-8ca3-f04735f985bb | -4.08074 | -55.3327 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 989b68b4-3a46-3744-a8d2-2dc4583232ea | 1.96036 | -55.88813 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 09947c58-1b23-388b-98db-2baebd24cfa8 | -1.47957 | -54.77409 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6749a4ae-3d5f-30f0-9901-0bfce3bdca96 | -3.44761 | -51.08835 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fc9c87b2-51d8-3bb9-9125-ba858f07bfeb | -3.02138 | -47.46597 | 2026-10-07 16:39:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8b5d6e91-d1d2-337e-a459-9afb2d21a080 | -1.24879 | -55.70638 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 168d6e42-8f92-3d9e-9fee-ed915233c550 | 3.21781 | -51.31429 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8c028fc7-d5dc-39b8-82ce-292aa08d419d | -4.5383 | -55.61403 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 2fd93f19-9fcf-3c1b-83ae-d9ee623e9016 | -3.30275 | -54.04093 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ea5101db-8425-31e6-a615-28801f614a02 | -3.53578 | -54.64936 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 82df4e66-746e-3a3f-b660-5c4af7b01fa2 | -3.27325 | -54.06617 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5e5c00ea-3e3a-3f30-aa7e-c715a33f8eca | -2.51633 | -56.25219 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 03f34638-6958-35c1-bdf8-0c8f26c2fe0c | -2.99171 | -42.83417 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 607c651f-092f-3c0e-b5a2-4d77583b844b | -1.86221 | -44.91102 | 2026-10-07 16:39:00 | NPP-375 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e79f64ef-1798-3885-b7c0-601681ed3ea8 | -3.08877 | -54.30342 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 11bd5ce2-7421-3175-ac4d-98e99e44914a | -3.30175 | -54.03413 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| f34b4e38-cf5f-30ae-b1fc-8dde8114b875 | -1.99947 | -45.08023 | 2026-10-07 16:39:00 | NPP-375 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4e888af-01be-3741-a532-ca08c0f66018 | -3.12863 | -51.14422 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 906d8a01-461e-3296-a1da-0cb1f50accad | -2.83896 | -54.12804 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| eb982f95-0575-3031-92ad-0969bbcfee64 | -3.1816 | -50.5624 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cef9a1d2-d314-3508-b46e-fbed78c8a96b | -2.78466 | -51.67559 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9b6397f7-8180-3d59-a9e8-455deeb5817c | -3.81201 | -51.04306 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1e266ea5-7fc5-3bdc-9f60-b137eed1d74b | -1.62735 | -49.39066 | 2026-10-07 16:39:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 108826d2-a5e2-3cfe-94b4-1ed726955dd5 | -3.54306 | -54.66 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1db952f2-2b7d-3307-ad45-98cf7ad7cc9d | -3.01485 | -54.07037 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| ec9a8584-e83c-38d2-88e5-9b0c88b4aab4 | -2.97988 | -57.67239 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 74c8d4cc-ae2e-3ec1-a073-443eac2b146e | -4.00264 | -56.2581 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a5675355-55cb-3a96-8112-608e51d07763 | -3.05537 | -54.26586 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e5222cf0-50ee-31dc-949c-04f9d215f32b | -2.93751 | -53.2268 | 2026-10-07 16:39:00 | NPP-375 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b8bc63c4-40ff-3ada-9db7-7d4010bde530 | -3.85364 | -50.41923 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 7aa75a8c-114c-3b7a-849c-7fe479b60797 | -3.58276 | -54.65472 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 325f3fd5-7aa3-3137-9b50-9e54eca95a3f | -1.28359 | -56.9815 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c815a8e4-4b8e-3149-97cd-5ce198d0fa25 | -3.65531 | -50.95044 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| e62bb82c-b010-32b0-bca9-f705b065a8c3 | -2.78464 | -51.67872 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 158a9368-bc1b-37f8-8e33-21d55b2b844b | 2.10714 | -50.9624 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e361d157-d6ec-3bcc-8722-2e0146f6e0a4 | -3.79149 | -50.87267 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| afbcb151-ab1b-34f3-9fa4-cc0e9ef7d1c5 | -2.93662 | -54.15253 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 5dba4367-1ee6-350e-bb6d-a1c814639aed | -3.65431 | -55.50493 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1291f330-6f00-3e4c-9c37-42ec5b32651e | -3.08656 | -54.24958 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 94e632b2-8825-3156-8727-59fac0265f61 | -2.57337 | -54.01365 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b77b57dc-a858-3df7-ac6a-3330d08c26cc | -2.82421 | -54.10228 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4aa5f9f4-6e5c-33dd-ae61-edf2072deaae | -3.08211 | -54.29474 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 1608dcda-69a8-369d-a0fa-0b6837dbb408 | -4.06102 | -55.32213 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| e6f27273-3d3f-33f8-812e-f366022b5109 | -1.16738 | -53.18915 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 72195844-bcc6-33e0-9294-af2537fb4992 | -4.15708 | -55.14845 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 44367ac4-dd1b-32f5-9420-0779c0608750 | -4.1329 | -54.90443 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6c2bb8b9-7df1-34b4-a98f-c8f3e5f199b8 | -3.01784 | -54.23919 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 87a1bcff-177e-38a1-b46e-7c96aecacc8f | -2.80886 | -52.08848 | 2026-10-07 16:39:00 | NPP-375 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 91bc3d1e-5751-34f8-a728-d9691f912f5d | -3.03686 | -53.90777 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a21663df-c59b-369f-ba4a-8bf4c554632a | -3.1087 | -53.76976 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b05c785e-3702-36b6-b3f4-19cf6d2667ce | -2.93818 | -54.16283 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 923b0098-3f45-3917-9fd4-bb5140642f97 | 2.12484 | -50.82448 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 2daf82d9-4936-3da7-b9e2-5e7de7995a69 | -1.71586 | -55.43246 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3a2d3a78-4a3f-3b0f-acac-4e2a94aa6abd | -3.65546 | -55.45687 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 460c4525-b377-37a1-bb19-11253ee99fbc | -2.50389 | -56.13487 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| dbac64eb-ffc5-3abd-b014-e128c4303fd6 | -1.49944 | -49.57748 | 2026-10-07 16:39:00 | NPP-375 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff726ae9-31a6-3e78-ab80-c420343773c9 | -2.24635 | -56.24633 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0c07f437-5e1b-31d0-9557-c7c1e862210a | -3.03586 | -53.93846 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 97b739a9-58df-3ad5-af18-dba7f704bcd8 | -3.5474 | -54.66405 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 9749b664-382e-3172-a751-16719a12760c | -3.44803 | -56.94712 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 169.3 |
| d74b419c-97f2-3d7d-967e-acb7b789fbf5 | -2.3915 | -56.13201 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c8c0d689-208e-3707-91d6-983cc3218d44 | -3.06275 | -54.20412 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fd2fc331-74c9-3f52-bf6a-b27a71bf226f | -1.15001 | -46.5748 | 2026-10-07 16:39:00 | NPP-375 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b51578c2-d34a-3c2d-a8a8-5c2f9153ed59 | -3.7209 | -55.48769 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| ad6182bd-3800-327d-a0d4-db1845a97d0d | -1.56801 | -47.73938 | 2026-10-07 16:39:00 | NPP-375 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| d05dd7b6-a4e2-313f-b74e-37ca12fe82b0 | -3.26827 | -54.03177 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1a70a0ea-b2a4-3e43-84fd-5d73649e09b4 | -3.7917 | -50.75348 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1837dc86-eaf5-394f-a462-4782acbe81df | -3.02771 | -54.23055 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ae4d4050-974a-354d-9547-77b9fa4cc609 | -3.49702 | -48.13964 | 2026-10-07 16:39:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0197707d-1c6a-36cf-ab9e-427155d8742c | -2.94122 | -54.05677 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 94fd8158-88f1-3778-a9a4-be3a312106bd | -3.28875 | -50.44006 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4f5ab838-5920-34f0-96ec-58df7b8ae714 | -3.26439 | -54.04307 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ad963343-0616-3681-92f8-6f4c9be13d36 | -3.07735 | -54.148 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ad34163e-e435-3cb5-b9e3-371fc4493b80 | -2.14046 | -54.4579 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c3b12dcc-81fc-3c79-862a-f5b6442656c4 | -3.0792 | -54.27599 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| faee4912-72c6-3cf0-ac4e-80c75b397500 | -3.99558 | -56.25396 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cc522194-a55f-3ca0-afb4-915dd5593fe3 | -2.18685 | -56.10413 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3deddec9-4228-3189-a3cf-b5642e7e63b6 | -2.84878 | -54.11966 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bb9f225-5640-3f28-9ce0-af2ab35a65d6 | 2.46366 | -50.85781 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8ea8cd7d-0954-32f6-bbe1-884d8bc0922d | -3.32164 | -57.69871 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 45c2fcf2-e869-3b32-b789-043a908621ca | -2.79045 | -54.07215 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 417071a4-d014-3b7c-ae89-a3dcaf8d3831 | -3.65496 | -55.50932 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7372fd60-57ca-3b78-b3ea-7d8a858c865f | -2.68756 | -44.29851 | 2026-10-07 16:39:00 | NPP-375 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d68ad1fc-5d64-3b5f-a457-196bafb7bc14 | -3.54 | -50.10056 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f1f3cb0c-e2f7-346f-b14b-b26632c1be76 | -3.57653 | -54.65159 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| ab1c8894-bb0f-30bd-ab41-79122d250760 | -3.30212 | -57.85374 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cade4cc0-7945-3397-8e46-7434568468ad | -3.2712 | -54.01392 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| da0f1239-d1da-3267-bc65-92d585d00e63 | 2.09451 | -50.964 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33c81c3f-f441-3a1a-9a5a-7ced0b9606b1 | -3.0684 | -57.75354 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e0ceb530-f0f5-3378-a0a8-a519447de777 | -2.81008 | -57.05112 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6cae2be5-8e5c-339a-a95d-6e9086a8827f | -1.42217 | -52.85312 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d75bf4eb-d5dd-39a3-b139-39dd4b833c3d | -3.53378 | -54.65024 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a180f7a0-aebd-319c-b41a-7116fe444215 | -3.01822 | -54.05605 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 7adc17dd-d05b-38fd-8d4b-1e539eb0effc | 2.33023 | -50.81444 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0894f294-a9ab-37ea-a8cd-31b9afd3fc8a | -3.50469 | -51.68303 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |


[Clique aqui para ver as próximas entradas](README230.md)

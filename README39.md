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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaa77565-3977-3d8b-a588-0ed33f65d34f | -3.11432 | -53.70448 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7e7022e6-217b-3680-b75a-0d49a89e41e1 | -3.59167 | -54.31726 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02ccac29-4ae4-3f10-b251-c0e323a9108d | -4.45452 | -54.96947 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42c0e632-6691-3041-83f5-4e9ea50c79c9 | -2.25418 | -51.93584 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef0b86d9-9156-347f-a582-c26db78e18a4 | -2.8203 | -54.11714 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d560499e-37cc-31b9-a21f-8729ee7a2b3e | -3.184 | -50.54145 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dc08e12-3ad7-3f7f-8551-7670703c68fe | -2.98334 | -54.04242 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb7cd0b8-f21e-32b2-b8c6-e8a3a8909de2 | -2.89652 | -54.07841 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63de38dc-5599-3c64-ac78-9e09bb83b522 | -7.43202 | -63.57267 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 805d9e09-5831-3e31-bcf9-e2ee1f5905ad | -4.05051 | -51.07719 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a483e41-6f97-319e-a9d7-f13d6e511195 | -3.0589 | -54.16134 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93d32347-07b2-35f5-8220-60a12072428f | -3.2768 | -54.18011 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 56546cbb-e0f0-3e62-ae89-ce22896f5eec | -2.98534 | -54.09639 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e93735e6-7dad-34f9-bb26-9f86940f4069 | -3.86672 | -53.41544 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b600ae7-0655-3c9b-aede-081d1055dc77 | -2.36524 | -55.27004 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e13b21-4c4f-3e2d-aa6b-f02281bee5c8 | -2.99695 | -57.79293 | 2026-10-05 04:57:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edb56ef8-5be6-3964-b7d8-0b7cd30b0fa1 | -2.68882 | -54.64254 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c74f024b-968a-3801-a39d-96c6de63da23 | -3.71006 | -50.65168 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf3cf6ce-6bde-360e-b9d6-10c8c17695bd | -2.8868 | -54.13843 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19449dee-002d-3c48-ac2a-acfdbad85756 | -3.04177 | -54.22429 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6f98582-4e37-3920-8886-ad3b050ee209 | -5.23064 | -48.40843 | 2026-10-05 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8ab7ef0-da4a-35a0-a0dd-7f1236fdf5f5 | -2.99104 | -54.10497 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 32a3c580-48a0-3884-be73-bd5b54ddf527 | -2.48269 | -56.08962 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49bcca8d-9481-34d7-8664-da03e4c17499 | -2.77954 | -54.10683 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0825eab-7a07-3fdf-9a7f-9c06424bcc2e | -2.57293 | -56.15434 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d426a898-4e83-37cc-84be-b12d42c9a81f | -2.95259 | -54.1027 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62b78b9c-c404-39a5-bfc9-8afe02e25e2f | -3.05049 | -54.21406 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d4f0339-da74-34d2-a11f-ca27c7f0b620 | -3.32255 | -53.84926 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48874ace-a606-3810-99fa-ad09b204cc5f | -8.52961 | -54.5801 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81654726-05f6-3d35-bbab-158aaa05e387 | -3.22115 | -54.30656 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14ec9706-3353-37a9-9193-d180f9cae844 | -3.37888 | -54.11178 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b6632eb-296b-3bae-b92d-b7e2f3956806 | -3.05093 | -54.23349 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e6c840a-543c-39bf-82a0-61dc1b939790 | -5.80648 | -52.75943 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eb8918c-6e44-391a-ba7f-c7601cb87234 | -4.11789 | -49.06933 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59a0202f-279b-356b-8032-3065bc5c48c6 | -2.58442 | -48.43525 | 2026-10-05 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3832a4d-f26e-3df8-8848-bb8b103c0562 | -3.0571 | -54.17263 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4abc7aa5-460b-3c5e-91a8-41939736b0c4 | -3.70144 | -54.19936 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfafa99a-e8a9-3b31-b8c5-601e076f4a78 | -8.66824 | -54.54366 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4179fa63-0338-3fca-bcb8-79657e5c49c9 | -7.22116 | -55.20626 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2200b825-80e7-35b3-8eda-956a3dadcdba | -3.612 | -54.60159 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 466ce56f-858a-36fd-be43-3fc5854e77a4 | -3.09952 | -59.74054 | 2026-10-05 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 566cbb92-3d38-3853-a752-443b13ed1506 | -3.28631 | -53.83602 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db1c1f6e-5d1c-3e77-b328-448913c95635 | -2.22238 | -53.71243 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27b20096-b569-3e59-a8d1-e0572478a387 | -3.04704 | -54.21351 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f712ee0d-2d88-3603-a166-ed7c308a65d5 | -3.55949 | -50.29284 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67da958b-e1b6-354c-a983-8e73242905c9 | -2.31014 | -48.63656 | 2026-10-05 04:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bc4bede-94e6-343d-bea7-b1531dc6a21b | -3.62531 | -55.28325 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd40e7b5-8c4a-32af-8646-f5a69c31e002 | -3.09843 | -53.71687 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 179cff91-5a2d-3984-8318-e9ff83215f7b | -3.04808 | -54.22916 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1552e04-dc05-397a-a379-3e818a0d6f50 | -6.90594 | -43.67724 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e9236f6-0d7c-3d7f-9273-fcf4639ad9ff | -6.00658 | -53.50967 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9fc46c7b-6182-3597-a5e3-7d4d1a0c02cf | -3.58943 | -54.30915 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aa04a11a-9c2e-301b-b98c-5513ae36481f | -2.85466 | -51.29586 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6abfbace-b8fd-3018-bf68-112ee0bced18 | -2.91698 | -54.10472 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ff8e863-24e9-313c-8acb-8fe56f962872 | -4.26187 | -50.7952 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 65e624f2-12b4-3d49-9a42-03eb79304bdf | -3.31011 | -53.83979 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ff399c6-a932-33cc-a2fd-8c1ebe4db385 | -1.51915 | -54.82408 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 57b6112e-ce7e-3270-859f-28effcf2088f | -3.33388 | -53.38949 | 2026-10-05 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 306e9373-4f9f-35b0-a15c-7b6e9449069b | -8.66431 | -54.54669 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f14cdb36-47ad-3067-829d-370b8b2ac6e8 | -6.26005 | -52.85629 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09ff026e-5c6a-3bd1-a438-57db0f215ea2 | -3.30155 | -53.84968 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb23aec4-a118-3a59-a384-7b80282b4c5a | -2.09444 | -56.62424 | 2026-10-05 04:57:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec55200e-1aed-3e59-a88d-c89e16ea773a | -3.122 | -53.76542 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4718e7d8-1091-37c3-8522-f1faec10d22f | -3.27383 | -50.39591 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bef45cba-8eb7-3fd0-a49b-ea6b6cb61514 | -3.84639 | -50.31752 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 08f257d6-acfc-33a5-a99a-62c0040cc689 | -4.46279 | -54.96288 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c79cb6e-4f60-36a0-87bf-12b7b4561851 | -3.11142 | -53.72266 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af33551e-a730-3555-9152-b3703a07ad44 | -2.81056 | -54.11173 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98703856-df60-35b5-9845-02646a9b7167 | -3.71401 | -50.64859 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a315260-6663-395d-bb48-9211205ee12a | -2.82133 | -54.13276 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b586a88d-54a8-395e-a7ce-291b65e16c6f | -2.93435 | -54.08442 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40b102ef-49c3-31d6-8a93-cc6dd6ee23a8 | -1.37504 | -54.64166 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b23fc2a-90d7-3b85-a270-0edfd98dd14e | -6.00158 | -53.51964 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97d0ac34-5f62-321c-8079-d56b99ba6753 | -6.91622 | -43.68203 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f61c3108-803f-3371-b09a-4f0bc6d04171 | -1.61475 | -55.1398 | 2026-10-05 04:57:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 683646a2-5980-3c1c-aaca-d0f0083b2418 | -2.16259 | -53.66951 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd309ef2-0105-3b29-a421-ec7b5540a5b2 | -5.93762 | -57.73751 | 2026-10-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 84cb1119-46f2-31c1-89fb-f557cd6ef649 | -8.65866 | -54.56045 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cbb992d-18d1-3763-84e3-4322d642b3f4 | -3.46621 | -50.10456 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06459502-ef10-3cce-abb0-e217d7c7b7c6 | -1.42156 | -57.85268 | 2026-10-05 04:57:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27b87287-dca4-3566-9ffb-39a936d4b46f | -1.88447 | -56.28364 | 2026-10-05 04:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3babb3f5-f74e-36f7-9651-b48f6e750cad | -2.88619 | -54.14221 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54d341b2-ed55-35d2-aee6-02567bc04962 | -2.97278 | -54.08671 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96c881fb-9bce-32c4-8d7e-c89f2674d116 | -3.927 | -56.17467 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6ac961f-2b88-3cb2-ae08-263e2d67a587 | -3.11026 | -53.72994 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1e6f146-c82f-38a8-8c76-da8bf34603a9 | -3.89593 | -56.03475 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c58d0dd-9ba5-3f48-ae5a-ef81229784f7 | -3.11771 | -53.70502 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2048b928-c294-3152-84cf-ff3ba35fb199 | -3.0583 | -54.1651 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f9d784e-8cc9-3b50-902c-70098a92b74e | -7.22647 | -55.19545 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5888cfa-b642-3274-b3a6-541e899d7dae | -5.82281 | -52.03236 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 826b176e-efd8-39bc-b6c2-e0a1ceecd7a1 | -7.23338 | -55.1966 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 705be373-f2d3-3388-9a71-e73e2a8c0041 | -3.29315 | -49.12551 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ca36f36-fc13-3b77-a5cf-7ab9f3346283 | -3.84014 | -50.31269 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4dd9897e-d958-3af5-a184-e512602f6329 | -8.52903 | -54.58369 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c82f49e-e1d4-36d2-bcf4-cfe3a362bc40 | -3.07837 | -54.17218 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d3554e4d-0e1e-3795-bddf-6df4c52f96bc | -3.10405 | -53.72522 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84343bfd-319f-3237-9908-8628be4298b8 | -3.7232 | -55.97371 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1978f7e8-63e4-3a4b-8569-c4a76223d6d6 | -4.11169 | -49.078 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7218cb4-3787-346a-b83e-fadd3b3eca6d | -3.30378 | -53.85753 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e380e88-6c6e-3799-b62a-219e642b79b5 | -2.87972 | -54.07657 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README40.md)

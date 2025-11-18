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
| 65ba76f4-5af7-3a3c-8924-57cdd3177825 | -0.83175 | -48.6423 | 2025-11-18 04:48:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 430629af-a7a9-3522-913d-2ae198cb1e8c | -5.42961 | -43.05085 | 2025-11-18 04:48:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 851199aa-b629-33a1-9438-0b7c203c6627 | -3.42991 | -42.42443 | 2025-11-18 04:48:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ecd110c7-ab74-352c-a043-63c22212d3c6 | -1.19512 | -48.93284 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7404890a-9455-3efd-ab1f-8e1119cd1ea9 | -3.08385 | -48.13233 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7a8093a-e402-37d9-85ea-d168af40e170 | -2.51624 | -47.81521 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fae24e29-e958-3c67-8374-af1795cf93c7 | -5.83564 | -47.8384 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 417e8959-7e93-3ac1-8103-ab09dce440ab | -3.14729 | -50.20337 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9880143b-98c2-3259-ae8e-f1e83dc6b993 | -3.51411 | -50.34592 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff7ddb85-5b79-3580-9a0a-942938a05112 | 0.23594 | -51.02335 | 2025-11-18 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f9c3ef6-d6b9-30af-a1bb-03ce991909a9 | -1.42987 | -48.90434 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5c06b42-5648-3aa6-be96-8eba13074331 | -4.27341 | -44.24416 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95fab2c2-5422-381a-82f0-cefea5cbaa1c | -1.42318 | -48.90329 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54cd9134-a9de-38b1-9ea6-f8802dfe8297 | -2.8108 | -45.14797 | 2025-11-18 04:48:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc5d5575-b39f-309e-9176-dc10359ba9e2 | -3.16992 | -49.80349 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 589f2954-2089-3305-a0cd-0c7c234607d9 | -1.33628 | -49.32529 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c4f3bfb-e56c-3adb-b900-789eeb6f4131 | -3.58367 | -50.42054 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2308124d-9917-306a-801e-9d6a27f1b406 | -2.38338 | -45.73832 | 2025-11-18 04:48:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c133efb-ddf5-3e01-ba76-a7fb24895ec4 | -3.64284 | -50.8366 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1438109-5acc-394e-bf27-68c2855456c2 | -3.23954 | -50.49674 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e821fe6c-cfcd-3fc1-a57f-abbbbf86761e | -3.17536 | -46.60099 | 2025-11-18 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 430509f0-161a-3c4a-a5cf-86fda5f849ca | -3.13581 | -50.25454 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 765acce9-ae38-3e78-8ecc-de3797b71ead | -4.17917 | -44.24414 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4553fd3e-5718-37d9-aa6c-ddf2be4195eb | -4.67774 | -45.80027 | 2025-11-18 04:48:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6684e5b-5a72-3d28-ab9c-f509e141d69a | -3.69702 | -52.6506 | 2025-11-18 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52a72f7b-1a63-3a4f-b62c-d7b749d0d56d | -3.18782 | -50.65136 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 276d9ccd-1e0b-3d3c-b932-e4226950bfe8 | -6.67302 | -42.03217 | 2025-11-18 04:48:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| cbc5ad54-d004-3c2f-a955-ff571cf00290 | -3.12428 | -50.17844 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9952634-6e37-3036-879a-6023d92f476b | -6.7091 | -40.79361 | 2025-11-18 04:48:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d8a1d11-731c-3239-a84b-295ea0ecf71c | -2.50867 | -47.81792 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea7dabbd-50a3-32d2-8c5a-174bce5cbdac | -0.98014 | -52.44629 | 2025-11-18 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fbdebc1-b5e5-3274-a1fd-ba6bd30e901b | -4.44288 | -47.99459 | 2025-11-18 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f178cc8-42c6-3720-9a46-e2c8b721a7c9 | -3.71649 | -52.11072 | 2025-11-18 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e87a160-31f0-33af-b5a2-6a48003dea1c | -3.02506 | -44.46285 | 2025-11-18 04:48:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd667b61-5a51-3d53-abb6-a402c3e66eb7 | -0.8284 | -48.64178 | 2025-11-18 04:48:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5672d1c4-59fc-32bb-aad7-2f3455e4812d | -6.41148 | -47.19768 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d502e06-4ad8-3516-9cf9-8d44beb4fafc | -3.34961 | -44.39469 | 2025-11-18 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f2373393-d6f6-38cf-8db2-94c1ff6278a1 | -4.14105 | -46.76735 | 2025-11-18 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7c12620-e04d-3a58-93e0-61be38ce9019 | -2.99534 | -51.05879 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61c196cf-6995-34ff-895c-c07bd477c725 | -2.82813 | -45.41685 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 734e6cd0-7403-30b9-8400-f7c6e21c4a31 | -1.12213 | -52.14571 | 2025-11-18 04:48:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3bebb66-301c-3c41-89b6-b3b66c82e6e3 | -2.99776 | -51.05924 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93422799-a335-31ed-90af-fce9fe9a67d9 | -6.30741 | -43.79106 | 2025-11-18 04:48:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1b530634-d7ff-3abc-934b-8ac1783c2772 | -5.42471 | -43.05025 | 2025-11-18 04:48:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e99a7ab6-dc4e-3d95-aaf8-c9ea26227bb7 | -4.1905 | -44.22846 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b5e9dd71-04da-3f70-a3ec-fda1a3c68a18 | -2.29463 | -51.78183 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bd4d47a-dd1a-3acd-835c-1ab04575a6a1 | -6.20768 | -46.88728 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60f42fcf-764b-32f4-9b39-96e359bf7d0a | -4.31221 | -46.70389 | 2025-11-18 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e93de66b-8390-314e-915c-f8e0d9f9eb76 | -2.47529 | -48.22439 | 2025-11-18 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2d4d180e-24dd-3bc5-af8d-a727fe0565e9 | -3.51674 | -50.28627 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a87627bf-2d56-3874-b4f6-0ecfdd9c9f61 | -2.47185 | -48.22387 | 2025-11-18 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73f6cf28-d0ba-3d31-828b-fcb1cc582bad | -3.75486 | -50.94357 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a3f9c74-dc1f-3a30-8ec9-fdbf5df1e3d7 | -2.99972 | -51.00941 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28495f20-e0eb-305a-93da-184e7342d190 | -4.64109 | -45.65189 | 2025-11-18 04:48:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a85b204a-5768-3699-9d2d-64949771e91a | -4.67542 | -45.80371 | 2025-11-18 04:48:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 345b97ab-3fd5-345f-9571-6e05d0bd928e | -3.22656 | -50.06738 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6ae3473-8268-39cf-888a-5ded254e1d83 | -0.99222 | -47.07268 | 2025-11-18 04:48:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 38e86754-4e76-3ddc-ac96-04013cc54fad | -2.29438 | -47.23278 | 2025-11-18 04:48:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a278427b-ab5a-3e87-8c2c-da8e9ecb3d5b | -2.3795 | -45.73772 | 2025-11-18 04:48:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 143ce987-78f9-380a-9c00-cec44dee1e58 | -3.25096 | -50.68252 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fe24a07-696a-36a1-922b-0b2fb6efeaf5 | -3.3011 | -53.84952 | 2025-11-18 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a008a91-49e2-3bf4-b2f5-886018b037a8 | -3.80984 | -47.49497 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9192e6d4-11df-3c39-bc34-0d00ff3abd6f | -3.16283 | -51.48938 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f09b567f-4336-3490-8f23-789d9305d0b8 | -5.46704 | -40.96922 | 2025-11-18 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c1db99d-4b31-3d07-b004-d3e3546b844b | -3.27381 | -50.0216 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab8049e2-a947-3898-a187-9ac5a9450d19 | -1.41483 | -48.91278 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28accd1d-8e09-39a5-8b51-79a0e1ae73a6 | -2.33142 | -55.7986 | 2025-11-18 04:48:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eec5cfae-49eb-3d23-8f3a-3c05a6d5ce08 | -3.93901 | -52.18263 | 2025-11-18 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b5e3012-cd59-3265-b8b2-f17d536e24e0 | -1.7626 | -47.26142 | 2025-11-18 04:48:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf5c3986-450a-3f9d-a026-3101e79aa071 | -1.83276 | -55.35394 | 2025-11-18 04:48:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 644f1e91-6e95-3b3d-ad99-be55ab4fbc76 | -3.12922 | -45.74747 | 2025-11-18 04:48:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b81aa59-7b65-37bf-9778-8f0e55543b13 | -3.49275 | -54.05216 | 2025-11-18 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fa67ae6-e5ea-3c13-8523-7dae46871a51 | -3.14554 | -51.32676 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12b7d2b2-57dd-3740-9229-5838c6dfb4f6 | -3.15991 | -50.1665 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4fd0c2f-74c0-34f8-a17b-a69a43da9d07 | -3.18837 | -50.64791 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c144e130-c4cc-32ee-9d60-037300338e5a | -5.43037 | -43.04549 | 2025-11-18 04:48:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21559508-dd58-3f19-ba1e-da3b09c07593 | -4.18419 | -44.24064 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83348bfc-a333-3eb2-a23d-eb21b43021c7 | -6.4392 | -43.81745 | 2025-11-18 04:48:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f68b8ed-618d-37e5-9a0f-8e5436df13e2 | -2.81274 | -48.2565 | 2025-11-18 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4729860b-f681-358b-83f2-04b63aaf2d48 | -2.49724 | -49.34961 | 2025-11-18 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ab49c85-89c2-3224-96ef-5c711a26073f | -2.68141 | -49.05487 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d1718ff-8be2-3505-86c0-bf6163d3f6d2 | -3.17925 | -48.02976 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3c9c8bd8-ec91-35b7-a167-2fb16bb9df7e | -2.92667 | -45.341 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf4e548e-4925-3fb9-b05b-2e7e74281ef6 | -3.52129 | -50.34351 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77b69295-145a-3f8c-9667-815e1e367a27 | -4.673 | -45.99652 | 2025-11-18 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24216acf-1521-3602-9b4e-9379b0c9fb07 | -2.91212 | -47.84599 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 105b6fad-8c2b-34e1-9619-d65b79e1dd34 | -3.08638 | -51.26692 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e68cdef0-57f4-3683-b5a6-06ffd9830ffa | -3.30548 | -50.0796 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa96ee54-2236-37fc-9a00-ac1b7cbb4dad | -4.1429 | -46.35272 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0b3acc51-9f74-3f91-be7a-b8d19324dca8 | -3.30252 | -53.85218 | 2025-11-18 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07526076-1de6-3901-a85c-1341110d24f7 | -5.405 | -44.0664 | 2025-11-18 04:48:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09da5587-0b34-359d-ab6d-f78d63594c65 | -3.08346 | -52.92286 | 2025-11-18 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a779940-4d50-313f-ab2f-93dc8cbe26c7 | -3.18118 | -50.65032 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ca859e6-3b2d-3581-af17-245dbba2ee63 | -3.59903 | -40.96448 | 2025-11-18 04:48:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| edfd98b1-5716-30cb-8978-a9a4d3dc1e1a | -3.42078 | -50.35971 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f37a4833-a29e-3e64-be46-1b1efc8be522 | -2.92615 | -45.34447 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4b38003-0365-374d-ab23-7ae7ecfa14df | -2.45511 | -50.27828 | 2025-11-18 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2b88911-1873-3816-bc96-80ae87fc9891 | -3.79857 | -50.12938 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76ad203d-7505-3e13-b77f-01878bfc283e | -3.07412 | -50.23769 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8448a1b2-c862-3fad-8658-752a59c67bb3 | -2.75833 | -48.42639 | 2025-11-18 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README42.md)

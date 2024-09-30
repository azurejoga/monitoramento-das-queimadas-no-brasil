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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4df553c1-bae5-3f99-850d-df78af81c39c | -3.10813 | -49.40804 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| eab7fbaa-5ba7-3a86-acdc-09cc029209ca | -3.10646 | -49.39592 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8e9ecffb-b295-3133-916e-1e4cfad44be3 | -3.10585 | -49.39978 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7207832c-3241-3b6d-9663-0f538229d4b8 | -3.10525 | -49.40364 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 07e61e9c-5581-38de-9612-811fc28f3ba7 | -3.10464 | -49.40749 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 81771a6e-f290-375a-ab20-efd2c0ed9918 | -3.10298 | -49.39537 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 97e3d8e4-f2e4-3778-baa7-f478fcb1ec2b | -3.10237 | -49.39923 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2c594104-9b14-35d4-a499-c1e19d18f1cf | -3.10176 | -49.40308 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| db795ae3-3534-3669-bacf-90640bd5f4a4 | -2.72241 | -49.53636 | 2024-09-30 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a99e18e-a3ad-324e-ada6-cb3f2474b77f | -2.62762 | -49.09234 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9bb06fb9-8589-3425-b3d5-8b24f836fd72 | -2.56973 | -49.10677 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38fdf339-16d4-3bab-92f0-cc36c044c48a | -2.49103 | -49.05237 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eeabc693-7136-3894-8983-7234a324a2c7 | -2.47486 | -49.15489 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8b9e46b-56a7-3dfe-9653-cf0f10a78821 | -2.47426 | -49.1587 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a40e933-6277-35b6-95ba-3ffcc937073a | -2.47366 | -49.16252 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 087888bf-a9f1-300b-b4c0-8b47c3c5fbe9 | -2.4714 | -49.15434 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7cd09e6-2152-3ff9-b375-e717b976364d | -2.47079 | -49.15815 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62dbea56-0540-39be-a8aa-155f25b34929 | -2.47019 | -49.16197 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58b28536-1502-3019-9c6e-4900ce85b939 | -3.09597 | -50.48251 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7cb656f-92c3-3f76-9b88-7b5063b4fdf0 | -3.09299 | -50.47763 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 51dcebb0-55ee-322c-8c50-f439e03f1216 | -3.0923 | -50.48193 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc79bf66-31ab-3699-a22d-8d8447a20f32 | -3.08932 | -50.47704 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 37c1b746-6ec6-326f-b369-8f17de64540e | -3.08863 | -50.48133 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d0b35146-8acc-35b6-82aa-bb23ae82547e | -3.08565 | -50.47645 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 81718214-ba2b-31fd-be94-0fb2625d6732 | -3.08496 | -50.48074 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 730a86e6-54d2-3a23-83ec-b5c899d2d047 | -3.08129 | -50.48014 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4be8c685-4617-3e40-9f6d-606764fea3a3 | -3.07762 | -50.47955 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c214744-cc5c-347a-b2e1-ac6331fa14fb | -3.07395 | -50.47897 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 237a4f73-39a8-38d5-a799-335d4f14bebb | -3.07325 | -50.48328 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52f8a0dd-dd1f-38ab-9263-540698ed417d | -3.06957 | -50.4827 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd1eacd9-9fba-33cf-84f5-1dac8ed5c03e | -3.06887 | -50.48701 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0506db54-e0e1-3560-8142-07389e243fbf | -3.0659 | -50.48212 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8aeb699b-0978-3031-8a2d-2569da50229f | -3.0652 | -50.48643 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b891f185-6586-3fcf-ab56-58451bbba668 | -3.03994 | -49.54441 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8d76385-9b12-3725-96cc-51a1fc46c2a8 | -3.03932 | -49.54834 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef719b02-97d5-37ee-822a-42d00308f799 | -3.03643 | -49.54386 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 427f79a8-b2c3-389f-8c06-0d6cb39e9362 | -3.03581 | -49.54778 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab928ecc-6e96-3d5c-af9a-e8a0d150d87c | -3.03293 | -49.54331 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bb85414-6a71-3274-86e3-0b4ed435d68d | -3.0323 | -49.54723 | 2024-09-30 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b19f4b4e-0648-3c34-8cb2-0aa64cce0992 | -3.00984 | -50.29571 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe7567b5-b70d-33e2-90da-38f3e4dcdfba | -2.94544 | -50.30013 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a90a3221-6fbd-3845-a3d3-62d618466f06 | -2.72593 | -49.53691 | 2024-09-30 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5b029d2-813e-31f2-a61b-fdbdc7a426c0 | -2.7253 | -49.54084 | 2024-09-30 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28abd5df-6e9d-3df9-ba98-db4aa97e4d49 | -2.72178 | -49.54029 | 2024-09-30 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ac59668-1105-32f7-99a1-f2626d28d9a1 | -2.71826 | -49.53973 | 2024-09-30 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 786a184c-a497-372d-a906-72230cee7f8c | -2.42236 | -49.69073 | 2024-09-30 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4dd0670-1d9e-3d1c-b4fc-3b3f79613182 | -5.09611 | -49.5984 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1824b788-9d33-3bf8-9f6b-feef5c8fa971 | -5.09387 | -49.59027 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5396c23-c265-3141-b3b1-ad0917017627 | -5.09327 | -49.59406 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f64c8ab7-fa4c-367f-911b-1dad9554e1c1 | -5.01188 | -49.75729 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7cb7617-95e2-3fca-ba8d-e6d066211932 | -5.00841 | -49.75672 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 486962d0-5fca-31ef-9c04-2645e3d862cf | -4.39541 | -49.63452 | 2024-09-30 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2237f5d-a92a-309f-8415-d81e5cd19b9e | -4.39479 | -49.63834 | 2024-09-30 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53efa96d-d8ea-3e2f-bfd0-8cd27a0e9530 | -4.39131 | -49.63779 | 2024-09-30 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed4bc28a-eaa4-3df2-b26c-b850dcc28097 | -4.3898 | -49.98122 | 2024-09-30 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57b5aba9-de18-3c72-b41f-ebed264677fd | -4.2809 | -49.96077 | 2024-09-30 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b323f7bd-7c32-31bd-82ca-0689eb747289 | -4.13139 | -50.2606 | 2024-09-30 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57a58a82-2682-3710-ad77-f1e0f1557bc7 | -3.93202 | -49.98969 | 2024-09-30 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3e4abaa-a2b5-352b-a618-8547e622e776 | -3.78784 | -49.60132 | 2024-09-30 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 096fe137-cc30-3c2a-a755-a878a7014d61 | -3.77743 | -50.1612 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a60ae84-b281-3d69-9551-19236f476d8a | -3.57034 | -50.37337 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c575c3ba-a7ee-315d-ac6e-e522958ab6c3 | -3.56767 | -50.57825 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54418d05-8557-3236-84fb-b93718970d61 | -3.567 | -50.58254 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cab46b6-1b14-3f6c-92cb-b0e30769abd3 | -3.56333 | -50.58192 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eebd2720-fe89-3afa-a18e-46f4bbda9955 | -3.56307 | -50.37228 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 030ea92f-2d7c-3f1a-858a-7a76a7e97fdb | -3.5624 | -50.37645 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6296accd-f80f-3697-a9b9-787612fa7957 | -3.55944 | -50.3717 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4048faab-7ba9-31be-af2e-3fc54657ceae | -6.30908 | -50.0125 | 2024-09-30 04:29:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 682f98b8-be60-3c81-a8cf-250023da9569 | -6.30846 | -50.01633 | 2024-09-30 04:29:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e1d9bbc-5039-39de-a646-ef549b0ed7f6 | -6.20031 | -50.90487 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62c647e6-3a4c-3709-aa84-f7766ac442f0 | -6.19308 | -50.90372 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ddb2b94-87d7-3739-9c77-75d3f481b6ca | -6.18878 | -50.90734 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d091e388-f675-30cd-8b56-d86c9d8d34aa | -6.18585 | -50.90255 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd9b3325-e468-3b48-9ace-89df9b6999d5 | -6.18516 | -50.90673 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad6318ad-61fe-3f35-9270-1d96f1c1cfc7 | -6.18156 | -50.90609 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 465d6eff-c23a-3fff-919b-352c9ba1fbd3 | -6.17794 | -50.90549 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fea877b-31ec-30aa-a5ca-ce305e609602 | -6.17725 | -50.90971 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdbab00d-1808-3766-8914-9d5f1063d251 | -6.17362 | -50.90917 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a5b9cb3-38dd-3f17-889d-d8e98ca1a999 | -6.17294 | -50.91338 | 2024-09-30 04:29:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad7d1fc6-8695-377b-a9dd-3a48bf79e8c3 | -5.98933 | -49.67086 | 2024-09-30 04:29:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63c04d45-6552-3814-af67-7a1bf31d3936 | -5.9865 | -49.66655 | 2024-09-30 04:29:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ce38cbb-ccde-3fd5-ad36-e907cb20d84d | -5.98589 | -49.67036 | 2024-09-30 04:29:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bf0761c-8ecf-3945-ad3e-1c1d4b8c9dfd | -5.98368 | -49.66214 | 2024-09-30 04:29:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a96f400-5739-30e6-a5de-cecdd61b5106 | -5.8896 | -49.72612 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18c55feb-bc72-361a-b413-2166f573507b | -5.78982 | -51.03377 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cca6789-107a-36b7-a964-34dda89fc0e2 | -5.78918 | -51.03678 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1219393-e921-3f94-9bf9-4f1d35a76d70 | -5.78913 | -51.03811 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1827589a-cdde-3a9e-b581-8f521eee9d7f | -5.78843 | -51.04124 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53d73e34-259a-39f9-a637-a43b8e468986 | -5.78841 | -51.04263 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2c87a52-c7be-3b55-8378-0f00878a9937 | -5.78769 | -51.04714 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73d0a25f-6729-34c2-a8e7-3809dab94a33 | -5.78768 | -51.04578 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 219621f2-6ac9-3be1-999f-4db922e36925 | -5.78628 | -51.03159 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6e440f5-65ce-32fb-8038-b5b93d8a6ac6 | -5.7862 | -51.0329 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1aa128f0-99e6-3088-bdd5-59b0294dd119 | -5.78255 | -51.03229 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0224d86c-07cf-311f-ac96-7ea8ef57c93d | -5.72275 | -51.07658 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2c7ffd4-f7f1-3566-87b3-0ee61b9b4457 | -5.71907 | -51.07602 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b28defce-c7cb-3a53-abe2-805192fd4bd5 | -5.71683 | -51.06672 | 2024-09-30 04:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b7e4f380-ea9d-3f7a-9248-6eaef0f7258f | -5.69281 | -49.98811 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ecc53e5-3c8f-3445-8a06-3ff01a377ebc | -5.52353 | -49.55682 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 574b373b-047a-3806-80a2-237a636e259f | -5.5201 | -49.55626 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README31.md)

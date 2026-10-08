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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff79e3ac-0b51-36b5-a9ec-5c589008d9cc | -1.33509 | -55.42993 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfd8249c-786a-3909-8114-0e8efc550233 | -3.08781 | -54.29505 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ebe9938-30ff-3c06-93a5-3e242f0c07fa | -4.93673 | -55.81742 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 916bb953-9c94-3e20-a345-96e39461e370 | -3.475 | -55.43507 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5b54708-71de-393d-aba4-9fa99af94dd8 | -3.00722 | -54.14227 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cdbbf44-8042-32a3-97b8-9e88c153bc87 | -3.18778 | -50.54754 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bdc47ec-8b79-340e-90c3-f6b16c2704eb | -3.52735 | -54.65795 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dac32824-60e9-3b4a-8478-94d11dc130f1 | -4.2947 | -50.78365 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d34e4937-2101-3e9a-a925-beba591957b3 | -3.21056 | -50.54932 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b6000d2e-cc95-3495-9c59-ebdb2d9f0d7d | -3.2975 | -54.01405 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 477317b7-2ec9-3f38-b5ff-d897643a4f8b | -3.06899 | -54.25008 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 069e125b-8c2d-3855-bbd3-929ab9aef3df | -3.09387 | -53.72486 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0df205db-1c42-3c87-bb9c-5d3fc09dc5d5 | -3.66887 | -60.62048 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21507968-7ef1-339f-ad47-b61dbbd3902b | -5.26152 | -60.17542 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e7e16c4-d9a8-33a8-8762-d96ff6318330 | -4.11017 | -54.4156 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a683ccb6-991b-3d10-a98a-b2bd544b8e27 | -2.77801 | -54.06445 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12621a98-9b2a-3979-8ef5-38c3a3343f11 | -3.85877 | -55.964 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afa220e3-5440-3b99-af43-b8f27d45f40d | -1.53693 | -54.55236 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 568df6c5-fb31-3065-92df-e977b26c9ed6 | -6.09875 | -53.49641 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 495d6844-1894-33f3-b6e9-ae4fb75c7254 | -5.83721 | -50.14597 | 2026-10-08 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c9edc58-50cd-3825-bfd6-f7b2658e3a20 | -4.3639 | -55.64509 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71b97155-bbd8-32ed-8723-5165c7cc8467 | -6.02533 | -51.72561 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e89f0710-f3ef-3a4e-bb9a-2dd6c33c5bf5 | -2.49843 | -56.07106 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4d609d9e-0ea4-3ebe-99ca-7dcb121c1945 | -3.29793 | -54.0342 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f16e866-9606-3fc2-ab3f-0cbaacbd06a6 | -2.99749 | -54.08933 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| acfe7af5-439d-3480-8bde-6bfe9505e2bb | -3.91816 | -52.03723 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1311efc-3cd9-3dd0-917a-e41707de9dfc | -3.18715 | -50.55163 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3ac6bc5-7f84-3e5c-a586-e0fa561447b7 | -2.99757 | -54.06554 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d2eb8f66-6d3b-38fb-a396-41a05227a00e | -3.0916 | -53.94815 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6506050-de82-36b9-bb58-de6ec09571ee | -3.2425 | -46.96261 | 2026-10-08 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 381b970f-c5c4-37cb-b38b-c47339507832 | -5.9811 | -55.3841 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a750bc4-e931-3746-ad32-ab2745caee17 | -3.51574 | -54.52924 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bbadac1-37c6-3ae5-be64-b7b6d85b424a | -3.02675 | -54.08596 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31fce830-df4b-3d9e-8fe0-99034e876aac | -3.44326 | -56.93898 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88e35a08-f3f8-3c94-a911-601b607ba223 | -2.79142 | -54.07047 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8b37763-5c84-33aa-ae17-d56c75e0d25d | -3.69746 | -50.67219 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c41321d-d1f3-3772-a1e9-458016637da6 | -2.99311 | -54.04515 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccb9a626-2d60-39b7-9dee-79c68b416c32 | -11.78565 | -46.77611 | 2026-10-08 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99650658-2f88-3ae6-8924-c9934c0fbc69 | -3.84709 | -55.97289 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf1027cd-5c1c-32bf-ad8b-649bb0b952c3 | -2.4641 | -56.09404 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5973ecb-b385-3a37-89fb-dd3fd65f6b9e | -3.6636 | -60.62905 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02a7c5ae-3639-34f1-9fda-67636ed6e510 | -2.49471 | -56.15906 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 373f2c0c-f077-3e35-9c63-74b0615d1706 | -3.09681 | -53.72943 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2504c294-dbbb-3c5d-a123-f9dd00c611be | -3.97182 | -56.12079 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7afc1c9-1137-3dff-8879-14617c628f4b | -4.77701 | -55.72031 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55e94911-c8ca-3cfa-930a-737b2eaeeebf | -3.14866 | -53.7251 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bb67dfa-2af4-3bee-9313-67cb5bebc452 | -2.77027 | -54.11451 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8c622ed-1e75-3d02-8f50-a230fac482b9 | -4.13852 | -54.02682 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4b92443-80e0-3fe3-99c1-fdf751104cda | -2.98704 | -54.0639 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66c262d4-9bb6-3f43-8242-a9cf822ae427 | -3.36688 | -58.20189 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b43b582-5c72-3e2c-8874-622c4e73f0e2 | -3.0075 | -54.07106 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ab83b46-a875-32b7-b097-0fa657934113 | -2.49307 | -56.16943 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f05b979b-73d4-3b11-912e-eb3e4f596fd4 | -2.5707 | -57.02229 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 494a5603-0fd3-3f3f-9c38-530c6bf297ae | -2.84885 | -54.13855 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6259fb69-52d2-329f-bf44-124bd4872a37 | -3.08157 | -54.24324 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acfb16e9-9784-32cc-9e1b-aa87c1dc30bd | -3.03437 | -54.08316 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c480088c-867c-370c-acfb-b7ab3eed9a14 | -2.46132 | -56.09006 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b18ed2b7-479d-375b-9936-19a3089a2436 | -2.48256 | -55.76658 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9770e0e2-aa19-3ee8-8e0c-b2469348b44a | -3.83651 | -55.9748 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dd7da20-bfc3-38bd-80b1-93074c08ad80 | -3.23564 | -50.1799 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b6132ca-78be-39b3-9c48-db87a0d29912 | -3.05581 | -53.92252 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8be33fe-fcb7-3c4c-9844-c73b3fc7fee6 | -3.26836 | -54.06169 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65748b28-2ebe-3918-a3eb-db2ff28f5502 | -2.41505 | -56.53227 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74dd8862-3959-3529-b3f0-452727971815 | -1.5182 | -54.51588 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d44041a-22a3-3b2a-82df-ab23c7f0be9f | -1.47501 | -53.61393 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e42db746-1ac2-3b8d-a57c-694c34fd5662 | -3.09635 | -59.19172 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9f3b5b0-d3ae-3807-ba63-cd605e7e03c3 | -3.49184 | -54.6141 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee6cc5ee-8381-3dd5-8203-816e980c5c7b | -2.58685 | -56.17333 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7049425a-c5e6-341c-a4f1-d0c79e6a6fd3 | -3.04033 | -53.9523 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d8ec8d9c-d085-3397-9d35-26d7e182d86a | -3.59375 | -61.63549 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52a47a79-e083-3ecf-b8d2-72d2d3eb2fdf | -9.35428 | -65.74816 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0244527a-d244-3ba0-ad7c-908c1416cb79 | -8.73468 | -45.14942 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 22ed336f-338d-3084-8844-3931ded119df | -10.88376 | -57.0793 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe367173-c878-39ea-8a9a-8e3b637eb345 | -2.58571 | -56.15899 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84e8355b-4973-3bf2-be3b-1c3d6c2e9cff | -3.86716 | -55.99749 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 473b5eef-60a5-3d54-b7cc-de93c5fede85 | -1.38306 | -56.89204 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d861ec58-185d-355f-8d26-e3fe62e6f8da | -3.02044 | -54.05717 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36a79d51-0e56-3377-a209-7312f6a0ba9a | -3.17177 | -54.74469 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a876196-3f6f-3d18-bf1e-f32fb90447c6 | -2.88845 | -54.16334 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc30864b-38cc-3392-8e05-006c2313cb74 | -3.21959 | -53.8899 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23f389de-96b8-3065-aa6f-be8d9f73fc60 | -4.75732 | -55.66988 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3867aa4b-19f5-39d5-808c-2e8f0d0728de | -3.86326 | -56.00047 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c015571f-9626-32e5-85de-d63faa1d0330 | -3.71248 | -58.54931 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ba03dc6-04d3-3231-9fbb-33913efe2f81 | -2.50688 | -56.1468 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c0f38988-c04e-318d-89f5-d8b165589610 | -2.88741 | -54.12386 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91c382a2-d706-37c0-9576-c12fd57f10f4 | -2.9857 | -54.11916 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| bc8c3b78-9b1c-3115-b22c-68b3935427a7 | -8.74 | -45.16172 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56b03d2a-8a75-3f74-a45c-c529f2716a00 | -7.22715 | -55.1092 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7814eb32-c4e8-3a73-b603-c7b69b190c87 | -4.90086 | -54.99312 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22f68718-f508-3fa6-b9e2-79141fca7a2e | -3.28244 | -54.06387 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 918e9f7b-4a44-36a6-84ea-b4d49f244b4d | -3.52133 | -59.35397 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 764cfed2-3db3-326e-a976-0ce290841a85 | -2.30143 | -58.0955 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20516386-1ba7-3080-9cb2-1cabbc41f37c | -3.59764 | -54.67592 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d812e78-7d73-33e8-a626-989c17e8d7c2 | -2.98623 | -54.13899 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60018387-c388-3545-a9b4-8ee3e6f24507 | -3.61205 | -54.05187 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6ba4f7f-318e-3664-a33b-29b33e3109ac | -3.00201 | -54.12963 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbd48f4a-3b27-3cf8-b63c-65f9266eabc5 | -3.52816 | -59.37963 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f889c696-fc49-350e-a42f-0f5e90071959 | -2.65451 | -59.43166 | 2026-10-08 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3f60a0b-7623-3b92-b735-32366183d974 | -3.08039 | -53.95044 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 3bce475b-c9b6-3d24-834c-36942367fba4 | -5.99834 | -53.49693 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README136.md)

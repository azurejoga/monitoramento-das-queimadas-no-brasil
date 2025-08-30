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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1cb43a5-d0c7-3fe1-883d-e4247d5ff1c9 | -8.95611 | -65.96262 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a70d1e0d-1006-38e3-834e-d9830e74eb21 | -6.07342 | -57.93427 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a293536-220a-308b-8b29-dbac4facd79a | -10.02702 | -48.05729 | 2025-08-30 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f155125-19fc-3010-bd15-07b618f99754 | -8.87671 | -60.7322 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 407b5dbf-7fbb-3bb1-92e4-732972e05bb4 | -10.35143 | -59.18691 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5576cbad-2e8d-37df-b384-fcf5cc092664 | -11.82992 | -46.45809 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ff6926a4-e269-3f90-9ce1-9cfc6443d0f2 | -7.95478 | -46.38247 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f244de7-29e7-3d79-8815-e868ca5012e1 | -5.69521 | -45.9607 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1572451c-e5c4-36e6-8095-15f5e42dd794 | -10.38015 | -57.8253 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 602a70c5-eca7-3ae2-996f-b2656496ae0f | -9.31797 | -56.90486 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85f743dd-f73a-36a6-9f88-32b178cd1176 | -10.53855 | -56.38556 | 2025-08-30 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 206b196e-5462-3622-954c-b74b7ad22ca8 | -11.83761 | -46.44829 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b5d99260-0f41-3c96-b3f7-eadaac98a108 | -9.43903 | -60.55051 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9a351876-15c2-3a01-a70d-cbef1c6fa5d3 | -9.44062 | -60.56279 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb4da0dc-441e-3079-8e02-311754b2ac61 | -9.11283 | -65.73835 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69c53c25-d84c-341f-8cbf-eacb3d18bb36 | -9.04726 | -60.49179 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a51932c5-b08e-3d3f-83e7-c2755384e8da | -9.45648 | -62.33201 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| bcaead2f-648a-3a07-a5ac-88d1c471608b | -7.43708 | -44.82184 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 40806baf-1230-3cd2-9280-c60630722b68 | -9.44895 | -60.56367 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a078639c-24eb-36fa-92a6-b11cb5a1384d | -9.44474 | -60.55945 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c9609fa8-9754-3300-88be-d1aeee3df660 | -9.46173 | -62.34765 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ba9438e-399d-33b5-a00b-f9513bab30f2 | -11.92058 | -46.69797 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4b8def4-d819-3d8c-ba09-0092cc69dc42 | -7.90232 | -63.00793 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2f50daa0-d490-354d-a5c3-449b6df4c1cb | -11.87954 | -46.37379 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12aa60c8-9d34-36a2-a417-9981aede63a8 | -9.46029 | -62.3327 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c6b25f78-dc02-3b79-9921-55998c12e250 | -8.89686 | -62.10254 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ce01e7ab-9586-3c9a-9287-a684f30c1d32 | -6.77356 | -43.78718 | 2025-08-30 05:10:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b91f148-80c5-3b3b-b5d2-9dbe2ec0379e | -11.06543 | -52.03848 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8a9057f-e348-371d-87b5-3d5123a18387 | -9.19916 | -59.69453 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1f76a3d-6cc3-35b4-a22e-59ffa6ecdc9c | -10.36409 | -59.21451 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3c9fb10-3948-3edd-bba7-331b7be0ea1a | -9.24339 | -60.92796 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 125f0419-22d1-3181-98d2-d58fedb9eeb6 | -7.11831 | -44.58957 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25727c5b-16b4-34fb-b98c-030a3b92e1cc | -8.86856 | -45.73457 | 2025-08-30 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6512a7c6-1ff0-389c-aefe-98a8882a6797 | -9.44727 | -60.54386 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ca6abeb7-9303-325b-95d0-cd0d5ad1c57c | -9.1109 | -65.77621 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d014eb83-cbff-3dd7-8eda-7f5609748821 | -10.37738 | -57.82127 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0041b5e8-f4d1-33dc-b0bd-c38c00be9723 | -10.3658 | -59.20385 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae359854-29a8-34b9-bafd-3d98e487f8b3 | -10.73116 | -47.01406 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 371631fa-d3d4-30fd-9af6-c27a5e932315 | -9.25686 | -65.84361 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e2e6e21-0060-367c-ab89-71e09e142f49 | -7.20471 | -43.70602 | 2025-08-30 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d93ffc6b-6dfc-3ad5-bef4-f1fbdb679337 | -5.69404 | -45.96498 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21943863-0f32-3f4b-a428-c60c2f09b49c | -10.44645 | -57.96526 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d8d102c-23bf-3884-a9ce-753728f5fec4 | -10.38065 | -59.38889 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92f52ccf-cc69-3885-8526-9e987871a811 | -10.37905 | -57.83233 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72e8c820-0b86-36bb-9dfc-e4b21bb14403 | -11.144 | -47.15453 | 2025-08-30 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 701549a0-3773-3ca8-872b-aba7ed1b3265 | -9.69257 | -48.30651 | 2025-08-30 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c75d1e08-74db-3848-868b-6db62f100ced | -9.12334 | -65.76232 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2224598a-1ee8-377f-8f9c-8f318ee8ac64 | -8.95069 | -65.95092 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 864f2082-9a20-3fa7-b425-a49a49b58a37 | -9.45462 | -60.57272 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53859bd5-0273-347c-8d7f-7fde66e1fc44 | -9.45345 | -62.32664 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 2a646c50-9373-3b13-a504-ce4da64a5bf2 | -6.59582 | -43.65034 | 2025-08-30 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b20c91e1-b7fe-3390-9f70-85950e1d202c | -9.58903 | -54.48211 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba447709-d63b-309f-a299-c82d2e294790 | -6.3441 | -58.17779 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64846f3e-03ae-31b5-a504-59e595c3f6e4 | -9.16956 | -59.56957 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89203cef-af41-3364-9338-43f0c4d4a317 | -9.44485 | -62.35451 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6297d1bf-5c9c-3d19-99c0-5cc48eb99f16 | -9.44947 | -62.35041 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| de7e2d48-1ea3-3ff6-a612-9571edd5e7e5 | -7.77997 | -45.46711 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cd28532-9bd8-309e-bd13-8e8d4cc6e963 | -11.1515 | -47.14266 | 2025-08-30 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d6c4b020-5688-3b4c-80f9-23f007b4f2f6 | -8.55983 | -63.02081 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bfaf181-61d2-37c8-b9e5-f27d4f2cb9a9 | -9.46237 | -62.36735 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91506ba0-ca42-33ed-9cd0-9b804a36a513 | -8.65741 | -70.04329 | 2025-08-30 05:10:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3521f1f7-bcd0-3cc2-9b27-9c9ca9e09684 | -9.12919 | -65.8124 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06d60ac0-e9bd-368a-9f44-a4b2ebea3011 | -9.57353 | -54.48445 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a352645d-e7c2-3b03-961d-085058cfff3c | -9.12533 | -65.80624 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05b123c9-0a5f-3d93-980b-43a81398d425 | -9.4483 | -60.5676 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0ef076dd-345e-3b6c-b58c-36ed5884fdc2 | -7.60736 | -44.94787 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1dc941f-a168-3613-9b94-daad2c1ace1b | -8.90587 | -62.11853 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9a8eacb-6d02-3799-ae28-299288e21815 | -6.37693 | -44.339 | 2025-08-30 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7dbd7235-b4d3-385d-8c9b-d14ac02b1260 | -9.17699 | -59.57455 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 283ae996-7849-3849-a979-1e5b36c8b0ea | -7.39473 | -60.59656 | 2025-08-30 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d3faac9-e374-3f8d-a281-1aae79251c30 | -9.1543 | -59.57819 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 149bd660-b9b8-3b9e-ad0a-8080413da9ff | -10.02182 | -48.05256 | 2025-08-30 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a82c6f58-3be9-359b-b932-64a2f27335ee | -9.4595 | -62.33744 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 76c0d18c-1fa2-314c-810e-0b9b529d83af | -9.43819 | -62.32404 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ba59323-e042-33c2-a6d0-94d5bc63d8e9 | -11.83059 | -46.86468 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| add935fa-1ec4-3918-ab5a-f7e407cd6a69 | -10.37518 | -57.83532 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84862981-3211-3ef2-a0b2-4eacad170b99 | -7.71757 | -50.27583 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f175a4f-6e0f-3973-bb70-54d9e1ed1a99 | -14.10141 | -51.77826 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c20faa1-5208-3fdd-9d5e-ea7a3a0a8f21 | -14.62409 | -48.07928 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f2339aed-542d-3d96-8eb4-942774caa1cb | -14.79896 | -59.71623 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97dc8cdf-a985-37bd-aae9-a9dabe2406bc | -14.50353 | -52.99286 | 2025-08-30 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50535c8f-0265-3bf1-842c-f48ab6d32363 | -16.53468 | -55.0452 | 2025-08-30 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0d79834c-376d-340f-8943-420ad1ad96c9 | -12.44145 | -63.919 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78d54370-cfea-362c-860b-c1b54fa4c357 | -14.49775 | -52.05053 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8336e9bd-d8bb-3e5d-9c84-d17e3ebfe724 | -14.59368 | -54.5452 | 2025-08-30 05:12:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83e0e0b7-dde2-3678-ab3a-ae4e21d18789 | -14.78894 | -59.73661 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d73f20d5-f3c4-3ee5-bf54-4a3a3bebb5be | -14.32699 | -51.95482 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 802b196e-6681-325b-bf5b-fc389879bb9c | -14.79282 | -59.73359 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96491b56-d4da-3b1d-a846-6b865d8a3af5 | -14.77454 | -59.74147 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa31c0fe-62f4-3814-8c3b-a8ff3890a906 | -14.45914 | -52.02024 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f70bac60-ec64-3bbc-b843-039449e4d088 | -14.34342 | -53.29877 | 2025-08-30 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87ac3e35-bd28-3c93-9aba-57173d73d99c | -14.55928 | -52.00013 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98216875-c0c3-3b3f-8f21-55ef577697cb | -15.58788 | -56.0185 | 2025-08-30 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d68e6b01-2225-353d-b850-d7d35f423b59 | -14.59398 | -54.54868 | 2025-08-30 05:12:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ecd71acf-587c-3343-a7d6-79005618568d | -14.7984 | -59.71982 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa9aabac-e2c2-3939-a6b1-46394dc08ab0 | -14.50069 | -52.05282 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55167f2c-17d4-3534-9ec7-3c7f3481fd81 | -14.49666 | -52.0472 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ef692fa-7545-367b-919b-47b200ab26b6 | -14.34386 | -51.89609 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a830f609-f320-3f78-8f89-a4c0ebde3f86 | -14.50533 | -52.05344 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e817985-a3dc-3874-8018-c77e1bbf39f1 | -14.33983 | -51.89031 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README72.md)

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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e9d201d-7f49-3323-b302-c5ed05a3c332 | -9.65991 | -57.90681 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0cda93f-6cf9-39a7-8673-b00a551c021e | -9.57386 | -57.75668 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6253183f-b952-3208-b9c7-571ba4a6bb0d | -9.54403 | -57.90781 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ad69aa5-790e-305b-8b81-2b96d003281e | -10.02399 | -57.99998 | 2024-10-11 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3931db69-0a6d-3617-8df6-5499fc3e4d2a | -11.15722 | -57.18929 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1dd27db-4552-35a0-bee9-7ddaba44a8d0 | -11.03438 | -57.21352 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91b6f1ff-ed38-392a-8334-ede2b50a4a15 | -11.03379 | -57.21756 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 417b03ad-50d1-326b-a72e-a35843f03498 | -11.03144 | -57.20888 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76893c61-d076-3303-8ae1-6b8f1a65ba97 | -11.03084 | -57.21297 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a47efa1-426a-33ed-b751-8d9c9d9fc422 | -11.03025 | -57.21701 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91239eef-9af2-34c0-9945-b73307c33c0f | -11.02966 | -57.22105 | 2024-10-11 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 549db1a2-b404-363f-9fac-934f4c1f3484 | -6.47431 | -58.43497 | 2024-10-11 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 900dcfc1-5c14-35fd-9a42-61fa899edae4 | -6.46228 | -58.4686 | 2024-10-11 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 415bebcc-9e56-3bca-bbce-9b9f84b8a4f5 | -6.46173 | -58.47206 | 2024-10-11 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78160cf7-fdb3-39bd-ae40-7ef83cc676de | -6.35141 | -58.17731 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e35096dc-e458-3de6-9e0d-33dd227433f0 | -6.35087 | -58.18079 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b94435db-07fe-38ed-a67a-5752c3d7c1fc | -6.34809 | -58.17679 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7163097-2f21-362c-b957-acc6c0ff68c3 | -6.24292 | -57.86644 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 463273a1-71a3-353f-bd58-c3f471d87454 | -6.19877 | -57.77966 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ae7789e-d20b-3779-a148-f3fb4c9336ca | -5.9604 | -57.69246 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1b919c0-5243-3361-ba83-7e605f78bdcb | -5.95706 | -57.69194 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3059b5b0-e74c-3f89-ad6a-20839150cd2d | -5.93876 | -57.70326 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa04a70a-05d6-34ba-947e-d4accc0297e3 | -5.93821 | -57.70681 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9314bc02-b29c-35bd-9d19-67372fe36094 | -5.93765 | -57.71035 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf10439-aa11-3a33-9be6-374d8b88a194 | -5.84147 | -57.71355 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62477e5e-f760-362f-9f34-d0791f701b61 | -5.84092 | -57.71708 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fe9d21a-3fe7-3b44-907b-01c04580257f | -7.20131 | -59.07442 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30a54e00-caff-3c39-b045-24158719dff6 | -7.20077 | -59.07787 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4c895d3-8d2d-35dc-8844-7cb4f0450dd8 | -7.19796 | -59.05267 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05a7a133-4752-3d50-bed2-c4d3e5d4bca6 | -7.54097 | -58.29188 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d0392e0-0601-3279-9cb8-46cddf629fbb | -7.45134 | -58.60731 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa5b9be6-a3a7-3c10-8d92-042b5560c754 | -7.44803 | -58.60679 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e26b8a73-29bc-304a-8be0-57ea00efd268 | -7.4458 | -58.59932 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77bca43d-7dd1-323b-826b-57cae7367cfd | -7.44526 | -58.6028 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fdd399c-571e-323f-8a77-f4b8233aba2f | -7.18378 | -58.16047 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 819f83ee-fa0e-3842-b784-cdcd92b1e0da | -6.92659 | -57.77623 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b758d66-ca42-3380-b08d-1355dc149a4f | -6.92324 | -57.7757 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76cf7215-2ba0-35a7-85c7-73cae728ba45 | -6.91935 | -57.77874 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69bedba6-29f9-39c1-bde8-0064d501f8df | -6.91319 | -57.77413 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff22dc1b-6e78-3d61-b756-03d2afc0e22e | -6.9093 | -57.77717 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77a14604-dacb-385e-9cd0-7a1898531309 | -6.90703 | -57.77642 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e730062b-f628-3ce6-88b2-27eb39ed8804 | -6.85544 | -58.5878 | 2024-10-11 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65b7cbd9-bf80-374b-8a2d-36936d201d22 | -6.72802 | -58.44653 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 521d093b-7d0e-3bd3-add6-bf78b84bb50d | -6.72471 | -58.44603 | 2024-10-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dbdf17f-b3f0-3a62-be76-0bfd4d276a0b | -6.52813 | -58.419 | 2024-10-11 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e6b9129-394c-3d75-b98e-2de431a3ce33 | -6.52759 | -58.42246 | 2024-10-11 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7020c75-7632-37c8-9b81-97303b176b30 | -6.52752 | -58.40113 | 2024-10-11 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6571a93c-371f-3a4e-8aae-ae65cb79b148 | -6.52367 | -58.4041 | 2024-10-11 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bda83aaf-09db-3d4b-bab4-9c22c0286bb7 | -6.51652 | -58.40655 | 2024-10-11 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b18fbbde-cf36-3057-9fae-3160403e98d8 | -6.89259 | -59.0465 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80db6ba5-7578-3046-ae17-16ff1dddf240 | -6.89254 | -59.02529 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d1a4b57-82e7-38bf-ba17-529ee9762d98 | -6.892 | -59.02874 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8aef3478-db77-3c1a-92fe-40466819528a | -6.88924 | -59.02477 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f98dad8-b398-3548-a2e4-142cebfbeca8 | -6.86328 | -58.97477 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f4896c9-de4b-3af6-a0f3-8bda8effce9b | -6.85862 | -59.09064 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fcd3416-b74a-328a-87e9-56e5ee7e6aba | -6.85808 | -59.09409 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63587c28-e540-33fe-abd4-8dbc142e1979 | -6.85533 | -59.09013 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd20e0fa-25c2-3ebb-ad53-2c7d89999c49 | -6.83391 | -59.09737 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7e07528-b339-342a-9fe2-091d310c9663 | -6.81704 | -59.0275 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9dd4fb-cd62-36a6-afb8-36269a3c3a79 | -6.81541 | -59.03785 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 334a0245-d827-345a-a730-453123b8081c | -6.81487 | -59.04129 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04c4c8e4-766b-3bfc-9169-fb62db5ec1cb | -6.81255 | -58.99147 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6798dab3-cfa0-3da7-a579-491abc197390 | -6.76717 | -58.87128 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 628548e2-e61d-3f48-8de1-d96f865b4036 | -6.76123 | -58.90922 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4de8cae-2bd5-3bdb-9856-1809790253db | -6.76107 | -59.06112 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 205d6ff0-049c-3e3a-b5bb-d21ee86f0b58 | -6.75777 | -59.0606 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86fc9a46-6bdf-38c9-a4dd-364521e7e3d1 | -6.75079 | -58.91112 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dd23955-aa9b-3d1f-91ca-d21076a9140a | -6.71641 | -58.99686 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 561c668a-0941-30f5-a426-3244456b66b3 | -9.30628 | -59.23547 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 733dd90c-dc23-3430-97ce-2612332a0dc4 | -9.30476 | -59.28871 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ac6c70a-77e2-3951-8bbc-0ed8914fa934 | -9.11207 | -59.53946 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e70f9061-bde4-3b71-88b7-a993d42087de | -9.10878 | -59.53894 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3718309e-84f3-3445-9e2d-98ec9f300106 | -8.80964 | -58.1982 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d35e4af-b20e-3034-930a-7d19b92a4432 | -8.8091 | -58.2018 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 609e3598-ce1c-37ca-ab53-609908a7bb86 | -8.80574 | -58.20129 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 942247ac-89c7-36aa-974b-13785e828331 | -8.36282 | -58.16925 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eae075e-9b1d-30d7-9fc4-f49840d43310 | -8.36058 | -58.1837 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c804d35-c786-3ba9-9ff4-9acbc3c1eb03 | -8.36003 | -58.16515 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32da248d-eaf1-34e0-86ab-81b7c51e4377 | -8.35948 | -58.16874 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8eb8209-2311-3ede-b86f-bbc7e6345b7f | -8.28307 | -58.15313 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc69ad5d-aa50-3dd5-9eac-3dc2e1c652e3 | -8.26761 | -58.78203 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03bbc8bf-1848-3ba1-9840-adb9456d6aef | -8.12333 | -58.04427 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 220d2e1d-a8b1-3dcf-95b1-dc57bfcbde56 | -8.11998 | -58.04375 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ac731c4-a558-358f-a077-a3841f92e3b4 | -8.11718 | -58.03965 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4e7d206-c216-35a8-a53f-678a37e89d88 | -8.11663 | -58.04323 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ae7c795-c1ba-3c5d-a1b8-3ac659b4c848 | -8.11608 | -58.04679 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 759568ab-3095-39ce-b7da-cf0b54f4e102 | -8.11437 | -58.03558 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7984522b-07c2-3715-8ea7-53be2155e93a | -8.11382 | -58.03914 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7e7b8db-089a-3bb1-b1fa-b44024fb78bb | -8.11328 | -58.0427 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db136525-b86b-35cc-934c-4d73198c5515 | -8.11273 | -58.04626 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3025bbe1-a3de-37aa-9bde-e8ce19c63178 | -8.11047 | -58.03862 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f98c8e0a-8a09-3953-b1fd-a9a4cfd34d15 | -8.10993 | -58.04217 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d178d08e-c60a-307a-8b3b-39802be0ce92 | -8.10938 | -58.04573 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fb825aa-a4a9-304c-a9f6-5a11534837bc | -8.09085 | -58.00982 | 2024-10-11 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d41dbcb1-de7a-3461-9b30-c94d3ade0113 | -9.99016 | -59.53749 | 2024-10-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 620224cd-ea07-3e90-bbcc-001f1451708f | -9.88949 | -59.5071 | 2024-10-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81172ec1-864d-30fd-9e62-c414da7087ac | -9.77394 | -59.26746 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fc40c6d-b5f3-3617-be96-95b6fb67a41a | -9.77063 | -59.26694 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 74711b5d-b883-3690-8b38-734f5882a070 | -9.72131 | -59.27653 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aa3e4e8-ed99-38aa-a4c0-467733e9ecc5 | -9.70593 | -59.04845 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README95.md)

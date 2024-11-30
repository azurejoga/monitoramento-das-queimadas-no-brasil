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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1491935f-cf1a-396d-a300-55a422c25aa4 | -1.14989 | -51.7062 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09960a67-323a-34cb-b7b8-df9546517d6b | -1.62924 | -53.86285 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c3d21d3-9b0d-35a0-87b2-5fd4afc4a320 | -3.24387 | -53.64575 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d02cbe8-3dce-3283-9f46-b29f847bc966 | -2.85194 | -46.69283 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0210f508-6a8b-3429-8d8a-74ea31c82b4c | -3.05873 | -49.53612 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5ae0f41-e465-3ac1-a32e-495e2a002e60 | -1.67808 | -52.52296 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fac00b7-75bb-3601-bbdf-25770e4d6812 | -0.95282 | -51.653 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6763e51d-7451-3311-8e5d-06dad7763b39 | -3.30719 | -50.27959 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3e8b689-4bf2-314c-ab7f-838085ba2355 | -0.98233 | -53.67736 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 083b2a3a-604a-30d1-b9b9-ebad6fd4c04f | -3.03564 | -54.0411 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6939562e-3c1c-3d52-a20b-01c5e008223e | -3.07134 | -50.33287 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76bcc9c4-347d-30ec-8708-220942f26f88 | -3.04485 | -49.37171 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 546fa58d-5273-37eb-92e9-49b5fdcc3bda | -4.87188 | -41.28929 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a99de687-8fdc-3ba9-904d-1e88e83e032d | -2.89052 | -54.16927 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b09feede-effe-3683-8c44-5dbee31b8a9d | -3.83011 | -50.13794 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 010e4c1d-0921-3c1a-8cdf-7f402d6fd7e8 | -3.47109 | -50.53961 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7997406-6a7e-3fa0-a5c4-162855764be7 | -1.69571 | -52.45595 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a422a32e-e59c-3848-b4da-db33836f807a | -1.13217 | -53.39437 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b01d520-ee2d-32b3-9a94-648f2067eb21 | -1.37893 | -53.64891 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5625c0b4-8159-37db-b85d-793d3cab9283 | -3.16186 | -46.2955 | 2024-11-30 05:01:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 662f5a8a-1595-3589-b7ca-7b7889752e9e | -3.24556 | -53.63498 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82ea96fc-7e4c-382f-bf2c-88f26b918985 | 0.98748 | -50.27172 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07c03f5b-483c-3764-bb83-0e2abac6b101 | -1.14375 | -53.70198 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6abe7470-1eeb-3e95-8afc-69391256fe08 | -2.79893 | -54.12656 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac46b71d-d5da-3ff9-9772-d15aebff1016 | -2.6555 | -51.71025 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6f484fa-1185-3494-845f-cc131c80c8d6 | -1.71067 | -52.47379 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83ec74ff-12d7-314c-a2e3-9f3a745e4b9b | -3.27465 | -50.43993 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a52afcb1-7f00-3452-bc09-9456548d1662 | -2.80701 | -54.03113 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d72f12f-c749-3df7-9882-549a19ff1ce6 | -3.1927 | -54.33403 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeb4e22d-e303-35c1-a7d5-350351237c6d | -1.7897 | -52.74628 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edaeeaba-44b9-3170-b99a-e91c4f4118a1 | -2.37041 | -56.11453 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b13605c-252b-344d-ad06-58267f6aab8f | -2.15473 | -56.02233 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecb3f83f-b2ed-378e-b36e-01ca3e11c95a | -0.56349 | -51.69384 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b17277f6-5201-381e-8a8a-87698e9e772c | -1.09972 | -53.40383 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3830b4d-e6f4-3218-b7a2-abb57308ca0f | -1.39854 | -52.5652 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df2e5af5-5feb-3170-a071-a220dc16e3c2 | -1.0868 | -53.35465 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f19b2707-0658-3268-b13f-362782acbd40 | -3.63945 | -54.44263 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca2e09e-fd3f-3126-a345-fbf132bc7a7e | -2.92356 | -54.26353 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6510234-3cc5-3676-b2aa-f425781cb1e4 | -3.25787 | -48.89355 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec4601ac-ae63-32b0-9b82-1981ac049abc | -2.0089 | -53.03939 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48e91841-64a6-34cb-afbb-04126b3c0ac6 | -3.11114 | -53.75634 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8cf25ec-272d-3cfb-a49f-356b149a4f47 | -2.54563 | -55.2239 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2c81311-0a88-32c3-9338-532d49b83b67 | -0.26826 | -51.64754 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96fd658e-db8b-3326-8b74-fc05b6c885ed | -1.68477 | -45.78037 | 2024-11-30 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48fa7297-f02b-3744-a773-8e497da374ae | -2.59389 | -54.09779 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95569af2-3c03-3307-8f98-617204a81b65 | -3.25569 | -53.63658 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 42c9f1d9-3ea8-3157-9867-7a9484189486 | -1.70792 | -52.44617 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 177ec970-8b0c-31f2-8db6-514ef4ed1c3a | -3.24872 | -53.86494 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 684c6b43-85d6-392c-91d4-13617b9f22f9 | -3.40117 | -50.65929 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 17fe5c6a-5acd-346b-91c7-f8784c97633a | -0.58477 | -51.69714 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ea239bc8-fc85-34ba-addf-9a84fa714b6d | -3.35517 | -49.56366 | 2024-11-30 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d70dc7d-db81-33fc-b633-a65421368964 | -2.60525 | -53.98156 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6724883-a265-3525-a7e8-9f09cd697df5 | -4.25095 | -46.37445 | 2024-11-30 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02f7e13c-3a0e-3a38-9ba9-f3362403ac04 | -3.26476 | -51.62109 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7139be9-c6ea-35e1-b613-79cd1e5ca264 | -4.00573 | -50.35033 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1c27823-1d0f-37c2-98a0-50855fb0fd45 | -1.70612 | -52.45756 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6b97a51-6f62-3aa5-9c3c-7f0a07c4bcb8 | -2.58253 | -54.21383 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 253d3f9d-55a8-3a77-b844-f93648f8d39f | -2.11733 | -50.62971 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3fb541b-2d50-36e4-82c4-d2b6a2ba4594 | -2.68914 | -54.13818 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 628a55c7-5855-31c5-83b5-8b41b36b79a3 | -2.44111 | -53.88808 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b845b41-3cd5-36e8-9ce5-464fc6f3a3d4 | -1.18861 | -51.76145 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4036976-0b44-32b1-9a18-eb922de4f550 | -3.53006 | -50.75494 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a835f73d-7738-39a5-afce-019a79f00378 | -1.45722 | -54.48467 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71359a78-d219-3add-be3e-3e70fa1666cb | -2.61749 | -54.20851 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe8ebcce-684d-3d52-a43b-158ac55ae4ea | -2.84775 | -46.68626 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 447377d8-0aba-3deb-89ef-4729ab741183 | -1.27049 | -54.55434 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0e25e2ae-e60b-3719-b685-a8c7856611bc | -1.20894 | -51.73861 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1d451f7-0d47-3260-951b-fabeb5b1b72d | -0.56704 | -51.69439 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 297c8c2f-00d6-3764-8c9b-40446e9a7964 | -2.98774 | -53.74484 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03027507-851c-35d4-ae7a-ad9e2634b547 | -1.06546 | -53.21712 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41ab5420-4ba4-39d1-8b6b-86f22abf552a | -3.11646 | -54.47884 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 782cabce-babe-3000-abe0-ca400aeac124 | -1.10382 | -53.59551 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 589d02eb-19ab-3807-b6f2-51a74650cc8b | -3.96284 | -50.19387 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49fecfea-3831-3806-b370-601bf6659282 | -3.25412 | -48.88874 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 094fe2a0-49d8-3de7-b44d-5574eb583014 | -1.15691 | -52.23588 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5faf7408-6eed-3308-941c-e1bc693eed8b | -0.13832 | -60.86349 | 2024-11-30 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcc5853b-5303-31ef-8b93-67b9d36fd4dc | -3.50598 | -53.82412 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e2e4466-ee29-395b-8ea4-507a63865fa7 | -2.23105 | -53.62791 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04334fc8-c8fd-3d03-8659-0e7edfba4a35 | -2.6047 | -53.98506 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79619c68-d73d-3ccc-a302-9486d1e371b9 | -3.34076 | -53.3154 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 327a606a-458c-3f22-9069-43faf5807043 | -2.98122 | -53.87437 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7dd7be0-be38-3b4e-817d-2d1632a1b659 | -1.30023 | -51.73092 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b7e5165-39fc-36a1-84af-c47b1657e6e4 | -2.80447 | -51.58929 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9efc7e0e-09c7-3be6-b014-c47ed746b658 | -1.70157 | -52.44131 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1301323a-4ce7-39b4-ae25-289adcad4fa0 | -1.70445 | -52.63773 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 084421f1-0624-3950-ba71-1ee19272974b | -3.71325 | -47.14545 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dd8fac7-fba7-384b-a67e-a4e1e9b97d20 | -0.19859 | -51.53991 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24147fe9-436c-36a8-8d65-600f531bc901 | -2.80822 | -54.06717 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aafae472-cdd5-3b69-a175-27c0aa14951f | -1.3038 | -55.74114 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99f8c451-a241-3d1c-a037-f8d9bf6c91bc | -4.07799 | -50.03176 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7590a12-6ffa-3c6f-9963-cceb016924d2 | -1.36897 | -52.5574 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12a1e4b0-79ee-39d9-b3a5-bceb17cb9fa1 | -3.19658 | -54.33107 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e785d038-fa2f-3cf2-ade1-8facc728fd16 | -0.23758 | -53.76029 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 611ff567-fcbd-3def-903c-84f648a6476f | -2.57571 | -53.97339 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0f83cb0-84fe-3b17-9dd3-d78a178649bf | -1.66114 | -52.40392 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6421861c-801c-345c-9c0a-fa24e9aaff77 | -1.59399 | -52.27676 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fb745d0-0e4c-3e35-afea-ef09a2c6cea2 | -2.2639 | -53.46183 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ba763fd-3635-39cb-acde-9534d73deca2 | -3.72431 | -49.21041 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b72900cb-9325-3ac3-9294-b94109282175 | -2.97014 | -53.92316 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27edc383-57c4-3fd9-b653-21bfab1fde54 | -2.89161 | -54.1623 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README106.md)

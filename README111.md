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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b23f1778-b7fa-3a80-9c2d-3fd69d049ce5 | -2.61084 | -53.9896 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a29ebc2-20cc-396e-9661-7bd085f02aee | -1.53545 | -51.62032 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c8fcf23-5542-33c9-b027-610e9a3006e2 | -3.2142 | -54.08685 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 763329b7-ff6a-32e1-bf50-b70e2e564274 | -3.09876 | -53.72528 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b80f2f4c-3167-35e7-abe1-eb410a087cff | -1.68564 | -52.08338 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c900021-c93e-3c33-844c-4ae2e7514865 | -1.66829 | -52.51757 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea4f8732-c7b8-35c8-b6ad-bad944377123 | -4.11034 | -50.98148 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e53a08f2-2a3b-305c-aa65-00579dcb8574 | -2.47881 | -50.36819 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2605ec8e-0f73-3ed5-b36b-66f5f8bfd561 | -3.14094 | -53.84112 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a64ca86-eecb-33ec-9856-0683eec94b50 | -3.29676 | -54.12841 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce655fa6-2711-31d8-8ace-3df542932b3e | -3.10954 | -53.81048 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fa4e29a-81f8-31e5-a64d-9290f4b66095 | -2.63219 | -54.07162 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2d65e21-b50e-3542-b843-a20a3cab5a84 | -3.27934 | -50.43559 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ecaa590-ca51-3856-ae1b-182d1f3804b2 | -3.04293 | -54.06019 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bb32387-4367-32ff-98d6-fe28ba53d845 | -3.31516 | -53.70393 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c469d28e-5eb6-329c-9d1e-4a019cb2f7fd | -0.98583 | -51.7592 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 582b3bb4-d9fd-3d4d-b78b-0ff418f30411 | -1.97267 | -52.89153 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c808e32-e20f-383a-a996-aa13a3e1e71f | -3.6228 | -42.74062 | 2024-11-30 05:01:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc2a9fef-b926-3314-bf20-708b591bea03 | -1.58564 | -53.84178 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4550d479-e9d1-39ae-b702-c4c122299202 | -2.45079 | -54.00072 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 671ccdf1-3a74-3728-b02f-f5524d8a7a10 | -2.13892 | -54.88429 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ca94e2d9-6547-31c3-bbbf-0caf85dcfed7 | -2.51493 | -47.41812 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7c8eb19-2783-3cf0-8fc2-f822586e493a | -2.304 | -46.5464 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| babf7b84-0ee4-3600-a141-c6323f5928d2 | -2.26952 | -46.43249 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 054031eb-ae67-3ea7-b049-46df122bdda4 | -3.28068 | -54.16536 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d012dcd-87fa-342c-8237-5e8565aa05c2 | -1.65738 | -52.49656 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa104093-e886-3ec8-9299-f84fa0d8f3e7 | -2.54896 | -55.22442 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8a4e6b8-e1ce-3e1e-81b2-0e0ffda9420b | -2.88773 | -53.99697 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77e749f9-df1f-338a-95b0-e7ae487569ca | -2.62713 | -51.77396 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e6ec466f-1821-3dfa-b2d1-1ab49e64eba5 | -2.88715 | -53.9789 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca797d45-a44c-3fa8-9767-57c3a9cf9a73 | -3.96845 | -48.09573 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11278553-af67-3d7e-9e8f-aff7532debb1 | -3.86384 | -50.16113 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e93467b-d486-37f8-a35a-b813ae0fe571 | -2.83096 | -54.03125 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fed6ee1d-34d1-3a45-a69b-8093c8883347 | -3.11368 | -54.47485 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92de070c-eac6-39ea-a397-030eabfbea66 | -3.78799 | -46.69753 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b2eb6a1-3dff-370c-b048-99be6adff833 | -1.45891 | -54.49551 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5b3d33f-c530-3662-a3ac-52ac117cfd6c | -1.36613 | -54.65746 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d761b953-5422-342e-b2c2-8f8ca4c6580b | -3.78065 | -46.69444 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 015fd2ca-ff65-38a9-b4ee-159d87395f11 | -2.59832 | -54.09134 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72297aa4-e15e-3564-a678-f657a05f4bb9 | -3.06334 | -53.68676 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7a54ac1-dc0c-3a2b-bfe2-773b3ddcf089 | -3.29036 | -53.28209 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14a80f6b-e911-31be-8684-7435b5b03f35 | -3.54595 | -50.18123 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7459403-03dc-3197-b084-57609a2f0d2e | -1.1461 | -53.75229 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fc94b84-d047-3b27-ba66-0cf09cf6b8c1 | -3.52711 | -50.38416 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26062afe-ae75-366d-986e-1867dcf0790a | -1.12522 | -53.62372 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a78aae7-691f-3e61-8a9c-a7ecd6c67b7a | 0.93967 | -50.74154 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e85f032b-49fb-3cc9-957f-3b2b4cbcb24b | -2.8699 | -54.00138 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a77a5755-5c0a-3f4d-a151-61111289e35f | -3.22135 | -53.61279 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1841b448-5ee1-3a1b-b719-d5c79871c1ac | -2.37949 | -53.68032 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64a5c259-ed49-357f-a825-6375615a9872 | -2.43413 | -54.0196 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b701c5b0-5ada-3c26-aa55-2bf7ab211bed | -1.68285 | -45.78314 | 2024-11-30 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d93e166b-c720-3132-9469-0a8f0c4007b7 | -2.96368 | -48.04224 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46bd3d33-cfb4-312e-bd92-f798b1f1da9e | -1.31094 | -51.73257 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67aeff69-e26a-3487-bd4a-01a20f9d0259 | -4.17451 | -48.62822 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 371d965c-fa4d-3f22-ab82-b6c0df01a5a5 | -2.19387 | -50.58112 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2c5d1e4-942f-3f5f-acd3-e2b68868ba4d | -2.95626 | -53.70356 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74e16639-bba0-3e7e-a2a4-fe5944eb2c5b | -3.39216 | -50.32045 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 149eba02-8aaa-3f71-b24f-1bc498b444c8 | -3.42022 | -53.88029 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 603bf08c-05de-32de-a160-7bc9e38ce489 | -1.4925 | -54.45485 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dae93283-b9bb-3700-a9ae-bcdb4dca4b35 | -1.1193 | -51.90117 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 978e12d5-1c45-37f8-8037-904d7d54303c | -1.11087 | -52.30281 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 215fe141-6ae3-307a-b69b-5bc5453b4e20 | -2.24141 | -50.48384 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab168f46-1697-36ac-8e37-0aac60a9d08f | -1.45071 | -52.61526 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e2936a9-3071-3ef2-8ebb-4b992584a11c | -2.94309 | -51.58718 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8672f32-48bd-378e-b123-5d9b4bdca4f0 | -4.67739 | -48.15606 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13177f4a-6ea2-3453-a3bd-20088a4a6191 | -1.67098 | -52.40933 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2f614f5-78a4-3fbf-9c08-09b48b6a1a1e | -3.29995 | -53.69067 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4be14ad3-6a28-3130-99fe-d956c835589c | -4.44645 | -46.3522 | 2024-11-30 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 384d77e4-2fc8-3edc-9187-9c7009ac1e05 | -0.99974 | -51.7164 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a14379be-b28a-3bd6-9019-3129cb7a6d49 | -1.09521 | -53.36684 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 783714a0-379b-3e2b-a65f-c3d8004f7bc1 | -3.38895 | -50.31478 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6df7a48-fe96-33be-b3fd-e2813e1c5d2a | -4.87832 | -41.29636 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c92ae85a-c582-36a7-b3f0-107332474c75 | -0.96825 | -51.71696 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5443cc5a-d96b-3863-b580-67786864ffae | -3.84393 | -52.02121 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 534620e8-6d7b-3cb0-aa65-8e51419eaaf3 | -4.12978 | -54.89916 | 2024-11-30 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dad7c09a-f3b9-3a48-a92d-7e1b41c6f991 | -1.16619 | -53.77668 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b24b1824-9770-3483-9f44-f61acd63be02 | -1.87191 | -53.9577 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61cc0bff-4272-3ded-9034-c68fb323f2c8 | -2.19864 | -48.34195 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ad1d1a5-5119-3349-8f85-b1f665e9038d | -1.20058 | -51.74552 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0652fe56-59cd-396e-9b86-673e7c5f623f | -3.09693 | -54.02181 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9247cd3-8dc6-3d7e-9997-dddf1f0fd3f8 | -1.11875 | -48.33831 | 2024-11-30 05:01:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04398409-5700-3905-b49a-f3c8c9327e89 | -0.1944 | -51.54336 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de0169b9-4f5a-3e34-ac36-ebad697bf565 | -2.8081 | -54.02412 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c926b230-08be-3b49-8ee8-aef64351b152 | -2.86931 | -53.98333 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2be1c350-2161-3996-913a-e43fbc0615ed | -2.68114 | -54.2546 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cdbf267-9f24-395b-9c43-52f736f7ad10 | -3.69958 | -47.12926 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c14fd17c-f467-3c0a-a75b-f0de16d8cca0 | -1.68154 | -52.52349 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91878337-5454-367a-9b6c-f52f95e68c9e | -1.95468 | -53.34187 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaa695f3-28a3-3c3b-8944-527623cf2f94 | -1.19515 | -53.87032 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aebb607a-742c-3095-b9a7-92d36331fed6 | -3.23658 | -53.92089 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3ee2b3f5-3f29-32c3-b757-7b5110a310cb | -2.81199 | -54.02114 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fc6c6cd-3ce3-315f-b601-7e6f4a0a15a4 | -3.514 | -50.25656 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0449ea34-e5ed-36d2-820f-68b86a42e62d | -2.45587 | -53.70651 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d362fea2-076c-350b-afa9-e73582843cb0 | -3.01945 | -53.40834 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24d9bd02-1785-3c1d-8758-13209e132ab3 | 1.21861 | -55.93174 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b4c176a-a337-3842-ac4f-01767df04c9f | -2.85381 | -54.03838 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7843c80-faca-3afe-bb9c-0f05a26e989d | -2.69587 | -51.97993 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d54d4f2c-afc0-3d7f-837b-bdec1f1cfb90 | -2.76182 | -54.06729 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 594f3bf9-d0d9-34f0-976b-2741585cadf2 | -3.09583 | -54.02882 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b258143d-8f8a-34d0-a4a8-d46666de84ef | -3.92911 | -51.17625 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README112.md)

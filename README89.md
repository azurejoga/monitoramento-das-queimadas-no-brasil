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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7925ab5-4fe2-3017-a14d-aaa5f55538da | -8.09958 | -71.2482 | 2025-08-28 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94a747b5-9d93-3cff-9de7-c47a6a8f69f9 | -8.09435 | -71.24742 | 2025-08-28 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1789258e-9328-39f3-afd8-a9fd633e17f1 | -8.57893 | -70.11793 | 2025-08-28 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dacad61-c4a7-3028-b990-d66e5a32b065 | -8.74349 | -71.00174 | 2025-08-28 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 528b249c-9339-3c82-b9c1-56788ff5660c | -9.134 | -65.7694 | 2025-08-28 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| dbfa040a-8a3b-321d-96fd-6b17590a13f7 | -6.1932 | -42.5259 | 2025-08-28 06:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| b2589229-b9e2-302d-99c4-abbb524e152e | -9.6627 | -48.3159 | 2025-08-28 06:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5ee9215b-cf88-3a7c-8f97-647ae390d8e9 | -6.178 | -44.0688 | 2025-08-28 06:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 73ba115f-8a49-3425-8554-088ee62c3981 | -9.1154 | -65.7886 | 2025-08-28 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 230.2 |
| 9782eea5-c4d9-342b-9434-8ea51d100472 | -6.8772 | -43.6152 | 2025-08-28 06:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| dc765ca6-fcfb-382e-ae9c-27083c217d5d | -6.896 | -43.6135 | 2025-08-28 06:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| f2fe99e8-3cd3-3cea-ae02-0a1ad8da67e0 | -9.1155 | -65.7699 | 2025-08-28 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 716cd8ea-f976-33dc-8b80-bf9e90ff3164 | -10.5371 | -46.7119 | 2025-08-28 06:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| acbbeea6-897e-3050-abbc-25a59744b6ae | -10.4738 | -57.9366 | 2025-08-28 06:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9ffd80c9-0aa3-3edf-b8fe-65bb5b7955ba | -9.1339 | -65.788 | 2025-08-28 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 46381c43-b88b-3387-b192-0cde7982a061 | -10.5561 | -46.7095 | 2025-08-28 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 100488f1-0048-368c-a56e-183d7bb6c0c8 | -10.4738 | -57.9366 | 2025-08-28 07:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6bb19096-c28c-3468-84ad-4af58ed2486b | -9.6627 | -48.3159 | 2025-08-28 07:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b385e669-0824-33e1-8fc5-8128566290f4 | -8.2893 | -45.1586 | 2025-08-28 07:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c8d7f2f6-84ac-3f40-9b4f-180bee04d39b | -6.8772 | -43.6152 | 2025-08-28 07:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| d0def4aa-0a11-3610-bb26-876cb170120f | -9.1154 | -65.7886 | 2025-08-28 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 242.3 |
| 1623175e-ce0d-3581-9c7c-9049ecbb30b5 | -10.5368 | -46.7343 | 2025-08-28 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 68110ef0-7ead-32e4-bdcd-233f8383d5c9 | -10.5375 | -46.6894 | 2025-08-28 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 387917fb-8138-37d4-8325-78a65c7efc65 | -9.1339 | -65.788 | 2025-08-28 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| ee3801f8-a855-3e26-9ff3-44cee6ff922d | -10.5371 | -46.7119 | 2025-08-28 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 0533f34b-1c9f-3d3d-9ea8-3bf7261c3bd3 | -9.1155 | -65.7699 | 2025-08-28 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 2e7e22d7-3ed9-3e99-89ec-da5c5cf5fb3f | -6.1932 | -42.5259 | 2025-08-28 07:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 683c2296-a5bf-380b-b9a9-50310ffb0ae2 | -9.134 | -65.7694 | 2025-08-28 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 50131189-39b5-3300-9033-198e87998357 | -9.134 | -65.7694 | 2025-08-28 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d9a6ce87-f5cf-389a-980c-d053b02c09b7 | -9.1154 | -65.7886 | 2025-08-28 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 245.3 |
| 0aa30382-e4b7-39e9-b213-af116c39ff39 | -9.1339 | -65.788 | 2025-08-28 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| ffa5fcf6-3ea5-35ec-94c8-bec0b5d2aa36 | -12.6878 | -48.1677 | 2025-08-28 07:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| ad0689a0-69ea-3f00-a9a2-35b5e04ab5f9 | -11.6116 | -46.211 | 2025-08-28 07:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 82cca7bb-9506-315d-97ab-1989e73c4cc4 | -11.5925 | -46.2136 | 2025-08-28 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b7cded05-b452-343b-b4b0-fba3f4866b6f | -6.8772 | -43.6152 | 2025-08-28 07:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| d7f4d07c-1aa8-31e7-9bb5-fa312a63ffac | -10.5375 | -46.6894 | 2025-08-28 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 27703cae-d38f-35b0-861b-8efa51e04d6c | -10.5371 | -46.7119 | 2025-08-28 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 87fcc950-975a-39e5-a0aa-0d1c81c97b84 | -12.9662 | -44.5781 | 2025-08-28 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 0eed4add-192a-305d-b919-fdf75cd8a471 | -9.1155 | -65.7699 | 2025-08-28 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| e95841cb-ba0c-3d4f-a3e5-78122bab4323 | -10.4738 | -57.9366 | 2025-08-28 07:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7a1d3e65-d99d-3029-ae3c-d208bb629693 | -14.3696 | -52.0813 | 2025-08-28 07:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f22524d8-119c-310b-a01e-7a2a41f7b227 | -8.2893 | -45.1586 | 2025-08-28 07:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 24f99977-43c6-31b3-a265-129b8db50009 | -8.3082 | -45.1566 | 2025-08-28 07:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 46780b2b-0457-30a1-84a6-f195a04f4b71 | -9.1339 | -65.788 | 2025-08-28 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.4 |
| a632c915-4f69-3410-abc0-02def2894690 | -9.1155 | -65.7699 | 2025-08-28 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 86aac928-6249-3056-8286-08b21a94b0a7 | -10.5375 | -46.6894 | 2025-08-28 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 1201c39c-8fc8-3700-aa25-6ff1242e3138 | -10.5371 | -46.7119 | 2025-08-28 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 181.0 |
| edf23d8d-d089-3a11-b6ab-d3cb6276259b | -6.8772 | -43.6152 | 2025-08-28 07:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| d103fcfd-8eaa-3f6e-9ef2-84d0dd43088a | -10.4738 | -57.9366 | 2025-08-28 07:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f06deaa4-2b02-39a9-a3e4-6a8b521a3972 | -9.134 | -65.7694 | 2025-08-28 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3937c835-3848-3473-abdd-dc1214fbec49 | -10.5561 | -46.7095 | 2025-08-28 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 88ed65fe-b193-386a-98d6-5dbead73c4ff | -6.4355 | -44.5764 | 2025-08-28 07:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| f64817bb-4b72-30fb-8286-dab361c6aa88 | -9.1154 | -65.7886 | 2025-08-28 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 189.4 |
| f4e0dfdb-9a4d-30ef-859c-e7d2c8416160 | -10.5565 | -46.6871 | 2025-08-28 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 119e9ea3-9c0d-3c51-9799-a7c2a1ce3002 | -6.4355 | -44.5764 | 2025-08-28 07:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ee4b5a7c-7a85-361c-ac14-71371df393ff | -9.134 | -65.7694 | 2025-08-28 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 647891db-ceed-3818-8d94-2cf203578824 | -6.8772 | -43.6152 | 2025-08-28 07:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| e0031fdc-dd0e-37e8-9c22-e1e1c700fbd0 | -10.4738 | -57.9366 | 2025-08-28 07:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| fa2583de-ce66-3322-9aee-79ad863601f1 | -9.1339 | -65.788 | 2025-08-28 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| ca714767-c1f8-35cc-8b95-49d56fe4df9b | -9.1155 | -65.7699 | 2025-08-28 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 81dfda2c-f619-38d6-8ab5-ebda8f00c202 | -6.896 | -43.6135 | 2025-08-28 07:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 88a7da6d-1a75-374e-8cbb-75b27d538989 | -6.4543 | -44.5749 | 2025-08-28 07:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 638d511c-830f-38ad-af44-e1fed0823e1c | -9.1154 | -65.7886 | 2025-08-28 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 074da512-3e52-3333-995d-15aac6b74127 | -6.4543 | -44.5749 | 2025-08-28 07:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c51f159f-1e6c-34bd-9f7d-8785cc67a241 | -9.1339 | -65.788 | 2025-08-28 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a4a86d54-c7e8-39ce-ac5d-8024b9290257 | -9.1154 | -65.7886 | 2025-08-28 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 196.8 |
| 8d2a94ef-a015-3921-85e3-5bfdc7d31a54 | -12.6878 | -48.1677 | 2025-08-28 07:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 448bee0e-aeb4-3903-805f-584a62c338b1 | -9.1155 | -65.7699 | 2025-08-28 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 3ae10c90-6a32-3052-8b9d-077a142a9cfd | -13.2075 | -46.0421 | 2025-08-28 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 6061a477-218b-3ca8-884e-e6e54be14434 | -6.4355 | -44.5764 | 2025-08-28 07:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 9f6588ac-5f9d-363d-8725-8b857307a478 | -10.4738 | -57.9366 | 2025-08-28 07:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bc9fdd39-10be-3d8d-aece-a5b724a4c0ed | -6.8772 | -43.6152 | 2025-08-28 07:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 150.6 |
| a40e07ad-c540-36fc-881b-958fc4f14c20 | -9.134 | -65.7694 | 2025-08-28 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| c459aecd-5866-32b5-9269-daca77911046 | -6.8772 | -43.6152 | 2025-08-28 07:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 9cfc0167-c03a-34c3-9d33-6c54a9897942 | -9.1154 | -65.7886 | 2025-08-28 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 6e746325-9c11-3fce-80d6-429c86ec7001 | -9.134 | -65.7694 | 2025-08-28 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 760a5b74-c134-300d-915d-a90917c01d9f | -13.2269 | -46.0391 | 2025-08-28 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 50d25d20-236b-3801-9f81-50da6687e591 | -9.1339 | -65.788 | 2025-08-28 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 52c211a8-1f1b-39c8-93e4-89de3d0d6df1 | -6.4543 | -44.5749 | 2025-08-28 07:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ed31be79-39a7-3c84-9a13-b2b2190c0673 | -9.1155 | -65.7699 | 2025-08-28 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| f9f11150-d6f4-3e7b-a1b1-176a3591dbdb | -13.2075 | -46.0421 | 2025-08-28 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| f1bc0dc4-f023-3082-a494-967c71a177cf | -6.4355 | -44.5764 | 2025-08-28 07:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 806aa20c-292d-3a16-bd76-70af061f8dae | -10.4738 | -57.9366 | 2025-08-28 08:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 49314c19-27d1-37c9-a676-5058642c5530 | -13.2269 | -46.0391 | 2025-08-28 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 586299ce-ca22-334b-99af-6bd78ce11dc8 | -6.4543 | -44.5749 | 2025-08-28 08:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 7953a329-c752-3779-ad3c-d86dfc8832b4 | -9.1339 | -65.788 | 2025-08-28 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.2 |
| a382ce8b-d801-3dff-a73c-3a6c9796be92 | -9.1154 | -65.7886 | 2025-08-28 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 2aba7c83-27fd-3d46-9e04-cc12b28f3b60 | -6.4355 | -44.5764 | 2025-08-28 08:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| ee737d65-c88b-3493-ac36-42f30d1a8889 | -9.1155 | -65.7699 | 2025-08-28 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| f3ce7d68-d1db-37e0-a160-f1f153f5a7e3 | -9.134 | -65.7694 | 2025-08-28 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a7b46da0-52ef-344c-83ff-c28c1186e262 | -6.8772 | -43.6152 | 2025-08-28 08:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| ddad144d-96f2-3796-bd89-a8a7550e5a38 | -9.134 | -65.7694 | 2025-08-28 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 34693c81-513d-3f43-9b80-c70d87180df9 | -13.2075 | -46.0421 | 2025-08-28 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| a79cf930-2c40-3cc5-b38e-8689c4bf0691 | -9.1339 | -65.788 | 2025-08-28 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 20085936-66d9-36dd-ab1f-bc599353fe9e | -9.1155 | -65.7699 | 2025-08-28 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| dc78ad28-e33c-350a-a906-cbe312452b86 | -9.1154 | -65.7886 | 2025-08-28 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 183.7 |
| cb725a94-3e7b-3c0d-bd1a-0534e7002fba | -6.8772 | -43.6152 | 2025-08-28 08:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 3209b814-c151-3af7-8013-c9bc3850f6a8 | -6.4543 | -44.5749 | 2025-08-28 08:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 24d231ed-fa9a-35f8-8510-cf13ebc49027 | -9.134 | -65.7694 | 2025-08-28 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e39f06c0-7aa9-38a1-aece-24ae20dc7353 | -14.3696 | -52.0813 | 2025-08-28 08:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |


[Clique aqui para ver as próximas entradas](README90.md)

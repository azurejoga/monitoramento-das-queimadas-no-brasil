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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 629db6a8-977c-3b54-88bd-b7c7b034c930 | -12.5033 | -58.4781 | 2026-05-05 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 200.9 |
| f60d0dbe-cf0d-3d6a-8952-c52adf2c70d3 | -12.3512 | -50.005 | 2026-05-05 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 262.5 |
| dbc62988-9a2c-3490-9cad-75f07e1f8285 | -14.1502 | -45.3543 | 2026-05-05 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 62c520df-9f65-3c6c-8e41-c586a40c52c7 | -11.4449 | -55.0996 | 2026-05-05 13:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 4f8174cb-24cc-39eb-9df8-c8e48e41eaf9 | -12.3508 | -50.0266 | 2026-05-05 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 5383847b-592a-3bd1-b5c4-8df13556fc12 | -12.0097 | -45.3315 | 2026-05-05 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b6c966bf-4812-3245-abb1-460b848098a9 | -14.0272 | -47.5898 | 2026-05-05 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3d283693-7b35-3d3f-be6e-58dbeae531a0 | -13.9924 | -56.6437 | 2026-05-05 13:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a5ea07c9-2945-3906-98f7-f4a1f7d1deec | -12.0674 | -45.3229 | 2026-05-05 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 288.7 |
| 1a97733f-7e40-369d-8f99-eb50cc4b3c1d | -12.5031 | -58.4979 | 2026-05-05 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| f2bed798-1678-3334-82fa-2f757c85ef46 | -12.3321 | -50.0073 | 2026-05-05 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 14105ea2-fa10-3910-abbd-80811008f25f | -12.3051 | -57.5605 | 2026-05-05 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d2554b6b-e28e-3b86-851f-3abebd2608f4 | -12.3512 | -50.005 | 2026-05-05 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 296.6 |
| 0023334e-f20e-34f9-8b46-bea7a27d9bc2 | -12.0674 | -45.3229 | 2026-05-05 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 232.0 |
| ec535692-9b23-371b-ae67-f7f92e9c4188 | -12.067 | -45.346 | 2026-05-05 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 9ab3edd5-4448-3238-a6aa-edb5b394d029 | -12.3508 | -50.0266 | 2026-05-05 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b6eb8f09-be2d-34b9-9415-40f39873fb3d | -14.0267 | -47.6124 | 2026-05-05 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7110a8c9-fc27-37a1-baf8-932449e9cbc7 | -11.9748 | -49.6838 | 2026-05-05 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 571bbf1a-25c5-3fa2-aa56-f4f5564d7d3d | -12.2862 | -57.5621 | 2026-05-05 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 383cfabd-9d12-39cc-b77f-9578f10022d0 | -12.0097 | -45.3315 | 2026-05-05 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 0c13810e-2bc7-33d8-8384-61689098cc62 | -14.0272 | -47.5898 | 2026-05-05 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| dc121c23-57b7-3ccc-84cc-aeeeabc915a8 | -11.4449 | -55.0996 | 2026-05-05 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 99e92a3c-9ab7-3b7e-869d-bb17204e2603 | -12.5031 | -58.4979 | 2026-05-05 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 3f4173da-72ce-392e-83a7-6bfe683366ff | -12.3321 | -50.0073 | 2026-05-05 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| a7f4d72b-f251-3f33-a3af-c5e7b5144dd6 | -13.9924 | -56.6437 | 2026-05-05 14:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| d69e1d23-c10f-366d-8f45-caa2a64d6b99 | -12.5033 | -58.4781 | 2026-05-05 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 348.7 |
| 02cb1172-fa22-3ec5-9258-2dcb068d48aa | -12.067 | -45.346 | 2026-05-05 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 3d3dcd22-e8c8-3dbf-b1de-4251d2657e89 | -12.2862 | -57.5621 | 2026-05-05 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 3f75ec2e-1c52-338b-8872-a7ea49c275dc | -12.3512 | -50.005 | 2026-05-05 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 241.4 |
| 3901e70f-75fa-3205-b53e-e35a8613e698 | -12.0674 | -45.3229 | 2026-05-05 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 289.3 |
| 0aa57a19-02ff-35d9-b686-eac5eb967358 | -12.3508 | -50.0266 | 2026-05-05 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| d8896e0f-e76c-3613-9d78-25749111a171 | -13.9924 | -56.6437 | 2026-05-05 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9b7a8707-1805-3751-b43d-a0876d08752f | -14.0267 | -47.6124 | 2026-05-05 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 95682d80-4a12-3a99-bc6e-37b67308a697 | -12.3051 | -57.5605 | 2026-05-05 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| ca2fa58d-8324-3a90-a45c-f7c5e1f04f4d | -12.0097 | -45.3315 | 2026-05-05 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 340b9d41-b8a1-30f3-a0a9-cdff874eb8db | -11.4449 | -55.0996 | 2026-05-05 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| fdee7b7e-8567-3cc2-8caf-f9165f109519 | -14.0115 | -56.6418 | 2026-05-05 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c89e1296-8037-309d-92c2-f2e23bcbb69b | -14.0272 | -47.5898 | 2026-05-05 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0b4afd1e-4f57-34f1-b391-6028139258a2 | -12.3321 | -50.0073 | 2026-05-05 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 519ebe01-297d-39c1-9fcd-bef53e7e9f1b | -14.0118 | -56.6215 | 2026-05-05 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 752b4cb0-396f-33fb-966d-0062dbefd068 | -12.067 | -45.346 | 2026-05-05 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ef009434-dbab-3107-8e42-ed5d1efe4a1b | -14.0267 | -47.6124 | 2026-05-05 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 48745b41-c2c0-3751-9b45-d8db8aed4ae0 | -14.0272 | -47.5898 | 2026-05-05 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 87998ba7-f905-3900-b605-3aa3c81d85fc | -12.3051 | -57.5605 | 2026-05-05 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| b72d0690-6a43-3feb-af9c-4d002b5f503a | -12.5031 | -58.4979 | 2026-05-05 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 212.8 |
| e4cc217a-1cbc-3bd9-ba6e-c0f2232fed19 | -12.0674 | -45.3229 | 2026-05-05 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 235.7 |
| 3262d21e-0cf1-3f7c-8149-da3166da24f1 | -14.0115 | -56.6418 | 2026-05-05 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 5683efea-c1c3-34c9-839d-298f088ae0d6 | -13.9924 | -56.6437 | 2026-05-05 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| fda523fe-6647-3c42-afb7-0002e9266a3a | -12.3512 | -50.005 | 2026-05-05 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 20a4a231-f851-30fe-9a83-8412179144a7 | -14.1502 | -45.3543 | 2026-05-05 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e53f42de-58fd-30f2-bac9-5c2192837752 | -12.3321 | -50.0073 | 2026-05-05 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 1bc90ad5-fc70-3a21-b990-3ff1348bf835 | -12.2862 | -57.5621 | 2026-05-05 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 0a1d52f5-dcfc-3553-bae8-50b41a1fa3cc | -12.3508 | -50.0266 | 2026-05-05 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 09392a1a-2b5b-3379-8674-d0fc7b91b610 | -13.9926 | -56.6234 | 2026-05-05 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| eab9906d-04e7-3ed1-ab54-6df98a5e310c | -14.0118 | -56.6215 | 2026-05-05 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| eb782317-b4b8-3062-b31f-f52413c92aa7 | -11.4449 | -55.0996 | 2026-05-05 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 72ae4b54-44e6-3294-92f2-43ad182bdcb1 | -13.9924 | -56.6437 | 2026-05-05 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7a8c3460-7705-3f86-8f13-d8c2173afa2f | -12.3508 | -50.0266 | 2026-05-05 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 014ae007-f85d-30cd-b565-09a5dc408d00 | -12.3512 | -50.005 | 2026-05-05 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 248.9 |
| 1d95ab26-040e-38e8-a197-c0e133168430 | -12.3051 | -57.5605 | 2026-05-05 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 188.8 |
| fb3437b0-fbc7-302b-8b70-e723dd0409d8 | -12.067 | -45.346 | 2026-05-05 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 51139349-c170-3e3f-b6c5-b7e526e06b04 | -14.0267 | -47.6124 | 2026-05-05 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f3b7c5f2-ea49-37ac-9f10-44b35bda5b9b | -14.0115 | -56.6418 | 2026-05-05 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| fd415705-0b0e-3b03-bc86-0f7f409c2f1b | -14.0272 | -47.5898 | 2026-05-05 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 08894eda-4958-39f7-a133-7891b6bb19a0 | -11.9748 | -49.6838 | 2026-05-05 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 245.1 |
| 93b9b182-2e69-3e9d-9357-9f05b8a4be31 | -12.3321 | -50.0073 | 2026-05-05 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 187.2 |
| de0e425f-ce6c-3754-8e57-127cbd624450 | -12.0674 | -45.3229 | 2026-05-05 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.8 |
| c19d6905-441e-3cb8-b8f2-284bdbc76118 | -12.2862 | -57.5621 | 2026-05-05 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| b2f908a5-aa7b-3feb-a6bb-16c4c75c578c | -12.2862 | -57.5621 | 2026-05-05 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| c1280db9-3347-31d6-a375-7ecffe07e452 | -12.3321 | -50.0073 | 2026-05-05 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 206.1 |
| de97e48f-9253-304f-891d-8fdf30c867fc | -14.0115 | -56.6418 | 2026-05-05 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 06fa76a6-6f2f-311f-9d02-61435c2b454c | -12.3051 | -57.5605 | 2026-05-05 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 216.8 |
| 8fa6ca8c-0597-36e5-a7bd-cb1955631808 | -12.067 | -45.346 | 2026-05-05 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 47bcf183-45d1-3cb7-a2c4-ada28f0f4501 | -14.0272 | -47.5898 | 2026-05-05 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 78e2256e-e434-3890-8ac9-98fada1d1f55 | -13.9926 | -56.6234 | 2026-05-05 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 9c1e5332-f99f-3269-ac58-332b3d148a3a | -12.3512 | -50.005 | 2026-05-05 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 1ca659ac-4992-322b-8a3c-d173a468b027 | -12.0674 | -45.3229 | 2026-05-05 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 731473de-a5b3-3f42-93b4-bde27120b3eb | -11.9748 | -49.6838 | 2026-05-05 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 543f68d9-a7e2-3428-886f-6583bf3fefa4 | -14.0267 | -47.6124 | 2026-05-05 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 831dd86c-5bec-32f4-9f11-245ee3a4e69d | -13.9924 | -56.6437 | 2026-05-05 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 2028d62c-d825-3891-9d1e-4961727a62a6 | -12.3321 | -50.0073 | 2026-05-05 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 7b55e05a-133b-31ce-af0d-ad1542550ff6 | -12.2862 | -57.5621 | 2026-05-05 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 5532c8a3-6bd9-3045-8da3-d93c3cc193e7 | -12.3508 | -50.0266 | 2026-05-05 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| fb31b5ef-1554-3599-a813-1ae07c5e67ae | -12.067 | -45.346 | 2026-05-05 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 843886f8-d3a6-3ad1-b206-bd916cbd6f80 | -14.0115 | -56.6418 | 2026-05-05 14:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ab59f252-55b5-36cc-b348-ba8151d5f2e4 | -12.3051 | -57.5605 | 2026-05-05 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 200.3 |
| e895549f-993d-3eb0-9bc7-a7a4dee4e27b | -12.0674 | -45.3229 | 2026-05-05 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 25c9d706-79b5-3b7e-9d4f-8ac2cd417fb9 | -13.9924 | -56.6437 | 2026-05-05 14:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| fb5a3e05-f5c4-3017-a7a9-14ed880583c3 | -12.3512 | -50.005 | 2026-05-05 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 4b087e4c-7e55-38c9-bb71-8407cac0a926 | -13.9926 | -56.6234 | 2026-05-05 14:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 745db4ee-c657-3a20-a63a-6241f15163c7 | -11.8599 | -49.7194 | 2026-05-05 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b18a85e3-428e-3ec9-85ea-63d2a990c002 | -10.3973 | -49.8629 | 2026-05-05 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9d132f38-4c84-3d77-b4e4-ade2a7f88ae8 | -14.0272 | -47.5898 | 2026-05-05 15:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| d884d0d7-0a6f-3803-beff-0fbb26acf861 | -12.2862 | -57.5621 | 2026-05-05 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 223.2 |
| 3d4b0842-0117-3a0b-a04e-1ca6e150fb56 | -12.0674 | -45.3229 | 2026-05-05 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 18fdfe67-f24e-3b8e-9c31-7f1c85d81b33 | -13.9924 | -56.6437 | 2026-05-05 15:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8eb266c9-e6b8-3251-8f9e-39edd9b29da5 | -12.3512 | -50.005 | 2026-05-05 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 196.1 |
| fcecf85c-fdb5-39d3-9a5d-1b7e5c4795a0 | -12.3321 | -50.0073 | 2026-05-05 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 965a9a37-e4f7-36b0-b8cb-4a32f8e7d1ae | -11.879 | -49.7171 | 2026-05-05 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| a2aa083f-9309-3e16-9bc0-ec172784bf3c | -12.067 | -45.346 | 2026-05-05 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |


[Clique aqui para ver as próximas entradas](README9.md)

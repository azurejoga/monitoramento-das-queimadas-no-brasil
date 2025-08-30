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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7314e1e4-3ef1-3055-9ede-2e8e25b44207 | -8.8401 | -47.8079 | 2025-08-30 12:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 26bf0096-e689-300e-95aa-712830fc9546 | -13.3628 | -46.9953 | 2025-08-30 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e724a442-cde2-3edf-b5c4-69248f315f94 | -11.3317 | -43.6162 | 2025-08-30 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.8 |
| da13be07-894f-3428-aff5-534245ec8fd8 | -13.3456 | -46.885 | 2025-08-30 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 74c3b4d2-e1bc-3884-ac10-4b25dcbaea65 | -11.8764 | -46.378 | 2025-08-30 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 375.2 |
| 471e27c1-a9b9-35f2-9112-5eb9591f3096 | -13.3817 | -47.015 | 2025-08-30 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8578e7b2-e8cd-33ab-ae87-305fd9107ede | -12.8605 | -48.1657 | 2025-08-30 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1b7a5ead-c032-3e5a-b295-1cdda9637280 | -12.6686 | -48.1704 | 2025-08-30 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0d8327e7-f6d8-3a41-9757-086ec95aa9d3 | -6.1665 | -43.3273 | 2025-08-30 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 351.6 |
| 34a7b753-e1dc-3144-b707-5631588d35ed | -11.3312 | -43.6399 | 2025-08-30 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 9f71fa27-365b-3349-8be7-5359bbaf0f81 | -13.3812 | -47.0377 | 2025-08-30 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6e3fe0c5-f920-3c7b-a535-3ae7eb1933f2 | -13.3632 | -46.9727 | 2025-08-30 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 9ef43f01-9010-3895-a51b-f790b0658c32 | -11.3513 | -43.5897 | 2025-08-30 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 38f967c1-b8b5-3ce1-a2a3-3e34192926b4 | -6.1853 | -43.3257 | 2025-08-30 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 229.4 |
| fba9556d-df52-3266-981e-e1fd542d839c | -6.1787 | -43.9995 | 2025-08-30 12:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ca451c9a-4499-3139-943b-0a523e2e0d20 | -11.1523 | -54.3104 | 2025-08-30 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 1422319c-5221-3fe6-a498-46dadc7f0082 | -11.312 | -43.6428 | 2025-08-30 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 57ce57a6-0244-3336-bf4f-db5754850a58 | -11.876 | -46.4007 | 2025-08-30 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 2a3d6de1-6155-397c-a75d-abb9f5bf3fe4 | -14.0118 | -44.5614 | 2025-08-30 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2172e34c-7c75-316a-9f7d-88a8cc490828 | -12.8601 | -48.188 | 2025-08-30 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f339a909-357b-3a24-a374-265a9e0d91d4 | -13.3645 | -46.9047 | 2025-08-30 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 9fd9b730-5303-3ca6-b3de-118979bab00b | -6.7814 | -43.7865 | 2025-08-30 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d2a837b6-0eb4-3aa5-98d1-a807da3f062e | -6.1665 | -43.3273 | 2025-08-30 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 387.0 |
| ff7c9f34-79c9-339e-b233-ace96e17fbfb | -11.8764 | -46.378 | 2025-08-30 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 02f37466-106c-3621-a0aa-49856352743c | -13.3456 | -46.885 | 2025-08-30 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8c33ea17-e24b-30a1-adad-3e477748cda9 | -13.3628 | -46.9953 | 2025-08-30 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| acc23a27-4050-3d7d-bd20-e51aebbcc4b4 | -11.3709 | -43.5631 | 2025-08-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a5aa2ba2-10fa-3ef6-bfd8-ba0925e5cf00 | -6.1853 | -43.3257 | 2025-08-30 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 274.7 |
| 9c9b014a-515c-3ef2-9993-d91e9672e9d9 | -13.3632 | -46.9727 | 2025-08-30 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a9032408-7ef0-3263-9543-9961d4b90e5c | -6.1787 | -43.9995 | 2025-08-30 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| f9646954-a759-35e0-8a8e-54b734b2b989 | -12.6686 | -48.1704 | 2025-08-30 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| f91cf42e-653b-34ca-89c9-9316febd7851 | -11.1523 | -54.3104 | 2025-08-30 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| f49be669-396d-3480-b49c-1afc4ad94b4b | -7.0951 | -44.3128 | 2025-08-30 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 368d297f-5d00-3335-b024-1fc989b4d282 | -11.8952 | -46.398 | 2025-08-30 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 5da1d62b-dabd-3aa4-a166-57389e470fa6 | -14.0313 | -44.5578 | 2025-08-30 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| c6dc8cf4-8d33-37e1-9a89-defa4329a180 | -11.3125 | -43.6191 | 2025-08-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 21df85bd-f51d-38e9-ad44-329ee7aba5b2 | -6.185 | -43.3491 | 2025-08-30 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 291.8 |
| ac07ed36-89d2-33b9-a789-729cef56b62b | -11.3312 | -43.6399 | 2025-08-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 306.4 |
| 5bb5f289-59cd-3ce1-85c1-bc3d6f9d4383 | -12.8605 | -48.1657 | 2025-08-30 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 14960c25-074c-3b8a-a77f-787bb9999ac1 | -14.0113 | -44.5849 | 2025-08-30 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ea56230b-212a-3fa8-92d5-49b9882a81df | -11.3513 | -43.5897 | 2025-08-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 331027e9-2378-3597-9943-e0cdc47d3f6f | -11.3317 | -43.6162 | 2025-08-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 5f1c2711-9712-3449-984b-53cf290367e6 | -7.8541 | -46.9747 | 2025-08-30 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 466.8 |
| 0961b77e-47d6-3172-a4dd-9f24e465adc8 | -6.7814 | -43.7865 | 2025-08-30 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 28d3410b-e67d-381b-a46b-200d4be9aac5 | -11.312 | -43.6428 | 2025-08-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 480f8321-ddaa-3bc7-a384-aa52b60af47f | -14.0118 | -44.5614 | 2025-08-30 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 1a54fe06-5d9b-33fa-ad2e-b4a83fcd96ac | -11.3705 | -43.5868 | 2025-08-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 0f722936-3fea-3f94-ac36-22556a5e615e | -13.3817 | -47.015 | 2025-08-30 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 6eb4cf38-10bb-3f96-9a42-6ad34572e510 | -13.3645 | -46.9047 | 2025-08-30 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 127.4 |
| b868a745-7d86-313e-ad7a-fe63bdf1a542 | -13.3812 | -47.0377 | 2025-08-30 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| a1a6e31c-34b2-3991-a841-3e3ecedd073d | -14.0113 | -44.5849 | 2025-08-30 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 2c333ea4-9a55-309f-bdbc-3c630a07a507 | -6.1787 | -43.9995 | 2025-08-30 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 199ca9bd-4f12-320a-b451-e81045d20407 | -7.8541 | -46.9747 | 2025-08-30 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| aa6e416d-579e-3f0c-b3bf-5d1265523b19 | -11.1523 | -54.3104 | 2025-08-30 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 6d2b5063-e85b-3e06-afa7-26e4628ee7f1 | -11.3513 | -43.5897 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 0435a240-b2e8-39ff-af6e-8ee8f4c71343 | -13.3817 | -47.015 | 2025-08-30 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 19be6257-4afe-39e2-a7c2-ce63ceb2632a | -8.8401 | -47.8079 | 2025-08-30 12:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| dd4984fb-d4ea-343f-8b75-d5ac0a2073fd | -11.3317 | -43.6162 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.2 |
| cb76f418-715b-3be9-8090-aa1bef70a9e2 | -6.1853 | -43.3257 | 2025-08-30 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 291.1 |
| 7710c1a3-927d-38e4-ae6d-dd1b820a3d47 | -11.8764 | -46.378 | 2025-08-30 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 8e6e5f9a-3b62-312f-8d01-7ceca6d5bd41 | -14.0123 | -44.5378 | 2025-08-30 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ff3ad9c5-82d2-37ea-83f1-d9c00180612c | -13.3645 | -46.9047 | 2025-08-30 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 159.8 |
| acb6164c-40fb-395a-af78-33ddbe4b26c0 | -11.8952 | -46.398 | 2025-08-30 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 164.2 |
| a19981cd-8af3-3817-97ae-68fc2183bce7 | -14.0313 | -44.5578 | 2025-08-30 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 405617b3-0111-393b-b841-c66522986323 | -14.4671 | -52.0259 | 2025-08-30 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 4c8a66d7-f6f9-3d0b-b89d-be8d95a046a1 | -7.603 | -42.7232 | 2025-08-30 12:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| ab281f90-37c1-30f7-ab4c-c329abefea03 | -6.1665 | -43.3273 | 2025-08-30 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 334.9 |
| 69cf0758-c9b4-3649-9450-b32ee1fbfb46 | -7.0951 | -44.3128 | 2025-08-30 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d9b54279-22f7-3009-8da3-c94300b80dcd | -13.3456 | -46.885 | 2025-08-30 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| fbecc96d-4d6d-37c2-a4b3-e07a47438b1e | -13.3628 | -46.9953 | 2025-08-30 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 84be3dce-6485-3753-b004-af64e68489da | -6.7814 | -43.7865 | 2025-08-30 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 20b12b45-5bbf-316a-85e4-e24b00c1166e | -6.185 | -43.3491 | 2025-08-30 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 426.1 |
| 7d09d846-8e37-3378-9013-29304ff2c5ac | -11.3125 | -43.6191 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 38b70504-2eab-3052-b283-6d4a0b33c65e | -11.3116 | -43.6664 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 816c6d9e-dcd2-361e-a2c2-298f1a63e3aa | -11.312 | -43.6428 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| e80a32ff-d4ac-388a-aeab-166315d71278 | -12.6686 | -48.1704 | 2025-08-30 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| cda0a55e-b3b6-39b5-9ba7-e2a9ab36863e | -9.4498 | -62.3294 | 2025-08-30 12:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 95a88c29-dced-38a1-9583-e21f01742582 | -11.3312 | -43.6399 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 280.1 |
| 8de0b17c-205f-366e-9f5e-6353d99937b0 | -11.3705 | -43.5868 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| f5d49679-08da-33ce-aaec-9ed2c45d70f7 | -11.0087 | -46.9442 | 2025-08-30 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f8274366-88cf-380f-8b6a-bab2b7f39ced | -14.0118 | -44.5614 | 2025-08-30 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 313.0 |
| 6e98e399-b359-3974-ad9a-92664299a535 | -11.3709 | -43.5631 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 26e26d5a-7377-36a3-b261-28890f2c9896 | -11.3517 | -43.566 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| bf8efe28-70b7-3880-8768-b8f818ea01f5 | -13.3812 | -47.0377 | 2025-08-30 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ea085ddd-6fde-3bdf-9924-562f3b2221c2 | -14.4477 | -52.0285 | 2025-08-30 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| dceb406c-5a16-33db-99bf-71028814d528 | -11.3713 | -43.5394 | 2025-08-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 79bf1d8a-7a3d-3044-8d8f-dd1c082ce7fd | -6.7816 | -43.7632 | 2025-08-30 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 1c038984-3dbf-3a1c-80da-a142d995d804 | -14.4674 | -52.0046 | 2025-08-30 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1b411eb0-a42b-3445-a24d-41168180853a | -11.3513 | -43.5897 | 2025-08-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 72e30656-75d4-39a0-bb6b-378b77a11303 | -11.3517 | -43.566 | 2025-08-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| b9bf5b73-2019-3151-88c0-27045e2f1c6d | -11.312 | -43.6428 | 2025-08-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| acc75d85-a952-3388-8e78-dfc5ccc132ed | -6.1665 | -43.3273 | 2025-08-30 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 276.2 |
| 110f43b8-6483-3c1c-844d-443692762866 | -13.3632 | -46.9727 | 2025-08-30 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 309e659e-68f2-30a3-ad98-bdf13759a89a | -11.8764 | -46.378 | 2025-08-30 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 2d5fca33-1761-34bb-8d3c-e9218a358b0a | -9.4498 | -62.3294 | 2025-08-30 13:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 69f8e775-17d2-3958-a4c5-936056989a74 | -13.3628 | -46.9953 | 2025-08-30 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| dcb53920-d87e-32b5-8b6d-1ed0dfde097d | -20.5048 | -57.0861 | 2025-08-30 13:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 33ec5b0d-1152-3677-bedd-09761b18b48f | -14.0123 | -44.5378 | 2025-08-30 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 194.5 |
| ed5bde38-5044-33e3-b6a9-d4415107d4c9 | -6.7814 | -43.7865 | 2025-08-30 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9bd17a59-e4ad-343c-a8e0-a1b1ff7a9880 | -9.1337 | -65.8253 | 2025-08-30 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |


[Clique aqui para ver as próximas entradas](README99.md)

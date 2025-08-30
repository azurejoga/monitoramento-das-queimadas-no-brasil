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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee43bbe2-81c8-3b93-8399-ce7b8384ae87 | -11.856 | -46.4487 | 2025-08-30 10:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 6e4a9989-62af-3060-9238-c8167bbc8617 | -6.1665 | -43.3273 | 2025-08-30 10:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 72124ac4-1ac3-30b0-9f02-73d247902394 | -13.3456 | -46.885 | 2025-08-30 10:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 71c8a644-7695-393a-bfa4-d10a4d96e79e | -6.1853 | -43.3257 | 2025-08-30 10:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 5935ffab-3b43-3b1d-887f-ca21c5f8f5b2 | -13.3452 | -46.9077 | 2025-08-30 10:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 131.0 |
| ddee1e7c-bf61-3ad9-8ace-c934748f6598 | -11.8369 | -46.4514 | 2025-08-30 10:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 63bc34b7-c931-30a2-a54f-f2e05321cecf | -11.8752 | -46.446 | 2025-08-30 10:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 052fac44-f439-391b-9aa6-a25cab97c355 | -6.1853 | -43.3257 | 2025-08-30 10:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| c8bf5838-e4ff-361e-9cf3-b7df749fdd7d | -13.3456 | -46.885 | 2025-08-30 10:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 72620582-d4d8-380f-958c-1cbdf1ea782d | -11.0097 | -46.8769 | 2025-08-30 10:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| cb5182e4-c8a7-34eb-80d9-c17e7475aa91 | -11.856 | -46.4487 | 2025-08-30 10:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 91b59cb0-729f-38bd-90c2-e0a43aef786d | -13.3254 | -46.9333 | 2025-08-30 10:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| bb72b641-8926-3712-a3df-52872dacc175 | -11.8952 | -46.398 | 2025-08-30 10:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| b12c8c1e-ca83-33c8-8bce-8304b1d688ce | -13.3447 | -46.9304 | 2025-08-30 10:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 236.2 |
| 68cfa9b8-3098-346e-bddd-7b60ee73a41c | -13.3452 | -46.9077 | 2025-08-30 10:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 538.0 |
| 0c45cb68-5926-3470-a017-7edb78f251fb | -11.8556 | -46.4714 | 2025-08-30 10:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 2c061fe6-5c73-31dd-bcec-860327a83c2c | -13.3649 | -46.882 | 2025-08-30 10:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 0b30ccd3-46f8-349b-8662-dafe8effc836 | -13.3258 | -46.9107 | 2025-08-30 10:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 0738e1d9-0499-3148-9102-2c7f8d46566f | -11.8748 | -46.4687 | 2025-08-30 10:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 2f2e68b2-1e6c-3af4-87d4-36d1715859e7 | -11.8752 | -46.446 | 2025-08-30 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 502c83f1-2452-3ccf-b7f7-7991c043641d | -11.894 | -46.466 | 2025-08-30 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 391.0 |
| a0359525-9023-3298-a67a-82add63ff019 | -13.3456 | -46.885 | 2025-08-30 10:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 58122ef4-1432-3c78-9ca8-82277b1e39d7 | -13.3447 | -46.9304 | 2025-08-30 10:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 134.8 |
| a99a6ebe-59c3-3d11-b785-7cf7228914b3 | -11.8956 | -46.3753 | 2025-08-30 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 240be21a-23f6-32de-84ea-8cd24e5785a9 | -11.8748 | -46.4687 | 2025-08-30 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 390.4 |
| 33f7dda9-19f5-36ef-8e91-a23391a5cf56 | -13.3628 | -46.9953 | 2025-08-30 10:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 2196be3b-dd5e-3fd0-b3c8-50b53a99c095 | -13.3452 | -46.9077 | 2025-08-30 10:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 363.2 |
| 4fdb76fb-115b-378b-96b1-d945326d850e | -11.8944 | -46.4433 | 2025-08-30 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| c6d89476-d752-3032-9948-726f6e565dc5 | -13.3258 | -46.9107 | 2025-08-30 10:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 172.2 |
| cadb2c00-5c97-3358-8505-c301561d792b | -11.8556 | -46.4714 | 2025-08-30 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |
| b284279b-9e79-3fe1-826f-4b434b1a5b75 | -11.0097 | -46.8769 | 2025-08-30 10:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a9b9f0b0-2fb6-365d-acdf-e32caca038da | -11.8764 | -46.378 | 2025-08-30 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| eb272470-26a3-3056-94a2-71be542fe163 | -6.1853 | -43.3257 | 2025-08-30 10:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 056e9656-5d8b-3178-a6ce-32646854292b | -11.856 | -46.4487 | 2025-08-30 10:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c6ec1a9d-1f24-36de-ac21-fb437bef68ad | -11.8556 | -46.4714 | 2025-08-30 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| ee6dcc41-09f9-3a47-a03c-38266a7c79f6 | -11.0097 | -46.8769 | 2025-08-30 10:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 01059745-5307-3ac5-99fa-65e3d6d08051 | -13.3452 | -46.9077 | 2025-08-30 10:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 398.3 |
| 64d0da96-e072-3ec0-b96e-3ea8520010d2 | -11.8952 | -46.398 | 2025-08-30 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 40a0ffe4-5b1f-33f4-a47e-37b1b6620372 | -6.1665 | -43.3273 | 2025-08-30 10:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| c1481976-96bb-303d-8b95-dd801bcdaf19 | -13.3258 | -46.9107 | 2025-08-30 10:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 60a40506-8ea3-3afa-aa60-f5947e8dd14e | -11.8956 | -46.3753 | 2025-08-30 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 6b5e1cd8-ca5a-3c6f-b06b-ca9c905414e1 | -11.8768 | -46.3553 | 2025-08-30 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| b1864a20-71a3-3e12-ad68-73231dddc532 | -13.3456 | -46.885 | 2025-08-30 10:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 156.9 |
| a8bb52d1-4be6-3ac1-8a5d-3e7f3b530da0 | -11.8764 | -46.378 | 2025-08-30 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 37223437-1f2c-366d-8ddc-d5645bfa77bc | -6.1853 | -43.3257 | 2025-08-30 10:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 304eaf0f-0e8d-3ac1-a6a0-6d4c67dda7fc | -11.894 | -46.466 | 2025-08-30 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 91833d2e-d59d-3aea-9a64-b0384f0f82e5 | -11.8959 | -46.3526 | 2025-08-30 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 7c48f549-584a-3a8f-bbc7-1c94f78932dc | -11.8748 | -46.4687 | 2025-08-30 10:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 9fbe6f67-f36d-300f-a32f-b92a55df387c | -13.3447 | -46.9304 | 2025-08-30 10:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 541043e2-0d42-3003-a82a-39ba92bc1b31 | -6.185 | -43.3491 | 2025-08-30 10:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| e1381af6-ffb9-38b7-9307-35eff08bd9c6 | -13.3452 | -46.9077 | 2025-08-30 10:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 287.4 |
| 67c8f219-ce8b-3dfc-9197-466e58434317 | -11.8748 | -46.4687 | 2025-08-30 10:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 721605e0-90f3-3198-aa4b-550caeedfc2f | -11.8956 | -46.3753 | 2025-08-30 10:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 2018f683-3b2a-39b1-9e28-f8667ed78aea | -13.3258 | -46.9107 | 2025-08-30 10:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| a3e4c1ba-0e85-33ec-9e3a-6487ba88e7bd | -13.3649 | -46.882 | 2025-08-30 10:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 519da53b-dd38-37f4-9dc0-9ce07f3cbd69 | -13.3456 | -46.885 | 2025-08-30 10:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 233.2 |
| a1079b8e-1916-3a0b-9ee9-e4bdd1011c07 | -11.8556 | -46.4714 | 2025-08-30 10:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 73a838db-d23e-38a7-b052-3ff37937f7b3 | -13.3447 | -46.9304 | 2025-08-30 10:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e1607e75-ae3f-3f60-9ed8-3913f88d3c7b | -6.1853 | -43.3257 | 2025-08-30 10:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 255a018b-23a8-3460-9d71-20a59d2e5c28 | -11.0097 | -46.8769 | 2025-08-30 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 530f16d2-4c80-391d-818a-cfe5b51d333a | -11.8764 | -46.378 | 2025-08-30 10:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 438d51ff-675b-3e80-9213-6e739dcbdbe8 | -13.3649 | -46.882 | 2025-08-30 11:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 08b872b3-638e-3f3a-afa3-9496ee5dd18f | -13.3456 | -46.885 | 2025-08-30 11:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 19460b3a-5d02-3e80-985b-bbaf36d9e01b | -11.8752 | -46.446 | 2025-08-30 11:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 92a380ab-ccae-3933-9b8e-a37c94af3add | -11.0097 | -46.8769 | 2025-08-30 11:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 356e83fb-5389-3adb-bb7c-0a07849d7fdd | -6.1853 | -43.3257 | 2025-08-30 11:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 8b18ac26-1f32-3221-86ad-91037e0ddcac | -11.8764 | -46.378 | 2025-08-30 11:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 241d131c-73de-34fe-8386-39bb8a32a6e3 | -13.3817 | -47.015 | 2025-08-30 11:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 3f26ffe7-18fa-3268-846a-5975d66ff16c | -6.1665 | -43.3273 | 2025-08-30 11:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 13838164-65c2-338c-868d-92279a4fcaa4 | -6.1665 | -43.3273 | 2025-08-30 11:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| aa64e019-7bac-3e4e-aafd-1b1b0110ee7a | -11.8764 | -46.378 | 2025-08-30 11:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 263.7 |
| 5cc4eaa9-4a54-33ec-8359-964d2c0aad4d | -6.1853 | -43.3257 | 2025-08-30 11:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| a9f34b1d-b728-3f03-ac14-fb03e4a61743 | -11.8752 | -46.446 | 2025-08-30 11:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| d283d54d-c6d1-3aee-a6c9-7d3799bdc01e | -13.3456 | -46.885 | 2025-08-30 11:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 5bfde38e-b61f-310f-bb90-00c540052c92 | -13.3632 | -46.9727 | 2025-08-30 11:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 11eb7d21-df66-3f75-9913-b27ad002f8ab | -13.3649 | -46.882 | 2025-08-30 11:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 20988465-a562-319f-91ea-034fc6bd03dc | -11.8952 | -46.398 | 2025-08-30 11:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 931612d4-bbb4-3fdc-b7b9-2bcd4384c9e4 | -13.3628 | -46.9953 | 2025-08-30 11:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 2e544d55-0ec8-3594-b4b5-baaaea3293a1 | -11.8764 | -46.378 | 2025-08-30 11:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 263.1 |
| db53b536-6645-37cd-bcb7-ba2eae7a2676 | -13.3632 | -46.9727 | 2025-08-30 11:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 00ba491c-ac77-31b9-8f80-b2038c063d83 | -6.1853 | -43.3257 | 2025-08-30 11:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| e8ff71ad-3cca-32d5-b44d-28d30f5ba9df | -6.1665 | -43.3273 | 2025-08-30 11:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| a8bce0ee-2246-3a69-84a1-82428d6aa362 | -11.0097 | -46.8769 | 2025-08-30 11:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 3017aaf3-1f05-3e3e-9359-7a1f93089040 | -13.3628 | -46.9953 | 2025-08-30 11:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1b1cd7c9-baf2-339f-b2ab-68414bbcaa64 | -11.8952 | -46.398 | 2025-08-30 11:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 59050589-66fe-3a6b-b325-d48d71dd6ca4 | -11.8752 | -46.446 | 2025-08-30 11:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 7e1e128b-1d26-35b4-85fe-1cbe786a071d | -11.8365 | -46.4741 | 2025-08-30 11:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| dedf127e-7a85-3989-b210-45ac2acc4335 | -13.3456 | -46.885 | 2025-08-30 11:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| a176bed7-dee1-3ac4-93b0-9bb15ec4b6a2 | -6.1665 | -43.3273 | 2025-08-30 11:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9fb41fb4-7f42-3d5e-9433-c8aa98b57475 | -6.185 | -43.3491 | 2025-08-30 11:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 1f8e66c8-593d-3edd-9fd3-7f656d142afe | -11.8365 | -46.4741 | 2025-08-30 11:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 571b03a1-9fea-3da5-a72e-b4fba06c6441 | -13.3632 | -46.9727 | 2025-08-30 11:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 834359d7-bdb4-302a-8f1d-539b0733d2a0 | -13.3456 | -46.885 | 2025-08-30 11:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 6c8714e7-1db8-3ee5-8840-0c23829daf8e | -10.659 | -48.7311 | 2025-08-30 11:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 97ae1d4d-5036-3bd7-b87e-abe5e520693e | -11.856 | -46.4487 | 2025-08-30 11:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9cdb9d5c-39e0-34fa-ab10-e1b4ebcdae50 | -11.876 | -46.4007 | 2025-08-30 11:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 5d009023-a1de-3d80-89aa-d21c877e4b0a | -11.8764 | -46.378 | 2025-08-30 11:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 411.7 |
| 30eb4e82-21fa-3d7b-ac07-a2c2022c930d | -9.6986 | -47.0555 | 2025-08-30 11:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 6a8e9288-8ca9-319c-ab21-c5c50bea6e19 | -9.6983 | -47.0777 | 2025-08-30 11:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a48673d4-4f11-3e60-b2a6-51b7201f800b | -11.0097 | -46.8769 | 2025-08-30 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 167.7 |


[Clique aqui para ver as próximas entradas](README93.md)

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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ed468b2-9115-31be-9ba5-063d74853c4a | -11.9777 | -58.06058 | 2025-10-27 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f377c3bc-cb9b-3045-ac66-7646af033c8a | -19.64416 | -45.38903 | 2025-10-27 05:04:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00782d26-b12d-3767-a103-d2288d68a004 | -14.36889 | -51.53091 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36f42c6b-1153-3920-b8f8-566d2ec6da12 | -15.29005 | -42.93998 | 2025-10-27 05:04:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b330fb-1ad3-3442-a65b-752a93b34607 | -13.24247 | -47.995 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d46f11f5-fef0-38e2-9e30-35097954c7b9 | -17.03831 | -47.05629 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f989752-f729-3d1a-9d5c-e5579c5c05d2 | -17.32141 | -43.65057 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 10ebc64b-4885-3238-b773-a6af0125c22c | -12.41166 | -54.19826 | 2025-10-27 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cbc5287-99f4-3148-aadb-955cd772a8df | -14.57001 | -47.99965 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d386338c-37d7-395f-ac53-525da1720582 | -13.3108 | -54.36343 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d036053f-872c-39ef-bc36-6a9a42fa4c43 | -17.23411 | -46.79403 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fb6c657-09c9-3ef6-a2dd-7fe4103347e2 | -14.88022 | -52.45311 | 2025-10-27 05:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec799aeb-1f16-37c4-82f7-3ee6d3e06a5b | -17.32237 | -43.65985 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 65667cfc-fda1-3764-9c79-0ad63bb49dbc | -14.82916 | -52.42864 | 2025-10-27 05:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f08ae50-5954-3e52-b0bc-52da0991c563 | -15.24705 | -46.05848 | 2025-10-27 05:04:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e268b497-5fa6-336d-9cb7-8c206565ced6 | -14.24837 | -48.13942 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a43f8f1-3c3a-35b0-8211-c90f41bd3ba7 | -12.65328 | -52.62888 | 2025-10-27 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e5c615b-3dda-330e-af2a-333f3236a2da | -15.19064 | -47.22047 | 2025-10-27 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9316ae1b-f023-3b56-8d3e-5831f42c5c2d | -15.24753 | -46.05429 | 2025-10-27 05:04:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5db2e2f3-6742-3354-bef8-85060a58ba92 | -14.37652 | -51.53378 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 636d431c-15ff-3449-bdd7-5dacf2be2d38 | -14.82543 | -52.42804 | 2025-10-27 05:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca0578bb-f869-39fd-9b49-035602bc0036 | -15.28964 | -42.93884 | 2025-10-27 05:04:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e68f1952-8728-35a0-874e-1ca20ce0f171 | -15.32936 | -43.8066 | 2025-10-27 05:04:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8080ede-140e-398c-9880-b315cc3bca41 | -14.56515 | -47.99827 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84b1a916-d867-36a1-a4ed-a9577cd8b733 | -12.65689 | -52.62942 | 2025-10-27 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ba20f26-2069-30fd-bfa6-6b03b23ad346 | -13.26521 | -47.97147 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e41ecef7-86a3-3bce-9407-040cb234275c | -14.3728 | -51.53149 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 627ace12-c4d7-355f-9e26-c510cac31be7 | -13.53989 | -47.16344 | 2025-10-27 05:04:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae156f36-13e5-3847-95c3-ef84edebbe3b | -17.31626 | -43.65212 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a6cff1e8-5962-3bc2-9003-ddd91a48ae9c | -14.2539 | -48.13494 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83b03575-bd42-3da4-9f59-9b4fc821cd71 | -14.93812 | -47.337 | 2025-10-27 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc44de3f-ba3f-3a10-95e6-cdebfb105fd8 | -16.37772 | -47.41374 | 2025-10-27 05:04:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 534614d5-0a71-3f2b-b6cd-d15b588de5f7 | -12.89797 | -54.73259 | 2025-10-27 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c0b4cff-897a-3b58-83d0-7a9ab9dd39de | -14.64009 | -48.4146 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2b51f125-de45-3ca3-a157-14651bd36351 | -13.24016 | -47.994 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 416ae815-8083-32a8-a82b-7ee696f86490 | -19.6406 | -45.38799 | 2025-10-27 05:04:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 803b2f61-6a20-39be-a7f5-f05a532d9ea8 | -17.40793 | -46.88306 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5227f82d-b943-3b90-8ccf-62baac87cf1f | -14.36938 | -51.52759 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad723480-065e-33f7-b820-70bd5d946433 | -15.15044 | -47.9406 | 2025-10-27 05:04:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8db18aca-bbf5-314e-be86-b743ff076c25 | -15.29695 | -42.94058 | 2025-10-27 05:04:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7508e89c-d2dd-39c0-87be-4de9ef71bcb4 | -17.32813 | -43.65154 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9110a0c8-4843-3303-9686-ca9bdd395411 | -19.64015 | -45.39273 | 2025-10-27 05:04:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd7262cf-f500-3379-8bd0-ccb119489e5a | -14.63458 | -48.41942 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce2a41b1-4431-32a2-b462-91000b0a8822 | -19.63793 | -45.38832 | 2025-10-27 05:04:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e540b99-6110-3fa6-9e65-da6ff3bd2d70 | -17.32747 | -43.65822 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fce4168a-8d64-3b21-bc43-d6ff8b6351eb | -13.26095 | -54.36734 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ce4759a2-1126-3d41-82e0-497f5e3fc5d6 | -13.23339 | -47.98851 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f3995fd4-9660-3878-b065-9206756c3434 | -14.37671 | -51.53206 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35c7a3ad-55f7-3f3f-a150-31f50ed39832 | -17.32966 | -43.65454 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 171db1eb-b7ef-3566-8533-e51be3940b88 | -17.0387 | -47.0528 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69f22580-8030-3c84-904e-a9a5003d06fb | -12.86059 | -48.63815 | 2025-10-27 05:04:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27d698da-1ed1-3de6-a261-ff1f7ce6b4da | -17.23966 | -46.79472 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e48edf0-e719-38c6-96fa-9261b4fd5b65 | -13.60091 | -47.59602 | 2025-10-27 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 739098f8-90e7-3a30-83a8-e6569ba914da | -14.88252 | -52.45527 | 2025-10-27 05:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cf6149d-6cc7-3917-badb-a28378731128 | -13.31703 | -54.36817 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e995241d-93f6-3749-943b-0eaf59dd7047 | -13.19691 | -48.43633 | 2025-10-27 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f4bb4e4-fffb-3cf2-8e24-98b0c069b7fb | -17.40938 | -46.88082 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa7175dc-9ee2-3c79-b3ae-a45484062a7c | -13.23529 | -47.99339 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 883d014f-d64b-3f88-ab99-a6219824accb | -14.54028 | -47.99598 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97838363-a731-37ef-b0bb-2e54365cd556 | -14.62976 | -48.41882 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26430ea4-854b-3dd8-9c38-7201b8071395 | -15.14956 | -47.94069 | 2025-10-27 05:04:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 790f3423-22e9-33c7-a522-043224727d6f | -13.42436 | -47.38207 | 2025-10-27 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b599d79-dd45-3a8d-ab95-0d9fe2ddb9d2 | -17.40894 | -46.88476 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c0dfb39-8680-3ce0-b13c-68b0fb6cb144 | -13.30672 | -54.36326 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c24494d4-96fc-3678-b45b-399e41535c7f | -17.32079 | -43.65697 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e3daff55-3b08-32f1-8864-f24cc894ef6b | -14.3986 | -51.54731 | 2025-10-27 05:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d8d5e65-935a-30ea-aa87-f419403b36c9 | -12.85598 | -48.63736 | 2025-10-27 05:04:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eaf712fc-85fd-3799-a2a2-d3100e9552fc | -13.30728 | -54.35957 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a716acc1-336c-32a7-ac2e-f754cd15e7c3 | -15.15027 | -47.93458 | 2025-10-27 05:04:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 462eb416-c19e-3e47-b2a7-45e6274ba72b | -13.42878 | -47.38818 | 2025-10-27 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c62e94f9-01b2-395c-96a3-c0855a195aac | -13.28751 | -54.39795 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cba011b4-7883-34f9-a135-81305469581d | -17.31569 | -43.65843 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c4b9180-e237-30eb-be67-334d987957df | -13.26032 | -47.97093 | 2025-10-27 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 48a0a14e-c354-38e0-a899-2577d8ff4494 | -12.45117 | -54.30214 | 2025-10-27 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65f6502e-bd85-3f80-a986-ca5a61383e98 | -15.18534 | -47.22014 | 2025-10-27 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 448cd889-28ab-309f-81fd-5b9967ad827b | -14.62151 | -48.40643 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78c95cea-1c79-3e48-9197-b883124d30f2 | -19.64106 | -45.38312 | 2025-10-27 05:04:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 709ffa52-54d7-31d6-8560-d754f3f88cea | -13.30954 | -54.36748 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f8b80c4e-6475-3485-b262-8e98d7374388 | -16.37638 | -47.42006 | 2025-10-27 05:04:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac297c1f-f57a-37d5-b658-734edad6463a | -14.82849 | -52.43338 | 2025-10-27 05:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fdb849f-32a5-3629-b891-cead559688fb | -12.66049 | -52.62996 | 2025-10-27 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b89e3f9-b155-31b5-8d1d-bfaaa8e68709 | -14.62216 | -48.40127 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eecbaa51-4212-33d7-ac62-86ad7fb927b0 | -14.94331 | -47.33783 | 2025-10-27 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c50235f-c103-3ba2-99b9-c38b1555225d | -13.54538 | -47.16149 | 2025-10-27 05:04:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 417a9f13-77b2-3b63-9e2d-b2504c2aae25 | -14.26007 | -48.12539 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de527b91-936e-3a47-b912-65ee7308d972 | -13.28695 | -54.40163 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0f06ece9-5f84-336b-8aa2-586a8ee21c4d | -13.31647 | -54.37186 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92a7e499-2ae5-39b2-ad94-3e8fd6eaae6d | -15.29654 | -42.93948 | 2025-10-27 05:04:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b09869ab-5613-3211-84dc-8d03daebf7b3 | -17.23368 | -46.79798 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7a766c4-7bd6-35e4-9cb8-e7f8e534d185 | -17.31411 | -43.65555 | 2025-10-27 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee6b8b60-30e9-36f4-92d7-928541220709 | -14.5409 | -47.99085 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5178369-ad63-3b15-a359-e2219c822171 | -16.37675 | -47.41667 | 2025-10-27 05:04:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12a5b0da-f7b1-3500-85a0-f788203d04b4 | -13.31308 | -54.37133 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f23fbd9-43e0-351e-a96c-77c91b2bc7d5 | -15.19508 | -47.22812 | 2025-10-27 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f77bd4c1-2b4f-3d74-8fcb-64004b78479f | -13.25756 | -54.36679 | 2025-10-27 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 97de06f9-6d80-3d57-8cec-99bb02cbe846 | -15.18003 | -47.21991 | 2025-10-27 05:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e1244b9-9c0f-38b1-ab70-8f07d8fa18a9 | -17.40752 | -46.88697 | 2025-10-27 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 224be5b6-c8c5-3899-87fe-462a7681687d | -15.32281 | -43.80586 | 2025-10-27 05:04:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e45f9d5-71fc-39bc-ac45-aca76a7ba4b8 | -14.64076 | -48.40928 | 2025-10-27 05:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4d355b0-67e3-3a10-9bd9-45515374b846 | -14.84477 | -52.42613 | 2025-10-27 05:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README66.md)

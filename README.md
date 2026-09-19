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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed18f5e4-5e05-3746-aa7b-8112e2025d65 | -4.6148 | -42.9488 | 2026-09-19 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 14c1672b-3459-3983-ac32-0c4bdeb4d3e3 | -6.0009 | -51.8111 | 2026-09-19 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f52145ae-350f-33e6-9ef7-727a0981bec5 | -12.5952 | -49.1046 | 2026-09-19 00:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 6833c9d3-19de-3b2e-b2a3-7072b0422efa | -2.8284 | -50.4863 | 2026-09-19 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 6f4b911c-52f0-35eb-bad8-12c9b184ca8a | -3.3494 | -59.8097 | 2026-09-19 00:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f9f28958-a7ed-32fc-be6b-98df8e1ffd71 | -4.596 | -42.9734 | 2026-09-19 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 3fd503fc-071e-33a5-bf89-6645249bbb1c | -4.5045 | -54.9646 | 2026-09-19 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| dac8c383-2ac5-36f6-b8ff-ec7e5b741d60 | -12.5956 | -49.0827 | 2026-09-19 00:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| aed946a8-2dd7-36df-96ec-24dc9b6cfbd4 | -4.5774 | -42.9512 | 2026-09-19 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 78a17a6d-7624-332c-a8cb-46c8f5f279ca | -22.3337 | -50.6188 | 2026-09-19 00:00:00 | GOES-19 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 94ce75e3-1293-3bcc-bcb3-a7a62d1b8156 | -5.5062 | -43.7966 | 2026-09-19 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 81f5781b-a3a1-3c85-bf73-7446bcf6a350 | -4.5961 | -42.95 | 2026-09-19 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| b7fd1c2d-2fa0-3041-aa2a-2af072f548e5 | -8.4983 | -57.6271 | 2026-09-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| abbbd9e2-f137-3593-b844-931e92710392 | -12.5761 | -49.1071 | 2026-09-19 00:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| cb946f77-9569-3e39-876f-94069f385212 | -4.3587 | -47.7853 | 2026-09-19 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 100bcbdc-93e0-3e01-9479-915ea5f78951 | -10.7994 | -50.8881 | 2026-09-19 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 66ce1da7-549e-3245-9a44-6a36bed6528f | -10.7303 | -60.7301 | 2026-09-19 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| dede22cf-1eae-3b6c-9077-96c8aa675191 | -3.3638 | -50.4492 | 2026-09-19 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 389c810e-8d30-3685-8319-1bca1de666cf | -8.4296 | -54.7262 | 2026-09-19 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| b1bf3198-c70b-3c1c-b4b5-830e6bb5c295 | -2.8101 | -50.4658 | 2026-09-19 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 57a6d691-79f5-369d-b8dc-3199216e3c26 | -6.001 | -51.7903 | 2026-09-19 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 455ed969-c859-3dba-8f67-04e7e89d9002 | -10.6928 | -60.7322 | 2026-09-19 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| b169b663-a59d-347b-af99-729294ea018a | -10.7115 | -60.7312 | 2026-09-19 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 33790c78-ea7e-39ff-9455-56ae156a3cbf | -2.8286 | -50.4444 | 2026-09-19 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| da63834d-f345-3fa0-a2f0-f7a40cd18881 | -14.6861 | -46.6657 | 2026-09-19 00:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| b0f7219b-41e3-3db4-aa22-448240849b23 | -3.3311 | -59.8101 | 2026-09-19 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 42b3b367-9a8a-3ccd-9bf5-9fc9c2e10370 | -5.5249 | -43.7953 | 2026-09-19 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 200.2 |
| eba15540-880f-3475-8c69-e577496bbff6 | -6.5898 | -44.15 | 2026-09-19 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a9e911d1-3b8a-3d88-b4ea-6661c583908b | -4.0576 | -56.2471 | 2026-09-19 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 5c430fd4-e79b-3a69-9a4a-8af0bf61f4ec | -8.411 | -54.7274 | 2026-09-19 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 88a2dc5f-7e06-35a7-b21c-a7aa6ce19755 | -2.8285 | -50.4653 | 2026-09-19 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 236.5 |
| 57df46e2-885b-350d-86f1-b8113262e240 | -14.6665 | -46.669 | 2026-09-19 00:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 1f35bf8f-9288-30a3-a1ae-f6a7e3450032 | -4.076 | -56.2466 | 2026-09-19 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 48e9af31-d796-3373-8610-b172403c57d8 | -5.7622 | -57.444 | 2026-09-19 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 64270ed0-de43-31e0-a6fc-ff371b8147b1 | -10.867 | -56.1975 | 2026-09-19 00:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 91fc8383-1a50-3b5b-861e-fb2c28009ab1 | -5.5064 | -43.7735 | 2026-09-19 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d0c78c4f-89ca-3045-8921-56e7eb9e6a05 | -10.7114 | -60.7505 | 2026-09-19 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 1f24c9ff-a966-3642-bfe5-e5b93bf24e51 | -5.5251 | -43.7721 | 2026-09-19 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 0481f4e3-2858-3964-9a26-1b0aa25d86cd | -4.076 | -56.2466 | 2026-09-19 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4ca3fda8-5f48-332f-9165-7580f378ae81 | -2.8285 | -50.4653 | 2026-09-19 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 244.3 |
| 4eee6b08-dcf3-3105-a559-5bbc1cbc526b | -3.3494 | -59.8097 | 2026-09-19 00:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c6a077a0-95c4-3cbe-b2bd-fef3711ba927 | -22.3337 | -50.6188 | 2026-09-19 00:10:00 | GOES-19 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 01663a1f-f5d7-327d-9dc3-e9e57039f604 | -8.4983 | -57.6271 | 2026-09-19 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 3083460d-96ab-3527-963e-aac9cede484a | -10.7115 | -60.7312 | 2026-09-19 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 11202d05-1c29-3a1f-8cd2-dec2bfd9b315 | -2.8101 | -50.4658 | 2026-09-19 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 534fb4f0-d321-34e9-88d3-ce1b9084c01b | -7.6386 | -46.103 | 2026-09-19 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 55a08ace-b43d-389f-9154-6138909c643b | -7.6384 | -46.1254 | 2026-09-19 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 32683882-1c2f-3d15-98ba-28fea170ed41 | -5.5249 | -43.7953 | 2026-09-19 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 169.9 |
| dd37b172-355e-3b1b-bb62-1d2bafe3ee7a | -6.001 | -51.7903 | 2026-09-19 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 84fd6d0e-f508-37ba-b7e8-922ec5111736 | -2.8284 | -50.4863 | 2026-09-19 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 194d8765-824a-319b-915a-8d3768b93806 | -3.3311 | -59.8101 | 2026-09-19 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 07b0ee8f-3921-3626-9c7c-42fe991cd2e6 | -4.3587 | -47.7853 | 2026-09-19 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e7492292-41b4-3923-8d5b-2d0004f3c20e | -4.0576 | -56.2471 | 2026-09-19 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 4f9046e8-f66e-3f2c-9274-5efc67d8b225 | -7.6574 | -46.1013 | 2026-09-19 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ac62a6d1-60c5-3204-83da-0b1fec6aef74 | -12.5952 | -49.1046 | 2026-09-19 00:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| c8953312-b7e7-38a2-b6bf-a27e79fde789 | -5.5064 | -43.7735 | 2026-09-19 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4a0040ee-6fd4-34af-8c8c-86163a4da51e | -5.5062 | -43.7966 | 2026-09-19 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| fc6fda4b-f657-3178-9b61-31cf22b25bf7 | -2.8286 | -50.4444 | 2026-09-19 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| aba4f12e-a222-36a2-a2b4-ccce571265be | -12.9971 | -46.9833 | 2026-09-19 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ab0a26a7-46be-38e8-9053-52e5db4b2fcd | -12.5761 | -49.1071 | 2026-09-19 00:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 9218f8c1-182a-3d99-ba18-ea132ae29376 | -5.5251 | -43.7721 | 2026-09-19 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 834a2315-be5a-3b88-a518-5f0bd8879d66 | -10.867 | -56.1975 | 2026-09-19 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 23e1827b-9db7-334d-9442-ea3810772fdb | -3.2313 | -46.9596 | 2026-09-19 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 1d7e2ef8-7bdb-3228-8bb0-0c0f866de37c | -3.3638 | -50.4492 | 2026-09-19 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 10385d44-f091-3a06-9ac8-5cb690c496f4 | -14.6861 | -46.6657 | 2026-09-19 00:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e385007b-4ca8-3e47-801f-e9627cd708f7 | -8.4296 | -54.7262 | 2026-09-19 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c25ed952-be4b-3de1-b965-64b5ffddb5f8 | -10.6928 | -60.7322 | 2026-09-19 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| c9bb8bad-1ba5-32ea-8425-7995583afdb3 | -5.51 | -43.78 | 2026-09-19 00:15:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82e631d0-86ed-32e2-87c3-bad45424b031 | -13.6137 | -48.3153 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 84aadad5-7322-3aed-a649-a1457edd69d1 | -8.3735 | -47.193001 | 2026-09-19 00:19:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f57e038d-5980-33bc-a03b-85d52bc0bce7 | -16.091101 | -49.6409 | 2026-09-19 00:19:00 | METOP-B | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1506a2e0-7e34-3450-9a2a-3c47295c0b69 | -3.1471 | -53.9328 | 2026-09-19 00:19:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fed3ba8-e000-3c66-9076-74f648f7c1d9 | -4.2695 | -46.5247 | 2026-09-19 00:19:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf93bc1-5723-3dd5-86dc-d871161b276a | -11.3267 | -47.676201 | 2026-09-19 00:19:00 | METOP-B | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 588c0a8c-7d34-32d1-a3b6-ef64cf519560 | -7.5469 | -61.3013 | 2026-09-19 00:19:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e0eb613-10c2-3492-90cf-04f0771faf30 | -10.5216 | -44.848598 | 2026-09-19 00:19:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2bbf00e0-64cf-3156-836c-7d1060e8a337 | -6.307 | -47.5686 | 2026-09-19 00:19:00 | METOP-B | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3219886c-b7a9-3235-b90e-defe402d54ed | -11.946 | -50.1353 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd5a44b5-2524-3fa5-8c89-9d36160cb16c | -8.7604 | -46.911201 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 679fd34a-ae02-3b1c-aa0e-6461eb24de8e | -11.3449 | -44.129002 | 2026-09-19 00:19:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95fbfcbb-fbaa-3649-81c6-c6a2f2331a6d | -11.1413 | -54.008202 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddd149d4-00ee-3dcf-9160-e5ca8a46d2d9 | -9.2454 | -45.9216 | 2026-09-19 00:19:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ff0d7ac-fded-34e1-a6c8-65fa651ce449 | -10.8205 | -50.1731 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0955c8ed-14b3-3222-9410-7943ddc906d9 | -7.8435 | -44.861401 | 2026-09-19 00:19:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a40c3f8-6c9e-3e66-87b7-761e8bc998cb | -10.4646 | -51.245499 | 2026-09-19 00:19:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc99cfe3-3cc3-3d9e-b2e8-cdd5e78b5037 | -6.6598 | -50.918098 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f31c74f1-4503-35c6-aef7-417740aa3d2f | -7.6365 | -46.0928 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d506dff-b0ba-3624-a33d-c04e57a8327d | -11.0012 | -48.313499 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9c33c5f-aff2-3fee-8e10-9b01f58dc151 | -11.8397 | -47.442799 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55fa410f-0536-36df-b6f6-50f463138c86 | -13.6295 | -46.9291 | 2026-09-19 00:19:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca504bd9-fb1a-3f72-8652-28e9b9b9b160 | -7.2202 | -49.628899 | 2026-09-19 00:19:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85439ca9-ae3c-3523-89fb-b436ee7bbf8f | -5.762 | -57.435699 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a9a924a-fb6c-3b99-bb0e-387d9da69157 | -5.8473 | -52.062401 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b093616-819c-3437-92ed-b1fc8fd72e54 | -7.5522 | -49.5924 | 2026-09-19 00:19:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5f2d61-f27a-3daa-a969-2dde6c39b66e | -5.8592 | -52.023701 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd4e58dd-e6cd-309d-b93c-5743f8e4e0fa | -13.6004 | -48.302399 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 66a520f4-bcb5-37bc-85dd-3cd2b42164b7 | -5.19 | -49.321899 | 2026-09-19 00:19:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b5387ed-aea9-3914-8ebf-ccb2aa2c24be | -10.3691 | -50.4552 | 2026-09-19 00:19:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a12ffdbb-9d19-3094-8b8d-05ea0077ed2e | -12.9105 | -53.894501 | 2026-09-19 00:19:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a84dc02-d153-3de2-bb54-48f1a640b4ac | -10.8026 | -50.869499 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)

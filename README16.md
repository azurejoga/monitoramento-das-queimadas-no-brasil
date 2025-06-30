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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46375033-63f5-3116-96cf-bb61e67ce723 | -12.6253 | -54.21395 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 532ecce1-8d5b-30d8-b5ad-b61e648d8306 | -14.0286 | -54.4863 | 2025-06-30 05:33:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b69183a-f1b9-3b9a-8a28-15a72aaef020 | -14.0282 | -54.48969 | 2025-06-30 05:33:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1299a8c1-3381-3cda-9798-3b8da93f588a | -14.03362 | -54.49026 | 2025-06-30 05:33:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17ff72f2-8940-34b9-ba3c-0aa6689c5b58 | -13.47423 | -56.85791 | 2025-06-30 05:33:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09dac93f-958c-3b95-83be-2f454aef3a89 | -14.03402 | -54.48682 | 2025-06-30 05:33:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f30b8e3f-c99f-3104-936f-bbdb6be7e963 | -14.50744 | -58.64727 | 2025-06-30 05:33:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85046057-1344-3f05-83b6-876e4f0ab2a8 | -14.02781 | -54.49306 | 2025-06-30 05:33:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f46c321-229c-38dc-bc3c-c2502e3261df | -10.7859 | -44.2346 | 2025-06-30 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fe4fc8b4-1e5b-39f7-b783-1ebfc058fe70 | -10.805 | -44.2319 | 2025-06-30 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| a747665a-c8a4-3f89-b426-cf9f3c3113c3 | -10.8046 | -44.2553 | 2025-06-30 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 44550e06-3aba-3114-a528-ec6f262a1f1c | -4.31708 | -48.0792 | 2025-06-30 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d9155a48-1aca-3cf8-81e5-4a57f2817c0e | -4.31858 | -48.0694 | 2025-06-30 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 351649ea-153f-3de1-b2a6-493f96542238 | -10.55424 | -52.03674 | 2025-06-30 05:46:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b255fe56-f8ce-3342-a3d6-4001ff92cd20 | -7.26478 | -45.38313 | 2025-06-30 05:46:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 10e18d2a-5706-3012-b02c-aff69793008f | -10.43139 | -47.43419 | 2025-06-30 05:46:00 | AQUA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bffefaa0-4e84-3482-9ac9-0f18289939e5 | -10.43005 | -47.44309 | 2025-06-30 05:46:00 | AQUA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c3e28395-d126-3e06-9fd2-558a6eb38e64 | -10.43886 | -47.44442 | 2025-06-30 05:46:00 | AQUA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f408c602-1ccb-3f5b-87c7-138de6331072 | -10.64848 | -44.49233 | 2025-06-30 05:46:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e4cc5cc6-4e4d-37b2-bf62-66dff4fa3f30 | -9.09536 | -47.95789 | 2025-06-30 05:46:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6efb974a-69e6-3d5e-a8e5-007fec878507 | -10.85493 | -53.73109 | 2025-06-30 05:46:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| a56d1a0d-1e7c-34b8-9c0f-49b04cecc689 | -12.05989 | -48.46151 | 2025-06-30 05:46:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 87f810cf-a210-30b3-947a-2756c08507a5 | -10.8516 | -53.75037 | 2025-06-30 05:46:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b1104c99-dcf6-38bf-8dba-735699c65077 | -10.65002 | -44.48139 | 2025-06-30 05:46:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 53564c61-b335-3efd-be61-36dbf4e8d5f4 | -12.06878 | -48.46288 | 2025-06-30 05:46:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 62f8b92f-8061-3c53-b2aa-f5942ee1bf7f | -10.8059 | -44.23731 | 2025-06-30 05:46:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d2a1d469-5cf0-3c85-bdaf-afe49879e433 | -7.25305 | -43.17389 | 2025-06-30 05:46:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c86e63ba-d6aa-3d48-8198-4b74fa7be745 | -10.79603 | -44.23591 | 2025-06-30 05:46:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 168.2 |
| edaa2580-dfc2-3093-b2bc-70f05e70959d | -10.79444 | -44.2472 | 2025-06-30 05:46:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 6c4ba654-fc4a-3275-b634-a68afd91cfd7 | -7.38077 | -43.8723 | 2025-06-30 05:46:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 81b11aca-ffc6-39d4-b556-111833b42d7d | -12.19963 | -49.63617 | 2025-06-30 05:48:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f2ea7a40-7764-3c8e-bfbf-7125e371f1a2 | -12.63073 | -54.2138 | 2025-06-30 05:48:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| b82aa1a5-66e3-356d-8584-a1769a20f31d | -12.61807 | -54.21155 | 2025-06-30 05:48:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 62da48b3-8d7b-3cea-8534-93310d96fa64 | -10.805 | -44.2319 | 2025-06-30 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| b371d3fa-44f3-36e6-b4a2-63f4acbac751 | -10.7855 | -44.2579 | 2025-06-30 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 33bf78a8-51a0-3a39-ab86-1e29ff1780e8 | -10.8046 | -44.2553 | 2025-06-30 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| be9ea845-14e3-3f12-a03a-cb3e7008beee | -10.7859 | -44.2346 | 2025-06-30 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 1e8d0d69-5516-3367-8319-6bdf9d4f7d11 | -9.23736 | -58.73182 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a4cb28d-2835-34bf-b27f-1d6825d698eb | -10.30161 | -57.04269 | 2025-06-30 05:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fcaed21-6ba5-3418-a925-421e813cecfb | -9.24681 | -58.74837 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d263422-331c-3941-bf9f-c048b0af348b | -9.23468 | -58.75085 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 384b193a-dcbd-3f64-9346-5bc2019160ca | -9.2295 | -58.74749 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 881b884b-6771-39b8-b899-284eefe2e294 | -9.22996 | -58.74186 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e7a05ae-8337-3a55-a5b3-982b7a5d1fdb | -11.20698 | -55.91885 | 2025-06-30 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62503ae9-95de-335e-852a-178071b85af8 | -9.23053 | -58.73924 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0252a948-2517-359e-ba70-ee4a3f567e69 | -9.24047 | -58.75165 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3559bf17-5a71-37fb-9348-f92304510522 | -9.24009 | -58.75723 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 705982bc-e9b8-328f-b4eb-a4405a641c82 | -9.25098 | -58.76143 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b356dc44-0925-3973-9935-dbe320604efa | -9.24573 | -58.75654 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 966bf7b8-68cd-3d6f-8dfd-908d07f22a72 | -9.70503 | -56.18817 | 2025-06-30 05:53:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6587989-aa1a-3841-8df1-56089fc43fbc | -9.24162 | -58.74503 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8074fcc1-df6e-355d-8462-c946c4407bcf | -9.2348 | -58.75238 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34471c59-4837-368b-8979-be6ab539efac | -9.24266 | -58.73668 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae263374-b76d-34a2-aa3c-58d395dd7ebc | -9.09088 | -59.49321 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c192919-1cb0-3ac8-9d26-01c0d5e3a7c6 | -9.11384 | -59.05162 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e79d4d14-6a4e-39cd-b143-bdec5cc33ce0 | -9.0849 | -59.49604 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7bf0cf9-b5cd-397f-9ef2-bc354f4596d9 | 2.7532 | -60.36706 | 2025-06-30 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ab3fbb5-0485-330a-a5b3-449b30126841 | -9.2411 | -58.74913 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ace2874f-90b3-3726-b5ab-bfafc1c04527 | -9.23104 | -58.73513 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 509484ae-0359-3827-aecd-103b43f1be10 | -11.02704 | -56.27446 | 2025-06-30 05:53:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6da03974-a2e6-3ade-9b09-5a9f5e162312 | -10.03911 | -59.35818 | 2025-06-30 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4d42ab9-4d58-3606-9d7b-44b60304fe81 | -10.2935 | -57.04988 | 2025-06-30 05:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36e7efac-77c1-362a-81d4-1c39f8f1be7a | -8.7263 | -64.15919 | 2025-06-30 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97546ea3-1cfc-3557-8970-a1224b70945f | -9.23994 | -58.75568 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66830d05-af04-3424-9279-43972362f460 | -9.24519 | -58.76057 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30ed418c-a291-3f2e-96ec-7975605acaeb | -9.23941 | -58.7597 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a36d9069-192f-3eb7-a238-88faa1bec420 | -9.09041 | -59.49686 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb3c4495-b04a-31e2-9137-6f199d3de0ba | -10.29366 | -57.05321 | 2025-06-30 05:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd061f00-3c81-3066-936e-b082b6307f69 | -10.03863 | -59.36201 | 2025-06-30 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 191d8341-b28b-3041-be47-25cb95ab9f33 | -9.25219 | -58.75483 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d0def71-63f4-3208-af63-62f1ff7f6204 | -9.24795 | -58.74159 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ee162e5-da6c-362e-8018-0ce0fe9f290e | -9.25116 | -58.76303 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c32c4422-3be8-3f19-bb42-0a53671065dd | -10.12318 | -57.77767 | 2025-06-30 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33446da3-81bd-3ba7-b98a-e7d2c91822e5 | -9.24627 | -58.75247 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ec503a7-bb28-38cb-8539-45b031763067 | -11.02705 | -56.27275 | 2025-06-30 05:53:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a83e9c91-0e14-364c-899b-43ec920a823c | -9.22941 | -58.74599 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f502784b-9619-3255-b3e2-6854ec17911f | -9.23685 | -58.73595 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6e6c0b3-b413-3c70-9586-c00073d6c23f | -9.25167 | -58.75894 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e938789e-a536-364a-afbc-b9c29680dd9c | -9.25207 | -58.75323 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fa19525-4a65-314e-8f09-c8327ff28c4d | -10.29434 | -57.0477 | 2025-06-30 05:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84151067-0697-3e7b-8f64-bf6134b88f04 | -9.10816 | -59.0509 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8d8b056-052e-3375-a440-18fba67e6f53 | -11.19993 | -55.91792 | 2025-06-30 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 587813f7-a332-3709-929e-b4ba534b04e7 | -9.2305 | -58.73774 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dddc3f55-c6a8-3aa0-bfff-52d7a4de7281 | -9.23002 | -58.74339 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05e71c5a-f4be-34bc-ae0a-347aa143cc24 | -9.17172 | -61.40419 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f48efc4-51fd-3624-912f-80f98feec03e | -9.23685 | -58.73443 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc0e0dff-c91c-325c-8b7a-2913cde57c19 | -9.24691 | -58.74994 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d6bcba2-cf60-3d84-a68b-f418289ecbea | -9.24737 | -58.74422 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad9c925a-8db0-3a3b-b412-1be2637b4f6d | -11.19913 | -55.92508 | 2025-06-30 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9833c107-f024-374c-8134-050714b73029 | -9.24214 | -58.74087 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c103597-1b7e-3687-a4dc-d0ac2b04ecf8 | -9.24743 | -58.7458 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed524d04-fac8-36b9-9e0d-fd1dd80ed92e | -9.22888 | -58.75008 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e88842c8-2193-37ba-bf2c-17402f1c791a | -9.24639 | -58.75404 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1de2ce3a-4c9c-30f4-99dc-f45e701a222a | -9.25044 | -58.76551 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4cf6cba-b6aa-3b57-b06e-59376c339d7d | -10.12942 | -57.77849 | 2025-06-30 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7769fb53-3ff2-349a-bff4-b2f2b1e64add | -11.19509 | -55.92115 | 2025-06-30 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41117a3d-2295-3353-bea2-a88dca907d4a | -9.24588 | -58.7581 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f1b1249-1dd9-34e5-a045-35977c29c80f | -9.70577 | -56.18193 | 2025-06-30 05:53:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fa2aeab-82f3-3980-9749-c0963b0bd0ae | -9.25153 | -58.75734 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af6f5f9d-3f4b-3de3-b004-db890fab9a33 | -9.04327 | -61.22935 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)

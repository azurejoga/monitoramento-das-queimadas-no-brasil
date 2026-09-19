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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dafd571c-9892-35bb-ab3c-66524ae9884b | -9.02581 | -48.73975 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b4e7c19-eea5-3336-a18c-20048d29da20 | -9.8993 | -46.53576 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c21a7ed6-0feb-3fb9-8e31-27cc0ee457e9 | -10.83734 | -50.91254 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 091ff178-b7bf-348a-b6eb-105236871b98 | -12.27594 | -49.16558 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2277a57-63aa-3459-8d9c-b22a296172cc | -11.80616 | -46.83895 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d8a4ff3-35fb-3540-a40c-918ed2a0e5a4 | -10.26874 | -49.99494 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae04bf6b-806a-3188-9586-21b15730e5f2 | -12.1609 | -47.00855 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 223e5c0d-b0b2-38a8-9994-a16f417e2990 | -8.35139 | -50.84129 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1009d740-014a-3d0c-b8dc-6e9afece7a3f | -16.09404 | -49.64291 | 2026-09-19 04:40:00 | NPP-375D | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ec7b516-19b0-318d-96ea-d6ea7c291637 | -13.3845 | -48.04028 | 2026-09-19 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c3110d0-0e7c-334a-be0d-779a27d23690 | -8.31817 | -50.92298 | 2026-09-19 04:40:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2123f5d8-355c-3116-857f-2bd715fc4959 | -10.59041 | -48.68297 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32e67352-df96-3c0c-ac0e-9c543fa06efe | -11.83006 | -46.83152 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45259d03-abce-3e72-ae78-eb0a7006f699 | -8.41858 | -54.7308 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8899800a-47b1-30f9-b65c-e5f7d31ddfd9 | -13.01677 | -46.93644 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07668c22-27c6-3faa-8dc7-47cce6617af0 | -12.41557 | -45.05362 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62a36b57-bb0f-3c04-b065-95a4536c8f2f | -13.68306 | -48.58728 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f758039f-fc56-3d2d-8cc2-a7101424fa05 | -10.55914 | -51.31238 | 2026-09-19 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 576a6f26-3589-3b11-a27b-676bf20676c6 | -12.40372 | -45.06538 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa12051c-f1b9-3437-83c9-164818bac78d | -13.86979 | -48.01116 | 2026-09-19 04:40:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24df9dff-a8e7-3f27-affe-02a791ad527f | -11.55608 | -46.90124 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 30a8f348-fd75-3f08-8b89-d2c863ec946d | -7.59718 | -55.69829 | 2026-09-19 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3289b60f-6173-3e99-9b8f-040df6eab5dd | -8.77642 | -48.68798 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0bb8de3d-3dcb-3d92-a33e-c4c85501f054 | -9.84447 | -48.37508 | 2026-09-19 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5745c0c7-8919-3618-bcca-67ccc9201169 | -10.93503 | -53.95718 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be7d9c51-03a8-3da2-b1de-592eb49ff197 | -9.25175 | -45.92528 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95ad223c-a86a-316a-be7c-1a9d22d7e902 | -11.55274 | -46.9007 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 5d2545c8-a5fb-3c93-bc6e-e84a140292ee | -13.61832 | -46.96576 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c337a937-dfea-36b7-ba9e-f00a1cad6d3f | -9.78409 | -45.05827 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f8a1c8a-500b-32ab-9cd6-6ab93fd7d8cc | -9.8055 | -48.33102 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ed405ad-ab8f-3c10-907c-9d016a502474 | -10.88296 | -54.05781 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fa372de-14fb-3545-bae9-4ffeaf8e6a51 | -9.72356 | -48.14772 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4149ae29-b4a9-3c62-a97e-048605e668bf | -12.98677 | -46.94327 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6c72f09-26cb-3804-84c1-c5a25be68cc0 | -10.40164 | -48.3213 | 2026-09-19 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f128b823-cf59-3b5f-a1e4-9337e8e6d323 | -11.30107 | -46.77662 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1063f7f2-c955-31e9-8fe5-1412eefa2962 | -13.00502 | -46.94585 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95d413fc-9573-3775-b5e0-8db49edb9db3 | -11.99028 | -52.46431 | 2026-09-19 04:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5151451f-f5c3-3b02-9397-5f588ac7f48f | -13.68087 | -48.57957 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca3cd047-bb93-3575-8beb-af7efce26641 | -12.28274 | -49.16674 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4274867b-14ad-3948-a6a6-25455aa6d6d9 | -10.69931 | -60.74008 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ba1924cf-3fd2-3aef-8303-201c6b1e477a | -10.45206 | -51.23853 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a50f434b-9724-3290-afad-3a307374b3a7 | -12.13309 | -46.96745 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b713732f-7741-3af0-8f32-9493aa65ecae | -10.0953 | -45.64181 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d3971e6-1949-3ad9-b7a1-20b1105e2d17 | -12.68801 | -45.96655 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b78e9882-999a-37db-a15e-e03192eb0e42 | -10.8707 | -56.2132 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5126a274-41b5-34b3-80c7-a7aecc576500 | -11.05623 | -47.94171 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f25c7e1-c537-3df5-9b1e-e378b129ea35 | -10.44817 | -48.67901 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff8ad68d-4a91-3eb6-8970-ab57cc268213 | -9.40512 | -50.19928 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd2210be-1ecc-3063-8b9d-36c78c946add | -11.52113 | -39.09001 | 2026-09-19 04:40:00 | NPP-375D | BARROCAS | BAHIA | Brasil | 2903276 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb56f405-7a60-3a46-81a8-feb98612a784 | -12.26163 | -47.12289 | 2026-09-19 04:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95136f6a-2be0-3c69-aeaf-b00ea4795009 | -14.51271 | -49.61291 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56e69bd7-bbc2-377e-b53c-b820efbc2f21 | -10.86985 | -56.18944 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccb4a8ef-6dee-302e-84a4-422cd2c1eca2 | -14.18106 | -47.85778 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| edcba45c-14fc-3f42-95dd-4cda85b64d17 | -9.65517 | -49.14386 | 2026-09-19 04:40:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02533d00-3202-3aaf-943f-98b3dff20dae | -14.94621 | -49.92874 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ea69d22-9dd9-30e0-81a6-5e31d9195c2b | -10.86398 | -56.19202 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bad7709-c260-3083-b7e6-3777fc52424a | -10.12519 | -45.5606 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4642a90c-19c1-3bdd-b416-e88c2417e7dd | -10.87652 | -56.21096 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a59e0c88-6dd7-3723-b279-5cfb7e2760a6 | -10.49687 | -46.2738 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01642889-b910-3def-909d-94775a8ad786 | -8.77886 | -48.67299 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9de55f2-04af-31c8-8a14-6329028eea31 | -14.93044 | -49.91816 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 847acdb0-43cd-3f7c-95d1-a13a18890532 | -10.97225 | -49.73935 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 731d14ef-c444-38d0-8881-6eba2e5b746c | -14.67391 | -46.67958 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d9b1dbf-310d-3500-b2c9-142de82a2e76 | -11.85729 | -47.60526 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a51a7241-0cc8-34b7-8d7b-059c2c89ba97 | -10.41115 | -48.32658 | 2026-09-19 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb9b95b0-0eb0-331f-84e2-9fb7e5738756 | -8.41954 | -54.72535 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd4c8dfb-9613-3317-956a-2704c63fbd54 | -9.80154 | -48.33402 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90f860d7-94a6-35e7-a17e-f849e9e2c332 | -12.16036 | -46.96823 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e073f9e-3a5d-3ff8-b1b8-3d9577afc490 | -10.20633 | -46.58469 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4488a3f4-b4a1-3ee3-8b4a-094b37fc7f13 | -9.24569 | -46.2156 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 697029a5-4cf0-30bf-860d-7cea8ff774e3 | -10.12938 | -46.29632 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c1a326d-353e-3526-b8e9-8da40eea2204 | -9.24011 | -46.20745 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4ae1656-cc33-3ad2-be73-5886ea964494 | -9.89322 | -46.55273 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 081a867b-bc55-3d60-9766-1ead1a95f785 | -10.50624 | -46.71867 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c457c749-8d02-3437-8813-fe17cb0730be | -10.12801 | -45.56491 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ced234ba-57a3-397c-847f-7307208a111e | -11.00274 | -48.31656 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5eef08bc-d166-3f73-aab5-909fab03a4dc | -13.01732 | -46.93284 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 390365b1-19df-3100-a3a4-9aec87da4914 | -10.53357 | -46.73437 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f495b85d-2ac9-37ab-9360-a09b534932d7 | -11.93907 | -55.92211 | 2026-09-19 04:40:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2062a15e-6617-3777-86e2-8d46bb8877f1 | -9.51423 | -43.24458 | 2026-09-19 04:40:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38841698-0690-3d78-a576-5c509f80dbc3 | -9.93701 | -53.98775 | 2026-09-19 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08d19d50-9e0e-3209-a018-f19eadf3efbc | -11.07295 | -48.31668 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5307d975-5c43-3bca-8312-e6c7ceefc8c5 | -12.14867 | -46.9773 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdee8b89-4fa3-355d-93dc-55db176224bd | -12.15701 | -46.9677 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d433640-ebe6-31e6-8266-26f8e37246f2 | -10.11785 | -45.56306 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1dcc054-442e-3a53-b1f6-671d87d4cc96 | -9.68033 | -48.32909 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3c6ca5f-ebba-3a69-92b3-c3fc1c4b8049 | -15.05135 | -48.59934 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec4620dc-963e-30d2-8f97-d2ad5291fba5 | -12.58466 | -49.09604 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3de74c3-7826-3819-99f0-65ca81716ff3 | -10.41173 | -48.32299 | 2026-09-19 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f89d42a9-b9d1-3c42-a823-6519e3d05e3a | -11.14168 | -54.02669 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 13f20b87-1955-34a2-8aae-a9b1c207c415 | -12.99503 | -46.98819 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3ba9ed59-ccc6-3c3b-9c5b-3d17b54da4c0 | -12.12977 | -47.01068 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59833df7-c6ef-31e8-b1fe-56a7d1f08690 | -11.12311 | -45.30045 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 743f8ae6-31f8-39c7-bb4f-691455b106ca | -11.07411 | -48.3095 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83c0b464-81bd-334c-9b73-6436ed894495 | -11.9802 | -52.45165 | 2026-09-19 04:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfaa53aa-d141-38d9-9608-10916cbd9b2e | -11.33466 | -47.36089 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe3e24bc-06cd-36e2-a5ef-5790ed06586d | -12.14088 | -46.98334 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c68d7cfb-c14d-3723-b78f-e6d2ff41d7be | -11.31408 | -51.7443 | 2026-09-19 04:40:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd8133a0-0c52-3bb5-b631-b566e2b10a71 | -11.80674 | -46.79155 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 395474d4-5267-3a21-8328-996b220dca53 | -14.66653 | -46.65928 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README64.md)

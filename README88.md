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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc54f9aa-c6ea-388b-abf0-5706331fdfe9 | -13.61483 | -48.32354 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1229fb2e-3d2f-30fc-8ac9-6e6a4fe9188d | -10.71252 | -60.73189 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66642b3f-c0cf-380a-8b1e-d75189461c00 | -14.94038 | -49.93759 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28e3714d-224d-32fd-aac6-782374af0fd3 | -12.12592 | -46.98573 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4cf1a1f6-6189-39a7-a2e3-6c4902380f4c | -10.90897 | -53.98444 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52392908-2829-311b-93c7-cbefb292bead | -10.86186 | -56.18767 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09601cd3-3805-369d-a3d9-0382eb926975 | -11.94222 | -55.91901 | 2026-09-19 04:59:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a986cf08-79f5-35d1-aff0-b954790dd0b0 | -11.0182 | -54.13114 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aeafed6f-08a3-3dff-8b3a-c48bee299811 | -16.79974 | -46.98608 | 2026-09-19 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e288e59d-2d47-39fa-beeb-30a2ffcfab9b | -11.49762 | -50.73092 | 2026-09-19 04:59:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcfd03c9-3766-3647-ae32-43ede9439354 | -10.87249 | -56.20949 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feb670e1-9c2e-3df0-89fc-5a4829c55f06 | -14.10013 | -44.83079 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3440e482-b25b-3161-82fd-8f705b07723d | -12.68795 | -45.95365 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4db70962-4fb6-32b9-abb8-4662d6eecf25 | -13.62944 | -48.31306 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e44f77aa-d7f5-3e2c-8ec9-556155c0ca02 | -10.68708 | -60.73874 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d579f53e-f1bf-3e74-a5c9-a00039c9878b | -10.86875 | -53.98146 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c1d8ee5-9f43-3164-bb7b-ef225c67e65d | -11.80422 | -46.84241 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c84821f1-528a-363f-914b-7bb80b913361 | -10.71166 | -60.73655 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bebbc61-fe92-3905-b5e3-afa8b69cb5a2 | -12.99019 | -44.8376 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01054839-9cd6-3519-9fb0-4c442b9378cd | -11.42448 | -51.45234 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c278769-c392-38df-95b0-f73b44746002 | -11.67166 | -54.44357 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 626532e0-8878-3b35-9b44-86377c74c739 | -15.66457 | -52.74475 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f19d325e-02d2-3bee-814d-bfa277bfc07c | -13.67929 | -48.57964 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7485b0e4-d15d-3b87-8e86-537d421f3120 | -10.86631 | -54.10315 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a84785a4-5918-393b-8e61-a7e9b5c3aad6 | -12.28273 | -49.15941 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bd3c7f58-41b2-3347-8251-f2a555afbe1f | -10.85922 | -54.10564 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c30bbcfe-8ce4-39d4-8f8d-bb619abf631d | -13.38362 | -48.03999 | 2026-09-19 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da43c013-95fa-3552-9d22-b65816fde5b5 | -12.58069 | -49.1002 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4517599-f5aa-3734-a55b-09adb94fcc5d | -11.11214 | -49.43911 | 2026-09-19 04:59:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bce66d66-ee61-3f67-8d77-8a6bf5e27dbb | -13.60732 | -48.31395 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ac582578-5672-3e8c-ba43-e0e9dc68a7c7 | -16.80469 | -46.98663 | 2026-09-19 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0376e7fe-402a-337b-8bac-a5fae9458382 | -12.59875 | -50.88062 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8968e2ae-1d54-375a-b099-6cbcd9b1b29d | -14.78467 | -48.58521 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f087e82d-b2bf-31f7-a4d5-d1da241d5463 | -12.58947 | -49.10159 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eb24a212-ab9c-30cd-a435-41471bdbc66a | -10.92997 | -53.95911 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a1b09cd-9448-3353-b83b-c7338c508876 | -14.0999 | -44.83391 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e04fb062-2725-3e9f-bf4b-f0871cf515ef | -12.69088 | -45.97083 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1841cad1-2f1a-3fbb-82b6-27604941425c | -12.58423 | -49.10436 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e94a9c5f-34ac-341c-bb2e-e8eb8861f6ca | -10.87184 | -56.21339 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f12bf3d1-5cf4-3a28-a288-0f459d465990 | -12.85671 | -46.33732 | 2026-09-19 04:59:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| af4edc9c-f74b-32ed-9dd2-fe02c2a77708 | -11.81178 | -46.84542 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 402a2712-ce08-3399-9a93-10bb003bb8f4 | -12.58879 | -49.10133 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 87d8617b-92b6-3a53-8058-2767a2ed5bbe | -17.24244 | -46.72186 | 2026-09-19 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f29fe2e9-8d11-32c8-b949-e45ca260e97d | -10.86476 | -54.09216 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29d9cf88-007a-394c-bfc3-966a15f4a4a9 | -10.8752 | -54.06867 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb62bfcb-c8fb-3b67-94ce-ca2d1345af2d | -14.79489 | -48.57444 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 160dce71-3b26-327c-9c35-56f7de4899e2 | -12.34934 | -50.69756 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed1481c7-6835-3fcd-8983-f9eb62b52902 | -12.15472 | -46.9725 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50c1b12e-e597-352c-ba71-923f1d5c1754 | -12.70301 | -45.95529 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0f6358d1-52c4-3d1f-9b6c-ab7099afd4b8 | -12.13577 | -47.00951 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5338cf7a-59ae-3921-bdd8-45b56d48be8e | -16.09497 | -49.64639 | 2026-09-19 04:59:00 | NOAA-20 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 684b075b-bffd-341b-8acb-e40b01e3ec91 | -11.80358 | -46.84716 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68bb447a-a536-3cf6-86d4-3bff5bba3e31 | -12.48613 | -50.05124 | 2026-09-19 04:59:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 175bd107-ca9a-391c-a882-bd6336aaf0d5 | -12.70247 | -45.95963 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ced2a4cb-511d-3398-8934-1a4def60c45e | -12.86231 | -46.33257 | 2026-09-19 04:59:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5f383304-6e4a-3435-8534-24c992355072 | -15.05675 | -48.60121 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5b2fc96-0ecf-380b-9f33-5c00d83e1d50 | -16.88395 | -50.58651 | 2026-09-19 04:59:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d6f84c4-67b2-3a1f-a6e1-b5e552fb110c | -10.71681 | -60.72982 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 679f1b24-06be-33d2-9d35-1575dc554c27 | -13.62246 | -46.96602 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba035bee-70e7-3ed3-8e0f-995586548cee | -11.40775 | -47.28461 | 2026-09-19 04:59:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf77e26b-8078-3552-b845-4bb301e8d9e5 | -10.87043 | -53.97103 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54a537f4-3bf0-3413-a276-c1eb33f0011a | -13.62511 | -48.3125 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68e90405-4d4e-34cf-a00e-59319916a07c | -14.68467 | -46.67965 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f30f072a-6d96-325f-8d12-9373a3b8df4f | -11.19944 | -55.03278 | 2026-09-19 04:59:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27133f9d-2352-36a8-85d9-266b1460d077 | -14.50929 | -49.61137 | 2026-09-19 04:59:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b30dd90-2416-387d-883b-6a4d11e83d8f | -10.86534 | -56.1882 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ded5f10-de43-35d7-bc9f-d9a640b9b424 | -12.58121 | -49.09661 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e344bfd-026c-367f-b81b-1c68873891a7 | -12.54006 | -47.09148 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7e67627e-0b79-3083-8d41-8430c43629fe | -15.02576 | -48.55505 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40e32274-6e76-3fff-afc4-8502f3df4ff5 | -10.86197 | -54.10969 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d23214aa-f122-3545-83d1-3d50d1be2c9d | -15.77209 | -56.46647 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef76c7f1-f293-38d2-83f4-8a19f0adc920 | -10.86947 | -56.18487 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2d82f9f-d747-31ef-ae38-448f86602e6b | -12.58898 | -49.1052 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 229a8344-148d-351c-a892-c89e63a825b5 | -12.85967 | -46.33347 | 2026-09-19 04:59:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4959bc0f-da4e-3945-9bb7-c69dc19b669b | -11.67885 | -54.44114 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d6fb738-3fd6-3362-b635-936237456886 | -13.87486 | -48.59649 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caec8f66-d9a3-3cd0-91e5-45e728067297 | -14.65732 | -46.65897 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 27a95c0f-773f-37eb-8ea5-bec7bdfe238a | -10.86902 | -56.20889 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea209add-fb0c-3263-b704-f0b8c480cd1d | -11.4198 | -51.45974 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b17adbe-a563-3db9-9096-c19a5423fbd6 | -11.30625 | -51.73026 | 2026-09-19 04:59:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f615b6bc-0cf8-3d7d-b446-1fa65867d8f0 | -12.54122 | -47.09084 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| adc0725b-d251-3fd4-a9eb-c0834f46ebcc | -11.19435 | -55.043 | 2026-09-19 04:59:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09b5096d-fbf8-39ee-968c-9179bc507f58 | -10.86055 | -56.19546 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cab6976a-a163-3f6d-b873-1ca9544dbd31 | -14.12849 | -45.55247 | 2026-09-19 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3dd06dd8-65b4-3595-a992-3c0e715a5866 | -10.86337 | -56.19993 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a99eec2-a488-3a6a-8c22-8c48a636767b | -11.83234 | -46.83293 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c0cfc01-1c5e-310e-8b7b-93b85f77efcd | -14.78952 | -48.58179 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9729c97d-1a76-3106-8c65-c0c47e21c9b6 | -11.41735 | -47.28133 | 2026-09-19 04:59:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8276856c-be63-389e-a095-625ceb360eb7 | -15.62605 | -52.72773 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efaee5d0-44f2-38c7-86e4-1c42c77f15e3 | -14.93065 | -49.92037 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bab8b787-22f6-36f6-bc51-916b320b594b | -12.15479 | -47.00798 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c56280b3-4cca-348b-8169-1dd3278162a5 | -11.80708 | -46.84517 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4edaaa04-764b-3bcc-a87e-fb4f496a7191 | -14.09968 | -44.83443 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 447ba21c-ca79-3ace-9b10-46a7258097f8 | -14.67487 | -46.67836 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6f613423-fb22-3869-90d7-fd4b9aa2b77c | -17.31815 | -46.62976 | 2026-09-19 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bc94b78-8390-3e23-b28f-350f269cbf77 | -11.96737 | -45.77443 | 2026-09-19 04:59:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4d8bb64-dc73-3fc8-af45-c09afd2ab406 | -14.94828 | -49.93886 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dab3506-2b3c-32c3-8477-cd1fa1a7d17d | -12.85419 | -44.39236 | 2026-09-19 04:59:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7ba1478-01d9-3be2-a485-2754d018a4dc | -15.02349 | -48.57201 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 211e4185-6537-3510-ab40-92fbb25530e9 | -12.3888 | -48.4762 | 2026-09-19 04:59:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README89.md)

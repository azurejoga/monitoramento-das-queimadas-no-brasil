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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75517240-6a6a-313d-9d4b-7b83a4b74bc7 | -13.84 | -45.26 | 2026-10-02 16:15:00 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 741a9ece-8538-3503-b9f6-9b8f5f9db4e3 | -1.29 | -54.55 | 2026-10-02 16:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf27593-cee2-3a2c-ab7a-9b7169381d1b | -11.51 | -43.5 | 2026-10-02 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94096733-2450-30ab-80c9-f022d6b0d17e | -13.35 | -43.85 | 2026-10-02 16:15:00 | MSG-03 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f71b54f2-3921-35a7-a4e5-bb65edeecb04 | -1.26 | -54.55 | 2026-10-02 16:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 209a618c-6ad2-3ce9-89cd-a969d6a31f6c | -9.95 | -43.47 | 2026-10-02 16:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90e3b583-5a3d-35db-b5d6-1a07431bb095 | -1.4672 | -48.9097 | 2026-10-02 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e630e046-b346-337d-b2c9-f85ca92c14af | -1.1351 | -48.8501 | 2026-10-02 16:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 2df185ad-e174-3b18-b51a-465fd4b19d78 | -1.4303 | -48.9102 | 2026-10-02 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e852acc9-2234-3b0d-a4e0-d82657ed6e60 | -1.4303 | -48.9316 | 2026-10-02 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 37b3aed7-2ba6-3742-a831-f042f2ca831a | -9.8806 | -64.9764 | 2026-10-02 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 13f03a6a-82b2-3a37-9685-3e7ef0559c2f | -1.1351 | -48.8501 | 2026-10-02 16:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 139c14d2-eef8-37f7-b2c2-3227e8202653 | -1.4303 | -48.9102 | 2026-10-02 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e394e348-7eb2-3f89-9395-616d6b421df7 | 1.8037 | -55.6051 | 2026-10-02 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 7a2177ce-ed7e-3116-822c-038f518b4b51 | -1.4303 | -48.9316 | 2026-10-02 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 471dd7e1-8536-3ca2-8df2-950821f02ff7 | -1.1351 | -48.8501 | 2026-10-02 16:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4375fc77-1210-3ecf-9af1-65b527949708 | -1.4303 | -48.9102 | 2026-10-02 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 28642f8d-ab68-33cc-8fd9-5fe21d99ae7f | -1.3192 | -49.1249 | 2026-10-02 16:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b7a24e68-80f1-3e6c-9d7d-cb645582c82a | -1.4303 | -48.9102 | 2026-10-02 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a58eeeab-9ca9-3740-807d-abae8b931b4d | -9.1147 | -65.9379 | 2026-10-02 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2ade9d60-8e44-3281-b4f1-6be4522ecf2f | -1.4303 | -48.9316 | 2026-10-02 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5310a715-eaef-3fd1-b99c-0cedcb41bed7 | -1.4487 | -48.9313 | 2026-10-02 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3327b4ae-b496-3c63-ab6a-f6d95d943132 | -9.077 | -66.0881 | 2026-10-02 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 2efd121b-e6e2-352e-881a-ae0a8c734323 | 1.8221 | -55.5654 | 2026-10-02 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| acdf06d8-76b7-3f51-bf37-215862a639f9 | -1.4672 | -48.931 | 2026-10-02 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6864d67d-4d4f-317e-b02c-d6dcd568b68a | -9.077 | -66.0881 | 2026-10-02 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| ba79af00-e997-3102-ad9a-0a76e6103a95 | -1.4303 | -48.9316 | 2026-10-02 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 6a224190-fc67-37a4-a49d-d5eeebfaae77 | -1.4303 | -48.9102 | 2026-10-02 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 0c81e53a-8a65-3c79-a177-cd304aa5c743 | -1.4487 | -48.9313 | 2026-10-02 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 1f27f972-5a1d-35ae-bec6-b964a2d039c5 | -1.3192 | -49.1249 | 2026-10-02 17:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 77c21283-ed7b-3702-8df9-961dbd538fea | -1.4672 | -48.931 | 2026-10-02 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c4bde5ba-4b4e-30b3-93e7-a9e86df9d9ba | -1.4672 | -48.9097 | 2026-10-02 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| e603f568-dfbd-3224-9613-4ed691894ae7 | -11.47 | -43.4 | 2026-10-02 17:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b916eb58-32c6-3d4b-9f80-1cfd06dd0acd | -16.54 | -40.53 | 2026-10-02 17:15:00 | MSG-03 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf45621e-65f8-3967-918c-25fad40c1dc0 | -14.48 | -40.7 | 2026-10-02 17:15:00 | MSG-03 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| eb96da7b-033d-384f-a50d-6cf24f3b029f | -1.26 | -54.55 | 2026-10-02 17:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31259803-30a6-3023-9997-d7228b10d3ee | -14.57 | -40.73 | 2026-10-02 17:15:00 | MSG-03 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 277ec15b-2f6d-3eca-8f23-af6da9c898cd | -4.89 | -45.13 | 2026-10-02 17:15:00 | MSG-03 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb29650f-f759-33fa-9334-9e0b5dea349c | -11.72 | -43.64 | 2026-10-02 17:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b78a59f2-3918-375d-b7aa-08eafbfbad29 | -14.48 | -40.75 | 2026-10-02 17:15:00 | MSG-03 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 179b5ff3-20a7-39aa-870c-fdd0e42a2d80 | -11.29 | -44.27 | 2026-10-02 17:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b4b326f-f97e-37b9-90a1-6b6e35550784 | -15.97 | -41.44 | 2026-10-02 17:15:00 | MSG-03 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93c02649-4cd1-325b-9dfc-034dbe7c7399 | -16.0 | -41.45 | 2026-10-02 17:15:00 | MSG-03 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b22471c-c62e-30d2-847b-eeb0629b3463 | -15.15 | -44.08 | 2026-10-02 17:15:00 | MSG-03 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 74a1c720-5b64-3294-a1c4-9d3c3ac9d4cb | -15.61 | -41.68 | 2026-10-02 17:15:00 | MSG-03 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b7265502-7851-3050-acac-cae8c635ea5d | -1.1901 | -49.0627 | 2026-10-02 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 0b59a513-68e9-365e-aef3-0e18d239de98 | -1.4672 | -48.9097 | 2026-10-02 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| be2ab623-730e-3d65-b5d7-a3ed6a505df7 | -1.4303 | -48.9102 | 2026-10-02 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 8b7c49fc-72df-3958-84ee-2eeaae9a1119 | -1.4672 | -48.931 | 2026-10-02 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| abe4d927-7bfe-3d37-b28e-bd7d024617e6 | 2.5502 | -50.9526 | 2026-10-02 17:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 92.9 |
| d75576f3-c115-3688-9cae-41f62d11c316 | -1.4303 | -48.9316 | 2026-10-02 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1b5125db-bb31-38b1-a9e3-815904be6a79 | -9.077 | -66.0881 | 2026-10-02 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 66f23839-e0b9-3dd1-8ca4-1478658870d7 | 3.4341 | -51.2808 | 2026-10-02 17:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 55.2 |
| faa45fc1-b693-3d9b-bd5f-f63685a4cb8c | 1.8037 | -55.6051 | 2026-10-02 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| e3981699-d452-3465-92ad-30233b821444 | -1.4672 | -48.9097 | 2026-10-02 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5d1dcc52-8590-3782-b94e-dbcad60ff29c | 1.1323 | -50.7277 | 2026-10-02 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 82bf9454-87d9-3df0-a460-0ef66552a68b | -1.4672 | -48.931 | 2026-10-02 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0a6c9091-5f7c-3e13-97c9-ec996acc740b | 1.7399 | -50.8235 | 2026-10-02 17:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 102.1 |
| fdb437db-490e-34bb-9d2b-f3b3b1ebdc78 | 1.8221 | -55.5654 | 2026-10-02 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 3bd0a562-6b72-3088-b30e-bca39c325dad | -1.1166 | -48.8504 | 2026-10-02 17:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fa85b8e5-56dc-3e5c-9b18-60a6dc6cfe69 | -1.1163 | -49.021 | 2026-10-02 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| cbe56a39-9137-37aa-a378-a8b38ae68c49 | -1.4303 | -48.9316 | 2026-10-02 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ffd39af5-4b82-35e2-813d-e1193422329b | -1.19 | -49.1053 | 2026-10-02 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a184d25b-bab6-312a-9ec4-38ae884b4e84 | -1.4487 | -48.9313 | 2026-10-02 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e462fdc3-b69d-3d4b-9a84-f3dcd2458113 | 1.8221 | -55.5851 | 2026-10-02 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f5baa2b3-008b-3b60-806c-c5ce14735d67 | 2.5502 | -50.9526 | 2026-10-02 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 108.5 |
| ae3a1cc4-456c-3c02-b4f6-8a2b2c246634 | 1.8037 | -55.6051 | 2026-10-02 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 381186a1-381d-3e62-b728-ab2ad3795a68 | 3.4341 | -51.2808 | 2026-10-02 17:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 63.1 |
| dc20119c-0857-3dad-9e3a-b729a0d4816e | 1.8221 | -55.5654 | 2026-10-02 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 9da85fb9-c1a8-359a-9088-6a6e94006bc3 | -9.4803 | -67.1555 | 2026-10-02 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 863e9dc5-fc1a-33b3-8951-e40baf8a5c16 | 1.8221 | -55.5851 | 2026-10-02 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| e1902438-6a54-3ce7-9483-677e7659cc77 | -1.4487 | -48.9313 | 2026-10-02 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| bd04d2f7-4bb4-39c2-aad0-696783da605a | 1.1323 | -50.7277 | 2026-10-02 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 919b8f3e-15e5-3162-8596-9b79be25cefc | -3.1061 | -50.2686 | 2026-10-02 17:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| e1b978cf-7045-392f-825d-8cc506f6c521 | 1.7399 | -50.8235 | 2026-10-02 17:40:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 7ebe88a2-5170-3af2-80f8-8cbb078fd4c4 | -1.2271 | -49.0197 | 2026-10-02 17:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 0070655d-35d2-3255-a138-569774406fc3 | -3.106 | -50.2896 | 2026-10-02 17:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 1230659c-66eb-34f2-a259-353accdcd25d | 1.8221 | -55.5654 | 2026-10-02 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 00edcd44-24e2-302a-aa7e-191e843b2505 | -14.4904 | -40.7031 | 2026-10-02 17:50:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 266.9 |
| 87b31461-167b-30d1-836f-fa84adbaae2c | -1.4487 | -48.9313 | 2026-10-02 17:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f5bcfdcf-59e3-3ba6-b8ea-387464887e0c | 1.8037 | -55.6051 | 2026-10-02 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 170818ce-5a24-3611-9a37-709f572737d6 | 3.4341 | -51.2808 | 2026-10-02 17:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 34933e74-e455-369b-9006-c36b646d051b | 1.7399 | -50.8235 | 2026-10-02 17:50:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 2b6c956f-910d-399e-a643-a7ff9bfb514c | -1.1163 | -49.021 | 2026-10-02 17:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 60ade2ba-c7ea-3291-a443-9174d7be09ab | -1.2271 | -49.0197 | 2026-10-02 18:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a2bd042f-9204-3d0e-b59d-81d29620b9a4 | 1.8504 | -50.8424 | 2026-10-02 18:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 804963ec-6ad0-3614-9c99-1ab1593b952e | 2.5502 | -50.9734 | 2026-10-02 18:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.7 |
| bdded87a-5659-3e9d-a03d-1a8d3f74d8cc | -6.8952 | -43.6833 | 2026-10-02 18:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e51d45ce-9cde-3b8b-bd8d-3924a1ecdf15 | -3.0575 | -44.392 | 2026-10-02 18:00:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f878393a-af1f-329e-9323-de4e70fdbb13 | 2.5318 | -50.953 | 2026-10-02 18:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 106.3 |
| e6596592-0b78-31ac-9c4a-808ec4b6d61e | -14.4904 | -40.7031 | 2026-10-02 18:00:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 220.9 |
| 2c37bf82-f493-3456-8141-6937dc5cede0 | -14.4701 | -40.7327 | 2026-10-02 18:00:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 146.7 |
| 859eaf0b-76ef-3152-a7c2-e08fbe61d3a7 | -0.8584 | -48.6392 | 2026-10-02 18:00:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c94f5dab-444a-34d7-95e4-4fc36f23617e | 2.5502 | -50.9526 | 2026-10-02 18:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 100.5 |
| e3b58367-8407-355d-815c-ae3e22a434b0 | -0.7839 | -49.2583 | 2026-10-02 18:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 32cd3e8a-8753-3e4d-9676-79800bf5154c | -14.0638 | -40.5435 | 2026-10-02 18:00:00 | GOES-19 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 1547a9d4-66c8-3b5c-aa5e-f8b22be4fcee | 1.9239 | -50.9035 | 2026-10-02 18:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 51ecfa60-8324-311c-95c3-c47fb5555b1c | 3.4341 | -51.2808 | 2026-10-02 18:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 39f08e94-f0a3-3d02-821a-7ed340618aac | -0.7839 | -49.2795 | 2026-10-02 18:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| b657a0fe-b61c-3f46-a17f-28916a49f757 | -6.914 | -43.6816 | 2026-10-02 18:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |


[Clique aqui para ver as próximas entradas](README107.md)

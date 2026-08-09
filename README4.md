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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc274fff-c977-30cc-8efe-0ec332fe2dc3 | -9.1493 | -59.652802 | 2026-08-09 01:30:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 987788c0-5a0e-3459-9e9c-8c29fae2764e | -6.8202 | -56.423698 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0704757f-d86d-32ec-885c-09a5829f448d | -10.0759 | -60.5005 | 2026-08-09 01:30:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c8cf7dd-d157-3e94-af8c-6ca38c685b2c | -6.1368 | -57.7146 | 2026-08-09 01:30:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22bec624-8e89-39b9-9cd2-35550bd02f2c | -6.8419 | -56.384998 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 465332fa-6d5f-3227-aea4-2a0b85e19447 | -6.8567 | -56.4039 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9af8896-0d0d-328e-b01c-ae47b712e7dd | -9.1477 | -59.645599 | 2026-08-09 01:30:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db91ae18-8359-3e3f-bc7e-9aad1c3aee29 | -6.8422 | -56.4296 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d7f84b0-077e-3036-8070-e09562c273f9 | -6.8275 | -56.4109 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01455c2b-284f-3f32-bcb8-1d2dcb198547 | -6.837 | -58.939499 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a24d2c18-6681-3695-a205-398c956306f6 | -13.9656 | -58.114899 | 2026-08-09 01:30:00 | METOP-C | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63f408c2-0cd2-3d31-961f-b3257a2b5e63 | -6.8896 | -58.943699 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0fbeef25-a58a-3d95-bd86-d9d2d3a44e7c | -6.8227 | -56.4342 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a41b38-e0f2-318f-9ccc-33a0dfb83fe9 | -6.8445 | -56.395599 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c8d3bb9-9d44-3967-88a0-9ee3aeb696c1 | -9.3334 | -63.445202 | 2026-08-09 01:30:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd0079a-bbc3-34f6-871f-d4cc5f39d3f2 | -7.3836 | -59.9604 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80c9fa28-f32b-3987-8443-9adc28a73424 | -8.1515 | -55.399399 | 2026-08-09 01:30:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1157c013-97b7-30dc-8440-7ad010ad49d8 | -19.093 | -48.294701 | 2026-08-09 01:30:00 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf2b7b53-7e67-3b97-aaab-ee1d3fcb1858 | -6.1389 | -57.723701 | 2026-08-09 01:30:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 545ee665-47e5-3959-9874-52c9aa6e4c80 | -14.0465 | -53.823799 | 2026-08-09 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1f5a28f-4bb4-30a3-b644-1c88dcb59f9c | -20.452299 | -57.405102 | 2026-08-09 01:30:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b2dbf91e-1296-3dcf-8f8c-b1aa41f3faa2 | -14.066 | -53.818699 | 2026-08-09 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 736b8790-7fdc-3397-999a-10c677649085 | -6.1486 | -57.721401 | 2026-08-09 01:30:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb0adbcf-ec08-319c-bcee-b2aa23093e48 | -6.8347 | -56.397999 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df3be922-219e-33d5-9377-82c33d15933e | -14.0562 | -53.821301 | 2026-08-09 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1cd815a4-03ef-3645-a841-19ad8cfa086c | -18.457701 | -50.515999 | 2026-08-09 01:30:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 473295a0-6be9-30bf-a560-c64501448974 | -6.1346 | -57.705601 | 2026-08-09 01:30:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b7d4c9-2a45-3141-9625-697b5a02eeb4 | -6.878 | -58.938202 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 507ea719-0501-3b5d-bc36-d7e8fead7801 | -14.3417 | -51.9818 | 2026-08-09 01:30:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00c5ba86-d490-3e1e-912e-f3496ce585c0 | -6.8542 | -56.393299 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23c2f9ca-52b5-35d8-b041-088ca773c570 | -5.8839 | -57.648701 | 2026-08-09 01:30:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 671114fd-ddd9-3bd4-8778-7c606caaf2d8 | -6.7202 | -58.925499 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a395176-e71c-3731-ba27-45b2d4915575 | -6.8762 | -58.930401 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd8b30b1-1bb4-3c91-ad76-90470d53b764 | -8.6828 | -62.873901 | 2026-08-09 01:30:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77fc5437-661c-339d-86d2-6988d52c93d0 | -6.83 | -56.421398 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41658a95-da45-3f45-9c95-00c5c22ab307 | -8.6465 | -64.1063 | 2026-08-09 01:30:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3c8b4b-ed4a-3191-90b0-b8c4e34b98a1 | -6.4181 | -55.779701 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e55fca5-5a2e-3af0-a4b9-9ff8a806b137 | -20.796801 | -57.699501 | 2026-08-09 01:30:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1310423d-48b2-3e17-9d4e-ffb6e661884e | -13.9639 | -58.107399 | 2026-08-09 01:30:00 | METOP-C | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92738b38-30c6-3fa8-90ce-31d81b041291 | -19.108999 | -48.314499 | 2026-08-09 01:30:00 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 43f0759b-86e8-37a9-983e-82dd46993427 | -15.3714 | -53.777699 | 2026-08-09 01:30:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1386d7d1-c853-35ec-a150-9205b1f81682 | -14.0757 | -53.816101 | 2026-08-09 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac54c79-987e-34e7-b4f2-2090777baa5b | -14.3158 | -54.947899 | 2026-08-09 01:30:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0cd03b4f-939b-3591-b7cb-9c764635078e | -14.0271 | -53.828899 | 2026-08-09 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9ab8ad-7374-37db-bac1-b582fe18fefb | -14.3458 | -51.997501 | 2026-08-09 01:30:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c522530-9bba-30a8-ac91-78d35ea71784 | -13.9559 | -58.117199 | 2026-08-09 01:30:00 | METOP-C | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6235a3cf-7dcc-3bc5-9fd1-ac306464c092 | -19.1026 | -48.291801 | 2026-08-09 01:30:00 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 98630c14-23d3-31c9-b97c-f8188b4f6747 | -6.8325 | -56.4319 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a949b10c-fd00-32fc-873b-f5e7c91525fd | -6.7043 | -58.945599 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c351f59-406a-39c7-bef8-1e4270700e89 | -18.4531 | -50.499199 | 2026-08-09 01:30:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c294087c-ecdd-3014-9fc4-a5d4fe2fd8f6 | -7.3951 | -59.965401 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6190798a-751c-3824-984a-9b99bdfcdc23 | -6.4209 | -55.791401 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6db8a514-413f-3903-b12c-4f06b0bab845 | -19.0994 | -48.317501 | 2026-08-09 01:30:00 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7683919f-6e06-390d-889f-5c3427bc9706 | -13.9461 | -58.119598 | 2026-08-09 01:30:00 | METOP-C | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bee37dca-f83d-388a-ad2e-21104d017348 | -6.8372 | -56.4086 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cee5310-ff74-3936-a236-5a88783de363 | -8.6926 | -62.8717 | 2026-08-09 01:30:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0586b6-ddac-3afb-afcd-762c526965bd | -18.6418 | -49.8531 | 2026-08-09 01:30:00 | METOP-C | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11da4209-8fdc-3d87-9c49-ebdfb0815062 | -6.8495 | -56.416698 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0be70a74-701b-3ae0-972f-0aa77e0797fa | -6.886 | -58.9282 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d58e42c9-6cf6-36a6-8c53-0e49a4217977 | -7.5552 | -61.158699 | 2026-08-09 01:30:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6f0a907-f0cc-3d8d-8a25-8af2cfa65584 | -20.450701 | -57.397701 | 2026-08-09 01:30:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 776c8a1d-7bd0-38a6-882f-bfc05f4ef2a2 | -20.816401 | -57.694599 | 2026-08-09 01:30:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 86c1f65b-d655-3bcb-b2fa-2bbc9fdb89cf | -6.7159 | -58.951099 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1a32b61-72d1-30ae-900e-cbe6cd87e2c9 | -8.6796 | -62.8592 | 2026-08-09 01:30:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 822b5e17-e254-3974-b0d0-37328e7ff180 | -11.9946 | -60.5075 | 2026-08-09 01:30:00 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d6f6c29-91a0-31eb-a815-194039ff267a | -6.8397 | -56.419102 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b36a4df-2ef5-38b0-b0ed-c1168f385dbe | -6.8351 | -56.442501 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b230c602-4578-33d2-af2e-4e0466a4ee39 | -6.8177 | -56.4132 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06bd68c1-486e-3ce6-baeb-943a2edf22ed | -18.6469 | -49.871498 | 2026-08-09 01:30:00 | METOP-C | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f7286a1-7609-313b-ad62-f6951289c3dc | -19.0961 | -48.269001 | 2026-08-09 01:30:00 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 936d2c2a-7680-3e6c-a857-b5471106f25d | -6.8352 | -58.931702 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 341784b6-f138-3650-8fa9-62608a520295 | -6.8878 | -58.936001 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cf12edc-36f1-36e3-a931-4c033f840b9f | -10.9207 | -57.118301 | 2026-08-09 01:30:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b91eb9b-de88-37be-be18-ca00741b31eb | -6.847 | -56.4062 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5479e619-bca4-3c9f-aa34-28057f96d45c | -13.9542 | -58.109699 | 2026-08-09 01:30:00 | METOP-C | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c38dc27-71f7-3301-b535-2bdcb752eca6 | -8.6812 | -62.866501 | 2026-08-09 01:30:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27da6f69-cad0-32e0-9bfd-8200ed5ff36d | -12.3322 | -53.142601 | 2026-08-09 01:30:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79f11f0f-86a8-341a-b109-53305d360e90 | -6.1476 | -57.7215 | 2026-08-09 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c021628a-436d-3a6b-92f4-782a8b82ccc5 | -13.9541 | -58.1162 | 2026-08-09 01:50:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| d620d42c-71df-38b8-b5e4-8c24add0a301 | -6.1476 | -57.7215 | 2026-08-09 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 165810c1-79c9-328e-bd22-3d98a08a5d84 | -6.8389 | -56.3949 | 2026-08-09 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3277e0d6-08a0-3f1e-b605-bfcba9a7de98 | -19.0926 | -48.3106 | 2026-08-09 02:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 140.6 |
| e8d909b0-0677-384b-adf8-1970e75ee6a7 | -6.8202 | -56.4353 | 2026-08-09 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 3bcd8b8a-0fa4-39e2-9576-496b24206631 | -19.1128 | -48.3063 | 2026-08-09 02:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 97b11085-7e33-38bb-bec8-b3ba29cbae54 | -6.8203 | -56.4155 | 2026-08-09 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 6fd535ea-8d7a-3e70-8923-19e7c563ec72 | -11.7908 | -51.8189 | 2026-08-09 02:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f076da51-252f-3ea8-bdbf-32ac5fa4bdef | -6.1476 | -57.7215 | 2026-08-09 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e278d28b-0814-3888-902d-90234a82161d | -19.0932 | -48.2876 | 2026-08-09 02:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 45.1 |
| b0176f84-bc70-3f18-87d4-dac0bd953855 | -6.8573 | -56.4137 | 2026-08-09 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d4a63e57-af0e-3bd4-bd69-55a8f750404e | -6.8388 | -56.4146 | 2026-08-09 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| ebbec01a-1bde-3cfe-80e0-36d44cc3b3e5 | -6.8387 | -56.4344 | 2026-08-09 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ec1ef141-403b-377f-9ce0-8c4a84fd5e27 | -13.9541 | -58.1162 | 2026-08-09 02:10:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 65dccde9-c5f4-3368-a092-9bba194c80b6 | -13.9733 | -58.1144 | 2026-08-09 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 2cb4343c-46dc-36fd-9e0f-5038fa4652a9 | -18.6327 | -49.8742 | 2026-08-09 02:20:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 9fe35ba9-b505-30ea-9bca-94004fc66ccc | -6.8573 | -56.4137 | 2026-08-09 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 3ee6f65d-9993-322a-b2d9-cb6cf174547b | -6.8388 | -56.4146 | 2026-08-09 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 7b6d94b0-f265-3a83-9b6f-732dfedf32a4 | -18.6533 | -49.8478 | 2026-08-09 02:20:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| 43c70520-7168-3b35-9537-e209c717e2cd | -6.8202 | -56.4353 | 2026-08-09 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 938d59d3-2d8d-39af-9b20-91ff1a2d13c7 | -18.6528 | -49.8703 | 2026-08-09 02:20:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.4 |
| dc0e03d3-eec9-3baa-a0ee-f5d66616a907 | -6.1476 | -57.7215 | 2026-08-09 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |


[Clique aqui para ver as próximas entradas](README5.md)

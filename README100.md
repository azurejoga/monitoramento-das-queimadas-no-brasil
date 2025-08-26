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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80306b1b-eecd-35db-99a9-feb8f7e92c29 | -11.53808 | -52.11543 | 2025-08-26 06:37:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1b5f0ac0-c392-3eb7-8f28-5317548e44c0 | -9.64392 | -59.63461 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4cbdfddc-1a3b-3039-bb0b-d2abbd807a88 | -7.29161 | -59.66211 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 485e1fe0-5978-302d-ad3d-7bfc82cbb998 | -9.57584 | -55.36937 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8a7b5069-5746-3fb4-bd0a-ad5b48abb21e | -7.38043 | -64.34532 | 2025-08-26 06:37:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 94f6412e-eaf0-3a36-a17a-5dd0ea83f495 | -9.17348 | -59.44796 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| ac2441d9-c886-3271-8b4a-cf9c100e2e02 | -6.77128 | -59.66354 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 40e18d0f-c136-3575-b0c0-e0745d0351b7 | -9.63337 | -59.64278 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3095816d-e127-39c5-ba08-bfef96aeb540 | -6.82374 | -58.975 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 96487ecb-d012-30aa-9a2f-4ce1f162082b | -6.23922 | -60.01719 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| a2aba399-7a8e-379b-9950-14e7f435d558 | -6.80854 | -58.95363 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b4440677-3947-320b-94b0-b30d1e4e6c9e | -9.58546 | -55.37073 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 643cf8ca-f670-36df-9a07-ea29f4e965dd | -6.8266 | -58.95634 | 2025-08-26 06:37:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 512331e0-3cf8-34c8-a09d-cab331054833 | -6.23127 | -60.00512 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e9f87a09-e5fb-3313-b032-593c9539358b | -9.65442 | -59.62667 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 59b3d899-09d5-34f2-920a-522cd549beed | -11.51057 | -52.12495 | 2025-08-26 06:37:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ca6260ac-7520-3032-b043-4ecd30ccf65a | -9.07957 | -65.70275 | 2025-08-26 06:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| f2571e17-5369-3b8c-91ec-9b13b2a78e78 | -8.98268 | -65.41621 | 2025-08-26 06:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 0bc85e7d-825f-38d7-b7cf-8c90c2f65ce9 | -8.86664 | -62.44028 | 2025-08-26 06:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| de94043a-21c8-32ec-81ef-5dd232e2c576 | -9.63485 | -59.63335 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 3e54c0bc-bb1a-39d3-b99e-335585f9fe10 | -6.24316 | -60.02344 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| b465c520-ee5a-33ef-81d4-b7797987a640 | -6.6757 | -58.85432 | 2025-08-26 06:37:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 962ecdc6-0873-3185-8250-e2ad6055b245 | -6.71146 | -58.55952 | 2025-08-26 06:37:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0c6f6512-7f13-3070-8b9a-9ed7cb34b3e1 | -8.99115 | -65.40079 | 2025-08-26 06:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| ef78d2dd-b660-3f38-9c31-458c06cde9be | -6.30586 | -59.87265 | 2025-08-26 06:37:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4da30a3e-c3ff-3769-8554-4894f263c8b4 | -9.1825 | -59.44936 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a1467bfc-2499-3e44-a084-029c68079f56 | -7.88522 | -63.01751 | 2025-08-26 06:37:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b2366d77-ab3b-3de4-8877-e2de1bd02520 | -11.5102 | -52.13198 | 2025-08-26 06:37:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1391a0f3-72ed-3b86-9079-163d39eab365 | -9.16302 | -59.45593 | 2025-08-26 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6e620975-bea7-3c1f-9f0e-a2f4d6dad308 | -11.1587 | -44.7627 | 2025-08-26 06:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 993607a9-b006-3fc1-b519-c7c9ffd964d9 | -9.153 | -59.5415 | 2025-08-26 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| b795be70-fb3b-392d-b806-a2d2b55d3696 | -6.2275 | -60.018 | 2025-08-26 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b7b93b2b-c7e3-30bb-a757-685953b331ae | -11.521 | -52.1209 | 2025-08-26 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 12f5435d-733f-3dbc-82c3-db08813f6b26 | -8.855 | -62.4313 | 2025-08-26 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 70ac5dad-4f5d-3634-b925-18bbf2ce2f96 | -9.1722 | -59.4629 | 2025-08-26 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 84affb1d-7b63-3a11-a598-b4b4d61f7b02 | -8.8548 | -62.4503 | 2025-08-26 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 0151098d-a55f-3a6b-93ab-c6b16191389e | -6.8228 | -58.9753 | 2025-08-26 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 991bb6f6-a2bc-36dd-8a0d-ba633531c8e8 | -11.1396 | -44.7654 | 2025-08-26 06:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 473983c7-778c-3948-aed3-b535726cedeb | -8.8364 | -62.4321 | 2025-08-26 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e0ab4a04-0176-367a-b78b-f1cbe83200c5 | -9.1717 | -59.5405 | 2025-08-26 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a60b9bf0-d2ed-3ee0-89a3-063aef100aab | -9.6366 | -59.6313 | 2025-08-26 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 34bb3a9a-7287-39f0-a777-d577b6ae157e | -8.8363 | -62.451 | 2025-08-26 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9f45f775-53be-3c4a-8fc9-0a5083c5f4c6 | -9.1903 | -59.5395 | 2025-08-26 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| f53427dc-abad-381c-b78f-371c297c88e9 | -11.54 | -52.119 | 2025-08-26 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 5be6f9c8-c9bb-3658-80cf-e2d246467053 | -9.1904 | -59.5201 | 2025-08-26 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 45c3c1db-7124-3a14-bcb4-7c085adbaca1 | -9.1718 | -59.5211 | 2025-08-26 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 313a79a3-803f-35f6-9a1c-dea6e1fbea5e | -6.8229 | -58.956 | 2025-08-26 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| cf7c07a3-b4af-3576-b38e-80a1c2cdeab5 | -6.2459 | -60.0174 | 2025-08-26 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 6ed4de9b-ffbe-37d1-9360-4b11fa966d52 | -9.1715 | -59.5599 | 2025-08-26 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 49c81676-d232-3b6a-8d82-0e306cd25423 | -11.5397 | -52.14 | 2025-08-26 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 6887632c-6076-36fa-98ff-5f27b5e68ce4 | -11.5207 | -52.142 | 2025-08-26 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 87b8e80a-6856-352a-8990-6daae84b7d62 | -14.75191 | -59.72282 | 2025-08-26 06:40:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa970a20-10b3-348f-9690-d3c55b85e0dd | -14.29306 | -60.36051 | 2025-08-26 06:40:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ed60a9d8-0b59-323f-85b0-a0190a0e8b9d | -9.6366 | -59.6313 | 2025-08-26 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 1302b771-23a9-3f0a-a614-be4ed72854ee | -11.5397 | -52.14 | 2025-08-26 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 0cc4153f-efb5-323f-85fe-59f43a2b013a | -11.54 | -52.119 | 2025-08-26 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 7eaa3a84-4e37-358f-83cf-4eb2bc58b7ad | -6.7635 | -59.6718 | 2025-08-26 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 46146896-3100-343e-8cf9-b0398ac51d3e | -6.8229 | -58.956 | 2025-08-26 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a9703091-288c-3a4c-a343-ede6c10650c8 | -9.1904 | -59.5201 | 2025-08-26 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 4d22d0e7-dde1-39fa-b7e7-179de36d0308 | -9.1529 | -59.5609 | 2025-08-26 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| ae42439a-347e-3147-b78f-159ac09b7dc3 | -9.1903 | -59.5395 | 2025-08-26 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e9a1e8c0-10ab-3d28-9276-d94c71a52781 | -8.8548 | -62.4503 | 2025-08-26 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 805d1200-662b-32ec-ad69-52685339a8ae | -9.1717 | -59.5405 | 2025-08-26 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| be860d65-6ee2-353b-8233-87729e510b71 | -6.7819 | -59.6711 | 2025-08-26 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| b0df6880-8b24-3976-8555-76104c33fe5e | -11.1587 | -44.7627 | 2025-08-26 06:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 06b6755a-285d-39d7-8e96-2a0cbd0c7a2a | -11.1396 | -44.7654 | 2025-08-26 06:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ef01ffba-25f2-3a37-ae38-da6a157bd72e | -8.9874 | -65.4192 | 2025-08-26 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| cc0da758-7ed2-3036-81ff-af433e33ebc1 | -11.521 | -52.1209 | 2025-08-26 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9ddfec82-12d1-35ca-8c2d-271e032eec9d | -6.8412 | -58.9746 | 2025-08-26 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ccd20fa1-1d32-330a-bb93-f1916a291a3d | -9.1722 | -59.4629 | 2025-08-26 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| bc688282-87a2-30d8-9c31-97370c69cc21 | -6.8228 | -58.9753 | 2025-08-26 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| f9d2dfdc-39d4-3236-a037-c57385e73ecf | -9.1718 | -59.5211 | 2025-08-26 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0d24478a-a39e-374a-b39e-95f4ce7d268d | -6.2459 | -60.0174 | 2025-08-26 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| cef2d453-59e4-393c-a60f-802df6cf6520 | -6.8413 | -58.9552 | 2025-08-26 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 75112151-9ed4-386e-a769-cac7e8bb4ca3 | -9.153 | -59.5415 | 2025-08-26 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 3bdb842e-2ae2-33fa-8d00-803a6defcc8a | -8.855 | -62.4313 | 2025-08-26 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f1b4f226-94a2-3bb9-8e2f-3ccb02665f05 | -8.8363 | -62.451 | 2025-08-26 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| d2dabc1b-e6ca-305a-ade2-2acbfd52da5e | -6.8229 | -58.956 | 2025-08-26 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 5abd6aa8-cf35-3c15-bad8-c87dd86117b5 | -9.1717 | -59.5405 | 2025-08-26 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 67614bac-855d-36f4-a618-5acd09bde142 | -8.9874 | -65.4192 | 2025-08-26 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ab028288-a7b9-3f98-9d1f-464332250397 | -11.1587 | -44.7627 | 2025-08-26 07:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 0a323858-4271-3722-b22e-859d24fe0717 | -8.8363 | -62.451 | 2025-08-26 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 31a8514c-7f60-3819-8449-c21afee98384 | -10.7597 | -47.0648 | 2025-08-26 07:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a3dfb693-00ad-3252-a22f-1162260050e7 | -10.1022 | -65.2874 | 2025-08-26 07:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| bc3c6ba6-42b9-3707-a913-fa1404003838 | -9.1722 | -59.4629 | 2025-08-26 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ba9ad69b-aecd-3e6c-a974-ad82b550e3ec | -8.855 | -62.4313 | 2025-08-26 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 15708632-7959-3202-9e90-0a7045b65471 | -8.8548 | -62.4503 | 2025-08-26 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.5 |
| cbed3b75-bcdd-3152-af6c-ff44a8563735 | -9.1718 | -59.5211 | 2025-08-26 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 321cd8b6-6bd9-349d-8843-06f480cf04e9 | -6.2459 | -60.0174 | 2025-08-26 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a69137f1-6162-3651-b9f0-2d7acdf37030 | -9.1904 | -59.5201 | 2025-08-26 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 2c5a8882-883d-3f3e-9a89-7ed061ed26a3 | -9.1903 | -59.5395 | 2025-08-26 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a033556b-994d-3d2c-9522-7bde8c5ea3c2 | -9.1529 | -59.5609 | 2025-08-26 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| cd9d91a8-3c95-3f7d-b146-a1bdf4f86123 | -6.8228 | -58.9753 | 2025-08-26 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| c977326c-6027-38a6-8143-1a79a1d78566 | -9.153 | -59.5415 | 2025-08-26 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6ea2b840-7d2a-3c10-8343-896a0e80647f | -6.7635 | -59.6718 | 2025-08-26 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 268fad1d-bff8-3f91-9f79-65807410cd87 | -10.1022 | -65.2874 | 2025-08-26 07:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 25d3d34c-1675-332f-b5f7-84ab81b9465b | -8.8548 | -62.4503 | 2025-08-26 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 108.2 |
| abb5feb3-55f0-3f77-8f86-d1993e2c30dd | -9.1722 | -59.4629 | 2025-08-26 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 89f9389b-8618-32db-8fa9-c4d1f06cda5b | -8.855 | -62.4313 | 2025-08-26 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8469ee82-8a52-325c-83d7-d2a4092eb727 | -9.1717 | -59.5405 | 2025-08-26 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |


[Clique aqui para ver as próximas entradas](README101.md)

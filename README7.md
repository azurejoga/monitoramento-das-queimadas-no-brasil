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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7751a96e-818e-35d4-8edd-f360ab917b8c | -10.9815 | -45.0874 | 2025-09-09 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 602.9 |
| 7738db49-88aa-3f2b-adfa-82fa542b2f96 | -22.2347 | -49.7256 | 2025-09-09 03:00:00 | GOES-19 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| af7f80ed-03ed-388b-84f4-2c3251cc1adf | -11.0006 | -45.0847 | 2025-09-09 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| ecd728c6-3c84-3066-8f28-54391f47086c | -11.9361 | -50.9765 | 2025-09-09 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| dab4e755-dc8c-321b-a449-ea12746b4018 | -18.8174 | -49.6816 | 2025-09-09 03:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 7179405a-8254-39be-9d57-900614cb37cb | -5.5703 | -45.0518 | 2025-09-09 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 688823f5-6bcc-3fcf-8a03-832ed1fe36eb | -11.3018 | -46.4792 | 2025-09-09 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 4641e811-6bbb-3441-ad96-716d0c360cba | -11.0003 | -45.1078 | 2025-09-09 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 9ce5e200-2a64-38b3-8224-a050033f03b2 | -18.8174 | -49.6816 | 2025-09-09 03:10:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 1f3ffc9c-cad5-3d7d-934f-827f95de28f2 | -12.1988 | -53.9024 | 2025-09-09 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e1ebad0e-63f5-3a9f-9d40-648a3dc9ca3d | -17.6847 | -52.2615 | 2025-09-09 03:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2af3612e-1957-3c22-855a-f23d7211acf1 | -12.1991 | -53.8817 | 2025-09-09 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 7978cf9c-c6be-3fd7-91fd-1f4fb646cf26 | -18.8168 | -49.7042 | 2025-09-09 03:10:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 69.2 |
| eb44f9da-7e2a-3523-ac0e-0bdf2c0badd7 | -10.0111 | -64.9151 | 2025-09-09 03:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 81a82406-6af1-38f6-9496-0b937b49998d | -18.8375 | -49.6777 | 2025-09-09 03:10:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 138.7 |
| 74bcd882-1653-3193-94b7-22019d95694a | -11.9361 | -50.9765 | 2025-09-09 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d0e41349-0f40-3eb7-b05f-1711da64ef03 | -9.9925 | -64.9158 | 2025-09-09 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 7b774c56-f906-3b4a-85fe-1c0cd6d54c56 | -18.8369 | -49.7003 | 2025-09-09 03:10:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d0db4c57-f2a3-3c1d-a6b1-f4409e7377e3 | -10.011 | -64.9339 | 2025-09-09 03:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5275e12f-2ddc-35c5-beb0-be1c4590dd50 | -11.3014 | -46.5018 | 2025-09-09 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 0c4cd6a6-fbc0-3d33-8c11-8b7a217ea387 | -11.9551 | -50.9743 | 2025-09-09 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a7d3fcf2-1445-3a65-bfb5-0c0dab9909ef | -10.9624 | -45.09 | 2025-09-09 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 81b8a5b5-0370-3066-8926-eb259cbf7647 | -12.1991 | -53.8817 | 2025-09-09 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 1ec835b7-176f-340c-914d-ef85b03f4d6c | -17.6847 | -52.2615 | 2025-09-09 03:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a635681f-fd8d-390a-95b7-290916cf9e20 | -10.011 | -64.9339 | 2025-09-09 03:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0967edb8-6356-38e5-a2f5-df776e80587c | -10.962 | -45.113 | 2025-09-09 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 209bcf79-8bd7-3b9a-b2dd-0111d5c0587e | -21.4555 | -48.8455 | 2025-09-09 03:20:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 78.9 |
| dd32b6bf-f7d0-3773-87ac-c0e630113da2 | -17.6852 | -52.2398 | 2025-09-09 03:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 87e0a977-420f-3994-9fb0-45bd708522ed | -18.8369 | -49.7003 | 2025-09-09 03:20:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c387d895-79eb-38fa-b95f-ff2031263463 | -17.2762 | -46.7305 | 2025-09-09 03:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 48a04100-e222-3fe8-aadd-dd60c44e1697 | -18.8375 | -49.6777 | 2025-09-09 03:20:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 146.3 |
| 2a56391f-42e8-33d3-b624-13942a660539 | -21.4562 | -48.8222 | 2025-09-09 03:20:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 0ac4aaad-1ced-3df2-97f3-1defed6170ca | -10.9815 | -45.0874 | 2025-09-09 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 474.4 |
| 0716a186-0e65-3dad-aca2-f96c6c593761 | -12.1988 | -53.9024 | 2025-09-09 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 985eeff4-fdef-35c3-bb62-4ac1dfb5dcf3 | -18.0418 | -47.1277 | 2025-09-09 03:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 427bff2a-5232-3b35-9155-4e26cb09d227 | -11.0003 | -45.1078 | 2025-09-09 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 64df4ddd-9af4-3b20-8544-b9e49feb72eb | -21.4355 | -48.827 | 2025-09-09 03:20:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7f702021-96f0-3d4a-8c15-3594b19e6c2e | -17.2757 | -46.7538 | 2025-09-09 03:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 62.2 |
| c6c9be82-494b-3f2d-bbdd-d438372bf572 | -11.9551 | -50.9743 | 2025-09-09 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e729f475-c8c2-3fb6-8621-5c468c475204 | -10.9811 | -45.1104 | 2025-09-09 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 661.1 |
| 4c12c9fd-6d57-3c8f-8fba-9c2d31387a17 | -21.4348 | -48.8503 | 2025-09-09 03:20:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 26bf7c7d-7370-30de-b884-2575fec8f572 | -11.0006 | -45.0847 | 2025-09-09 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9d285f0f-8451-3637-bf30-4248337fd895 | -18.8174 | -49.6816 | 2025-09-09 03:20:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 133.7 |
| e62811ba-28c0-3c24-b80e-1af1d796801b | -10.0111 | -64.9151 | 2025-09-09 03:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 3cfa1002-d5c1-3143-b55b-7cb6420ae9b9 | -21.4562 | -48.8222 | 2025-09-09 03:30:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 07dd3dce-2013-33c2-9904-78c78715320a | -21.4355 | -48.827 | 2025-09-09 03:30:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 37d7862d-7c36-3097-8645-7ef7f1fa76bc | -17.2757 | -46.7538 | 2025-09-09 03:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 54.2 |
| aa98655e-61d1-3303-9e8e-42b6761df121 | -21.4348 | -48.8503 | 2025-09-09 03:30:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ed60a37d-0893-321b-b678-70ffa4a43a8f | -12.1988 | -53.9024 | 2025-09-09 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 7de17b5b-9464-3ac1-852a-232bdadba677 | -11.9551 | -50.9743 | 2025-09-09 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 8f954efa-a9f7-33cb-83c5-c1d42ec40402 | -10.011 | -64.9339 | 2025-09-09 03:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 74a369b5-b0e4-3703-bb1c-223e9f7416c6 | -10.0111 | -64.9151 | 2025-09-09 03:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| dfb55272-4cb9-3d8a-b5d5-f5d580e68d50 | -18.8174 | -49.6816 | 2025-09-09 03:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 22f84e05-d5a3-3d7d-ba00-c27f8a91b5e6 | -21.4555 | -48.8455 | 2025-09-09 03:30:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 157.1 |
| ef91ac6d-cdcd-3549-b1f9-4775bfcefeb0 | -12.1991 | -53.8817 | 2025-09-09 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2c787db3-c863-3cae-af0c-cf9d1845b973 | -18.8375 | -49.6777 | 2025-09-09 03:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.4 |
| 11b5e0f9-9790-3d87-b743-1b33b51dde10 | -12.1991 | -53.8817 | 2025-09-09 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 77ccfb9c-228c-3339-8980-8dc68c52ca40 | -21.4562 | -48.8222 | 2025-09-09 03:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 7e30abe0-e2d4-3a1e-8b02-8fe587602f62 | -21.4555 | -48.8455 | 2025-09-09 03:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 146.8 |
| c08f7193-2264-39a4-a908-cfe8669e258e | -21.4348 | -48.8503 | 2025-09-09 03:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 269be17f-23df-38cb-8ff6-4aca71213376 | -18.8174 | -49.6816 | 2025-09-09 03:40:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 170b48db-7b4b-37a1-b371-574f81d48bd5 | -12.2178 | -53.9005 | 2025-09-09 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a9e6cf64-1e43-3f18-a788-95394be44a57 | -12.1988 | -53.9024 | 2025-09-09 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 2277b1fb-b5af-3c50-ab58-8aeae0c1e8a7 | -10.0111 | -64.9151 | 2025-09-09 03:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 83a8671c-681d-3b8a-9da5-daf099385f38 | -10.011 | -64.9339 | 2025-09-09 03:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2aafd015-f4db-3e49-acdf-ae22c8e48f6e | -18.8375 | -49.6777 | 2025-09-09 03:40:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| 25f36b23-6ecb-3d94-a792-5cf6a613ada2 | -21.4355 | -48.827 | 2025-09-09 03:40:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 74.6 |
| eb430785-ea18-3a07-9aef-9ba7f8c56028 | -5.26603 | -44.44751 | 2025-09-09 03:40:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6a95ebc-2d10-3d9f-8b76-2310403e6f29 | -4.78777 | -37.73301 | 2025-09-09 03:40:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fe97a239-159a-38b9-a5b6-321f8d7e8ec7 | -5.42693 | -42.81124 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c7923e8-6027-3a4d-b38e-8b7e73c497d2 | -5.49538 | -42.99541 | 2025-09-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 329ed1fc-481a-36eb-8af3-fa58e3710449 | -5.79757 | -35.53213 | 2025-09-09 03:40:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f6aa5139-b2cd-3400-98ee-24ece5dd5351 | -4.26785 | -48.19452 | 2025-09-09 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 859809a4-2edb-322a-8c7a-1610ee08dee8 | -5.26492 | -44.44958 | 2025-09-09 03:40:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 16d72061-62d6-389d-8235-e24d7058a94a | -5.45556 | -42.80691 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| ead594f8-7b70-3fbf-a1d0-c8ae2e9fee8c | -5.4336 | -42.8013 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 596c9869-eb2b-31ed-9489-75751a9e7bea | -5.1637 | -42.94307 | 2025-09-09 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4494395-c7ad-389e-8fcd-08deec444c80 | -4.85475 | -44.36825 | 2025-09-09 03:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 091a019e-bea7-3ff1-881a-281a432d4b4d | -2.62855 | -46.8475 | 2025-09-09 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 801d9df5-aca8-30c4-b70d-54cac62e80c9 | -5.48921 | -42.66962 | 2025-09-09 03:40:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a221e993-86d1-3013-a4d0-60277c3682ea | -5.43936 | -42.79674 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a33d3023-3057-3e1c-9897-dfa3fbbda1bb | -5.54011 | -42.66183 | 2025-09-09 03:40:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 009640a5-834c-38a1-b423-244455529d73 | -3.94491 | -41.83091 | 2025-09-09 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a87be7d8-79e8-335a-bdd7-f579267be903 | -3.47105 | -41.54059 | 2025-09-09 03:40:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 86fb9792-c16a-3159-9f21-29cfa982aa56 | -5.84443 | -37.49324 | 2025-09-09 03:40:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ccf443a3-7e7e-304b-a1fc-ef727a29452f | -6.05173 | -39.43824 | 2025-09-09 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f3d8922-00d9-3659-83c3-d50967680772 | -5.08402 | -42.42456 | 2025-09-09 03:40:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b1a1ecf5-c7d0-35b2-8cf0-31bc13912906 | -5.26431 | -44.4532 | 2025-09-09 03:40:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 909f7f76-aabb-3f9e-be24-3d837f720af4 | -5.16277 | -42.94859 | 2025-09-09 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1dca777f-b935-3189-b837-c1912fb7cd8e | -4.55749 | -40.34263 | 2025-09-09 03:40:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 398a6e62-6b01-3d8f-afd5-d4cf1a1f56fb | -5.45161 | -42.80075 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| db0f64d7-d27b-397c-ba43-c07b2d14aec8 | -4.17278 | -42.03201 | 2025-09-09 03:40:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3a972511-c805-3a8f-8373-61510a99b032 | -5.4147 | -42.85434 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 25740723-75cb-3e13-8f7f-4cdd42f19891 | -5.57656 | -42.90639 | 2025-09-09 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 2fe6a313-89d2-3585-a578-feef2a4f170f | -4.88987 | -42.21035 | 2025-09-09 03:40:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 03664d5d-4287-3ae8-b24f-4db01a20a3bd | -3.76159 | -41.66006 | 2025-09-09 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d77c099c-3eaf-34cb-afa9-af8011d0492c | -5.2654 | -44.45111 | 2025-09-09 03:40:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4eef20f-1474-3fc7-a619-3b3717489ada | -4.60726 | -46.59616 | 2025-09-09 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 705720eb-bcb9-339e-b600-3227088dc318 | -5.4128 | -42.85057 | 2025-09-09 03:40:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 127df2f0-ce05-34fb-a6e6-123c342e9b67 | -5.26119 | -44.44311 | 2025-09-09 03:40:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README8.md)

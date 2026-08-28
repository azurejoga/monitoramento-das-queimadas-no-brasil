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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9b4df35-7ccd-34bb-8f32-6d53c2c1df40 | -10.63695 | -70.08253 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2b7f4601-c12d-346e-8f56-dd11c8276f05 | -9.16008 | -49.97655 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| fc0a6b9a-4cf7-3bb5-a745-efe90cc1d9a9 | -10.05563 | -68.83646 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2278cfe8-fbee-345f-a112-dc0cf4addc2c | -14.43103 | -52.60481 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5231d77d-85c7-3c96-84c2-dfbb59450894 | -14.71914 | -58.72612 | 2026-08-28 17:45:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e0ef54d1-16b8-3c4f-8b4d-17ee25a27e27 | -8.19242 | -54.95717 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 78e3fcd2-dda7-31c2-833e-f6833cd0f94a | -11.27946 | -54.0364 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| c640a1e3-b4a0-3bcd-993f-44817c8370a6 | -9.01489 | -57.54264 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b68bac5a-d832-3e99-94c4-237101c037d4 | -9.92011 | -60.4339 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 8c5bd642-2865-3797-a704-a0861900f4a0 | -10.49506 | -64.49026 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| d3b81123-03d9-317a-b061-3f2e8498b51a | -14.65129 | -57.00352 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e56ca0be-bbf7-3de5-8793-04bbad805cec | -11.72024 | -54.54221 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4c124b36-7509-3881-a2cd-d992686e4ace | -14.47012 | -58.51812 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6fe04a07-57de-3e9b-8dd5-31c32003a692 | -14.64653 | -57.00694 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 33057cc9-fa69-36f2-9907-c5bab111b91b | -11.20927 | -53.9897 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 41820f8c-86fb-3173-a54a-a7675b8e0b3f | -9.89364 | -67.01631 | 2026-08-28 17:45:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5eb1170f-f86a-3256-8250-e05653208a3e | -10.99709 | -49.63866 | 2026-08-28 17:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 686071e5-8052-34ad-a2ac-e30147725030 | -11.02682 | -49.65075 | 2026-08-28 17:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c53707f6-d4df-394a-8956-45d98b7fe8e4 | -9.19393 | -59.56477 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c85dc029-b663-38a0-9c09-74813763ff38 | -9.28136 | -57.06964 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 0d246b6f-9b7e-34b7-a689-a92a3e5e8fb9 | -10.58392 | -63.56113 | 2026-08-28 17:45:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 91690c5a-7159-3c26-9664-95754a7e71eb | -10.83154 | -50.51201 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0f82ed57-83c5-3d40-a34c-11dacafbfe05 | -14.6487 | -56.99633 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a38ef37b-06ba-30a8-962c-6fd942b9b46a | -14.88044 | -52.62915 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 43cf0534-90af-3e69-8dc5-bfc78e1a1dcb | -11.00599 | -49.64886 | 2026-08-28 17:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1e98941f-7e19-3bac-9f34-27df87531b54 | -11.27844 | -54.03074 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c67bb67a-5484-39b0-9fa5-62cae3849a3c | -14.87245 | -52.61534 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6fc161a8-a0c3-3945-bd2d-6075dd496735 | -9.41813 | -50.43777 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f6483efc-5e61-3e56-b1f3-2ddea3b39af1 | -9.93107 | -60.43602 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 336.0 |
| 6a3a496f-3879-33d8-ac70-ce2455ea7356 | -9.46397 | -60.55864 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e7afcbb-6312-36e1-a60e-1856ee48ac2f | -10.50473 | -64.50811 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e2e9c47d-cab5-39a2-ada9-27b209892bb5 | -10.39954 | -61.20362 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c4e808b7-96bf-369c-a5f1-eca8d36347ea | -13.6434 | -51.70388 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ff73631a-ce3d-37be-a877-e8adb11b6d1d | -14.88557 | -52.62833 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 33abdceb-5640-3cb5-9549-024eb5a7ba0e | -9.15779 | -49.96484 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| f2225bed-f54f-3c6c-9158-cb2666bf5c25 | -14.64655 | -56.99926 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 20844f1e-6716-3153-b5bd-b6141124fc5e | -14.45516 | -53.44777 | 2026-08-28 17:45:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 94aad3cc-df3e-31cb-8151-abdc744abe33 | -9.01835 | -57.53833 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d757238-83fe-3e95-88b2-543ec5b79c48 | -14.43243 | -52.5846 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44beee51-d25f-39a6-aad4-997be425772c | -8.23542 | -54.96071 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 55e29201-9bb9-39cb-889e-6a39d5c859c0 | -8.60259 | -54.82935 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d6f910cd-41b6-34c7-8a85-cd4f89df29ca | -14.15575 | -52.83537 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f70d890-3fa5-36c4-9f72-a892a811047c | -10.51805 | -59.62604 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f40618ab-e538-3bc2-bdfc-25a5e68e0349 | -14.92573 | -56.3174 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6c04c4e5-0edb-3fac-ad6f-fc6f1600cb82 | -14.4706 | -58.51279 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 159f43ab-a5d4-327a-9d48-41b2d78d125b | -12.90986 | -59.87997 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e986a63f-7e63-37c6-9ac0-76c9f067315f | -14.91436 | -56.32327 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1134726-4655-3f4a-8e00-7ded5fa0aa1e | -9.87081 | -60.26031 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e02dd96-deb3-38e8-917a-8708ec023627 | -10.48708 | -64.48373 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |
| e1eb4a75-7be8-3e62-b684-7e41bde68748 | -9.00735 | -57.54763 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2cc7cda8-6f92-319d-b4d1-11f0fde99231 | -14.17103 | -52.83242 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f425b0a7-6b6e-36d3-a172-20b857973f82 | -14.65041 | -56.99857 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| d09a07d6-ee13-399e-98fe-f5b9e18bb9ff | -11.22919 | -53.98608 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| f354a67d-949e-39ab-af3f-e80714c2ae65 | -12.9242 | -59.88153 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 46b4dbd9-21d1-3074-a0d9-794477d07329 | -13.47257 | -57.04035 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 33630763-39a1-313f-b6d5-4552588ce4a4 | -14.9236 | -52.60616 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 325f4017-fd1e-33bd-91e1-2f7b7fc5a7b0 | -14.43555 | -52.60063 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ffd2596-67b0-36fe-b44e-2f7487d0275c | -9.69638 | -65.09863 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 764ed485-9d41-3ea3-b640-67e34e107482 | -9.46112 | -60.563 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| baa6534d-20bf-3f12-98f6-a9ca11b82b8b | -13.1082 | -50.04345 | 2026-08-28 17:45:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 984b92e4-e2ab-3a33-8e26-bc213fa086c2 | -14.64269 | -56.99996 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 78e03c26-d6d3-30c8-ae4a-5ba6ba02ba58 | -9.85922 | -65.02274 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 562b8a83-da79-30a5-9363-b5fa17b37a0e | -14.91709 | -56.31534 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 621bf3be-a341-34a7-8420-0dd1efdc44c8 | -15.56941 | -56.29004 | 2026-08-28 17:45:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4aeaad40-f8c7-3272-a5b2-b06c0625b48b | -14.2052 | -51.80794 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4565a79d-0adc-39fc-8c04-5d7c2f7714ff | -9.22297 | -59.76954 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 4369540f-992c-3f08-bdf0-08ea25665f2d | -15.57642 | -56.28323 | 2026-08-28 17:45:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| ba07423d-32f8-3256-837a-48405b19411c | -14.64743 | -57.00421 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a5407b95-70e9-381f-80ef-8aa9339aac06 | -9.19283 | -61.08584 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a00af5b3-5f14-3d11-a424-6ee7a52e1dd0 | -9.17833 | -59.60608 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 4a4bc151-7211-3fc1-9ef6-0b0bfd61e6f6 | -9.1743 | -59.39445 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 10012bb9-dce3-3fd0-a6a1-cd9c7f11b4e0 | -9.89174 | -67.01381 | 2026-08-28 17:45:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5845e950-6b6e-399f-a998-d711d418d1f4 | -10.3193 | -68.45642 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 26.4 |
| b9da7455-07c5-35fb-b93b-40ddccfee377 | -11.20077 | -55.10017 | 2026-08-28 17:45:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 46205d07-a62b-3cff-b53d-93b7c611eb4f | -14.46654 | -58.51872 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 385405ff-7e8a-3d88-bb00-1c56d5791f0d | -10.63759 | -70.08459 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4102382a-f04d-3326-b4c7-d11053bfc527 | -8.11858 | -51.65987 | 2026-08-28 17:45:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0b04042e-7ba2-31a3-946f-47441b2b5370 | -9.41621 | -50.43068 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 7891ad0f-b06f-30de-b57d-f73ef8ebfd78 | -9.97062 | -53.93221 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 96257fd4-8648-3fa0-88da-df6fe1d77722 | -10.51384 | -59.62251 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c0f20ab4-df7f-3e1e-93aa-1e03d609962f | -12.25879 | -59.34783 | 2026-08-28 17:45:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5513776f-105a-3c42-9e71-edb87a84b905 | -9.16933 | -59.57325 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0957ff08-1c4f-3867-b9e8-14e6a1d150a9 | -12.38523 | -48.19002 | 2026-08-28 17:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 39517219-49f4-3a48-8c0b-90f4a49642cd | -14.92046 | -56.31099 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 2f5784ff-66d5-30c4-bdcf-d371cd4940f0 | -13.41017 | -51.7644 | 2026-08-28 17:45:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1addebc3-9c21-3513-93b9-1d0164a7c200 | -9.16573 | -59.57389 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 24e0c2be-edf0-3372-8417-f9ee43d88fd6 | -11.00487 | -49.63431 | 2026-08-28 17:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 12faf596-1064-311f-ba46-77347b7237cf | -8.59918 | -54.77379 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6ef93124-afeb-324d-8c54-070d55253904 | -11.21865 | -55.06679 | 2026-08-28 17:45:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0703d2e2-6d91-35f6-a3da-d65117a16ceb | -10.31503 | -68.45703 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 7af8f3ae-5fa9-3a65-89ea-a933012010d3 | -9.09736 | -59.4059 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c682894b-f04a-3916-9b0a-e9d4b5932939 | -8.78383 | -50.06894 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f3ea228a-4ebc-3da5-99c1-efc1786704e3 | -10.76273 | -53.97453 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e66f5f60-a2e5-3bad-b5cb-12649af83aaf | -14.23798 | -51.76969 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 45f03caa-0c28-31e7-a7a3-fac38a7bf803 | -15.24024 | -53.86111 | 2026-08-28 17:45:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d0058968-a4c7-3a42-9019-0500ef9b7109 | -14.65341 | -57.00059 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 482bbb1f-a07a-30fc-9505-e8d912823539 | -14.92173 | -56.31816 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9a386f1f-bb73-3b90-8c3d-390969ed6466 | -9.01428 | -57.53906 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 32ab4562-ac87-3179-8b29-aefba372abaa | -13.46473 | -57.04178 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d0b618e1-de42-3280-97e6-3c2636efc9a0 | -10.66725 | -63.4852 | 2026-08-28 17:45:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 34.6 |


[Clique aqui para ver as próximas entradas](README139.md)

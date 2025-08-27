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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f37b8f5-f496-3e43-9a0a-c9fdd78179d2 | -11.14234 | -46.33766 | 2025-08-27 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 575fbc1b-a0da-3a39-b0e1-a8d5f8ed6a9e | -11.81715 | -46.80903 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b05fab0c-98ba-3987-951c-099c2d32992d | -8.92217 | -65.92741 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7aacb6ca-0a51-3282-8bb1-018e55b35665 | -10.01047 | -65.03126 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60dfc9ce-1e33-31a3-aea4-ab7734cadf21 | -9.15815 | -59.54147 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c36172e-6728-39c3-ac6c-05d0c959649d | -9.27633 | -56.90374 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 544f0615-8f16-3cfa-9bc8-db6b7b391e11 | -8.96414 | -65.96934 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1c2598f-4514-3c08-8c11-8fdfc5db6315 | -8.1101 | -47.30738 | 2025-08-27 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a8cdc12-c220-38a7-96e7-ba6c026943ec | -9.40747 | -60.53244 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 269c162d-5233-3809-a788-cc78ebe2e3f2 | -9.15544 | -59.55886 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6c81a0d-311e-33c1-8b8a-7919fefbd092 | -5.43485 | -60.17962 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1310279-eead-3f14-b0c9-2e2d76f48ac7 | -10.48916 | -51.60637 | 2025-08-27 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5db77526-b7cd-34de-984c-7a1219c7bbe3 | -9.25278 | -65.62638 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6412340-f7c6-327d-a30f-8db34adf113b | -8.90181 | -60.78019 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b6fb9a2-0dc0-33b3-903c-f9cee0f43d08 | -9.5946 | -55.36967 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9df2fc9-00a6-37b9-8dd5-a15c7e59267f | -10.59941 | -54.89832 | 2025-08-27 05:18:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27069eeb-6a57-3e2d-b690-df5303dbdff8 | -5.30468 | -60.20609 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20cfa891-7759-371a-bb92-77a384729b82 | -6.83084 | -58.95951 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da44cf1b-02e9-3beb-83bb-25171a9d46c0 | -6.63071 | -60.01826 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7f1440f-a414-3f58-ace0-4675e1bf2589 | -9.44889 | -65.42212 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47a93660-cbc4-3a47-9247-5c9c6b304792 | -8.88028 | -62.45977 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26e3badd-35a5-3a21-b464-ccf368fa967c | -9.34478 | -59.63199 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1532391-e0c9-3e40-8011-21e674dc77b9 | -9.23614 | -60.92553 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bfddf30-337c-331f-9a0e-7362939732f7 | -6.62376 | -53.32473 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7153aa81-2955-31ad-b593-50659a2fc91b | -8.96267 | -65.95172 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e3e1d72a-c7a5-3313-9e13-15591e926f44 | -7.3671 | -70.14906 | 2025-08-27 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43558a5a-a8ce-304e-bf37-2276736c16a3 | -10.40605 | -57.69731 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 569477f5-afb1-3aae-8f0d-5b3d6884c49f | -10.77562 | -60.78692 | 2025-08-27 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b17afef-16a9-3a8c-a056-4f569de917fa | -12.79615 | -48.11983 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d2374270-4c06-360d-b2af-62ec8799d87d | -9.17469 | -59.45918 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3372bc48-8044-3ee7-b595-04992cff4807 | -9.13456 | -65.27854 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66c124a8-47bc-33cf-b776-bea131c1efc4 | -7.54124 | -63.84283 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 962ee930-585d-3b46-b8ff-0cf07ec0033f | -7.53529 | -50.53517 | 2025-08-27 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b06284a9-5b59-36bc-b66a-97c6a8c86f74 | -9.42021 | -60.51647 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a538d114-d7cc-3df1-9238-82de86c17052 | -9.64794 | -64.99358 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 071c7821-062c-3cdf-8f14-e72f5788db7b | -9.41799 | -60.53052 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f32b73d-9dd8-3d62-95b4-efbcffa13ad4 | -6.70377 | -58.55273 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34d7511e-17c7-3413-a785-ce297291db7d | -7.35715 | -57.62193 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8839bd71-543d-3592-a0ba-a7c6a4bdf917 | -5.72917 | -59.88922 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c0548a5-c3ca-38df-a073-c0e6e685c83c | -9.65485 | -59.6281 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d133589-ad53-386d-9a32-ada14330f8bb | -10.76842 | -60.78938 | 2025-08-27 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58deeb31-ca5b-30d2-89ca-e0c2b503879d | -8.90811 | -60.71928 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd99a55c-a9f6-3987-9a94-6cec1ee71395 | -8.92866 | -65.94155 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05b36bae-157a-3a74-9aa7-fd473f25090e | -9.81221 | -64.29255 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62814cce-ebb1-375c-af64-407f71c8a48a | -9.5683 | -55.37913 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48551ba0-3ef4-3c73-b163-c7917e41ca55 | -7.43078 | -60.61723 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd4f5a8a-91e7-3e93-8c13-7abb2b5c6be7 | -9.40526 | -60.52489 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 209b728d-3c51-3c1d-b410-3e9a47b604c7 | -9.52355 | -60.52948 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01b36990-19d5-3140-9707-1e5f6da46cd8 | -9.41356 | -60.53702 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b495ee95-62e5-3c45-a516-ba59b6e4166f | -8.12628 | -55.55492 | 2025-08-27 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bca03903-c54f-3a34-8902-a57e83c08020 | -6.83691 | -58.964 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c58f3cbe-a12e-3d94-8c89-217934aff028 | -6.83745 | -58.96054 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5120643-4d15-3d39-8861-b6cd92d8b236 | -8.8952 | -60.75725 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e0174e0-8caf-3a63-befc-8faafcaffddc | -9.07137 | -66.0605 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52972141-2402-39d2-9236-07458cc18db1 | -5.61154 | -60.24373 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e69d4863-e75a-3adf-9f10-91bcdecc2b7a | -7.43925 | -60.02576 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 950c68a5-52f1-3360-b4cf-fcae42c58a60 | -12.87694 | -48.10187 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92b1d2de-b08b-3a24-ac5d-f32abcd55fec | -10.61219 | -54.89923 | 2025-08-27 05:18:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62c17661-ea70-3f92-bcd1-44337cc27bca | -9.80942 | -64.24994 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26892cf4-d03d-3f52-bc8b-287bd3876ac5 | -8.99409 | -65.41245 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d2574a7-0a7e-3613-9c51-ce6eb34332c3 | -8.95085 | -64.1326 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80809c9f-8d7c-3fe1-bf67-df36feb1dcb9 | -9.08637 | -65.734 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec122b2f-1c8b-31a0-ba4b-c0ce86bf841b | -6.70324 | -58.5562 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8405d6e8-2c69-3afb-975c-8247cd88d5f4 | -9.40359 | -60.53543 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e975169d-733d-3ef3-8a1c-773a3a705d40 | -8.91424 | -65.92168 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31478297-3422-3714-a88d-ecae9e5bb29e | -8.94965 | -65.94942 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9bdcdabb-984d-3378-9f41-c8da80c3867f | -9.19915 | -59.54143 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 374f8c20-3f6d-3e72-a213-d7c3341fd87c | -5.3553 | -60.39839 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f06e8594-93fa-3772-b012-75bc7f6706b5 | -9.22976 | -59.67095 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4dba5ae-e060-385f-848d-8ab979a4dc1a | -8.49974 | -69.80087 | 2025-08-27 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3045e6f4-7135-35ed-a616-a7e5869899de | -9.41191 | -60.50435 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00b7f631-624c-3d88-8509-39769396bde0 | -9.01911 | -65.69785 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a1f6cee-0069-3535-aa59-02d560173c7c | -7.42743 | -60.6167 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c986dfdd-00b4-3099-bd5f-6bbb7587f781 | -8.93808 | -65.93877 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 13f390e2-5567-3f8f-9ca7-4aa8ce6d81c3 | -8.94169 | -65.94375 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e22b0aba-d358-3a66-aec6-d457466d7c44 | -9.17224 | -59.45105 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adddca0a-7b38-3bc3-a0c2-3bbbc68fa13e | -10.09282 | -62.90052 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a062d2e3-fe5d-34aa-986a-7760498fcb60 | -5.80838 | -59.21151 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b7ce76d-a655-36a7-8b2e-3b01385af011 | -6.25419 | -60.0123 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0931e529-9d6e-363c-a555-eae2f48c24ae | -9.418 | -60.50892 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71304967-360e-3f36-81c1-d452220bdcf4 | -11.14154 | -46.3447 | 2025-08-27 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5bbdc0f6-0e39-30f7-953c-6dc46810574c | -9.64054 | -59.63298 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f27f1108-8e23-3857-9c96-69d1739e345e | -9.18696 | -60.80443 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f2305a6e-320d-385c-a2d2-75da09c1a49c | -8.84692 | -62.44195 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd4e1b16-5cbc-3f76-9f49-be9a508d9420 | -6.61992 | -53.32567 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3572b37a-98a9-378e-b0ef-faa7f26fdf69 | -7.48231 | -61.35102 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15e59174-2104-3d09-9a23-6e660f84607c | -9.28519 | -56.91753 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a3deb82-3c2d-31ff-bb3d-b2f60a3598e7 | -8.72915 | -49.74134 | 2025-08-27 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6b689a8-9e1f-3e3b-bc9d-89036ec3e24f | -6.7697 | -59.67668 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 648b8748-88b9-3190-9bc3-1289b646db42 | -5.79847 | -59.20996 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14c82feb-9db4-3eba-8421-7daf95fe3973 | -9.18118 | -60.86184 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb95f11-f6c1-303e-97de-670a61baed49 | -8.34458 | -62.93607 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82182e44-75a0-32fa-8627-afc17414dd90 | -8.67 | -66.58777 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48bb43d9-2e3e-3047-8ad8-f86ae4e4e08a | -7.48033 | -60.66547 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf256363-63cb-30d6-ac21-71d9813009ce | -8.96195 | -65.95595 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bb2c9014-037a-3b1a-ae5a-5a2366cb9516 | -9.58864 | -55.38388 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb9a163c-7c57-3e97-9523-558289d04f50 | -5.80784 | -59.21496 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfe52b84-ed8e-3004-b0ca-81c001e2df29 | -9.0254 | -65.68662 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d76ad80f-da61-36ea-a2a1-c29bde0c7ca8 | -8.10541 | -71.24803 | 2025-08-27 05:18:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5036cfe8-71d9-3c35-b805-8df293a62fb2 | -9.15381 | -59.56929 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README61.md)

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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 970b97bd-61c1-3f6f-8b2b-e6401fc15c82 | -13.4225 | -46.8957 | 2025-08-25 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 928be75d-d870-3b25-9d1b-7afc999f3007 | -6.782 | -59.6519 | 2025-08-25 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 27fb8738-287b-324a-895c-61db09089342 | -8.8734 | -62.4495 | 2025-08-25 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 8390da50-0ac2-3a81-b0de-09d77da39467 | -13.4132 | -51.7784 | 2025-08-25 06:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| d3ae1c23-fde2-38c9-a373-76bd5a5cab66 | -8.9874 | -65.4192 | 2025-08-25 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 411d9dd5-4a24-38f9-a3e8-00c2620852f8 | -8.4951 | -63.8805 | 2025-08-25 06:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 939f7046-c1f9-3f8b-b236-41ecf2dcf53e | -13.4419 | -46.8927 | 2025-08-25 06:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 032f3878-8018-3d06-ab63-a1ac690381b2 | -9.006 | -65.4 | 2025-08-25 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 38374622-d09a-3cfb-aef9-dcfda3046575 | -8.9875 | -65.4006 | 2025-08-25 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fc46a8ff-3781-3304-8069-0389ba009bc6 | -8.5136 | -63.8799 | 2025-08-25 06:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d210110b-ca31-3d07-b271-8322fe37254b | -8.8735 | -62.4305 | 2025-08-25 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 850861eb-f33c-3f65-bb63-e6fb66dfc232 | -8.8734 | -62.4495 | 2025-08-25 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c84f2d61-6d7a-3348-b13c-b6372c626b56 | -8.8733 | -62.4685 | 2025-08-25 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 7bef946b-269d-3d27-89c5-1e718fd262c5 | -8.8735 | -62.4305 | 2025-08-25 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 128.3 |
| e80bbab0-2c7e-3db5-98a6-baeec5a21c94 | -8.8919 | -62.4487 | 2025-08-25 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ef52e160-f48e-3ba7-bbd9-0f553a7de09b | -9.1722 | -59.4629 | 2025-08-25 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 1c1348b7-2922-3536-99f5-af916f97d164 | -8.855 | -62.4313 | 2025-08-25 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.6 |
| a8364b4a-5f8c-3253-bbc9-f50bd9855e9f | -9.006 | -65.4 | 2025-08-25 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9f20051b-06a3-3cf3-a924-6698b5b45cf3 | -8.9874 | -65.4192 | 2025-08-25 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 197fac65-b20a-3a83-87c4-574b88d888c7 | -8.4951 | -63.8805 | 2025-08-25 07:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 349557e5-bda5-392f-ba51-6248b87780d3 | -8.9689 | -65.4198 | 2025-08-25 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 465cd66b-f9f6-38a6-be3d-185e69b8341f | -13.4419 | -46.8927 | 2025-08-25 07:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| abb8281b-5034-3a20-828d-f2ffdd09ddd4 | -8.8921 | -62.4297 | 2025-08-25 07:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 463d48cc-c2d4-3604-b1c0-faf64e629724 | -8.9875 | -65.4006 | 2025-08-25 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 462c195e-f76f-3ebb-ae0d-d68862aacaf4 | -6.782 | -59.6519 | 2025-08-25 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 594773be-fab3-3683-ae59-e37e85c820a1 | -6.7819 | -59.6711 | 2025-08-25 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| c6d259cb-980f-338b-840a-558a1e95a1cd | -6.2643 | -60.0167 | 2025-08-25 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5b29812d-5237-3b7d-af4f-dd069dc37d6b | -8.8735 | -62.4305 | 2025-08-25 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 1953bebf-0e86-3ce5-a55e-ad7e530509e6 | -9.1722 | -59.4629 | 2025-08-25 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 1c3a85e7-b5da-3334-b0ae-470b97211195 | -8.855 | -62.4313 | 2025-08-25 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5f0229e4-76e5-3c49-bf7c-75098511b80b | -6.8229 | -58.956 | 2025-08-25 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f04c1037-63e7-38a5-8bc2-0f23d13638a0 | -8.9874 | -65.4192 | 2025-08-25 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| a1f56ce8-f6d1-35ee-b617-ec27b6ce67e8 | -6.2644 | -59.9976 | 2025-08-25 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| de19a840-803c-38d4-8ca9-3d4e91a9ffd9 | -9.006 | -65.4 | 2025-08-25 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0721cb65-d619-337d-babe-e34588764519 | -6.2459 | -60.0174 | 2025-08-25 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| cd6de237-c88b-3a35-ab55-a468b17ddd82 | -7.8892 | -63.0737 | 2025-08-25 07:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| bf0ddbee-9d31-359b-a57d-4f57290353e1 | -7.9077 | -63.073 | 2025-08-25 07:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| be89d11c-dc76-3421-be28-a646c4e9e472 | -8.8734 | -62.4495 | 2025-08-25 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 52f9214d-3543-39b9-a2ff-e3df3335a407 | -8.9689 | -65.4198 | 2025-08-25 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7230304a-753e-3b55-a287-a3fae2832e1b | -6.246 | -59.9982 | 2025-08-25 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| a2872cd4-d796-3467-9408-1964286dfbe5 | -8.8919 | -62.4487 | 2025-08-25 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8606718d-d5e9-3239-b091-39629f069e2c | -8.9875 | -65.4006 | 2025-08-25 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c921053f-7d9a-3a41-8530-63a4a51f3253 | -8.9689 | -65.4198 | 2025-08-25 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2939c53d-3145-35d3-b2f4-f0c7d9a7dab2 | -11.6089 | -46.3699 | 2025-08-25 07:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 5a814e43-4663-3f7d-8148-5df7b17f9b15 | -8.8919 | -62.4487 | 2025-08-25 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 572590bf-81b5-36f7-af1d-ae0817f7a695 | -11.6093 | -46.3472 | 2025-08-25 07:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6006dd45-baea-325e-a54f-fcd932c0b1b1 | -8.8734 | -62.4495 | 2025-08-25 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f19a79bf-b2a6-336f-b8a4-6df8dc03194e | -8.8735 | -62.4305 | 2025-08-25 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 5af2d55c-df29-3efd-ba2c-f2f26f979846 | -8.9875 | -65.4006 | 2025-08-25 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f4f25559-c977-3727-88d3-e96d016d2ddd | -8.855 | -62.4313 | 2025-08-25 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 348c6f20-ffad-3360-8577-a3cd3360c06e | -9.006 | -65.4 | 2025-08-25 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c5c5b6e8-de8e-3990-b938-fd228a6c6473 | -8.9874 | -65.4192 | 2025-08-25 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b37924cd-1183-3254-837a-82e40e4658f6 | -6.246 | -59.9982 | 2025-08-25 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| fbb973a4-9831-3fc6-b5d5-2664c9bd6e0a | -8.9875 | -65.4006 | 2025-08-25 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5c9b8409-3b7f-3067-b969-ff4029d49c7b | -9.1722 | -59.4629 | 2025-08-25 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| d8b9f4ec-9a37-3092-8a55-0b3460e6beb4 | -6.782 | -59.6519 | 2025-08-25 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 03fdbd39-f0e4-3437-829d-4408fafbdc11 | -9.006 | -65.4 | 2025-08-25 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e1a8a927-cdca-332b-9867-06ce8fb35c40 | -11.6089 | -46.3699 | 2025-08-25 07:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 388502e3-09fa-3246-9d7d-d3509649aae3 | -8.969 | -65.4012 | 2025-08-25 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3ad24f06-5c4b-3813-85f8-89fd2e21041a | -8.9689 | -65.4198 | 2025-08-25 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d6b47552-7bf1-343f-827c-89e880703b54 | -8.9874 | -65.4192 | 2025-08-25 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 508bd29a-d428-3822-bdf0-5fcea802645a | -8.8734 | -62.4495 | 2025-08-25 07:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ca5edc16-ced6-3961-85df-183e44c723c7 | -6.2459 | -60.0174 | 2025-08-25 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| c15e3d31-b253-3a04-bbd2-392350ddd2e5 | -8.8919 | -62.4487 | 2025-08-25 07:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b4e3493b-8f94-31a3-b609-a1ccd40cf9f0 | -13.2269 | -46.0391 | 2025-08-25 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| b78b9172-79da-383f-994c-59c1a5882854 | -8.8735 | -62.4305 | 2025-08-25 07:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 0bafa722-c557-36f9-96e0-57e1d3cadb6b | -9.00788 | -65.69087 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 56efd673-073b-3f4a-94bb-8f394431960d | -8.88085 | -62.4389 | 2025-08-25 07:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 30ce23fb-0671-3d4e-b0dd-87b4d7a00ea8 | -8.49548 | -63.87991 | 2025-08-25 07:37:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 94542cfe-cc6b-3fe2-992a-c8c2d28ee666 | -8.88264 | -62.44381 | 2025-08-25 07:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e41493cf-ed5c-374c-b26c-6760f6cb399c | -9.01359 | -65.37256 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 674a38c2-f253-330b-9821-6faddcedeaf8 | -9.06612 | -65.72873 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 9fe0dd71-4d70-3ff1-8d28-8dd5c2a573c7 | -8.86515 | -62.4417 | 2025-08-25 07:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 99d58dec-b2a0-3457-afbe-4d549cbc2c78 | -8.1236 | -62.86179 | 2025-08-25 07:37:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 3c1ba603-7343-3815-98e7-9276507145c9 | -9.0963 | -65.70937 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| e81a01cd-e1fd-3b1d-8931-e23cab5c971e | -8.97928 | -65.41753 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ba3f093f-68d3-3f43-993a-27670e9af49d | -9.01037 | -65.39697 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 91012849-cb35-3e05-acc7-04ff92f0692a | -9.00222 | -65.40119 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 412d6ea3-6f1b-3935-8597-96671cd63b67 | -9.00523 | -65.37679 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4fbf00ff-2bb9-3a3e-b47f-4945beaf6084 | -9.08675 | -65.72414 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 0e939fb0-1ee6-3cf0-aa18-3d82b792aa7d | -8.49962 | -63.84832 | 2025-08-25 07:37:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| b3f46853-ddb5-33fb-9044-03dba0f1498a | -8.9964 | -65.39516 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 4cd376fd-ed9f-3ba3-8a18-3b9579973666 | -8.98242 | -65.39338 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| eac4336b-8836-3db4-93f2-b6221d0ad294 | -8.86335 | -62.43687 | 2025-08-25 07:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 125.2 |
| d6197988-dc6c-3a8a-8116-2dcbe205b830 | -8.87016 | -62.40003 | 2025-08-25 07:37:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 71b171c7-0f27-3f60-831d-bd0ff2bc3d85 | -8.96533 | -65.41576 | 2025-08-25 07:37:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| a1f4bb94-8d84-3e40-95fb-51a417a45ae5 | -8.8735 | -62.4305 | 2025-08-25 07:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 36b5a555-eef4-316a-8c5c-bdd4e44b2756 | -6.2643 | -60.0167 | 2025-08-25 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| bae8de3e-9762-319e-a9ae-d4727226e359 | -6.2459 | -60.0174 | 2025-08-25 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ab00ab9e-cc94-3401-8acd-75f85f732f04 | -8.9689 | -65.4198 | 2025-08-25 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 531fb3f0-d431-3895-9eab-4d56dda61e92 | -6.246 | -59.9982 | 2025-08-25 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 07553f70-15f8-33a6-8258-a940b261130c | -9.006 | -65.4 | 2025-08-25 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 672a5034-fd43-3485-a02b-775d2327f1cb | -11.6089 | -46.3699 | 2025-08-25 07:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 202.1 |
| d7343bbd-f214-3454-b463-6a802d4ad316 | -8.8734 | -62.4495 | 2025-08-25 07:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 633f70fd-100f-3015-ad11-0a8c492cf212 | -8.9874 | -65.4192 | 2025-08-25 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 049af149-a800-3a80-ac66-67f3bde1d3df | -9.1722 | -59.4629 | 2025-08-25 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| cb460493-5bd5-3188-a6c5-5fe4937acae5 | -11.6093 | -46.3472 | 2025-08-25 07:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6353f53e-f9ef-3802-8ef6-30848774cbaf | -8.9875 | -65.4006 | 2025-08-25 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 019f65e9-9ca8-38ab-96b1-ebfad240a946 | -11.5898 | -46.3725 | 2025-08-25 07:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 7bf83e26-d77c-3c13-b7df-cb9d6331b580 | -8.8919 | -62.4487 | 2025-08-25 07:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |


[Clique aqui para ver as próximas entradas](README91.md)

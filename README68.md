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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42713fd4-d0a1-3354-a219-02f1294cc4b6 | -9.5158 | -60.53559 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 780df01c-dbed-3292-a2f2-07eeb1e53462 | -7.52591 | -61.3197 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecffcb8f-f963-3285-86c4-e5b583df8612 | -9.51331 | -60.52723 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3115c7fd-ebbe-3735-b5ec-5c291e05763d | -8.45832 | -64.05138 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cab954d7-e589-361e-9ec3-a0397e152628 | -7.61887 | -63.3377 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4f8dd7a-b081-3f22-9faf-3efc273edcea | -8.99416 | -60.50605 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2d8a4118-2762-33ef-8a1c-78acb084e484 | -8.98369 | -60.51411 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 40dfecb8-cf96-34e3-9a6b-352beafc8491 | -8.99222 | -60.55639 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1a4c2e2-c0d5-3789-a819-172ee5181089 | -9.20768 | -59.63734 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f14e953-1a7d-3460-9d46-f78d3f26dbf4 | -9.50597 | -60.53905 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7074b14-144a-370e-9b4d-facc762de598 | -9.50998 | -60.5508 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f75d6e7-9c5d-3066-be8c-2106e8ff3123 | -8.56236 | -63.90565 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20a0656b-166d-31ba-b105-6ac2277daa3a | -7.41856 | -60.02028 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dabfabea-b886-3f43-8594-82965e6cd798 | -8.67278 | -62.45498 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bee4a37-e348-393b-81df-5b1ba5a6c12c | -9.16701 | -59.66351 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0ec13db-4f51-3c19-bcae-dad0c7e64332 | -8.98563 | -60.53652 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 211a5fda-96e7-306d-8756-7f0b33fcb07d | -6.94299 | -59.53197 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b3544f4-05d4-36a6-bb4a-e4c5e516edd5 | -9.16923 | -59.6473 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 410d4de5-7871-302a-b756-9245cb144666 | -7.61599 | -63.326 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4acb0ad-457c-351e-b90e-09d72d432e56 | -8.563 | -63.90138 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60a31662-b86f-3a93-9586-49b7c1d03a6e | -7.6171 | -63.32376 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76a0e87d-5a60-3ab3-b9fb-b0a097cc7b18 | -9.50671 | -60.54079 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bdb6b83-4a43-3b15-9c82-2cb4e42d3a71 | -6.94917 | -59.52258 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 201bc22e-8531-326b-a952-560f8bcd4ff6 | -7.91903 | -61.75031 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70d6460e-d68e-3b3c-b4c1-8f365e207bc0 | -8.56409 | -63.91904 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ca695ee-489b-3328-a9ee-390c3295be10 | -7.95119 | -61.74762 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd740732-f7ed-3769-b013-8c4cc38f3c19 | -9.51247 | -60.52547 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb4858a4-f310-337e-acca-c642f1f524c5 | -8.98893 | -60.51007 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8ba029bb-f0c5-3d44-94ec-0545513c1708 | -7.5862 | -61.41054 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4802376-f6f4-331e-928f-ae7c683095fa | -8.10758 | -61.19481 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee7a2554-9005-35be-97e3-802661804fcd | -7.52556 | -67.48631 | 2025-08-16 05:50:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f0e8009-c3de-3171-99df-679e4664b7b6 | -7.42577 | -60.03561 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8caa15e-0614-3e86-9fc7-bf7d04d824c8 | -6.13938 | -57.9356 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94f348e0-0254-36d0-9675-ad2e0599fa15 | -7.94851 | -61.75079 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 130425c5-1118-3db3-ae4e-98c9d7aea31c | -8.97941 | -61.70406 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 58f1ab18-8bf5-3bea-ae6a-022551c99d9b | -8.92746 | -62.2406 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b350fb1e-d181-3530-9d07-9bcae600b0a5 | -7.0467 | -59.62531 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04756398-4471-3324-8baa-f776350f2609 | -7.90663 | -61.74849 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4077535-ccb7-37f9-a977-df3f09afa90a | -7.45246 | -59.93393 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93ac74ad-87c5-37e9-92d6-3b30967c1990 | -9.38906 | -60.54659 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd21a9c6-d4f2-3176-8f36-9e8f681cbe81 | -6.94482 | -59.55283 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb631d73-42ff-3531-82fd-196931199adf | -7.50009 | -61.3794 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3338357-7c53-3068-9781-0d1fc4e83620 | -6.94444 | -59.5218 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7285ae2f-c29e-32d0-ae70-d5f78c7a32e0 | -7.56231 | -61.42397 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a0ef7b7-7a8c-3ba5-b4ad-110bb38be39b | -9.20548 | -59.63617 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a76facf4-a363-3ccc-8e7f-bb42c8e8c17e | -9.1916 | -59.68428 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de16ab5d-a8e0-3ffb-9439-ecb3e701b1b7 | -8.99027 | -60.50071 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5d87444d-4603-3b4b-8721-312710360573 | -9.20555 | -59.65344 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b9b03a5-31cf-32cc-8edc-1ed092502b63 | -7.52168 | -61.31908 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51b7644e-2d7a-3490-b626-de39e9026252 | -6.15024 | -57.93717 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47c04042-158e-3c36-a441-91098e4803b1 | -8.98882 | -60.54325 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e298476a-86cb-369c-b5ee-212ded00cbd1 | -7.8764 | -61.81193 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 001019ab-7cc7-34ee-b683-82a067a8a134 | -7.62083 | -63.32432 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1edc2864-2626-3083-899f-a03bb63e61e4 | -8.98626 | -60.52869 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 90525890-cbe7-3abf-86fd-467fc02e4029 | -9.20485 | -59.65878 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ab91ae0-90f4-3bb7-b4c4-ab8499d6ce4d | -6.95248 | -59.53326 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b269cb87-a41f-3f2d-b676-4e0a35ed8d1f | -8.98825 | -60.51477 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 01ef36ce-61cb-3b27-93e0-c902e87a372b | -9.50079 | -60.54959 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 889fed78-e181-3b68-b529-b434fe451363 | -7.56594 | -61.42843 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c0519ee-a153-380b-9b65-5451a3eb5a87 | -9.17336 | -59.65335 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f6cbc0a-973e-3572-b9dd-1422212783bc | -6.93209 | -59.54054 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe6e2ba5-f977-3624-b96a-4ef416608600 | -7.53014 | -61.3203 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caf70ede-4eec-380b-b873-65f2edd8ef16 | -8.98948 | -60.53867 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7540b2ab-1c80-3a92-8eee-0fe9c0719ce1 | -7.9474 | -61.75822 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69c877bb-dc36-3bf0-87ed-c9eeccd192d5 | -9.06207 | -58.9442 | 2025-08-16 05:50:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ee2f7e8-9895-32ff-8e44-ab16a8ea35c3 | -9.21859 | -59.64877 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d7ffe2ff-8de9-36f8-8674-c3e18d59f41b | -7.04271 | -59.61962 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d92b154-a441-33fb-98cc-e9db02c17a63 | -8.9741 | -61.71122 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 48514f42-10d0-3208-a54c-6ff638863bed | -7.95067 | -61.75134 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4350c49c-1644-3229-8d20-bedd2bc28918 | -7.07456 | -59.22443 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ed30917-75dd-3a73-95e2-04a39eb2a3a4 | -6.70878 | -58.82065 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bcafd03-2caa-3cb7-ac35-d1713f9c6829 | -9.50472 | -60.55487 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 805740f8-f5a9-37c1-8e64-e60bcefc7e8d | -7.95264 | -61.7514 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cba24ae5-1270-380e-b835-07ee9d69b878 | -9.16023 | -59.64065 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0cf0b15b-ef35-3f66-b990-0e62f544f38e | -9.21223 | -59.65878 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7b16e21-b8fe-35ec-90fe-e7454a9b93c4 | -7.6751 | -63.31878 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4bbed2f-31f7-3e71-bc35-093315ba8d7f | -7.87998 | -61.81625 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18ab4dd8-f6b5-3e9b-88b3-0ab7cef82d3a | -9.18831 | -59.68831 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10c26087-8d20-36ad-a1d5-c9de81ea0e6a | -7.94812 | -63.21944 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91f8167c-9359-3d22-b0eb-666cba678490 | -6.79864 | -59.82555 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c357e3f-abe2-36e7-96e7-74e3b0126a38 | -6.79469 | -59.82014 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 526919bf-2725-3495-9185-d1dc29290469 | -8.99285 | -60.55177 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea497239-06d0-329a-81c8-07d2cb20874d | -9.5066 | -60.53434 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cafe767d-8195-362f-bc33-e1668321201f | -9.39795 | -60.54947 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd4425a8-8b6e-3c40-afbe-3659c7ad39a8 | -8.10445 | -61.18608 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 767e4c28-71a4-30e4-b9db-06a24d5f52ff | -7.92479 | -61.73982 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39469587-d70a-3012-8807-6fa23452ddae | -8.99094 | -60.49604 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 879aabb6-92e4-3efc-bdda-89285b88e940 | -8.97831 | -61.71183 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 37.9 |
| a8105139-389d-32fe-aeaa-5983f0e1d473 | -7.49511 | -63.82502 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49c64e12-0b77-318b-b125-1a629dadae24 | -7.90609 | -61.7522 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ae052ca-85dc-3867-a2cd-26f864cc3143 | -9.21523 | -59.63735 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5f31346-8ec9-393b-b08d-ddf86d5173e4 | -8.98758 | -60.51947 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| de8b476b-2144-3fe0-930a-980283053ba5 | -6.94626 | -59.54282 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70f6cab6-b1f0-310f-a2d2-2cbba71039f2 | -6.93752 | -59.53634 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe2d14c6-e66e-3b57-a405-fae197d4d73a | -7.95153 | -61.75884 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c28bf0a-1958-3107-a315-a2a11927058d | -8.96899 | -61.68666 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d7db70cf-3599-3a3e-aca2-575944f0c9cd | -8.98816 | -60.54786 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cff1043f-827e-34e1-b66d-f0a6e8b0b0bf | -7.95787 | -61.76004 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8d1cb2b-be98-301a-b245-d54b093f1424 | -8.98683 | -60.5571 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ec404a3-3722-30b1-ba86-55d4f64cff21 | -9.51517 | -60.54033 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README69.md)

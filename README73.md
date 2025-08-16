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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fb60555-bce1-3a80-9998-c343d60dfd86 | -9.04336 | -67.42328 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79462179-93f0-37e5-8738-dfaf45f1d8c0 | -7.9568 | -61.76035 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ec58747-301d-3f1c-83de-fdda2791363c | -7.67882 | -63.31579 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 534d7020-633f-35ad-8ada-1eb8f7d5e9d0 | -7.53333 | -61.35035 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db141f3f-0de3-3042-8348-04a61ad37e42 | -8.99586 | -60.52511 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0e638dad-e433-3ec9-9337-73cb98ec7e0e | -8.99913 | -60.49844 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f7697bbd-c411-3434-8de6-43bfd52b3120 | -7.61807 | -63.332 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c6e3a3e-c96e-3c84-a1d7-58ba1dcd70d1 | -9.8422 | -67.77518 | 2025-08-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c177d121-aa00-36ae-b548-f6f57032639a | -8.57318 | -69.6936 | 2025-08-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16b3995f-b8f6-3579-81f8-844ffdc981be | -7.6214 | -63.34101 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5baf3f9-fdf6-35a1-81cf-94656d069d15 | -7.91344 | -70.92561 | 2025-08-16 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5380c26-d3da-3a6f-87b1-aaf567b3883f | -8.98278 | -60.51651 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 838e3a09-ece9-31e2-b9f8-ecd8909a2577 | -7.66783 | -63.31018 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 901e0e2c-167c-361c-b3d5-70e272e7cc71 | -8.98574 | -60.55007 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71fc9dc3-c25f-3267-aa30-f60e303ef4fd | -7.94536 | -61.74809 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0b4f38c-2183-3957-890f-704abcf3cf72 | -7.53045 | -61.32176 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c60a484-a1f6-39f7-b326-d2e944c9c7c1 | -7.62306 | -63.329 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1956e10-0865-38ac-a317-992497ab74b4 | -7.56296 | -61.42574 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2710712-13cb-3f01-86ce-c0414bd85d27 | -10.39514 | -64.50112 | 2025-08-16 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d441f626-bcfa-33a1-9617-fc1624733ab4 | -7.6162 | -63.33624 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4255eecc-fa4d-3085-9ec4-6e4841afe316 | -7.92682 | -61.74057 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 66e9356b-3603-3fd2-b64f-91aa385bde32 | -8.89143 | -60.74642 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 360dab1e-ae93-3b08-911f-b2fc2ce9c0b7 | -8.7911 | -71.02573 | 2025-08-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c57b44fe-2ba5-3fbc-8a5a-063bc6786216 | -7.91459 | -70.22366 | 2025-08-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19ed67a0-89cb-30d9-bbf8-6cda38afd3c7 | -9.34203 | -62.58503 | 2025-08-16 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7b02385-d204-369e-a0a8-afb99f45d531 | -9.55794 | -68.5777 | 2025-08-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5f13d3b-9fb5-337d-8d88-5eb32a390cb9 | -6.93978 | -59.55598 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81d208e7-4a98-32fe-8f52-d8fcbad34449 | -7.91255 | -61.73714 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cda110e7-7d41-3600-835c-c6b12827cd93 | -7.04583 | -59.62833 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 671d63fb-d2db-3086-91dc-a86c8b1f4f14 | -9.85488 | -62.22339 | 2025-08-16 06:14:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1a9da83-efe8-34fa-9e86-20b420487f83 | -9.002 | -60.53264 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da38ff5f-3e57-32eb-a4e0-3a70ffe92871 | -9.38695 | -60.54575 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb6cb300-5736-3301-80f4-513d6f00cb83 | -7.53403 | -61.34497 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cd97f54-8c08-3eca-8964-cdddd178abc1 | -8.98813 | -60.53053 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1b455253-c9fb-3847-a9a6-28c6fdcd14e1 | -7.611 | -63.33147 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 218ba8ff-550b-33fc-96e4-df70d2632297 | -7.91689 | -61.75356 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8a30eb4-dc8d-3769-9e66-2734dc4496dc | -8.98359 | -60.50984 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 468e6b5b-73f2-3dd3-897e-490ba790ed40 | -7.95233 | -63.21402 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c43fb1f2-7d25-38b2-b4ae-fc51bc6b75d6 | -7.9176 | -70.22853 | 2025-08-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 234cb271-06e4-3bc2-8028-e6b360b304be | -8.46178 | -64.05258 | 2025-08-16 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11412f68-5321-3c6d-adb6-1b8d1eaa306e | -7.04266 | -59.62689 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed211f7f-55ad-3f24-96c9-3f49fdad97b0 | -8.99507 | -60.53156 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ad73e356-6f62-34f4-984d-1afcfb5f5634 | -9.50787 | -60.52143 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d241fad-1d61-3195-96cc-f905dd30d64f | -9.50708 | -60.52811 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 71917a06-e9eb-361a-bfff-c7f6a1aeeba0 | -8.10798 | -61.20285 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d88ab8f-4a06-32dd-a67e-b8c4f6e588c7 | -9.50067 | -60.53269 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eac0d904-fdf4-3aca-b636-9d64adf564f1 | -6.9362 | -59.5473 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c38e218d-2017-3768-afdc-35beb82cacb5 | -8.96944 | -69.27296 | 2025-08-16 06:14:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0dfc74e5-c360-3807-aab8-d417e2cb9f91 | -7.81949 | -61.33321 | 2025-08-16 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8aa4cba7-26a9-3bf1-b0e3-b0979df0425c | -8.96456 | -61.68196 | 2025-08-16 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4fd8214a-b445-35db-a899-796b17fa6ab7 | -8.11609 | -61.19226 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de33aadc-91bd-3664-b802-b00dade2118f | -8.81393 | -68.61285 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbe35545-adfe-342c-aba6-7721bce7d321 | -8.97881 | -60.54907 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e21a2961-dd09-3d5a-8367-edd1abac2852 | -11.73602 | -64.89899 | 2025-08-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1691016d-e1c2-3467-a737-eaa383dfa852 | -7.91893 | -61.73807 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5e56a890-726b-3002-b2a9-9d7660544751 | -8.9787 | -60.5156 | 2025-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 21c5af8f-225b-3fc9-b905-028ddcc79ff1 | -8.9971 | -60.5339 | 2025-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 8a1754e3-19d4-3984-adb3-74c03ac95c42 | -8.9785 | -60.5349 | 2025-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 998b765b-c515-31e0-9ecc-2c36e7b886a1 | -8.9708 | -61.7033 | 2025-08-16 06:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f1d1b3c5-497f-3539-8f4e-ecb38670fa02 | -8.9709 | -61.6842 | 2025-08-16 06:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| dfe1cd64-d7e3-392e-b630-5f00fd00eb82 | -8.9788 | -60.4964 | 2025-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| c4190aef-96e2-32c7-80db-ac163911d792 | -6.9487 | -59.5297 | 2025-08-16 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| f44f50a7-4e37-3d48-849e-d6bc4d0c4531 | -8.9974 | -60.4955 | 2025-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 26829ccf-d428-3975-9b28-1d23ad7c2f64 | -6.545 | -43.0373 | 2025-08-16 06:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3c6a0275-556a-38f1-8ec1-9fc1a6828085 | -21.0897 | -48.7219 | 2025-08-16 06:20:00 | GOES-19 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.1 |
| fe89f1ec-fb5f-3e42-b3c0-87e78c112b8b | -8.9973 | -60.5147 | 2025-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| b456f00f-2fa5-3d0a-bb95-538fc219b72a | -6.5638 | -43.0357 | 2025-08-16 06:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| fe9237d1-47ba-30dc-95f7-cdaca2dca68c | -9.1709 | -59.6374 | 2025-08-16 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 968537ac-9236-3792-94ca-3b2b60bd13c3 | -8.9709 | -61.6842 | 2025-08-16 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6bdf0081-0083-3a1a-9adb-db8d8768f3c4 | -8.9971 | -60.5339 | 2025-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 71e3d92a-a3d4-3ed5-b206-61c4c0c7b6ed | -8.9973 | -60.5147 | 2025-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 8244b488-3552-33b4-a129-468d7cb19a47 | -6.9486 | -59.549 | 2025-08-16 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 6be137eb-84a0-3f25-89e6-5179db2597af | -8.9788 | -60.4964 | 2025-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| fd4f4320-af9b-3579-adaa-d0a02b1f7f4f | -6.5638 | -43.0357 | 2025-08-16 06:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 06af92e2-df27-347c-a4ff-86d7ed6c36f6 | -8.9787 | -60.5156 | 2025-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1d5dc7e2-db8e-37fc-81b8-40f78998e1cc | -6.9487 | -59.5297 | 2025-08-16 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 67441b8a-0bd9-319c-8d43-12e78b3f91f2 | -9.1709 | -59.6374 | 2025-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 11940e5e-28a3-3a0f-96aa-5ed84db20626 | -8.9785 | -60.5349 | 2025-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ef230c28-1fc1-3864-a0e4-12d37d56cee6 | -8.9974 | -60.4955 | 2025-08-16 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fbd08189-08d1-3904-8eed-30d95ef2df52 | -8.9785 | -60.5349 | 2025-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7f0d920b-103c-399d-9d41-1e695f7d453b | -6.9487 | -59.5297 | 2025-08-16 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 95ac92d2-0c1d-37d8-855e-bf71317699df | -8.9974 | -60.4955 | 2025-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 1a5799f6-38ff-388d-ba34-8a8e9886872e | -8.9709 | -61.6842 | 2025-08-16 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bed55882-beea-31ab-85a7-1ed50f7b69fb | -6.5638 | -43.0357 | 2025-08-16 06:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 59be4c1c-bb8e-38f8-99dc-572758472def | -9.1709 | -59.6374 | 2025-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| bd734239-da67-3cf1-88cc-3a97b5d40e42 | -8.9973 | -60.5147 | 2025-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 5b802a6b-c91a-3971-af2f-92fb2c3938d3 | -8.9788 | -60.4964 | 2025-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 51786185-a1b6-394e-9435-c8e976c3b46b | -6.545 | -43.0373 | 2025-08-16 06:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3cd5f11d-7719-3511-a726-c6af4ecab43c | -6.9486 | -59.549 | 2025-08-16 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| f0943174-351d-3aa7-9b76-e59f8ae28a80 | -8.9787 | -60.5156 | 2025-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 15b431c0-adcf-3aaa-a931-d2afed9b46ba | -8.9971 | -60.5339 | 2025-08-16 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 15766f30-e11c-3aad-beff-0411ad7f555d | -8.9708 | -61.7033 | 2025-08-16 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9df2bdc4-6b27-396b-8636-0e7cd9e865e4 | -9.5071 | -60.54503 | 2025-08-16 06:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 578606f0-d650-303a-85fc-1cb02c53ce59 | -9.50088 | -60.51886 | 2025-08-16 06:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3169c1b0-ab00-3682-8de9-b33b1eee4d54 | -7.52887 | -61.32801 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a34d086e-8eac-32cc-bcee-728c4d419861 | -9.38621 | -60.54179 | 2025-08-16 06:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 01d557af-b3ec-3f7d-82d2-f38c61a73db5 | -9.50571 | -60.55406 | 2025-08-16 06:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| abf7c6a3-3b1c-37a8-a10b-a4d1b2ea95c5 | -9.21739 | -59.65057 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9611f483-f66b-3233-97ab-4167d994c454 | -8.99359 | -60.51247 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7696ed52-95c6-3076-a90a-037bdf760711 | -7.61674 | -63.32741 | 2025-08-16 06:42:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |


[Clique aqui para ver as próximas entradas](README74.md)

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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28273aba-3441-35a7-a210-379959850f36 | -8.43267 | -62.67796 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.2 |
| c00e96df-f539-3108-9403-dc99712260cc | -10.62487 | -53.89817 | 2026-08-16 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b365f6b2-8a68-3c5f-b189-4e139201d846 | -8.95405 | -60.52697 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| c9532817-0677-3675-b8ff-97bb12506e7f | -8.65326 | -54.73478 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0e6f90d-337c-32a1-b414-79a856ba8f24 | -6.85282 | -58.95726 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35570d04-502b-3a54-a801-c382be8b7397 | -7.58064 | -60.87306 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8e8319d-e664-32e9-a90f-970396b3212c | -8.61114 | -54.70425 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5777ec0c-640d-3151-b62e-a4b72a9c31c9 | -6.96306 | -59.28926 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c96dca7-97de-3de3-bcb2-333aa3c9ae69 | -7.42753 | -60.01455 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40d42def-aec0-3665-af50-a2b004c14f64 | -9.2722 | -56.90162 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d622815-02ba-30c5-8148-288d9a9bb8f5 | -6.70647 | -58.93831 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5913af2c-007d-3e8e-940d-78e4741d0554 | -6.70187 | -58.96833 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3d425d3-948a-3161-ace2-3b897708be3e | -6.7108 | -58.93449 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| efeae23c-cf33-3002-a187-1b14655aca24 | -6.79211 | -58.78958 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c98f00f6-b4a7-31d2-99e8-e861a45da9f4 | -8.89891 | -60.56194 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bad4df3b-1e0c-3021-8a67-ea521d390051 | -11.21083 | -54.82 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7388c32-d0c6-3385-9056-4f87da41d5b4 | -7.42432 | -60.00691 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16a8587c-848a-31a6-be55-85859ded2351 | -6.86124 | -58.97616 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3bc599d7-3bb0-3d3a-b13b-31ad0e17e5f4 | -7.58459 | -60.89244 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a2c4b4a-7438-3bcc-ab18-148ac60e31b2 | -8.96399 | -60.50864 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8908aaf-fbfd-3850-8cab-ea3cb48d59ca | -7.38989 | -59.99754 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 65154df2-a9d2-3149-b559-a9a37786ca21 | -8.94539 | -60.51373 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| de25dd3b-55d6-37b8-9002-79bf5383fd3f | -8.96976 | -60.51749 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bfca137-dee7-3931-84e5-67830fe0bd08 | -11.23091 | -54.82583 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d579a65-a855-34a2-a0d6-4361790fdd3f | -9.08288 | -61.40081 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 486a9e49-31ad-301e-839d-d14830227d18 | -6.42964 | -60.07439 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42358afd-7551-325b-a6d8-e4d5eb9dcbe3 | -6.61389 | -58.98136 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e32653dc-6232-3664-95b5-a7d349b4b6ea | -6.96731 | -59.28564 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 895b9b56-4c73-3b27-8698-b26ebc3b9855 | -8.97095 | -60.50972 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da4def8f-2179-385d-b403-db7c8ae29e96 | -6.7246 | -58.93923 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8bc6c53-fd8b-3380-9781-0658569830ef | -7.55575 | -61.16703 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 743864ec-8747-3505-9d8b-8a341584cc24 | -6.63034 | -59.07069 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bb762850-6c83-3490-af31-697bc0cb0ca6 | -8.96161 | -60.52417 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 361761e0-7e79-38ee-a759-1a0713a7f512 | -9.26299 | -56.90443 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6823aec-d412-3a45-8d55-1a7f2627ace8 | -6.63098 | -59.06645 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e3e583c7-48d3-3b45-9152-1d585a6cc459 | -6.6875 | -59.06196 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75a9e62b-f0eb-3443-82a7-3b42e02933fc | -8.97264 | -60.5219 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dceec630-b0cc-3f3d-bab6-0eef515a239e | -10.04353 | -62.45451 | 2026-08-16 05:36:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4413976b-3efd-3e09-8bac-467c3b5c5e58 | -7.89347 | -63.71603 | 2026-08-16 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edb3e8e6-6d85-3966-8ed3-d53dc2bbfb30 | -8.43763 | -62.66807 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0cc2e348-ddd2-324f-adc8-d5069df0d534 | -6.61944 | -59.06904 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e4a271a-be17-3462-a16d-3dbc710270da | -9.49336 | -60.47746 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77187a41-c4b0-3d73-b4b4-41ac8a432007 | -8.95788 | -60.59471 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85f6e94e-5e64-326f-a923-ec9b726d1d1f | -6.97942 | -59.0098 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b49a872c-ff0a-3b62-b46d-71c70e1651ab | -9.50787 | -68.49941 | 2026-08-16 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b36cd766-ccfc-3f3a-9452-b5d9d68ce481 | -6.95458 | -59.29648 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b19581cf-4f89-35e8-ae24-2a3e2387f2ef | -8.5668 | -69.9062 | 2026-08-16 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1936ac6f-57c0-3fa2-ab0a-35955a86842e | -9.37694 | -62.35253 | 2026-08-16 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae44c492-c5ac-3d73-a94f-61cb316bfa63 | -7.38526 | -59.98083 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4555ba54-48ea-3350-91d6-385ee867b0c8 | -6.60287 | -59.00343 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cd73210-c8b3-316c-9860-e84dcfcc6919 | -8.96797 | -60.5291 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 55767a48-3e73-3a7a-b91a-6f63bdcf93c9 | -8.95441 | -60.59417 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6005103-60f7-37cb-89a0-8b50a08ada7c | -6.60616 | -58.98212 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ce06e3e-4393-38c6-af56-db61536ddf18 | -8.89366 | -60.59667 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc0e173d-3274-38f3-b368-503c658227bc | -8.97319 | -60.52945 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed9c155c-85bb-388d-8a05-b8a13c0f9c50 | -8.2651 | -57.34073 | 2026-08-16 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b29764b7-147c-3849-b094-f27c5da73f60 | -6.61769 | -59.05582 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0ea5fda-3227-3a72-aab8-fe20cfe9f0c0 | -6.61706 | -59.06004 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c2067cd-8615-34de-a41d-0865b38d421e | -9.26729 | -56.90511 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a27900a5-d0de-3321-887b-f9ba21d8db63 | -8.89254 | -60.55701 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08e2677a-5059-37ec-9eff-71654ac50a1f | -8.97494 | -60.53017 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f446c110-b3c3-3578-ae6a-68ef22bec121 | -6.72313 | -58.92755 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fe64f9d-5678-30e5-be9f-5c68f9f533b5 | -6.43252 | -60.07871 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b480364a-61a9-3772-b74c-a6d805681779 | -8.97376 | -60.52559 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 535e8d8e-5a82-3903-b97c-4bc0a2ce9b12 | -7.88443 | -63.75097 | 2026-08-16 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10530195-c29e-3d4e-8669-4e6387a05921 | -6.61325 | -58.98564 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 842022af-7b9c-3f45-a1c6-4a7a71e6e53f | -8.41535 | -62.65705 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c53e3ac2-2d87-3c02-a9da-7b946b7d6a4c | -6.70081 | -58.95076 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3a811acf-f1a0-3a13-b11b-8ca12c33b6f1 | -9.25867 | -56.90382 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe70b122-1d9c-3577-9991-07d91e66351e | -6.62925 | -59.05325 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 599e9e97-738d-3cfa-91c5-efeb00bedf6b | -8.42992 | -62.67396 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03130925-a203-343c-aefc-4d2ab33d1797 | -7.4138 | -60.00534 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3d5724d-ca42-3c96-bb93-76e0b110d8f6 | -9.37475 | -62.36658 | 2026-08-16 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c43a7ea8-361c-3c0a-85b4-5007f4f7fb66 | -6.59988 | -58.9986 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0f9dff9-b094-3ae5-96f9-a27b6b71a69b | -8.90005 | -60.57792 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f61ba2a0-2a75-3d1f-be20-500d16ea6755 | -6.6188 | -59.07327 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0969e58-13e6-3235-b27e-e16f9155805e | -6.60251 | -58.98154 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5a415dc-be5d-3073-8606-d19cc85b1896 | -7.58113 | -61.23737 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62a49fc8-d0a8-3d47-b8c3-de7322f8bff4 | -9.29504 | -56.81491 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33ae251d-4ad6-3fb4-bd06-477854bcee68 | -9.29562 | -56.81068 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a445975-f33a-3a79-8fba-fd6451d30dd4 | -7.37833 | -59.95561 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e83d8c6-1ff8-3b6d-93b9-6192b8997312 | -8.43322 | -62.67449 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 2f8c36a5-0bff-36c2-ae90-9c76547dfe32 | -9.07441 | -61.38828 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17585a9d-8d94-3e8c-b560-3da1105844b5 | -7.49629 | -60.08073 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6d9c1ee-5cb7-3fa9-9195-742f26bfa051 | -6.71814 | -58.93559 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3dde8e85-fa05-37ec-9bcd-5685bb56de11 | -11.22108 | -54.8213 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 465baca1-de36-3cf2-909b-907ca0dc264d | -8.96042 | -60.5319 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85b3be9d-41a7-3dad-aa9b-be30ef870d70 | -9.1303 | -66.97031 | 2026-08-16 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fc036e41-1751-3c93-bfcc-3edc3d29dae3 | -8.89485 | -60.56527 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f67943f8-dcdd-3091-afa5-797e32cb0ef6 | -8.94828 | -60.51813 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a4745cbf-c53c-3484-b1ca-f7a0c19feb0a | -6.71513 | -58.93073 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 61d4f698-5b2e-3072-87c5-f2eef40d01b7 | -7.4097 | -60.0087 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9888881d-6ae8-3b69-8b50-45bfb1839b98 | -10.07216 | -60.49944 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfc9a039-e067-350a-9e09-6e8e518b8836 | -6.85887 | -58.967 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a000c089-7b83-3b93-8220-c370f0ed9163 | -6.62134 | -59.05635 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c692f557-e9c0-3487-b0e3-41a6c1830ad7 | -11.58492 | -54.69042 | 2026-08-16 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0385345-737b-3afc-8ee8-09655adfb011 | -11.62247 | -51.09327 | 2026-08-16 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e635a0e7-66b4-34ac-beb7-72e25915a2fd | -7.42402 | -60.01403 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74f86627-1c18-3564-ae04-d7420322aa22 | -11.21162 | -54.81376 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb6ac605-890b-36cc-9147-0f12f3ce50dd | -9.25376 | -56.90739 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README52.md)

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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8dac8e7-2b1a-3fda-bb0d-1a60d3064e23 | -9.18382 | -59.49893 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4e04dc7-136a-31c0-a243-41a7be988686 | -9.18182 | -59.51314 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80bd8fe1-38d6-314a-9692-41fb9f699fc1 | -8.86001 | -62.4478 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ef9830e-374e-3f6b-af0d-cb4215377d9a | -8.864 | -62.44457 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0e82e97f-2b4d-36d4-ab48-3847be100e4f | -9.17484 | -59.53366 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6ff1244-3bd8-31b4-b339-76946a7a9586 | -11.54834 | -52.12757 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1301cf12-84ab-3886-a98e-a643e64b89cf | -9.17319 | -59.45753 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7369da5e-6bc8-3f7d-8f18-7536cccdb193 | -9.17429 | -59.50837 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3ada6c4-fc83-326a-b784-6cfe30fac641 | -9.2202 | -59.67272 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67dee579-d34c-3289-8b92-f2feae7ea132 | -8.57275 | -62.62943 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d17f0d1d-e752-30c5-803a-f72e23051d2b | -10.82537 | -62.44662 | 2025-08-26 05:38:00 | NOAA-21 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5962b446-2a07-3649-a9f8-c72820d263c4 | -9.05259 | -65.7229 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4446c0bb-3088-3438-94c1-72bcb00f23d4 | -8.97708 | -65.42632 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84e0a80e-47e8-399a-b101-f94c6895a80d | -9.03468 | -65.72739 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c218350e-d4fe-3f6c-9f86-fec0d149acd6 | -9.93115 | -65.00793 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6349bd43-66fa-381e-a182-180d2a306de1 | -10.87426 | -55.79431 | 2025-08-26 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| da9f9d42-6365-3469-be9b-404da3a20e2e | -9.16388 | -59.55354 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fe7ed64-e064-3443-b129-bb25f38ee2c0 | -11.57207 | -52.12309 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 71bcad1e-5e16-3a1c-81ae-9a76d329b146 | -9.27855 | -56.90439 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce80604-aa90-3fcc-9e3e-a89af5c513df | -10.64784 | -51.59016 | 2025-08-26 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1344f5e1-4ac8-3b5a-ad1a-dcb50094ec4b | -8.58351 | -62.60465 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ec7f7ac-b835-30d5-a6fe-8a9c7bb3b182 | -9.17281 | -59.51894 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f61893c1-2eae-3a77-9344-74de91192b88 | -9.31204 | -63.43508 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a133b29-a201-3a47-8aac-fb90fd10d0ac | -11.56533 | -52.12231 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38ad375c-13a4-3f2f-a538-f42cfc53dbff | -9.12814 | -60.33 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb4fde0-e775-3fe0-baa0-8372b12586fe | -9.08835 | -65.72868 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 676d3df4-3546-31d2-8e96-6d08efecd73b | -8.84742 | -62.43819 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 111052ab-847f-3cf0-911a-7a6a4e422cec | -10.42185 | -64.39326 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 854933ef-3e48-376d-a6e2-29314da68045 | -8.74367 | -63.74738 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8538374-d909-3a02-948c-4553e1fa8d3d | -9.15552 | -59.45827 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1b2148a-1d63-3d1e-a41e-d94ed27abf92 | -8.56312 | -62.62416 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f73b20-7367-3222-832c-2f0e4d671439 | -8.84573 | -62.44945 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 26363f91-17ca-3e1b-b0bd-5c42953cabf2 | -9.18485 | -59.52072 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 867e8212-a510-3543-abf6-359c7e343084 | -9.19593 | -59.61539 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9388f11-1501-326e-b66b-0976952d5dad | -11.05898 | -52.00248 | 2025-08-26 05:38:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8fa311ae-e7fb-3e04-a5a9-9f230195c970 | -8.57388 | -63.92112 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c80bb45-d450-3862-b24f-c7279f7d6a6d | -14.30977 | -60.36866 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60387222-b69b-3117-b9ee-f928dca21604 | -8.90885 | -60.72124 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09182843-b2cc-3918-a587-95d0962ad1b1 | -11.53558 | -52.11957 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 2b8013f8-6dd5-31cc-9f45-7cb546025a4e | -9.15784 | -59.53825 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 99840c9f-fc73-33ed-a706-c151c192cfe6 | -14.68259 | -59.64178 | 2025-08-26 05:38:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d06fea1-f58c-3a7f-b780-0b02bf0009a2 | -9.19537 | -59.50425 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c4d29e9-bdcd-363e-81fb-ebda076c505c | -9.18734 | -59.50308 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80afcb4c-466a-38c4-bcaf-805d4b40e898 | -8.63324 | -62.64942 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cdd2436-4375-343c-83c9-e6444a696216 | -9.2532 | -60.92555 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6206a753-e432-3e0b-8ec8-bffb66e94bb0 | -11.30653 | -55.11667 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e49420d5-c637-39f8-b943-a9ab3f4213d5 | -9.17034 | -59.53658 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6a93f24f-2035-37e3-9caa-860a3648ed57 | -9.70258 | -57.87884 | 2025-08-26 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f0c02e3-910f-389f-9f99-f3a7b358cf99 | -9.23795 | -60.82356 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0da7e9a-5421-3883-9c38-698c5296ec07 | -9.15539 | -59.5558 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 50df6c75-1620-35ff-a5b4-2549e946774e | -8.98262 | -65.43446 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3ada432-d6d0-3fc2-a849-c2bab18a5d56 | -9.02422 | -65.68533 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1afd14a-3f1f-332c-9796-8a339da787ee | -9.17583 | -59.52661 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51e4797d-4b02-3d0f-a81a-5b861724907d | -8.88802 | -62.47129 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d435776-7c77-30cb-a5c5-feea4105d417 | -9.02251 | -65.69601 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eed0050e-8250-364f-8856-b5c934b77c7f | -8.80856 | -69.29473 | 2025-08-26 05:38:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa54c323-2d23-347d-80a8-e80aecafa648 | -9.49634 | -60.53707 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0c75ccc-7318-3323-bd02-449c92fa3e2a | -9.18737 | -59.53188 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ddef82c1-9aff-345a-8951-a1330528e7a2 | -9.1541 | -60.78598 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 160815cd-0d18-36ef-ae4b-d1f0215e74a7 | -11.50256 | -52.1417 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9267deaf-3cbd-371e-ac1b-4d41f6b6ed0b | -9.16536 | -59.54299 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 938a5031-3c1a-3e46-9df7-22853d1d2f06 | -14.29061 | -60.35652 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d31d0f4-7512-3a46-af30-ff006825fab3 | -10.64094 | -51.58943 | 2025-08-26 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 693976c1-3512-317a-9f3a-8c631b99dde1 | -12.43813 | -63.70155 | 2025-08-26 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d76d1999-9bfc-3274-8bef-2901498c0007 | -9.03747 | -65.73151 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 439cb34b-12e2-32c9-b57a-7aed7f35e2ed | -9.04474 | -65.729 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b575220-2d22-3075-b8b9-d0e63bb15bd4 | -9.01639 | -65.69138 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a72b602-251a-3e2e-ae96-81ad29f53476 | -9.10295 | -62.67142 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab5e8dd6-d907-33dd-a8b7-0f1321f7cb09 | -8.61328 | -62.59726 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86db746d-65c6-33bb-955c-6a0c9e168eba | -8.81484 | -69.29781 | 2025-08-26 05:38:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb51f928-c206-348a-9fe7-5fe713230bf5 | -9.17386 | -59.5407 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 93a1a3c8-4d3c-3f59-81b0-b3129a138160 | -9.07853 | -62.67146 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91d4d688-17f4-3cfb-8679-bc3dbf1a2142 | -14.36364 | -51.92643 | 2025-08-26 05:38:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0355aa4a-37ee-3efb-946e-963c4d0033ee | -9.15782 | -60.78652 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea4da4ed-8a5e-364a-84af-2ecebdc18f5b | -9.01859 | -65.69906 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6967362-53bb-3681-984d-a5536bbc67b7 | -9.001 | -65.40475 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4954c3e6-5ca3-3f20-813d-ac7f8afe0fb1 | -9.18224 | -59.45161 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fd71c62e-a1a8-36f2-aff9-fca5a7f31d8f | -8.54559 | -62.64781 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81c2d75d-e479-3f59-8edf-90b2cc60fc0a | -8.88856 | -62.4445 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4785964a-6e30-30f1-8f9f-5c3922268a66 | -10.41963 | -64.38576 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 172a0f42-3cc6-30e8-824d-33ba9649d23f | -8.88343 | -62.45523 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 893bf4d6-6b3c-39ac-ad9c-7c927142e486 | -11.55042 | -52.10916 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb1f3551-f685-30d8-a6a9-55d6a34dabd5 | -7.79141 | -66.95611 | 2025-08-26 05:38:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e30e1a9a-d3bc-3241-bfd1-9c188aec24b4 | -9.18747 | -59.61761 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3b5fe37-05a7-3ea3-889f-fc88547e1db8 | -9.32767 | -63.19904 | 2025-08-26 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b880a396-99b3-38bb-a655-aa7c54231bb2 | -9.00682 | -65.7082 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28bb4fe2-a954-3655-a663-5e2e36dda990 | -9.16135 | -59.54237 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8b259269-3d41-3217-8357-cf214ea23d6d | -9.18826 | -59.43797 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e43d50c8-7471-3363-9184-2a801a768d50 | -11.54442 | -52.10173 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7629840a-dd56-343b-8eb5-551acfc3f41c | -8.8486 | -62.45373 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6253edf6-1163-30ff-9432-194244d93206 | -11.55373 | -52.14025 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41ee5476-2b86-36e9-915d-e81e7158eb2d | -9.2423 | -60.81973 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f88e1a90-0af6-3ebc-9880-fcd23d0321c8 | -14.75736 | -59.72703 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 239ec73f-2156-31fc-a5bc-dea6a31223cf | -9.19186 | -59.50013 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e23b956-e726-3cae-946b-ccd5e68d479a | -8.86972 | -62.45312 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 272cce65-77d9-37f2-bbe7-54835e7eb0e4 | -9.18026 | -60.85584 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f81e3109-9d7d-38d7-9f94-953bb0ca7a9f | -9.80342 | -64.259 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22601227-1226-3801-8b20-5952d5743bc4 | -9.13487 | -60.78772 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ba6b654-59e3-3014-8ccd-030859dcc7a4 | -8.98876 | -65.4173 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be24263d-f848-3c46-a72f-de8cf4640e43 | -9.25082 | -60.91611 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README82.md)

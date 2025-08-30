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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b889899-ffed-3da4-9a1e-40783bd0d3c3 | -8.18046 | -61.37516 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f6c8278-333c-39d9-9c14-a9332f8c76eb | -8.87972 | -60.73746 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6138839c-af38-3fd7-ab5e-ed78f587e668 | -8.65504 | -68.68565 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60479ae8-0aa7-371f-b8e0-1e043fa601f6 | -9.45374 | -60.56124 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2312ebb0-df2b-318f-8c83-c379d1d60309 | -9.43513 | -62.33468 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 028c7b89-7736-35b7-9ee6-d254bd6fc184 | -9.45125 | -62.3309 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 9f3871a8-4156-3441-88d4-9238f398f325 | -9.45219 | -60.57318 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19819fb1-2932-3125-803e-9baed3cf221d | -9.77398 | -64.24854 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ac21461-d4a9-3863-942c-4e03b7c24b29 | -8.61548 | -72.38972 | 2025-08-30 06:01:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 696f7e12-82e2-38e9-8fae-c90f0b3aa4ae | -8.74252 | -71.10717 | 2025-08-30 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ef5ee318-cd69-3601-92e3-7c64462b0120 | -8.57223 | -70.06136 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19501961-2b7a-371d-9f1c-55c24080d52a | -9.45085 | -62.33399 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8af373fb-1245-3e78-bd95-518bd0da535b | -9.46844 | -60.31073 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2919710-6641-35e6-947c-8533ff6c3b2b | -9.44379 | -60.5476 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5372f123-7a95-3d87-9d72-977008f9b721 | -9.06496 | -65.44231 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9d10a4f7-64c5-3371-b463-84015a892e33 | -9.78751 | -64.2505 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3de1e58-f326-363a-b574-72ab97b0de8b | -8.65598 | -63.29489 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 571fa084-eb06-3089-9dc2-70e0a8d11dfa | -8.18249 | -61.38478 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 526812a9-c148-3f64-ba40-45fadcc4d859 | -9.43805 | -62.36929 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e6b9a60-fad2-33a0-932e-ba5c90b003db | -9.45469 | -60.5608 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7e1b4e67-e53e-3b8f-bbcd-05568ce27f53 | -9.4611 | -62.33536 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 1c84763f-eb9e-3f4a-a94a-1d3c1729610c | -9.17427 | -65.55254 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb9452f1-42a2-3bc6-9eb3-c3d8d6f74020 | -8.52185 | -70.03555 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c9dfd4a-daab-3545-8547-000f5b72ceea | -8.61998 | -63.95651 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49205a1b-a06b-33d5-8ed2-09198ba0528b | -9.45519 | -62.34079 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 483f5162-c814-3905-ba6c-e0b9997de9fa | -9.45425 | -60.55735 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2700387a-9e95-3f9e-bc4f-650a659d8320 | -9.44066 | -60.57175 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 74428c43-5da9-304e-a080-8f3c81428e4d | -9.45759 | -62.32212 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6c5853f0-266d-3b0c-859d-b30258847f3f | -9.17107 | -65.77738 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 344df32c-9079-3aa4-8994-a90db45bdcc0 | -9.44217 | -60.56734 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4013cc73-20f6-3b63-8394-ba00fdbeed48 | -9.97441 | -64.95358 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bea419f5-012f-34cc-a74e-01a430c755bb | -9.77974 | -64.24004 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a9d2c37-5082-3426-b746-40181578350c | -8.90116 | -62.10332 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4a70f0fb-d771-3731-92d7-2a5c16ea685d | -10.10987 | -68.96331 | 2025-08-30 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 394ea365-766a-3203-8d66-64330f8aa24a | -9.45206 | -62.32459 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7872c450-5f2f-33a0-b5e5-22311a0dbe11 | -8.25549 | -61.45086 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e10ddb54-4a99-3074-b322-ab2710f3b1a5 | -9.44185 | -62.36359 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cccc9b9-d71a-3b33-b398-92aaccea33ee | -8.5952 | -69.71559 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 477f21fc-1af8-3f8f-9fcf-b899bf86f51c | -9.67583 | -65.02721 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 641697ac-919e-3ff9-b28e-825f0cb70a95 | -8.87922 | -60.74128 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88dbee48-a982-3365-9775-e090d3aa715c | -7.89895 | -63.00827 | 2025-08-30 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7d05a32-0537-35d5-a141-0f9d06757e24 | -7.99381 | -70.28375 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e6fd4eb-b5b5-3068-9947-149cda0853c6 | -8.55156 | -63.02462 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 657ab7ec-1fa1-3873-a337-25ab5fe21de8 | -9.77336 | -64.25311 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8fa6d54-3a91-3f46-8d87-bfc549efe38c | -9.78238 | -64.25439 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c2e6c82-25f8-3be8-b337-74b45963702e | -9.4369 | -60.5625 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5d07d41-a5a0-3d8e-9ee8-c1703fb231d6 | -10.19985 | -68.43672 | 2025-08-30 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 161b6ee9-b4ba-3e5a-b569-5df0a9457a83 | -9.44011 | -62.35407 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55e9f22d-f899-311b-8b4f-17fd31f59d54 | -9.24169 | -59.78027 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eb7555f-6d5c-3420-9154-a7530d75c59d | -9.45517 | -60.5569 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a0904c7d-1b00-37fd-be57-e4635634aae3 | -8.56119 | -63.02601 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 611f3ee2-bae4-3f31-b59f-03a395c6d487 | -9.46544 | -62.3421 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37f04f09-ab79-3122-9762-94b49d42b747 | -8.85118 | -70.62977 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6623bc42-d36e-3110-8328-c9f5a9a838e7 | -8.17999 | -61.37857 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35bd67cf-bdef-3d72-adc1-069ad90b4267 | -8.55301 | -63.01399 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f55a776-0803-3db0-8a38-b5301409e207 | -9.46663 | -62.33289 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a4bf9a81-6d47-3d82-9a57-f9faf9e7c89a | -8.58235 | -69.68823 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 613edba1-5098-318b-9c79-7c84bd4e55e6 | -8.90672 | -62.10103 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41031e3e-36a3-3f86-a600-4ac3930f6c48 | -8.94626 | -67.71714 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3fc38bf-ffc4-3edc-8d36-3d5a405e9a93 | -8.53679 | -70.74678 | 2025-08-30 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33c87dc8-5998-3e5d-ac71-4e28f548ecd3 | -10.36871 | -59.2127 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c5d3013-9f4f-3c69-b7b0-9e96d463a1df | -9.6764 | -65.02317 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6db32f9e-be19-377b-b33a-c135c4376e0c | -7.89824 | -63.01346 | 2025-08-30 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f952675-4791-30ce-887c-f315e9ffda3e | -9.45585 | -60.54503 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5fe5e340-fe93-39c7-83f8-5082c7c2a490 | -9.4542 | -60.56478 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 86a9899e-9379-31a8-b449-82c5f0a486ba | -10.37279 | -59.20241 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5be86dfd-0da7-30f1-9b85-f43a9635aaca | -9.44064 | -62.33236 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 99701c52-1ec7-35da-a111-304ced65ee2d | -9.72668 | -64.91403 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20bbac8e-6944-3891-93e1-791fdd008883 | -9.45637 | -62.33162 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 4d10aa78-6797-3352-a79c-0b1fe01e89e8 | -9.45007 | -62.34008 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| aa369965-3741-34b3-be7d-d78eac700085 | -8.67226 | -62.43652 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60222340-e43d-3588-a93e-3aca297a5ee7 | -10.36641 | -59.20175 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5bad9cd9-d377-38a5-82eb-12e13015ea14 | -8.87508 | -60.72897 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a6f763e-9150-3fb5-b789-f5e97718bf4e | -9.27816 | -60.45685 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2e9960b-c7c9-3cc5-a864-c1ac46b0a734 | -9.44564 | -60.53893 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 26e834fb-0c5c-366b-8b8c-8e08266d9f88 | -8.56192 | -63.02071 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c0191a41-2a6e-35c3-8e5f-71a4b68034ff | -9.18058 | -65.79693 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b94743f-a6fe-3adf-aa81-5bcd5163b422 | -10.82653 | -68.2349 | 2025-08-30 06:01:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e282fe8e-6bca-3e39-b339-f3af443621eb | -9.4438 | -62.34835 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 280cbea0-f3a5-30e7-a0c1-8b3ab924d08d | -8.17952 | -61.382 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7cc2628-4361-3c91-952a-9544c9a81ef5 | -8.67204 | -62.43938 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83c64f47-455c-30df-a318-5ef8005b3a1e | -10.3747 | -57.83132 | 2025-08-30 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d32600dc-44bb-3d1f-a93c-2cfde53e66fe | -9.80794 | -61.19833 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65516ed2-aa18-3f48-a43a-f9e35aaca368 | -8.7623 | -71.06755 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c5c479f-9aa9-3780-8d56-3a0e1000efd8 | -8.90157 | -62.10024 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec4ac55e-6333-3d4a-9e70-30ac7bab6813 | -9.45362 | -62.35297 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b211457-535e-3b8c-8885-3fd0caf7776c | -9.43641 | -60.56652 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 45e3de4e-ee53-303b-b440-0531d353d23a | -9.44514 | -60.54301 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 108000da-b59e-3899-a12f-f75ffb088fae | -9.72923 | -64.91254 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dabad977-3e66-343c-9568-9b8fbc999fda | -8.44766 | -70.14204 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb48ebfa-37a5-3894-83bc-63fff11c8127 | -8.28441 | -61.42253 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f666251-1b81-392e-9012-c26bc2387bcf | -8.67767 | -62.43428 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 796773f5-52d9-3378-9701-e73991b839e5 | -9.2577 | -65.84068 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa9bf4f8-5374-3eef-866e-e726cddbdd96 | -8.56838 | -70.06435 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f89e1607-a538-388d-aa17-7c7bbd8d8c5d | -9.45284 | -62.35907 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7575a810-9daa-36ba-aa6b-45728d450401 | -9.75849 | -65.08302 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc01e945-8c29-3c09-babf-39046fb29736 | -8.87454 | -67.74155 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6771564b-e92a-3f79-9fbd-a95b8f24a230 | -9.44143 | -62.32618 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 98ea1dd3-02f0-373e-a48f-ce2d957a265f | -10.38166 | -57.83163 | 2025-08-30 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e399f61-3449-3a26-9725-d6a87d92f259 | -7.35196 | -70.12549 | 2025-08-30 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README85.md)

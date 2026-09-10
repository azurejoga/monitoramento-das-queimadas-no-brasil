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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0e81d65-25b9-329b-88df-83ae1f66cbbd | -10.73707 | -45.92179 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d59288c7-6c86-37fe-a5fd-a3eda224c140 | -12.35478 | -48.19927 | 2026-09-10 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7769b72c-1d1f-38b7-888c-0cd49d925026 | -9.04272 | -65.41566 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5180a164-4a1c-3ef5-96f6-eed0d0ae28eb | -9.83815 | -59.46771 | 2026-09-10 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc1fcb66-7736-3dbd-a5b6-f57e593ff0ef | -9.22099 | -63.64434 | 2026-09-10 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c6a09e6-f03f-3cad-8410-8f36410bdc35 | -9.03956 | -65.4168 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea9f73ed-c9c6-3d34-a9c4-9319046c3506 | -9.08998 | -59.46471 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e0ba88d-337d-3d09-abf9-edcaa52bf492 | -9.08018 | -67.86582 | 2026-09-10 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b67e1f60-059c-3b31-af91-0105d4763d62 | -8.98401 | -60.58069 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c9cf1b9-0f54-3227-9663-7f3958526a6f | -10.84977 | -60.83137 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e05833d7-bc34-37f8-9485-a034f1bb5a39 | -8.9107 | -62.36146 | 2026-09-10 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c29c9019-3a4d-3f23-87f1-81db87734ab9 | -8.88867 | -61.42836 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 391be473-b7e9-3d78-8486-594262c8ce0b | -10.60353 | -60.78761 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41541513-d6c0-3f81-a0fd-ebcf35be4e48 | -9.04972 | -65.41354 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50a46915-fd47-3673-8b63-cf6262ed0ec2 | -9.20397 | -65.7751 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a9f6b02-166c-355e-be2f-4ab5413f4d98 | -9.29895 | -60.90142 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c72ba6f5-6b38-3583-8e4b-1bbe168fcd0a | -9.65312 | -59.60682 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb8143d1-9871-35dd-8475-399a2d6a272e | -8.98526 | -60.57288 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbbe9d16-4fe5-3b5c-b8bf-38768656c755 | -8.88406 | -70.84175 | 2026-09-10 05:12:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4041d1f9-c88f-3ba1-8e0b-e397227999bc | -9.15191 | -68.24791 | 2026-09-10 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa97d1b6-e8b0-3e9c-a86f-66c935ae91b5 | -9.08566 | -67.86683 | 2026-09-10 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07734f0c-2695-3c6c-9bf1-59b9ee6accf7 | -9.21029 | -64.50636 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b5686de-c18e-38b6-9acb-c903fd53d788 | -8.82073 | -62.48153 | 2026-09-10 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06b7b21d-1e39-38e3-8a14-d6f6ebe84447 | -9.00315 | -65.40528 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 905eacee-f32e-3459-a4c1-8c33dfa682a9 | -9.04826 | -65.41158 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3693bb7e-d0ca-3b40-85cf-63bfef55c0f0 | -8.68624 | -62.45926 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d697599-89b4-3857-bd85-92f271d5206f | -10.07698 | -45.47896 | 2026-09-10 05:12:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0e15814f-2eaa-3968-948e-a0146a5579c6 | -11.42312 | -62.1064 | 2026-09-10 05:12:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df4f3495-8c7c-3113-8827-2067e0fafeb4 | -8.99098 | -60.5818 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a7f3334-fac6-3c53-9c96-52575196fa6b | -9.22227 | -63.63681 | 2026-09-10 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5907c9a-a10b-318e-b0b2-e8d77f7c05aa | -9.1994 | -65.7763 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 071bd498-7119-3a19-9971-ec3167ea51fb | -10.41256 | -57.22272 | 2026-09-10 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dba5190-71ef-3bb3-9a78-92bb142127db | -9.13702 | -64.40682 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a40a14e6-493f-3356-8350-a15dba67ae25 | -8.88797 | -61.43262 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f51ee21f-a6f8-3060-bd71-1008ae706eeb | -11.21699 | -49.94202 | 2026-09-10 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6befc2b-9985-33a2-884a-6e7526eb5d62 | -8.89311 | -61.44658 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fc6ac66-2381-375e-8deb-4397caf684a2 | -8.99261 | -60.5814 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac527a70-5bb5-3209-846a-2864cc6fc415 | -9.68619 | -48.3725 | 2026-09-10 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0742aec5-7edd-3b9d-bbb5-f05270821dcb | -9.04738 | -65.41649 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a9563228-24a1-33cf-8432-74e0ca49cbc6 | -8.68238 | -62.45861 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b6221b1-cf77-3eb7-9e55-a5f8ca4d0110 | -9.21971 | -63.65189 | 2026-09-10 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de9d5c7c-b078-33e4-bb94-bed30f9a44fc | -9.03837 | -65.73787 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35d51ba1-9862-3d9f-bf19-3ec290293d2c | -10.93823 | -54.08262 | 2026-09-10 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aac0011-2322-3510-8cdc-85604b21e58d | -8.89816 | -61.43867 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ca485bf-b7d1-3c17-b511-2318142296b1 | -9.22035 | -63.64811 | 2026-09-10 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35649233-99d0-33fe-89f2-2a2eae7d57a4 | -10.85952 | -60.83694 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74472079-7494-3576-b188-93530780cfb8 | -8.67852 | -62.45797 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47f5e3f2-ab47-3bea-a805-0332e084c937 | -8.99937 | -65.39952 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 97ba4155-6757-3cfc-bb45-ecc0ff9a311d | -8.92505 | -66.854 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90f71189-56e1-3a3b-9ce7-8060ea214147 | -8.98463 | -60.57678 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 067f27a6-407d-30d5-af35-739f76b425c5 | -8.99161 | -60.57788 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1f280fc-6bbd-3140-ac15-8fe8636e3fe9 | -11.87631 | -44.8484 | 2026-09-10 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7782d462-96d7-387a-aadc-3d4b6877af7b | -10.60417 | -60.78373 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68012ed9-d1a0-3f0f-a01f-048f3c5026bc | -10.99067 | -60.65808 | 2026-09-10 05:12:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88730672-8c15-3478-8ac0-fdd92305add5 | -8.8246 | -62.48216 | 2026-09-10 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebee8f37-6895-3f3b-a86b-a019432f8734 | -9.13627 | -64.41104 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52c5bbdd-3a7c-3fd6-b098-10c5d2de24d4 | -9.03807 | -65.41485 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f55e866-6230-3c0b-88ee-c0f9c4c9f1b4 | -9.2175 | -63.63988 | 2026-09-10 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cd15813-e6ae-3442-be30-8f50f6fe7fc3 | -10.99006 | -60.66183 | 2026-09-10 05:12:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b71da5f-bf16-31e1-869d-d152d89117ac | -10.75644 | -45.92838 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6c0130e-2850-311c-86f5-ecd12cd44205 | -9.04128 | -65.74915 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 088ea0ba-603a-35f6-85e5-011442b96615 | -9.19921 | -65.77425 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 703400aa-80d1-3990-9c84-eb532daa4163 | -9.78905 | -47.05515 | 2026-09-10 05:12:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc8331e7-4d92-35ce-8b65-27ad055e7fbb | -12.63922 | -47.08705 | 2026-09-10 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 545df846-fcc1-3118-94a6-035c5a2ba541 | -8.89453 | -61.43806 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e23e2533-531a-3bd4-9a1b-82b9360b7262 | -9.14062 | -64.41178 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41dfc2a6-4afb-3159-a39b-80b3929f02db | -12.7706 | -48.68416 | 2026-09-10 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4aa61b6-a7d9-3458-aace-39d10cc82bed | -8.37052 | -62.93213 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e2af8f2-be07-35b0-8498-dcfddb24bc68 | -10.84913 | -60.83524 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d67ef97f-b25a-3a25-9424-85e67ac6d9f7 | -10.6759 | -46.00231 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29499728-8ddb-32f1-a4a0-bb10684926d9 | -8.3711 | -62.92863 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e117e72e-0233-326f-b34d-be8c50954be5 | -9.9302 | -59.61497 | 2026-09-10 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fc81fba-e0cc-3342-a804-bf42e198641e | -8.68062 | -62.45579 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c911a85-7d2e-3a72-9968-d3844357351d | -10.7378 | -45.91528 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e642fc8-b3da-3e44-bcdf-a1b328a617cd | -8.90249 | -61.43502 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46d0fc8d-148a-3932-80bf-a36f85b92327 | -10.86078 | -60.82921 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5b7b9a97-4007-3bfd-b2a6-6580c7234e46 | -8.73608 | -62.38566 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e54cf51c-7649-32e7-9801-bfe5a5b35436 | -9.03745 | -65.74308 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b658604-ff82-37f6-85c7-c990717d5024 | -8.9921 | -65.41354 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 634f9666-c682-3fb7-989e-96b96ba5ec62 | -10.03312 | -67.82642 | 2026-09-10 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e2a949c-81f9-3113-8ce6-b06e2104633c | -12.64551 | -47.08793 | 2026-09-10 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acee584c-5fcb-3630-9553-3b4c20b857b7 | -8.88938 | -61.42411 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87da8b89-f9e9-3ac2-b538-17e033632747 | -10.19549 | -68.77062 | 2026-09-10 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74583180-9eee-3dd5-869e-f58ea6303c1e | -8.99197 | -60.58532 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e368751c-e8ce-392d-99ff-ea245d95ef07 | -9.15535 | -60.36216 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0000ee3d-faa1-3a2a-9ca1-76fc8a644ea2 | -10.67657 | -45.9966 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9b39013-20da-3f19-93af-84b459264722 | -8.9985 | -65.40448 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d4834fb3-8edc-3f9f-a09c-aaeb0f390ba2 | -9.02804 | -65.44363 | 2026-09-10 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c262f45-2b1e-371f-aa74-276d509fb5ec | -10.98945 | -60.6656 | 2026-09-10 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 497bf5d9-50c0-3e26-a5aa-2ebcbfa1a7ea | -8.87985 | -70.83945 | 2026-09-10 05:12:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50574a0e-a75d-3dd0-b3ac-55dde5c180ef | -9.21686 | -63.64365 | 2026-09-10 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a365986-24ca-37cf-ae64-79fec40908ba | -9.65369 | -59.60327 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2704789b-c579-38c7-abfe-a57fc0ceb866 | -8.89382 | -61.44233 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b05657f-cb04-3a65-b932-695aeee87baf | -10.73896 | -45.92206 | 2026-09-10 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87e4a705-4e71-3ff3-9405-e5be57a74282 | -9.88705 | -47.59652 | 2026-09-10 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de1e20b5-5d24-31bb-a51a-19d4e2b36fbd | -9.68744 | -48.37275 | 2026-09-10 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1591b683-296a-3a80-be02-01cbf46403c5 | -9.83758 | -59.47128 | 2026-09-10 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 174540ff-462e-3687-8833-64bbf7e93370 | -8.15413 | -62.90151 | 2026-09-10 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b9792f7-5341-33bc-bc6a-8a104679edac | -8.90612 | -61.43565 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4fce966-32c5-3ad6-a708-8586e50176ac | -8.89019 | -61.44173 | 2026-09-10 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README35.md)

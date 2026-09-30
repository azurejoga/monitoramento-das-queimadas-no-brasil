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
| 06dd977e-2c6a-353e-8000-89a988797907 | -3.00649 | -54.22598 | 2026-09-30 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aefadc7f-6cb9-31b5-a28b-23f74753552f | -6.33981 | -55.32967 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18d2cea2-f2b9-3f87-9f7c-dbee45485ca6 | -2.90246 | -54.0938 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| aa502a1f-bce2-3670-b6c9-6b8825e092f1 | -2.89378 | -54.11609 | 2026-09-30 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3410bab5-e1d7-39e7-a23d-27d2030669ed | -9.54771 | -56.1639 | 2026-09-30 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c59d7e33-f2be-35df-a288-0800120e1217 | -9.15227 | -67.93582 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0745f41-52f9-39d8-bc90-c5b93c679290 | -9.07816 | -67.81551 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51db1719-658c-340d-8f79-1234bd608d95 | -10.06853 | -63.08346 | 2026-09-30 05:38:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf7371de-0fdc-32ed-82dc-e026e60daaef | -10.07587 | -63.08081 | 2026-09-30 05:38:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58963aed-071e-31d7-821f-a474374baca0 | -12.78623 | -53.9994 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b1cabdd-9ed4-386a-818b-42836f0ad715 | -12.77948 | -54.00887 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1de76c9-9757-3b78-97b1-94f5a5226c41 | -9.08788 | -67.75635 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29fd680a-65d1-3bef-8a88-63fd44bda753 | -12.79169 | -54.0104 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04e13bb3-2e0a-3288-a1db-33c8f6fc7e23 | -9.54486 | -56.15723 | 2026-09-30 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d4cec77-b96b-3bef-9fe2-364ad2cbee52 | -9.54303 | -56.16006 | 2026-09-30 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fa7bada-3bb7-327f-816d-88879fa40fd8 | -9.13771 | -67.93342 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1462813-56a1-315f-911a-5e1b29c3b7a3 | -12.15089 | -60.74421 | 2026-09-30 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fac94cc-af6e-3f6c-b923-18beb91077b8 | -9.12244 | -67.9353 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2ba51b2-bdba-3529-a295-2e1f1ee2dcee | -12.12678 | -61.14749 | 2026-09-30 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6abd886f-9e55-370c-9f7d-61924e4d956c | -12.12613 | -61.15217 | 2026-09-30 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a319104e-38f8-35d5-b827-1b31f7747b45 | -9.43953 | -67.42701 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9472a1f-a2bd-3404-aea9-47b056b6591d | -12.78611 | -54.00479 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8dbe8d6-0543-3692-b69b-9d25294415ab | -9.11661 | -67.83055 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efce38b5-ab26-30a4-ab5a-3b69b2f00392 | -7.93182 | -70.68122 | 2026-09-30 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 07dbc782-05a4-3919-bdeb-c110dd0beacc | -9.11709 | -67.83368 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5bd9fbc-2e01-3395-aaf5-9bfa52f1df8a | -9.12315 | -67.93102 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e369c912-f6ad-3842-8507-b8c45b5ec0bf | -9.22938 | -63.6354 | 2026-09-30 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7331e029-5250-3b73-b148-a557d175782b | -9.09638 | -68.20406 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 220fa055-5d6e-3432-959c-2d0d7f0b4807 | -12.78558 | -54.00963 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e77a7b61-d791-3cd1-91a3-ccbe6f371af4 | -9.42752 | -63.69543 | 2026-09-30 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 044671b5-982e-370d-a9b5-85b37d58dacc | -9.47515 | -66.78231 | 2026-09-30 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ff59ff4-7ebd-322d-827b-0559ce8d08e7 | -9.12104 | -67.75751 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4d4c597-3df0-3a29-b1b0-35cceedd989c | -9.10849 | -67.72095 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dda274cb-bbc5-3a8a-9ca3-8d5bf2ccc57b | -9.01529 | -68.57243 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 658b5967-dbef-34ac-af5c-3c9a8033b3f1 | -8.04761 | -71.35094 | 2026-09-30 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d77a560f-f3b4-3cf8-b841-640895e1aadb | -10.07531 | -63.08449 | 2026-09-30 05:38:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1584564d-ecda-370c-9509-c63cf4d11c6e | -9.11637 | -67.8379 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1498b62-75df-3617-990d-24ad33713349 | -8.84306 | -68.69683 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a61b480d-3ab8-3bb9-8a75-c69db5d4d41b | -8.93727 | -68.6672 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89d5e5ae-5600-324c-b827-f77c51bc82d3 | -9.12263 | -67.75654 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ed7ae6d-7979-3ee1-a3f4-719a6078bd34 | -11.4416 | -58.78821 | 2026-09-30 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3680ce68-d1e1-3675-bee5-22b0b243c439 | -9.5434 | -56.15712 | 2026-09-30 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aee09797-eec1-358c-ba25-1687f5b6c491 | -8.77504 | -69.53677 | 2026-09-30 05:38:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d587a5af-4e15-372d-9298-a2bf7777545d | -9.4034 | -68.16482 | 2026-09-30 05:38:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d77d583-f5ff-3c32-9eae-caa12d6e8297 | -9.08427 | -67.75576 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f846e442-57d4-3472-9080-2733f04ab729 | -9.46474 | -67.12115 | 2026-09-30 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54f29893-f984-32ab-aeeb-d930e61a014a | -9.12465 | -67.94447 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fac4edc-c196-376e-87d1-274457fbcab8 | -9.10007 | -68.20467 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5fdf0dc-b1c6-38a3-a0a0-fdd94ebb5461 | -9.14031 | -67.85058 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7992ab76-dcd5-370e-9541-bec02ebd615d | -9.12291 | -67.84333 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf20d74a-e1c0-35bb-90dd-d62da0671c77 | -12.779 | -54.00836 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 255b2b9f-7bd7-33ce-bd97-b782467a0d14 | -12.78664 | -53.99991 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99b8663b-025a-3518-969b-59dcb75a7d1b | -9.09149 | -67.75695 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 095c2568-35c4-36da-889c-fb70e6e195ed | -8.3821 | -70.0294 | 2026-09-30 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36596677-8267-38da-8ede-f85ae4bbd308 | -8.25964 | -70.13644 | 2026-09-30 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2e2f3c4-0ca4-3b38-a5d2-a0327a1326ef | -9.54447 | -56.16015 | 2026-09-30 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dae0fbd1-959a-3114-9d61-7858d428498e | -9.10917 | -67.71676 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dd4f3551-41b1-30f3-a146-b4739c9743f8 | -9.29778 | -63.74331 | 2026-09-30 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53095185-7eb4-3293-be30-b1314cf08b3a | -9.13669 | -67.84998 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33725325-6017-3475-9ec7-a34b4b36aefb | -9.39973 | -68.1642 | 2026-09-30 05:38:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a103f046-0dbe-35b8-9378-811a3244bdd4 | -12.12235 | -61.15161 | 2026-09-30 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 407cb158-89d8-3533-96dc-696f124cfefe | -8.00932 | -72.34126 | 2026-09-30 05:38:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 747e34dd-9c00-3fa4-8035-3f99f3c1b0f4 | -9.45722 | -68.71983 | 2026-09-30 05:38:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06416010-e36e-381d-8f81-e26a9b652fd7 | -9.10303 | -68.20971 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0402829e-148f-38eb-b96b-7477a2cce9d4 | -8.60478 | -70.20222 | 2026-09-30 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5069bd46-4080-3530-b99f-5125513733b2 | -8.06814 | -61.26947 | 2026-09-30 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 671c1d72-93c1-3278-a08b-61462967e842 | -9.10868 | -67.8336 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e36aedb5-823d-3a3b-b942-cd96504da28a | -9.10574 | -67.82878 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c818407-a928-31b9-8e76-470037950d4d | -12.47553 | -61.58844 | 2026-09-30 05:38:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 579e7c55-67c7-37d4-a38b-b44cff4db67a | -9.08719 | -67.76056 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d92577f0-ec13-3031-a4f3-a1899ec07b55 | -7.78843 | -61.07323 | 2026-09-30 05:38:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4991651-1429-32d2-93f4-66201230aedd | -9.46021 | -67.14858 | 2026-09-30 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31b1d753-1381-39c8-8b77-6c89b9e5d403 | -8.48452 | -54.91166 | 2026-09-30 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 997f3be9-4e22-3977-a83e-f935957a99d1 | -12.78506 | -54.01443 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55652c21-88bd-3379-b659-44360336d065 | -12.68772 | -61.96578 | 2026-09-30 05:38:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bf493ac-955f-33a5-b05e-b8979427fa78 | -9.72065 | -67.08573 | 2026-09-30 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a6e8e86-fb85-36ad-a385-1894fbec2532 | -8.04965 | -61.27084 | 2026-09-30 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5e82671-6a6f-3cb2-a6df-9c4a0e7324fd | -9.42419 | -63.69492 | 2026-09-30 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 773ba13d-b66f-3b37-821d-13c195a9ab7e | -9.09564 | -68.2085 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 879ff825-7709-3448-8581-6c3674b6b9d7 | -14.50861 | -59.80204 | 2026-09-30 05:38:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9e2b2cc-7d46-3fdb-8b5d-6d66e44e2b28 | -9.09218 | -67.75274 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7478e306-1eb4-3bc1-9b5c-5e3b60f8a348 | -9.11592 | -67.83479 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f9c5a92-ff9d-391a-aa5a-aa9a969496a9 | -9.10984 | -67.83249 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 352d950d-6bdb-3a1b-bbba-288df5ed93bf | -9.69655 | -63.20237 | 2026-09-30 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8f654ac-1d96-3d50-b415-3545bc406c1c | -9.09441 | -67.76176 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c65b1527-1c58-3caa-a167-9215241ee4a5 | -8.06456 | -61.26891 | 2026-09-30 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ea4b2ff-753a-32af-b5d9-917c45f407db | -12.78 | -54.00406 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dc733c2-ec56-3572-84b2-6425825a7726 | -9.47453 | -66.78613 | 2026-09-30 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e52ebe7-99fe-3ff9-9dd3-728bb86cbebb | -10.07248 | -63.08031 | 2026-09-30 05:38:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7998dcb6-1dd2-3cda-9213-5865de1458ea | -12.78567 | -54.00427 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b63437ca-0f36-301f-878b-48065e1ce37f | -9.08178 | -67.8161 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 666eb2a4-bb15-35ed-925b-5f603109985b | -9.17816 | -67.55676 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ae5d1cc-40f9-3499-a4da-c5e4ce5b916a | -9.12623 | -67.75714 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2b0bc62-e422-3322-84f4-160b52a9d948 | -9.16836 | -61.40707 | 2026-09-30 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2edc8a8-77d8-341e-a54f-3cd6a3252b62 | -9.12465 | -67.75811 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bf25b8b-abff-3e28-9985-c9262700831a | -12.90271 | -61.71137 | 2026-09-30 05:38:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78a9ea76-5530-3c6d-9ab2-f78bfc541534 | -8.84688 | -68.69748 | 2026-09-30 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ded57a99-febd-3fce-9ade-cbb95413c31c | -8.48499 | -54.90811 | 2026-09-30 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07db8f32-4c3e-3eac-9628-92d9d2286393 | -12.77896 | -54.01365 | 2026-09-30 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af9d193a-9ea4-3407-9119-3884cda77fa8 | -9.72001 | -67.08962 | 2026-09-30 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README61.md)

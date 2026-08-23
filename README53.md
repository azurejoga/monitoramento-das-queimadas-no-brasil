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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32a37f0f-4558-3b3e-9163-35e0969b6453 | -6.87846 | -59.40613 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e08cb54-3528-3981-acf0-8e903cdd7297 | -7.67673 | -63.35511 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d72b6001-0b42-3bba-8335-e02580c140b4 | -6.94605 | -59.08003 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1a5848c-16f5-38a7-a984-5b0c9a7f29ad | -11.20233 | -55.04854 | 2026-08-23 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0bc32b8-4d21-368b-8c1b-fea3ab693bc3 | -8.91521 | -60.71547 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d38312c6-ddc3-3c0e-8252-eea0eda2387d | -7.61017 | -60.98038 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed9c9066-444a-3011-8329-5829f1c27bf0 | -6.81108 | -59.67803 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de186d31-a3f2-353b-b55b-b9170ed9e319 | -6.11545 | -59.93253 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 618bcd2e-1cd0-31a5-bc2f-65e9ffea843c | -6.81167 | -59.67446 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96c975dc-7451-3ffb-b572-74c91e916e16 | -6.55474 | -55.09598 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9c62142-9a4e-37eb-9fe8-de719ec6f5c7 | -5.77778 | -57.57068 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 615292d0-2992-3dad-ba0c-ed9b43f54962 | -7.68606 | -50.75331 | 2026-08-23 05:04:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45aceb40-b056-333d-914e-ff7b01b52a20 | -6.91973 | -46.41141 | 2026-08-23 05:04:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2197f4ef-f886-332d-8066-9f71940864a6 | -9.65057 | -63.84029 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e025fdb7-4409-3601-8ef8-2e851ca03525 | -6.70706 | -58.72726 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e6ca062-ef49-3056-afed-e326ea0a56b5 | -6.95637 | -59.06644 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b9f9c4c-8c1a-3ffc-979a-82160488ba06 | -11.20178 | -55.05206 | 2026-08-23 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6173e820-04f8-3a37-bd26-bcd3e06709fe | -6.76309 | -58.69764 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 378d0df3-3fed-352b-9f3c-eacd5a900acb | -10.8375 | -49.39376 | 2026-08-23 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c2595da-a14f-34c8-a95e-3f7ebc074a62 | -7.48556 | -55.33083 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fbb8afe-9507-3c2d-b59b-05364ff6704a | -9.44833 | -56.90752 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b59ff81c-5b23-3196-97c6-e30fbaae4c4c | -6.68548 | -58.73845 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f71fa239-cdcd-37a8-afb3-d07b33a17669 | -6.1943 | -53.52813 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c63802d5-5928-3b3e-a8ec-9f216b0b6072 | -7.03619 | -48.02195 | 2026-08-23 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca8e91f2-aab6-3ac7-9863-245e32ce5062 | -6.37593 | -54.96009 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb04378a-08e3-3a24-b830-3f2c081d6e5e | -6.20205 | -53.52217 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfe1fb2d-6c47-3352-b77b-dfbb0296443b | -6.78177 | -59.43208 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7124ca4d-8a87-3bee-9493-d28b2d3a8a73 | -6.25448 | -55.42171 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 129ca4e3-c335-3bd1-94a6-54bd85151c93 | -6.84347 | -59.45683 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b2ac192-3a59-3760-bbbf-7d754c2a5e28 | -6.08275 | -59.96702 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a675e8a-44ad-3d41-8899-ebbeeb30ecd0 | -6.81756 | -59.66465 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a601e48-7635-3a50-b59e-09dbb73d159b | -4.15791 | -60.72998 | 2026-08-23 05:04:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f293b67b-cc7b-3cfe-834e-fb59f8d4e95d | -6.54353 | -58.52121 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e53ac5b-0718-33b8-9569-42f3f9adbbc6 | -9.1556 | -59.48372 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13516d14-4f16-3dc7-8240-76ac93e93bda | -7.58402 | -57.69305 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5870f2f6-6d3f-3841-8b5f-ce498de5821a | -6.79784 | -62.91319 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dea5eab-1e37-3d59-b571-b9b4757c32ce | -6.79927 | -59.5986 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ca07dbfa-7e5e-3aa0-b740-81106f9cf297 | -7.62434 | -61.60234 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd97422c-3c7b-32a6-8e0f-63bfbaeb7c0d | -6.74707 | -58.67555 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02e3da30-7128-329f-8775-d1eb1b830d29 | -6.67941 | -58.72761 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c64bd327-b9d2-38f8-8ef8-f70ed34fcc3c | -6.67174 | -58.72633 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 337c321e-b857-3ad7-aa3b-e7dd0cf196fd | -11.85145 | -51.67513 | 2026-08-23 05:04:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 545a75b1-7f99-3807-983b-7035cf628e9d | -8.94939 | -60.57203 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29b34c9e-3d96-3f13-99fd-701ae03dab6c | -6.672 | -58.7952 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67e0ceb0-4426-3b89-b4f8-6eab9934a805 | -6.20259 | -53.51867 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff1413c8-fcb6-3259-a955-48650fd5d657 | -6.79379 | -59.80236 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6587440f-0d51-3ff7-bed7-06e61d107a6c | -6.76617 | -58.67172 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d2e0e2c-4deb-361d-b065-a3808ca0a818 | -6.96249 | -59.07772 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85197353-6bf1-3069-b375-b467dd95368c | -8.08978 | -47.26487 | 2026-08-23 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 82086a0a-e91f-3fef-a819-c1518e8836f9 | -9.21756 | -60.77441 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72abc5c7-c46c-351b-b0f1-797ae16951c4 | -8.95219 | -60.58046 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2d98401-48b7-31db-bc03-175377ab542d | -6.11996 | -55.71042 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8fc3b5d-ed0d-3db6-8dc6-3923a6f6aa46 | -8.17817 | -54.97114 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81bb0265-9a78-3862-a5b2-1be3d841ccd3 | -6.07263 | -44.89436 | 2026-08-23 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80b34205-6a35-3bce-862a-610c51809829 | -6.18846 | -55.43269 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ef88320-0f41-3747-b2cc-878974bce537 | -9.04388 | -50.87654 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d33fe7ba-28d1-35b4-9713-7b48bf83cd4c | -6.79907 | -58.66278 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 630e97da-da8c-3f8d-a05d-e6ff84f49794 | -6.38036 | -54.97507 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2a448dd-29b0-381f-a030-ce967d9a25df | -6.54006 | -56.1754 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7e57f0a-8b63-347f-87bb-3ab35a81bb0a | -9.16064 | -59.45441 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21015f4e-08b6-334c-84bf-fe7399fbf6a1 | -11.46791 | -54.32565 | 2026-08-23 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9313a1b4-9d96-37e7-98ee-b9588b5e16f7 | -6.12451 | -59.92249 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57223467-6090-3e91-8c36-db8ce8b56d6c | -6.76618 | -58.6787 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a6d6ab1-2920-36b7-8c3b-b9b91171e5ff | -8.68919 | -54.74673 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a17307fd-025d-332e-b681-5d8af336bfdf | -6.76758 | -58.68652 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 633b4640-a02d-3798-8689-a29beb35c470 | -9.06914 | -60.43754 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37162ace-cecb-3768-a9a5-176743f61ee3 | -9.13032 | -60.92589 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6f65db0-4b94-3985-996e-518870faaebd | -6.697 | -58.74033 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1894421a-a158-39e1-af24-2e0ad404c699 | -7.01177 | -59.6009 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ae84352-7dd5-3f62-a730-1d52c7d21065 | -10.84057 | -50.97245 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 29c002ec-a602-3c32-a690-18c5c12854fe | -6.79832 | -62.9019 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0f2e233-f5d2-3136-a2ee-ae819e1c53c9 | -6.79779 | -62.90486 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 951df588-c05a-3e23-90bb-753b5bd0ce3c | -9.10781 | -61.58961 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7974da63-1847-33b4-9ae5-da1ed8c1b520 | -5.0033 | -56.13504 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4af80053-8826-3c48-bd6f-2be9cbadf7eb | -9.44773 | -56.91123 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c1a5f87-0b03-3186-9217-2b3d3750608b | -10.84621 | -50.98831 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e5d90679-773e-3f6c-b9e4-32fa18df9727 | -6.76296 | -58.69059 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2838a6d9-7041-3e3c-9670-403964da1b2a | -6.08695 | -59.96764 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 614847a7-f529-380a-a9c3-2b32c0201caf | -9.29828 | -56.92517 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e530219a-f902-396b-aebf-75ddf331e188 | -9.50947 | -60.50227 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17247def-1287-3e1f-822c-8a79b8e7e12a | -6.81286 | -58.65062 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9564e31c-b36f-3111-8e3e-a546a7f2580e | -9.10789 | -60.33756 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d115a2-c76d-3c9e-9c91-ed4c7d1b914c | -6.83947 | -59.45617 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 019fd680-4be6-3c95-97c1-91250353840d | -8.89223 | -60.54797 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e3e8719-2164-351f-b8f7-f66a1d90d292 | -11.44227 | -44.53008 | 2026-08-23 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c6bfe42-c5d7-3878-9ae9-7c02a1ed1118 | -12.22579 | -43.17227 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 897bb110-072f-3c1a-beeb-27a9405964a3 | -9.2069 | -59.79335 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9604dc12-08b0-3ad5-9a99-4346096ad912 | -8.55468 | -54.84633 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9545b7e-7666-31d0-b5bd-da663d95d36f | -6.11479 | -59.93636 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5303881-a03d-3783-9a76-69d5077ea222 | -7.59901 | -61.22904 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14755f3f-a10d-393a-b425-674b526f92a7 | -6.5405 | -56.2586 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2640e26e-7548-3ac4-a546-05c3d578fe98 | -9.21403 | -60.76972 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f882dea-cdac-3bdd-9f0a-7935788dd390 | -6.80812 | -59.42215 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 428a5265-da46-357f-a756-a960cfead1d9 | -7.73696 | -46.14524 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3eee5bec-4405-3289-bd81-c63c00d3b7a4 | -6.43159 | -54.95113 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 527765c3-5603-3ab4-b6d7-6fd7ea60de00 | -12.06403 | -50.5985 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63748590-b3a0-3057-8e52-4051fe55c8eb | -7.03174 | -48.02125 | 2026-08-23 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1acad133-e51e-35d5-8ce9-90b063be887a | -6.76695 | -58.674 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ea90581-a530-32dd-8d08-0b0cc623ee3b | -9.44474 | -51.59555 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d465d978-bd0f-39da-8934-15764afce4fb | -4.92583 | -56.13427 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README54.md)

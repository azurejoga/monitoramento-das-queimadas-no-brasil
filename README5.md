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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57421be2-7492-3766-a905-af873b08fc5d | -9.56463 | -44.60723 | 2025-12-21 04:53:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6c4a525-ac8a-377e-a481-5c28b4ed5d7e | -9.56504 | -44.60411 | 2025-12-21 04:53:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51640217-2821-3a53-8c78-8f163de57949 | -1.4554 | -53.3882 | 2025-12-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 758d50b6-ad15-35cd-894a-f8478b6f4009 | -2.60043 | -51.94956 | 2025-12-21 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70749365-e0ff-32c3-9b4a-7d0d3c3c9340 | -9.57026 | -44.60492 | 2025-12-21 04:53:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1247492-77b1-3c23-aeed-d69e2484851f | -9.56545 | -44.60101 | 2025-12-21 04:53:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 482411ba-0879-3399-9857-179387d55acc | -20.63532 | -51.68002 | 2025-12-21 04:55:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb8151cb-6640-30db-ada8-129db0240279 | -21.32586 | -55.78355 | 2025-12-21 04:55:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 219592dc-e2c9-3c67-ad12-7697044c75b6 | -9.24852 | -60.33418 | 2025-12-21 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1dd6ed04-bba9-306e-8f42-7d5beb7dcd66 | -21.20483 | -56.93104 | 2025-12-21 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81c7aee6-f0bc-3b6a-862b-ed009df24b70 | -20.63915 | -51.68058 | 2025-12-21 04:55:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14681a1a-8ddf-3b29-b4cf-1d38f59594ed | -9.24771 | -60.33883 | 2025-12-21 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 434b3420-f2e1-3266-9bbe-a681b7769f9c | -20.63702 | -51.67877 | 2025-12-21 04:55:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86e5052f-49b5-3109-9e97-285793eb5e41 | -9.72064 | -60.20566 | 2025-12-21 04:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8baf5640-1d4d-3a6a-99f6-d69147281e1a | -9.72145 | -60.20116 | 2025-12-21 04:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ddc0c023-46d2-36f3-b5eb-04fdb6c69779 | -9.24849 | -60.33713 | 2025-12-21 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 05c0dc72-0eb6-3669-b824-4f7fd1f73a5d | -9.71888 | -60.20232 | 2025-12-21 04:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 16cc551a-149d-3a22-934f-d65e6f950401 | -21.54124 | -57.53389 | 2025-12-21 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d960f39a-9d56-381e-91cb-fbd8fe40ef4b | -25.47138 | -51.29041 | 2025-12-21 04:57:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7c6c56a-67c0-31e2-b2a1-00f09ea17667 | -29.22562 | -50.88425 | 2025-12-21 04:57:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7df31254-6fa4-3972-a761-5d134209e99e | -9.4648 | -57.8449 | 2025-12-21 05:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8ca05382-cfa1-31a8-bfcc-d5278440d6f2 | 3.3751 | -60.13542 | 2025-12-21 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a02c0ae7-20b4-3308-a374-ddc7e8225887 | 3.37445 | -60.13132 | 2025-12-21 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed9ca710-3063-3f48-8095-edd40fa1d1ea | 4.00878 | -59.9924 | 2025-12-21 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99261a3d-f43b-36a9-816f-e9aede83600e | 2.70947 | -60.96479 | 2025-12-21 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56b20ec9-76e0-3a20-8228-c419f29d841a | 3.50845 | -60.88542 | 2025-12-21 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42aa00f3-3e2a-3a3c-9ee4-e69ec8f768cb | 3.31574 | -60.67163 | 2025-12-21 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 456e0500-e967-3718-a8d0-68e11cde7e9d | 1.33337 | -60.72675 | 2025-12-21 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 074ebb1f-b19c-33f7-aa52-152c69d3e8b3 | 3.60717 | -60.22621 | 2025-12-21 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9adfa6f-6446-3e0d-94dd-e385ae5e5986 | 3.50153 | -60.88651 | 2025-12-21 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ef9fb56-9eb8-3787-96be-e7e8bc7d2750 | 3.50438 | -60.88216 | 2025-12-21 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 679f71b9-4925-3cd8-83b3-50bc973e2250 | 3.38814 | -60.12495 | 2025-12-21 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1605d77-afe2-3f73-81ed-1da45dab7e3e | 3.49521 | -60.89139 | 2025-12-21 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7453435e-df30-3084-8ad3-52a085a4b75d | 3.49746 | -60.88324 | 2025-12-21 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 180e8127-8eec-30b1-aa9a-870433067409 | 3.37803 | -60.13074 | 2025-12-21 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab38652b-220b-3cbf-8aac-4e9d019c154c | 3.49867 | -60.89086 | 2025-12-21 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75f7c77f-18cb-3a6f-b75c-e111ff30cdad | 3.23893 | -60.53412 | 2025-12-21 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7c64764-7416-3609-a0d2-928cd059e20e | 3.50499 | -60.88597 | 2025-12-21 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d3fdabf-eb88-3b12-8cb5-13bdf020524f | 3.37869 | -60.13484 | 2025-12-21 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcb5306b-2adc-32fd-9d1b-f107a362f437 | 3.39172 | -60.12439 | 2025-12-21 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b0c9fc6-6bd2-33bc-8f55-a7b0f077cb10 | 3.49807 | -60.88705 | 2025-12-21 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09d16e2a-ee84-3d17-82c2-4dba5e0e50c8 | 3.20423 | -60.70021 | 2025-12-21 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a47f8587-0803-3f82-a8d4-3cb6d1694517 | 3.3878 | -60.14598 | 2025-12-21 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f8396a5-cd5c-3e87-9178-47fe9230e2c5 | 4.00459 | -59.98921 | 2025-12-21 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d41ff8e-836d-339d-8402-2adb256422e4 | -9.2683 | -64.50695 | 2025-12-21 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff9659e-ed1a-38cf-87ed-35e7ce06097a | -10.62251 | -65.3102 | 2025-12-21 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b74f4bce-7558-3de0-b041-37e43c9b5642 | -9.46697 | -57.8467 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 615a5dab-3970-3d23-968c-a5e02f3135ff | -9.46275 | -57.84032 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d3043d1-729d-39b3-8dd3-be58f1c357ca | -9.24817 | -60.33817 | 2025-12-21 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d7f61fa4-5bc4-312d-acfa-ec473e301b48 | -9.35906 | -64.44269 | 2025-12-21 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d05e507b-452b-3b79-912c-541aa9284cef | -9.46227 | -57.84601 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 841a9c64-c5e3-3d04-832a-755a5e74b377 | -9.4619 | -57.84885 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd7f66b1-ac9c-332a-836b-76144039edcc | -9.46197 | -57.84603 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2cf99585-16d0-353d-8ebf-f3152e9c5f41 | -9.46314 | -57.83745 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bf74989-dea9-31d6-add3-e74313a9615b | -9.46158 | -57.84886 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d840e38e-522e-367f-a44e-efe785686e1f | -9.46236 | -57.84318 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3be1cd0-7b5d-372f-96ce-776c9f0becfc | -9.46263 | -57.84314 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d3df7d1-f889-3067-9680-31d2dc60bb0b | -9.45776 | -57.83952 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05816ad0-11f9-3314-a00b-309bdf51ce97 | -9.46727 | -57.84668 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 665384e9-f9f1-355b-abe6-fff987e95d16 | -9.46814 | -57.83815 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc7418b0-e004-3be4-b4d6-8f37c2ca4765 | -9.46775 | -57.841 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79548cd7-4d21-3a54-9076-eba7683f818f | -9.4612 | -57.8517 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 927e293b-eed2-3074-a0c4-8ed85e66834e | -9.46393 | -57.83163 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b836480-2211-361c-b65c-98cd5d0572ae | -9.47228 | -57.84732 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 361d53b0-ba55-3c4f-8a23-9bbffdc5be5a | -9.45659 | -57.84812 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b13ab2e-fdf3-3c83-9e8d-a5b145472883 | -9.463 | -57.84028 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12e2b393-3176-33fe-890d-af6f8c332384 | -9.24871 | -60.33423 | 2025-12-21 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 7c4fd6a2-bf9e-3e04-a07d-348b9f80ca9e | -9.45698 | -57.84525 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9852e5e7-f5cb-3c16-8145-502166ab28c2 | -9.46337 | -57.8374 | 2025-12-21 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9899528-8e3e-32ed-a7ff-221d7fe53916 | -6.7247 | -63.07169 | 2025-12-21 05:44:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89907de7-8e54-3417-bb2d-65ab4465c7ff | -21.5399 | -57.53454 | 2025-12-21 05:46:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed6e2754-6c62-3831-b1cf-369aa1a7920a | -9.4648 | -57.8449 | 2025-12-21 05:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 76fcf4bb-5201-3ee7-8f0d-cefc65826b4c | -9.4835 | -57.8438 | 2025-12-21 05:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 954e45ad-b3d2-304c-ad97-5a5a9b908d2e | -9.465 | -57.8252 | 2025-12-21 05:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 05905bc4-74d9-3538-a75c-1b806c32030a | -9.4835 | -57.8438 | 2025-12-21 06:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 01efbb83-2f9b-3cb5-a297-5bf00667597a | -9.4648 | -57.8449 | 2025-12-21 06:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 27edf0da-0238-31b6-a270-b453ece026e5 | -9.465 | -57.8252 | 2025-12-21 06:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| e1016ab9-1b4c-3b10-a19f-ffd6b0d44758 | 3.50104 | -60.89108 | 2025-12-21 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bff072eb-bb78-30b3-a533-61d66abc197a | 3.49945 | -60.88176 | 2025-12-21 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3fb3650-fb17-3f96-abb8-6ad520fde638 | 3.37771 | -60.13548 | 2025-12-21 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eb45ed1-cefe-34a4-903a-4aacd25512f8 | 3.50568 | -60.88716 | 2025-12-21 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afb52cac-f9aa-3474-964e-f6e88df84f3a | 2.72137 | -60.39505 | 2025-12-21 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6785022-de1e-318d-8287-a2cda1624727 | 3.49998 | -60.88489 | 2025-12-21 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2633c0fc-4517-3973-9050-221acd03ecab | 2.72194 | -60.39849 | 2025-12-21 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbb68833-084d-3e29-94e9-e93bb8a41a3e | 3.37712 | -60.132 | 2025-12-21 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e3281d1-006c-399c-a11b-888b8eec130f | 3.50516 | -60.88406 | 2025-12-21 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d962908-8554-39d4-b9c2-b79631aac25e | 3.49586 | -60.8919 | 2025-12-21 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1287e214-169f-35ba-80d3-45ed77f05346 | 3.50051 | -60.88801 | 2025-12-21 06:09:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef0ec525-e6c2-354f-9960-12f0cb7356f1 | 2.7208 | -60.39161 | 2025-12-21 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3393bd4-adf5-34c3-8a38-1d695c0f0759 | -9.4648 | -57.8449 | 2025-12-21 06:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 764bca2c-fc69-381e-a276-b705fba55405 | -21.54184 | -57.53009 | 2025-12-21 06:31:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 65d4d626-60ff-3361-a495-726b2bfbfe0a | -20.58409 | -54.13464 | 2025-12-21 12:40:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cb1980db-3dd4-3b6e-b6ce-d512c06a610f | -18.32407 | -46.60574 | 2025-12-21 12:40:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 259e44f5-85e3-34ba-9197-ba6b77bc15a5 | -19.81527 | -54.74266 | 2025-12-21 12:40:00 | TERRA_M-T | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0e74cb9d-ddcd-36ff-9dcb-8b2004ca84fa | -19.35826 | -52.61843 | 2025-12-21 12:40:00 | TERRA_M-T | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d327ece-81a4-323b-9fda-a06b9b2d6449 | -20.70377 | -49.16493 | 2025-12-21 12:40:00 | TERRA_M-T | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 91895022-db33-3927-9ed8-c3a119fba334 | -24.33229 | -50.62573 | 2025-12-21 12:40:00 | TERRA_M-T | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 3f91be08-7b43-3d0c-a8db-bf1dd488d7a1 | -25.45559 | -49.52896 | 2025-12-21 12:40:00 | TERRA_M-T | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 94c1ac51-1115-33fd-9f26-43a9ad6709ca | -18.79777 | -52.61992 | 2025-12-21 12:40:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c5848578-69e9-3923-a8a6-bc4a45dedd4e | -19.15372 | -52.94359 | 2025-12-21 12:40:00 | TERRA_M-T | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README6.md)

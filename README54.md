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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 908b0495-7127-34a4-9cc7-4c2dde00f45c | -9.4202 | -60.53808 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57e6d857-44fc-3132-b1c6-9045c59611ed | -7.44419 | -57.62773 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec0a9f67-b145-3653-bfad-b2cb5eebc423 | -8.90963 | -60.77415 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c12a85c8-ee18-3a46-b1c7-c2c62a81f420 | -9.23671 | -60.92196 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 466e7676-a1b4-37cb-bfe8-5a48c29105be | -9.65154 | -59.62759 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd1c640a-f53b-3708-bf60-1726f7a211f3 | -8.88625 | -60.7704 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7d1281f-d271-3ab1-8ee5-24f80d98a7f8 | -9.02945 | -65.73245 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d23f5c23-6733-340a-a8fb-598b94b6b47b | -11.81089 | -46.80173 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbcd3db7-6d74-369b-9621-44bfb3b47760 | -9.39918 | -60.52031 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28c6c5ff-9c5a-3fcf-baad-05c273779508 | -9.4191 | -60.52349 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94edc124-2645-34a9-a4d9-b835544e51a6 | -8.96523 | -62.14461 | 2025-08-27 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e8c6c6d-2fa1-3f11-8df3-f8b024cb9ac8 | -10.08432 | -62.90767 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2daf8448-7a03-3bdf-a1f3-242b08f09956 | -11.81476 | -46.82298 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48b17863-0619-3275-a866-304a234e2964 | -9.04728 | -65.73117 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97aa8602-1026-38a4-a4fc-d3882e0d38cd | -11.81866 | -46.79546 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38ae52a9-ade6-3416-b6e9-a7bded67abf5 | -12.88293 | -48.10785 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6e0f5b25-cad2-3730-a296-e027000fcf97 | -6.82646 | -58.96591 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bb79d83-0419-323f-bbd0-7d84562ae604 | -7.04989 | -59.82098 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d1fe863-7ba8-3661-a3ef-3bd690d7cc07 | -8.34892 | -62.93242 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6940c40a-f549-3560-8a80-ae5e9a15e240 | -8.68911 | -62.87213 | 2025-08-27 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d280f43f-643a-3afb-8be2-08c600f7808a | -9.41135 | -60.52946 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9b414e83-9337-3cef-88a8-7741c8c07ef2 | -9.32963 | -63.20136 | 2025-08-27 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19bfbb22-8f4d-334b-b68f-0839fb808e2a | -10.41915 | -57.69486 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 849b0e64-16d1-3c8c-a605-9779673e3219 | -9.40304 | -60.53894 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8a44626b-4d2b-33e7-9146-0733bf0e77b5 | -9.40582 | -60.52137 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 62c3dd16-4e7c-3dc1-9df3-d21d4aa52b87 | -6.87728 | -59.81451 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cebf9787-6523-37b4-8d7a-21da1ae0afe2 | -8.88447 | -62.45635 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41aca758-1bbd-3c63-8cc9-09b90b21d595 | -7.43414 | -60.61776 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85ce0321-8097-3f5c-9b8a-052484ab6fc5 | -12.77123 | -48.16648 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| da45eda5-1fc1-3d5b-947e-7e8f02dcf79c | -9.18184 | -59.45673 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de25a4bc-12eb-37dd-b377-d633f6342fbf | -6.24032 | -60.01371 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0e6b1c1-a366-33f2-bbe1-51e0c7384d15 | -6.71211 | -58.56471 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38d6cbfa-42cc-34c2-a517-e46418278381 | -9.41632 | -60.54106 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4295ada1-88cb-3e44-bef5-7a1d831ee635 | -9.081 | -49.57865 | 2025-08-27 05:18:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 353275dd-18cb-326b-80cf-3fa828d13abe | -5.53222 | -60.20935 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ebe447b-44e8-3e6c-b064-f207fbabb67c | -9.15743 | -59.59186 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93411483-8a15-3be4-82cd-92078caa615c | -9.10494 | -60.31479 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba868f6f-b160-3bb9-a105-b3ba880a092b | -9.28224 | -56.91296 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4f5bca2-d654-35ee-b811-bf7c0242ce44 | -9.61766 | -62.2607 | 2025-08-27 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8952559a-dc3f-302d-a3ad-4031fc3f7b81 | -10.41472 | -57.71042 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40475821-fecf-32e3-982d-6ee5e7571246 | -9.16506 | -59.56456 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 51e02ce3-f429-3c93-9ed6-69b088389b6d | -9.47548 | -57.82513 | 2025-08-27 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2783183a-cb3a-32eb-9739-766622439a2b | -6.78679 | -59.67583 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11f76aa6-0341-33aa-9f4c-104dfb05627f | -8.55139 | -63.94075 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1302527c-76ba-33c7-85f7-fe6f47bb72cd | -7.25949 | -57.68588 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da0a2dc-41dd-36fc-a86f-a9f2ac96f294 | -6.68955 | -58.86318 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 996a03e6-c8b1-3625-96cd-777f735cc653 | -9.09387 | -49.56847 | 2025-08-27 05:18:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e16873a-0188-37e8-8b67-fb3ecb141d8d | -9.15797 | -59.58838 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5505bfbd-7425-3277-ba62-ec010ea01558 | -7.3824 | -64.36427 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee9d1336-d162-34d0-b7de-b749721de22d | -9.40196 | -60.50276 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3ae387d5-678a-3a27-b490-e870c28a2302 | -6.78402 | -59.67184 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f397b93-5bb0-340e-b281-44647960fe2f | -5.96346 | -61.76072 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2f54276-7706-3390-b676-d4a3c51f0d7a | -7.25554 | -57.68899 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdf282e5-ce58-31e8-9261-1f7c0d379743 | -9.18034 | -59.51 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60b9efa3-4b1e-3320-899f-f18c2e2f11ad | -9.02025 | -65.68493 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86439454-0d57-3d9c-bea2-46526156343b | -9.16723 | -59.55065 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c3a7149-5b08-3bef-8f8a-1e8375a5905d | -6.35948 | -55.80355 | 2025-08-27 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dca642ce-c223-3c82-ab87-5357e209ed9c | -12.74775 | -48.2007 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d71ad0cd-15a1-31fc-866c-2d481a68f761 | -6.70879 | -58.56419 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d3e9e77-aaee-30ed-b50b-0a43766f48ec | -9.40749 | -60.51084 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 897e7031-f1a7-3f80-bf4d-7d309ead8971 | -9.62114 | -62.26127 | 2025-08-27 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20163171-227e-3aec-a8f6-56da72595c59 | -8.65217 | -67.26843 | 2025-08-27 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a9011be9-b2c5-3c44-a7b3-694d9feda8db | -9.21871 | -59.65496 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 331eafc7-c32b-3033-8c37-c6f9f74c74dc | -8.73085 | -49.73988 | 2025-08-27 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bde9afde-0f28-3af8-bde8-008634b19efc | -6.26432 | -60.0104 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5392f3e-2ba1-32fc-bc96-48f91314f227 | -9.17116 | -59.45801 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62adeb5f-62a0-314b-b404-f43d12483e34 | -7.37897 | -64.36008 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cf7de33-cf3b-31e2-be4c-244ed8bb3ca4 | -12.77186 | -48.16063 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b4fadf57-3c40-37df-8c1b-e912d9314b63 | -8.84914 | -62.45054 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc22aec-e2dd-3327-be89-e6e822316429 | -11.53269 | -56.42269 | 2025-08-27 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b51c7f49-6fb4-36ca-b2d6-4e391b6a370a | -6.25141 | -60.00826 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73ffce0e-7288-3011-9672-b5c084270f41 | -9.34424 | -59.63547 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b84a5b4f-d095-3c0b-b723-fb758acb907f | -6.56656 | -60.05853 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ce9fa7b-6656-3c6d-aa8b-f202e060c5da | -6.71157 | -58.56819 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f65b99ce-f0f7-3845-a4a6-478c2fcc1bbc | -7.35969 | -59.66714 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16e854c4-b576-324b-9aff-9f1cd3e4a757 | -12.74146 | -48.19552 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8a50fb8d-593e-3686-85fd-f2fc3d2fe1d8 | -8.90074 | -60.76543 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a051da61-ae65-3314-9107-3be2a6ff8f45 | -6.95093 | -60.08015 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f671523e-9665-3ac6-87ce-b963a6397912 | -10.77286 | -60.78286 | 2025-08-27 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0146d20c-954c-3fb4-a69e-128eead22831 | -8.88893 | -62.47356 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e04344f4-b379-3fbb-b790-efd10121e37e | -6.62916 | -58.5518 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9793429-4405-3efa-aa15-800c8c2a1a04 | -7.35638 | -59.66663 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 262de36b-7bc1-38ab-8e3b-c722324dba29 | -6.68876 | -58.53969 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 782de80e-3950-3d69-ae77-9a411a926e0c | -6.83415 | -58.96002 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c52c882-5504-350d-9472-759c8899f62e | -6.81431 | -58.95694 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c859f39c-eb22-3396-850c-6b17864eca35 | -8.69272 | -47.19967 | 2025-08-27 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6996916d-ff4c-33d8-81dd-b73819c4202d | -11.13849 | -46.34196 | 2025-08-27 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| de838abe-6539-3c63-bca7-692608b760e8 | -9.26212 | -56.90152 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 698c8c7b-3aa6-39ee-84af-82f0d04eeb28 | -9.41412 | -60.5119 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7bab7ef5-52eb-353c-b27d-05cf2268e8b6 | -12.70368 | -48.18155 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 42f06a82-6967-3f1a-b844-6e01affc8b1f | -9.1055 | -60.31129 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f76d2cd-6f47-399e-afb1-7a87c5a1e6fc | -9.07498 | -66.06551 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b64172df-bb76-3305-8a45-f88de1e6dc9b | -8.12338 | -62.86676 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8975d383-c18c-33e5-94e1-d17f23e94cb6 | -9.13109 | -60.72994 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af380aa4-3e11-358e-8a2a-264dcdc4b6f5 | -7.27246 | -57.66919 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ae7615e-4aa5-394f-a4ad-041c56685f95 | -8.90408 | -60.76596 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9d572b-c784-34cd-87db-18f7d6d53b71 | -8.06828 | -61.5515 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c30f313f-2b71-3caf-a8bb-848e4bd43061 | -6.82538 | -58.97283 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43da4e46-6ab3-35ac-b378-a5cd80cb03da | -9.18918 | -59.51851 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 301ca58e-b20b-37cf-ab8e-b77b8af57d5f | -8.91258 | -60.71273 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README55.md)

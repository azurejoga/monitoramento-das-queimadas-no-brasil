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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cd48911-ab17-3b09-b100-7a74522639d7 | -8.91112 | -62.41357 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 193606d6-2ea1-3bfa-a08a-d69b3a17914c | -8.50778 | -63.87665 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3d5f0a91-7db5-3371-8661-3ea95a99cce4 | -9.02595 | -65.71393 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3e38f1a-e741-391d-9f1a-624ccb6cc327 | -8.89244 | -68.6964 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99b7bec0-a44e-3f97-8772-3587ce068a06 | -9.81802 | -64.28044 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c16429db-e0db-3e86-a79d-2d910e093c85 | -8.49554 | -63.8748 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d9525710-a64e-3b65-95c5-425a0a8973f9 | -7.91249 | -63.07194 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e5de3b45-c674-3627-afba-c4c0439dfd7d | -6.7944 | -58.64488 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eaf00325-5c47-3ae3-86c0-ec9720793ad6 | -8.22719 | -61.42498 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fc8b7f3-44b0-3420-9921-f7b2b60349f5 | -10.10214 | -65.28304 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bb02369-e4e4-322b-b70f-3ed6444a8141 | -10.41321 | -64.39438 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba00b825-2c95-3c1e-ba05-474f3766ae27 | -9.0181 | -65.69047 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 427a80eb-0003-3480-af3a-3c93b63b6231 | -9.20143 | -60.83496 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 800fb33a-6528-3345-91d7-c8b378a7a368 | -9.02659 | -65.70959 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca5dba52-0d52-3cfc-aacc-7f5394a5faf1 | -9.8001 | -61.20766 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddce3ba8-d818-3ce6-9985-3e8a33d8a76d | -9.2541 | -60.48196 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9201bbb4-4ba3-38b5-9525-0690ffb13e0d | -8.98193 | -63.07978 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73c61b91-fa9b-3534-aa64-a9f262512737 | -10.2584 | -59.1106 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53b3fbfd-eafd-3d95-aa47-e9e6464c5752 | -9.18694 | -59.46284 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5e867b07-cd85-3782-86fd-19386b18ab30 | -8.17085 | -62.77353 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfa1cdb9-ca12-32da-908c-e98768bffbdd | -8.87131 | -62.45749 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f39e768d-70e0-36fb-b677-b794ed4653e6 | -5.79823 | -59.22437 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eaebda7-eca7-3f6e-a41e-1ffb64624fe8 | -8.57776 | -62.62555 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 447db5fb-f753-38f9-8f7e-0afde5ea5266 | -7.91192 | -63.07598 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ace15611-ffdb-34a3-bbd1-b6ae55bbe7f3 | -9.0015 | -65.3996 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6bf8148d-bcc8-3d8b-9e99-854d8f02f237 | -8.9494 | -62.13372 | 2025-08-25 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 114b3e11-c9c8-3359-8653-efa2722d0279 | -9.82466 | -64.26302 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04d16ecf-88ca-3ca8-b074-e2bb94ff7ad5 | -10.40966 | -64.39017 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dc98c025-4fff-383e-ac38-119769359d49 | -8.9771 | -65.40977 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1eff89a5-8304-39f9-8f70-75d13de35993 | -7.73174 | -67.0674 | 2025-08-25 05:55:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c0370a0-3cb4-3228-bd96-16da0b3d89e4 | -9.20224 | -59.47038 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7c6468a-3f10-396c-9f20-fdb8a214fee0 | -10.45717 | -59.12973 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e386b34b-534c-3422-8396-20826f515bc4 | -6.6347 | -58.54805 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6c0ad6d-499e-3b8d-af92-3b5c2a175351 | -7.72776 | -67.07058 | 2025-08-25 05:55:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb6cf41d-a441-3b84-a346-0f8e02f9f50d | -9.81353 | -64.25403 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5533536c-8a59-3134-be28-7e8f087ab470 | -9.81751 | -64.28402 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cfbc018-ed68-3e89-81bc-c231d61aa654 | -8.682 | -62.87821 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc0f3261-d1cc-3af6-8ba8-079c75a7079c | -6.91577 | -63.00183 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e99b4eb9-82dd-3a52-88ae-aef1955345ee | -6.63101 | -58.5471 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24028e95-a907-325e-bc18-f820bad4510f | -6.82566 | -58.94876 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51daf5c7-6740-39ab-aef2-6fcf7db00fd4 | -6.63153 | -58.54314 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c95f9de-cef2-3860-9811-fe15828834cb | -9.16228 | -59.47822 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2732885d-d55c-3559-a13c-c4d0f37e9ac8 | -12.22307 | -64.23505 | 2025-08-25 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fd52291-dc2e-3b69-8387-0049da51dacc | -9.82112 | -64.25884 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f196a12-0746-3846-882a-57ef47e55d4e | -6.82416 | -58.95998 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40e9ec89-c1ef-36e5-96ab-10d9a8dcd32c | -7.55885 | -63.85418 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d639c0b-3f2e-3db2-9fc2-e82d41799783 | -8.88806 | -62.40373 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32bfab17-a226-39d4-8947-af417f591053 | -9.17804 | -60.8165 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2dbdc68-d8e6-32e2-9edc-fce882bdb892 | -7.55381 | -63.86066 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 693c7ad8-f535-3928-a5f2-3dfecab2bccf | -8.87454 | -62.46728 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c71db31c-9e9d-3c9f-aa34-6e0558cb67ea | -5.79331 | -59.2201 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4806a6ac-e3e6-348e-9864-ef9573eb0da1 | -8.47116 | -63.9306 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ebbec46-65e7-3cbd-9704-afbe39bf5167 | -8.21707 | -61.39125 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e978b9e4-f0b1-3337-8d70-95584dae3caa | -8.63109 | -62.63327 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cccee96a-21af-3300-8e55-000f939e9df1 | -9.07067 | -65.71632 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fedc23f-857f-3afc-bdf3-94da2ad3a1fb | -9.96692 | -60.18105 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0233a2b0-ebfc-36bb-bc62-806cfedccd1a | -9.03937 | -65.72484 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daf52051-a482-320d-887c-4f4e15bc75f3 | -8.6571 | -63.42667 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f70140d2-6867-370b-b1b2-f5eda8f191d2 | -9.20154 | -59.60905 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fc0045e-c970-3674-b445-4e610e234c0a | -9.19547 | -59.44127 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed4096ae-c47b-3ec2-bcd4-98ffa173544e | -6.69156 | -58.85571 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85306fcb-24b9-3a1d-bb75-03d228dbceda | -8.99071 | -65.42103 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3c492511-4064-3595-801e-94869cc29ac8 | -6.82366 | -58.9637 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96b10a62-fe05-3c7f-95db-66bf95f6aa41 | -7.6211 | -62.71952 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11becdad-bd36-3616-98af-c478e16f0a50 | -8.12552 | -62.87457 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9963c62b-5f4f-379b-95c9-c5b8028e9d63 | -8.68756 | -62.87033 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9faac849-5224-3527-9ecc-98ab36e08166 | -9.09549 | -65.72227 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6cf5b924-a93d-3228-bb44-4fd8b966e70b | -9.20357 | -59.50458 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a99fe04d-8d85-3953-a93c-f1f95de3189a | -9.36032 | -67.5651 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bba73832-412e-3bed-907d-d18128cf0c25 | -12.05468 | -63.15181 | 2025-08-25 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b11f654-4c1d-351b-bcab-a14e97b43b8a | -9.10606 | -61.42853 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80105806-1605-3bce-a52b-4ad728d044af | -9.16631 | -60.82703 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b82e2773-e35d-384e-afe1-2cf3ace63ce3 | -8.69691 | -63.83603 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f2189b9-6270-3b06-8fa8-edde395f0bac | -8.22529 | -61.40302 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e7236e-2885-3929-a2ad-f59b779e6194 | -9.14325 | -60.76591 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eefd8532-cb4a-3e0c-938e-65c0f57f9f6c | -9.26521 | -59.77178 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e250319d-d3de-300a-b7fc-583e84394257 | -9.19802 | -59.50385 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8f283db-087c-383b-b325-1d5159972f8c | -8.87646 | -62.45356 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 41d12903-e4fc-3b77-aa24-4c1c4e267691 | -7.54777 | -63.84531 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3274f9e1-8df1-30c7-9274-85e235f42e91 | -10.41017 | -64.38657 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f32e2b34-008c-39b5-8060-1822016145f9 | -6.79493 | -58.64102 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffcb76ea-c1cc-3b16-9fa9-a941bf6169e8 | -9.19854 | -59.45474 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 828d5727-b3e5-3fb0-a91b-5d74df17e989 | -10.24477 | -59.6624 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d559a53-d94f-3d4e-9b2b-af4718b1b366 | -9.88049 | -64.28224 | 2025-08-25 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aa364e5-8986-3be3-9d48-809cb6d797d3 | -6.62846 | -58.55107 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c52ab8c2-41cd-3ee2-a0e6-62cc1abc8914 | -9.21194 | -59.70215 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a163f49f-63f2-3f1d-8f4f-d68e27f08aac | -8.12611 | -62.8704 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a53063aa-e646-3d21-9ecd-9c5deebe7422 | -7.47363 | -45.02054 | 2025-08-25 05:57:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3e1d9264-393b-338d-b279-45ae0a835c3d | -5.29702 | -45.26151 | 2025-08-25 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a2bb0212-6a66-33d4-897b-3e1951e2ea69 | -5.11233 | -43.19963 | 2025-08-25 05:57:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| ce5533bc-46db-3ec0-82e6-13b93857b4ee | -14.2275 | -58.6249 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99519e92-0635-3088-a56a-944814d72c56 | -14.26436 | -58.6147 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deff9eda-055b-370f-826a-0b36ff7f56c6 | -15.15137 | -59.59872 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a986ca2-af50-3ba6-9814-087382045a0a | -6.89781 | -47.92873 | 2025-08-25 05:57:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 29afcf0b-014d-36a8-a423-6aab315cfdf9 | -15.14682 | -59.58455 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c3cf4e41-a03f-34f4-b712-645420c0f21b | -15.14635 | -59.58903 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b2accad0-4e30-3488-a74b-04bbd2ba6c67 | -14.42548 | -56.47191 | 2025-08-25 05:57:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| df374bd8-3941-3132-bc8a-09cde0bd06de | -3.43638 | -49.03998 | 2025-08-25 05:57:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fbd4a624-472c-32b2-9e63-868274d2aac9 | -7.58746 | -45.23667 | 2025-08-25 05:57:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 49818882-7b2f-3bc0-9bb0-2a1efa7452f1 | -14.43331 | -56.46529 | 2025-08-25 05:57:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README88.md)

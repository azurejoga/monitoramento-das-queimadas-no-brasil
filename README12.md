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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f8e6c6c-887b-33ad-80fe-b6f1d15d063a | -2.047 | -56.872601 | 2026-10-02 01:12:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2d8077-f6a4-3d33-bdf0-38ba82cc5266 | -6.6694 | -55.0933 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6adfe694-4b01-393b-b283-1c6b61b86afb | -3.1249 | -53.7472 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d57209-d10c-39e5-8267-073faf9b2f3f | -13.3609 | -43.8955 | 2026-10-02 01:12:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6251e6bb-f4d4-3e8b-a1ee-28b16b251ec2 | -10.7987 | -53.7672 | 2026-10-02 01:12:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9cec1a6-62a9-3622-bca1-9bc9e077343b | -10.4185 | -53.775902 | 2026-10-02 01:12:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2afd234-27f2-30be-9fe4-bb97e101855c | -3.1346 | -53.744999 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53582c40-bef3-3b25-ab4d-48e8687854ac | -5.9704 | -55.370701 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db37ce94-d1eb-3d37-ba3e-1810d447f0b3 | -7.4703 | -54.986401 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d81e85ae-800e-3e05-a74f-718539a0bdef | -7.7265 | -54.801701 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52fd1608-7842-34e1-8e48-6d8005e86230 | -3.0234 | -53.973701 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd2fd508-e040-37c1-911a-a59b0226ce76 | -12.5294 | -43.100498 | 2026-10-02 01:12:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 33b09f7a-12cc-3277-b781-df75b1d6e16f | -9.8544 | -44.855598 | 2026-10-02 01:12:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d28d1cc-daf7-34c8-b980-26123b24ada0 | -8.0878 | -54.889999 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e57dd07b-7cdc-3a27-b407-d72736494bc8 | -5.8564 | -53.4795 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90f43572-e6a2-3921-a357-864166c73945 | -11.4633 | -43.445801 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5500f62-c298-3494-9d9c-4459e8f9a2b6 | -8.1575 | -54.8349 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7466ef15-b3c8-3b91-ba08-c60f21688264 | 1.8102 | -55.607201 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55156f4d-68ee-391e-b56c-f5c6759fa24a | -7.5607 | -55.019901 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bb29db4-7c32-3ae9-bfec-6a0831d35884 | -11.4659 | -47.4814 | 2026-10-02 01:12:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9af64ab9-fb14-3fac-b29e-69ef8f745412 | -7.6378 | -55.040798 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4e63e2-a210-356c-bc66-a5d46047bb3c | -3.2823 | -53.847099 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c535a36-b72b-3010-b11f-31b96e10f5e8 | -5.9802 | -55.3685 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61160df5-06a5-312b-9e35-80a57eb8e622 | -4.3086 | -49.102001 | 2026-10-02 01:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 832f16e2-c15d-3401-94d7-7acc5e5ac310 | -7.0899 | -55.480801 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99a90626-8c84-3bf9-b55b-3462a688c25e | -4.2765 | -50.7495 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f43a0f3d-ccb9-390e-9f7f-3cbd12c11dd6 | -10.4313 | -53.8302 | 2026-10-02 01:12:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1f3e856-ce25-36e2-81b6-87d15030f25f | -7.5492 | -55.014801 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5afa57b-bb9c-3552-ac6c-75dd17b47662 | 1.8199 | -55.5648 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23575752-8d9e-3295-a5b3-48f2b0878873 | -5.8684 | -53.486198 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73e4091c-cfb4-3231-89e4-231a544564fa | -6.666 | -55.078499 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d12f781-839a-32c6-9bc1-b0b0abbd37bc | -3.139 | -53.763599 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a0bc4fc-8ea7-3a01-bab3-398b51da2bca | -5.9819 | -55.375801 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5acf336-b89e-3ebc-a80e-2c5654b57510 | -7.8825 | -54.7183 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2d931eb-b930-36e2-8ddc-8f2f46554b83 | -13.0402 | -51.3004 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de3d82d1-22de-3a53-b3c9-4b72a3ea92da | -5.3722 | -56.038898 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8dec136-dd1c-34be-85bb-c9c27c37a9ca | -7.4997 | -54.979599 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef76c961-17f8-35f2-80d7-56dd90d71bda | -7.2816 | -55.595001 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 487ac8d6-de9c-384b-910d-300e8ee6b87d | -8.2649 | -55.6968 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b5a5114-853c-3577-b114-59419d48ec80 | -8.2629 | -54.7556 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9c79a99-5264-375a-88c7-f9416078b27b | -2.9887 | -51.0378 | 2026-10-02 01:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f395e0-aabe-3f86-947e-41e75a780002 | -9.5096 | -45.334702 | 2026-10-02 01:12:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a9ed702c-4c8e-37b5-a261-4de25a7b99f0 | -6.2655 | -55.4417 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88a33ace-ff3c-33a9-96b5-5c1421e5080f | 1.8024 | -55.5966 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d97906-f4a3-3e10-9aaf-a0c7680d8637 | -13.3338 | -43.872299 | 2026-10-02 01:12:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d158ca14-9cdb-327a-a300-39d4850f3f1b | -7.495 | -55.004002 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42082579-d613-36de-92ec-8d88ac4156c3 | -4.306 | -50.786499 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f7643bb-f364-381c-9639-cb0675ad5116 | -11.7844 | -43.565201 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b21960f-272b-3c23-9706-52b9dfbd1d08 | -6.796 | -55.548302 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e0e530-b264-3c16-8c46-c2b356772145 | -7.3239 | -55.244202 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da56c5b6-d024-34f2-9948-7a15c27d56c4 | -6.0293 | -57.684101 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe50daa-0acd-39f5-9350-28a9e4feb451 | -4.0268 | -48.955799 | 2026-10-02 01:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdec559d-eeae-3cab-b2c0-1c91890d3aa9 | -3.1466 | -53.751999 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72dec0ea-b147-3954-8fa2-252d468b437f | -0.3759 | -51.7561 | 2026-10-02 01:12:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 264f5fd2-4270-34a2-8c14-734fdae9b87e | -7.3404 | -55.581501 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c56c9432-bb6b-3073-b11a-7edfe9215c90 | -6.864 | -57.7286 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1632846-edc7-343b-afc8-ac578246f077 | -7.7167 | -54.804001 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19a60216-b271-3692-8367-93da198a5128 | -7.539 | -56.127998 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbdddbb2-486d-3d3e-a7f9-283f41182b82 | -6.5219 | -55.390499 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04db9129-c594-3558-b30f-117fea7ac2cf | -8.2612 | -54.748199 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be3334d4-7392-37cf-9aa6-4ab48bd3eb7c | -5.3772 | -56.0602 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 828dab1b-82e0-3a02-acfb-3cbfc0839a2a | -11.4806 | -47.458401 | 2026-10-02 01:12:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6efd323-98b3-3818-9b23-79f9e6477f39 | -2.5746 | -54.7444 | 2026-10-02 01:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 336eed34-3388-3f61-82d3-df8e1765c1b9 | -3.1423 | -53.733398 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3514b001-ef11-3623-9e88-50fc23c14c5b | -10.4087 | -53.778198 | 2026-10-02 01:12:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c8f58e0-a803-34ad-8d0c-9863e01506b5 | -7.3891 | -55.213799 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 374adb47-e9ed-34fb-a87e-8b3972bc9de9 | -5.3739 | -56.046001 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8272067-311f-3803-ab63-d1dc3df06cf8 | -8.2174 | -55.091301 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ffb5c81-24d9-3a36-a01d-c7ec0f54f235 | -7.8431 | -55.124298 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1934036-dc6a-32c5-b760-1743e58dcea0 | -8.1604 | -54.802898 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cfcbc3a-02bc-3918-a241-38c9bd4dd949 | -13.3513 | -43.8983 | 2026-10-02 01:12:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f37aed94-52ab-3513-9f21-9f5cd1e1d839 | -12.8585 | -51.023102 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8a33a04-bee8-372d-b987-5f7f5794b195 | -6.6968 | -56.144199 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af04b166-65c4-38a6-a9ed-b088f42b1b98 | -6.9151 | -59.277 | 2026-10-02 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b684a45d-22fe-3c97-9877-36d8ecfaf7f3 | -7.7282 | -54.8092 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 112a9b87-6383-323c-81f9-ef4a4b2d40ff | -7.3421 | -55.5886 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b309193-385c-37b1-aad9-1f4046c60104 | -3.1702 | -54.072601 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0120dc66-18f6-3129-853e-a7de3dacab92 | -4.3885 | -54.827099 | 2026-10-02 01:12:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8930e446-3395-32ee-8f81-064fc3b52689 | -11.7749 | -43.568001 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81f42b0d-2121-3e84-a0d6-2e56b8ee0d04 | -8.271 | -54.745899 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53a700d6-0f25-30fc-8482-ba746526b6f1 | -2.0568 | -56.870399 | 2026-10-02 01:12:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67c64500-ea1e-36ab-9c7d-d9b21a747cc5 | -7.0317 | -55.629902 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab2a035-7025-31d4-bd45-5a3516991dc6 | -3.1086 | -50.292999 | 2026-10-02 01:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07d8f6dd-4cf1-35e6-bc4a-465f44f5a215 | -11.482 | -43.4762 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8625c9d9-69d3-3ee6-9b2d-95dc933e4084 | -7.2931 | -55.5998 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90fda6d4-3230-3f9f-af78-39d8eed4387a | -7.3339 | -55.598 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cded5bf1-6c50-315c-ab17-48b621ba433b | -7.7443 | -54.789799 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24553e18-a85e-34bf-a2a9-cf0ce830a3b3 | -7.0529 | -55.6325 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa3b43db-f901-3291-a8b4-1dde08899bd0 | -10.821 | -51.108799 | 2026-10-02 01:12:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 93a63f29-aeae-374d-bcae-8d5a5b0dbe50 | -8.2968 | -54.724201 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b107ad52-778a-36ad-bc75-41a0852b492b | -10.4331 | -53.837898 | 2026-10-02 01:12:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 353e27ee-94f0-38d7-bf6d-d2a1426c70c8 | 1.7829 | -55.6366 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33fc9093-88d0-3607-bdfc-78252567a015 | -7.8316 | -55.119301 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6a7d5e-72b3-3a2c-b2e1-571546719df8 | -8.1783 | -54.791 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab61c8f4-7385-39d1-8816-be2bc2926658 | -7.7461 | -54.797199 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa70fb0e-3c59-3e9a-891e-9a41a7f98b50 | 1.8141 | -55.590302 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c9459c7-6158-3f9b-b404-5132a4591083 | -5.3755 | -56.053101 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b94f8a1-db0f-37fe-bce0-c2d78c2d3154 | -3.1271 | -53.7565 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70abeccd-1a46-3f05-9837-5abe21bffedf | -7.4916 | -54.9893 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cec0d4a2-e616-38bf-b48c-a1f794882b42 | -6.8723 | -57.719398 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)

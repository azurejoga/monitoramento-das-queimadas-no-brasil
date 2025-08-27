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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57148e4d-9fcd-33dd-95a0-da600d4c52c9 | -6.82592 | -58.96937 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1913683a-cbf2-3235-8c6d-5a06c9c5afa4 | -8.13383 | -55.36882 | 2025-08-27 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2400cf53-f240-363c-a8f1-091f11d5b81d | -10.48954 | -51.60341 | 2025-08-27 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 365f5484-8ea3-3501-a6b0-ebf70a0047ed | -7.3437 | -59.66108 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f8a05c9-7d8a-3d99-b062-615c395832ed | -9.41357 | -60.51542 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b11a442d-e03e-3543-bf2b-b155f30a4343 | -9.81068 | -64.28999 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b9586f0-1ee0-3b3f-9e99-65cce893c0d5 | -7.17861 | -59.73811 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d968839c-76e8-3636-8d89-d2417f314a49 | -9.06624 | -66.06404 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d02f65ef-07a1-3723-8524-145c5a58c7c9 | -9.1656 | -59.56109 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9d1a8d54-343d-3dd4-9d13-9ebe1c53f677 | -9.58019 | -55.38765 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f02b372-9e41-36c7-ae5f-7fab125bbcf3 | -7.37955 | -64.35658 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b07b09b2-1a75-39d9-b685-65fee525fe7e | -9.39821 | -62.4886 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3d56b94-26a4-304b-b96d-235312f13e1e | -9.17042 | -59.50843 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37307dfa-0afd-3f89-847b-9a303818e53c | -6.91396 | -52.85658 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dcf05e24-2a16-3386-9bd8-4ab9870f368a | -9.64493 | -59.62653 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f8120899-3574-300f-ad99-7b782c98edbc | -7.17144 | -59.74054 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d262454-e668-3366-9ae2-a30d13e9546b | -8.89627 | -60.772 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3493225-7832-3cef-b730-3f81648d7e85 | -8.96342 | -65.97353 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01e98a5a-535e-3e0d-bde0-9f1a800fe871 | -7.53751 | -61.37909 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d2f264f-4051-37f8-8f83-538d33325d6f | -9.19086 | -59.52943 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89a1d2fb-dac2-3f1e-99d0-3aaf28df18b0 | -9.01387 | -65.69614 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e8d6864-b1e0-397f-860d-12c4db94edd9 | -9.39862 | -60.52382 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e1bbd00-2aac-38d1-848b-b2dd84a9a73a | -7.45404 | -60.40595 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835dc5b4-f4b2-3e11-93f5-96f3adbe1584 | -5.79793 | -59.21341 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 367cfefc-3199-3fce-b450-f8000f1b365c | -9.40248 | -60.54245 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2489098-c582-35e1-bee8-b1af9ecb9274 | -9.2226 | -59.67338 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de1d32e4-0697-39e7-b65d-9911ca93c546 | -8.94385 | -65.95715 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 2721fa3b-c399-383a-b4e7-30dfe8b90f83 | -9.41743 | -60.53404 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e8ebb83-192b-370f-a98a-5f867a80cb1b | -7.47727 | -61.33876 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a11ea93-a8d8-358f-807e-55587b95361e | -5.793 | -59.22324 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ea91346-fd01-3a7d-8602-ecdeb80de3f8 | -12.49966 | -47.23543 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe2d9f7d-a240-3ccb-9cf7-fb3c60866626 | -10.77838 | -60.79098 | 2025-08-27 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d7a9a2-7907-35b8-9170-52597682053a | -9.26525 | -59.77262 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bd1bc17-da8a-3d85-af55-b26d0fa267cb | -9.02518 | -65.73167 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 196d2775-8b44-3bbd-977a-e96df4847dc8 | -6.84298 | -58.96849 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a0fc8d66-f77f-3669-a0fd-f7dc1ea0c279 | -9.41744 | -60.51243 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d18a6934-27bb-36e7-baaf-d3917c58336a | -9.10881 | -60.31181 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbed5f73-9700-3a7b-8be2-8f2e5a2fff1d | -9.69356 | -65.71675 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 576fd80d-f50b-3771-8219-4f9e22d0666f | -9.80436 | -64.24644 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c51a5a1f-b4f3-347e-aa23-719d0670768a | -10.77174 | -60.78991 | 2025-08-27 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4cc516d-19d5-36a6-8cdb-539d59d119f1 | -9.16831 | -59.54369 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e8ad3f2-61e5-367a-8aaa-a46ad5f17102 | -8.96935 | -62.1413 | 2025-08-27 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82b7292f-8ce7-30e8-8b91-2bd5bb6b097c | -6.31422 | -59.86766 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a1fc791-55d4-3a7c-94b4-4fee1e068cc6 | -8.96323 | -65.981 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bf5be6e-7be8-3f71-82a4-29594bc1128c | -8.90177 | -47.3256 | 2025-08-27 05:18:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8c78465-1030-3158-bbbe-8155d66405bb | -8.12656 | -55.54843 | 2025-08-27 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d1fdf22-4a8d-3395-b1bf-137c11633eea | -10.06612 | -58.36916 | 2025-08-27 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb73b938-3d25-3094-9ceb-72a4de3c1574 | -8.96871 | -62.1452 | 2025-08-27 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 917d53cb-605a-3c05-a460-68ee60377173 | -9.95233 | -46.37072 | 2025-08-27 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 31b63c24-d0fe-3a72-be50-b3397d8498b4 | -6.68822 | -58.54318 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e548d3d2-cab3-3419-a542-31649f6512ca | -8.85818 | -62.43968 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d81b1a0c-9758-3e4c-a5c6-3cfaf92ef7c9 | -7.34646 | -59.66506 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daaab9dd-0f89-3872-ae96-4fe2baf94a1f | -10.03388 | -59.35526 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8929919-793a-363e-9d69-e3eabc1bb91d | -10.59588 | -54.89403 | 2025-08-27 05:18:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72ff706a-b293-3134-8911-2be16b798f1a | -7.25893 | -57.68951 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c44977e-ed64-357a-bee7-0c5f958e87ca | -8.6531 | -67.26325 | 2025-08-27 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1f7e919b-33e1-341c-bf93-06407d5b752f | -8.96398 | -65.97678 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af8089de-f502-3f16-beb5-72671589b082 | -9.04799 | -65.72712 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc490dda-da0d-3a39-992f-eac9637590c8 | -8.35185 | -62.9373 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d2d49ea-02c9-3723-9da6-eb19d91eb11e | -9.2614 | -59.77557 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98d5a64a-b3dc-3bdf-869a-cbd81579db1a | -9.56371 | -55.38343 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2451790-38c5-3604-9e5d-4a521bddd175 | -8.34529 | -62.9318 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f6045f4-7fe8-3810-8558-6e2e3daaa6fb | -9.39756 | -62.49258 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b013b0d-23ec-3b7d-afc5-5fb1641afaf1 | -5.79516 | -59.20945 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d488b764-28cf-32d0-b7ee-a9532b4b6245 | -7.62462 | -61.03667 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 78d34c6f-7069-3376-b4c8-98d00fbad507 | -9.06983 | -66.06496 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 57774dc1-2dea-32e5-9865-0c555b36cc47 | -11.80223 | -51.47079 | 2025-08-27 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a81160-41b6-3472-bbf5-08c0d2db17e7 | -8.95544 | -65.94176 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e895912b-09bc-3050-980c-f7316077220b | -9.00246 | -65.41391 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9703b235-5bb5-33e0-b1b9-9ef835bd1fc9 | -10.04022 | -67.5325 | 2025-08-27 05:18:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d262fd71-e657-3f35-9d39-e587ae919a79 | -7.47442 | -61.39966 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7469855d-15c2-3881-98b5-155f3116e400 | -9.41025 | -60.51488 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dde2973f-7dd4-3510-baae-64b439674064 | -9.1798 | -59.51347 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53a85e8e-07d6-3446-a123-03bf5933e25d | -9.41467 | -60.52999 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3787051-7d79-3d1a-8cda-1555008984f3 | -6.83361 | -58.96349 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e39027e9-2c85-32aa-bed1-dfebc50861e9 | -8.93158 | -65.92466 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 273cb784-4275-3c76-9787-349803fb68e3 | -9.15899 | -59.56004 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 73769a65-b37d-39f5-bd5c-a2df843a051d | -6.62746 | -58.54083 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb58d786-08a7-3f7c-88e0-a1ebc3ff6a76 | -7.35308 | -59.66611 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76978a84-8c47-3f41-a85c-63a8a3ce512f | -9.82543 | -64.28481 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 517cd287-e7c8-3f7f-ae63-7f2cdb39b2ac | -9.16446 | -59.54665 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0b9b921-2f16-30e2-93dd-01d12adf6fa2 | -6.81708 | -58.96091 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a84dba5-7290-306f-9059-08d799ae78c8 | -8.89016 | -60.76738 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b972b538-b575-350b-a238-a81e3806a760 | -9.02381 | -65.68965 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 509b80a0-dafb-3570-8544-daf5c7dfc878 | -11.19194 | -62.64654 | 2025-08-27 05:18:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37986ec6-b776-370f-853a-ef9c8fd5a6fe | -9.18515 | -59.45726 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78792696-d48c-34ba-95a4-7e49a7cec561 | -9.17157 | -59.52287 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2c3b51f-12d9-30b8-86b1-ced3f8ef8eb3 | -6.23976 | -60.01722 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fd1494f-94be-3c46-a6bd-d86f4756ac81 | -9.27573 | -56.90782 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a632de6b-f03e-3265-a071-93fb22c91fb0 | -7.5096 | -64.60574 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e38fb6b-7b74-3067-8cb3-e4029e623883 | -9.18251 | -59.49608 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea5540e6-8530-3f2b-bc8a-e04274c00fbe | -7.55367 | -63.83988 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 406db08a-8267-3c8e-a7a9-497442a5f8b0 | -9.41689 | -60.51594 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b69e1c73-4865-3b7f-935b-bc415a98404e | -11.91524 | -46.74501 | 2025-08-27 05:18:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86a1c76f-a272-37a3-86df-15783816787b | -8.72361 | -64.02397 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c8bfd42e-d5b3-3843-90b4-332587dad0bc | -11.19259 | -62.64264 | 2025-08-27 05:18:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 452c810b-84eb-3f7a-ba95-557306754c03 | -7.05266 | -57.80668 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7397a868-eb17-3008-846e-257bbf140796 | -7.41288 | -60.62172 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68a5d28b-65bc-3f34-83c0-6c857dab8989 | -6.62862 | -58.55527 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61cf8242-002f-308d-a12f-82e301e214cd | -8.89407 | -60.76436 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README56.md)

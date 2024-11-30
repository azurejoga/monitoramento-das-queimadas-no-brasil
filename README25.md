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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57d71ee9-75d6-3514-8c93-96e35b8cc7fb | 0.97982 | -50.25394 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 23e896a1-b724-351f-aff1-302d8f939971 | 0.10366 | -51.46958 | 2024-11-30 04:38:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fab5c12e-ec54-39d0-a33f-bd33c457ad05 | -0.09665 | -51.74846 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbc2cc1c-6638-3ea3-a5d0-136e574a7ff1 | 0.97988 | -50.1228 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| fd56d928-7445-367f-b787-b40f9fc1f9c5 | 0.03266 | -51.10294 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff262c91-c2d1-3447-ae49-b31bdccf6031 | -0.0501 | -50.82727 | 2024-11-30 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a5eadf-d56c-3a7d-bfb8-18ca0ba4cf7c | 1.63894 | -50.9499 | 2024-11-30 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f794493-6f71-3307-9457-7d83f95195d7 | 1.20449 | -55.93736 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c5db04c-dca0-3595-85cf-c5a1f2f9fa7f | 0.69466 | -51.44075 | 2024-11-30 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4868f388-6490-3e80-b9c7-ad4df036a757 | 1.37817 | -50.945 | 2024-11-30 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccfac502-20e5-34fc-99d1-6534216bbc42 | 1.16205 | -50.79014 | 2024-11-30 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14027503-0c43-34a0-8f4c-5effa21ee441 | 0.98971 | -50.2718 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce7ec431-c314-34c6-8f9e-1a9c15a7b5e3 | -0.3858 | -51.57736 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 990b2a01-23d4-3da0-8f6c-e66989e57a86 | 0.98566 | -50.26854 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 49e35a01-c182-3ade-85c7-dbc6a0deb2bc | 0.9915 | -50.26745 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a67c57d-394d-3ef4-a443-9db9a81d0f27 | 0.93345 | -50.74258 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a752d28d-01eb-3d04-a22b-9288864007e7 | -1.02023 | -47.1045 | 2024-11-30 04:38:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e11a01e-960e-3fae-ba48-601db877732c | 2.80511 | -51.08528 | 2024-11-30 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2969dc2c-78a3-387c-bc81-78cdcd6a6f60 | 0.94279 | -50.73309 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0be340a5-1fc8-31ed-9a42-3b747d6a380f | 0.09042 | -49.92968 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cc45c2d-fb3f-3d1e-a1db-6165bab5635f | 0.03328 | -51.10695 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dafe7e3b-0485-3ccf-ac64-39d2a8fe1252 | 0.98626 | -50.27233 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8230a889-6fa0-34e4-9cb9-9144a76f25dc | -0.26703 | -51.64225 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07416da2-91e6-3aa0-a052-a2165571fcbd | 0.10556 | -50.47751 | 2024-11-30 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c921a6ad-a6fb-3547-89c0-3b7ee404b419 | -0.97202 | -47.67252 | 2024-11-30 04:38:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bde4b0d-0ff4-3883-abb6-508f7b79d4f6 | -0.03266 | -50.73322 | 2024-11-30 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbd5c8ec-7a85-36a0-804e-644350c1370a | 1.21352 | -55.93032 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af941408-40b1-3598-a7f8-903e70b89331 | 0.14467 | -49.87681 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a319c050-6d15-3397-9f8c-f53cc5fb2232 | 0.66145 | -51.63861 | 2024-11-30 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1038e7a2-cc02-362f-a3eb-f6637b617c67 | 2.81245 | -51.0842 | 2024-11-30 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cfa8e0b-43fb-3763-b5f0-02810250ac1c | 0.71753 | -51.46761 | 2024-11-30 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e575695a-c3a4-34e8-8859-a7311128e7b3 | -1.01389 | -47.99456 | 2024-11-30 04:38:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42b53c54-8609-3ff5-a3af-01be007448cc | -1.30823 | -46.77202 | 2024-11-30 04:38:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d0c2f7e-d570-384f-9a8a-168e794c0288 | 0.93407 | -50.74653 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ab577793-3c1b-3837-aa48-f514b11adc60 | 1.35499 | -50.72595 | 2024-11-30 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee934eca-bee5-3fde-8ce0-1ba0a001d309 | -0.07283 | -49.66702 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 242aab7b-613b-3e40-be97-d43be25cf52e | -1.01004 | -47.99749 | 2024-11-30 04:38:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac017a30-64fb-304c-a458-c0a58f5d76d0 | 0.97696 | -50.25825 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb2595c9-7668-3308-86d6-74f3871ef936 | -1.35576 | -45.89331 | 2024-11-30 04:38:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e70b8fa9-03be-3599-971a-17201a7670d5 | 1.21844 | -55.92956 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8944aa50-983a-3ac3-858a-212ce8044a9e | 0.66171 | -51.63692 | 2024-11-30 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54840675-3207-3964-b22a-1106c376a446 | 0.9376 | -50.74601 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6a8fc0ad-df25-3242-aad5-240899da8ad4 | 1.182 | -55.96656 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 335a4c0e-c9e1-37cb-811d-3b50ea4c4bf0 | -0.0472 | -50.82284 | 2024-11-30 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1599cfc9-ce07-355d-9af1-68d207cbc518 | 1.64018 | -50.94853 | 2024-11-30 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a61cf0d-f6ef-39ee-8f8e-1b3ca6eafa31 | -0.10967 | -51.49534 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a14eb638-98f1-3f1f-9e58-1e5dc307a9bb | 0.94342 | -50.73704 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eefe6b7-51be-32c5-90d4-431d16bdff00 | 0.73583 | -50.86891 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 620f18b5-85f6-340c-9d7b-fa8b975d248d | 0.98912 | -50.26802 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b26170a-6a8a-3844-b6a5-f62ca78b2d29 | 0.93822 | -50.74995 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 02126592-f9ec-3ec6-a599-8d8384a034e9 | 0.94051 | -50.74152 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b786c4c-586a-3928-8d6a-fb39c4caa86f | 0.98268 | -50.24965 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9988298b-6a32-3805-bab7-0a838d7271df | 0.03012 | -51.10662 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d1fffea-67dc-3657-a9aa-9ef9ff991bec | 1.20942 | -55.93661 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b45bc15-8cba-3928-a03a-dab778ac55da | 0.73937 | -50.86837 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ecb00fe-1f94-3aea-8920-f0af071ba282 | 0.94175 | -50.74942 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ba0d7a2c-b48d-3ee8-9e9f-35d43caaf462 | -0.26401 | -51.49584 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dae7ba30-a89c-39c1-b2ac-335e876b498e | 0.88393 | -51.98288 | 2024-11-30 04:38:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3c395c17-183d-34d4-9315-7898ef04f541 | -0.02917 | -50.73269 | 2024-11-30 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a531e2c-f2cb-3130-83be-afe2eb7c5c92 | -0.90579 | -47.70495 | 2024-11-30 04:38:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb9d6b37-be9d-3b96-8f9f-b96694ba25db | -0.26336 | -51.5 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e07ff530-f346-3eb4-b6fd-96c9b57dd13f | 0.98328 | -50.25342 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f616e9-5c60-34fa-b92f-191fe69edcd5 | 0.0659 | -51.49567 | 2024-11-30 04:38:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 073a9f1d-69eb-3c93-bbfe-a4b0a26ca4e7 | 0.33681 | -49.71408 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5546952c-555e-3a70-83ef-9191f369205f | -0.26669 | -51.6206 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e4ceca4-d634-3625-96a1-e15c193ac21e | 1.20322 | -55.94075 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8435df48-7d01-3b04-bbb4-e4adb4c065df | -0.26235 | -48.62566 | 2024-11-30 04:38:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| adb48fc8-4172-3e52-86ac-ecc30bac6448 | 0.96956 | -50.12438 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca69ad61-10a3-38b5-b9b3-77b39bd6e90f | -0.27033 | -51.62114 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa18f876-beb5-3bd3-a912-f8ac211fbffc | 1.20531 | -55.94288 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90aeacc3-f06f-3e09-9db8-b3e3aef8c11b | 0.94528 | -50.74888 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c99d1c3-abe7-3394-858f-8ecd8b8611f9 | 1.35853 | -50.72542 | 2024-11-30 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65cb3c85-0c7f-33b7-a3db-0f633622306d | 1.20408 | -55.94625 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 939613b0-9f79-3522-8d60-d40c578e28b8 | 1.19914 | -55.94694 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e77b523-5d44-3f67-9887-2ab052de163d | 0.99208 | -50.27124 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70f5b8dd-e5cc-39a4-a52e-e5da8cbc1c59 | 1.64254 | -50.94938 | 2024-11-30 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddfc88ae-eb2b-3060-8d0e-99e8cf267ae4 | -0.27927 | -51.63547 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4da9c710-d010-38a0-ac0d-51736be14835 | 1.67865 | -50.66261 | 2024-11-30 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72746cc2-1139-3f9e-af79-a7fc6143be7c | 0.03368 | -51.10608 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb1ae335-f0b1-368d-98cc-a5374afb3962 | 1.18286 | -55.97211 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42958c09-0bfa-33ad-a7bb-78c218ad9aca | -0.27862 | -51.63969 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36b94772-d86d-36fd-9da0-219144a092c8 | -0.34518 | -51.98286 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 728cecc3-8b64-31e5-a07d-e211dcb2a209 | 0.62786 | -50.56845 | 2024-11-30 04:38:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a11ed923-adfa-3f68-b011-d3f239862eff | 0.09939 | -51.46597 | 2024-11-30 04:38:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67f9d5d6-a132-32e5-ac4c-9355dde6cf81 | -1.21449 | -46.7654 | 2024-11-30 04:38:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58cb81ca-d159-3e60-b8f3-0b598094f7f1 | 0.98041 | -50.25772 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ff5bd52-6b63-3f0b-ba23-e4775cbccbeb | 1.21714 | -55.93303 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebcf22a9-f4f6-34ab-9000-4b16d284029c | -0.04552 | -51.74126 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa5f1bf1-2e5a-3079-9b73-2a6431367715 | 0.98045 | -50.12654 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9cf00c43-36f8-301a-b8ad-43a20dd843b4 | 0.99437 | -50.26314 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b40e49b-064c-31ee-8a89-118801384a62 | 0.98389 | -50.12602 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 02b6b584-5432-3c82-b9b1-a117c70514f8 | 0.09441 | -49.84372 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0689811-20b3-3568-9f21-29081b267585 | 1.8716 | -55.74035 | 2024-11-30 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18fba846-f5c6-35ca-af3a-3b4788757cf8 | 0.97409 | -50.26255 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ffe5f87-53de-3818-82df-bc404a5ed13c | 0.32162 | -49.63926 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e43d7210-f664-357e-baf6-f96e047bfba9 | -0.54274 | -51.41025 | 2024-11-30 04:38:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4d37af8-37ab-3993-ad2e-ff0a2cccf97e | 0.94217 | -50.72914 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 421284c4-ed0e-3601-b6ce-b81de845e19c | 0.07695 | -49.82051 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 776ed472-90ee-32a9-877e-eb93e623e415 | 1.67738 | -50.9609 | 2024-11-30 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cd4f767-27c8-3ab1-beba-beafb88ea929 | -0.20301 | -51.40305 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README26.md)

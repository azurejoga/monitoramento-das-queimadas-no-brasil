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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b847f17a-737a-309f-b1d9-35c58b348778 | -6.782 | -59.6519 | 2025-08-25 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ae38bf15-fa83-32a0-b74c-2e7762e8a6c7 | -6.2644 | -59.9976 | 2025-08-25 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| fe2bf11e-24f3-3612-8d62-633a1de023a9 | -11.6089 | -46.3699 | 2025-08-25 07:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| e05beb35-fe9e-3eda-a6aa-c067354d50bd | -8.9689 | -65.4198 | 2025-08-25 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 83c01adb-c361-3af8-b137-93db2b9e3d3c | -8.9874 | -65.4192 | 2025-08-25 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| d059476d-1ce6-31e3-ba4a-a07df2572f4d | -6.8893 | -47.9333 | 2025-08-25 07:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| bbbf85bf-535c-3702-b35f-0b963f5fbc8a | -8.9875 | -65.4006 | 2025-08-25 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| eb3e9a55-3626-349e-960e-cc77a99f478a | -11.6093 | -46.3472 | 2025-08-25 07:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| ca7e3bf4-7b57-3505-8ee0-8eabf773700e | -11.6281 | -46.3673 | 2025-08-25 07:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 30f4b2c5-8e2b-382f-a51b-c2dce29c767f | -7.8892 | -63.0737 | 2025-08-25 07:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| aae558b2-504f-33f9-8e70-adce479d606f | -8.8919 | -62.4487 | 2025-08-25 07:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 2878e1d2-79f7-35dc-96c2-092a1c0d16b9 | -6.7819 | -59.6711 | 2025-08-25 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 103f91aa-61e6-38e1-a12c-1769fb931c55 | -6.4538 | -44.6207 | 2025-08-25 07:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 778efbbd-d360-34f2-9a68-8b99e31ae43c | -6.782 | -59.6519 | 2025-08-25 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ceaeb71e-d8e0-32f1-bf7b-a2aaa2b27214 | -6.2459 | -60.0174 | 2025-08-25 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 2d1e648f-9415-3e3b-b780-aa2cd7812c08 | -9.006 | -65.4 | 2025-08-25 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 491e0e4f-722a-3a89-91ae-f11173f005ae | -6.2643 | -60.0167 | 2025-08-25 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 76ce110f-07ce-35b2-adfe-c6d4514a1671 | -6.2644 | -59.9976 | 2025-08-25 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 83dcb7dd-0f32-3a46-8bc4-bfac643a96c7 | -8.8735 | -62.4305 | 2025-08-25 07:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0c418fa3-2dc2-37bd-ad61-cd549cfef749 | -7.9077 | -63.073 | 2025-08-25 07:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 879d5fa6-b35e-3575-83a8-d23f7b470582 | -6.246 | -59.9982 | 2025-08-25 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| e2c7f534-79fd-3683-9c9d-d8fbe089f1e4 | -8.8734 | -62.4495 | 2025-08-25 07:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 96694322-8e6e-3958-8e5a-2d72d0ca6b83 | -9.006 | -65.4 | 2025-08-25 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 51c4db39-68eb-3161-96de-86918feda27c | -8.9874 | -65.4192 | 2025-08-25 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 9b9ff8df-c5e7-3229-98bb-0ca8515df31c | -8.9689 | -65.4198 | 2025-08-25 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 995b0128-5ba4-3d0d-9732-29aabf78e9f2 | -11.6093 | -46.3472 | 2025-08-25 08:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 91649494-c042-37dc-b3d4-eda6dccf302a | -8.9875 | -65.4006 | 2025-08-25 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 51c7ed5c-5c55-3697-84d8-9267d3db8c6f | -8.8735 | -62.4305 | 2025-08-25 08:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7dfddb1b-e1b8-3e8b-9ddc-e6fc2cc677ec | -11.6089 | -46.3699 | 2025-08-25 08:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 817714fc-731a-34f8-9171-456473349b03 | -8.8734 | -62.4495 | 2025-08-25 08:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b4cdd718-f605-3266-a381-8654ae29cd24 | -6.2643 | -60.0167 | 2025-08-25 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 2838574d-a7dc-36f5-90bf-8c7efc79fb59 | -9.1722 | -59.4629 | 2025-08-25 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 161b7cb5-0b5e-37c0-acdd-5a4cb7b2f51b | -6.8893 | -47.9333 | 2025-08-25 08:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b1905422-410b-3533-88b2-e3d156d5cb7b | -8.8734 | -62.4495 | 2025-08-25 08:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c29c8084-5a01-3ffa-a19c-af1ac4c71e18 | -11.6093 | -46.3472 | 2025-08-25 08:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 918ad486-d22f-31d7-a4f7-39a2c8ed3402 | -6.2643 | -60.0167 | 2025-08-25 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 519a1338-bdb5-3efe-885f-c7a07f84c260 | -11.6285 | -46.3446 | 2025-08-25 08:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 01cf765b-4c58-38e2-a8ac-e31dc1247075 | -11.6089 | -46.3699 | 2025-08-25 08:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 0d56e4b3-6be9-3cd3-91a3-a08ecfdfb329 | -8.9689 | -65.4198 | 2025-08-25 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b3249f64-4b3d-3321-a44e-7078671ac2ef | -8.9875 | -65.4006 | 2025-08-25 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 16f88548-706a-3570-a3f5-dee14fec93a8 | -8.9874 | -65.4192 | 2025-08-25 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6932d733-355e-397f-9b58-cc4a853c67bf | -9.006 | -65.4 | 2025-08-25 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5069c6c9-0bf9-362c-b60a-9d3bbef42e04 | -11.6281 | -46.3673 | 2025-08-25 08:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 586bf79e-6fb2-34ce-a879-5d48d12033f6 | -8.9875 | -65.4006 | 2025-08-25 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 4698ca4f-acb4-383a-99f3-a3af2257e6c5 | -8.9689 | -65.4198 | 2025-08-25 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| fd075881-72a5-337d-b0ab-14214a70e9d3 | -8.8734 | -62.4495 | 2025-08-25 08:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 20ddc591-c3f1-390c-bc43-951d1d717e68 | -8.8735 | -62.4305 | 2025-08-25 08:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6bf25267-9e25-33bf-abfa-6f1782d0565e | -9.006 | -65.4 | 2025-08-25 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 700c7f19-ba70-3202-a1c4-4c1e0c70371d | -9.1722 | -59.4629 | 2025-08-25 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| d8066853-df9e-323a-8a65-147f69b2b638 | -9.06 | -65.7344 | 2025-08-25 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 6a9fa822-6d75-339d-8198-bea3902c6f50 | -8.9874 | -65.4192 | 2025-08-25 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| bb756d38-238b-3b72-be85-dd15d4d4e15f | -8.0683 | -49.6738 | 2025-08-25 08:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| acfa9f8f-6539-36bf-9532-3ff775b31656 | -9.1722 | -59.4629 | 2025-08-25 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 4d9e7b71-fd41-3e94-9c4f-6895e0bafbd4 | -8.0681 | -49.6951 | 2025-08-25 08:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 09b58415-d507-345c-ab37-1ff997e534a0 | -8.9875 | -65.4006 | 2025-08-25 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| af9117b9-4289-39a2-b66a-16160734b22f | -8.8734 | -62.4495 | 2025-08-25 08:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 0106ea72-1641-3254-bce9-9d9ba1879bbd | -9.006 | -65.4 | 2025-08-25 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4f660cd7-dd72-3d1d-aeb8-d8e34237b3ab | -8.9874 | -65.4192 | 2025-08-25 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ab7edafe-ce3e-3eb7-a6a9-bd7158a282cf | -11.6089 | -46.3699 | 2025-08-25 08:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 75a4a181-9fb5-3031-b44f-00bbf3e27370 | -8.9689 | -65.4198 | 2025-08-25 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f50b0241-420a-3fe8-8c30-48e4056a761d | -9.006 | -65.4 | 2025-08-25 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a3cc3471-47c4-32e2-8ecb-9226789526dd | -8.8734 | -62.4495 | 2025-08-25 08:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a459f82b-28a0-39c1-804f-b9ab1a1acd96 | -9.1722 | -59.4629 | 2025-08-25 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 679c4757-b847-3ca5-81c0-6e08847eeb81 | -8.8735 | -62.4305 | 2025-08-25 08:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 4c37c195-8df4-36af-8680-b6afd668bce4 | -8.9689 | -65.4198 | 2025-08-25 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| faf538e0-6ff2-38e1-98d5-f70290cf532c | -8.9874 | -65.4192 | 2025-08-25 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b472f094-e928-353f-bad4-d00caad46989 | -8.0681 | -49.6951 | 2025-08-25 08:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b303cd35-c064-3e9d-9b57-0b0cfef67ccf | -8.9874 | -65.4192 | 2025-08-25 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c33bae84-7fb1-3f9a-8113-e1e42bcebd00 | -8.9689 | -65.4198 | 2025-08-25 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ac8ee3bc-ad2f-3936-926d-69bd11c147ef | -8.8735 | -62.4305 | 2025-08-25 08:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a3fd9c3d-cf41-33d5-9d22-93970a62f0ff | -8.9875 | -65.4006 | 2025-08-25 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| cbbfea76-ddcb-39b8-a700-a4e33147abad | -9.1722 | -59.4629 | 2025-08-25 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2de30063-edd7-3cef-909e-6e329088feb8 | -8.8734 | -62.4495 | 2025-08-25 08:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 48a40cd3-7470-3219-a6a7-631709e540ff | -8.8734 | -62.4495 | 2025-08-25 09:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 9f35a13e-fb4a-3aa3-aa4c-58c1206eb46c | -8.9874 | -65.4192 | 2025-08-25 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1d205e58-c608-3fd2-bd57-58299f6f8590 | -8.9875 | -65.4006 | 2025-08-25 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e552a08d-6196-336f-816c-efdce60ebef4 | -9.1722 | -59.4629 | 2025-08-25 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| c2ce3243-906e-3813-86b7-95c3a3e38fae | -6.7819 | -59.6711 | 2025-08-25 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 932fed3e-d208-3950-9dc8-a59b87734671 | -8.5758 | -62.6323 | 2025-08-25 09:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c442ec8d-645d-330c-8e54-7af2bbe8c626 | -6.782 | -59.6519 | 2025-08-25 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| fd5e47cf-222c-37b4-a76b-c2eeba1408dc | -8.9874 | -65.4192 | 2025-08-25 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 37565477-d8a2-32c5-8413-1c937eba9490 | -9.1722 | -59.4629 | 2025-08-25 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 9f54aa63-0c5d-3dd3-8f8a-99a9231a561c | -9.006 | -65.4 | 2025-08-25 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b4272163-c2d9-302e-bc68-e0c59a7ff473 | -8.9689 | -65.4198 | 2025-08-25 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| bebc9bde-47bf-332d-ad29-05522448ee2b | -6.7819 | -59.6711 | 2025-08-25 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 904584dd-a50b-3eb9-ae89-c84e3c6cc680 | -8.8734 | -62.4495 | 2025-08-25 09:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e87bcb3e-832a-3af9-8f3c-f3d9f87881c6 | -8.9689 | -65.4198 | 2025-08-25 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d4cb4cdf-5d5f-3883-b2dc-f111e17b39b7 | -8.8734 | -62.4495 | 2025-08-25 09:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0897e1e7-f571-3551-a882-a6e1266bf3a7 | -9.006 | -65.4 | 2025-08-25 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| cf48369a-f8b1-3a88-a818-9901b91a6acb | -6.782 | -59.6519 | 2025-08-25 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 8f2e04d4-37be-31fb-a932-12ac0b3b77d3 | -8.9874 | -65.4192 | 2025-08-25 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| df01b379-b8ee-37d6-b9ee-dcfdbbc9a6ca | -9.1722 | -59.4629 | 2025-08-25 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d9d6d4a1-635f-34a8-a679-e7cddd1e3701 | -6.7819 | -59.6711 | 2025-08-25 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 9cf2749e-8c99-39b6-8a1f-dc52ce3a95d9 | -9.006 | -65.4 | 2025-08-25 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 3770264c-c1ad-3096-9991-f26f1dbaee88 | -8.9689 | -65.4198 | 2025-08-25 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 14694eaf-fe31-349b-a37c-23d7f05a913e | -8.9874 | -65.4192 | 2025-08-25 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f7fb2fd2-b7ad-3443-897e-0025737deb48 | -8.8734 | -62.4495 | 2025-08-25 09:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 740a88b5-6f67-3ecd-868a-a43c179ebada | -8.4951 | -63.8805 | 2025-08-25 09:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 38c7879e-ad24-3f70-93c2-9c6c34c2f9ee | -8.9689 | -65.4198 | 2025-08-25 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6c366420-488e-3751-ad25-bddb0ffdad25 | -8.9874 | -65.4192 | 2025-08-25 09:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |


[Clique aqui para ver as próximas entradas](README92.md)

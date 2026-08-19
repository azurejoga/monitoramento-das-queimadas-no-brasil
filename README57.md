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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c397264a-fe3a-31ee-bc68-6425fe97b043 | -6.75262 | -59.16401 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86958b37-c662-3ae1-96ee-ae55015250b0 | -6.84093 | -58.99443 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5dbf5df-63c8-3e63-b413-6f76e2d31339 | -8.58317 | -54.74897 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bae70268-1443-30a5-9e71-214609d19854 | -6.95583 | -59.04519 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fb0f422-2c36-3569-9a92-9eb95c154f54 | -8.56502 | -54.68667 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48c25b8b-9674-3269-802c-721d73ffe61f | -6.70186 | -58.94298 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 35bd88fa-8e69-33e8-841d-bb05aac371c3 | -9.42804 | -60.42375 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 392c112e-7c6f-3fa9-bd7f-ed052923ac72 | -9.46715 | -51.60096 | 2026-08-19 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a7943f7-607a-35fd-886a-744f042f447f | -8.50818 | -54.86736 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56505f73-46e7-3aa5-8679-c41f5e161ddb | -8.55332 | -54.76919 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d1934759-66d7-394e-841c-b9863d5a3c82 | -8.58582 | -54.76252 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8de94be1-33a3-39a5-a31b-eddec45da0c6 | -9.08914 | -50.8019 | 2026-08-19 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4ddb4af-ac78-3cfc-8acb-63542e545262 | -6.74814 | -59.1707 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b88704c-bf09-3216-b313-85f926b5c60a | -8.57705 | -54.69727 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 111fc057-f0f9-3ba6-85a3-e5533370aa79 | -6.63141 | -59.07856 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9fa488a-15a1-351d-a821-06144180cd18 | -7.05721 | -59.84282 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6b7521fe-d781-3318-8c20-86150ee27e9b | -8.58117 | -54.73061 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a574f5f-e7f5-347a-86bb-9219044301f4 | -7.57095 | -55.5625 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1231e8e-6cad-321f-9b20-9ad871b78b9a | -6.87624 | -56.41938 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec3c0958-300f-350f-9300-de1185714f89 | -8.54132 | -54.75874 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6200269-af96-3920-a5cf-49fd94f26be2 | -8.55512 | -54.75651 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19bb1dd0-2397-3275-bd26-f0af6944bae9 | -6.74531 | -59.16653 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14448acc-b590-3fde-8f15-2962595f26d5 | -8.53737 | -54.72287 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f1f76c4a-667b-321b-8808-29e588617040 | -8.96006 | -60.52759 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe5a0ec7-c6dc-362c-9d0c-a41d27da5964 | -8.56937 | -54.6844 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58cf6f1f-d0fc-31a2-bca7-1b407a6cca9b | -6.80164 | -59.44387 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28cf9a07-790d-324c-851d-184df011e950 | -6.7972 | -59.4505 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35e4aa13-a0a9-318c-8f41-5c3eed306ad3 | -8.18248 | -55.00788 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52fcd47d-ef5d-3a9b-83a8-4ce41e341858 | -8.56378 | -54.75949 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e1bcef2-a813-3cbf-ad13-acff94273205 | -8.55825 | -54.76724 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 368a4a8b-c944-357e-93bd-05ca56824096 | -9.40302 | -60.56441 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d7a7a62-6624-3c21-9654-44c4dd988731 | -8.10882 | -51.66292 | 2026-08-19 05:23:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2a7edb4-5fde-3d30-8f63-91da583e9123 | -7.61016 | -60.9669 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1c4943f-7698-345d-a2df-5af7d593f801 | -6.81344 | -59.45667 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6c34012-c0c4-35f9-b97d-7b9584e4d45a | -6.71986 | -58.59136 | 2026-08-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3b7d3dc-c1d2-3316-8564-79ab774236d5 | -9.08333 | -50.80117 | 2026-08-19 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 849c9c19-a85c-3938-b2e7-0d3b0f8432e6 | -7.61293 | -60.97089 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0269222-3e17-3de4-9a09-a9c5801eb984 | -7.10248 | -59.76654 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ea7f763-802d-36d3-bac1-00c9dd052c36 | -7.60409 | -60.9624 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f8f9ca3-3260-3b5b-939c-b61e7d75875a | -6.63613 | -59.07877 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e172b1-c84f-3da5-b065-48a5c4e61d0d | -8.57203 | -54.76492 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4c18dcd2-0fc9-33d1-8c6e-630019ca43ae | -6.8828 | -59.0452 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25af6f06-51d3-301c-8d51-c61bfb34bba7 | -7.539 | -55.58047 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dd289536-4015-3762-a19e-04e0557aafd0 | -8.56407 | -54.72392 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 969354f6-cd8a-3385-b626-c66df4775a12 | -8.95349 | -60.54813 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1677de87-9ed4-3883-b644-c619d4a648ab | -9.19913 | -60.78414 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff8935cb-0b98-3eec-a485-b873b36b9cf3 | -8.56114 | -54.74571 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86bd453e-d7b7-3cba-af37-afb20a778872 | -3.0156 | -51.06036 | 2026-08-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa8405b2-df53-3217-b404-2410f8461576 | -8.57586 | -54.73711 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a1e3c736-3aa2-38ec-8ce5-936e2006372d | -6.81117 | -59.44901 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24b84dc7-0b98-3ce5-819d-51fcec7ba39a | -9.11399 | -60.38923 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a74e3349-b494-3da5-b3b8-464954e7e8c6 | -6.99463 | -59.04688 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93847898-f318-3b3d-b8b6-d18f0464ee3b | -9.39392 | -48.2433 | 2026-08-19 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5720e39f-f831-38b3-89c8-1a7f976bb154 | -8.5733 | -54.72354 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9576c178-f8a1-3f12-934f-77b913849a2b | -8.55072 | -54.75581 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0f4cd9c-7c75-32be-b7ea-24e0655008a6 | -8.89737 | -60.60403 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cdfabb0-e908-3e79-a760-3e9819a1b276 | -3.27163 | -49.51862 | 2026-08-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42a71855-a706-30e7-9576-a5e498f11f9d | -8.5776 | -54.75696 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c00be7a7-aab3-3d6d-91a7-940e1b957e9b | -6.78934 | -59.44234 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26e8bb9e-2f17-32d1-b3fd-bca5181c7850 | -7.60423 | -60.83115 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b10a5ec4-21a4-3709-aaca-5e1dc69251e1 | -2.68136 | -60.92674 | 2026-08-19 05:23:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e0b7e89-430e-3a0d-b511-2a191a032e88 | -8.55832 | -54.76558 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 92528220-a540-3404-bb90-3e704b0037be | -3.68399 | -47.65267 | 2026-08-19 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6dbc85ec-612f-3b5b-af57-b49c3a632179 | -7.47481 | -64.26354 | 2026-08-19 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ceb32bfa-4895-3291-9acd-3cc431ec3f63 | -8.53678 | -54.72714 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07b7c547-a604-3e48-adf6-d62323d42842 | -8.58207 | -54.69065 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bb02df3-871e-3621-bf4e-4501e25b65d2 | -8.53296 | -54.72221 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08b90a45-8e44-3521-bca9-9a6c6b797ecb | -8.22477 | -55.03683 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e83c6fa1-3712-3db3-b3f4-6c809f8b4e80 | -7.60848 | -60.95599 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc99703c-21c1-30f6-8f9f-77ae3d1e60ff | -8.89886 | -60.55044 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73e599d6-0858-396e-be1c-f1afe9c982da | -6.75207 | -59.16764 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9a145e4-39e8-3b68-81fc-2ad63d5870d2 | -8.57833 | -54.71985 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a74478d5-3064-3580-8e7f-979268547e2e | -9.2039 | -60.82052 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeb105aa-dea9-3d06-8029-bff36263254f | -3.10129 | -61.19931 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf0b7896-1b83-3b05-b7d6-ff798f126a4b | -6.88169 | -59.05253 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a606c4b-4617-3077-b597-d89a11ed7ede | -6.75655 | -59.16088 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c353769e-13dc-3fb0-8f99-27c0eb16fa44 | -8.58292 | -54.71769 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bec15a1a-ea59-35bf-b60d-f27b67f639f3 | -7.46427 | -63.64421 | 2026-08-19 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 983bb6ba-22a1-3696-ac03-94b318b8b138 | -9.40642 | -60.58655 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ec0a857-4a95-3e81-8c32-67d1a8847f2f | -8.29233 | -62.89319 | 2026-08-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a570693-4ada-3c2a-bb97-25ade16a77c5 | -8.5738 | -54.68503 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41843ff7-809e-3c27-8279-a94d77ac86e6 | -7.54257 | -55.58479 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49a3edb4-4aab-3689-a4d6-f9bf165d9833 | -7.53543 | -55.57614 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 10d1adc8-0e64-3309-ac5e-26ec0093b717 | -8.57527 | -54.7741 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2b67dc6-f9ee-31ba-a4ec-86910cd531a5 | -7.05775 | -59.8393 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13e1ad6e-01e8-31e6-a7dc-e576237cca0d | -8.5571 | -54.77414 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce888a94-da1d-315f-9679-dbd77127e0b9 | -8.56384 | -54.72672 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a9a48c47-7de6-376d-acc1-d8475e7412b6 | -9.08191 | -50.80919 | 2026-08-19 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5df7a193-0505-30ba-b23a-6ab8c2a2f342 | -8.55994 | -54.7547 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 334ac99c-ecda-307f-8e02-637e03492977 | -8.55767 | -54.77153 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a3c3a18e-7123-3131-85fd-df3e553a6b99 | -8.53876 | -54.74505 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46b38785-6021-3235-ac6a-092552d63bfc | -9.14207 | -58.30511 | 2026-08-19 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 293808c3-0c84-3212-b236-7b47a9faa98b | -6.80836 | -59.44491 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f97de88-5b67-3412-826f-8d0643683a1b | -9.42913 | -60.41668 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6aadd53d-3ef6-34f2-bd53-8b1b2b52e181 | -9.12323 | -61.59974 | 2026-08-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed6f9a2e-7002-3a95-9daa-c848c585fcb8 | -8.5744 | -54.68057 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5deb5f00-908c-38a0-ae69-97ac9154f06c | -9.08887 | -50.80105 | 2026-08-19 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 275d0fce-6a07-3c83-81c9-8ece9c340c67 | -7.44744 | -60.00051 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 085a71c1-050a-30ce-95b0-932f9ef3c871 | -4.71121 | -47.15943 | 2026-08-19 05:23:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e1f15fae-c01f-3837-b7ac-8837a4e74848 | -6.85171 | -59.01488 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README58.md)

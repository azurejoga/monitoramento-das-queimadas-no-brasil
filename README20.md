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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6d3a77b-4c75-37d2-8245-e56f880d2f6c | -2.0676 | -52.010799 | 2024-10-09 00:42:54 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9a09a47-2d3d-3726-9b83-e9f648ece68b | -2.0697 | -52.020302 | 2024-10-09 00:42:54 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a599dea-63e6-3751-87c9-7017e3fe76d8 | -2.0719 | -52.0298 | 2024-10-09 00:42:54 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29df9fea-9e40-331f-9d49-f8a76df3f710 | -1.0583 | -47.9991 | 2024-10-09 00:42:55 | METOP-C | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d7c0ac7-1960-3823-b51f-2fd881f39412 | -2.2206 | -53.6367 | 2024-10-09 00:42:57 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f6b2629-7475-358d-b5f3-9f2a125afed4 | -2.2234 | -53.648899 | 2024-10-09 00:42:57 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88f4969a-c88b-3d47-b97d-5adb0581b7cf | -1.1163 | -53.606098 | 2024-10-09 00:43:15 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12176103-6918-3b80-be7e-99df28a0b34f | -1.1039 | -53.596699 | 2024-10-09 00:43:15 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb9bda1-6415-3949-b8f4-e5347e298ccc | -1.1065 | -53.6082 | 2024-10-09 00:43:15 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4544995-7eb6-3a24-a54e-539798b2cb73 | -1.1092 | -53.6199 | 2024-10-09 00:43:15 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65b72f92-1690-3a43-afd4-46662be0a3e7 | -1.0968 | -53.610401 | 2024-10-09 00:43:16 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5536266-0fa8-3d9b-9d90-c8ff0a87541f | -1.0204 | -53.725601 | 2024-10-09 00:43:17 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e689f9-674d-3da6-844c-f6ed10bbf498 | -1.11 | -53.6173 | 2024-10-09 00:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 6d6bd8e3-726e-3d7c-b040-4183770930c0 | -1.1284 | -53.6171 | 2024-10-09 00:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 48533d90-3d5e-3289-a1a4-2db23344d6dc | -1.9609 | -50.8404 | 2024-10-09 00:45:17 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 8028f0fc-79fb-3379-aa7f-f079b273eaf6 | -3.8008 | -41.5989 | 2024-10-09 00:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 8001013b-4c11-3397-bd31-8d7e8aaf81d0 | -3.8196 | -41.5979 | 2024-10-09 00:45:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 78591f47-3fbd-3088-8000-fe072dc6fdfe | -3.9021 | -46.4689 | 2024-10-09 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 89f67dfa-655b-3912-b6c5-72280eb4f437 | -3.9023 | -46.4467 | 2024-10-09 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 285bd5b3-742e-3b0d-b309-d2759d811327 | -3.9207 | -46.468 | 2024-10-09 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 13bc9e7e-802c-3672-8eea-173bb9ad0d49 | -3.9208 | -46.4459 | 2024-10-09 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 004e384a-8e47-3a11-bf80-222a9d1abf00 | -3.9393 | -46.4672 | 2024-10-09 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7797d16e-fbb8-38bb-86ac-e6aa105c3869 | -3.9394 | -46.445 | 2024-10-09 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| f6c916ff-189d-33e8-a0c6-cfe94f5e7141 | -5.4421 | -49.5559 | 2024-10-09 00:45:37 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7e0fa886-0de0-394c-9f58-3f5e1de0b16c | -5.8216 | -44.1196 | 2024-10-09 00:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f893a714-a0fd-34a1-add4-408f05d0b0d5 | -6.7613 | -60.0751 | 2024-10-09 00:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.5 |
| dca170b6-ef67-3d1f-a6aa-5873bd67c78e | -6.7614 | -60.0559 | 2024-10-09 00:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 005d4d62-e6fb-3c00-8894-aa55f3a780a4 | -6.7615 | -60.0367 | 2024-10-09 00:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9c39ebe2-7ffa-3c17-b1cc-02e289b16d7f | -6.7797 | -60.0744 | 2024-10-09 00:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| c145faae-bd8d-31b0-9fa8-16dc4b78d92b | -6.7798 | -60.0552 | 2024-10-09 00:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 233.1 |
| 7b999e90-e94d-3145-9529-0bc59d212c0d | -6.7799 | -60.036 | 2024-10-09 00:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 85ac7ccd-f799-3603-a653-7407aa14e95a | -7.0231 | -59.4303 | 2024-10-09 00:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 5c6b836d-68b3-3d80-a6c2-52ba4d2fdc81 | -7.0232 | -59.4111 | 2024-10-09 00:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 453a9b4b-af67-337e-bc68-354516d9350c | -7.0417 | -59.4103 | 2024-10-09 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 9bc25d21-fd1f-3608-a63f-16589f36605b | -7.1871 | -59.7893 | 2024-10-09 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e045f31f-aabe-3c0f-b886-995078dbeb72 | -7.1873 | -59.7701 | 2024-10-09 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b98cb06a-7afd-3b86-ab39-5b4564277ca7 | -7.2435 | -59.633 | 2024-10-09 00:45:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| e8160cb3-e0b3-3f21-97dc-e675227c309b | -7.2619 | -59.6323 | 2024-10-09 00:45:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 89445633-a388-3928-98e1-e0e6084e4330 | -8.4919 | -48.6476 | 2024-10-09 00:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 200.2 |
| 9f1e484a-85b5-3573-b049-fcd57b8b517a | -8.4921 | -48.6259 | 2024-10-09 00:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 85e4a8c5-8bd6-3cd7-857e-86be8a260f23 | -8.5107 | -48.6459 | 2024-10-09 00:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 140.3 |
| a7efbdc5-e217-3f96-a3e6-9f734c24d326 | -8.5109 | -48.6242 | 2024-10-09 00:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 95.2 |
| dead3dc5-4e8a-3153-a32e-94b8b1dd6a41 | -9.0543 | -63.2375 | 2024-10-09 00:45:58 | GOES-16 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 048dad0c-e69c-3e54-a927-943795436830 | -9.1573 | -61.5803 | 2024-10-09 00:45:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ef08d97e-fcc3-3688-bc8f-df729792d5c5 | -10.0438 | -36.4015 | 2024-10-09 00:46:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 84.0 |
| f5b0a843-a580-3e41-97e6-05d22c66069f | -10.3894 | -61.2502 | 2024-10-09 00:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 52895456-a834-34df-90be-391c364e3257 | -10.3895 | -61.231 | 2024-10-09 00:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 182fbae9-72a5-3d85-8a88-d3a95a5d768a | -10.3843 | -64.8255 | 2024-10-09 00:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 09c5151c-7ada-3174-9a2a-5a74e29858fc | -10.4287 | -60.9979 | 2024-10-09 00:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 40d1533e-52e7-3ded-9c15-09a7bed95e6d | -10.5902 | -57.5333 | 2024-10-09 00:46:07 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 72fa0c95-757e-38a5-9180-542329cd604e | -10.5943 | -64.024 | 2024-10-09 00:46:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 4eb94954-6262-39e2-9923-6da3f340c50a | -10.8567 | -63.9177 | 2024-10-09 00:46:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 72314483-4e42-326e-931d-2aae64917e4d | -10.8568 | -63.8988 | 2024-10-09 00:46:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b969b2f2-20fe-3bde-8ba3-df0a284edb07 | -10.8754 | -63.9169 | 2024-10-09 00:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 120.9 |
| cc76c6c8-2e15-30e5-9b56-87cb41ff9fce | -10.8755 | -63.8979 | 2024-10-09 00:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| a78c9200-bf8d-30c3-8381-ffd85601fe07 | -10.8925 | -64.1623 | 2024-10-09 00:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d87fdb43-e2ca-39e1-8b67-6431fb35fc94 | -10.8941 | -63.916 | 2024-10-09 00:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| ed5fa983-c2b1-39e8-bc5e-f2bbfc27329f | -10.9112 | -64.1615 | 2024-10-09 00:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 169.8 |
| f0e94199-30df-382f-b838-230000bf7c72 | -10.9113 | -64.1426 | 2024-10-09 00:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 204.2 |
| 1f5a1301-6cb2-3996-abd6-d510572e83c3 | -11.3838 | -51.0807 | 2024-10-09 00:46:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 9a1f2829-e2d4-3270-a763-71c7b29404eb | -11.464 | -49.4853 | 2024-10-09 00:46:11 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1de2aa49-4586-3a69-b0f4-2563058beb09 | -11.483 | -49.4831 | 2024-10-09 00:46:11 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 8f591872-0727-3e69-84b6-3851b8b4dcba | -11.5728 | -58.9423 | 2024-10-09 00:46:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 20ccdcaa-8668-3ced-9cb0-4df5f5c664f4 | -11.5726 | -58.9619 | 2024-10-09 00:46:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c7b207a9-a703-3fd5-b96a-369c1c9c7ab1 | -11.6806 | -64.0312 | 2024-10-09 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 3e6f265c-eb11-305f-b7b6-916ee3552981 | -11.6808 | -64.0121 | 2024-10-09 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0c600e0d-d07f-306c-a7d1-decfe7046a2c | -11.9917 | -51.0766 | 2024-10-09 00:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| fd6ec11d-75f8-3130-99d9-e2ad1184f152 | -11.992 | -51.0553 | 2024-10-09 00:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 575339f1-44fe-362f-abe5-493b3583d606 | -12.0107 | -51.0744 | 2024-10-09 00:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 562acf35-79be-3e60-af5d-b7c567239425 | -12.011 | -51.0531 | 2024-10-09 00:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 303.2 |
| 63e0b07a-d913-340e-b587-0a87138b1364 | -12.0298 | -51.0722 | 2024-10-09 00:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3d821317-2d09-3aa1-9c36-e1e36f5bccfd | -12.0301 | -51.0509 | 2024-10-09 00:46:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 96685284-1cb4-32de-8dcb-30c7f71cc46f | -12.7673 | -44.8904 | 2024-10-09 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 6d37f9b2-55a3-35bd-b2a0-4b05102b42d3 | -12.7678 | -44.8671 | 2024-10-09 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 6aa55c6d-5a82-356a-9b29-4edf3028452b | -12.6676 | -63.0819 | 2024-10-09 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 110.9 |
| e5a1e743-c091-35b6-9487-353802ad8dd1 | -12.6876 | -62.9464 | 2024-10-09 00:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| eeb2be29-ce69-3bbd-acf1-f06ce63fc632 | -12.7501 | -62.269 | 2024-10-09 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| eaf5ec39-031c-3de0-afca-d7e065bf4cc5 | -12.769 | -62.2678 | 2024-10-09 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 8c0266b1-baa9-357a-a2ae-3a4062de2211 | -12.8589 | -62.8211 | 2024-10-09 00:46:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 119b7023-3c85-30ee-8533-89f82587f9a0 | -12.8591 | -62.8018 | 2024-10-09 00:46:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 236.8 |
| 84f41c8f-4d06-3633-b133-ac4f24a94e9d | -12.8779 | -62.82 | 2024-10-09 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 137.2 |
| e52710e0-e363-3431-be62-8ce8012aca8b | -12.878 | -62.8007 | 2024-10-09 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 357.4 |
| 5a575e1f-9fce-30d8-a5ae-9d210eaf9ce5 | -12.8782 | -62.7815 | 2024-10-09 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 267152de-ce31-3fb7-ad80-44efd9322d20 | -12.897 | -62.7996 | 2024-10-09 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 830910b9-ee5b-3b00-b0a2-cded56519dcd | -12.9166 | -62.7214 | 2024-10-09 00:46:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ddc7db15-e783-36cc-bf4f-81b874c6c32d | -13.3978 | -61.9376 | 2024-10-09 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 117.2 |
| ffa54020-a11e-3aa5-8019-f11c4c1f56f8 | -13.398 | -61.9182 | 2024-10-09 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 137.8 |
| ef1c638e-7ba4-35d3-9da7-ee54f22ede74 | -13.417 | -61.9169 | 2024-10-09 00:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c07e1349-7faa-35c5-b2cd-d967b203367b | -14.1192 | -44.9872 | 2024-10-09 00:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| d5c6a44a-d9f1-3449-a357-41fe0af8fe8c | -14.1197 | -44.9637 | 2024-10-09 00:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 51f5c2d8-3880-3acc-b535-f82edc3cd9ef | -14.1387 | -44.9837 | 2024-10-09 00:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 91a9f886-97e7-3b6d-a848-1c49496c9a16 | -14.1392 | -44.9603 | 2024-10-09 00:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 26646b1a-3138-39c8-96e1-dc8c8f4d82e2 | -15.5996 | -57.3699 | 2024-10-09 00:46:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| eb950866-4d6e-3d24-8d42-233fbaa08305 | -15.7076 | -59.3726 | 2024-10-09 00:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 004b4f56-164a-3324-8480-0fb31e94c52a | -16.3988 | -55.9479 | 2024-10-09 00:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 9fdda82d-c519-3142-958a-7aaa4b4a01e4 | -16.3992 | -55.9272 | 2024-10-09 00:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.4 |
| bbf580e7-3602-339c-828f-ad1544fcfbb3 | -16.4184 | -55.9455 | 2024-10-09 00:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 120.9 |
| f6410e36-c02d-34da-b13f-fded5f679b23 | -16.4187 | -55.9248 | 2024-10-09 00:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| b81849ee-b4aa-3461-9f01-de03ab092d72 | -16.4379 | -55.9431 | 2024-10-09 00:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 99cdcf19-faf9-369d-85e0-e2f3067f4054 | -16.4383 | -55.9224 | 2024-10-09 00:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |


[Clique aqui para ver as próximas entradas](README21.md)

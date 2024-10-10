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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 291e4f60-a600-3aad-b830-5277e9a2b824 | -11.0443 | -57.2222 | 2024-10-10 00:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 328.6 |
| 92aa1bb2-2a3e-37b1-b3e4-e35e910ae261 | -11.0445 | -57.2023 | 2024-10-10 00:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 278.2 |
| 79575316-6011-3d7c-8fe9-41595cec85b9 | -11.5349 | -44.0324 | 2024-10-10 00:06:11 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| de848f73-8b6a-3aad-b6b7-90278b23b5db | -11.2575 | -60.4855 | 2024-10-10 00:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 14175b28-20cc-3767-be01-781ba675090b | -11.2582 | -60.4079 | 2024-10-10 00:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9a314c19-2c82-32da-8af2-bb4e15072abc | -11.2583 | -60.3885 | 2024-10-10 00:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6457a08a-7d1a-3f7c-8828-bfe2d95d181f | -11.2763 | -60.4844 | 2024-10-10 00:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e0310c80-4f8c-39ee-94eb-b64d5e4ef082 | -11.277 | -60.4067 | 2024-10-10 00:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9fbd676a-6fd7-3c8f-a8a8-76c1f5c7bb0d | -12.1955 | -46.7396 | 2024-10-10 00:06:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7d707ad0-ef45-3e0f-b5e1-56f949e092f9 | -12.1958 | -46.717 | 2024-10-10 00:06:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ee0bcfe9-af4b-3c56-b85b-5c78098df1b6 | -12.2147 | -46.7369 | 2024-10-10 00:06:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 3456fcca-e94b-3ac1-aa5e-39d4419b59db | -12.215 | -46.7143 | 2024-10-10 00:06:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| fd09340b-cde4-3a3d-b289-025b8a3363e5 | -12.663 | -54.7193 | 2024-10-10 00:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 754000f2-a0e2-3994-897a-2b747929765d | -12.7245 | -63.0595 | 2024-10-10 00:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 99af78e9-8328-313d-be72-54dc191b831f | -12.9255 | -51.1361 | 2024-10-10 00:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 98309e36-28f2-3ef5-aaf6-86f3bb7caa1c | -13.4083 | -44.6907 | 2024-10-10 00:06:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ec67ff8f-6db4-3f61-b42d-3bb4aa1784ae | -13.5131 | -44.2971 | 2024-10-10 00:06:22 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| a7d4a0d6-8643-326b-a293-cc88070385d8 | -13.5321 | -44.3173 | 2024-10-10 00:06:22 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 55fec901-c1f1-3180-9885-b54ca5031d66 | -13.5326 | -44.2937 | 2024-10-10 00:06:22 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 7ed843c9-5fe5-38fc-9048-e534d60bc1b8 | -13.8374 | -44.5455 | 2024-10-10 00:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| daa8e942-bdf3-3d71-8288-2f90486b0dd1 | -13.797 | -44.6231 | 2024-10-10 00:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ea5f057e-ee8a-39fd-b32c-7d4b098b3e13 | -13.8179 | -44.549 | 2024-10-10 00:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d7cc5ee9-979c-3818-863d-f9b7eae4ac45 | -13.8184 | -44.5254 | 2024-10-10 00:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2c2e471c-1bc1-30ae-b49c-cee772c5f374 | -13.8379 | -44.522 | 2024-10-10 00:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 0e70f631-1fc6-3217-b424-00ff7f5136c1 | -13.8569 | -44.5421 | 2024-10-10 00:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 3fae53a2-3046-388d-b296-29656bf6630c | -13.8574 | -44.5185 | 2024-10-10 00:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 5fc4bee3-9d1f-3e4d-aad0-2534ebe9796a | -13.8579 | -44.4949 | 2024-10-10 00:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4b18e26e-e714-39ec-b6d8-0dc454e566bb | -20.3148 | -48.7121 | 2024-10-10 00:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 01e04377-1c5d-3617-a61e-468dcc273d8c | -21.416 | -57.2048 | 2024-10-10 00:07:05 | GOES-16 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 4f8dd745-cf7a-3b45-a88c-0ff0dff125da | -13.94015 | -42.56115 | 2024-10-10 00:13:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 7dd0f93b-287b-3662-b5b6-5c0c03d387bd | -15.40495 | -43.05102 | 2024-10-10 00:13:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 15.7 |
| aad1ce0c-053d-3fba-9ae0-f8bf9e1ac4df | -14.08474 | -44.15819 | 2024-10-10 00:13:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 280cfcd9-2ef9-387d-9643-05882ae432f3 | -14.06983 | -43.6887 | 2024-10-10 00:13:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d8d632dc-b3fa-379c-bce0-92382ae592ef | -14.06031 | -43.69624 | 2024-10-10 00:13:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| ff54f0c4-cd6d-37bb-a765-c3fd6138304f | -14.04424 | -44.04311 | 2024-10-10 00:13:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 2bdd830b-9614-3b5e-b7e5-80d62aef3b03 | -14.0417 | -44.01975 | 2024-10-10 00:13:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| bd3f84d3-7a65-3c4a-959d-47049a20ed12 | -14.74899 | -41.68745 | 2024-10-10 00:13:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 69983043-9810-35d0-86bf-4c2e38b98d67 | -1.2541 | -55.7101 | 2024-10-10 00:15:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 105c201f-b650-3df4-94ac-92435cd19430 | -1.2541 | -55.6904 | 2024-10-10 00:15:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 48651b00-c6ee-3aa3-aec3-230701383a2d | -3.2571 | -54.1824 | 2024-10-10 00:15:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 49d9ea81-33a4-30dd-b10a-54cb4e290eda | -3.3341 | -53.232 | 2024-10-10 00:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a0df4f3d-5e43-3928-87aa-40a18bcc5418 | -3.3342 | -53.2117 | 2024-10-10 00:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 07d158c0-7bd3-36b1-bafb-9003af9d12cb | -3.7247 | -44.9547 | 2024-10-10 00:15:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9b8ef401-0763-3c26-89e5-3552e4c51815 | -3.7961 | -45.4927 | 2024-10-10 00:15:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 60618f43-cbf4-3b18-8f19-2a99fc918273 | -3.8146 | -45.5143 | 2024-10-10 00:15:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| fd60381d-be37-3119-99b9-de297161ffb3 | -3.8147 | -45.4918 | 2024-10-10 00:15:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 156.3 |
| c5e7ec4f-480a-343c-98a9-82d18783f667 | -4.0961 | -48.2739 | 2024-10-10 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 173.8 |
| b21b3713-a2b5-34dc-9d08-a43ffb1e5acc | -4.0962 | -48.2523 | 2024-10-10 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 83d76565-7237-378f-b153-41ca9eb82cfd | -4.1102 | -49.0675 | 2024-10-10 00:15:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 66c7cc2f-520f-3f69-bc28-18873562f048 | -4.1146 | -48.2731 | 2024-10-10 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 175.0 |
| b6366524-fd58-3fb6-85d6-fdbbb1a6d534 | -4.1148 | -48.2515 | 2024-10-10 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 62c71ca5-1322-3bc0-bb61-02a72bf6f38b | -4.2802 | -45.4688 | 2024-10-10 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ca7c3d0f-b976-3387-a9f9-97d37e2dcd7a | -4.4775 | -46.6177 | 2024-10-10 00:15:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d07924bf-408a-3ff7-872e-d6a03c2338fc | -4.4776 | -46.5956 | 2024-10-10 00:15:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 239.3 |
| 1cbc6405-4834-3c5e-8067-c6033151945b | -4.9513 | -42.9973 | 2024-10-10 00:15:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2f46196f-b051-3b2b-aadf-dc66dcd231a3 | -4.9515 | -42.9739 | 2024-10-10 00:15:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a579034f-438e-38ad-9329-ab99ae84947e | -5.1904 | -41.2923 | 2024-10-10 00:15:35 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 3489819f-93dc-3fc2-9736-2e9e4c52a263 | -5.2361 | -44.8018 | 2024-10-10 00:15:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0fe1c694-d18b-33d6-bfcb-a2ed4f8b791b | -5.3946 | -45.9865 | 2024-10-10 00:15:37 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a91dc03b-4884-3957-afb6-64b649e25dc5 | -5.4833 | -44.2822 | 2024-10-10 00:15:37 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 4b7ad30f-52b1-308b-9e57-972c708f477b | -5.9034 | -45.4353 | 2024-10-10 00:15:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 62335488-6737-3605-85dc-b4ea8d903d7d | -5.9036 | -45.4127 | 2024-10-10 00:15:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 57023b3b-0774-37a5-bcee-39c878010cbd | -5.9221 | -45.434 | 2024-10-10 00:15:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 62cc1c7e-d835-3ace-a8a7-d0b720be713c | -5.9223 | -45.4114 | 2024-10-10 00:15:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 0d871ebb-9345-3d01-a1a6-8da3e0cc95b0 | -6.5218 | -60.0649 | 2024-10-10 00:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 99d93cbd-0e15-3e35-ba82-ce795e364079 | -6.5219 | -60.0457 | 2024-10-10 00:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8176ecde-078f-3dc8-a05c-26a3c27ce59d | -6.747 | -59.3259 | 2024-10-10 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ce2f0b8e-fd57-3d17-b9ae-c2e1c9b32a5c | -6.7654 | -59.3252 | 2024-10-10 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 0af6227d-0522-3c6b-bde6-e1973052628d | -6.7655 | -59.3059 | 2024-10-10 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b733dd83-3c3b-34b9-b139-4ad5d5f1c134 | -6.7798 | -60.0552 | 2024-10-10 00:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 6424297f-4de7-3a54-ac35-2c7c110f1865 | -6.7799 | -60.036 | 2024-10-10 00:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 7a7606f8-4835-3f2a-88dd-9ce005c3ca8e | -6.7839 | -59.3245 | 2024-10-10 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 97b9eb38-7da3-32f3-bc0c-cc73c3b98a19 | -6.784 | -59.3052 | 2024-10-10 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 1b720d73-de59-355e-9cf7-f92b3bfa320e | -6.9532 | -45.2846 | 2024-10-10 00:15:45 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 158.6 |
| e2c32074-2b11-384d-b8c6-ef8f45121a48 | -6.9535 | -45.2619 | 2024-10-10 00:15:45 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b1f063eb-43c5-32d2-95ac-806b77d061ed | -7.0416 | -59.4296 | 2024-10-10 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 6f2f11fb-7104-38c3-bd7f-bfcced064553 | -7.0417 | -59.4103 | 2024-10-10 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 35db9dbd-3865-3354-8453-752f1f4291f5 | -7.06 | -59.4288 | 2024-10-10 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 9cb0bffa-d445-3671-b7d2-55e11618540e | -7.0601 | -59.4095 | 2024-10-10 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 21c467fd-46bf-384a-bff2-0588aa234dcf | -7.1341 | -59.3871 | 2024-10-10 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| a70071b1-5682-3797-bb84-2de077c74b81 | -7.1342 | -59.3678 | 2024-10-10 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| da64e395-9d83-3457-84c5-5b47de637ea9 | -7.1346 | -59.3099 | 2024-10-10 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c6b91f78-c532-30a8-90ef-3225e5e32de4 | -7.153 | -59.3092 | 2024-10-10 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| b20f2bc6-6b2d-3234-b142-947145559177 | -7.3942 | -46.1472 | 2024-10-10 00:15:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ad2fdfb5-b6e8-34a6-a633-ebdfd3aa9f32 | -7.5746 | -46.8 | 2024-10-10 00:15:49 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2026176f-2d4f-37dc-b7c3-d75f1444ed98 | -8.2325 | -61.1823 | 2024-10-10 00:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 16c8c886-e29d-3bad-8b35-7e6456a051b5 | -8.6173 | -54.5924 | 2024-10-10 00:15:55 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 595a8734-1cfe-3942-aeb8-a2e8357e921c | -8.6843 | -63.1009 | 2024-10-10 00:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| bc161981-c30f-3abc-be15-e75f83b456fb | -8.6844 | -63.082 | 2024-10-10 00:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 84cf96a6-57d3-32a9-b6e5-efa555823481 | -8.7028 | -63.1002 | 2024-10-10 00:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a09a896f-3e67-3f8e-8c5e-85e6bf05001d | -8.7029 | -63.0813 | 2024-10-10 00:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| e0431b35-1ce4-3b30-9865-5c875de56345 | -8.8422 | -61.4992 | 2024-10-10 00:15:57 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 56b1f7a7-40f8-3e12-81a4-f3ecc31d703d | -8.9898 | -61.6261 | 2024-10-10 00:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b9a30fee-80f5-36ca-b8ca-d7592d2c579a | -8.9899 | -61.607 | 2024-10-10 00:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 344881d4-a9cb-3cd8-9dcc-3f8ee16b3a30 | -9.0084 | -61.6253 | 2024-10-10 00:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9e86ccc9-49a1-31d7-a233-276fb1e6c32f | -9.0085 | -61.6062 | 2024-10-10 00:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9a038212-24e1-3df7-9703-2b436187a22a | -9.027 | -61.6244 | 2024-10-10 00:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 289a7983-d8d7-385c-9a88-9affa1981689 | -9.0271 | -61.6053 | 2024-10-10 00:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 98.9 |
| daf987c3-ef02-332d-a17a-a0f0a18b8b74 | -9.0656 | -61.3934 | 2024-10-10 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 331d990c-30ec-336a-b673-016a73230ffc | -9.0841 | -61.4117 | 2024-10-10 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |


[Clique aqui para ver as próximas entradas](README3.md)

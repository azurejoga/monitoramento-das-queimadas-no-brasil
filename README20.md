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
| a3cfd901-f1fe-3910-934a-b59f8f31054c | -21.36559 | -48.7658 | 2025-05-22 04:49:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2297b89a-d990-3113-a947-6b2833020613 | -20.94547 | -56.58584 | 2025-05-22 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6b47379d-7089-339b-ae56-33b2fcef1163 | -20.94823 | -56.59053 | 2025-05-22 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 22.6 |
| fdc2960d-a153-316a-a226-9342173bc1e4 | -22.95256 | -49.10965 | 2025-05-22 04:49:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ef13a29-4a0f-3bf5-8981-43924615ac43 | -21.3661 | -48.76179 | 2025-05-22 04:49:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b22fbd3c-4f95-3fe5-ad9c-2f1ff9048cc1 | -22.54156 | -48.81271 | 2025-05-22 04:49:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07c800bc-76b2-3e4b-9874-247630eb1546 | -21.25242 | -50.3052 | 2025-05-22 04:49:00 | NOAA-20 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a661ed9e-1d16-369a-9c2e-54756ec2b17b | -18.91222 | -54.48153 | 2025-05-22 04:49:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 049396fc-5db9-3a0f-96e2-8109c739c36f | -19.2589 | -55.1465 | 2025-05-22 04:49:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7670464a-b1d0-333c-ba11-b293bb5f724f | -11.5719 | -47.4521 | 2025-05-22 04:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 05749a04-2ac7-363b-8066-7c9cdf1522d0 | -11.5528 | -47.4546 | 2025-05-22 04:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1e07764d-393e-3609-a706-3256481bdeda | -11.5528 | -47.4546 | 2025-05-22 05:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 776c81a5-d9d6-37a6-b24c-bd00d4cecc71 | -11.5719 | -47.4521 | 2025-05-22 05:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 0fe5b753-2fc7-3e09-aab4-035e57e154b4 | -11.56423 | -47.4408 | 2025-05-22 05:04:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| d868c547-4e07-3772-aa4e-71cdaefe23f7 | -11.57323 | -47.44728 | 2025-05-22 05:04:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a05549cb-608c-3360-bc33-271346ba6a97 | -11.55716 | -47.44435 | 2025-05-22 05:04:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 5402a4e2-79c8-3fc0-804c-a419a521fdb0 | -11.54816 | -47.43786 | 2025-05-22 05:04:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| f129986b-50b0-3a4b-b3c3-0cdbe54ff21b | -22.16322 | -42.94089 | 2025-05-22 05:08:00 | AQUA_M-M | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| ab7b5e00-342a-37d0-a902-d2084b2011ec | -11.5719 | -47.4521 | 2025-05-22 05:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| e3a1d306-d2ee-3056-858a-68d47587222d | -11.5528 | -47.4546 | 2025-05-22 05:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 82a5ac3f-0f71-339d-a6eb-4f6fefaf7900 | -11.5723 | -47.4298 | 2025-05-22 05:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| b5a4ea07-d45c-398e-b3e5-a897cf6a664b | -11.5528 | -47.4546 | 2025-05-22 05:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 70bf4878-f9b4-3253-afe2-183145358688 | -11.5719 | -47.4521 | 2025-05-22 05:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| be787a0b-7333-3605-840f-49232c108180 | -11.5719 | -47.4521 | 2025-05-22 05:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 291634c5-7ea3-3449-b097-0eb0c6dea0a7 | -11.5528 | -47.4546 | 2025-05-22 05:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 05dafc79-f6a7-3b96-beef-6cd34cb8e0b9 | -10.70642 | -59.12455 | 2025-05-22 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6eeaffa4-a2c5-3ba9-8199-29ae09b70d90 | -11.1139 | -54.66068 | 2025-05-22 05:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59d0c0e4-0e12-37b1-90a0-8fbfff341ba0 | -9.4213 | -58.31633 | 2025-05-22 05:36:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d5d67e7-37ba-3453-9e3c-73933399e275 | -9.4233 | -58.31772 | 2025-05-22 05:36:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 142a3caf-d7cf-3959-85d0-a5d50779247a | -11.11911 | -54.66519 | 2025-05-22 05:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ecceebc1-a5c9-3ee2-a2b8-2ceeee009719 | -11.29538 | -53.9813 | 2025-05-22 05:36:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 24d92ccf-d9a1-3b91-9ba7-d023a326f1f4 | -11.08234 | -54.77961 | 2025-05-22 05:36:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a46a4998-b410-3470-bdac-6ef0d08f99e7 | -9.57752 | -62.46901 | 2025-05-22 05:36:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5356cdc-12d0-30da-9394-7c03540602ac | -11.3013 | -53.98218 | 2025-05-22 05:36:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 437e5f18-f4b8-3224-b5e6-ce936ea7fd88 | -8.16686 | -61.47678 | 2025-05-22 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fcb4dde-94a0-3378-8ef5-0da0ca30ca69 | -10.70845 | -59.12638 | 2025-05-22 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29c7ba74-5f94-351c-88f1-bca353df7f6e | -10.68641 | -57.5995 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69b45766-e377-3145-bdc8-fc7cc053ee9e | -10.82608 | -56.95845 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 581b370e-0520-3be7-8eab-4c343819424a | -11.11958 | -54.66135 | 2025-05-22 05:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cad92841-08a3-3490-ab85-451e78707186 | -9.42186 | -58.31216 | 2025-05-22 05:36:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fc0367a-17aa-3795-9329-7c0cac15eb8b | -6.63146 | -55.01297 | 2025-05-22 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19382cb3-7888-3dce-a050-1e5030c4ba45 | -10.68574 | -57.60447 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7648f10-476c-3135-9b51-98d43bd17582 | -10.83161 | -56.95381 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f062da6f-d788-34ba-b8bc-455480cd6e61 | -11.08281 | -54.7757 | 2025-05-22 05:36:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28abe5b9-7795-3d9a-a83a-fc34ef785935 | -10.12092 | -58.22084 | 2025-05-22 05:36:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ff89564-2560-304d-9bc8-700a50d472f7 | -10.68115 | -57.60368 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a401dfc4-9913-3b71-b0f1-339964345513 | -11.08187 | -54.78352 | 2025-05-22 05:36:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3af7da4-d78c-382b-80e8-46be886bee38 | -10.70485 | -59.12182 | 2025-05-22 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21eff73b-66db-347e-a5d6-7ad211a8262f | -11.11344 | -54.66449 | 2025-05-22 05:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a159c72b-6746-3294-b5e1-2b1347682dfd | -9.41957 | -58.31297 | 2025-05-22 05:36:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 532161ff-da7e-34f7-8448-3c315b0c0369 | -11.29589 | -53.97699 | 2025-05-22 05:36:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a73e509-dd7d-3956-90a8-db6393771a14 | -9.16612 | -61.40401 | 2025-05-22 05:36:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 016aed7b-3d59-3301-9d81-bf26d54c4eb7 | -10.82539 | -56.96381 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7d7930f4-9990-3bae-96ae-d2d12817f599 | -9.57318 | -62.47284 | 2025-05-22 05:36:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4384272-23eb-3766-9137-671e5cac90c6 | -9.4129 | -58.32898 | 2025-05-22 05:36:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2842d785-0e6a-3277-9e4e-c0e9323e83ad | -8.16745 | -61.47283 | 2025-05-22 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71099f52-4965-31ab-ac51-538ae865c4ae | -10.93703 | -55.32259 | 2025-05-22 05:36:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8672c297-4a4e-3bd7-9ce3-ee11bd32c75d | -10.38099 | -57.64402 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a03f3e04-c8d7-37e3-81f8-44083ab9bf2f | -10.68048 | -57.60862 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0be9bd58-cd5d-3417-93d9-94ade1bbb5fd | -11.08328 | -54.77178 | 2025-05-22 05:36:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d55b308-0213-30ff-ba1d-21db8c9439cb | -10.12033 | -58.22515 | 2025-05-22 05:36:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b160962e-c608-33bb-9e6b-97265b3f508c | -10.381 | -57.64273 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f10c3974-0c0f-3a62-871a-460bc86c11dc | -9.86019 | -60.3196 | 2025-05-22 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f73907fc-b202-3f0e-b8a4-f7abb04ec6d4 | -10.83091 | -56.9592 | 2025-05-22 05:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4350b998-786e-3f12-aca6-fe33eed09b5a | -9.29258 | -57.55425 | 2025-05-22 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6682ec8a-8a34-39cd-8660-7e4d6a1171dd | -9.42389 | -58.31357 | 2025-05-22 05:36:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e2c5ee2-6e05-3bd9-9b20-99cd9e006fdb | -9.57717 | -62.46964 | 2025-05-22 05:36:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4ef3e94-abcf-35de-997b-9adff462885e | -10.29871 | -57.14241 | 2025-05-22 05:36:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e4f3586-5929-3862-8f25-b42f51c38024 | -6.63665 | -55.01377 | 2025-05-22 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f4d5c69-7d18-3a57-acfc-819e543d6247 | -10.69452 | -59.10467 | 2025-05-22 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28c218f5-f70a-37c6-af6e-399388bf982c | -10.31305 | -59.56811 | 2025-05-22 05:36:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f75a550f-0301-3653-b180-5a2a3903cabf | -6.6371 | -55.01065 | 2025-05-22 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b20f726-2cbd-353c-8835-1578058867fa | -11.29488 | -53.98557 | 2025-05-22 05:36:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 297612bd-682e-31bf-9a55-861c1eecf212 | -14.02975 | -53.37629 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7246fc1d-8776-3961-87be-7b3922582f25 | -12.68795 | -58.13084 | 2025-05-22 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71ba24f7-f9f8-39d6-b34f-70227727aba8 | -12.47302 | -54.46527 | 2025-05-22 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a30d286-aef1-3799-b930-a8881bb827be | -13.47822 | -52.27859 | 2025-05-22 05:38:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 845d58ae-1c49-34ba-96ea-98d694895a52 | -12.30258 | -52.50751 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1938262d-2464-38e7-9d32-e60376a63e0e | -10.05583 | -65.00229 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abe9f1f1-220a-353c-892f-f5a8b87fa042 | -12.64514 | -57.18905 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b2137e1c-5951-36c2-815f-9f8e54540018 | -14.03612 | -53.37709 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5134b00b-1cd6-360d-b0c3-a6da716b06dc | -12.02562 | -63.79211 | 2025-05-22 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2801ed11-91a8-301e-8656-cb707928deb0 | -16.28071 | -58.66595 | 2025-05-22 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| aa23514a-5d68-37c4-aa19-0407eb40d735 | -12.02617 | -63.78849 | 2025-05-22 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a2f1308-ba0f-31f9-a517-9109759943e0 | -14.17227 | -58.32173 | 2025-05-22 05:38:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 181e8c78-4c98-393d-b019-9c154856be46 | -12.48537 | -57.18736 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7b1d7a47-0e33-327a-a9fc-db4b91776375 | -12.66342 | -58.215 | 2025-05-22 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cf4e2a8-173f-325a-b283-8c5c5cd6a91c | -12.28475 | -52.50043 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8b7fc75a-025b-3dce-8936-88f62ec95de7 | -12.28605 | -52.48896 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 321c91f2-c344-35e6-a69a-bfe569c0cc5e | -13.78619 | -54.31288 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baa43948-7702-3527-b820-5a3d17b5afdf | -11.66837 | -54.93863 | 2025-05-22 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fa3f460-5cf5-3ab5-8fbe-33a8978e30e5 | -12.72559 | -54.97312 | 2025-05-22 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 43a5afb3-8e27-34c9-8541-81dd14346e34 | -14.02551 | -55.14355 | 2025-05-22 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b678caec-3320-3ac4-b593-c4626964bdc6 | -12.48835 | -57.18958 | 2025-05-22 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf3ad3cf-2f82-3de5-8c36-f75943410dd3 | -14.01547 | -55.1297 | 2025-05-22 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa0ff9ba-ddd9-3469-954f-0a0b8e3629a6 | -12.30448 | -52.50293 | 2025-05-22 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 12e994e4-b878-34cb-bf6b-c584da563823 | -13.78669 | -54.3083 | 2025-05-22 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94672d8d-41b4-3fa6-b082-a1c50e9de31d | -12.47254 | -54.46453 | 2025-05-22 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32fc6f2f-515e-3c4f-94c9-160ac16867d8 | -16.38503 | -54.57654 | 2025-05-22 05:38:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebcdbfc6-6056-3c6f-bce2-45e869223743 | -11.67 | -54.93777 | 2025-05-22 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)

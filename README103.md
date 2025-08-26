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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 235148a3-4b1f-3e93-a25c-26d668a46e08 | -8.08408 | -47.34467 | 2025-08-26 12:53:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| ce211546-bfec-35f2-bad3-d5adc2f92737 | -9.62802 | -49.76751 | 2025-08-26 12:53:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 18a5cf5d-4c20-329e-82a0-508721811118 | -8.43105 | -48.2514 | 2025-08-26 12:53:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| c08e2d32-edec-3343-9d00-a8b78ddb89fa | -2.93202 | -53.69152 | 2025-08-26 12:53:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 31e64769-e5f5-3580-8aed-120bd595086a | -6.82064 | -58.96186 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 22916021-4f02-302e-9f70-9148a4eb1a8e | -4.70219 | -56.063 | 2025-08-26 12:53:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d8d00b9e-46d2-3dae-8fd1-94dac9ddd48f | -6.23418 | -60.02515 | 2025-08-26 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e3b6f5ac-3c0a-30d7-923f-f82371951ac4 | -6.81884 | -58.97379 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d0d5f871-9abf-32d9-a842-b8fd6a30629d | -7.36009 | -59.66072 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 9b46af08-c775-3764-8fc0-266ba6b53095 | -7.42017 | -60.62315 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e8600816-5c1b-377c-8f8e-c5661037c8f6 | -7.52709 | -61.32549 | 2025-08-26 12:53:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cdb6960a-445b-3dbc-958e-c110519f4cc1 | -8.42634 | -48.24539 | 2025-08-26 12:53:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 3978f4ea-7894-3e82-bcb1-bf797a961700 | -6.80314 | -44.98278 | 2025-08-26 12:53:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 3b3ae0f7-f5e6-30b9-b2a6-6d6b099c1e7f | -7.25954 | -57.68482 | 2025-08-26 12:53:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e11b26bc-651c-325b-8f50-d9ddaecf5ac2 | -6.84096 | -58.96481 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 90e13c7c-a0bb-35c0-bbdf-702ac6f400da | -5.76003 | -53.77233 | 2025-08-26 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 754f36c2-a8fb-332c-a845-823fc0ad9be7 | -3.58772 | -49.43732 | 2025-08-26 12:53:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9fb3c9dd-526f-3bcc-89aa-743d4455f059 | -6.80324 | -44.98808 | 2025-08-26 12:53:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 95c3dc47-a924-3149-b1e3-63347bc63fdc | -6.92275 | -59.36551 | 2025-08-26 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| efe81242-f022-3061-bea6-42686c8dc213 | -4.96017 | -55.81581 | 2025-08-26 12:53:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| c2b46ae7-20b1-3ddf-b35a-c9d7b6191d44 | -10.68267 | -47.16115 | 2025-08-26 12:55:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 7a631426-1200-3309-af8a-04dccfe082bd | -11.3124 | -55.11182 | 2025-08-26 12:55:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 4a31f2b7-6e82-3ba7-bd7d-29472ee90990 | -9.23921 | -60.92356 | 2025-08-26 12:55:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 0fd803c7-b8e6-3fed-8b33-2ae960ff07af | -12.6688 | -47.84899 | 2025-08-26 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| c18f00cc-054d-3b59-ad85-8f4afd96d0db | -12.72678 | -48.16465 | 2025-08-26 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 6d16706e-50ce-333f-b2ed-2b11289983b6 | -12.73009 | -48.13595 | 2025-08-26 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 80b66411-58b8-3344-8e43-dfdd12347a2c | -12.7549 | -48.17537 | 2025-08-26 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f3370a74-2b09-3310-aef2-e2eb2aa0277e | -9.63782 | -59.63846 | 2025-08-26 12:55:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| b7fa5487-4050-3c52-bdb6-8cf8eb52c08f | -10.77079 | -47.04585 | 2025-08-26 12:55:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 2fb53992-256d-3c72-adf4-945f4b42ff78 | -11.6126 | -46.40025 | 2025-08-26 12:55:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| b7670e28-ffb6-36c5-b6d7-3eb1ab64bf5a | -10.5362 | -46.79996 | 2025-08-26 12:55:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 08b35c51-b7a3-3538-977e-9a374800745e | -11.50901 | -52.13881 | 2025-08-26 12:55:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 9f6c1041-72de-3310-8ad4-f8ce44fea94d | -10.69995 | -55.14412 | 2025-08-26 12:55:00 | TERRA_M-T | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ff76585-ff29-3877-a4c8-6dd8f5348f1d | -10.808 | -47.08789 | 2025-08-26 12:55:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| ed15e0aa-c49e-34cb-908a-06e1a286c103 | -10.89664 | -47.34116 | 2025-08-26 12:55:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 512d0660-7d83-3358-9303-3ccf5e905266 | -9.25773 | -56.90439 | 2025-08-26 12:55:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b666f50a-8507-3d30-ac4d-bcf58a01e63e | -8.98703 | -65.41051 | 2025-08-26 12:55:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 16fd8a43-2a9b-3df7-8609-2c2e4a337969 | -13.36674 | -54.5652 | 2025-08-26 12:55:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| e4e1845f-c024-321c-b9cb-e776901d03c8 | -11.6091 | -46.39291 | 2025-08-26 12:55:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 3e212b36-0401-36c7-bc5a-a9321814e318 | -11.5747 | -47.62538 | 2025-08-26 12:55:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 396da627-53f8-38c2-a590-21fc829816fd | -10.71517 | -47.10635 | 2025-08-26 12:55:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| f1d2ec41-b7b3-3489-8581-a41685a3c3a8 | -10.76366 | -47.04967 | 2025-08-26 12:55:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 85e09dac-bb34-3a9e-b891-1701a697d6b0 | -11.56665 | -52.11808 | 2025-08-26 12:55:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9a01caed-93bd-3429-9ac1-821c4c7c31d8 | -10.6158 | -54.88849 | 2025-08-26 12:55:00 | TERRA_M-T | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4fe570f7-a58f-3052-a736-dd27ca8184bc | -10.24862 | -59.67224 | 2025-08-26 12:55:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1ec1d440-e4dc-37a5-9210-0d4302e19a1e | -10.81681 | -47.09539 | 2025-08-26 12:55:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| e7eee4fb-a446-39cf-bdab-785cb836e083 | -11.20045 | -50.57016 | 2025-08-26 12:55:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 43172103-8924-3f30-84db-5c46579b1602 | -11.63885 | -46.43487 | 2025-08-26 12:55:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 8e451c82-d192-378e-ade4-c5126ce8080c | -11.30336 | -55.11055 | 2025-08-26 12:55:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 49fce7f6-6d62-3b38-8052-ef69a112b5d1 | -11.51702 | -52.13338 | 2025-08-26 12:55:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 638c291b-bd2a-376a-9556-7059cd3f9e48 | -9.20528 | -60.91824 | 2025-08-26 12:55:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 12169281-8446-3eb9-9b06-b7172281b9ae | -9.26743 | -59.78255 | 2025-08-26 12:55:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 122403e6-4df2-3e33-a1bf-0a946c5a91a1 | -9.15749 | -60.78125 | 2025-08-26 12:55:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 087ebc27-ad62-346b-8c82-331766ce0a09 | -9.2379 | -60.92937 | 2025-08-26 12:55:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cb34f2c3-224f-348f-9da9-5315431a921f | -10.89359 | -55.7946 | 2025-08-26 12:55:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5726de64-518e-3e2e-9712-f9e29687f21e | -11.57872 | -47.62092 | 2025-08-26 12:55:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| d8d4d762-14eb-3603-aa0f-175f34db01ef | -13.06024 | -46.3199 | 2025-08-26 12:55:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| f60184de-8b55-342a-8b3d-2530cde1ab15 | -12.66549 | -47.87994 | 2025-08-26 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 2989ff92-4db1-3b07-8214-263ad104686f | -13.48758 | -46.87416 | 2025-08-26 12:55:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 6ea7eb3a-0da6-3884-985e-aba33b73d9e4 | -11.08855 | -49.99101 | 2025-08-26 12:55:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 7b913ead-dd9d-3922-adaa-67b85106c25f | -11.62955 | -46.40277 | 2025-08-26 12:55:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| a0fed199-7f6e-3f18-bbd7-9ac7046a9850 | -12.72781 | -48.14259 | 2025-08-26 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 7005e772-9e74-3f7b-a504-b1528a2c9ed4 | -10.54013 | -46.76476 | 2025-08-26 12:55:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 72f0ee59-75ba-3af8-8800-64b21e7d4fb4 | -9.24406 | -60.81681 | 2025-08-26 12:55:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 967cedff-b766-32de-af59-fb5de80e67c2 | -9.24352 | -60.82285 | 2025-08-26 12:55:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 43143581-dbf0-3507-a128-1ddbbf556f87 | -12.66919 | -47.87503 | 2025-08-26 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 973d8de3-1555-3afb-b7f1-b7d7bb3dfee2 | -11.5062 | -52.13204 | 2025-08-26 12:55:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c264d87b-a8cc-3a97-bc70-ce08a9dcdc43 | -11.07578 | -49.98945 | 2025-08-26 12:55:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 1bc341f0-6c0c-3160-8cb9-ad0647bbcf64 | -9.19035 | -60.79315 | 2025-08-26 12:55:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 71e54d9f-ce4b-3518-b5bc-96bbb67586cf | -11.54268 | -50.45196 | 2025-08-26 12:55:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 6244744e-36f9-3b67-b92e-9512a8e8fb98 | -8.85972 | -62.44174 | 2025-08-26 12:55:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7dbe74c6-532c-3d1d-8f15-765104764199 | -9.58933 | -55.36995 | 2025-08-26 12:55:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2e03c785-6ca2-3a4e-aed6-5f758ad58f07 | -11.08615 | -50.01076 | 2025-08-26 12:55:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c58dc6db-d3e5-31df-9f53-40818ad3b26d | -11.51074 | -52.12489 | 2025-08-26 12:55:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| e13d3cf9-ff4b-37ea-a06b-abbed3a6d5a7 | -9.27558 | -56.90696 | 2025-08-26 12:55:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a999a33d-db7c-3886-9ad9-f7fd7a421083 | -11.64299 | -46.39788 | 2025-08-26 12:55:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 2026b06e-3af2-3551-972f-ced1e7285c3c | -14.31441 | -60.36621 | 2025-08-26 12:57:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 92f51fa2-cf02-3f26-b60f-453032713f66 | -14.76306 | -59.71484 | 2025-08-26 12:57:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 28e1cb06-292d-3ec1-a47f-c51a5e54e863 | -15.11052 | -48.74503 | 2025-08-26 12:57:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 0fc476f9-266e-3e8c-8f72-a2fef7834bf6 | -14.76145 | -59.72532 | 2025-08-26 12:57:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 41dab157-2337-30d1-bb5a-60c26354c52a | -14.85192 | -47.14532 | 2025-08-26 12:57:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 127.2 |
| d30d017c-4928-32f6-bf2c-9be1cc85fad5 | -14.32578 | -53.23874 | 2025-08-26 12:57:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 36da087e-54f4-37de-a62e-a68204913415 | -14.43298 | -56.44873 | 2025-08-26 12:57:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 199175b6-b698-3fb9-9a02-64fb328e7e27 | -15.64625 | -52.72652 | 2025-08-26 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3f652834-49db-3898-bdd2-9c9d76d4488f | -15.01951 | -48.17057 | 2025-08-26 12:57:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| a6298d28-b10d-310e-8e91-a1178ce609f4 | -15.1113 | -48.73976 | 2025-08-26 12:57:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| b637d6e2-e6fc-3520-8f5f-a8bd05593298 | -15.32047 | -53.84122 | 2025-08-26 12:57:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 55212743-ed9f-3bda-b6e6-f36bc65fd651 | -16.72165 | -49.3701 | 2025-08-26 12:57:00 | TERRA_M-T | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5b6fcfb6-1f3e-3934-b4f7-252f72e7d111 | -15.64441 | -51.49002 | 2025-08-26 12:57:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e59ee1bf-0261-3df5-8979-16ce03295325 | -14.84757 | -47.13776 | 2025-08-26 12:57:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e8ae564e-f2b7-3d19-85c9-a449338622bf | -20.19963 | -56.25937 | 2025-08-26 12:57:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1acbaa6-3f4b-334a-b91c-3d330d8c518d | -16.72452 | -49.34241 | 2025-08-26 12:57:00 | TERRA_M-T | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| e6ae7e5c-0d58-3ae0-9252-a55f795a431d | -15.64732 | -52.73321 | 2025-08-26 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 52cd6171-051c-3adf-b08f-f2745e6802ed | -15.09744 | -60.21675 | 2025-08-26 12:57:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dbd6e49f-da3f-3070-96ae-13eb5e5cabce | -14.29482 | -60.35801 | 2025-08-26 12:57:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8b669627-e62a-3bab-ae75-1d97a7837660 | -9.1717 | -59.5405 | 2025-08-26 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| d9107853-df8c-3a9b-a2d8-b4d634b11e21 | -12.6737 | -47.8812 | 2025-08-26 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3a97b887-c4c2-3cd4-bb76-7310e432eea4 | -16.6224 | -49.3708 | 2025-08-26 13:00:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| db2302d2-f177-3747-9665-5969278a5133 | -6.7635 | -59.6718 | 2025-08-26 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f7622fd8-2453-3b83-a810-8ef8f257e5af | -10.7787 | -47.0624 | 2025-08-26 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |


[Clique aqui para ver as próximas entradas](README104.md)

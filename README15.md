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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc4285d7-4d89-3a1f-83c4-d69389bf4ec7 | -6.3169 | -54.7775 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f144bfc8-218c-38fc-b7bf-a020adcc2c9c | -7.3989 | -55.211601 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5df8942-539d-3f5f-87a1-ee694d5d1353 | -7.7276 | -54.762199 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee03b4f5-437c-3839-9d62-7843a8cde15b | -8.066 | -54.8405 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a91cc39e-55a9-3fa2-8634-02da82798ccb | -11.1405 | -44.591499 | 2026-10-02 01:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8391f05-8817-3193-8f22-22a22c2335cd | -5.7685 | -45.1637 | 2026-10-02 01:12:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc0b0afe-5a05-3c1d-a023-367357f0e661 | -3.1723 | -54.081501 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b00be27d-8e49-3338-8968-124780040e9d | -8.4161 | -54.7043 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc8ed78-0b94-332f-b9c1-c6963f875127 | -10.7871 | -53.761799 | 2026-10-02 01:12:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db54bf4c-afc7-3868-8b5a-f7b8452f76b9 | -7.1968 | -52.607201 | 2026-10-02 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d127ea35-f1c7-3328-94b0-c5296ecedd1d | -11.4728 | -43.4431 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d85332b-b4f6-3bd5-a15f-64cc9ec50bd6 | -6.4084 | -56.4147 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba6f4d1b-8adc-3fa6-a941-896b366e6a91 | -6.1611 | -57.719601 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32abc817-0570-3b3d-9f16-bf48aebf4458 | 1.8062 | -55.579601 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eff2af7-b839-3db3-be4b-0c66ea3c02b8 | -7.7202 | -54.819 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac65710-a63e-3dfc-a465-4695a99cebb1 | -5.2726 | -56.054199 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6803294-2d10-3e37-a146-4f77b4da0e0f | -8.3049 | -54.7145 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc40775b-7137-3ae2-a873-c6634971f4b0 | -3.29 | -53.8358 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94bc87df-ea06-331f-8995-3f548dfa36d1 | -7.4622 | -54.996101 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0962ea80-640b-315f-a01f-7fb8cf527e6b | -9.8275 | -44.832199 | 2026-10-02 01:12:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b435fc21-9c95-317c-96dd-1b4ac7581a9b | -6.3529 | -55.3293 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2888624-61e1-3fc2-8294-ddc2467fffc9 | -4.2989 | -49.104401 | 2026-10-02 01:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4180d4f3-dc8f-3726-b2f8-98ce610b5301 | -11.1576 | -44.616901 | 2026-10-02 01:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9dcd6352-2cc0-3c5d-b9a2-6b8c9f57fca7 | -9.7802 | -53.828602 | 2026-10-02 01:12:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01a9d21c-2c11-363a-a352-20c7844d32a0 | -3.1183 | -50.290699 | 2026-10-02 01:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bca0afb6-5f26-3824-93fe-3e1f770cd088 | 0.6258 | -54.3993 | 2026-10-02 01:12:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb7bc34f-9915-391a-a20e-e11c78d4ab59 | -7.0431 | -55.634701 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e02c105f-c49f-3786-9cba-b806b84f4e78 | -11.77 | -43.57 | 2026-10-02 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32a06232-455e-3216-bf23-8d83ad58a712 | -13.32 | -43.89 | 2026-10-02 01:15:00 | MSG-03 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9340359f-faf9-3a17-aeab-b2ba8f2fa4a1 | -13.35 | -43.9 | 2026-10-02 01:15:00 | MSG-03 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90ed40db-974e-3951-aaca-24e43a34b0a5 | -13.35 | -43.85 | 2026-10-02 01:15:00 | MSG-03 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54c6a788-0bd0-34ed-87c9-3a0424c7f1cd | -13.32 | -43.84 | 2026-10-02 01:15:00 | MSG-03 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b73a9be7-a72d-3f0e-94dd-3efb918da4f7 | -4.2676 | -50.7506 | 2026-10-02 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 850ed003-fb16-36fb-beac-46f6f621ddbb | -4.2677 | -50.7297 | 2026-10-02 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| bf1b3850-e517-3ce0-ac34-f588f79f59a5 | -11.4691 | -43.4299 | 2026-10-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 51fd86f3-0727-36ac-b916-ec8a8e816f34 | -6.914 | -43.6816 | 2026-10-02 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| bd86d8d8-707c-3f71-8c39-9d7f4575ca03 | -13.0759 | -51.3095 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 91b05939-169e-3844-ac78-2dcf73f0a961 | -13.3476 | -43.8776 | 2026-10-02 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| b1122272-446a-3a4b-83e6-d2429d5720a3 | -3.1299 | -53.7431 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 18b66d91-c173-3df3-8c40-249d21a88038 | -13.3676 | -43.8504 | 2026-10-02 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| b6b62ed9-0141-3841-b594-938b815b2c6d | -11.793 | -43.5452 | 2026-10-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 86992b5a-abb5-3854-bf5a-117ae9555c8e | -10.8005 | -53.7682 | 2026-10-02 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 172.4 |
| dc17b863-bc38-35d7-91f2-13b2c6568fdd | -7.4031 | -55.2114 | 2026-10-02 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d32e984a-5abd-39eb-85aa-3cc44c8e8e32 | -12.8257 | -51.404 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b65bb69d-b83e-3863-8684-9b9c5edf37bb | -11.7375 | -43.4356 | 2026-10-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| be3a7ead-0f4b-32b4-a5e8-694b211d9815 | -2.0394 | -56.8593 | 2026-10-02 01:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 8a90d0bd-a7e5-3a2b-ae0b-de5c05e8a0b3 | -6.8952 | -43.6833 | 2026-10-02 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 699d958b-75a8-381d-9248-f9506e618d14 | -8.2217 | -55.082 | 2026-10-02 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 3ecc7ad4-9b80-3d89-a08f-823be7b5f329 | -3.1483 | -53.7426 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1b5bf832-ada2-3a2e-8ecb-d23fa0ccac5a | -14.8903 | -47.1315 | 2026-10-02 01:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 297eb2c7-6b04-3805-8117-dbc626ebb808 | -3.1655 | -54.0844 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 267555f0-5b4b-3b4f-926c-75e5e07f48e5 | -4.2953 | -49.1021 | 2026-10-02 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 2f675db3-71e7-390c-b3b6-8a5f9de8425c | -3.2766 | -53.8602 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3eb01c36-c943-3419-bed1-40736e087725 | -13.0375 | -51.3143 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3d089969-dd26-3db2-8262-c56e88eb1e49 | -3.2767 | -53.84 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 795794c6-a86d-3d60-80a0-0604d645680a | -3.0192 | -53.887 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 77210984-37e7-3a6e-812c-391c8faec6cb | -6.3952 | -56.4158 | 2026-10-02 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| c14ee5df-3ce7-3a2f-b113-e14829cca5f0 | -11.1424 | -44.6029 | 2026-10-02 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 8cf0e008-d42a-3216-a7c6-267ca53c4100 | -2.0577 | -56.8591 | 2026-10-02 01:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 21f5b46c-375a-3a48-84c5-f246c458cd2c | -11.4764 | -47.4645 | 2026-10-02 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| f1eb9b96-332c-32d9-ac7c-e2c71a4c945f | -11.1615 | -44.6002 | 2026-10-02 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0f2229ba-6c5c-3484-85c9-cbcbb63706fb | -12.8062 | -51.4276 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 12afa7c8-5809-31da-8726-9fe595866dd9 | -11.7733 | -43.5719 | 2026-10-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 351.3 |
| 4a68f411-74a8-334a-a130-a7fcaca7fcd4 | -3.0008 | -53.8874 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 452e5f13-21b1-35c5-af02-ae3d816e4b33 | -12.8254 | -51.4253 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 145.1 |
| a8c8a023-6526-32f0-97e9-513323914786 | -2.0393 | -56.8789 | 2026-10-02 01:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 934ced39-d329-3c59-820b-52333f9f96e0 | -12.825 | -51.4466 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 6319c2cd-d497-30fa-ab8b-e3a4995f9759 | 1.7853 | -55.6251 | 2026-10-02 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 92189986-f4d9-33e6-9f74-76a7f9e74a74 | -11.7729 | -43.5956 | 2026-10-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8fff2a13-3386-38ab-aaae-57de87b9c37f | -11.7541 | -43.5749 | 2026-10-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 58bd217e-b19a-320f-b19d-881dbb7a7895 | -7.8682 | -44.169 | 2026-10-02 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 323ecb88-d7dd-3fad-8768-9cd5393b14c6 | -11.4768 | -47.4422 | 2026-10-02 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 446cd552-d4b4-31ca-8a81-735e7a5908b5 | -13.0378 | -51.2929 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 3e1210f4-c62a-302c-82bc-6ec4ea1f03c4 | -13.0762 | -51.2882 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 35256f93-39dd-317b-9686-c24f75473ea9 | -13.3287 | -43.8573 | 2026-10-02 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 3c350dcd-9b82-3eaf-9bde-2ae88a996337 | -13.057 | -51.2905 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.0 |
| aba0dcfb-a29c-38a5-815c-b0bf6defbb66 | -3.1839 | -54.0839 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 44199023-11a5-36c4-8a0d-ba473908dbb1 | -8.2215 | -55.1021 | 2026-10-02 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0ed6b655-6143-3056-9b0b-81f3bbeea5e2 | -2.0576 | -56.8786 | 2026-10-02 01:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| afb7e0f5-218e-3799-b334-d29b90753959 | -11.4695 | -43.4062 | 2026-10-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b6652264-1907-3439-80c6-ea578f40bb6a | -14.8908 | -47.1087 | 2026-10-02 01:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9afb99ca-d9f6-3278-b228-706655f72f9b | -7.0478 | -55.6302 | 2026-10-02 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 06db56b5-025b-3cac-a024-b7bea829646b | -10.7816 | -53.7699 | 2026-10-02 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.0 |
| c57bae35-5805-3bb4-ac2a-914ad7ebfdee | -12.8066 | -51.4063 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| bc31f48c-0b97-3f27-bd7e-a2cc54858662 | -13.3481 | -43.8538 | 2026-10-02 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 368.8 |
| 94ca90cd-5edf-3eff-b817-34c710c598b2 | -7.7219 | -54.8114 | 2026-10-02 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| ddd107c2-c663-3dcd-86a6-595403dd6d39 | -13.0567 | -51.3119 | 2026-10-02 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 25ffac19-a313-3c56-88ad-b347e732cdae | -3.1299 | -53.7633 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ab976464-86b0-3619-82bc-33db6228faf3 | -3.2951 | -53.8395 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| bc455a79-a734-3d05-9eed-767f113ecc2d | -10.8007 | -53.7476 | 2026-10-02 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| e3685041-c60e-3ba5-bedc-c299554d7ca5 | -9.844 | -44.8449 | 2026-10-02 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 136dc3d3-ee22-3974-a3bf-4d4eb570bffa | -3.1483 | -53.7628 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| a27afd79-7c6a-3294-87f3-98336253d71a | -4.2954 | -49.0807 | 2026-10-02 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 36d8a022-97e7-37b6-979d-a15b01074213 | -11.7738 | -43.5482 | 2026-10-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 534c4f97-bee6-3da2-983e-90b606806c3d | -3.295 | -53.8597 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ec0baffe-0ed5-394d-8ede-b444074c7570 | 1.7853 | -55.6449 | 2026-10-02 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ee743998-4dc0-3460-ac4a-613b67d53f24 | -11.7926 | -43.5689 | 2026-10-02 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 73863077-d45f-3947-b3ba-f109f912a2dc | -14.9098 | -47.1282 | 2026-10-02 01:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 85a07598-f53c-313f-a0c0-ef22960c420d | -3.0189 | -53.9675 | 2026-10-02 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 43c2709f-2d2b-384b-bab6-a5dc6d420f46 | -6.0072 | -53.5528 | 2026-10-02 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |


[Clique aqui para ver as próximas entradas](README16.md)

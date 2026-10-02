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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 433257bd-fad0-381a-8f44-24d96ad1c299 | -4.0171 | -48.958099 | 2026-10-02 01:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d97794-aa29-3c2e-bda9-0c8e89b90cc7 | -8.0763 | -54.8848 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 788f44b9-97da-36a6-b388-e6efd5c7749c | -3.0259 | -53.896301 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 471283b3-1337-32f1-a662-1701492412ea | -7.2702 | -55.590099 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f03c0b6-d299-3820-a8b7-b1d43c267221 | -3.0042 | -53.891701 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 779f1874-fbd7-36e9-9126-cbbc1c66c3d2 | -7.3418 | -55.232399 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f7a9249-16be-3440-8734-d1e4e2d5d222 | -6.2438 | -57.766102 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dffe1032-81cf-37f3-bee8-74e4c391f1d3 | -7.472 | -54.993801 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff91987-0fc3-313c-afbb-1fca8efeddeb | -7.5722 | -55.025002 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f86c66d1-6284-3676-9dc8-6706e59d9077 | -9.5263 | -45.358898 | 2026-10-02 01:12:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33479f4b-90a1-34bd-a268-8c28d3e10348 | -6.753 | -55.0975 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1911f7d-7ef0-32cc-a5ca-5773cc9d59c8 | -7.0415 | -55.627602 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3aca775-aa8a-3ac4-94e7-e1ac6d453b58 | -13.3448 | -43.837898 | 2026-10-02 01:12:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61799eb7-5347-3895-b77c-a9d2c4492873 | -13.3418 | -43.9011 | 2026-10-02 01:12:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa90494a-8d7f-37e6-95b3-5e935ea58a5b | -11.7743 | -43.602798 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d49926c-0136-3618-8e99-e1db398784fe | -3.5421 | -55.533401 | 2026-10-02 01:12:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 815533b5-49fc-320e-a37c-76a888178666 | -2.0454 | -56.865501 | 2026-10-02 01:12:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 751d70a7-8262-3f0a-bf0f-68f53a8c12a3 | -2.3946 | -56.993099 | 2026-10-02 01:12:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e3ca500-3443-31da-b14f-690b73ac94f1 | -6.0045 | -53.538502 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbd1ad9a-2561-3e68-94db-a47535f4d4e1 | -6.4705 | -55.524399 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3205667-0a03-3884-b29c-15ae2f804c91 | -12.9851 | -51.1595 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1d17f52-f0e9-35d6-a13f-0b5bb8390b86 | -11.1481 | -44.619598 | 2026-10-02 01:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b549c6c0-29da-34a9-ba7f-bc06d20e5231 | -8.2387 | -54.784698 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d58bfc7c-2a90-37ed-88c9-318e875291df | -7.5668 | -55.134399 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acb21c4c-71a5-3e9c-8579-70d5d91d8f82 | -7.0448 | -55.6418 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0353314e-91b3-3984-804c-12a4cbba3c4c | -7.1991 | -52.616798 | 2026-10-02 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e179e27-8915-3811-aaad-b751f5c7d47c | -11.4852 | -47.4762 | 2026-10-02 01:12:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa4858f2-0004-3be8-8164-e0974ad36e0c | -3.8497 | -55.9697 | 2026-10-02 01:12:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b41a1077-7dc5-3d0f-abef-e2274840fc6c | -9.5192 | -45.3321 | 2026-10-02 01:12:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5dbbf807-98c3-3c50-a602-d02f8b5376f1 | 1.7867 | -55.619701 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c216af02-83be-30ab-aaef-fdf72b6434a3 | -3.0145 | -53.233601 | 2026-10-02 01:12:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99436ba4-4807-3e1c-bb43-1dac03a80154 | -6.0391 | -57.6819 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 556f8dfe-fcd0-3238-8637-71ca2a876337 | -8.2208 | -55.105801 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5e6544e-9e3d-38e5-9e74-aa02ffd34945 | -7.4042 | -55.589298 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 157c60f7-8161-3d88-921f-61cf31a7e692 | -6.3465 | -55.346199 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a91f53e-e341-3226-94b0-d70935919dea | -4.0692 | -51.128399 | 2026-10-02 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 853fcdd3-cb8d-3ea6-9f8e-f6f1ad7c476f | -5.8662 | -53.4772 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88bda4bd-a6dd-3d15-8691-190aecc126e5 | -7.0627 | -55.630199 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e483aff-100e-3ff0-9e14-ed18f2607ed5 | -7.8448 | -55.131599 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50e2d1f2-ab81-31de-a607-e167867ee767 | 1.8004 | -55.605 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42f155a4-032d-391a-a763-b0ecb01ad324 | -7.846 | -56.610298 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce75bb57-b329-34c4-81dd-caeb2a7245fa | -7.8218 | -55.121498 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed4c4ab-14f6-3585-a540-78df725f82d7 | -8.07 | -55.345798 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06594f0c-6b36-3da6-97f9-e11f17096c66 | -7.4933 | -54.9967 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd3cedb-988e-3f38-8975-bb0e9a5061ac | -7.5651 | -55.127102 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d836e599-81b9-32ac-9b8e-cf0f766b12c7 | -11.794 | -43.5625 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71f4c6fc-be71-3959-9606-de177912b219 | -6.0755 | -57.616001 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4440b9e0-cf1e-3309-8ca8-481301e03ac5 | 1.781 | -55.6451 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee4d812d-ffcc-33e9-a2b2-922c920006ae | -13.3529 | -43.866699 | 2026-10-02 01:12:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1071aff1-9b22-3fcb-b538-9a9404ff673f | -8.0861 | -54.882599 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2b9a510-f901-3c08-a842-ed9e96ccfa13 | -7.28 | -55.587898 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06b9c3ef-9130-32d0-a7c3-e8ac5606f46a | -7.4025 | -55.582199 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a58e2fa7-cebc-3af6-989f-2e2ab0e9db4a | -8.2 | -54.707401 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e735fee-7caf-3f9c-aefe-eeac257af3f5 | -7.7258 | -54.7547 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81c41147-92c9-324e-85fe-02ba53804b94 | -8.1685 | -54.793201 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8668d4ae-694d-32e4-ac62-b3614f758726 | -6.4903 | -58.533401 | 2026-10-02 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc4c0931-6bf0-385c-b543-1d65b9f33229 | -3.0734 | -49.3778 | 2026-10-02 01:12:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ef1ded9-42e0-36a1-bc26-d46ca41f79b7 | -7.4588 | -54.9813 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce6e815-fdf3-304a-858e-bb0b08943e16 | -6.0066 | -53.547298 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf2b3daf-a66a-398c-867a-6d7e8baff135 | -6.074 | -57.6091 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f010ccf-d7d1-3a94-a1a8-7dab255e7485 | -7.2522 | -55.6017 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 901ef709-0def-3e97-9d3d-240f9660feb9 | -7.5445 | -55.039101 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e21eff50-57ab-32a5-877a-235b38f56a32 | -4.2701 | -50.765701 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 286d826f-98e0-32c2-9e56-6baab0f65090 | -7.8476 | -56.617199 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c02c1692-f5c0-3cb8-b245-5c614373b78f | -4.293 | -50.775002 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8590abf7-82af-394f-9c02-182f61badaec | -6.8529 | -59.274899 | 2026-10-02 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd1bc90-8ad8-3d9b-9622-e80eb3d9efb5 | -7.5573 | -55.005199 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16fe531c-6788-3000-8080-480f57257d94 | -3.1884 | -54.105999 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f50ddb6-2054-3a86-84b1-18bb5c3a45a7 | -4.3027 | -50.772701 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 244c822d-ff35-3f3a-b155-74ee594bddc9 | -10.7969 | -53.759499 | 2026-10-02 01:12:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6f5c9f2-79ce-3933-8bd3-5d3af6fa9abd | -4.2892 | -49.106701 | 2026-10-02 01:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13508f8f-5b8c-39a5-b879-d1623472f7dc | -10.8185 | -51.098202 | 2026-10-02 01:12:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2115da33-710f-36be-85cb-f38781922e0f | -6.41 | -56.4217 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e09d9951-be73-3992-904f-a33b96b5c03f | -6.2638 | -55.434399 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c93b6e69-a416-31cc-8e0a-dbcbd8dc4d9b | -7.3385 | -55.2178 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81ee1933-ca69-3236-a21d-dc6411184755 | -5.1206 | -56.0214 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5b311e4-78b2-3ce6-9178-aa63a9168eb5 | -7.0611 | -55.6231 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b51f59c4-6ef3-3db5-a951-6538f2cad9d9 | -7.7569 | -49.200802 | 2026-10-02 01:12:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| eb66f660-ad41-3eab-9de7-6a5388ac38ac | -9.782 | -53.836399 | 2026-10-02 01:12:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa0d70f6-bee8-3480-bab2-f774d45efaf3 | -11.1385 | -44.622299 | 2026-10-02 01:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7d15c7a-3095-3dd6-910a-b0493f16efbe | -11.471 | -47.460999 | 2026-10-02 01:12:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abe85d38-acdd-3867-b784-7a0104486024 | -7.559 | -55.0126 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8666b2f4-368c-3aba-ad8e-1cf2b2be1c91 | -8.1028 | -55.353298 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e75c8202-def2-3ba4-a905-1dba1936ef51 | -7.7248 | -54.7943 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1d4ff89-0342-3e67-a78b-96b5ffa5f059 | -6.4068 | -56.407799 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c48f53d5-bfeb-3a7c-a502-c82765756e7c | -7.4852 | -55.006302 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cb0d5f1-0562-380c-9364-02e830d162b5 | -12.8106 | -51.419201 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b54e35e-c850-37cd-95d7-3e50195bf349 | -7.8333 | -55.126598 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad022039-766d-3fe1-a615-0d7677b626f8 | -7.6331 | -55.065102 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b67ebcc-cdef-3b7d-b25d-3282ccc0c827 | -4.3033 | -49.122398 | 2026-10-02 01:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35dca8ef-477e-3d65-ac36-48f946722a94 | -6.4052 | -56.400902 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac1e719-b996-34c6-a66f-739d54db17c1 | -6.4416 | -55.622002 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa0af63-4bbf-375c-aa23-d516b8054951 | -7.0546 | -55.639599 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62c9fd79-def1-34d0-9100-fd4235b64247 | -5.9968 | -53.549599 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4005b11d-340b-3248-8970-0061e283307b | -3.1904 | -54.114799 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2170edca-17b4-3450-841b-c0c406a22161 | -8.2076 | -55.093601 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17a06e5a-d0f6-3b93-b7f4-de1985de7c30 | -11.7654 | -43.570702 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6438fe37-935d-39e2-ba49-44ee159a4b34 | -7.6314 | -55.057701 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41d78d34-8be1-35d4-911f-ce2dc709bb08 | -4.6862 | -55.794899 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0573d649-e9dd-34c5-8116-aa0216f99da7 | -12.8268 | -51.4856 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)

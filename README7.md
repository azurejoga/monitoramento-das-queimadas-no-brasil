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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3622118-47b0-3859-a329-d5b00e5dd37e | -3.295 | -53.8597 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| e03b6298-60ff-33a9-bb29-515313aa0a60 | -11.7541 | -43.5749 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| c6493a31-1e62-303f-9937-773dd347f1dc | -13.3481 | -43.8538 | 2026-10-02 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 53745c99-5df6-3726-adda-06d85391e91e | -9.5149 | -45.3199 | 2026-10-02 00:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| fa57ed02-0ca4-3d96-9ecf-074828d99ef2 | -9.5146 | -45.3427 | 2026-10-02 00:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 11d9c462-f23d-34b5-b4c4-489fcbe6f39a | -2.0576 | -56.8786 | 2026-10-02 00:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 14048b1a-e865-3081-847f-2ddf614a9659 | -11.1232 | -44.6056 | 2026-10-02 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 46494887-9abf-35b9-b5d8-3c815b78de68 | 1.8221 | -55.5654 | 2026-10-02 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 96e9412c-9182-3806-89b2-22d8741c81fe | -6.3952 | -56.4158 | 2026-10-02 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 30f4534d-c762-35ba-aa23-b40b20a90cd4 | -11.6964 | -43.584 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 97d8b118-b737-3099-b60c-e4d06b3f1fa2 | -7.7551 | -54.816299 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 214f5a8b-d1be-3be6-b2fb-314d78fc88fb | -3.8471 | -55.812199 | 2026-10-02 00:50:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd9c333-3eb8-32e4-89ab-683b1618ecc8 | -6.7501 | -55.100399 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb0170c1-8e78-335d-a366-5493593e8158 | -7.0323 | -55.640301 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae5a913-2bae-3701-8a7b-fc55d2f5022e | -6.0006 | -53.554901 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 196dc362-7792-37a1-8abd-d2664ed615ed | -3.0076 | -53.892601 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bee4e85f-800b-3ec3-99ec-d825be311ad4 | -6.7476 | -55.089901 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e76e22f-26c9-3c68-9bdc-2e873786048e | -7.8486 | -56.613701 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1571b044-4d51-39b4-9770-3fcb2963b8ac | -7.1908 | -52.645699 | 2026-10-02 00:50:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7256d2ba-e8af-372c-aee3-108b8260a686 | -8.2145 | -55.098999 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4203850e-8b3f-3d2a-b8b2-f1bd19ac2095 | -3.2836 | -53.843601 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 255e8aed-e157-3ca7-aff2-8c1ee21cfa03 | -4.3035 | -49.1502 | 2026-10-02 00:50:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be03dda0-33e4-3af2-84c8-4e7af862e2a8 | -7.4606 | -55.0089 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1480698-e60b-3469-8b24-65dc29d445d7 | -6.8629 | -59.280399 | 2026-10-02 00:50:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b10bcf1-dbd6-3925-99b6-88b4b1c6f7c9 | -3.2771 | -53.8601 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a289f0b-7950-38a7-b711-f938ad5c1cad | -7.8388 | -56.616001 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2af326a-92a4-38ea-9b88-28ac5693ad3e | -8.2168 | -55.109001 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 947ee5a3-94cf-3139-9565-011b908352ae | -7.0346 | -55.650002 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53c1e221-f699-3791-8136-884abcbe9b0c | 1.8213 | -55.591 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 513ef40a-2bfe-3f52-abce-95a33ac8772f | 1.8027 | -55.6278 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9764549a-7922-370d-8da3-985ee86afc7a | -1.268 | -54.5742 | 2026-10-02 00:50:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6bfe123-6d57-3843-8c83-e19ec6e8ee1b | -7.8412 | -55.134998 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4cd11b7-ed65-338a-adef-e4b0828f18ca | -3.1774 | -54.091099 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7ac3c98-c134-3834-a79c-ab5041751e89 | -7.1872 | -52.630699 | 2026-10-02 00:50:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 577b8bc5-12fd-3bf5-8684-82ba2a4d157c | -6.8515 | -59.2757 | 2026-10-02 00:50:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 326bd501-d135-33bf-8c93-39dd64014a63 | -3.3 | -53.8699 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acc63957-9a71-3cdf-93a3-ac7d9a10b049 | -3.1395 | -53.754902 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb46667c-4062-323c-b068-4c70fa76a128 | -7.3345 | -55.609699 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eec21a26-6faa-360b-a18a-895332ef0a0d | -3.1429 | -53.769501 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2fc308-42e7-3e38-b0f0-d3bdf4c0bd89 | -4.2939 | -49.152599 | 2026-10-02 00:50:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4675c3b7-6ec3-3a78-b29e-e06d260731a9 | -7.4581 | -54.998501 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf0469e2-cd20-3f2f-ac0c-04a83fc99866 | 1.8184 | -55.604 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e7b3b5a-bcc5-3847-96c6-7300c3b999b5 | -7.342 | -55.597698 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55be9027-a20a-34e4-8378-520aa05c5961 | -7.7161 | -54.8256 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 217afd8b-8dab-3297-88fe-128eb191ca40 | -6.3915 | -56.426201 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e835549-7410-370e-9976-5a30efd1c91e | 1.7745 | -55.662399 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6067eb0d-66b1-3235-88d0-c41bf03501da | -6.8547 | -59.2896 | 2026-10-02 00:50:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00a1605c-0e7c-3049-88c0-03d541ea7eee | -6.0039 | -53.568501 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63debc2a-7100-3d54-9992-bada67bc7568 | -3.0277 | -53.978298 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16402a95-e9e5-3689-99ae-b552c24f7e94 | -6.6993 | -56.154701 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73a06b98-5d98-3466-8234-dae3fc40eb81 | -3.011 | -53.907001 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b9d915d-b5a7-3b0b-8aa7-f3fc1c16098a | -7.8388 | -55.124802 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68603498-360a-31af-b29f-a2f20e1790c1 | -6.4111 | -56.4217 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 871049ce-31e3-3f1d-afd2-2325a998bd96 | -2.0536 | -56.870998 | 2026-10-02 00:50:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4f56e9-ac99-3398-b80d-b82ddbd69ea8 | -6.8726 | -55.575199 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a22ebf5f-3fdc-3b4f-b77c-57911e862582 | -6.4013 | -56.424 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f3878bb-80ad-35e0-a412-16d779190035 | -3.2869 | -53.857899 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 201d5805-7828-37ad-b6cf-315fbfd1f954 | -6.4069 | -56.403801 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bdae0f4-8467-373d-ac39-44bffff7adde | -6.3594 | -55.1483 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49d09ff7-ac7a-3fe9-a855-38c8785318c3 | -7.3397 | -55.5881 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14473da4-48a4-326c-ad04-675904fd2411 | 1.7774 | -55.649502 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5356154-12a4-3f68-8730-61f5341c6017 | -7.7284 | -54.8339 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aeec004-4d22-300a-9d12-ad969835c5ad | -7.4899 | -55.0019 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65585be3-59e3-3b89-ad94-86701389ec9f | -6.2644 | -55.4445 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80b99d1f-27da-36b4-b571-cfeaf1906659 | -6.4711 | -55.5341 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 214f1937-16bf-383f-a6ae-07f4516af1f7 | -7.8362 | -55.157501 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9dc55b7-393f-3ee2-b59d-70a218fff674 | -3.2805 | -53.874401 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37323413-0d4e-37cf-9680-c1aa45082ddc | 1.7871 | -55.6516 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8774fa-e8bc-3cdc-b6c8-1c523d5d0f3c | -6.8484 | -55.5602 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c14bb901-4f3b-36b0-8c96-cd2e87300980 | -3.0213 | -53.994701 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cde2964-b938-309e-b104-5c20f88fdcde | -7.8436 | -55.1451 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c4520a1-dece-3b32-ad56-2248951f3805 | -3.5698 | -54.625401 | 2026-10-02 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d05809a0-5c30-3e3e-8edb-9fb62aa7d283 | -6.3894 | -56.417198 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7caa63f-21e4-3eb8-b12d-25ffeeb143ff | -2.0461 | -56.882801 | 2026-10-02 00:50:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33c27315-0e1f-357b-9f8b-550f06727964 | -2.3924 | -57.001301 | 2026-10-02 00:50:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b36a3bc6-d9f2-34b2-bebd-e5169b985b5f | -7.463 | -55.019299 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 380bd4d5-83c3-3039-a6d6-f8f798be6279 | -3.1644 | -54.079601 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff1b5d9-a7a1-30c0-bb0d-f694ba9246ce | -8.1681 | -54.817402 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c270fd33-70c3-3027-a00b-ab8eb7323e4c | -3.1579 | -54.095699 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49752804-d2f2-35fb-a3e1-82a9c2811730 | 1.8086 | -55.601799 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3431fb6c-72aa-3500-a2a8-ee6d0530aa37 | 1.79 | -55.638599 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcc42319-fb39-394b-baf4-f0bd6e92e66b | -7.7259 | -54.823299 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e16e14e0-ea4a-3db3-95a6-fa25c2be0a95 | -6.409 | -56.412701 | 2026-10-02 00:50:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5694bdb6-777b-3904-b484-86fc37983d39 | 1.8144 | -55.575699 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed454cf7-00e0-35c6-941d-4b4bcad75814 | -7.4703 | -55.0065 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f27f5f2-f0e4-3ae5-9b26-45dec90a104a | -7.8338 | -55.1474 | 2026-10-02 00:50:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b382d108-be5b-3b85-a6e0-71bee75db6fd | -7.4678 | -54.996101 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc9f4760-14c7-39c9-a6fe-c8114b21d11e | 1.8155 | -55.6171 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39674a92-271e-34b5-9636-083e3738d107 | 1.8057 | -55.614899 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 177a698b-f801-3b97-bc10-18b6142266ad | -5.9973 | -53.541302 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e21b34b9-3516-3037-b4c8-c64c2d06eb2a | -4.2867 | -49.123402 | 2026-10-02 00:50:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a11b3992-35ec-356b-844f-f8dbb249bc9c | -7.6267 | -55.056801 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f577a1b-6d4c-3db5-9d71-1c456c3bda04 | 1.8115 | -55.588799 | 2026-10-02 00:50:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0081eb8-f8e7-3041-ae39-12ab0e9875b3 | -2.8812 | -54.889801 | 2026-10-02 00:50:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e75521-216e-378d-a03c-079fa99a69b8 | -3.1806 | -54.1049 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c2f166c-9272-391b-a551-e77dba63361b | -6.7599 | -55.098099 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8b632d-700c-3a9d-a213-9f2d65245c67 | -3.031 | -53.992401 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc3a93d-2901-3c0d-bc4d-58729169ac03 | -6.85 | -59.2687 | 2026-10-02 00:50:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6355f62-13fe-32de-8f06-ec85e4e5893f | -7.7233 | -54.812698 | 2026-10-02 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf1bb483-e993-30ae-8d83-e212d8850df8 | -3.018 | -53.980598 | 2026-10-02 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)

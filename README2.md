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
| f6f63f45-f38e-3926-bf7d-d90065c7af0f | -8.9434 | -44.2373 | 2024-12-07 00:50:00 | GOES-16 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 3725cb9b-966f-36c1-8098-b959ad907961 | 2.5064 | -61.0012 | 2024-12-07 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| aef954b7-0b61-35e0-9b82-ff5a09a217a3 | 2.5247 | -60.982 | 2024-12-07 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 24d5ec11-33f4-3f08-8971-9921d63aacb1 | -15.2528 | -53.5723 | 2024-12-07 00:50:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d3940c22-d655-3948-89b9-1f9d2b1a1948 | 2.7267 | -60.3916 | 2024-12-07 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 22aa4c17-c374-3481-8bff-643da306c093 | -12.2944 | -45.4958 | 2024-12-07 00:50:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| eb9290f9-aeb3-3bd7-b212-9c7b40a5f1a9 | -12.2703 | -45.451599 | 2024-12-07 00:53:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8faeeb0c-7185-31ec-885d-95565ca3898c | -13.6653 | -52.933399 | 2024-12-07 00:53:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4d2518-9876-35c0-bda9-bc5ae0a0f359 | 2.4138 | -60.636002 | 2024-12-07 00:53:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 17eb3fb6-0d8d-388c-b831-b7ea3eb3f8f5 | -10.759 | -54.767899 | 2024-12-07 00:53:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9fa8ce-9607-3c53-bf41-1adf6b905caf | -12.2326 | -52.4431 | 2024-12-07 00:53:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f37676d-14a8-3576-abbd-a8e864c2915b | 2.946 | -60.3353 | 2024-12-07 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f78935f5-b068-3a00-91ae-d3aae9777023 | -12.8576 | -51.930801 | 2024-12-07 00:53:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a24620cc-de69-3f91-bd24-8c8962476a34 | 2.7404 | -60.378399 | 2024-12-07 00:53:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d5f62a94-3587-3411-93d6-1a2383526d36 | -12.2849 | -45.468102 | 2024-12-07 00:53:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ce79c83-1c12-3b77-9d82-da2ee221559f | 2.9443 | -60.342999 | 2024-12-07 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fff867dd-98e8-340e-b1ba-ab98698cf7ca | 2.5099 | -60.9827 | 2024-12-07 00:53:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5a5617d2-d4ac-3523-b1ee-df4801d14d9a | -15.2664 | -53.5462 | 2024-12-07 00:53:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cdda9b75-eb4a-354a-99aa-599812605227 | -15.2695 | -53.560299 | 2024-12-07 00:53:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| adc3778b-8f11-30dd-9422-bf6089a59abb | -12.2752 | -45.470699 | 2024-12-07 00:53:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79b55df6-7229-304f-9049-6bd22a8c4657 | -8.9136 | -44.217201 | 2024-12-07 00:53:00 | METOP-B | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b9954ff-c7d3-3c8e-bf49-31e09d158636 | -11.0492 | -45.356602 | 2024-12-07 00:53:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d8c42e1-6298-36dc-8c67-5aaec288970f | -9.218 | -50.6782 | 2024-12-07 00:53:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79478067-a79a-3986-8404-4d5e0640497a | -15.2566 | -53.548401 | 2024-12-07 00:53:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa12807c-119c-3835-9a7d-057c05d1e8b9 | 2.7323 | -60.368401 | 2024-12-07 00:53:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3331d9f6-bb1e-33bc-b21a-fa3a43c3343c | 2.5057 | -60.9557 | 2024-12-07 00:53:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5c521d-4668-345c-a37c-2151401d451a | -12.9116 | -49.667599 | 2024-12-07 00:53:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32b74e08-b774-32ac-bba8-3be0f29d19c3 | -8.9232 | -44.214699 | 2024-12-07 00:53:00 | METOP-B | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f1fb7c1f-d76b-312c-9e90-90b04dee804f | 2.7306 | -60.376202 | 2024-12-07 00:53:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d124bbfe-170d-31dc-93ac-c8eddc1dedfa | -12.5335 | -49.258099 | 2024-12-07 00:53:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a922409e-16ba-3195-882a-f5ba45b61dc0 | -12.8674 | -51.928398 | 2024-12-07 00:53:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c35860d-7b23-3fb4-8b01-72cdaafb062d | -5.7652 | -46.533298 | 2024-12-07 00:53:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18b1bb38-6a8f-3705-95f3-03a0f0e4092e | -9.2203 | -50.687901 | 2024-12-07 00:53:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ae009d-ba26-3e6f-b1b4-84f7683052ef | 2.5118 | -60.974499 | 2024-12-07 00:53:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0729f544-583e-3eef-9575-e84de5075ff9 | -11.7353 | -54.296902 | 2024-12-07 00:53:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7b949f5-b332-365d-8813-0025dac1c97f | -15.2581 | -53.5555 | 2024-12-07 00:53:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e1d0f69-bc37-3ba6-8882-bd7bcc45cd5d | -13.3814 | -41.276901 | 2024-12-07 00:53:00 | METOP-B | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bd252d42-59ec-3ab9-807a-6fc018f82134 | -13.3909 | -41.274101 | 2024-12-07 00:53:00 | METOP-B | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 06957ad7-96ce-3f7f-8bb8-da3f41bde0b5 | -12.4048 | -49.666199 | 2024-12-07 00:53:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63b2dd0d-995b-3737-aecb-a6fbc4d8ab91 | -12.2802 | -45.489799 | 2024-12-07 00:53:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69389afb-1f38-33d5-9367-0d421d5fd078 | -17.5646 | -47.994202 | 2024-12-07 00:53:00 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cad12f54-3309-34e6-90ee-f687ad6e274b | -12.2343 | -52.4506 | 2024-12-07 00:53:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cba0c80-2415-372d-92e0-6770a6baafc9 | 2.502 | -60.972301 | 2024-12-07 00:53:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e52de623-5579-3c54-8018-21107fecc6ac | 2.4156 | -60.627998 | 2024-12-07 00:53:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f442f348-2ca4-3da6-9c9a-d80f46b867a8 | -10.0347 | -50.5532 | 2024-12-07 00:53:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 424145c0-9d64-3dc7-a22e-074ca150d882 | -11.7338 | -54.289902 | 2024-12-07 00:53:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4654b5f8-bf7a-34bd-9aef-f3aa3fb203ab | -10.037 | -50.562801 | 2024-12-07 00:53:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5e4e016-9b2c-3482-8139-510e2c6df6df | -12.8656 | -51.920601 | 2024-12-07 00:53:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d49f8943-106e-38a7-b993-0890b1d5c9c3 | -15.2597 | -53.562599 | 2024-12-07 00:53:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5699673-32c9-3da4-92d5-9958aa88cc61 | -12.8638 | -51.912899 | 2024-12-07 00:53:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efa321ed-3051-3295-884c-a8d73c088625 | 2.5137 | -60.966202 | 2024-12-07 00:53:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b093318c-bb2f-307a-9493-a5f032dd9cf5 | -15.2679 | -53.5532 | 2024-12-07 00:53:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8a7c17d0-abcc-361a-b08b-08e10afb0081 | -16.0126 | -51.8675 | 2024-12-07 00:53:00 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b4e6bb41-dd96-3edc-ad10-c79aca9eb749 | 2.5039 | -60.964001 | 2024-12-07 00:53:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac0ec02-6fdc-3bf1-8789-7e487409a060 | -17.561899 | -47.983398 | 2024-12-07 00:53:00 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9cf0394b-3b76-3c78-9424-dd5d74c45407 | 2.7421 | -60.370602 | 2024-12-07 00:53:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 917dc150-014d-3f97-a06d-25c1d1600c90 | -12.8558 | -51.923 | 2024-12-07 00:53:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 476b20a6-3aae-33ea-afe6-b9048f9a3108 | -13.4027 | -41.3273 | 2024-12-07 01:00:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 105.7 |
| a0bd5ca4-88ec-3ea0-a673-f7722f765950 | 2.5065 | -60.9822 | 2024-12-07 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 5f722ba7-a17c-38b0-b1a4-731952a3e341 | 2.5247 | -61.0009 | 2024-12-07 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| cbab4033-9248-32aa-9916-afc4456cdc26 | 2.5247 | -60.982 | 2024-12-07 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 5ce1ca15-0c4e-3762-8dbe-0cece757b45a | -15.2528 | -53.5723 | 2024-12-07 01:00:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b8dece6a-1c37-3b5e-be81-d9642060500a | -12.2944 | -45.4958 | 2024-12-07 01:00:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 7f3a7798-cccb-3130-9f0e-d8399eed5427 | 2.5064 | -61.0012 | 2024-12-07 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 75a8c711-034b-3b96-a733-c8130a370171 | 2.745 | -60.3913 | 2024-12-07 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5647bf7f-4b12-3803-956c-12cf1eeaf9cc | -13.4222 | -41.3234 | 2024-12-07 01:00:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 129.4 |
| d72992b2-2f7d-3727-885e-2913f0c2dc71 | -13.4222 | -41.3234 | 2024-12-07 01:10:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 6f8c9d1b-75cc-345c-8179-a0a2fa898b9a | 2.5065 | -60.9822 | 2024-12-07 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 109.8 |
| e6475e63-a246-3903-b040-cb57ff283e16 | -12.2944 | -45.4958 | 2024-12-07 01:10:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 9dbd1e98-fa7c-3a3a-8ec5-d89a152074d8 | 2.5247 | -60.982 | 2024-12-07 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 4b1ed0cd-fdd6-36b4-92cd-4721eb7d3ddd | -13.4027 | -41.3273 | 2024-12-07 01:10:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 939db178-2ba3-3519-b22f-0cf971f95461 | 2.5064 | -61.0012 | 2024-12-07 01:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 3af68d5e-0ad2-3b74-9bf5-19a2e6fd500c | -15.2528 | -53.5723 | 2024-12-07 01:10:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d3551e8f-02bc-38dd-8517-e4e5115a0bc1 | -16.01535 | -51.88938 | 2024-12-07 01:11:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2d659306-ac47-3f43-8463-3f9acb73e236 | -17.5681 | -48.01587 | 2024-12-07 01:11:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7f0bc2f6-fef8-36ca-aa3b-7be53f94ba76 | -15.25891 | -53.56678 | 2024-12-07 01:11:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| d5c01325-12f2-3776-8a87-d170b75da953 | -15.26019 | -53.57648 | 2024-12-07 01:11:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 23466820-9665-32ea-aed3-8900f093a159 | -16.01407 | -51.8802 | 2024-12-07 01:11:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e6df70e8-2da2-3fdb-8cfb-6147e0666ed3 | -7.09136 | -45.21053 | 2024-12-07 01:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4a71b1f7-11d6-333f-9a12-44eab0774349 | -12.40549 | -49.68316 | 2024-12-07 01:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9f59f76f-bc54-37b7-9cc9-92f84521e5d3 | -12.4153 | -49.68159 | 2024-12-07 01:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 20c0ff5b-655e-3819-9754-d37cddc09060 | -12.23685 | -52.45339 | 2024-12-07 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6d1c0dd8-983c-3fd4-88b9-c158c9f8364e | -11.7357 | -54.30563 | 2024-12-07 01:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3c6653a4-aba3-3050-98fe-d0c7d9b16252 | -13.6587 | -52.94819 | 2024-12-07 01:13:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| adcf6296-5dd4-356f-b0bb-0de71fc597ed | -12.86446 | -51.94612 | 2024-12-07 01:13:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ee12fe51-d6c5-3124-9213-37f958bf2548 | -11.06521 | -45.38856 | 2024-12-07 01:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| f31cdb48-0800-3752-ae17-0e756878f549 | -12.91793 | -49.67866 | 2024-12-07 01:13:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bfb20648-b013-3105-905d-69275ae3a4bc | -12.23812 | -52.46243 | 2024-12-07 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5972afc6-d36c-3a55-88c0-1a44c5d977d4 | -12.86317 | -51.93698 | 2024-12-07 01:13:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 27ed7aba-312e-301d-997f-576b24621fd6 | -12.538 | -49.27231 | 2024-12-07 01:13:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 535e3893-02c1-3fba-97b5-e21b8d3fd69e | -10.04062 | -50.57714 | 2024-12-07 01:13:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 2436f46c-e3f3-3044-9875-8c96e2a0de5b | -11.41477 | -51.27868 | 2024-12-07 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9c6d74e0-be4d-3777-ae40-e9bb77d03e87 | -8.93239 | -44.25742 | 2024-12-07 01:13:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 210d0713-a80f-3f10-b2db-0dff082cce90 | -12.2799 | -45.50333 | 2024-12-07 01:13:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| b77f1ebf-44dd-34e1-8b65-65e4e81a8ac9 | -11.73697 | -54.3152 | 2024-12-07 01:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0c83312f-a7d1-3465-9c55-d33d938fc5b8 | -8.27381 | -48.03642 | 2024-12-07 01:13:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5ef7bf8a-0685-3089-bd0e-856b50df113f | -12.85426 | -51.93833 | 2024-12-07 01:13:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 419c5e7a-d8df-394c-b2b8-7c23f151ee3e | -8.93898 | -44.26283 | 2024-12-07 01:13:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f2d9505b-3399-313f-9556-d3648aa2ee88 | -12.2933 | -45.50064 | 2024-12-07 01:13:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ec439493-5a67-3238-b9c2-3b27606ab1c4 | -8.93381 | -44.23087 | 2024-12-07 01:13:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |


[Clique aqui para ver as próximas entradas](README3.md)

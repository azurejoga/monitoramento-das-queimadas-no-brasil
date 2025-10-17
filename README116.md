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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea9c8d76-833f-3ebd-b7d8-84c23f7e81c2 | 1.73377 | -55.78535 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e03bb2de-783c-382f-8851-14a2b8c0bdff | 1.81639 | -55.71309 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 966f2d06-ebe5-33f2-9b15-72e2a21958a5 | 1.79146 | -55.89056 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4c9beecf-ffbe-37aa-9dab-2618fc4d293e | 1.85521 | -55.67144 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7c9771f-788b-30ae-8f1c-9b240c2f6a63 | 1.82054 | -55.70709 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4bd19819-d8d2-3231-b380-be11f17fe582 | 4.5369 | -60.85177 | 2025-10-17 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea02f45a-1707-3ca0-aac0-6983b2bda0f0 | 1.7272 | -55.78638 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2732891-1de4-3526-b2d2-ae68ad3233cb | 1.84956 | -55.67821 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dee4b09d-b1f3-3469-ae0d-973c84b53701 | 1.87743 | -55.84657 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67699e99-94e5-3edf-a9b6-0b918be73847 | 1.85428 | -55.66579 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7f820c27-c591-3646-9019-1280c95d0543 | 1.83425 | -55.69801 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5244203a-1443-3361-b7b6-5b418ba876f1 | 3.96162 | -59.81965 | 2025-10-17 05:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aebca5a2-005f-37d7-878b-3a0bea63ca7d | 1.78416 | -55.88684 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6677c073-ff39-3352-a3c6-bd5f246ac7e4 | 1.82614 | -55.70015 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b05b66ee-41fd-38d2-ae02-57c290b24227 | 1.82769 | -55.69927 | 2025-10-17 05:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62c7f970-597f-3eae-875b-f26df3ebc062 | 3.956 | -59.81592 | 2025-10-17 05:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96adb12f-6151-38dc-92e9-080b862eb6aa | 1.79061 | -55.88537 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 421a0ca6-894a-3658-a7ca-9b004b6c22ee | 1.78385 | -55.92554 | 2025-10-17 05:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11886e74-7597-365c-b3f7-1830dc2229f8 | -1.60406 | -55.7271 | 2025-10-17 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6e5d0ec-aa83-36b7-9af2-51b3618d3636 | -5.10376 | -56.15302 | 2025-10-17 05:59:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd56877f-f1e8-3cf5-ae34-b495dfca58ac | -1.44576 | -60.36327 | 2025-10-17 05:59:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d071712-ef60-31d8-b508-8fad264b70fb | 1.7485 | -55.7639 | 2025-10-17 06:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| bb16f22a-652b-32ef-b239-5209acefbd89 | -9.21622 | -61.54362 | 2025-10-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82feeacf-ed78-38e2-a92b-a502ceafc55f | -9.13881 | -62.3013 | 2025-10-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7a16d10-f35e-30db-ab7f-039a843a6e78 | -12.07092 | -63.68729 | 2025-10-17 06:01:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c8538a-a33c-304d-9589-08928cbaba43 | -9.02646 | -63.55815 | 2025-10-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 218e01bb-9cb3-3c1a-8953-ab0a88897b73 | -9.73153 | -62.95246 | 2025-10-17 06:01:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38b9c405-4174-3702-9b1b-78d08af14643 | -9.87473 | -62.4129 | 2025-10-17 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c7f596c-da33-3898-a693-0fef782036e0 | -9.87512 | -62.40991 | 2025-10-17 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9022e204-a7dd-3da0-a698-5c50e8dfa039 | -8.97272 | -61.97402 | 2025-10-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4dbdb91-528d-3418-b5b6-e319fa172c4e | -11.38242 | -61.21253 | 2025-10-17 06:01:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ccac30b-8297-3e9f-a5b9-036b4c083c3a | -9.14385 | -62.30195 | 2025-10-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 523b597c-601a-3028-b9fa-61747b69c34f | -9.14423 | -62.29905 | 2025-10-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dada0f3c-8aa2-37a4-b5fd-d2920614d842 | -11.38195 | -61.21624 | 2025-10-17 06:01:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69a58c1c-bfa5-3b34-a3ac-c8a70d03d0cf | -12.1332 | -64.29385 | 2025-10-17 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cc541b3-3e50-361c-b81f-5e7c227b0ed6 | -11.38111 | -61.21335 | 2025-10-17 06:01:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7120c6b6-9e30-3ed0-9938-2115f71b2d91 | -9.0156 | -62.00534 | 2025-10-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89302461-d36c-3937-b0c0-864679679268 | -9.15377 | -62.41917 | 2025-10-17 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70522579-b236-3998-b254-f05b5a2d308d | 4.53522 | -60.86431 | 2025-10-17 06:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 700d72d6-0235-3176-89be-a5f4f546fb99 | 4.52863 | -60.86697 | 2025-10-17 06:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d70aa9d0-7587-38c1-86d0-25c7f4a2dc37 | -13.4219 | -47.9511 | 2025-10-17 10:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 8138be3a-5572-3d58-b33b-2f82020c6477 | -13.4416 | -47.9259 | 2025-10-17 10:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 1790d8dc-190b-351a-ae75-990d736c580e | -13.4219 | -47.9511 | 2025-10-17 10:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 201.8 |
| c2883cf4-75b8-381c-922d-433d46ec5fd9 | -13.4412 | -47.9483 | 2025-10-17 10:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 352.6 |
| 3d380695-5cbd-3146-95ad-981c9c1cf80e | -12.3304 | -45.6282 | 2025-10-17 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| c8a5b031-668a-3f8a-a5bb-926abf228d8a | -13.4412 | -47.9483 | 2025-10-17 10:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a0678537-ba4d-34aa-a722-195df22ef766 | -13.0488 | -47.3131 | 2025-10-17 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 0500861b-25e3-338b-966d-26b884a47f36 | -12.3112 | -45.6311 | 2025-10-17 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 348.1 |
| 1ac3e619-75b8-33da-8b47-2fac7d58d75b | -12.33 | -45.6512 | 2025-10-17 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 062d4856-3c0e-31bd-884e-7552eb898518 | -12.3107 | -45.6541 | 2025-10-17 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 047924c1-dd77-3d08-b8c3-109a28e26d24 | -12.3304 | -45.6282 | 2025-10-17 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 7be8c938-a87a-3d23-b2ca-55b5467babb8 | -12.3112 | -45.6311 | 2025-10-17 11:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 93778576-ca9d-3ade-9034-291c4fdc5a1d | -13.0483 | -47.3356 | 2025-10-17 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| c10b6adb-8995-3fff-830d-7e98349e8b8b | -13.0488 | -47.3131 | 2025-10-17 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 162.1 |
| e06904a3-b3bc-30e6-8caf-9f81515ac7d9 | -13.0483 | -47.3356 | 2025-10-17 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 90109d42-6424-3c27-973c-e14f9060b4b0 | -12.4866 | -45.4895 | 2025-10-17 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 15164d64-55bf-3734-9661-9b834ad7b403 | -13.0488 | -47.3131 | 2025-10-17 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 2350811e-ffd7-3b69-8760-1268e179beb1 | -13.0488 | -47.3131 | 2025-10-17 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0a63435d-22ae-34a0-b2ed-19427fa19b99 | -12.1678 | -45.0771 | 2025-10-17 11:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| b5b050a4-e276-3bc4-8d7f-aa4bc7ec110d | -13.0483 | -47.3356 | 2025-10-17 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e4befa95-4d5c-3ad4-bf7f-9661a123f352 | -12.4678 | -45.4694 | 2025-10-17 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 858c1f9e-4379-3a62-a2d8-78ba8dbd62e7 | -12.1678 | -45.0771 | 2025-10-17 11:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 851b32cb-83ad-31b1-a290-3d564b36d215 | -10.534 | -49.5471 | 2025-10-17 11:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 17e5e4a3-12a7-33c8-b3c8-d8387fca38e7 | -13.0483 | -47.3356 | 2025-10-17 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 8235ae45-3844-371f-a4d8-8a1a7bba43a6 | -13.0488 | -47.3131 | 2025-10-17 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9862d7c7-9fee-39e6-b001-99eb421f7e84 | -13.9312 | -45.6239 | 2025-10-17 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| dc8e3793-0b46-3371-b6ff-291ebecd666d | -11.4164 | -44.2373 | 2025-10-17 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| c6e24471-1fbb-32c2-a393-e4b9eb25ec97 | -11.4168 | -44.2139 | 2025-10-17 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 85fe7880-0c7c-3202-ae72-b9fd8ea829b3 | -11.1406 | -45.8437 | 2025-10-17 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a4ad2fa0-3cf3-3f7a-86b1-d6a4c9659a34 | -11.398 | -44.1933 | 2025-10-17 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4f2b1725-729a-3bfd-9b3f-0e196d5a19e4 | -11.3972 | -44.2401 | 2025-10-17 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 5893ede8-2104-3c92-8b00-b3bb1b5084a9 | -13.4412 | -47.9483 | 2025-10-17 11:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 771ac867-f1b4-3e44-a57f-c1dacf855ba5 | -11.5917 | -44.0707 | 2025-10-17 11:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 90160461-a0b4-36cd-960f-4922babd2062 | -12.5054 | -45.5096 | 2025-10-17 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 68c08e99-097a-3f8d-8782-f7b93ca04866 | -13.0488 | -47.3131 | 2025-10-17 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 0d0b23ce-7207-30a6-9d2d-02b5cd981225 | -11.1403 | -45.8665 | 2025-10-17 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| b360ca66-2372-3590-a626-29e9286e6405 | -11.3976 | -44.2167 | 2025-10-17 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 6f31114a-282e-3e5b-9ed5-b4252d44fe18 | -13.0483 | -47.3356 | 2025-10-17 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 9981852d-b86e-3522-a08d-5eb3ddd6817c | -12.4866 | -45.4895 | 2025-10-17 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 1776ea5d-038c-3be2-8065-2c4e8309d786 | -11.4172 | -44.1904 | 2025-10-17 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| fd69ee47-cbd3-3be8-a790-aa6b90d25436 | -13.4194 | -42.3293 | 2025-10-17 11:40:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 6138247d-e701-34a1-a38a-885d6c07d32f | -13.4412 | -47.9483 | 2025-10-17 11:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1ff1714e-8386-340d-89ba-05fd6c629542 | -11.5729 | -44.0501 | 2025-10-17 11:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 80b04524-fc55-31fa-b191-80c3864d6eb6 | -11.398 | -44.1933 | 2025-10-17 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 571338c5-9f2d-3548-916d-201a3f3883f4 | -11.4172 | -44.1904 | 2025-10-17 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| e43749cc-8bef-3ae2-ba89-4d230e2ba527 | -11.4164 | -44.2373 | 2025-10-17 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| b24ae494-19a9-392b-aef7-cd0f28beae09 | -11.1403 | -45.8665 | 2025-10-17 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 287e7bae-215a-3648-b6a6-702b2b3e07b5 | -12.4866 | -45.4895 | 2025-10-17 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7e5d3988-3594-394a-b70f-6eab771bf9d9 | -11.5917 | -44.0707 | 2025-10-17 11:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 0e282f9f-70ea-3ecd-b461-1ebc6d92e748 | -11.5921 | -44.0472 | 2025-10-17 11:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 8833a25e-30fe-3a0c-81b1-66ad052c1eda | -12.487 | -45.4664 | 2025-10-17 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3b73589e-0cef-32a2-ab51-95475730b8cb | -13.4194 | -42.3293 | 2025-10-17 11:50:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 11df07fe-1806-31e7-8fc6-21bb9cb2383b | -13.0483 | -47.3356 | 2025-10-17 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 059dad40-b34a-32f2-8369-893377431b51 | -11.4168 | -44.2139 | 2025-10-17 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| ca02646f-f1df-306b-b05e-6a70128fd9be | -12.5054 | -45.5096 | 2025-10-17 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 8670772e-a5fb-3480-9b7d-16135469b444 | -12.4678 | -45.4694 | 2025-10-17 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| f72af60a-495c-3fd6-af4d-9e5079522e2e | -11.3976 | -44.2167 | 2025-10-17 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| fc00a0d5-510d-39e6-80aa-a4ac91729389 | -11.3972 | -44.2401 | 2025-10-17 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 67cbab82-4705-3ae1-9b5e-323076d87475 | -13.0488 | -47.3131 | 2025-10-17 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 0559060a-334e-31bc-8227-29e18c920a68 | -11.5921 | -44.0472 | 2025-10-17 12:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |


[Clique aqui para ver as próximas entradas](README117.md)

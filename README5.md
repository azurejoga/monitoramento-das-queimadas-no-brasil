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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64436ad3-a92e-379d-be71-0331185d9c06 | -14.2729 | -45.9803 | 2025-10-31 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| bfc3275c-c237-3976-8c4b-477b32d39550 | -8.0821 | -45.1568 | 2025-10-31 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 5175f511-0a78-3d9e-a532-4d5fb8803e62 | -5.7072 | -48.8784 | 2025-10-31 02:00:00 | GOES-19 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 4fb614b9-66a0-3bd8-bddb-78f6e9efe8b8 | -14.253 | -46.0068 | 2025-10-31 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| b26df805-2905-38d9-90e4-ceab914b96b2 | -14.234 | -45.987 | 2025-10-31 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| a83c22f5-6777-32ba-8a63-6f2c175982ef | -9.7232 | -48.0248 | 2025-10-31 02:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| dfd28dfc-3c9a-3e6e-b7d6-6ee207a98196 | -4.858 | -42.9566 | 2025-10-31 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0046db18-1a18-30dd-b950-0b876f3615d9 | -9.7421 | -48.0228 | 2025-10-31 02:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a09251cc-b9d4-3c5b-8c1b-6e8c26d0bfc8 | -10.5458 | -48.7002 | 2025-10-31 02:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| da50641a-daef-34c6-8f90-9fbd39dc94b9 | -5.0399 | -43.6205 | 2025-10-31 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| fa6a8408-59b5-3238-8969-8c71edffc6f6 | -10.5483 | -44.7773 | 2025-10-31 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 603b0be2-1b95-3a80-9d02-204751c62dd6 | -5.0401 | -43.5973 | 2025-10-31 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 146e34cf-bbe1-3294-a8e8-3a54a5d6d21b | -14.2335 | -46.0101 | 2025-10-31 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0a2b027c-0fc6-3470-a30c-b1e8caa0d491 | -5.0212 | -43.6218 | 2025-10-31 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d9973e57-b0a5-3cd7-8623-4c05e49f9f42 | -14.253 | -46.0068 | 2025-10-31 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c67b3be7-3e9f-3ae1-a59a-92170b4e654e | -9.7421 | -48.0228 | 2025-10-31 02:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b5fd4b38-e36e-367c-84f9-43a1526e4439 | -14.2729 | -45.9803 | 2025-10-31 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| af497b99-52ff-3800-89e8-ce9f60e1b063 | -9.8631 | -44.8425 | 2025-10-31 02:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| e1ced22a-20a9-3919-a287-08ad04183b00 | -9.8627 | -44.8656 | 2025-10-31 02:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3e8cff00-8904-3cf2-8df7-d92d7ae454b8 | -10.5293 | -44.7798 | 2025-10-31 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 468f0599-cd18-34f7-9bce-6d5d8f5949ec | -14.234 | -45.987 | 2025-10-31 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 9a3b36c6-47c7-3a3a-be70-78f16232c6b3 | -2.3178 | -48.5717 | 2025-10-31 02:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3111736e-200b-3c16-a0a8-71456f5dfc3e | -14.2535 | -45.9837 | 2025-10-31 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 2150bbe7-068e-3bd9-9cea-7f6480ed7a2d | -9.7232 | -48.0248 | 2025-10-31 02:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 973bf70b-abff-3813-adf8-58fa4807dd8a | -14.253 | -46.0068 | 2025-10-31 02:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 6766404e-7d46-3fec-9270-b8ac2bea2844 | -8.0821 | -45.1568 | 2025-10-31 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 8c783af5-4f7e-3efc-a9f3-242482bb0b4a | -9.7421 | -48.0228 | 2025-10-31 02:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 115c1457-387b-3254-b938-c04c9887707a | -9.8631 | -44.8425 | 2025-10-31 02:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| fc1ff96f-40bb-3d8b-a8a3-a4c71b724853 | -8.0824 | -45.134 | 2025-10-31 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 7f39cc8f-0ba9-3dc9-a98b-6abe3ce02a7b | -10.5293 | -44.7798 | 2025-10-31 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 84ce7d83-a5bf-306b-9848-2d1904e96192 | -10.5483 | -44.7773 | 2025-10-31 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 0fe07b59-f696-3e67-a0d3-7de2642ba553 | -5.0401 | -43.5973 | 2025-10-31 02:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| d4802406-301b-3560-a7bc-c0fdc8ebfc72 | -9.8627 | -44.8656 | 2025-10-31 02:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 1a1938eb-bf14-3e21-bc71-983d7b87a5c6 | -9.7232 | -48.0248 | 2025-10-31 02:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| cab8fcff-61b7-3935-8845-6acf2478e488 | -14.2535 | -45.9837 | 2025-10-31 02:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 85a21050-d947-334e-b613-c3862dbbdffc | -8.1013 | -45.1321 | 2025-10-31 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 3a173d8f-bd93-3cb8-b34d-1fba8dd657cb | -5.0399 | -43.6205 | 2025-10-31 02:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 8db85708-f8e4-30a4-a68b-24b7b2cb1765 | -8.101 | -45.1549 | 2025-10-31 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 06533707-557b-3aa0-934b-c43e9bf1b918 | -8.0824 | -45.134 | 2025-10-31 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 116a3ef8-1ef9-3f09-906d-9d42386b119f | -5.0212 | -43.6218 | 2025-10-31 02:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| df587226-3c7d-3d85-a4cb-a7351ed88e5e | -2.3178 | -48.5932 | 2025-10-31 02:30:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 6335ae06-7341-3e5b-8592-0fcb462e2b5d | -8.101 | -45.1549 | 2025-10-31 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 99c80d1d-c02f-33eb-a39f-89444c9abafe | -8.1013 | -45.1321 | 2025-10-31 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 504b6713-28f5-361e-a1dc-5a3da2e59394 | -5.0399 | -43.6205 | 2025-10-31 02:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 54d9a668-6a9d-3d89-9c0c-737c4db7bd2b | -5.0401 | -43.5973 | 2025-10-31 02:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 535c82dd-b7c3-34e8-b6c2-b34a1836e894 | -9.8631 | -44.8425 | 2025-10-31 02:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2670e67b-5d95-360f-92e2-acc5c24d901a | -10.5483 | -44.7773 | 2025-10-31 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 7c91ecb6-8820-39fb-af50-c3c5018b73cb | -10.5293 | -44.7798 | 2025-10-31 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| fa3e9c6a-866a-31fa-882c-5286562cf059 | -7.668 | -43.5857 | 2025-10-31 02:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3d3f5881-758d-3547-bd09-03dc5522ac25 | -2.3178 | -48.5932 | 2025-10-31 02:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b32f6b9e-474e-3518-864a-252c73f20603 | -5.0212 | -43.6218 | 2025-10-31 02:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 6eb2d90e-94d9-35e4-a717-7c5568d9b921 | -7.6491 | -43.5876 | 2025-10-31 02:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| a6c1bf3a-dc83-3702-bb24-22742f1047fd | -5.0399 | -43.6205 | 2025-10-31 02:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 081148ab-7cc7-345b-94df-bc78373bb5f0 | -3.017 | -49.4482 | 2025-10-31 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0bee35b6-04d6-367d-bd65-45625a9898be | -5.0401 | -43.5973 | 2025-10-31 02:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a508a7d8-9409-304b-95bf-735237d59c5e | -3.3024 | -51.9254 | 2025-10-31 02:50:00 | GOES-19 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| fe62d813-024f-389d-9153-87ececfe6f5b | -3.0355 | -49.4476 | 2025-10-31 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 494cc746-3760-3591-a4d3-3ea56ed83c16 | -9.7421 | -48.0228 | 2025-10-31 02:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 01fd0d44-1568-32a5-b783-cdddc09df7c8 | -11.1423 | -50.7242 | 2025-10-31 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 91014e7e-3d5c-37da-ab7d-36aa8cff9a0e | -8.1013 | -45.1321 | 2025-10-31 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 385eb9ce-cc5a-33df-a76b-32cd529a84bc | -7.6491 | -43.5876 | 2025-10-31 02:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 49ba4361-8047-362a-ae0e-09dc6d73f9fe | -7.668 | -43.5857 | 2025-10-31 02:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 9eacfdfb-5d80-310d-b193-600fc98ef4f1 | -8.0824 | -45.134 | 2025-10-31 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 07a510c0-28f0-3749-a8d0-3d4add4722ec | -11.142 | -50.7455 | 2025-10-31 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 8935ddf6-ecab-33bd-b0af-be3451e1c712 | -5.0399 | -43.6205 | 2025-10-31 02:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 98657182-fb4d-3977-a8c8-34b48f0ff474 | -9.8631 | -44.8425 | 2025-10-31 03:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 0e45c24c-a940-3e91-b4ab-54c984224a52 | -5.0401 | -43.5973 | 2025-10-31 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 2f4882c4-f664-3e49-83ce-5c845241e3bd | -5.0399 | -43.6205 | 2025-10-31 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 03beff0a-c2f7-3590-b757-2322d10ebb52 | -9.8627 | -44.8656 | 2025-10-31 03:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 36de8856-65ce-39bc-86ca-fe7deaa5bdd9 | -8.0824 | -45.134 | 2025-10-31 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 47633079-1ce5-3358-aff0-fb3085fb9c02 | -3.017 | -49.4482 | 2025-10-31 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| bf528d7b-ac42-366b-b8e1-f836cfd504ae | -9.7421 | -48.0228 | 2025-10-31 03:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8fbd3fd5-a1da-3cdc-b1b2-1f30575835e4 | -8.1013 | -45.1321 | 2025-10-31 03:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f48a9852-aff3-301e-978f-12675adff7fd | -8.1013 | -45.1321 | 2025-10-31 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 203bf222-cc73-3ab8-886c-3189915c97a7 | -3.017 | -49.4482 | 2025-10-31 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 96dd1a3f-29f0-3a05-b639-825db6766bb9 | -5.0399 | -43.6205 | 2025-10-31 03:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| d196ffe0-97e9-3a6c-b0e8-672102ccea7e | -13.8967 | -47.3405 | 2025-10-31 03:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| da481274-cfb9-393c-99ca-201719098f28 | -8.0824 | -45.134 | 2025-10-31 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| abeac506-c4e9-36ac-be48-2fb071aa908a | -5.0401 | -43.5973 | 2025-10-31 03:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 9725bcef-6804-3d92-9c67-963c533c55d9 | -3.3024 | -51.9254 | 2025-10-31 03:10:00 | GOES-19 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 06da5167-4030-3f00-a733-b299eaa834f8 | -6.19716 | -42.51968 | 2025-10-31 03:15:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 69529ab9-6a99-3f60-b8ca-f64bab62b432 | -8.39319 | -41.84566 | 2025-10-31 03:15:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3ced1d85-d17b-3bae-91c5-14e9e353b498 | -6.16668 | -41.618 | 2025-10-31 03:15:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 201054cf-23f7-3f0b-a997-c5f9c27979e6 | -8.51466 | -39.6433 | 2025-10-31 03:15:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 033d92ca-67d1-3251-a994-8cd63a846a02 | -5.45842 | -40.87189 | 2025-10-31 03:15:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 064bd28a-7f2b-38e0-8703-52cf5ebb26e3 | -5.9505 | -39.83877 | 2025-10-31 03:15:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1eadbd8a-008b-3c4c-a86d-31600ad61924 | -8.90071 | -37.96629 | 2025-10-31 03:15:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31ae27a1-9e7f-3987-a344-9e7f52164036 | -7.33836 | -39.32274 | 2025-10-31 03:15:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4c82f72d-357f-3d16-89a3-5fa012c82d44 | -7.33384 | -39.32119 | 2025-10-31 03:15:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9a91c075-23b1-3691-ba9a-b591039edaa1 | -5.94989 | -39.83623 | 2025-10-31 03:15:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f81715fa-2bff-357d-bc43-20921e4a85c6 | -5.79124 | -40.80817 | 2025-10-31 03:15:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0fabcc45-52a5-3b6f-bbf0-b6e538c91cc9 | -5.8067 | -40.83066 | 2025-10-31 03:15:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3d112872-6a71-3037-be1f-5b4557539c81 | -6.51678 | -40.79551 | 2025-10-31 03:15:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f4e36c92-a788-334d-bbf5-268f653b57c2 | -5.88664 | -39.76311 | 2025-10-31 03:15:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c135e04d-4bc3-30b5-8b4d-1e014a4c7c4c | -6.5179 | -40.79826 | 2025-10-31 03:15:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 64c761a1-f6d3-349c-ba90-bfc65f6005bd | -5.5451 | -38.03428 | 2025-10-31 03:15:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3754c379-f6e0-3299-a98e-d666f68f0d9a | -5.46399 | -40.87457 | 2025-10-31 03:15:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fea8a9f9-0609-3b05-aa63-cb184b030b66 | -5.80288 | -35.58517 | 2025-10-31 03:15:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cbb8037f-0353-3f24-8472-e3dbe81beb7d | -5.46489 | -40.87336 | 2025-10-31 03:15:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e7925b42-a776-3758-8e4e-85d0a3c5dd00 | -4.57071 | -38.28621 | 2025-10-31 03:15:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |


[Clique aqui para ver as próximas entradas](README6.md)

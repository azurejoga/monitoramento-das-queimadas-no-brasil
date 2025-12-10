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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95e0fb8a-d0f1-3b3b-ab20-c3afcbe616b5 | -3.68687 | -43.82347 | 2025-12-10 04:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56d9e024-9f19-3656-bf54-dfabb285cbb8 | -4.31299 | -50.67846 | 2025-12-10 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fec73d9b-e043-32b9-baf8-2098744a944e | -1.32339 | -52.4604 | 2025-12-10 04:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f679ca5-72c1-30e9-a912-441c377dce20 | -2.38614 | -56.05931 | 2025-12-10 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8a5549b-7b48-37a2-bac7-ae1af8f8efcb | -2.59239 | -54.55711 | 2025-12-10 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 044c3a59-4ae2-356f-b6bd-9157dcb55dc7 | -2.58617 | -53.99517 | 2025-12-10 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a48dfe48-5644-3d1c-a713-2a792f41d76d | -1.58754 | -54.12288 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f76a85f-95bd-36e2-8229-bb4574cda733 | -5.16946 | -43.12321 | 2025-12-10 04:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f0285481-b08e-37d4-ba34-ecd93a34a2cd | -3.39737 | -42.46347 | 2025-12-10 04:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c73b96e3-0dba-3131-a769-5cd9a1a71d09 | -2.3747 | -45.80516 | 2025-12-10 04:57:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5198c30a-f8f4-3a8d-bed9-2806819ac546 | -3.41952 | -41.65873 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d72eef9a-8ce1-3453-8936-4701dd22d8e1 | -6.00276 | -40.38165 | 2025-12-10 04:57:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ba460ab2-f2c3-366b-b5d1-ecaaa55a1673 | -3.57823 | -52.1118 | 2025-12-10 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 632106e4-e6c0-3495-a652-5c3a8d66b076 | -2.86586 | -48.7795 | 2025-12-10 04:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37fde2e3-0284-350f-b998-f6e4e3002569 | -3.41856 | -41.65578 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 57e70c59-f995-392b-836a-039a9d5f8617 | -2.38677 | -45.82308 | 2025-12-10 04:57:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 842960fc-ad3c-3a60-9868-96bbe2f19aa7 | -2.41802 | -45.84386 | 2025-12-10 04:57:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1b4010f-0532-3f12-8160-7c11d3151786 | -1.41433 | -54.29227 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aff876ef-73d8-36e7-990b-3a2206a963b5 | -3.22765 | -52.64282 | 2025-12-10 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27c10076-f5dc-3467-845e-6d39c2c4f998 | -2.6551 | -54.84647 | 2025-12-10 04:57:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02dd03fa-65e5-332e-9b76-e94a130221da | -2.8209 | -45.28092 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aae6e956-78c7-39d9-9308-e0f5a6ab5566 | -2.88332 | -45.24284 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58626947-9b6f-31a9-9e36-9c82a55b0678 | -3.43955 | -41.65633 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0b3bad9a-45b2-3366-aa2b-6b2b2ee30d2f | -3.0105 | -52.68453 | 2025-12-10 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 055a67e2-8a89-327d-9e08-c799acc24af1 | -2.8833 | -45.23866 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa8a659f-a1f8-3e08-ae02-55a1d470d1f6 | -4.34778 | -46.09228 | 2025-12-10 04:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52416111-a484-31d5-b604-3f58815966c7 | -2.48551 | -47.7731 | 2025-12-10 04:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2efd3a94-0ef8-382d-a1c3-983596f1758c | -3.68125 | -43.8227 | 2025-12-10 04:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aef03ed4-fb13-38c8-823a-0c6f4776eac9 | -3.37333 | -45.83326 | 2025-12-10 04:57:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05957f18-2f7c-394d-a520-b6c7df09aa25 | -6.00748 | -40.3796 | 2025-12-10 04:57:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc58579b-bcd8-3eda-8e59-d0384befb542 | -2.84161 | -48.90938 | 2025-12-10 04:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ded7aee-ffa6-3cf8-84b4-97aae0d6dcbd | -2.8006 | -47.34723 | 2025-12-10 04:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7b574ec-c826-3698-8bf7-14c535405253 | -2.06779 | -49.00601 | 2025-12-10 04:57:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e346413-827d-32e0-92f5-5da0f5c85d77 | -1.58809 | -54.11939 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f8fa714-e0f1-3c33-907b-793387243213 | -3.39734 | -42.46542 | 2025-12-10 04:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| af8deaa8-27df-30dd-8cb3-412432ee8f2a | -3.55537 | -53.12894 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ebf0f9f-da40-324c-b121-f692bf31fded | -8.31868 | -54.95544 | 2025-12-10 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8fa6548-e3c6-3e2b-9ece-24fc6a223c91 | -2.30006 | -48.59472 | 2025-12-10 04:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86e0488d-d553-3d5e-bd13-ea468245c992 | -2.37466 | -45.80813 | 2025-12-10 04:57:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b80b09a-cb4b-304b-8a39-7ceacde03864 | -3.43863 | -41.65337 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 61024edc-bd3c-39ed-a228-bbc0d351c50d | -1.59774 | -53.86465 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a89a5c4-9577-3404-a50b-9e7e0ea8fc6b | -1.66742 | -54.57948 | 2025-12-10 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74822327-ad20-34ce-9ea9-5d75a3850fec | -2.72211 | -53.19908 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1db350b3-adf0-3653-ae11-fc1b8e989598 | -1.47652 | -54.20183 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ff33342-ee23-30e1-bfe4-7d88a0a7cfba | -3.69976 | -50.94427 | 2025-12-10 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77703f60-2c36-37f1-80de-d5d0e2366a3f | -1.62015 | -53.37755 | 2025-12-10 04:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae3ee5a4-0015-3552-904e-d024e5eaaf3c | -2.88791 | -45.24235 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6e81ae0-f9ea-3b6c-8aec-0d40305410ba | -4.5452 | -45.90648 | 2025-12-10 04:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 309913e4-7955-3548-bdc4-fcde024e4bf1 | -1.47603 | -53.53794 | 2025-12-10 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a2f07bf-5bfc-390c-8532-e0f2c903b7ec | -2.74656 | -45.40281 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b61255a-ea36-3872-8d63-e8c4db3dcf0e | -2.06394 | -49.00542 | 2025-12-10 04:57:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 27cd04e8-7d9c-3b00-9727-a7f125f6a31b | -3.23111 | -47.47458 | 2025-12-10 04:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 33431c5d-cfe8-3ca8-a46d-46a25154303b | -2.0839 | -52.05136 | 2025-12-10 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e6e3a42c-d6c8-3b86-9ae4-78cc899fbed8 | -3.69413 | -43.81318 | 2025-12-10 04:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39ee43d1-df49-359f-9b09-79893cf131eb | -3.39669 | -42.468 | 2025-12-10 04:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fa8f7a15-9c02-399b-9b9b-b8f3ab10a173 | -2.59295 | -54.55359 | 2025-12-10 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01473913-86b6-32e0-b238-49d644da7783 | -2.74623 | -45.40152 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35f31c34-6a1d-3de5-9e00-e0431c9f4fdc | -12.51329 | -58.36165 | 2025-12-10 04:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a9b928d-97ea-312d-9d15-3a42a5aecb39 | -9.81469 | -47.93325 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b167b6c1-d3be-39d1-bc43-90276be2c9bc | -9.81833 | -47.93139 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df921470-a761-3fb6-9db9-262baf219130 | -9.80904 | -47.93003 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6adb93f-7662-3426-bd14-436e70b3de69 | -10.98993 | -53.99941 | 2025-12-10 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a0c5d18-450a-361d-a03a-e1a1bbcbef0f | -11.12842 | -53.93914 | 2025-12-10 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eec1bd38-5776-3b8e-b478-faec968e8958 | -12.51613 | -58.36628 | 2025-12-10 04:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb0c9928-d136-38f8-b633-583256bd7769 | -9.81368 | -47.93071 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 107824e5-e3dc-383c-b2dd-63dea5e406a2 | -9.81074 | -47.92762 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39ce23f1-4324-30ab-82ca-77b0147434b9 | -9.81933 | -47.93393 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c38fc3fd-4095-38bd-b5ae-aefd2c8fc340 | -9.80439 | -47.92935 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 958eed2c-1c03-395f-ba99-b11f1f845c8a | -12.5168 | -58.36226 | 2025-12-10 04:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 348283d5-ee91-37c7-846a-bf5c122ec0cf | -9.81005 | -47.93257 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64e9c428-15d2-30d9-b93f-43a3beb5466b | -11.13179 | -53.93967 | 2025-12-10 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94e15373-6077-3dc4-b224-6f34b50373ee | -12.51261 | -58.36567 | 2025-12-10 04:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 693885ed-71df-37d4-8048-3e7c45796c10 | -9.82231 | -47.93703 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 957f1ba6-b003-3425-8030-207594a74b10 | -9.81766 | -47.93635 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c8fb018-39d0-3af7-bb5d-dc24ba42fa03 | -9.81863 | -47.93885 | 2025-12-10 04:59:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11f294a7-c8ee-39fd-a1b5-9607f51d1ffb | -12.50978 | -58.36104 | 2025-12-10 04:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5845c6a-83c8-3484-a777-643d1a6f09a1 | -12.51396 | -58.35763 | 2025-12-10 04:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b8e51fd-44e3-3b2c-b07c-0ede24ea8ed9 | -20.91711 | -56.37936 | 2025-12-10 05:01:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b235ee85-8890-38fb-9831-c3b411bda233 | -1.01704 | -53.72977 | 2025-12-10 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 532804f4-e4da-3676-aaef-96e2812c7ecf | 2.02703 | -55.6718 | 2025-12-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e2f22ac1-7989-3d45-8200-5e6ad390460b | 2.02542 | -55.66186 | 2025-12-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b733c566-4ff1-3e00-ac83-3e217329934c | -1.47289 | -54.20033 | 2025-12-10 05:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a223eb5-1b65-3c12-977f-5bc2b2e23342 | 2.02764 | -55.67561 | 2025-12-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 715302de-2bab-32bc-b5d6-cc93f8309e5a | 2.02596 | -55.66521 | 2025-12-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 161c3035-fb6c-3dba-a7eb-1681e1d632c2 | 3.27669 | -60.84638 | 2025-12-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d72be9f-14e2-3096-b6ac-1d4cda96a86f | -1.01535 | -53.73003 | 2025-12-10 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39f776c6-c6c5-3b3c-80a3-6b2bbcf0e625 | 3.34237 | -60.87285 | 2025-12-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68238f60-33f0-3455-8319-8514daa5aa02 | 2.20808 | -60.15381 | 2025-12-10 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9eb2636a-93c6-3b9e-acc4-beee9a4bab53 | -1.41651 | -54.29314 | 2025-12-10 05:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8ff303f-2d3b-3952-9755-f2179f778f1d | -1.02175 | -53.73113 | 2025-12-10 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28a43c2a-03da-3246-bb68-b26da64be5e2 | 0.45701 | -60.42453 | 2025-12-10 05:46:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed6fced6-54eb-3822-acb8-812b89cf89a7 | 3.37306 | -51.27007 | 2025-12-10 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39dbfb1f-6e00-38e9-bdc3-45be18b2c62d | -1.47552 | -54.20029 | 2025-12-10 05:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 591760e5-b629-3f6c-8dbc-46491ab65025 | 2.02648 | -55.66842 | 2025-12-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c0d9da1b-8e0d-3043-8638-c7291c6444c6 | 3.38 | -51.26876 | 2025-12-10 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1254d2a7-88c5-360e-bf8c-005a8742e3ae | 3.37747 | -51.26049 | 2025-12-10 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca9b92cf-21fe-33fa-a145-af6d9c4f843e | 3.37889 | -51.26214 | 2025-12-10 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1631a568-6c48-3bdc-9193-2393c90fe9b6 | 3.34332 | -60.87069 | 2025-12-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 122334cd-8ef1-3b61-96c7-a74662597b82 | 3.37862 | -51.2671 | 2025-12-10 05:46:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 516c10bc-6a8a-333b-b3a5-ff7525c9e857 | -1.4782 | -53.53699 | 2025-12-10 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README15.md)

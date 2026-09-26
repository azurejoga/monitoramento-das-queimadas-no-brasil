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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2185d84-207e-32e3-b803-c4745780e080 | 1.5835 | -55.8448 | 2026-09-26 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 89a09dca-572c-30b4-82b9-508cf88b0ea0 | -12.2887 | -50.3358 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 347d9550-d810-3651-8729-b9d3f3e7151e | -12.9461 | -51.0481 | 2026-09-26 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f6d0e8eb-74bd-3b01-9966-9740ef3bd2f2 | -12.0365 | -50.6233 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 6104dfa3-bf53-3eec-a601-7c83dba43832 | -12.2254 | -50.7294 | 2026-09-26 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| a7042b4c-48f9-375e-a3ab-835046d61219 | -13.3824 | -51.3138 | 2026-09-26 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 42ae7193-5f3f-36f2-926c-f814f494447a | -11.7322 | -50.6158 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 35105eda-34b7-38a5-b21a-814468736c96 | -11.8472 | -50.5598 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 720a0587-f0fa-3966-ae48-75d714e272a6 | -11.7094 | -50.8745 | 2026-09-26 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 46fde4a0-f99d-33a7-81d7-8996d26b7058 | -13.7146 | -48.7951 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 8aec75c6-be90-3604-93a5-c48ebb9de508 | -11.1372 | -54.0045 | 2026-09-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8c59cbe0-1c3e-3189-bac1-2ad6073a7952 | -12.1112 | -50.7215 | 2026-09-26 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 90d2523e-c98b-39ae-a0fb-f5b8cc26d7ec | -11.118 | -54.0268 | 2026-09-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| edbdd1c0-8c0d-30cf-9677-227e3f553f0b | -11.7697 | -50.6543 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 887cbd46-c6ea-3d8a-87b4-307ff454b8c8 | 1.6566 | -55.9424 | 2026-09-26 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| bde8309d-8927-36e9-a842-a4dae700e313 | -12.2508 | -50.3189 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 918cdc25-5033-3ffd-8cb1-356ca32604e5 | -11.8475 | -50.5384 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| f3a246f7-7d11-3c06-a7af-855b5aba279c | 1.6018 | -55.8643 | 2026-09-26 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 98c3d9b8-70cc-3323-b150-003a050ac80f | -11.1183 | -54.0062 | 2026-09-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 796bffaa-c158-3e32-b5bf-aff95a28ec11 | -10.6928 | -60.7322 | 2026-09-26 15:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 981703b1-2deb-3563-a7a0-82b21c4262b2 | 2.1083 | -50.8375 | 2026-09-26 15:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1cfcca6a-8a9d-3780-85ea-97c3ea947f2f | 1.6382 | -55.982 | 2026-09-26 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| b5c9ff40-7454-3e0d-88cf-7b111cce246e | -10.7115 | -60.7312 | 2026-09-26 15:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 686d6a12-c377-39c5-9c7b-b5215a730784 | -1.0976 | -49.2127 | 2026-09-26 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1c37c85d-97dd-3ce1-b299-5e0f4fe64255 | -12.5883 | -51.9406 | 2026-09-26 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 9c45325c-9772-35b1-93b7-4296d32c3859 | 1.2794 | -50.851 | 2026-09-26 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 63f1a0dd-028f-3297-b088-bbefb990c907 | -11.751 | -50.6351 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| eca54cd6-49c3-34b8-a5a5-e6eef0655b13 | -11.8094 | -50.5428 | 2026-09-26 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 7d5cf1d0-bb4c-3e82-9f70-a1908c28d5b8 | -12.588 | -51.9617 | 2026-09-26 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3e0bd460-8974-3cad-a405-57b2fc83e153 | -13.4012 | -51.3328 | 2026-09-26 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 78286336-5bb3-3528-b6c3-fead35351212 | -12.9461 | -51.0481 | 2026-09-26 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 8ca1f71a-32f3-3f35-b7ad-ec0d59cab0d6 | -11.0802 | -54.0302 | 2026-09-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 633c026b-484d-394c-b408-b83d65757eb7 | -12.1938 | -50.3043 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e9bf3ca9-7f69-38e4-9144-6948d16e63e6 | -1.0792 | -49.213 | 2026-09-26 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 9bd40a0e-7b70-304d-ad3d-3cf28df92df1 | -11.118 | -54.0268 | 2026-09-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| a3237844-6556-3e6c-99fd-89427cf2206a | -12.1306 | -50.6978 | 2026-09-26 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3481eaae-cd34-390c-8fc7-011f5bb79b4f | -12.5883 | -51.9406 | 2026-09-26 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 006810b9-b09e-374e-8bcf-195b781f2c44 | -12.7674 | -54.0502 | 2026-09-26 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8bda3bb9-be36-3f92-b0b9-1610b0d6ba83 | -12.0454 | -50.0424 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0ee5c327-5aff-3eca-adb7-37c100f93403 | -12.0645 | -50.0401 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| f025e259-be5b-3cab-aa4f-029d3d84aa71 | -11.1183 | -54.0062 | 2026-09-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 2f101154-f60f-3303-acb5-c0f1a80068d7 | -1.3008 | -49.0826 | 2026-09-26 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b8931dcb-732d-3730-86f7-402c19b89718 | -0.8584 | -48.6606 | 2026-09-26 15:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 21c981da-b8d7-3d39-8e09-95b425b334e6 | -12.1303 | -50.7192 | 2026-09-26 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| c96ab880-c6b7-3714-86ed-91ebd8766351 | -6.2401 | -41.6153 | 2026-09-26 15:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 284.3 |
| 7770e7ec-cfa2-3531-b934-879c1e2c8830 | -12.1112 | -50.7215 | 2026-09-26 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| d96a48c2-fd48-3a14-b0f3-f157be01c9a7 | -1.3008 | -49.0613 | 2026-09-26 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| eec9cf0b-ddb2-3418-82e0-812c7c09d5d1 | -13.7146 | -48.7951 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| fc0feb8d-6c01-33f7-b5fd-2992703adc6f | -10.6928 | -60.7322 | 2026-09-26 15:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c3a90207-3dae-31cf-aff4-5d9677ec49db | 1.6199 | -55.9626 | 2026-09-26 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 1d98373d-34ab-3d99-a579-ba395d6debcf | -11.7887 | -50.6521 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 49149749-0d2f-3937-907f-446e5f807e8a | -12.0277 | -49.9583 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 319ed36d-b2c4-3158-816a-8daf30b438f3 | 0.7082 | -51.437 | 2026-09-26 15:40:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 06608c59-23da-3152-85aa-c4e0c884e9e1 | -11.0994 | -54.008 | 2026-09-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e2761171-843d-3b66-9c02-5c3562a30937 | -11.77 | -50.6329 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 2b663849-239d-39aa-b4f0-ef61f58307f2 | -13.3439 | -51.3187 | 2026-09-26 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| cb356f9c-6cdc-3328-a538-5b81522bc2a8 | 1.6382 | -55.9624 | 2026-09-26 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| cb40eb2b-82bc-3d75-be6e-7034ec2a0a8a | -13.3824 | -51.3138 | 2026-09-26 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c8cb8e62-9604-3852-9e9f-f03f13590e25 | 2.1083 | -50.8375 | 2026-09-26 15:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 4c19d28e-d82a-331d-b809-20444d5614ff | -13.2057 | -51.5703 | 2026-09-26 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e4525637-c6b6-3a15-82ea-557e31cd49c3 | -11.7697 | -50.6543 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3910d9b9-ebea-3f54-89dd-7e713809e24d | -12.0642 | -50.0617 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| abd972f3-9e8f-3bb7-9b64-1b8da833c926 | -12.2508 | -50.3189 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| b9b60201-d9b2-37e2-ab44-43beeddabffc | -12.9481 | -50.9195 | 2026-09-26 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 529d0a01-d7d7-3f75-ab26-39069d72db54 | 1.6015 | -56.0219 | 2026-09-26 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 674f33a7-3a8f-3e1e-b831-58ff9d1dcb96 | -12.1681 | -50.7362 | 2026-09-26 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 81bed312-c5f8-3c95-8f16-32930d53e6b9 | -13.2186 | -54.5182 | 2026-09-26 15:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 17768b36-ded1-3024-89e0-0a33dad35371 | -12.1869 | -50.7553 | 2026-09-26 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| d63ad181-a8dd-3e07-b705-1c1e13fa38bf | -12.9457 | -51.0695 | 2026-09-26 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 49e3b598-9903-3b39-9b2b-90d4becfa43e | -11.6508 | -50.9875 | 2026-09-26 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d62ad438-b64b-33bc-8b6b-6910001f88e9 | -12.1872 | -50.7339 | 2026-09-26 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 885821ef-63b7-3cec-bbd9-dcf8b4c20c5f | -13.2061 | -51.549 | 2026-09-26 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e9e9747c-e1a4-30d9-aa64-70bc962d7187 | 1.2978 | -50.8715 | 2026-09-26 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0778f26f-79d0-3532-8a32-40c7f751314c | -12.1115 | -50.7001 | 2026-09-26 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1bed4301-a5a0-3cfe-b168-812132a2c2b5 | 1.5099 | -56.0426 | 2026-09-26 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 30823153-ebe6-365f-8c1c-e4abdc3b21e9 | -11.6324 | -50.947 | 2026-09-26 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| dd511da4-18cf-3a25-84b7-7390531e7bdc | -11.751 | -50.6351 | 2026-09-26 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 46e355a3-8ddc-35ec-8fd4-ddd520075d6f | -1.2455 | -49.0407 | 2026-09-26 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 03e8a12b-85ef-334c-b76e-16a45f87043b | -11.6511 | -50.9662 | 2026-09-26 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 27a4cdd5-04be-325a-a5d9-13e717ee4c7a | -6.2401 | -41.6153 | 2026-09-26 15:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 149.6 |
| c51d1b71-d288-3bee-a44d-f887851f37e4 | 1.6565 | -55.9621 | 2026-09-26 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 51aca6d8-3239-3ed8-b696-199b10809e69 | -1.19 | -49.1266 | 2026-09-26 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| f8f275ef-76e7-3ed9-99d7-7959985f76a4 | -12.723 | -50.6475 | 2026-09-26 15:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 22b2a07c-da72-3492-af3e-3dd039895273 | -1.116 | -49.2338 | 2026-09-26 15:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 8a0440db-1735-3f22-81e2-abca0210ac04 | 1.5649 | -56.042 | 2026-09-26 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 97b26596-94cb-3427-ae5c-cb2c33266b6e | -11.6324 | -50.947 | 2026-09-26 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| e70793fc-abb6-3e33-a101-fd5cf7a7f844 | 1.6015 | -56.0415 | 2026-09-26 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| d729011c-7e07-382e-a81a-3e8ecb1b2189 | -11.7659 | -50.9107 | 2026-09-26 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| b9a88cb5-e787-3971-a9f3-1573fccbbf82 | 1.6198 | -56.0216 | 2026-09-26 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 46c088df-e995-3d87-a156-e163c4ccd7b5 | -11.0991 | -54.0285 | 2026-09-26 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 747ed289-d43a-3127-9312-411539efd6a1 | -12.8059 | -54.0255 | 2026-09-26 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b842f271-9360-386f-9e63-356c036e3355 | -11.8094 | -50.5428 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| d650c6d2-7a76-3865-8fa0-c03e2d19ad60 | 1.6018 | -55.8446 | 2026-09-26 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f6a3bdc9-9b2f-33a3-ab79-f6adc85aeaa2 | -10.9112 | -53.9635 | 2026-09-26 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2aa899d7-dba6-3bf2-bfa0-5c51377e6c38 | -13.2186 | -54.5182 | 2026-09-26 15:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 1700ca92-42d0-3062-8622-415a7a479016 | -12.2911 | -50.1849 | 2026-09-26 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| ec404b49-7630-3e0c-9313-5b72fbb1cbfa | -1.2086 | -49.0625 | 2026-09-26 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| c8606c8b-d8de-35d0-bc6b-b34478a17d6d | -1.1715 | -49.1268 | 2026-09-26 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 942117cb-fb55-308d-8a43-cf170d24d35e | -11.8024 | -51.013 | 2026-09-26 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 135.5 |
| a64b8ce4-b847-3d3f-a84d-8f39b3a5d4da | 1.62 | -55.9232 | 2026-09-26 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |


[Clique aqui para ver as próximas entradas](README39.md)

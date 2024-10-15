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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0461b2eb-f8bc-3b08-b73c-1a5c287dd090 | -13.9075 | -45.8355 | 2024-10-15 01:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 20424a49-3e81-3617-bffc-efedb4512fd4 | -13.9269 | -45.8323 | 2024-10-15 01:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 816cd59c-0479-32f6-9b5a-1a2cf3f3fbf1 | -11.9228 | -64.871101 | 2024-10-15 01:56:35 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 058c46e7-df99-3e68-8f8e-ab85517ce917 | -11.9244 | -64.878098 | 2024-10-15 01:56:35 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ed581abc-7ec1-30b8-bd7f-c28e484331f6 | -11.9445 | -65.012901 | 2024-10-15 01:56:35 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6c2abb83-ab7e-374f-abe0-a3de027f733c | -11.6919 | -65.217499 | 2024-10-15 01:56:40 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f9fb0ad4-8dd4-308f-b586-94aa5162018f | -11.6934 | -65.224503 | 2024-10-15 01:56:40 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d05d5615-5fb7-3053-9fab-4831cfe5d21b | -11.695 | -65.231499 | 2024-10-15 01:56:40 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b9494eab-ef2d-3094-a77e-365567e862a7 | -11.6821 | -65.219803 | 2024-10-15 01:56:40 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 16f5e2ee-fdf2-387b-8107-416b082e1821 | -11.6836 | -65.226799 | 2024-10-15 01:56:40 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f5af5ca7-f650-3d82-a6eb-0228def552be | -11.6852 | -65.233704 | 2024-10-15 01:56:40 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c2c275fc-69b7-32dc-98b9-018b1c8c6e3f | -10.8583 | -62.319099 | 2024-10-15 01:56:43 | METOP-C | TEIXEIRÓPOLIS | RONDÔNIA | Brasil | 1101559 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1284adc5-17ce-32d8-a7ed-b7f34d330814 | -10.8602 | -62.327 | 2024-10-15 01:56:43 | METOP-C | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 168204cb-dd9f-3624-8ff2-348ce2577250 | -10.624 | -61.420799 | 2024-10-15 01:56:43 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea840f7f-9556-312e-88a0-b2401b630f18 | -10.6261 | -61.429501 | 2024-10-15 01:56:43 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e6b8498-e319-3a2c-808e-ae85e14b0da7 | -10.4208 | -61.005001 | 2024-10-15 01:56:45 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67c1fa33-ffa8-3068-9e5c-92d0f3030658 | -10.423 | -61.014198 | 2024-10-15 01:56:45 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43be41ec-f286-375a-9548-656538ae0f0b | -10.4252 | -61.023399 | 2024-10-15 01:56:45 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12231664-c473-3312-a7ff-cb0a2fb62aaa | -10.4505 | -61.257301 | 2024-10-15 01:56:45 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87aadb2d-5b0b-3058-99ea-75e9c763f357 | -10.4407 | -61.259701 | 2024-10-15 01:56:45 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f69716f5-e559-3c4e-8173-af8efe51966a | -10.4429 | -61.2686 | 2024-10-15 01:56:45 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 801c9298-708b-3aff-94bd-40a56117ad1c | -17.8249 | -57.4425 | 2024-10-15 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 017efefa-98a7-3b3f-bbfe-e682f24d6df1 | -17.8253 | -57.4219 | 2024-10-15 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 14679ed0-b784-3125-840d-0a8a27e7bcb7 | -17.8447 | -57.4401 | 2024-10-15 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 1d08827b-6573-3149-ba2f-b5724f3dbb31 | -17.845 | -57.4195 | 2024-10-15 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 288f046c-4a5c-30c1-b875-5bfa6fbed057 | -17.8644 | -57.4377 | 2024-10-15 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 9ee086b3-b878-375a-b6c9-b2fdc1a0ac26 | -10.3682 | -61.172501 | 2024-10-15 01:56:46 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9120199e-5695-3ce9-8f85-e6ddc10d51d4 | -10.3703 | -61.181599 | 2024-10-15 01:56:46 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37c656bc-4ee2-3120-b00e-30d35863b66b | -10.3725 | -61.190601 | 2024-10-15 01:56:46 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2100198-53b2-3c2b-8b8a-a776a62021e9 | -10.3584 | -61.1749 | 2024-10-15 01:56:46 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 545f3b2e-f3f4-34e9-9c54-16cc0fd939b3 | -10.3605 | -61.183998 | 2024-10-15 01:56:46 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 200ea39f-47b1-3217-ad2c-556593bdee12 | -10.3627 | -61.193001 | 2024-10-15 01:56:46 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4e8946b-51d2-3ff6-8212-fecbdb9fdf26 | -10.0102 | -62.096401 | 2024-10-15 01:56:55 | METOP-C | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d5ca41c5-65ef-3b3d-b9d7-26a75fdf2451 | -10.0004 | -62.098801 | 2024-10-15 01:56:56 | METOP-C | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 59e134ab-c4e6-3355-acf2-047c98b1f2ee | -10.95 | -68.240196 | 2024-10-15 01:57:03 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 04352957-3a88-3a76-88d2-59e0e32d6ad9 | -10.9251 | -68.362099 | 2024-10-15 01:57:04 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b535b1b7-46cb-3e77-a1a0-6048d862ba10 | -10.7893 | -68.778503 | 2024-10-15 01:57:07 | METOP-C | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 405d2134-07bb-3a7e-b5e6-70970904caf0 | -10.7913 | -68.787498 | 2024-10-15 01:57:07 | METOP-C | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1d43da68-b7be-3f61-8f44-943b74b08656 | -9.4402 | -64.563301 | 2024-10-15 01:57:14 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 916f9b6d-c421-33ef-83f0-9dbbfc6c03ee | -9.4418 | -64.570297 | 2024-10-15 01:57:14 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| afaf6626-ad17-3cc3-9d27-c3db013c0f58 | -8.0546 | -61.2584 | 2024-10-15 01:57:24 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12adb60c-4dda-3414-a217-fa9fd48b817a | -8.5968 | -64.216797 | 2024-10-15 01:57:26 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9836770f-57bb-3f97-9a54-ba2e384f4e79 | -10.95495 | -68.25085 | 2024-10-15 01:58:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 83499cdf-0634-3942-8c88-d31b0dfc78f6 | -9.21469 | -59.77122 | 2024-10-15 01:58:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1572cb93-b359-3b27-b415-bbca7f5e9970 | -9.21283 | -59.75882 | 2024-10-15 01:58:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| afdb75d5-2e58-37e1-8a51-da16547ad239 | -9.15854 | -62.41761 | 2024-10-15 01:58:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10906041-a9fd-3cb7-8d33-b7aa5ca59c2e | -9.11663 | -62.64382 | 2024-10-15 01:58:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07fec002-ca62-3d10-9141-049e74d79c8e | -9.08959 | -63.43066 | 2024-10-15 01:58:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 001b19b1-fe8b-3f91-9ef5-136756b88115 | -9.01844 | -64.51447 | 2024-10-15 01:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e4b9ac7e-af90-3281-a543-e3672ab2fa87 | -9.01434 | -62.5724 | 2024-10-15 01:58:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b0d11e53-7c2c-3a0b-aa48-80dc1131d1b4 | -8.99393 | -63.40508 | 2024-10-15 01:58:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4b9ddae2-276f-39fc-b116-1a16ae20ab94 | -8.99269 | -63.39619 | 2024-10-15 01:58:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 595a5e2b-571c-38c6-af42-171246bceeb2 | -8.73209 | -64.24036 | 2024-10-15 01:58:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7912ecd9-cb9d-3241-86ae-835c3bd8d8d5 | -8.60014 | -64.2254 | 2024-10-15 01:58:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e993990-0b84-3cdd-9aed-e4a12becba70 | -8.5989 | -64.21643 | 2024-10-15 01:58:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c07b6f07-38cc-3c40-a6c7-7d12fa70737e | -8.55637 | -64.03998 | 2024-10-15 01:58:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8b964924-9b73-3e73-9a88-d8b5ba5bda93 | -7.9464 | -63.62954 | 2024-10-15 01:58:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 973ca75d-993f-3efc-b145-1828e4ed3889 | -6.64764 | -60.00314 | 2024-10-15 01:58:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 33f530e1-847d-3303-995e-6fda9381ea50 | -6.6371 | -60.00476 | 2024-10-15 01:58:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0b9cd776-3c21-350f-977b-d89e138c49c7 | -10.93413 | -68.36729 | 2024-10-15 01:58:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 12.9 |
| fe093fa5-42a7-3179-9ec5-caed6909e2df | -10.79078 | -68.78867 | 2024-10-15 01:58:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6c1cd2ec-ce99-3e8a-b4b7-1ec64a189840 | -10.38681 | -61.27092 | 2024-10-15 01:58:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e7de0dab-2229-30c1-96fd-621ce41885e1 | -10.37674 | -61.20097 | 2024-10-15 01:58:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 591b173a-7a9a-39ec-ad2c-509ba2afcf44 | -10.3753 | -61.19099 | 2024-10-15 01:58:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| e1970cb6-0cb0-3699-bd6e-474a2b37fa9f | -10.37386 | -61.18102 | 2024-10-15 01:58:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| c467845a-89b1-38e9-9dd5-40477a0c92bc | -10.36746 | -61.20239 | 2024-10-15 01:58:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 09cd6f48-86aa-3804-9c4a-530d1659e9ec | -10.36602 | -61.19244 | 2024-10-15 01:58:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| c4832bf0-40e7-3d45-b8d6-966b3ec62005 | -10.36457 | -61.18246 | 2024-10-15 01:58:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| e50ce60b-bc34-361d-b7b4-4cf8e884feda | -10.35673 | -61.19386 | 2024-10-15 01:58:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1cf3d484-a33c-38d5-94d7-7ffc521a12fc | -10.33975 | -61.6504 | 2024-10-15 01:58:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1165d8b9-40ed-39df-93b5-8c275a2665f2 | -10.00884 | -62.10794 | 2024-10-15 01:58:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 23.3 |
| d36e8266-b956-314e-a56a-d5839aee41e0 | -10.00751 | -62.09865 | 2024-10-15 01:58:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1651fe6a-9322-3421-a26c-4a639353b52d | 1.0016 | -52.2164 | 2024-10-15 02:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fae08b58-3335-3830-b81b-b79016599035 | -3.1099 | -54.2263 | 2024-10-15 02:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5bd6eef1-6b86-3ae8-8778-d93c33bdb52a | -3.1282 | -54.2459 | 2024-10-15 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d636df33-96d8-3f65-abc9-b2b7f7f90627 | -3.1283 | -54.2259 | 2024-10-15 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 98ad3b1b-e809-3d0c-b976-68a00d18e465 | -6.5503 | -48.2625 | 2024-10-15 02:05:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 1c786126-8f25-3232-8e41-62c8003c50d5 | -6.5689 | -48.2612 | 2024-10-15 02:05:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 98.1 |
| f7a66150-5da3-374d-bac0-784c00f6e3dc | -6.5691 | -48.2395 | 2024-10-15 02:05:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 129.6 |
| fda4bacc-71a6-3851-a4c9-3a221c6021b2 | -6.5878 | -48.2381 | 2024-10-15 02:05:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 79c22a83-1da6-358b-b45f-b4f0d1608140 | -10.0816 | -44.2133 | 2024-10-15 02:06:02 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 3fd97241-2a9b-3cfb-9096-64f01787d7a1 | -10.0415 | -54.3442 | 2024-10-15 02:06:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6ad09523-9f82-3caf-b4a2-7154e73d99d5 | -10.4918 | -42.433 | 2024-10-15 02:06:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 962509d2-7ef8-3ccf-b300-498b785c3610 | -10.3711 | -61.1935 | 2024-10-15 02:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 315c7254-f6fe-3aaf-9cb8-dcca81166f2f | -10.3713 | -61.1743 | 2024-10-15 02:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 05cca766-b80f-3457-a425-5f1389080fc1 | -10.3898 | -61.1925 | 2024-10-15 02:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 537a724f-02f9-34ca-8c39-3ec8810891c6 | -10.841 | -49.2539 | 2024-10-15 02:06:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6b300510-98e0-31a0-87ca-071aa1affd55 | -11.6915 | -65.2432 | 2024-10-15 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| ca2c7782-b727-3596-926a-322a899d156f | -11.6917 | -65.2243 | 2024-10-15 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 609c3ec2-a66a-3572-8c52-4cef39e6b878 | -12.099 | -50.2728 | 2024-10-15 02:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 74a607b1-d3ed-3e41-b2ef-3d6fb7b43507 | -12.3997 | -53.1147 | 2024-10-15 02:06:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2d83f1f0-a683-3ec6-898d-36c43e3bdc14 | -12.3982 | -63.7284 | 2024-10-15 02:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 89b6503b-957f-34dc-92e6-003978329a6b | -12.3983 | -63.7093 | 2024-10-15 02:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 50a98e75-d555-31a2-9292-f1645b37cfe2 | -12.4603 | -63.0169 | 2024-10-15 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 46ede8f2-45cd-30b2-bf4e-51507efbd79d | -12.515 | -63.263 | 2024-10-15 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| e7a743ac-6698-3118-9e9d-da5b872ee44c | -12.9728 | -62.7951 | 2024-10-15 02:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ad0c9947-1e1c-3c4e-9287-1c8c40705259 | -13.1285 | -62.3227 | 2024-10-15 02:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9b0deed3-7346-33e3-89d9-ec1baf331f6a | -13.1287 | -62.3034 | 2024-10-15 02:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8c3b89ce-eea7-3921-828d-7e9625c93dc1 | -13.1473 | -62.3408 | 2024-10-15 02:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 51d9239f-b327-378e-a83b-e2df449c7eba | -13.1475 | -62.3215 | 2024-10-15 02:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 111.2 |


[Clique aqui para ver as próximas entradas](README20.md)

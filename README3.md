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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 017ccaa0-aec6-3185-a869-8f09b8ed306b | -6.3417 | -55.73444 | 2026-08-05 00:54:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 1fe5431c-050a-38cf-8c85-e38c65c41a8f | -6.72506 | -58.93631 | 2026-08-05 00:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 28eb4cdb-d534-336c-9671-522b2fd505f2 | -6.54634 | -55.16217 | 2026-08-05 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 4626d58a-e319-349d-9e83-2462a1a712bb | -6.55907 | -55.16024 | 2026-08-05 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 3c57ee65-148e-3fdf-95a0-f67368a5455d | -5.37056 | -55.88948 | 2026-08-05 00:54:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0e7aafad-baa1-30af-836d-f42268ce20af | -6.5718 | -55.15828 | 2026-08-05 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 03077f1e-58bc-3c92-b002-f9b476d526e6 | -6.53358 | -55.16393 | 2026-08-05 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 1136d7a9-f75c-3e58-bfd8-afa90f10066e | -6.72008 | -58.93275 | 2026-08-05 00:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 09a5e73b-c756-37a9-908f-bd06a5cce3a8 | -6.55607 | -55.14079 | 2026-08-05 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 08179043-9e7f-35dc-849a-d8edc620d878 | -6.33302 | -55.73005 | 2026-08-05 00:54:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b5cada75-add6-316f-87f6-7cbbff9ad0ac | -6.54938 | -55.18173 | 2026-08-05 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| c555aa89-1ff8-3bc2-af38-726160752d51 | -6.54658 | -55.16874 | 2026-08-05 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 39357f91-835b-3555-ae10-dba487f9fecd | -6.64729 | -56.41877 | 2026-08-05 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3ef3aa60-faa9-3076-8177-1f56ca269b8c | -6.71348 | -58.95509 | 2026-08-05 00:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5b9c63ff-c8b7-3702-bf42-2605eca17bd8 | -6.53091 | -55.15084 | 2026-08-05 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 44f53101-67c2-3aa2-9c7c-f0a9da6da243 | -3.1936 | -52.88655 | 2026-08-05 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 7b069716-30f5-3fd8-81d3-4f41f4c070a7 | -3.18486 | -52.88284 | 2026-08-05 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 8bf7ae6a-1709-3147-84eb-7e51f98b70d9 | -6.53384 | -55.17061 | 2026-08-05 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| bbfb7d96-9385-32fc-8581-b96b51d05a1d | 3.48103 | -61.31599 | 2026-08-05 00:56:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a1212100-d470-333c-b162-3c1a12618dc9 | -14.1779 | -54.4124 | 2026-08-05 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e09335e7-c24d-3123-9ac6-522a6b58d08b | -9.4761 | -40.3862 | 2026-08-05 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.9 |
| da835832-a04e-39e4-a4ad-d137abe872fa | -12.5754 | -46.9329 | 2026-08-05 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5debb517-f57c-357a-b425-f65b993d070a | -9.4952 | -40.3834 | 2026-08-05 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.1 |
| a38e5826-a3d2-3c36-b87e-c2a40364fa8a | -9.4765 | -40.3613 | 2026-08-05 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.8 |
| d9ffa89d-77a8-33ef-ae1b-d71e4c7e9bc9 | -14.1587 | -54.4146 | 2026-08-05 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 7ae5cccf-43ec-3b46-aafa-4684854795b6 | -9.4956 | -40.3586 | 2026-08-05 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.0 |
| d0fcc764-2cc8-3c92-8cb9-fdcd5ec2cf62 | -14.1783 | -54.3916 | 2026-08-05 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d28a6bb2-eb4a-3e41-b7b2-b7e29fd02c7e | -12.5947 | -46.9301 | 2026-08-05 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 207.5 |
| d44ff451-3183-366c-8c60-06aebe55cf73 | -14.159 | -54.3938 | 2026-08-05 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 2c68ac7c-fff8-3033-86cd-7c4276f59d12 | -12.5942 | -46.9527 | 2026-08-05 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 5dfe4bda-9677-3296-bfac-d7211eaec45d | -12.575 | -46.9555 | 2026-08-05 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| cbefc770-cae0-3038-a2a8-cf63fbf0f946 | -6.5514 | -55.1569 | 2026-08-05 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 9c4c4c4f-28a9-331a-bbd9-09d572d2c986 | -12.4386 | -50.5109 | 2026-08-05 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 47c173f3-3ae0-3e28-9d2e-d8eadf3c45c2 | -12.5942 | -46.9527 | 2026-08-05 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 6a241a52-f635-33e1-8db5-178797b3da0f | -12.4386 | -50.5109 | 2026-08-05 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 66a47f3f-0d37-3cae-b111-f8e25e273dda | -6.8904 | -42.4152 | 2026-08-05 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 3b5b95a6-795d-3ebf-b156-f517ec02f955 | -12.575 | -46.9555 | 2026-08-05 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 8bc4fd1b-78ec-3592-9c27-a61f8400c2fb | -12.5754 | -46.9329 | 2026-08-05 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| e62111f2-f730-3449-8aa1-c5394823bc48 | -12.5947 | -46.9301 | 2026-08-05 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 69655cb8-cf4a-3bdc-ba0e-ea3e22e5d531 | -15.0755 | -49.493 | 2026-08-05 01:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| bb2db087-f9da-3548-83d1-0c962fa44079 | -15.095 | -49.49 | 2026-08-05 01:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 03018d8b-7644-3d9c-9e23-2fb45d411ff7 | -6.5514 | -55.1569 | 2026-08-05 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 51aab6a5-3c0b-342a-80bb-b80578ba0868 | -11.1812 | -54.908298 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e984db75-ccc1-34c9-acd1-db4053e1de4f | -12.4425 | -50.525902 | 2026-08-05 01:13:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b72c73d-7df7-3f97-a444-ff5b761aad9f | -14.1824 | -54.4062 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3564aab4-41c3-386c-bb4c-90cdfc3fc02a | -11.1845 | -54.9226 | 2026-08-05 01:13:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eee4f509-fbc4-3fe4-bfb1-502cb3032110 | -6.5753 | -55.1628 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ede0d889-80f8-321a-afc7-e5056c6cdac2 | -6.5476 | -55.176998 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c16de99d-31bc-397d-8517-fee06cec2d66 | -12.4398 | -50.514999 | 2026-08-05 01:13:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b59127b-db78-3649-9849-77e8bcd56479 | -11.1942 | -54.875099 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f58b6391-76aa-3fb7-8248-a2c109bd5757 | -6.577 | -55.1702 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49e74fcc-0cbf-36f2-9b53-914d08e1199f | -6.5672 | -55.172501 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39690c85-381f-3ef9-9ef0-338531a35944 | -6.5603 | -55.142899 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75ff4fe2-fedd-3682-88c9-69740dc319eb | -6.5736 | -55.155399 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 986bd697-809f-3927-8d2e-c63c085b1dd1 | -13.2532 | -54.2696 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35deee79-b319-3640-9cc8-872ad5deeecb | -14.1357 | -55.245201 | 2026-08-05 01:13:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58bc1266-f1b9-3c19-b8ee-8da1fafda500 | -3.1874 | -52.8895 | 2026-08-05 01:13:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec8f3658-77a2-3f01-b488-79f59548497b | -11.1731 | -54.917702 | 2026-08-05 01:13:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ead63e72-90a8-3ff3-abe9-87de80a15ddf | -15.0847 | -49.494301 | 2026-08-05 01:13:00 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9302fe79-633f-3a57-b8e2-9d4eb5b5feab | -14.1726 | -54.408501 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60a82762-ef56-3c06-bf78-4094a11f4dc9 | -6.3368 | -55.737801 | 2026-08-05 01:13:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a04d08eb-2681-3dac-a615-ddb14d6f7d0b | -6.5424 | -55.1548 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc0e0e41-c6fb-3521-860f-10d099f8e2a8 | -11.2055 | -54.834801 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 370b5509-474f-37fe-afc7-77f4e497bba8 | -11.2023 | -54.8657 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb678e0-cf32-329f-8ffe-f1ae43652bb7 | -11.1648 | -54.881901 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 926bcf5b-2865-392c-993b-167ba8ede95c | -11.2154 | -54.922798 | 2026-08-05 01:13:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cde29d8a-3290-38ef-b573-0cc390f7e50e | -11.191 | -54.905998 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7d6eb6-e942-3937-8c12-0e9d93d0138d | -6.5442 | -55.162201 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 415c3490-870e-3149-8a21-0dc9e2396ba7 | -11.1698 | -54.9034 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee21d53b-0973-375c-9d70-57b98d2a6ee5 | -11.1665 | -54.889099 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c666965-2d5f-327d-9db2-28723d2d7e1c | -4.3762 | -47.782902 | 2026-08-05 01:13:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d26dbe39-f7e4-3b05-9ed0-a9706519e5c0 | -6.5344 | -55.164398 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56f1c254-33f6-35aa-ab14-bdfcb4c931b1 | -11.2006 | -54.858501 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4866a1e3-4481-3a0b-bf9a-0fadaccd98a1 | -6.422 | -55.7934 | 2026-08-05 01:13:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae4c4f4a-c6cd-3fd1-b4c7-e349fdcd2d23 | -11.2008 | -54.903702 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4915fdb9-2ee3-352a-b148-8c55af38e34c | -12.4496 | -50.512501 | 2026-08-05 01:13:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae624518-015a-3643-ae47-81b36b1e42ee | -11.173 | -54.872601 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6ae4fad-1094-33bd-af74-0b9282db78ce | -14.2004 | -54.439602 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40019692-9349-33ba-93c5-a29ac0fb7bb2 | -6.5459 | -55.169601 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbbdf63a-fad5-387f-b285-ef8c026a6cf0 | -11.1632 | -54.874802 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa35f5e-083e-36f7-9a13-f9b48cf25ba6 | -11.9156 | -55.9128 | 2026-08-05 01:13:00 | METOP-C | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf9eeff4-cdec-3802-add1-5a9b6322f184 | -15.0818 | -49.482601 | 2026-08-05 01:13:00 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9fa4b63d-9e02-300e-b031-f575ba62d36e | -6.562 | -55.150299 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d803ed3-ac23-33de-aaf3-9f6be1bd8c66 | -6.7237 | -58.9347 | 2026-08-05 01:13:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63e0ce73-2f96-35f6-b736-40a22acce132 | -3.1972 | -52.887299 | 2026-08-05 01:13:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf3ba1a-e9bf-3f49-8a01-3d7a52142120 | -11.1959 | -54.927399 | 2026-08-05 01:13:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bcc6f65a-fa27-3940-af35-b03b34ee8928 | -11.1844 | -54.877399 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c140e2eb-a7a8-3d0d-a339-b47aae7aa0d3 | -12.4523 | -50.523499 | 2026-08-05 01:13:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a387b053-e12d-35d1-89ba-f8fa487ba0c2 | -14.1629 | -54.410801 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b7676d1-6b4a-351f-acc9-82fbf650856e | -11.1861 | -54.884602 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d3772e8-e7c4-37df-a7dd-932973311f06 | -11.1926 | -54.868 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56585ecc-2de9-3d45-88f5-c6d217127493 | -15.0944 | -49.491798 | 2026-08-05 01:13:00 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b481c6b-58a3-3ebc-9bb3-66988f200f80 | -6.7171 | -58.9515 | 2026-08-05 01:13:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4e33115-b58c-37b8-96de-5d1d75f389f3 | -6.4236 | -55.800598 | 2026-08-05 01:13:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23fab84a-d091-3f63-ae19-f4292cbaaa4d | -5.3809 | -55.8871 | 2026-08-05 01:13:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 532672f0-31b3-3c64-985c-acf311cd0030 | -6.5841 | -56.543999 | 2026-08-05 01:13:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b557b27-c8b0-393a-9748-9d113d6a3613 | -11.2041 | -54.917999 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61a366ef-6ffb-3474-bd23-1b5f231e32ac | -11.2105 | -54.901402 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8179eb5-f89b-3558-b6ac-6ae94954a471 | -6.5696 | -56.525501 | 2026-08-05 01:13:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7dc9f53-8dd5-30ce-851c-4f6ab53ef868 | -11.2025 | -54.9109 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)

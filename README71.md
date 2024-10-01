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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8b09a4b-f1a7-31b0-a0ad-04c907f931de | -8.66051 | -49.42554 | 2024-10-01 04:12:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e459c52e-4411-3e46-b44c-11e44f4a4975 | -8.65981 | -49.42954 | 2024-10-01 04:12:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31dad101-2b65-3be9-a816-3e1ed21ededf | -8.55206 | -49.60529 | 2024-10-01 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 055cf2f5-3b19-3c5d-878d-225e8b542957 | -8.55136 | -49.60938 | 2024-10-01 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1891cd5-3714-3fe5-8547-3cd0e7ef4c41 | -8.16143 | -49.45596 | 2024-10-01 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d429effe-e273-35ee-ad85-c126c41edbaa | -8.16074 | -49.46006 | 2024-10-01 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ada6ff90-7873-3c7b-9e90-217e84953c1a | -8.15715 | -49.45512 | 2024-10-01 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f4993e3-3773-3f75-9f31-b6ed0400d2b7 | -8.15644 | -49.45929 | 2024-10-01 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 336946dd-a058-3ba0-a8f0-30e9137f6f95 | -8.15574 | -49.46346 | 2024-10-01 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2df4cce-79ce-3338-8288-98fb9a693102 | -9.58793 | -50.19919 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e7e38dd-ffac-3a09-b960-460f620b66ee | -9.58789 | -50.12306 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38debec1-e0f5-3a47-9f03-40358222abe8 | -9.58352 | -50.19839 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66dd15cb-6f75-3a23-9e8d-4529056becdf | -9.58351 | -50.12225 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e394ca28-d7ad-391a-978e-840c705032ec | -9.58342 | -50.12419 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd2d8160-9a4e-3b96-842d-b1b0a0c429c2 | -9.58284 | -48.92206 | 2024-10-01 04:12:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2b1f6fa-59f8-3a30-8ace-051696223265 | -9.57912 | -50.12145 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ba4f401-4873-3e73-951b-1ba2ea8451c0 | -9.57903 | -50.12337 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21a5db36-5e37-3fbd-bca5-d0555c736f0e | -9.57599 | -50.21507 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5777f14-021b-30ac-9a41-b187e51e5932 | -9.57473 | -50.12067 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0df135bb-6ad8-35f2-8ecb-9617697da930 | -9.57464 | -50.12259 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d16ec3fb-0fa9-3c2d-8cba-6bce583984ae | -9.57079 | -50.21865 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62dbb966-7b0a-3467-8069-f92156333b0c | -9.57034 | -50.11989 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edc469f7-14fa-335e-9ac4-036f3101be69 | -9.57025 | -50.1218 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1bc82c5-bce1-33f1-baef-c5c48547908e | -9.54566 | -50.21162 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b2c71f5-5ff1-32f3-b347-e832d505b6e6 | -3.93596 | -49.9958 | 2024-10-01 04:12:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05247a57-db65-3327-99de-e93dfd7e732f | -9.17115 | -51.31215 | 2024-10-01 04:12:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bdc4e95-2dd6-3cda-8b0d-62cb155ffe71 | -9.66028 | -50.92636 | 2024-10-01 04:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08221409-cb78-3ff9-9468-d160e34e52c1 | -12.99502 | -51.25513 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 653a6d94-cd8a-3841-9bc2-a0e12a74aa28 | -12.99475 | -51.2316 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86afef92-92ce-30a5-a45d-4dee2bf44295 | -12.99445 | -51.2833 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2344f717-cc21-367c-b2f0-904a242f97e8 | -12.99419 | -51.25968 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26c7c352-8677-38e9-b0b2-1df7368abe7b | -12.99392 | -51.23613 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| add0f6a4-0cd4-3154-b147-ed5200c42008 | -12.99335 | -51.26423 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| d2690fa8-a595-3a47-99d6-1d01ba10c85d | -12.99308 | -51.24067 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 145c5be0-945f-357b-93fb-22cf8ceecb0b | -12.99303 | -51.31615 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0b96fbe6-d8cb-3ea4-b486-8b62f7d9a6dc | -12.99251 | -51.26876 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| e43e929e-992a-350f-ad99-09917850bb21 | -12.99219 | -51.32074 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0a63e125-217e-3b20-b9da-d89313d29b7d | -12.99167 | -51.27332 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3d8cacf3-9837-3d24-946f-9779cb3f1e52 | -12.99114 | -51.22622 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e32a717-5188-3d42-b87a-5d02d42d3292 | -12.99083 | -51.27787 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 93881472-dbd7-352c-bd63-a81922b7a061 | -12.9903 | -51.23075 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c95b3f6b-9657-359a-9fa2-bfb6c717d87c | -12.9899 | -51.35841 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee6b72cf-5709-34e8-bbca-f44404601168 | -12.98946 | -51.23528 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 157570d6-4d07-3a24-a1c6-a37fc88a126e | -12.98914 | -51.28699 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 137c84de-d842-3171-96bd-0a098d677b76 | -12.98888 | -51.26336 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 389d25c0-52fa-3e62-979e-11b507ed3058 | -12.98862 | -51.2398 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b322c418-7618-3dfa-af87-63eb87da3dd0 | -13.31474 | -51.33927 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06b137d1-8a55-3bc5-b40b-d0e0b10bea15 | -13.31029 | -51.33838 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ade36eb-8b6d-3318-ba42-2a0c936ae014 | -13.03582 | -51.31027 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| d7a638dd-64bf-3b98-b15a-a90358f8bf06 | -13.02937 | -51.2948 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 988bb447-cd53-3203-b149-3116dc8a2e88 | -13.02437 | -51.32226 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 84e2b201-180f-3ac4-8470-5e6ebee1c1df | -13.02407 | -51.2985 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 37a79565-e8a7-3f0f-b0fe-336b7cf7fa78 | -13.02323 | -51.30308 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ea842c9b-c5cc-3828-9921-40ef452e9f7f | -13.0224 | -51.30765 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9cb240f1-e507-3454-8cf0-127e5c9ad98c | -13.02157 | -51.31223 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f6c2b258-68d8-38ae-b87c-08275835ac1c | -13.02073 | -51.31681 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8818283d-9a41-392d-8065-79dc0c1086e1 | -13.0199 | -51.32138 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6ebdc468-12df-3a80-8511-7d8e10ac30cd | -13.01959 | -51.29764 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| a8d805a6-7a79-3185-9808-b8a4222e72b3 | -13.01906 | -51.32597 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 39b1f21d-7588-36a6-8d25-898dfb1a4468 | -13.01876 | -51.3022 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| e8f8415a-42f5-3037-b3b2-f2f4a363d74f | -13.01823 | -51.33057 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d77cc09d-dc9c-3364-94e1-df9b190082b5 | -13.01793 | -51.30677 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ae0cd2c0-8926-34b8-a705-4955e3289e2b | -13.01709 | -51.31136 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9e5c0497-4100-325e-973f-790a3016d673 | -13.01542 | -51.32051 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4fb53fb9-14b0-382a-86a4-1bc605ca441a | -13.01375 | -51.32969 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c675ff72-8893-3c93-9f80-09c53e4c1b99 | -13.01345 | -51.3059 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 18de4600-6489-3a3e-a22d-8832165c2990 | -13.01178 | -51.31506 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1435797a-635c-3dad-bd94-a5a56ec512b9 | -13.01094 | -51.31964 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a659b5f1-0d3d-3126-9bb9-147b1607542a | -13.00814 | -51.30961 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c03ce00-8576-37fa-8b57-d30b47c7524c | -13.00646 | -51.31877 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 0ddb336e-cd9f-374f-8d6d-7cd155148269 | -13.00506 | -51.35181 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eee18a9-b866-38d7-bc9b-ceaa925b938b | -12.99751 | -51.31703 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 38c36f36-ecaf-316c-b535-6b4a581e0126 | -12.99524 | -51.35467 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1e662d8d-9c04-3925-9515-0a3f196f8ca6 | -12.99134 | -51.32533 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0999d736-1119-3f6c-9b10-5427d8a46fdd | -12.98686 | -51.32446 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b5f14ab-9509-3af7-a056-6ac0bc10147f | -12.98069 | -51.33276 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36a0da55-73d8-3ee4-a5c7-454c19880649 | -12.97813 | -51.34657 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b79f9974-926d-3304-ac7c-7cb359105ec7 | -12.9745 | -51.34109 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b778b18-bfce-3a8f-8885-3f0b9e34fcd7 | -12.97149 | -51.30723 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7886e78b-291f-3e9f-9eaf-905bd3b00703 | -12.96038 | -51.367 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4b173ddc-2f91-3d3d-a096-f6fb71d7308f | -12.96018 | -51.34307 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09e63496-0e2a-344b-85cd-fc0497858e89 | -12.95932 | -51.34768 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df4c2d34-6050-34fc-a8f5-40c1c0c37bce | -12.95761 | -51.3569 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bab8a73d-3184-381a-afb1-4023d2e012eb | -12.9099 | -51.30297 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1990057-374e-3298-bd2f-acec4f6abc3d | -12.90542 | -51.30212 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7985b8b0-d236-3c97-b130-5223bbf4cb7a | -12.90458 | -51.3067 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4337407b-9af9-38a4-a3cf-2ffaa1dbb5f9 | -12.88581 | -51.3078 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d98336b-9242-3aec-8b15-06b4b99d07e4 | -14.64773 | -52.8639 | 2024-10-01 04:14:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e04e2189-2440-3546-84ed-f898fc222e10 | -13.79417 | -52.70391 | 2024-10-01 04:14:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 88bd0279-ff26-3878-87bb-b6d7098df7e1 | -13.78863 | -52.42332 | 2024-10-01 04:14:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| debba7b3-b6f3-32a8-a2c0-8de2a841cf40 | -13.78284 | -52.42789 | 2024-10-01 04:14:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06eb65ae-1d47-3e8d-9145-a5c15b6359a8 | -13.77809 | -52.42691 | 2024-10-01 04:14:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5ef64b4-c4b0-34a6-a6d2-28d2a46fc81d | -13.77436 | -52.42056 | 2024-10-01 04:14:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3ee1062-32ed-335f-a4c5-eae004a1cacf | -13.76856 | -52.42513 | 2024-10-01 04:14:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 259bad38-9707-3be3-b1dc-71834f912e94 | -16.62798 | -52.58018 | 2024-10-01 04:14:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92fcaa9a-5cf6-345c-8cf4-c3c6e9defd6c | -16.62743 | -52.58282 | 2024-10-01 04:14:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 063ae109-84c7-34c1-b46f-454ebec5d646 | -16.62705 | -52.58509 | 2024-10-01 04:14:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a46be52a-3287-33bf-9d94-7ede698889c0 | -16.62646 | -52.58775 | 2024-10-01 04:14:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e6ad9d2-beb8-31c0-82c3-47a771db7095 | -16.62611 | -52.59008 | 2024-10-01 04:14:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63892b50-be84-3311-8bc0-34b25d04bf2c | -16.62339 | -52.5794 | 2024-10-01 04:14:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README72.md)

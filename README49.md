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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e490166a-7292-30bd-b5cd-d5373ae8a6d8 | -20.50768 | -48.12767 | 2024-10-07 03:40:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 11ddfed8-1653-3c66-bb78-dce674cacdc9 | -20.50669 | -48.13203 | 2024-10-07 03:40:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4c7eaf02-0612-3f89-af1d-853ed12d4be1 | -20.47432 | -47.66163 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f78f0c6c-522a-30fb-ab84-f0883702581a | -20.47334 | -47.66598 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7279dd3f-b08f-36dd-b45f-b5554d3c3631 | -20.47237 | -47.6703 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b8e174e2-1110-3c4d-a13c-e09fca3fa486 | -20.4714 | -47.67462 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fe0f4ba6-7d21-3fce-b568-7dbda1b5f173 | -20.46964 | -47.65591 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 783a105a-b3b5-36a4-9240-bbd509f5194c | -20.46868 | -47.66015 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b0613b0-d55e-3bc5-9320-af4c3b68b61b | -20.46773 | -47.66437 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5ebab580-1ad0-3834-ac29-c87b2447a46f | -20.46678 | -47.66858 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7cabb745-dda6-3179-bbe2-f9aeb272a9e1 | -20.46582 | -47.67284 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 511b8ee5-6a9a-35ba-95b3-e2559fc3432b | -20.46485 | -47.67714 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| edd39aa1-6c3d-3f36-b402-39171ff7b4bc | -20.46404 | -47.65422 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef959123-e4b8-3380-b803-35415fdd2ce8 | -20.46389 | -47.68139 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 20eae0c0-ecca-3d59-8ba5-02b157245931 | -20.46119 | -47.66684 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd409ffd-4824-3af2-8030-91c765a067bf | -20.46022 | -47.67113 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 11d302cc-1f2e-32ba-8c55-36ec7fca6b54 | -20.45924 | -47.67549 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b0228887-236e-30d4-b636-3884b9938163 | -20.45826 | -47.6798 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6e29b3e0-0793-32d1-b9db-521fcf664d10 | -20.45732 | -47.68397 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ba924a9c-8c1a-3608-b257-cd5b79e4ae33 | -20.45545 | -47.69223 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f725132c-48fb-3e82-a266-337f681e7d66 | -20.45451 | -47.69641 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 9681f74f-dba1-3ed8-bca4-5a55573073f4 | -20.45357 | -47.70058 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 78fd0d00-21f0-37f3-b9d8-4a02d020e9e3 | -20.45357 | -47.67405 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0002112e-10aa-3d90-801f-9333afcd39c8 | -20.45262 | -47.70476 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 3a0f0378-d570-391c-a266-715e34f91bb1 | -20.45259 | -47.67838 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7e5bfd15-0e52-3e0e-b4bd-3d6344de2d6c | -20.45167 | -47.70898 | 2024-10-07 03:40:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| e2ada494-d4cb-3a18-b55a-0f97be53aea8 | -20.45164 | -47.68258 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2bb60f72-1a95-337d-bb58-ace758c10fd5 | -20.4507 | -47.68674 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3000ddc4-e12a-39be-bf56-df485507117b | -20.44974 | -47.69097 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 10568330-53f1-31ad-bfb0-e6bc9b2421ee | -20.44878 | -47.69523 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 75bbce15-0291-330f-8196-6a8ca6e9961c | -20.44784 | -47.69936 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 41.4 |
| d21cf1b9-c9f5-3abd-a0c0-f776a722f708 | -20.44692 | -47.70343 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 72a56feb-e708-3681-bcb8-f6cbeee124c0 | -20.44598 | -47.70757 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 16683a61-1159-3f66-9f45-ff2ba4e8c94e | -20.44503 | -47.71176 | 2024-10-07 03:40:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87c464bf-c520-3fad-b3ad-d7b21404f94e | -21.59716 | -47.71001 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 131adec1-3829-339a-af9e-cca3af9aa056 | -21.59708 | -47.95503 | 2024-10-07 03:40:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3f2a18ca-16f5-33c3-bdfa-0d2913a6c99f | -21.59354 | -47.93875 | 2024-10-07 03:40:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7292ebd-31a8-3d7a-a058-8424764a46ec | -21.59172 | -47.73436 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 34068b40-1d92-349d-a661-3b7f4565fdb3 | -21.5908 | -47.95113 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4f144ca-d397-3cae-a1a8-6ed22bc9674c | -21.58957 | -47.96179 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 432e6815-f249-36d5-8aa7-148fded46907 | -21.58897 | -47.95938 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b0248fbb-72ab-3daf-9c56-5d56c5496a27 | -21.58529 | -47.73687 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 08b33ff9-e73c-3458-98db-21728b45d8f6 | -21.58077 | -47.73077 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 203f2d79-1e04-3b1a-a872-2545e00904c6 | -21.57837 | -47.93268 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 13ce535d-31e8-3bb8-b2fd-54fa5f6e1c7a | -21.57689 | -47.74809 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3712911c-0e45-3788-a273-fb44d493bdde | -21.57179 | -47.7184 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de78d309-e8df-39cb-adf8-01e1102ad57c | -21.57132 | -47.74672 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1f3f72f9-8021-3004-8a55-a82c7b4d5173 | -21.57086 | -47.72255 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62e89920-72fa-3a56-9760-62f324330e44 | -21.56878 | -47.73182 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cfbf49bf-f34b-3529-8351-017a19eeaa47 | -21.56515 | -47.72181 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 145f5134-dcaf-3a1c-8110-52ce347dc207 | -21.5648 | -47.7495 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0032af9-53b2-3323-9bc0-a1bfb3f03aa0 | -21.56415 | -47.72626 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d845f2ff-2c40-3159-9eda-ead6ff8adbb0 | -21.56389 | -47.75356 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ee4f7dc-ab04-3e3c-9d01-87e1d8ff756d | -21.5612 | -47.73939 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 492bb68d-4817-3199-8eec-24ad9f288291 | -21.55569 | -47.73772 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6605e99a-d3a4-3db7-b9b1-32ed12ba6774 | -21.40518 | -47.80941 | 2024-10-07 03:40:00 | NPP-375D | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa6f0f5e-fc7b-3e7b-bd28-78655e9e9ca3 | -21.32226 | -47.61175 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 395e71da-773f-364b-91e2-a35f8a8505f9 | -21.31787 | -47.60503 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| edb3fbc3-8e28-33de-bae7-79f87b32edbb | -21.60536 | -47.72589 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5940eae5-94ec-38a9-ad65-1326047256bd | -21.60253 | -47.71223 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d896bd47-a298-3ab2-a039-049f689365fa | -21.60167 | -47.71612 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9206eff8-7d97-34c0-ba27-be2209adcec0 | -21.59996 | -47.72379 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f08086c7-5029-3418-9964-93b09fc4c60f | -21.59548 | -47.71751 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d312376-0408-3d41-819b-fda37aba8e0c | -21.59428 | -47.9412 | 2024-10-07 03:40:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25117b37-ebc2-314d-9b3a-c104a64bdb73 | -21.59334 | -47.94532 | 2024-10-07 03:40:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b5d722a-d13c-32d0-8e12-be0965d50314 | -21.59145 | -47.95356 | 2024-10-07 03:40:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ecc34b0f-feba-33db-b714-2565c70ccbac | -21.59051 | -47.95767 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 12df703d-4afd-31fb-922e-4472c51c5084 | -21.59008 | -47.71541 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bb97bca3-7c12-37eb-9df9-5e93b1400064 | -21.58722 | -47.72823 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ab574da1-8958-381c-bd49-57511246db0f | -21.58519 | -47.94957 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6266358-ed31-3e16-bfeb-03cc1e96b06a | -21.58377 | -47.71739 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e94f1b5c-977b-3c24-85ba-b1db5ee8847f | -21.58304 | -47.93826 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 293cb722-e5b8-3042-8e5f-d5f8df2a02e0 | -21.58244 | -47.7496 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2230841d-d66c-3625-b06d-2f3131e8e603 | -21.57637 | -47.72417 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e51bafb-28b9-3dd6-b356-35f600569f22 | -21.57227 | -47.74247 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7d45dbc4-9132-337e-8609-eb3ed34698df | -21.57036 | -47.75095 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9221f02f-c97a-3713-8603-12e3c21736e9 | -21.57019 | -47.93676 | 2024-10-07 03:40:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d756c088-57a9-3f58-b6fb-df16fb743ad9 | -21.56851 | -47.75918 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a72eddb7-908e-39ed-8547-60b4c73b4d75 | -21.56671 | -47.76721 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e11766c5-e5dd-385d-bbef-b8b7bc24a221 | -21.56218 | -47.73503 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 706b95d1-253e-382b-a055-83799815508f | -21.56022 | -47.74374 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55ac91cb-c5cb-31c6-bc24-a24ada6f71c8 | -21.55946 | -47.72099 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 129c6e9e-2a1b-389a-ac75-0a7da6f1c0b5 | -21.55929 | -47.74786 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c09b23f0-7b0a-3e46-9ab8-aec34091e9fd | -21.55664 | -47.73349 | 2024-10-07 03:40:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ac2916b4-07bc-3384-bd1c-ed55f5db7c47 | -21.32176 | -47.6032 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 088089f3-754d-313c-956f-60c58c0097c5 | -21.32081 | -47.60738 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b81ce42d-e0d7-3a25-b88e-e9e0cc512ecd | -21.31152 | -47.60727 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6b1f632c-c51a-3634-ac69-01f4352b1c9a | -21.31043 | -47.61221 | 2024-10-07 03:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 60e3f2d2-47e9-3ff6-84af-832a2f1b415e | -21.28965 | -47.39166 | 2024-10-07 03:40:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f03adafd-0bef-3b74-b136-2da6e1f3b052 | -21.28872 | -47.39581 | 2024-10-07 03:40:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2c5bed4-ed94-35d2-a26a-fa56e496f557 | -21.28238 | -47.39825 | 2024-10-07 03:40:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 65e32284-50ce-312a-b979-f099704a8ed4 | -21.2779 | -47.39912 | 2024-10-07 03:40:00 | NPP-375D | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fb79c1be-0743-3b4d-b60e-edb4e33fe5c4 | -21.08353 | -47.23747 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7d9b7229-6050-3833-aa77-9c26d30fffe5 | -21.28418 | -47.39024 | 2024-10-07 03:40:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9d3ac68-6b26-3be0-8fee-33ab246c6e2f | -21.27784 | -47.39268 | 2024-10-07 03:40:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b0a46c82-57dd-3f98-9b30-975aad11380f | -21.27697 | -47.39657 | 2024-10-07 03:40:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 130a9da3-90ac-3881-9eb0-639f727505f5 | -21.27607 | -47.40055 | 2024-10-07 03:40:00 | NPP-375D | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| edff64be-814d-35ca-9f5a-5b50fe4a5b2d | -21.08504 | -47.23505 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b00331ac-fc58-369b-bfb0-cb755abe034e | -21.08463 | -47.23258 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e19b261-4333-3487-bd63-df4a7380c114 | -21.08404 | -47.23965 | 2024-10-07 03:40:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README50.md)

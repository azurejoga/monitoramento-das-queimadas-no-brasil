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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 135db8d5-b34e-3e41-8e38-f0abbb0eb3fa | -13.05358 | -51.41833 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ce64557e-f9de-3515-b082-3819ece20fef | -13.05275 | -51.32845 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f91bc0e2-7657-3dfd-9b33-becd31c7e356 | -13.05234 | -51.39302 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04d4db32-dfe9-345f-b3ee-3b131587770d | -13.05179 | -51.33318 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34ce51c4-e1ea-3224-ad01-817fcebb306e | -13.05137 | -51.39781 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 803a7e10-5f72-329b-81bf-0507f1852dd3 | -13.05083 | -51.33792 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 202257aa-54ce-32e2-aa9a-eea92d9c69f8 | -13.0504 | -51.40259 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 311b648d-f0a1-3c5f-9059-c4453fb48953 | -13.04986 | -51.34267 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fc00f2a-8a59-313f-8fda-26500f6b2373 | -13.04943 | -51.40738 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 806285fb-ffb8-39be-b7d4-f84ff9bce604 | -13.04846 | -51.41217 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c4ef0ffc-4597-3c08-b8c0-ebe09ef7f519 | -13.04236 | -51.41082 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5124fc0e-f3d0-3ebf-96eb-4d994a54efbe | -13.03676 | -51.34474 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6989d43-b479-3921-8cd4-135fd6d94cce | -13.03579 | -51.34951 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd67bf65-b1ec-37c2-8350-c38df43f60a8 | -13.00945 | -51.50967 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 45f717f7-939f-367a-84e3-1cf761ce6259 | -13.00331 | -51.50834 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 11aaa4a6-98da-3739-a52e-145140285337 | -12.96762 | -51.52591 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76a9008c-e09b-3e05-9f89-03feb6970750 | -12.96661 | -51.53076 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 057e7c32-6b13-3cf1-b3ae-27e758a7459d | -12.96561 | -51.53561 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c918895-ff44-3585-8173-df2557d984c3 | -12.96506 | -51.51355 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d781629c-bbf8-36cf-a75c-a930060f2aa9 | -12.96461 | -51.54045 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b986e825-696d-3237-a8e8-698c0de2587b | -12.96409 | -51.51844 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77251526-e98c-3145-a0f2-08840f54dd4d | -12.9635 | -51.5148 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb12c5e8-80b5-3217-917c-96fe3f1b9e3b | -12.96311 | -51.52333 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95c4d67c-3f9c-33bf-a1b6-8c551700762c | -12.96248 | -51.51969 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a06820bc-3e98-398a-9226-8304374c1ee8 | -12.96213 | -51.5282 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2640574f-7060-3551-85ba-98d1a13c74f7 | -12.96116 | -51.53306 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d092fb83-e2ab-3b90-8c80-d004b466be1c | -12.96047 | -51.52942 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3ab22b4-20ca-360c-a514-d7e07fd20893 | -12.96019 | -51.53791 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0055422c-3265-3f1b-ac27-2d9133f4b515 | -12.95946 | -51.53426 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3843b089-ca50-31ec-929c-26bc59577774 | -12.95599 | -51.52682 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b35c5da-a369-3b83-a99d-46512ef5324d | -12.95534 | -51.52319 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc3d480f-f25d-3f41-bea1-4a09488ff8b1 | -12.95502 | -51.53168 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba6b0986-e294-32d9-8952-9a1670aad81f | -12.95433 | -51.52806 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9493d327-d7b4-35bb-968a-1bbcd9de1ba5 | -12.95404 | -51.53654 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3fd93ae-979b-3e80-9fa8-f92694e39e99 | -12.94765 | -51.50449 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bf61d51-4090-33c8-87c0-1e9d70a808f9 | -12.94151 | -51.50312 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cd6ce4f-013d-36b0-a592-aa61b094c13b | -12.89455 | -51.3266 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56ada3d2-fe71-3bd8-b183-166d7fd5ba61 | -12.89419 | -51.32802 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f39c1d1e-8987-352f-970c-dbad489a6d6d | -12.88811 | -51.32667 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 425a1d46-0806-3d4b-86a9-2d5fa1661edc | -12.88748 | -51.33006 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97a88014-263e-30f8-a179-eec1a9c09625 | -12.88716 | -51.33145 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61ad0320-0b02-3cb3-87b5-5c551fbe433f | -13.14229 | -51.23386 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b05312d5-06b4-3408-8fdc-885ebe3a68ad | -13.13723 | -51.22789 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58ec12a5-eed3-3875-8183-001ea97eeff9 | -13.13628 | -51.23252 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d726ff9-deeb-3eef-8472-852c540bc1d3 | -13.13122 | -51.22657 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30603681-76f2-3c2e-ac93-afb4968aaeda | -13.13026 | -51.2312 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8b925c7-0ec7-33ae-aab8-cf58b8806cc1 | -9.9367 | -64.9179 | 2024-10-02 03:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 9713f4ac-ade4-3bad-8fba-238dec65925f | -9.9368 | -64.8991 | 2024-10-02 03:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 2667f196-defc-3c07-99b9-922aac9d73b8 | -9.9553 | -64.9172 | 2024-10-02 03:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1c98e6a7-c3ee-34ae-bce3-e74cdc69f7c1 | -11.6742 | -65.0172 | 2024-10-02 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| afbc063f-4855-3099-89b0-11b7ec501b40 | -11.6743 | -64.9983 | 2024-10-02 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 03b3c35a-6cef-32b0-b327-8011c5a87c2a | -12.6484 | -63.1214 | 2024-10-02 03:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 8b3b259d-031c-3cc1-abc0-8f9caa1307b6 | -12.8423 | -62.5526 | 2024-10-02 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 05ad16df-ec24-3bd8-955d-448def5266c6 | -12.8424 | -62.5333 | 2024-10-02 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 3222642e-103b-3b40-86ee-fcdf88cb3612 | -12.8612 | -62.5514 | 2024-10-02 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 030be3f6-558f-37ad-87da-1b4ecb3adc7b | -12.8614 | -62.5321 | 2024-10-02 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 130.8 |
| a0135edb-0b1e-3c89-bf81-9c88393d1678 | -12.8803 | -62.531 | 2024-10-02 03:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 1d51f253-01e3-3b2e-b93b-cf8b3971b146 | -13.198 | -48.6267 | 2024-10-02 03:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 12f704fe-d530-3bba-9f00-2ede544134ec | -13.2173 | -48.624 | 2024-10-02 03:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3177d30f-8cc5-3271-a1b5-20e37ea3e2f0 | -13.055 | -51.4186 | 2024-10-02 03:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| c168f8e8-b49c-30f1-b7d9-4f2acb2cd9c9 | -13.0742 | -51.4163 | 2024-10-02 03:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4604fd25-5096-3acf-8717-796b8d7663d1 | -13.1122 | -51.4329 | 2024-10-02 03:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c275667e-dfa3-39d1-9362-156fbcaad58c | -15.3708 | -55.8431 | 2024-10-02 03:56:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| f89f3b53-e9ad-3bd2-b02a-00b228c79583 | -15.3712 | -55.8226 | 2024-10-02 03:56:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 66f8f408-a9b6-30a5-b275-b7dbad6729c5 | -15.3902 | -55.8409 | 2024-10-02 03:56:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d1f43856-b15a-3e15-8630-5fb3d9462bda | -15.3906 | -55.8203 | 2024-10-02 03:56:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c2830419-9000-3be7-9f84-35ff1a3ada00 | -15.8933 | -57.1754 | 2024-10-02 03:56:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| d99411dd-45a3-36c4-a70a-bdf104e075d7 | -15.8936 | -57.155 | 2024-10-02 03:56:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| a5382ace-def9-3871-a99a-d7833b936b3b | -16.0895 | -53.5242 | 2024-10-02 03:56:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 02441343-7796-34d8-8b7b-d2c04c149c6a | -16.109 | -53.5215 | 2024-10-02 03:56:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 5bc9538d-0e52-3751-b719-10f804bf2065 | -16.1094 | -53.5004 | 2024-10-02 03:56:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3a9d3d0e-3c48-3d88-9571-0dfc5c81c700 | -16.474 | -57.3553 | 2024-10-02 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.2 |
| 408b7d1f-4c61-3371-bbc8-2b0a5f5e99e6 | -16.6912 | -57.1875 | 2024-10-02 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 31cddc94-a796-34ec-9edf-46acacc8b7b9 | -16.8292 | -55.9152 | 2024-10-02 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.0 |
| 7393eed4-892a-3eae-952a-fe00775e90c2 | -16.8295 | -55.8945 | 2024-10-02 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| f4f46fc4-58e9-358e-ad80-f4a732fb586b | -16.8695 | -55.848 | 2024-10-02 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.9 |
| fe627227-fa30-3139-aa47-23b4398c809d | -16.8698 | -55.8272 | 2024-10-02 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 33f96412-5ca1-3578-867f-b50790b9a6f6 | -16.8891 | -55.8455 | 2024-10-02 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 34a7dece-4dd0-3e80-aa47-c36bb32ca750 | -16.8894 | -55.8247 | 2024-10-02 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 4ed08e98-ecc5-321c-a4e4-7551476aef93 | -17.0695 | -56.7733 | 2024-10-02 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 3ca88db4-3a75-32d4-b177-ba737312cbac | -17.0892 | -56.7709 | 2024-10-02 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.4 |
| f4d18566-738e-3a92-90ce-5bb70572ea0c | -17.0895 | -56.7503 | 2024-10-02 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| 7b46e7a2-8993-363b-90e8-04fbd5a9e82a | -17.1088 | -56.7685 | 2024-10-02 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 4edfbb6d-2543-3e40-929c-f370eac083aa | -17.1091 | -56.7479 | 2024-10-02 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 2e4fa334-736e-3e8d-932b-dc7e3112d3f2 | -17.1288 | -56.7455 | 2024-10-02 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 7e123f61-b49f-3526-829d-dbc71180325e | -17.1971 | -56.1795 | 2024-10-02 03:56:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 42916b7d-1e95-30bf-808c-722d6cb1f26b | -20.5259 | -46.3023 | 2024-10-02 03:56:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| abcfd55a-defc-3e8b-96a0-c6bdf378c8ec | -19.97895 | -55.47675 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c364d96b-99fd-3969-b90d-26cdcb6ee359 | -19.97831 | -55.47478 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e6e48f53-2bf0-3dc0-aaf2-fa7996883df5 | -19.97756 | -55.48243 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1515ab19-90f0-3ba0-9f2a-174bbe1ea44f | -19.97691 | -55.48064 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ee284c29-98cc-38f4-a3ef-ef9fe86df0a3 | -19.96198 | -55.4875 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49b85a6b-45ec-3177-86a9-fa3ffa447f64 | -19.96 | -55.49555 | 2024-10-02 03:57:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a8ac411-d46d-370f-b4d4-f5028e77a846 | -19.74751 | -54.5213 | 2024-10-02 03:57:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99f7cf92-a625-3c75-abf7-aaf6825eb1c9 | -19.74655 | -54.52374 | 2024-10-02 03:57:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c198d16d-86ab-3a43-9f3f-a6b0fee44d8c | -19.74616 | -54.52713 | 2024-10-02 03:57:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78b2c959-6be6-37bc-8046-f2d8e2e139ce | -21.35369 | -55.69142 | 2024-10-02 03:57:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 29.0 |
| a6b56e6c-ad0c-3be8-a1d1-bd3b689c7c6f | -21.35196 | -55.69842 | 2024-10-02 03:57:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 5a0d69ba-7802-345b-ad7c-5167ce65caac | -21.34723 | -55.68887 | 2024-10-02 03:57:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 29.0 |
| abea874f-5fe4-3c54-bcb6-856ed4d80869 | -21.34555 | -55.69567 | 2024-10-02 03:57:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 21.2 |


[Clique aqui para ver as próximas entradas](README76.md)

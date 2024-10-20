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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ca154bd-16ed-34a6-897a-01d606f52f73 | -2.40868 | -50.40675 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3427b898-7d3d-3119-9e7a-3b6b51d7f381 | -2.20531 | -50.17783 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1456f06-a2be-34fd-9f07-0efc65eab8cf | -2.20411 | -50.30289 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 800d314c-d2ae-3666-9fd7-6cf092202c91 | -3.55118 | -50.31075 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| acafc7ec-0d63-3269-8b91-efee6dc274fc | -3.54756 | -50.3102 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 42f94dfc-e1b8-3845-9a44-13a26fe25374 | -3.54692 | -50.31441 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d4ddb091-323d-369f-9c5b-0696515e779c | -3.54394 | -50.30964 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d9e1178-167e-3c38-8e9c-85a95476ce31 | -3.50229 | -50.53608 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 986c280e-911a-3866-9ab6-53f902cf28a2 | -3.47811 | -50.48779 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ebd0a32-6d9b-30d3-bfdf-1de77b2075ad | -3.47747 | -50.49191 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e5b5e748-7e7c-3f58-8464-ab68b2888303 | -3.47389 | -50.49134 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd214afe-273a-386a-89e2-cf147ec470c1 | -3.46908 | -50.35554 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f4f07db-e06f-3b4b-94f1-754c3c4a28a2 | -3.46845 | -50.35968 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77996267-91c1-3a96-b371-692ead064ace | -3.45546 | -50.17711 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f23a107-8446-3f41-810d-c09626fa035c | -3.45123 | -50.32725 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a6b60a4-08ed-37a9-84a1-fee3c13c8fa1 | -3.4506 | -50.3314 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7054ace3-33b9-3da9-8815-6d085d26ba1e | -3.44089 | -50.17485 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db940708-d67c-3bf2-a01a-80d61fd37c6d | -3.43778 | -50.19337 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2c3c67e-1592-3c63-9fd7-30f90ebe4c62 | -3.43768 | -50.19619 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9458fcbf-3075-3a9f-bb52-d5ed41defbc3 | -3.43415 | -50.19279 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c900788a-3f6f-3e81-b5b9-71bac18c0f6d | -3.43404 | -50.1956 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8337bae-5420-3c3e-81f5-0eb1daf53727 | -3.4338 | -49.97782 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14acab48-233a-3074-aa42-f186feceec6f | -3.43149 | -50.21259 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b780c2c-6a4d-3491-812c-9d7b260761b7 | -3.43086 | -50.21677 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cebf573-b1ec-3fa3-bfa8-a46b694612e5 | -3.43084 | -50.21395 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27b95c52-3649-3b22-81da-178f54b955ad | -3.43079 | -49.97292 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 821df400-d9cb-381d-b3f9-1d353203c3d3 | -3.43019 | -50.21812 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14277d62-3e43-3d08-9e8c-1254b333dcdd | -3.43012 | -49.97726 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4d217e46-5b92-308b-ba28-845ff52ff658 | -3.42891 | -50.32808 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5600b02b-4673-3130-9488-578e9d691f95 | -3.4272 | -50.21341 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 095f57a2-ef18-34a0-9d5e-9a0913d9e128 | -3.42423 | -50.20861 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bf1d6a3-1b1f-308a-a347-eac9c800e4b6 | -3.4201 | -50.38624 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e99ebce3-e2f8-3dd3-8759-c152ae874fcb | -3.38825 | -50.34454 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca18b08e-d317-3975-a2d4-e72250c9528d | -3.3876 | -50.34871 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82ff9c15-9057-3df7-a146-b134ad18e7bf | -3.38464 | -50.34398 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e2e4457-e99b-3d5f-af8f-9415b7455f3a | -3.38399 | -50.34813 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06476152-c7e7-3d65-9e00-6fb5e621df41 | -3.38039 | -50.34755 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a2cba54-2b40-375a-8c2b-23cde94b9dc0 | -3.36513 | -50.30265 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da86af6a-66e1-354a-8e21-3882a703c057 | -3.36151 | -50.3021 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cf7f918-1be2-3927-b652-d6a2b2d98ecb | -3.3579 | -50.30154 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 057164f4-599e-3464-ba21-7c7ffc0c63c6 | -4.97618 | -49.86753 | 2024-10-20 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cba815c3-919a-33ba-ab04-3713487cffac | -4.88126 | -49.93006 | 2024-10-20 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b1b380a-039d-3b8f-b352-387cd9f926aa | -4.84057 | -49.91928 | 2024-10-20 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45b3ed8b-2d2a-311b-a48f-31b525b9f36c | -4.82685 | -49.95909 | 2024-10-20 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c00e875-d66f-3274-8805-40e97caba861 | -4.80909 | -50.59634 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec6de847-4832-3545-acdf-5e4b97950053 | -4.80546 | -50.59583 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5db082c4-a8db-3fc7-abf7-2559be143367 | -4.73044 | -50.37289 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d83c46f5-e8c7-3e49-a41e-aed66c8dda6e | -4.58823 | -50.67189 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f3ad528-e1d9-3c8d-a951-565893dc23e1 | -4.5876 | -50.67603 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a6eb21d-1c7e-39a3-b267-5c928d5bb33c | -4.47949 | -50.45176 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b888696c-562d-3615-b72c-d330fe60521a | -4.47882 | -50.45317 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7969d8f-6e51-3236-991c-495db3f13944 | -4.46022 | -49.62092 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f144d7ee-d337-3844-952e-f06d9fc5934c | -4.44958 | -50.15416 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 592a90c7-60cd-3f84-ba76-f841686ffecc | -4.43835 | -50.68999 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8f1ded9-cd18-3cc5-9188-3a60cd2b86f3 | -4.43818 | -50.45139 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6e5a254-5853-39a7-b176-4ac023b00a65 | -4.39818 | -49.74905 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee44caea-4101-396c-93ee-49ed9361142d | -3.96193 | -49.89536 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a221ba1-9371-3bd5-920e-edf83aa81221 | -3.9582 | -49.89485 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77fc530e-7646-3220-8bc2-201c4f8e17ba | -3.90554 | -49.75591 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 052d3c10-4fc7-36e0-8560-bd65b4cdb5dc | -3.90324 | -49.99259 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 6f16bd9f-bb40-3575-a39e-3d6f8f5676b0 | -3.90267 | -49.9861 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 68b3a3a4-0f43-3b1d-b8a8-d29449127dbe | -3.90201 | -49.9905 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 511a3140-9a48-3139-ba26-d91555781041 | -3.90022 | -49.98766 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4ec53c3d-662b-3dc1-a412-f5ac1de3b1da | -3.89953 | -49.99204 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 38432875-43b4-34e2-b6de-a923b90cb717 | -3.89896 | -49.98556 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ff0381c4-236f-3bb8-87b2-8556e293621f | -3.89831 | -49.98994 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 31d6c352-ac17-3fc8-8b84-eda26d50bc4d | -3.89765 | -49.99434 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ff3c9063-81e6-34fd-ac58-c45b8e32db8a | -3.89651 | -49.98711 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0872ba9e-fbc1-3dd7-8759-e4a4ac240cba | -3.85234 | -50.6859 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3dd6a08f-9a52-32f0-90c3-4f59bbbfd7b4 | -3.85213 | -50.07865 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fdfabe9-aa0d-393e-a3c6-3d0cd170211e | -3.84876 | -50.68537 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48f16caa-5db5-3fef-af0d-1611f6eb54ea | -3.81835 | -49.95291 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb230126-7463-3946-bd83-0675627a5af3 | -3.76525 | -49.98679 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25462237-547c-30bb-a1f7-c507ffe681e4 | -3.69178 | -50.19643 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a732fe26-825d-30a8-bb29-b9d83574835b | -3.68878 | -50.19161 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b14ab03-41d6-3ac7-890a-a8afacc1a20d | -3.68813 | -50.19587 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b21f4eb-1d90-31df-b2b2-ca6d07037a31 | -3.67514 | -49.7943 | 2024-10-20 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b400396-4e5c-3a91-ad10-de6b023b3c66 | -3.60702 | -50.58414 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5e4f2ced-20e6-3356-ae93-e9c966c1bf0a | -3.6064 | -50.58824 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5ff32d2e-4119-3178-8171-1db77e01d95e | -3.60407 | -50.5795 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83dcb278-35ac-3ca4-a03b-afe055126e63 | -3.60345 | -50.58361 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 50ced274-b59e-3be3-89a8-ddb5b97e6faf | -3.60282 | -50.58772 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a738345-ced5-3c22-8b42-3e0ef8d684f6 | -3.60221 | -50.5918 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3623bcd9-930a-3e76-b95a-8f4347cecf6f | -3.59986 | -50.58311 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 400c882e-e614-3a3f-b854-31628e743925 | -3.59863 | -50.59129 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96a393b4-8c60-3659-ae13-f05fc4138782 | -3.59615 | -50.59214 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6772ac7-bef1-32e9-ae59-5f11a00b892d | -3.59505 | -50.59077 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afdfaa52-81e4-3873-a110-66c38c0ef8db | -5.0153 | -50.83742 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a98ce8bb-11b3-30a7-994a-47872d119439 | -5.01467 | -50.84153 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 655c7500-d801-349b-8630-98c9b44103d9 | -5.01171 | -50.83686 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4934fbef-9aa7-3d04-b7f1-d4e24b93c2b7 | -5.01109 | -50.84098 | 2024-10-20 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a0f6ed6-7ddc-3b87-b91b-348ddc6283eb | -6.51153 | -50.25598 | 2024-10-20 04:55:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 966883bb-9f59-3a06-8193-8050b6dd6d10 | -6.21873 | -50.88877 | 2024-10-20 04:55:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d051431a-d1d2-34e0-a6aa-ed725d0af9d6 | -6.21511 | -50.88819 | 2024-10-20 04:55:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50525ed5-612c-3e64-b49e-03f91a9150e1 | -6.19163 | -50.87165 | 2024-10-20 04:55:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 731b46ef-f8d8-3fa5-824e-dd43cb08bc52 | -6.18374 | -50.87477 | 2024-10-20 04:55:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d254efa1-5752-374e-a282-bedccba4d24f | -6.17948 | -50.87843 | 2024-10-20 04:55:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 698a5d9a-5976-32fe-88ac-658286eda4f4 | -5.89006 | -51.0562 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de519566-e72a-379b-b9c7-cc14fbfcc2d5 | -5.86125 | -51.07697 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78a54ba2-97be-3268-85e2-087b9b6c10b0 | -5.86063 | -51.08106 | 2024-10-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README47.md)

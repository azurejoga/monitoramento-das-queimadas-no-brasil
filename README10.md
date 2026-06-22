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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56ad8432-6abc-366c-b4bb-499f1a12ad72 | -11.0432 | -52.4622 | 2026-06-22 13:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 384.8 |
| e76670a8-97f6-3085-9e0d-357c2099af7b | -14.0907 | -59.4768 | 2026-06-22 13:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 64c70c99-7759-3307-adcb-55abd8b5f89e | -13.522 | -52.1676 | 2026-06-22 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| cb9eb218-c3db-357b-b72d-dbcdd88c0f6d | -10.7145 | -50.1723 | 2026-06-22 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d8422272-09e1-311e-aeb6-a08e3daabc06 | -11.0432 | -52.4622 | 2026-06-22 13:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 403.4 |
| 6d2f55a4-4d63-31db-ab21-a0c8f2e0183c | -11.0619 | -52.4812 | 2026-06-22 13:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 187.6 |
| fb0a8f0b-2a6e-3f27-9209-c710e36bf4ab | -13.522 | -52.1676 | 2026-06-22 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 937bc78c-b47e-3324-b979-80a43f9b6fe7 | -14.0718 | -59.4585 | 2026-06-22 13:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| d16e9e92-a16d-33e3-bac5-b2b170562e8f | -10.7335 | -50.1703 | 2026-06-22 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| fa60d922-7e9e-32c1-9b6d-960432aa3c19 | -11.043 | -52.4831 | 2026-06-22 13:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 173.7 |
| 8c21349e-beeb-30f0-a96c-bfb5e74a6f37 | -10.7145 | -50.1723 | 2026-06-22 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3f0869ec-3f68-3f7c-b19f-434729493214 | -11.0622 | -52.4603 | 2026-06-22 13:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 417.6 |
| 3fc1c9bc-2127-36d3-af42-7d248c583e88 | -14.0907 | -59.4768 | 2026-06-22 13:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| fae2df95-38e6-35d1-8715-9db9f90960b0 | -14.0718 | -59.4585 | 2026-06-22 13:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| cac6adf7-0e15-39f4-a9fb-b121c3ac43d9 | -11.0432 | -52.4622 | 2026-06-22 13:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 470.3 |
| c4e31281-52fe-32b0-9f07-24fbb8d20e67 | -10.7335 | -50.1703 | 2026-06-22 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 33501964-0610-30fd-beca-087a0e9741b0 | -11.0622 | -52.4603 | 2026-06-22 13:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 380.3 |
| bd4a60e7-642a-342f-8913-f38c8bacff2c | -14.0907 | -59.4768 | 2026-06-22 13:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| f0a8a749-68cf-3871-8b5a-4ff074048c05 | -11.043 | -52.4831 | 2026-06-22 13:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 194.7 |
| 32472d9c-e184-3765-a135-d61b41a93f60 | -10.7145 | -50.1723 | 2026-06-22 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| ad76d440-bad7-36ff-8102-adeeb2b38a76 | -10.7145 | -50.1723 | 2026-06-22 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 236.3 |
| af1b9d65-5b36-3c69-8703-5ab7f840398f | -13.522 | -52.1676 | 2026-06-22 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| c706ef68-b9a1-3891-819d-be960e88ff53 | -18.5134 | -51.5783 | 2026-06-22 14:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 90b998e3-c0eb-3fc5-b797-b1ccccd17aa9 | -14.0907 | -59.4768 | 2026-06-22 14:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 06ccf08e-4af5-3182-ad24-e4b4f91f24f3 | -8.8697 | -46.9437 | 2026-06-22 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 72b16564-d8ac-3585-acce-775384ea0740 | -10.7335 | -50.1703 | 2026-06-22 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| a7011948-9cca-32fe-bc02-ac73cdfab06b | -11.0622 | -52.4603 | 2026-06-22 14:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 366.4 |
| 6d9e0d08-0250-3661-b142-8f85961cc56b | -10.7335 | -50.1703 | 2026-06-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 47bdc0c2-8783-31ac-9491-9fbf7a82958f | -11.043 | -52.4831 | 2026-06-22 14:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 0dec4043-5d4b-33a4-8076-9853e62f56bd | -11.0432 | -52.4622 | 2026-06-22 14:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 374.1 |
| 3299eb89-3e9b-3846-ab03-c9793264f03a | -14.0907 | -59.4768 | 2026-06-22 14:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| ad2e20bc-355c-301f-865b-4392de789218 | -10.7145 | -50.1723 | 2026-06-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 41445d80-637d-3a9a-95cd-85fcbea3f04e | -13.522 | -52.1676 | 2026-06-22 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 140.0 |
| bb905a89-5967-392f-b130-e3a8bae27672 | -14.0907 | -59.4768 | 2026-06-22 14:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 063672bf-babe-3fed-8c9a-0877250a7033 | -10.5426 | -46.3516 | 2026-06-22 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 64d87966-686e-3999-95fb-ac5a6580113d | -18.5134 | -51.5783 | 2026-06-22 14:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 237.3 |
| 8a2a2ee0-1d45-33b2-b4ec-01a34a7b75d1 | -18.4934 | -51.5818 | 2026-06-22 14:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| daa1862f-b58b-362e-b4bc-6d0fecf0b259 | -10.5617 | -46.3492 | 2026-06-22 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 4fef46aa-357b-3af3-8a7a-c1ab35fa889e | -10.7335 | -50.1703 | 2026-06-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f436fdc3-0da2-3553-86e2-037adac13196 | -10.7145 | -50.1723 | 2026-06-22 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 192.9 |
| 9ff98bdf-bc91-3ffc-8c15-8fc3273bfde2 | -14.0907 | -59.4768 | 2026-06-22 14:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 20221725-a062-3ef6-a433-75a69aeb6def | -14.091 | -59.4569 | 2026-06-22 14:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| c95c9c8e-4fd9-33a1-9b5b-9d2f6de6969e | -10.7145 | -50.1723 | 2026-06-22 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 898cf37b-844d-30dc-9037-63a545f518c4 | -14.0907 | -59.4768 | 2026-06-22 14:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d58f2f29-892b-360c-8740-c47efb9d0074 | -10.7145 | -50.1723 | 2026-06-22 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 195.8 |
| c3bcf57e-39e9-3ca8-8350-c5c8fa0961ed | -10.7335 | -50.1703 | 2026-06-22 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4759e915-41a2-3a50-97f6-72e124b61b0b | -11.043 | -52.4831 | 2026-06-22 14:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 45be3a56-9da9-336a-920c-dd4c9a0f1e11 | -11.0432 | -52.4622 | 2026-06-22 14:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 375.7 |
| bc066bd3-1618-3dfe-8010-5a47cd8dfa98 | -18.5134 | -51.5783 | 2026-06-22 14:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 36bffbc2-5ce1-35cf-9875-e04fcf7ceeb2 | -11.0622 | -52.4603 | 2026-06-22 14:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 301.0 |
| 57085d83-1e0e-3f16-a559-278480b3a097 | -10.6408 | -47.391 | 2026-06-22 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f2d83ca5-7f65-3240-b802-d708d46c9a73 | -10.6598 | -47.3887 | 2026-06-22 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 9ee623db-1158-3252-85ee-88475544bf9d | -12.8741 | -44.3593 | 2026-06-22 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1699.4 |
| 979931c2-0b8d-3102-81e8-adc46df6fd69 | -14.0907 | -59.4768 | 2026-06-22 14:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4e208fce-5ea1-355c-b41d-bced2fbe945f | -11.0432 | -52.4622 | 2026-06-22 14:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 266.4 |
| a6afa575-8da6-3f5f-8ce5-e09430f7baf3 | -10.7145 | -50.1723 | 2026-06-22 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| a7cfcbcc-038b-382b-9c05-09a403704c81 | -6.2311 | -48.5224 | 2026-06-22 14:50:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2a9e47d1-de8a-3720-8d4a-89619fbe198c | -12.8736 | -44.3828 | 2026-06-22 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 376.8 |
| ba978e58-99c0-3ae7-8deb-302da083aeae | -12.8543 | -44.386 | 2026-06-22 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 117f0f30-4588-3e3a-b714-12f68583c01f | -11.043 | -52.4831 | 2026-06-22 14:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| b65df5d8-6f20-3433-962e-8649568b6162 | -10.7145 | -50.1723 | 2026-06-22 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 2aa9173a-a6c2-3a49-936c-29ee5b0e0cb6 | -11.0432 | -52.4622 | 2026-06-22 15:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 252.9 |
| 4ae9f036-06c1-34bc-bff4-d277b1506fe2 | -11.043 | -52.4831 | 2026-06-22 15:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 48581d0e-33c3-3ff8-853b-6ffe5391332b | -10.7145 | -50.1723 | 2026-06-22 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 60803648-83e5-33ef-a366-595167c95b81 | -12.8741 | -44.3593 | 2026-06-22 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1444.7 |
| 99953b6e-8c5e-35e2-aa83-c90db6813b85 | -11.0622 | -52.4603 | 2026-06-22 15:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 321.0 |
| 3aaa2783-21c5-3b3d-a6b9-f5fe584ae40b | -12.8736 | -44.3828 | 2026-06-22 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 343.0 |
| 5f85c1fb-d7fd-3d7c-ac76-0b5820425f6b | -11.043 | -52.4831 | 2026-06-22 15:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 17869a6e-af68-331a-aef4-9758d68e3fe3 | -12.8543 | -44.386 | 2026-06-22 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 5a8ba874-e884-3a38-8c09-c3146d93f35d | -18.5134 | -51.5783 | 2026-06-22 15:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 01c5a0f1-d408-3218-bd01-56c0affd3db4 | -11.0432 | -52.4622 | 2026-06-22 15:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 217.2 |
| 5be83a59-e05a-350d-a005-2b4ada43bbaf | -10.7145 | -50.1723 | 2026-06-22 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| b4dedff7-be2d-3336-ba69-3f2df96dbc2a | -12.8354 | -44.3657 | 2026-06-22 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 26f4e1aa-4871-33c7-a547-3149b7202440 | -14.0907 | -59.4768 | 2026-06-22 15:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3cddfe55-d28f-3792-be85-2d3d49aad2db | -10.7145 | -50.1723 | 2026-06-22 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| ecb0194e-ed84-3fa2-a25f-e5de9ebde6fa | -18.5134 | -51.5783 | 2026-06-22 15:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 4dee1938-ff38-3a8b-bd36-c57746085a19 | -11.043 | -52.4831 | 2026-06-22 15:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| ccfc292a-8acc-3aef-b232-8c4d91d671dd | -11.0432 | -52.4622 | 2026-06-22 15:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 272.0 |
| 023e799a-0bc5-3b87-bf8f-735a53babca7 | -10.7145 | -50.1723 | 2026-06-22 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 64ae18c3-ef2f-3d5c-9816-8d02037d938e | -18.5134 | -51.5783 | 2026-06-22 15:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d16042d7-06a8-310f-b600-138bb1a1de96 | -11.043 | -52.4831 | 2026-06-22 15:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| a13d5a08-38b9-3e09-98a7-890d2ae15568 | -11.0559 | -50.1353 | 2026-06-22 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 256f466d-7d4b-343c-9d1a-e06860e45010 | -18.4934 | -51.5818 | 2026-06-22 15:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5ea7cbed-269a-3706-b2e4-e0cd6256b87b | -12.8741 | -44.3593 | 2026-06-22 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1451.6 |
| 2b9a9313-9f1e-3473-a1d5-0fbc1890a8d8 | -8.8697 | -46.9437 | 2026-06-22 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 1c7815be-da92-37cd-9e43-a7277993c491 | -12.8543 | -44.386 | 2026-06-22 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 312.3 |
| 08bba254-d546-3100-ad9b-2c9aa37942c3 | -12.8736 | -44.3828 | 2026-06-22 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 479.3 |
| 2eee87d7-cc9c-36c2-84b2-654c34668555 | -10.7145 | -50.1723 | 2026-06-22 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6f0e908f-f34d-34e6-bad7-45f6bb2caaca | -11.043 | -52.4831 | 2026-06-22 15:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 0e28c32a-8785-3500-bdeb-8fc9c0de4974 | -12.8354 | -44.3657 | 2026-06-22 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 490ad6ba-695c-38ed-b9fc-5d08c0821c10 | -18.5134 | -51.5783 | 2026-06-22 15:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3020762e-b0f7-3f5d-aea9-6afabe349101 | -11.0432 | -52.4622 | 2026-06-22 15:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 233.2 |
| 657bf4c5-9361-3dae-a59b-a0369e9c51bc | -11.043 | -52.4831 | 2026-06-22 16:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| de10bd94-4460-304c-8b92-06c26c7c7048 | -11.0432 | -52.4622 | 2026-06-22 16:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 235.4 |
| 83c1d549-c5c6-33ad-a064-be288b0c0f90 | -10.7145 | -50.1723 | 2026-06-22 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| fc9dcd13-fa01-3637-934a-7d27e8c5f525 | -18.5134 | -51.5783 | 2026-06-22 16:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 31b9ee0b-a712-32f1-b5a1-172a0aee9214 | -18.5134 | -51.5783 | 2026-06-22 16:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b616f325-fb4f-39a0-98ee-9b167e752385 | -12.8354 | -44.3657 | 2026-06-22 16:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 142446cd-ba6e-3382-9643-d44d1aa46fb7 | -12.8741 | -44.3593 | 2026-06-22 16:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1450.6 |
| 48707bd5-7f77-3eef-b9a0-315fd081658d | -12.8543 | -44.386 | 2026-06-22 16:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 322.1 |


[Clique aqui para ver as próximas entradas](README11.md)

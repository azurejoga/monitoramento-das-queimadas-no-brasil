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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 475fe10d-8cff-3064-81c2-defb5a8a1051 | -16.60939 | -49.5155 | 2025-07-06 12:12:00 | TERRA_M-T | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ef693b6-0110-3eaa-a37b-630e7ac3fccd | -22.34548 | -47.26641 | 2025-07-06 12:12:00 | TERRA_M-T | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 77bf70d0-77ec-3885-8b25-c137c0cd93ec | -16.43378 | -43.72892 | 2025-07-06 12:12:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 75bc87d8-bc30-391b-8a76-2c51c65ed702 | -5.6065 | -45.1852 | 2025-07-06 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| bb700e31-5404-3ca3-bd81-15e5bbd6f0d5 | -5.6065 | -45.1852 | 2025-07-06 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 2a0174f8-53b5-303f-b85c-6943c02e50e8 | -5.6065 | -45.1852 | 2025-07-06 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 935a9371-52ed-37fb-938f-4b0f356aae68 | -5.6065 | -45.1852 | 2025-07-06 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| e2a9c1c2-a88e-3ae0-bc56-6bd7358821b8 | -5.6065 | -45.1852 | 2025-07-06 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 414982db-7c07-314d-900a-2bf9c6ac836c | -5.6065 | -45.1852 | 2025-07-06 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f8d61993-bee6-3fd8-857d-21d9625f8b58 | -5.5878 | -45.1865 | 2025-07-06 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 84ad44ba-1fa2-3cc8-9a3a-152507c88738 | -6.9296 | -45.7607 | 2025-07-06 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 173.1 |
| cf36cc96-9e4b-346e-887b-42faffae36fc | -6.9296 | -45.7607 | 2025-07-06 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 040ea4ec-7ffc-3634-8eff-151f718b7ad4 | -5.5878 | -45.1865 | 2025-07-06 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ec9d502c-7974-3927-abca-a89c70a16e01 | -5.6065 | -45.1852 | 2025-07-06 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 3bd1aa4e-2f51-321e-99de-affb5d732e32 | -5.6065 | -45.1852 | 2025-07-06 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 34c6ea36-7f65-32d6-b667-573ed5dce785 | -8.0979 | -45.4053 | 2025-07-06 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5dce9159-40e3-35ba-894e-4f025fdc3538 | -6.2934 | -45.7216 | 2025-07-06 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| b69d1a49-50f0-30e8-8542-c39dd59c5564 | -5.5878 | -45.1865 | 2025-07-06 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 32064ad2-9aac-3b0d-b67f-54b37dce67ad | -10.6483 | -44.4861 | 2025-07-06 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 09df4892-d0f8-3e6a-acbe-fa891263516f | -5.5878 | -45.1865 | 2025-07-06 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 681fe70a-e908-3d07-bf53-c3057cb3cf6b | -5.6063 | -45.2078 | 2025-07-06 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f9ad5a05-db71-3030-98ef-7357b5a05ea2 | -5.6065 | -45.1852 | 2025-07-06 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 5526374a-9bba-359e-80c6-d790c4a7d50f | -8.0979 | -45.4053 | 2025-07-06 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 6d4b8e30-ce4b-3bf5-8adf-75e46215ca30 | -6.2934 | -45.7216 | 2025-07-06 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 6dde4924-aecc-3271-8bb8-eb5e911fd809 | -5.6063 | -45.2078 | 2025-07-06 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| bc2d87bc-02d3-39a5-a17a-40c1b4716eb3 | -5.5878 | -45.1865 | 2025-07-06 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 178.0 |
| a5b37dda-954e-379f-b97f-ef12cee69b3b | -8.0979 | -45.4053 | 2025-07-06 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e20eb974-df25-379e-a321-4a4f11458417 | -5.6065 | -45.1852 | 2025-07-06 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 75e10dd9-4f58-343d-b7e5-866a21d8cfb2 | -12.0266 | -57.0845 | 2025-07-06 13:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 7c9eec4f-c46f-3544-91ce-bd95f15e6fae | -5.6063 | -45.2078 | 2025-07-06 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e3335a84-da9a-359a-88c9-e4705f06e8b5 | -5.6065 | -45.1852 | 2025-07-06 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 875fe5e9-6dcb-3dcd-bddc-e313cb0f37ff | -5.5878 | -45.1865 | 2025-07-06 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 98fd346c-cfc6-350f-9d1e-a11e5e4a7e58 | -5.6067 | -45.1625 | 2025-07-06 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1afc5b19-ea51-34e7-a5d7-d070b7877acd | -6.6755 | -43.143 | 2025-07-06 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 058aa168-4869-3f9d-9398-221532768866 | -6.6943 | -43.1413 | 2025-07-06 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8ee06c13-4232-3715-baf9-b3ea49456fea | -8.0982 | -45.3826 | 2025-07-06 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| da52d7f7-f640-32b7-8df6-2657b93d496b | -8.0979 | -45.4053 | 2025-07-06 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5c186ee7-59ba-3a32-807a-4204ab413067 | -6.6752 | -43.1665 | 2025-07-06 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 71.1 |
| a8301240-7fb2-30e2-acea-3508debb0d53 | -12.0266 | -57.0845 | 2025-07-06 14:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f4152d63-4e48-3301-9143-c96184a9ea6f | -5.6065 | -45.1852 | 2025-07-06 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 265623a4-7edf-363c-853b-dc6777f74055 | -6.6755 | -43.143 | 2025-07-06 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ca08b0c4-3b4e-3b28-9b3c-3eb301cefebb | -5.5878 | -45.1865 | 2025-07-06 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 7990d25b-7265-375c-ae12-f8d3b7b59685 | -5.5876 | -45.2091 | 2025-07-06 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f3069bd9-4c16-3adc-a654-65fd6648581d | -8.0979 | -45.4053 | 2025-07-06 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c5c1541c-8cb5-3424-a36e-a95da48df642 | -12.0266 | -57.0845 | 2025-07-06 14:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 6ccad87c-f172-36fa-af9a-82a3efef5c5a | -6.6943 | -43.1413 | 2025-07-06 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a1f773a1-4dc1-31e5-ac4d-41433a42f672 | -6.2934 | -45.7216 | 2025-07-06 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 30413aeb-7783-3c73-b000-541781e685e7 | -5.6063 | -45.2078 | 2025-07-06 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |


